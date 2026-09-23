"""Health, identity, and direct assessment (used by the MCP server and the portal's quick check)."""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from app.api.deps import ContainerDep, IdentityDep
from app.domain.verdicts import Verdict

router = APIRouter()


@router.get("/healthz", tags=["health"])
async def healthz() -> dict:
    return {"status": "ok"}


@router.get("/readyz", tags=["health"])
async def readyz(c: ContainerDep) -> dict:
    try:
        await c.ready()
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"database unavailable: {e}") from e
    return {"status": "ready"}


@router.get("/api/v1/me", tags=["auth"])
async def me(identity: IdentityDep, c: ContainerDep) -> dict:
    return {
        "user_id": identity.user_id,
        "role": identity.role,
        "kind": identity.kind,
        "adk_web": c.settings.enable_adk_web,
        "auth_mode": c.settings.auth_mode,
    }


class AssessRequest(BaseModel):
    proposal: str = Field(min_length=5, max_length=20_000)
    context: str = Field(default="", max_length=40_000)


@router.post("/api/v1/assess", response_model=Verdict, tags=["assess"])
async def assess(body: AssessRequest, identity: IdentityDep, c: ContainerDep) -> Verdict:
    return await c.assessment.assess(body.proposal, context=body.context, user_id=identity.user_id)


@router.get("/api/v1/assessments", tags=["assess"])
async def assessments(
    identity: IdentityDep, c: ContainerDep, all: bool = False, limit: int = 50
) -> list[dict]:
    user = None if (all and identity.is_admin) else identity.user_id
    return await c.assessments.list(user_id=user, limit=min(limit, 500))
