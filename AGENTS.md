# AGENTS.md (repo root)

Instructions for AI coding agents (and humans) working in this repo. Each project has its own `AGENTS.md` with project-specific notes; this file covers repo-wide rules.

## What this repo is

Tutorial projects for applied AI, numbered by track. Code must stay **minimal but structurally complete**: every project is independently deployable (Dockerfile, k8s manifests, pyproject/package.json, tests, CI).

## Layout rules

- Top-level project dirs: `<track>.<name>-<variant>/` (e.g. `1.chatbot-nextjs`, `2.angular-full`). See `docs/CONVENTIONS.md`.
- Inside a project: `backend/`, `frontend/`, `deploy/`, `docs/`, `README.md`, `AGENTS.md`. Extra deployables sit alongside (e.g. `mcp-server/`), and cloud infrastructure goes in `infra/terraform/`.
- Deploy target: Kubernetes manifests (projects 1-3) or Terraform + Cloud Run (project 4). Either way, every deployable has a Dockerfile and is built in CI.
- `backend/` and `frontend/` are separate deployables. Never import across them. They talk over HTTP only.
- CI lives at repo root `.github/workflows/<project>.yml`, path-filtered to that project.

## Coding rules

- Python 3.11+, `pyproject.toml` with `uv`. Ruff for lint/format. Pytest for tests.
- Config via environment variables through `app/config.py` (`pydantic-settings`). Never read `os.environ` elsewhere.
- Backend structure: `app/api` (HTTP), `app/services` (use cases), `app/agent(s)` (ADK/Claude definitions), `app/tools`, `app/rag`, `app/db`, `app/mcp`. Keep HTTP out of services and agents.
- Frontend calls the backend through one `api` module/service. Base URL from env (`NEXT_PUBLIC_API_URL` / Angular `environment.ts`).
- Illustration-only components (in-memory vector store, hashing embedder, mock MCP server) are marked with `# ILLUSTRATION:` and have a `# PRODUCTION:` note or a dummy production class next to them. Keep that pattern when adding new ones.
- Tests must not need an API key. Mock the agent service at the FastAPI dependency boundary. Real-model evals are opt-in (`-m eval`).

## Commit rules

- One project per commit when scaffolding. Conventional commit prefix: `feat(1.chatbot-nextjs): ...`.
- Don't commit `.env`, `node_modules`, `.venv`, `*.db`, or `dist/`.

## Verifying a change

```bash
# backend
cd <project>/backend && uv sync && uv run ruff check . && uv run pytest
# frontend (Next)
cd <project>/frontend && npm ci && npm run lint && npm run build
# frontend (Angular)
cd <project>/frontend && npm ci && npm run build
```
