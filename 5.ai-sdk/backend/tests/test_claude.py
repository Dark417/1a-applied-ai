"""Claude adapter: Agent SDK wiring (CLI replaced by a fake) and the real Messages API tool runner."""

import uuid

import pytest
from fastapi.testclient import TestClient

from app.adapters.claude.adapter import ClaudeAdapter
from app.adapters.claude.agent_sdk import make_can_use_tool, make_hooks, provider_env
from app.adapters.claude.tools import as_sdk_tool
from app.main import create_app
from app.providers import build_profiles
from app.tools import calculator
from tests.fakes.claude import (
    CliScript,
    api_message,
    api_text,
    api_tool_use,
    messages_client,
    result,
    text,
    tool_result,
    tool_use,
)


@pytest.fixture
def cl(container):
    def make(script: CliScript | None = None, messages=None) -> TestClient:
        script = script or CliScript()
        container.registry.register(
            ClaudeAdapter(
                container.settings,
                client_cls=lambda options: script.client_cls(options),
                query_fn=script.query_fn,
                messages_client=messages or (lambda p: None),
            )
        )
        return TestClient(create_app(container))

    return make


def run(client, pattern, message="", provider="raw", ok=True, **kw):
    body = {
        "framework": "claude",
        "pattern": pattern,
        "provider": provider,
        "message": message,
        **kw,
    }
    r = client.post("/v1/runs", json=body)
    assert r.status_code == 200, r.text
    data = r.json()
    if ok:
        assert not [e for e in data["events"] if e["type"] == "error"], data["events"]
    return data


def of(data, type_):
    return [e for e in data["events"] if e["type"] == type_]


def test_agent_sdk_options_events_and_session_resume(cl):
    script = CliScript(
        [
            tool_use("t1", "mcp__tools__calculator", expression="0.17*2340"),
            tool_result("t1", {"status": "ok", "result": 397.8}),
            text("17% of 2340 is 397.8."),
            result("17% of 2340 is 397.8.", session_id="cli-1"),
        ],
        [
            text("You asked about 17% of 2340."),
            result("You asked about 17% of 2340.", session_id="cli-1"),
        ],
    )
    client = cl(script)
    data = run(client, "agent_sdk", "What is 17% of 2340?")
    assert [e["name"] for e in of(data, "tool_call")] == ["calculator"]  # mcp__tools__ stripped
    assert of(data, "tool_result")[0]["result"]["result"] == 397.8
    assert data["output"] == "17% of 2340 is 397.8."
    assert data["events"][-1]["data"]["cost_usd"] == 0.001

    opts = script.options[0]
    assert set(opts.mcp_servers) == {"tools"} and opts.mcp_servers["tools"]["type"] == "sdk"
    assert "mcp__tools__calculator" in opts.allowed_tools
    assert "mcp__tools__run_cli" not in opts.allowed_tools  # sensitive -> can_use_tool decides
    assert opts.tools == [] and opts.can_use_tool is not None
    assert set(opts.hooks) == {"UserPromptSubmit", "PreToolUse", "PostToolUse"}
    assert opts.env["ANTHROPIC_API_KEY"] == "test-key" and opts.session_id == str(
        uuid.UUID(data["session_id"])
    )

    run(client, "agent_sdk", "What did I ask?", session_id=data["session_id"])
    assert script.options[1].resume == "cli-1" and script.options[1].session_id is None


def test_subagents_options_and_attribution(cl):
    script = CliScript(
        [
            tool_use("task1", "Task", subagent_type="calculator", prompt="17% of 2340"),
            tool_use("c1", "mcp__tools__calculator", parent="task1", expression="0.17*2340"),
            tool_result("c1", {"result": 397.8}, parent="task1"),
            text("397.8", parent="task1"),
            tool_result("task1", "397.8"),
            text("It is 397.8."),
            result("It is 397.8."),
        ]
    )
    data = run(cl(script), "subagents", "What is 17% of 2340?")
    assert [e["agent"] for e in of(data, "agent")] == ["main", "calculator", "main"]
    assert [e["name"] for e in of(data, "tool_call")] == ["Task", "calculator"]
    opts = script.options[0]
    assert set(opts.agents) == {"researcher", "calculator"}
    assert opts.agents["calculator"].tools == ["mcp__tools__calculator"]
    assert opts.tools == ["Task"] and opts.permission_mode == "dontAsk"


def test_external_mcp_servers(cl, container):
    container.settings.playwright_mcp_enabled = True
    script = CliScript([text("Ticket created."), result("Ticket created.")])
    run(cl(script), "external_mcp", "File a ticket")
    opts = script.options[0]
    assert set(opts.mcp_servers) == {"workbench", "playwright"}
    assert opts.mcp_servers["workbench"]["type"] == "stdio"
    assert opts.mcp_servers["playwright"]["command"] == "npx"
    assert set(opts.allowed_tools) == {"mcp__workbench__*", "mcp__playwright__*"}


def test_cli_error_result_becomes_error_event(cl):
    script = CliScript([result("boom", is_error=True)])
    data = run(cl(script), "subagents", "x", ok=False)
    assert data["events"][-1]["type"] == "error"


@pytest.mark.parametrize(
    ("provider", "expected"),
    [
        ("raw", {"ANTHROPIC_API_KEY": "test-key"}),
        ("bedrock", {"CLAUDE_CODE_USE_BEDROCK": "1", "AWS_REGION": "us-east-1"}),
        (
            "vertex",
            {
                "CLAUDE_CODE_USE_VERTEX": "1",
                "CLOUD_ML_REGION": "global",
                "ANTHROPIC_VERTEX_PROJECT_ID": "test-project",
            },
        ),
    ],
)
def test_provider_is_env(settings, provider, expected):
    assert provider_env(build_profiles(settings)[provider]) == expected


async def test_hooks_and_permissions():
    hooks = make_hooks({"browse"})
    policy = hooks["PreToolUse"][0].hooks[0]
    denied = await policy({"tool_name": "mcp__tools__browse"}, "t1", None)
    assert denied["hookSpecificOutput"]["permissionDecision"] == "deny"
    assert await policy({"tool_name": "mcp__tools__calculator"}, "t2", None) == {}
    ctx = await hooks["UserPromptSubmit"][0].hooks[0]({}, None, None)
    assert "Current UTC time" in ctx["hookSpecificOutput"]["additionalContext"]

    can_use = make_can_use_tool({"approve_sensitive": False})
    assert type(await can_use("mcp__tools__run_cli", {}, None)).__name__ == "PermissionResultDeny"
    assert (
        type(await make_can_use_tool({})("mcp__tools__run_cli", {}, None)).__name__
        == "PermissionResultAllow"
    )


async def test_sdk_tool_runs_neutral_function(scope):
    out = await as_sdk_tool(calculator).handler({"expression": "2+3"})
    assert out["content"][0]["text"] == '{"status": "ok", "expression": "2+3", "result": 5}'


def test_messages_api_tool_runner_mcp_and_history(cl):
    factory, captured = messages_client(
        api_message(api_tool_use("tu1", "calculator", expression="0.17*2340"), stop="tool_use"),
        api_message(
            api_tool_use("tu2", "create_ticket", title="Try tool runner", body="x"), stop="tool_use"
        ),
        api_message(api_text("397.8, ticket filed.")),
        api_message(api_text("You asked for 17% of 2340.")),
    )
    client = cl(messages=factory)
    data = run(client, "messages_api", "What is 17% of 2340? File a ticket.")
    results = {e["name"]: e["result"] for e in of(data, "tool_result")}
    assert results["calculator"]["result"] == 397.8  # our function, run by the SDK's runner
    assert "Try tool runner" in str(results["create_ticket"])  # MCP via async_mcp_tool
    assert data["output"] == "397.8, ticket filed."
    assert {t["name"] for t in captured[0]["tools"]} >= {
        "calculator",
        "search_docs",
        "create_ticket",
    }
    assert captured[0]["model"] == "claude-opus-5"

    run(
        client,
        "messages_api",
        "What did I ask?",
        session_id=data["session_id"],
        options={"mcp": False},
    )
    history = captured[-1]["messages"]
    assert history[0]["content"] == "What is 17% of 2340? File a ticket."  # we own the history
    assert [m["role"] for m in history] == [
        "user",
        "assistant",
        "user",
        "assistant",
        "user",
        "assistant",
        "user",
    ]


def test_messages_api_client_per_provider(settings):
    from app.adapters.claude.messages_api import default_client, model_for

    p = build_profiles(settings)
    assert type(default_client(p["raw"])).__name__ == "AsyncAnthropic"
    assert type(default_client(p["bedrock"])).__name__ == "AsyncAnthropicBedrockMantle"
    assert model_for(p["bedrock"]) == "anthropic.claude-opus-5"
    assert type(default_client(p["vertex"])).__name__ == "AsyncAnthropicVertex"
