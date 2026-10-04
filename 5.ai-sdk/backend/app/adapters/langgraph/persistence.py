"""LangGraph persistence per provider branch.

Checkpointer (short-term: full graph state per thread_id, after every step)
  raw / vertex  AsyncSqliteSaver                 PRODUCTION (vertex): Postgres saver on Cloud SQL,
                                                 or host the graph on Agent Engine (LanggraphAgent)
  bedrock       AgentCoreMemorySaver             checkpoints stored as AgentCore Memory events
Store (long-term: across threads)
  raw / vertex  InMemoryStore                    ILLUSTRATION: process memory
  bedrock       AgentCoreMemoryStore             put() writes messages as events; search() reads
                                                 facts AgentCore *extracted* from them
"""

import asyncio
import re
import uuid
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from langchain_core.messages import BaseMessage
from langgraph.checkpoint.base import BaseCheckpointSaver
from langgraph.store.base import BaseStore
from langgraph.store.memory import InMemoryStore

from app.config import Settings

_in_memory_store = InMemoryStore()


@asynccontextmanager
async def checkpointer(provider: str, s: Settings) -> AsyncIterator[BaseCheckpointSaver]:
    if provider == "bedrock" and s.agentcore_memory_id:
        from langgraph_checkpoint_aws import AgentCoreMemorySaver

        yield AgentCoreMemorySaver(s.agentcore_memory_id, region_name=s.aws_region)
        return
    from langgraph.checkpoint.sqlite.aio import AsyncSqliteSaver

    async with AsyncSqliteSaver.from_conn_string(str(s.data_path / "langgraph.db")) as saver:
        yield saver


def store(provider: str, s: Settings) -> BaseStore:
    if provider == "bedrock" and s.agentcore_memory_id:
        from langgraph_checkpoint_aws import AgentCoreMemoryStore

        return AgentCoreMemoryStore(memory_id=s.agentcore_memory_id, region_name=s.aws_region)
    return _in_memory_store


def _is_agentcore(st: BaseStore) -> bool:
    return type(st).__name__ == "AgentCoreMemoryStore"


async def save_message(st: BaseStore, user_id: str, thread_id: str, message: BaseMessage) -> None:
    """Long-term write. AgentCore wants namespace (actor_id, session_id) and a BaseMessage."""
    await asyncio.to_thread(st.put, (user_id, thread_id), uuid.uuid4().hex, {"message": message})


async def search_memories(st: BaseStore, user_id: str, query: str, limit: int = 5) -> list[str]:
    """Long-term read: AgentCore's extracted facts, or (locally) this user's past messages."""
    if _is_agentcore(st):
        items = await asyncio.to_thread(st.search, ("facts", user_id), query=query, limit=limit)
        return [str(i.value.get("content", i.value)) for i in items]
    items = await asyncio.to_thread(st.search, (user_id,), limit=50)
    words = {w for w in re.findall(r"[a-z0-9]+", query.lower()) if len(w) > 3}
    texts = [str(i.value["message"].content) for i in items if "message" in i.value]
    hits = [t for t in texts if words & set(re.findall(r"[a-z0-9]+", t.lower()))]
    return hits[-limit:]
