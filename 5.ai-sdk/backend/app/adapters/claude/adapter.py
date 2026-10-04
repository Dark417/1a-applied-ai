"""Claude adapter: the Agent SDK (three patterns) and the Messages API tool runner (one)."""

from collections.abc import AsyncIterator, Callable
from typing import Any

from claude_agent_sdk import ClaudeSDKClient, query

from app.adapters.claude.agent_sdk import OPTION_BUILDERS, SdkTranslator
from app.adapters.claude.messages_api import ClientFactory, default_client, run_messages_api
from app.config import Settings
from app.core.adapter import PatternInfo, RunContext
from app.schemas import Event

PATTERNS = [
    PatternInfo(
        "agent_sdk",
        "Claude Code's agent loop with our tools in-process, hooks, and a permission callback.",
        (
            "ClaudeSDKClient",
            "create_sdk_mcp_server + @tool",
            "HookMatcher: UserPromptSubmit / PreToolUse / PostToolUse",
            "can_use_tool",
            "allowed_tools",
            "session_id / resume",
            "env-selected provider",
        ),
    ),
    PatternInfo(
        "subagents",
        "The main agent delegates to researcher and calculator subagents via the Task tool.",
        (
            "query()",
            "AgentDefinition",
            "Task tool",
            "per-subagent tool scoping",
            "forward_subagent_text",
        ),
    ),
    PatternInfo(
        "external_mcp",
        "Our workbench MCP server (and Playwright MCP if enabled) attached as stdio servers.",
        (
            "mcp_servers (stdio)",
            "mcp__<server>__<tool> naming",
            "wildcard allowed_tools",
            "@playwright/mcp",
        ),
    ),
    PatternInfo(
        "messages_api",
        "The bare Messages API tool loop; we own history. Provider = client class.",
        (
            "client.beta.messages.tool_runner",
            "@beta_async_tool",
            "async_mcp_tool",
            "AsyncAnthropic / AsyncAnthropicBedrockMantle / AsyncAnthropicVertex",
        ),
    ),
]


class ClaudeAdapter:
    name = "claude"
    description = "Claude Agent SDK (Claude Code loop) and the Claude Messages API tool runner."

    def __init__(
        self,
        settings: Settings,
        *,
        client_cls: Callable[..., Any] = ClaudeSDKClient,
        query_fn: Callable[..., Any] = query,
        messages_client: ClientFactory = default_client,
    ):
        self.settings = settings
        self.client_cls = client_cls
        self.query_fn = query_fn
        self.messages_client = messages_client

    def patterns(self) -> list[PatternInfo]:
        return PATTERNS

    def providers(self) -> list[str]:
        return ["raw", "bedrock", "vertex"]

    async def run(self, ctx: RunContext) -> AsyncIterator[Event]:
        pattern = ctx.request.pattern
        if pattern == "messages_api":
            async for event in run_messages_api(ctx, self.messages_client):
                yield event
            return
        options = OPTION_BUILDERS[pattern](ctx, self.settings)
        translate = SdkTranslator()
        if pattern == "agent_sdk":
            # ClaudeSDKClient: a live, bidirectional session (needed for can_use_tool, interrupts,
            # follow-ups on the same connection).
            async with self.client_cls(options=options) as client:
                await client.query(ctx.request.message)
                async for msg in client.receive_response():
                    for event in translate(msg):
                        yield event
        else:
            async for msg in self.query_fn(prompt=ctx.request.message, options=options):
                for event in translate(msg):
                    yield event
        result = translate.result
        if result is None:
            yield Event(type="error", message="the Claude CLI ended without a result")
            return
        ctx.session.native["claude_session_id"] = result.session_id
        if result.is_error:
            yield Event(
                type="error", message=f"claude: {result.subtype}: {result.result or result.errors}"
            )
            return
        yield Event(
            type="done",
            output=result.result,
            data={
                "usage": result.usage,
                "cost_usd": result.total_cost_usd,
                "turns": result.num_turns,
            },
        )


def build(settings: Settings) -> ClaudeAdapter:
    return ClaudeAdapter(settings)
