# Conventions

Derived from the project brief. Applies to every project in this repo.

## Naming

- Project directory: `<track>.<name>-<variant>`
  - `track` is a learning step number. Two projects in the same track are the same lesson with a different variant.
  - `name` is the thing built. `variant` is the distinguishing choice (frontend framework, agent runtime).
  - Examples: `1.chatbot-nextjs`, `1.chatbot-angular`, `2.angular-full`, `3.claude-sdk-full`.
- Container images: `<project>-backend`, `<project>-frontend` (e.g. `chatbot-nextjs-backend`).
- Kubernetes: one namespace per project (`chatbot-nextjs`), resources named `backend` / `frontend`.
- Python package inside a backend is always `app`. Entry point is always `app.main:app`.
- Env vars: `UPPER_SNAKE`, read only in `app/config.py`.

## Directory layout (per project)

```
<project>/
  README.md            quickstart + what you'll learn
  AGENTS.md            project-specific rules for AI agents
  docs/
    DESIGN.md          one-page design doc: problem, non-goals, approach, tradeoffs
    DEPLOY.md          how to build images, run compose, apply k8s, wire CI/CD
  backend/             FastAPI + agent runtime (independently deployable)
    pyproject.toml
    Dockerfile
    .env.example
    app/
      main.py          app factory
      config.py        settings
      schemas.py       request/response models
      api/             routers only, no business logic
      services/        use cases; wrap the agent runtime
      agent/ agents/   agent definitions (ADK / Claude SDK)
      tools/           function tools
      rag/             embedder + vector store + ingest (project 2+)
      db/              sqlite schema, seed, repository (project 2+)
      mcp/             MCP server + client config (project 2+)
    evals/             eval sets + config (project 2+)
    tests/
  frontend/            Next.js or Angular (independently deployable)
    Dockerfile
  deploy/
    docker-compose.yaml
    k8s/               namespace, configmap, secret example, deployments, services, ingress
```

## Illustration vs production

The brief: for MCP, RAG, and vector DBs, use illustration-purpose implementations, but write dummy code showing the production replacement.

Pattern used everywhere:

```python
class Embedder(Protocol): ...

class HashingEmbedder:            # ILLUSTRATION: deterministic, no network, no deps
    ...

class GeminiEmbedder:             # PRODUCTION: dummy body, shows the real call
    def embed(self, texts):
        # from google import genai
        # client.models.embed_content(model="gemini-embedding-001", contents=texts)
        raise NotImplementedError("wire up in production")
```

Selection is by env var (`EMBEDDER=hashing|gemini`, `VECTOR_STORE=memory|chroma`), resolved once in a `factory` function. Swapping a component means adding a class and one branch in the factory, nothing else.

## Build order (MVP ladder)

Every project is built as vertical slices:

- `MVP0`: one HTTP endpoint → one agent → one model call → one UI textbox. Deployable.
- `MVP1+`: add one demoable capability at a time (tools, RAG, MCP, streaming, evals).

Each project's `docs/DESIGN.md` lists its ladder.
