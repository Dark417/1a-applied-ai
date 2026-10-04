"""Google ADK adapter: Runner + App + plugin + provider-specific session and memory services."""

from collections.abc import AsyncIterator

from google.adk.agents.run_config import RunConfig, StreamingMode
from google.adk.apps import App
from google.adk.runners import Runner
from google.genai import types

from app.adapters.adk.callbacks import AuditPlugin
from app.adapters.adk.models import ModelFactory, default_model_factory
from app.adapters.adk.patterns import PATTERNS, AdkKit
from app.adapters.adk.services import memory_service, session_service
from app.adapters.adk.translate import TranslateState, translate
from app.config import Settings
from app.core.adapter import PatternInfo, RunContext
from app.schemas import Event

# One ADK app name for every pattern, so long-term memory (keyed by app + user) is shared.
APP_NAME = "ai_sdk"


class AdkAdapter:
    name = "adk"
    description = (
        "Google Agent Development Kit: workflow agents, graph Workflow, services, callbacks."
    )

    def __init__(self, settings: Settings, model_factory: ModelFactory | None = None):
        self.settings = settings
        self.model_factory = model_factory or default_model_factory

    def patterns(self) -> list[PatternInfo]:
        return [p.info for p in PATTERNS.values()]

    def providers(self) -> list[str]:
        return ["raw", "bedrock", "vertex"]

    async def run(self, ctx: RunContext) -> AsyncIterator[Event]:
        req, profile = ctx.request, ctx.provider
        pattern = PATTERNS[req.pattern]
        kit = AdkKit(
            profile=profile,
            settings=self.settings,
            options=req.options,
            model_for=lambda role: self.model_factory(profile, req.vendor, role),
        )
        sessions = session_service(profile.name, self.settings)
        memory = memory_service(profile.name, self.settings, profile.memory)
        plugin = AuditPlugin()
        try:
            root = pattern.build(kit)
            runner = Runner(
                app=App(name=APP_NAME, root_agent=root, plugins=[plugin]),
                session_service=sessions,
                memory_service=memory,
            )
            session_id = await self._ensure_session(sessions, ctx)
            st = TranslateState()
            async for adk_event in runner.run_async(
                user_id=req.user_id,
                session_id=session_id,
                new_message=types.Content(role="user", parts=[types.Part(text=req.message)]),
                run_config=RunConfig(
                    streaming_mode=StreamingMode.SSE, max_llm_calls=self.settings.max_llm_calls
                ),
            ):
                for event in translate(adk_event, st):
                    yield event

            session = await sessions.get_session(
                app_name=APP_NAME, user_id=req.user_id, session_id=session_id
            )
            # Long-term memory: hand the finished conversation to the memory service
            # (Memory Bank / AgentCore extract facts from it; InMemory indexes it).
            await memory.add_session_to_memory(session)
            output = st.last_text
            if pattern.output_key and session.state.get(pattern.output_key):
                output = session.state[pattern.output_key]
            elif st.workflow_output is not None:
                output = st.workflow_output
            usage = next(iter(plugin.usage.values()), None)
            yield Event(type="done", output=output, data={"usage": usage} if usage else None)
        finally:
            for toolset in kit.toolsets:
                await toolset.close()

    async def _ensure_session(self, sessions, ctx: RunContext) -> str:
        """Our session id -> ADK session id. Agent Engine assigns its own ids, so we map."""
        rec, user_id = ctx.session, ctx.request.user_id
        sid = rec.native.get("adk_session_id")
        if sid and await sessions.get_session(app_name=APP_NAME, user_id=user_id, session_id=sid):
            return sid
        requested = (
            None if ctx.provider.name == "vertex" and self.settings.agent_engine_id else rec.id
        )
        session = await sessions.create_session(
            app_name=APP_NAME, user_id=user_id, session_id=requested
        )
        rec.native["adk_session_id"] = session.id
        return session.id


def build(settings: Settings) -> AdkAdapter:
    return AdkAdapter(settings)
