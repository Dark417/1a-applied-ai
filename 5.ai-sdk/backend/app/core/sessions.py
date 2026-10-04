"""SessionRegistry: our session id -> bound target, native ids, and a run lock.

The lock is the pattern from 0.learn/fastapi-bedrock-asyncSessionMemory.py: one agent loop per
session at a time; a concurrent request gets 409 instead of interleaving two loops on one history.

Conversation *content* is not stored here. It lives in each framework's own store (ADK session
service, LangGraph checkpointer, Strands session manager, Claude CLI session). See
docs/design/04-tools-mcp-rag-state.md, "State: three layers".
"""

from __future__ import annotations

import asyncio
import time
import uuid
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from dataclasses import dataclass, field
from typing import Any

from app.schemas import RunRequest


class SessionBusy(RuntimeError):
    pass


class SessionMismatch(ValueError):
    pass


@dataclass
class SessionRecord:
    id: str
    user_id: str
    framework: str
    pattern: str
    provider: str
    created_at: float = field(default_factory=time.time)
    turns: int = 0
    last_output: Any = None
    # Framework-native ids or state handles, e.g. {"claude_session_id": "..."} or
    # {"pending_interrupt": {...}} for LangGraph hitl.
    native: dict[str, Any] = field(default_factory=dict)

    def summary(self) -> dict[str, Any]:
        return {
            "session_id": self.id,
            "user_id": self.user_id,
            "target": f"{self.framework}:{self.pattern}:{self.provider}",
            "turns": self.turns,
            "created_at": self.created_at,
            "native": {k: v for k, v in self.native.items() if isinstance(v, str | int | bool)},
        }


class SessionRegistry:
    # ILLUSTRATION: process memory. Correct for one replica only.
    # PRODUCTION: records in DynamoDB / Firestore / Postgres; the lock as Redis
    # `SET lock:{id} {owner} NX PX 300000` (or a DynamoDB conditional write) with a lease, so a
    # crashed replica cannot hold a session forever.
    def __init__(self) -> None:
        self._records: dict[str, SessionRecord] = {}
        self._locks: dict[str, asyncio.Lock] = {}

    def get(self, session_id: str) -> SessionRecord | None:
        return self._records.get(session_id)

    def list(self, user_id: str | None = None) -> list[SessionRecord]:
        return [r for r in self._records.values() if user_id is None or r.user_id == user_id]

    def check(self, req: RunRequest) -> None:
        """Cheap pre-flight check so HTTP can answer 409 before a stream starts."""
        if not req.session_id:
            return
        rec = self._records.get(req.session_id)
        if rec is None:
            return
        target = (req.framework, req.pattern, req.provider)
        if (rec.framework, rec.pattern, rec.provider) != target:
            raise SessionMismatch(
                f"session {rec.id} is bound to {rec.framework}:{rec.pattern}:{rec.provider}; "
                "start a new session for a different target"
            )
        if rec.user_id != req.user_id:
            raise SessionMismatch(f"session {rec.id} belongs to another user")
        if self._locks[rec.id].locked():
            raise SessionBusy(f"session {rec.id} is processing a prior request")

    @asynccontextmanager
    async def acquire(self, req: RunRequest) -> AsyncIterator[SessionRecord]:
        self.check(req)
        sid = req.session_id or uuid.uuid4().hex
        rec = self._records.get(sid)
        if rec is None:
            rec = SessionRecord(
                id=sid,
                user_id=req.user_id,
                framework=req.framework,
                pattern=req.pattern,
                provider=req.provider,
            )
            self._records[sid] = rec
            self._locks[sid] = asyncio.Lock()
        lock = self._locks[sid]
        if lock.locked():  # lost a race after check()
            raise SessionBusy(f"session {sid} is processing a prior request")
        async with lock:
            yield rec
