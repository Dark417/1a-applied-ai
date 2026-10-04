"""LangGraph adapter: compile the pattern's graph with a provider-specific checkpointer and store,
stream updates (including subgraphs), and handle interrupt/resume."""

from collections.abc import AsyncIterator

from langgraph.types import Command

from app.adapters.langgraph.models import ChatModelFactory, default_chat_model
from app.adapters.langgraph.patterns import PATTERNS, LgKit, UserContext
from app.adapters.langgraph.persistence import checkpointer, store
from app.adapters.langgraph.translate import TranslateState, final_output, translate
from app.config import Settings
from app.core.adapter import AdapterError, PatternInfo, RunContext
from app.mcp.clients import server_specs
from app.schemas import Event


async def load_mcp_tools(settings: Settings) -> list:
    """MCP servers -> LangChain tools via langchain-mcp-adapters (a session per tool call)."""
    from langchain_mcp_adapters.client import MultiServerMCPClient

    client = MultiServerMCPClient(
        {
            spec.name: {
                "transport": "stdio",
                "command": spec.command,
                "args": spec.args,
                "env": spec.env,
                "cwd": spec.cwd,
            }
            for spec in server_specs(settings)
        }
    )
    return await client.get_tools()


class LangGraphAdapter:
    name = "langgraph"
    description = (
        "LangGraph graphs and LangChain v1 agents: state, reducers, checkpointers, interrupts."
    )

    def __init__(self, settings: Settings, model_factory: ChatModelFactory | None = None):
        self.settings = settings
        self.model_factory = model_factory or default_chat_model

    def patterns(self) -> list[PatternInfo]:
        return [p.info for p in PATTERNS.values()]

    def providers(self) -> list[str]:
        return ["raw", "bedrock", "vertex"]

    async def run(self, ctx: RunContext) -> AsyncIterator[Event]:
        req, profile, rec = ctx.request, ctx.provider, ctx.session
        pattern = PATTERNS[req.pattern]
        if req.resume is not None and not rec.native.get("pending_interrupt"):
            raise AdapterError("nothing to resume: this session is not paused")
        mcp_tools = (
            await load_mcp_tools(self.settings)
            if pattern.uses_mcp and req.options.get("mcp", True)
            else []
        )
        config = {
            # thread_id = our session id; actor_id is what AgentCoreMemorySaver keys on.
            "configurable": {"thread_id": rec.id, "user_id": req.user_id, "actor_id": req.user_id},
            "recursion_limit": 2 * self.settings.max_llm_calls + 5,
        }
        async with checkpointer(profile.name, self.settings) as saver:
            kit = LgKit(
                profile=profile,
                settings=self.settings,
                options=req.options,
                model_for=lambda role: self.model_factory(profile, req.vendor, role),
                checkpointer=saver,
                store=store(profile.name, self.settings),
                mcp_tools=mcp_tools,
            )
            graph = pattern.build(kit)
            graph_input = (
                Command(resume=req.resume)
                if req.resume is not None
                else pattern.to_input(req.message)
            )
            st = TranslateState()
            interrupted = False
            async for namespace, chunk in graph.astream(
                graph_input,
                config,
                stream_mode="updates",
                subgraphs=True,
                context=UserContext(user_id=req.user_id),
            ):
                for event in translate(namespace, chunk, st):
                    interrupted = interrupted or event.type == "interrupt"
                    yield event
            rec.native["pending_interrupt"] = interrupted
            if interrupted:
                return  # the run is paused; the client resumes with {"resume": {...}}
            snapshot = await graph.aget_state(config)
            yield Event(type="done", output=final_output(snapshot.values))


def build(settings: Settings) -> LangGraphAdapter:
    return LangGraphAdapter(settings)
