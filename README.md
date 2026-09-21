# 1a-applied-ai

Tutorial projects for applied AI. Primary stack: **Google ADK** (Agent Development Kit) agents behind **FastAPI**, with **Next.js** or **Angular** frontends. Project 3 swaps the agent runtime for the **Claude Agent SDK**.

Each project is a self-contained monorepo slice: independently deployable `backend/` and `frontend/`, with `deploy/` (Docker Compose + Kubernetes), `docs/` (design + deploy), and its own `AGENTS.md`.

## Projects

| Dir | What it shows | Agent runtime | Frontend |
|---|---|---|---|
| [`1.chatbot-nextjs/`](./1.chatbot-nextjs) | Minimum multi-turn chatbot. Wholesome structure, minimal code. | Google ADK | Next.js |
| [`1.chatbot-angular/`](./1.chatbot-angular) | Same backend as above, Angular frontend. | Google ADK | Angular |
| [`2.angular-full/`](./2.angular-full) | Project 1 + MCP, local RAG, local tools, SQLite tools, orchestrator + loop, evals, streaming. | Google ADK | Angular |
| [`3.claude-sdk-full/`](./3.claude-sdk-full) | Project 2 with the agent runtime replaced by the Claude Agent SDK. | Claude Agent SDK | Angular |

Read them in order. Each project's `README.md` has a quickstart, and `docs/DESIGN.md` explains the *why*.

## Conventions

See [`docs/CONVENTIONS.md`](./docs/CONVENTIONS.md) for naming, directory layout, and the "illustration vs production" swap pattern used for MCP, RAG, and vector stores.

## Quick start (any project)

```bash
cd 1.chatbot-nextjs
cp backend/.env.example backend/.env      # put your GOOGLE_API_KEY in
docker compose -f deploy/docker-compose.yaml up --build
# frontend: http://localhost:3000   backend: http://localhost:8000/docs
```

## CI

`.github/workflows/` has one workflow per project, path-filtered so a change in one project only runs that project's checks. Deploy jobs are stubs: fill in your registry and cluster (see each project's `docs/DEPLOY.md`).

## References

1. [google/adk-python](https://github.com/google/adk-python) and [google/adk-samples](https://github.com/google/adk-samples)
2. [ADK docs](https://google.github.io/adk-docs/)
3. [Claude Agent SDK (Python)](https://github.com/anthropics/claude-agent-sdk-python)
4. [FastAPI docs](https://fastapi.tiangolo.com/)
