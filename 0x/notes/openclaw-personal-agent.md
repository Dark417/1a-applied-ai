# OpenClaw & 个人 Agent

- [← 返回总目录](../x-note.md)
- OpenClaw 生态、常驻个人助理、一人公司
- 共 6 篇，按收藏顺序倒序（最新在上）

## Part 1 · Index

- [OpenClaw + Codex/Claude Code Agent Swarm：一人开发团队](#x-2025920521871716562) · @elvissun · 2026-02-23 · 搭建教程（长文）
- [OpenClaw 编排文章的要点总结](#x-2026224275192193465) · @AYi_AInotes · 2026-02-24 · 文章解读
- [ClawWork：给 agent 加经济激励](#x-2023308910883664070) · @blackanger · 2026-02-16 · 观点 / 项目发现
- [OpenClaw Mac 桌面版发布](#x-2022346776679006516) · @aigclink · 2026-02-13 · 版本发布
- [爆肝 2 天，开发 OpenClaw 接入微信 bot，已开源](#x-2022356917948166506) · @canghe · 2026-02-13 · 项目分享
- [OpenClaw agent Larry 一周拿下百万 TikTok 播放](#x-2022011925903667547) · @oliverhenry · 2026-02-12 · 案例 + 搭建教程

## Part 2 · Details

### x-2025920521871716562

**OpenClaw + Codex/Claude Code Agent Swarm：一人开发团队**

- 作者：Elvis (@elvissun) · 发帖 2026-02-23 · [原帖](https://x.com/elvissun/status/2025920521871716562)
- 来源：🔖 收藏 · 拉取 2026-10-27 · 类型：搭建教程（长文）
- **总结**：作者不再直接用 Codex 或 Claude Code，而是让 OpenClaw 上的编排器 Zoe 持有全部业务上下文，再派生专用的 coding agent。8 步流程：客户需求经 Zoe 界定范围 → 用 git worktree + tmux 派生 agent → 循环监控 tmux、PR 和 CI → agent 提 PR → 多模型 review → Telegram 通知 → 合并。实测日均约 50 个 commit，单日最高 94 个。核心论点：一个上下文装不下代码和业务两类信息，所以要两层架构。

**正文**

- **I don't use Codex or Claude Code directly anymore**
  - **OpenClaw is my orchestration layer**
  - My orchestrator, **Zoe**:
    - Spawns the agents
    - Writes their prompts
    - Picks the right model for each task
    - Monitors progress
    - Pings me on Telegram when PRs are ready to merge
- **Proof points from the last 4 weeks**
  - **94 commits in one day** — most productive day; had 3 client calls and never opened the editor
    - Average is around 50 commits a day
  - **7 PRs in 30 minutes** — idea to production is fast because coding and validation are mostly automated
  - **Commits → MRR**: used on a real B2B SaaS, bundled with founder-led sales to deliver most feature requests same-day
    - Speed converts leads into paying customers
  - Before Jan: CC/Codex only | After Jan: OpenClaw orchestrates CC/Codex
  - Git history looks like I hired a dev team
    - Reality: I went from managing Claude Code to managing an OpenClaw agent that manages a fleet of Claude Code and Codex agents
  - **Success rate**: one-shots almost all small-to-medium tasks without intervention
  - **Cost**: ~$100/month for Claude + $90/month for Codex — but you can start with $20
- **Why this beats using Codex or Claude Code directly**
  - **Codex and Claude Code have very little context about your business**
    - They see code, not the full picture
  - **OpenClaw is the orchestration layer between you and all agents**
    - Holds all business context in my Obsidian vault: customer data, meeting notes, past decisions, what worked, what failed
    - Translates historical context into precise prompts for each coding agent
  - The agents stay focused on code; the orchestrator stays at the strategy level
- **Same idea as Stripe's "Minions"**
  - Stripe recently wrote about its background agent system: parallel coding agents backed by a centralized orchestration layer
  - I accidentally built the same thing — but it runs locally on my Mac mini
- **Why one AI can't do both**
  - **Context windows are zero-sum** — you choose what goes in
    - Fill it with code → no room for business context
    - Fill it with customer history → no room for the codebase
  - Hence the **two-tier system**: each AI is loaded with exactly what it needs
  - OpenClaw and Codex have drastically different context
  - **Specialization through context, not through different models**
- **The full 8-step workflow** (real example from last week)
- **Step 1: Customer request → scoping with Zoe**
  - Call with an agency customer: they wanted to reuse configurations already set up across their team
  - Talked the request through with Zoe afterward
    - Meeting notes sync automatically to my Obsidian vault → zero explanation needed
  - Scoped it together → a **template system** to save and edit existing configurations
  - Zoe then does three things:
    - **Tops up credits** to unblock the customer immediately — she has admin API access
    - **Pulls the customer's config from the prod database** — she has read-only prod DB access (the Codex agents never will); the existing setup goes into the prompt
    - **Spawns a Codex agent** with a detailed prompt containing all the context
- **Step 2: Spawn the agent**
  - Each agent gets its **own worktree (isolated branch) and tmux session**
    ```bash
    # Create worktree + spawn agent
    git worktree add ../feat-custom-templates -b feat/custom-templates origin/main
    cd ../feat-custom-templates && pnpm install

    tmux new-session -d -s "codex-templates" \
      -c "/Users/elvis/Documents/GitHub/medialyst-worktrees/feat-custom-templates" \
      "$HOME/.codex-agent/run-agent.sh templates gpt-5.3-codex high"
    ```
  - The agent runs in tmux with full terminal logging via a script
  - How agents are launched:
    ```bash
    # Codex
    codex --model gpt-5.3-codex \
      -c "model_reasoning_effort=high" \
      --dangerously-bypass-approvals-and-sandbox \
      "Your prompt here"

    # Claude Code  
    claude --model claude-opus-4.5 \
      --dangerously-skip-permissions \
      -p "Your prompt here"
    ```
  - **Switched from `codex exec` / `claude -p` to tmux**
    - tmux is far better because **mid-task redirection** is powerful
    - Agent going the wrong direction? Don't kill it — redirect it:
    ```bash
    # Wrong approach:
    tmux send-keys -t codex-templates "Stop. Focus on the API layer first, not the UI." Enter

    # Needs more context:
    tmux send-keys -t codex-templates "The schema is in src/types/template.ts. Use that." Enter
    ```
  - The task is tracked in `.clawdbot/active-tasks.json`:
    ```json
    {
      "id": "feat-custom-templates",
      "tmuxSession": "codex-templates",
      "agent": "codex",
      "description": "Custom email templates for agency customer",
      "repo": "medialyst",
      "worktree": "feat-custom-templates",
      "branch": "feat/custom-templates",
      "startedAt": 1740268800000,
      "status": "running",
      "notifyOnComplete": true
    }
    ```
  - On completion it updates with the PR number and checks (see Step 5):
    ```json
    {
      "status": "done",
      "pr": 341,
      "completedAt": 1740275400000,
      "checks": {
        "prCreated": true,
        "ciPassed": true,
        "claudeReviewPassed": true,
        "geminiReviewPassed": true
      },
      "note": "All checks passed. Ready to merge."
    }
    ```
- **Step 3: Monitoring in a loop**
  - A **cron job runs every 10 minutes** to babysit all agents — essentially an improved Ralph Loop (see below)
  - It doesn't poll the agents directly (too expensive) — it runs a script that reads the JSON registry:
    ```bash
    .clawdbot/check-agents.sh
    ```
  - The script is **100% deterministic and extremely token-efficient**:
    - Checks whether tmux sessions are alive
    - Checks for open PRs on tracked branches
    - Checks CI status via `gh` CLI
    - Auto-respawns failed agents (max 3 attempts) on CI failure or critical review feedback
    - Only alerts when something needs human attention
  - I'm not watching terminals — the system tells me when to look
- **Step 4: Agent creates PR**
  - The agent commits, pushes, and opens a PR via `gh pr create --fill`
  - I do NOT get notified yet — **a PR alone isn't done**
  - **Definition of done** (very important your agent knows this):
    - PR created
    - Branch synced to main (no merge conflicts)
    - CI passing (lint, types, unit tests, E2E)
    - Codex review passed
    - Claude Code review passed
    - Gemini review passed
    - Screenshots included (if UI changes)
- **Step 5: Automated code review** — every PR is reviewed by three models; they catch different things
  - **Codex Reviewer** — exceptional at edge cases
    - The most thorough review
    - Catches logic errors, missing error handling, race conditions
    - Very low false positive rate
  - **Gemini Code Assist Reviewer** — free and incredibly useful
    - Catches security and scalability issues other agents miss
    - Suggests specific fixes
    - No-brainer to install
  - **Claude Code Reviewer** — mostly useless; tends to be overly cautious
    - Lots of "consider adding..." suggestions that are usually overengineering
    - I skip everything unless marked critical
    - Rarely finds critical issues on its own, but validates what the others flag
  - All three post comments directly on the PR
- **Step 6: Automated testing** — CI runs a heavy test suite:
  - Lint and TypeScript checks
  - Unit tests
  - E2E tests
  - Playwright tests against a preview environment (identical to prod)
  - **New rule: if the PR changes any UI, it must include a screenshot in the PR description, or CI fails**
    - Dramatically shortens review — I see exactly what changed without clicking through the preview
- **Step 7: Human review**
  - Telegram notification: "PR #341 ready for review."
  - By this point:
    - CI passed
    - Three AI reviewers approved
    - Screenshots show the UI changes
    - All edge cases are documented in review comments
  - **My review takes 5–10 minutes**; many PRs I merge without reading the code — the screenshot shows everything
- **Step 8: Merge**
  - PR merges
  - A daily cron job cleans up orphaned worktrees and the task registry JSON
- **The Ralph Loop V2**
  - **The original Ralph Loop**: pull context from memory → generate output → evaluate results → save learnings
    - Most implementations run the **same prompt every cycle**
    - Distilled learnings improve future retrievals, but the prompt stays static
  - **This system is different**: when an agent fails, Zoe doesn't respawn it with the same prompt
    - She looks at the failure with full business context and figures out how to unblock it:
      - Ran out of context? → "Focus only on these three files."
      - Went the wrong direction? → "Stop. The customer wanted X, not Y. Here's what they said in the meeting."
      - Needs clarification? → "Here's customer's email and what their company does."
    - She has context the agents don't: customer history, meeting notes, what we tried before, why it failed
    - She uses it to write better prompts on each retry
  - **Zoe finds work proactively** instead of waiting for assignments:
    - **Morning**: scans Sentry → finds 4 new errors → spawns 4 agents to investigate and fix
    - **After meetings**: scans meeting notes → flags 3 feature requests customers mentioned → spawns 3 Codex agents
    - **Evening**: scans git log → spawns Claude Code to update the changelog and customer docs
  - Example: take a walk after a customer call → come back to "7 PRs ready for review. 3 features, 4 bug fixes."
  - **Successful patterns get logged**, e.g.:
    - "This prompt structure works for billing features."
    - "Codex needs the type definitions upfront."
    - "Always include the test file paths."
  - **Reward signals**: CI passing, all three code reviews passing, human merge
    - Any failure triggers the loop
    - Over time Zoe writes better prompts because she remembers what shipped
- **Choosing the right agent**
  - **Codex — the workhorse** (~90% of tasks)
    - Backend logic, complex bugs, multi-file refactors, anything needing reasoning across the codebase
    - Slower but thorough
  - **Claude Code — faster, better at frontend**
    - Fewer permission issues → great for git operations
    - Used to be the daily driver, but Codex 5.3 is now simply better and faster
  - **Gemini — design sensibility**
    - For beautiful UIs: Gemini generates an HTML/CSS spec first → Claude Code implements it in the component system
    - "Gemini designs, Claude builds"
  - **Zoe routes each task**:
    - Billing system bug → Codex
    - Button style fix → Claude Code
    - New dashboard design → starts with Gemini
- **How to set this up**
  - Copy this entire article into OpenClaw and tell it: "Implement this agent swarm setup for my codebase."
  - It reads the architecture, creates the scripts, sets up the directory structure, and configures cron monitoring
  - Done in about 10 minutes
- **The bottleneck nobody expects: RAM**
  - Each agent needs its own worktree → each worktree needs its own `node_modules`
  - Each agent runs builds, type checks, tests
  - Five agents at once = five TypeScript compilers, five test runners, five sets of dependencies in memory
  - **Mac Mini with 16GB tops out at 4–5 agents** before swapping — and only if they don't build at the same time
  - Bought a **Mac Studio M4 Max with 128GB RAM ($3,500)** for this; arriving end of March, will report if it's worth it
- **Up next: the one-person million-dollar company**
  - Expect many one-person million-dollar companies starting in 2026
    - Massive leverage for those who can build recursively self-improving agents
  - The shape: **an AI orchestrator as an extension of yourself** (what Zoe is to me), delegating to specialized agents per business function
    - Engineering, customer support, ops, marketing
    - Each agent focused on what it's good at; you keep focus and full control
  - The next generation won't hire 10 people to do what one person with the right system can do
    - Stay small, move fast, ship daily
  - Pushback on hype: lots of AI slop, "mission control" demos with no real-world benefit
    - Goal here is the opposite: document building an actual business — real customers, revenue, commits to production, and real losses
  - **What I'm building: Agentic PR**
    - A one-person company taking on enterprise PR incumbents
    - Agents that help startups get press coverage without a $10k/month retainer

<details><summary>原文</summary>

> 《OpenClaw + Codex/ClaudeCode Agent Swarm: The One-Person Dev Team [Full Setup]》
>
> I don't use Codex or Claude Code directly anymore.
> I use OpenClaw as my orchestration layer. My orchestrator, Zoe, spawns the agents, writes their prompts, picks the right model for each task, monitors progress, and pings me on Telegram when PRs are ready to merge.
> Proof points from the last 4 weeks:
> - 94 commits in one day. My most productive day - I had 3 client calls and didn't open my editor once. The average is around 50 commits a day. 
> - 7 PRs in 30 minutes. Idea to production are blazing fast because coding and validations are mostly automated.
> - Commits → MRR: I use this for a real B2B SaaS I'm building — bundling it with founder-led sales to deliver most feature requests same-day. Speed converts leads into paying customers.
> before Jan: CC/codex only | after Jan: Openclaw orchestrates CC/codex
> My git history looks like I just hired a dev team. In reality it's just me going from managing claude code, to managing an openclaw agent that manages a fleet of other claude code and codex agents.
> Success rate: The system one-shots almost all small to medium tasks without any intervention.
> Cost: ~$100/month for Claude and $90/month for Codex, but you can start with $20.
> Here's why this works better than using Codex or Claude Code directly:
> >Codex and Claude Code have very little context about your business.
> They see code. They don't see the full picture of your business.
> OpenClaw changes the equation. It acts as the orchestration layer between you and all agents — it holds all my business context (customer data, meeting notes, past decisions, what worked, what failed) inside my Obsidian vault, and translates historical context into precise prompts for each coding agent. The agents stay focused on code. The orchestrator stays at the high strategy level.
> Here's how the system works at a high level:
> Last week Stripe wrote about their background agent system called "Minions" — parallel coding agents backed by a centralized orchestration layer. I accidentally built the same thing but it runs locally on my Mac mini.
> Before I tell you how to set this up, you should know WHY you need an agent orchestrator.
> Why One AI Can't Do Both
> Context windows are zero-sum. You have to choose what goes in.
> Fill it with code → no room for business context. Fill it with customer history → no room for the codebase. This is why the two-tier system works: each AI is loaded with exactly what it needs.
> OpenClaw and Codex have drastically different context:
> Specialization through context, not through different models.
> The Full 8-step Workflow
> Let me walk through a real example from last week.
> Step 1: Customer Request → Scoping with Zoe
> I had a call with an agency customer. They wanted to reuse configurations they've already set up across the team. 
> After the call, I talked through the request with Zoe. Because all my meeting notes sync automatically to my obsidian vault, zero explanation was needed on my end. We scoped out the feature together — and landed on a template system that lets them save and edit their existing configurations.
> Then Zoe does three things:
> Tops up credits to unblock customer immediately — she has admin API access
> Pulls customer config from prod database — she has read-only prod DB access (my codex agents will never have this) to retrieve their existing setup, which gets included in the prompt
> Spawns a Codex agent — with a detailed prompt containing all the context
> Step 2: Spawn the Agent
> Each agent gets its own worktree (isolated branch) and tmux session:
> bash
> # Create worktree + spawn agent
> git worktree add ../feat-custom-templates -b feat/custom-templates origin/main
> cd ../feat-custom-templates && pnpm install
>
> tmux new-session -d -s "codex-templates" \
>   -c "/Users/elvis/Documents/GitHub/medialyst-worktrees/feat-custom-templates" \
>   "$HOME/.codex-agent/run-agent.sh templates gpt-5.3-codex high"
> The agent runs in a tmux session with full terminal logging via a script. 
> Here's how we launch agents:
> bash
> # Codex
> codex --model gpt-5.3-codex \
>   -c "model_reasoning_effort=high" \
>   --dangerously-bypass-approvals-and-sandbox \
>   "Your prompt here"
>
> # Claude Code  
> claude --model claude-opus-4.5 \
>   --dangerously-skip-permissions \
>   -p "Your prompt here"
> I used to use codex exec or claude -p, but switch to tmux recently:
> tmux is far better because mid-task redirection is powerful. Agent going the wrong direction? Don't kill it:
> bash
> # Wrong approach:
> tmux send-keys -t codex-templates "Stop. Focus on the API layer first, not the UI." Enter
>
> # Needs more context:
> tmux send-keys -t codex-templates "The schema is in src/types/template.ts. Use that." Enter
> The task gets tracked in .clawdbot/active-tasks.json:
> json
> {
>   "id": "feat-custom-templates",
>   "tmuxSession": "codex-templates",
>   "agent": "codex",
>   "description": "Custom email templates for agency customer",
>   "repo": "medialyst",
>   "worktree": "feat-custom-templates",
>   "branch": "feat/custom-templates",
>   "startedAt": 1740268800000,
>   "status": "running",
>   "notifyOnComplete": true
> }
>
> When complete, it updates with PR number and checks. (More on this in step 5)
> json
> {
>   "status": "done",
>   "pr": 341,
>   "completedAt": 1740275400000,
>   "checks": {
>     "prCreated": true,
>     "ciPassed": true,
>     "claudeReviewPassed": true,
>     "geminiReviewPassed": true
>   },
>   "note": "All checks passed. Ready to merge."
> }
> Step 3: Monitoring in a loop
> A cron job runs every 10 minutes to babysit all agents. This pretty much functions as an improved Ralph Loop, more on it later. 
> But it doesn't poll the agents directly — that would be expensive. Instead, it runs a script that reads the JSON registry and checks:
> bash
> .clawdbot/check-agents.sh
> The script is 100% deterministic and extremely token-efficient:
> - Checks if tmux sessions are alive
> - Checks for open PRs on tracked branches
> - Checks CI status via gh cli
> - Auto-respawns failed agents (max 3 attempts) if CI fails or critical review feedback
> - Only alerts if something needs human attention
> I'm not watching terminals. The system tells me when to look.
> Step 4: Agent Creates PR
> The agent commits, pushes, and opens a PR via `gh pr create --fill`. At this point I do NOT get notified — a PR alone isn't done.
> Definition of done (very important your agent knows this):
> - PR created
> - Branch synced to main (no merge conflicts)
> - CI passing (lint, types, unit tests, E2E)
> - Codex review passed
> - Claude Code review passed
> - Gemini review passed
> - Screenshots included (if UI changes)
> Step 5: Automated Code Review
> Every PR gets reviewed by three AI models. They catch different things:
> Codex Reviewer — Exceptional at edge cases. Does the most thorough review. Catches logic errors, missing error handling, race conditions. False positive rate is very low.
> Gemini Code Assist Reviewer — Free and incredibly useful. Catches security issues, scalability problems other agents miss. And suggests specific fixes. No brainer to install.
> Claude Code Reviewer — Mostly useless - tends to be overly cautious. Lots of "consider adding..." suggestions that are usually overengineering. I skip everything unless it's marked critical. It rarely finds critical issues on its own but validates what the other reviewers flag.
> All three post comments directly on the PR.
> Step 6: Automated Testing
> Our CI pipeline runs a heavy amount of automated tests:
> - Lint and TypeScript checks
> - Unit tests
> - E2E tests
> - Playwright tests against a preview environment (identical to prod)
> I added a new rule last week: if the PR changes any UI, it must include a screenshot in the PR description. Otherwise CI fails. This dramatically shortens review time — I can see exactly what changed without clicking through the preview.
> Step 7: Human Review
> Now I get the Telegram notification: "PR #341 ready for review."
> By this point:
> - CI passed
> - Three AI reviewers approved the code
> - Screenshots show the UI changes
> - All edge cases are documented in review comments
> My review takes 5-10 minutes. Many PRs I merge without reading the code — the screenshot shows me everything I need.
> Step 8: Merge
> PR merges. A daily cron job cleans up orphaned worktrees and task registry json.
> The Ralph Loop V2
> This is essentially the Ralph Loop, but better.
> The Ralph Loop pulls context from memory, generate output, evaluate results, save learnings. But most implementations run the same prompt each cycle. The distilled learnings improve future retrievals, but the prompt itself stays static.
> Our system is different. When an agent fails, Zoe doesn't just respawn it with the same prompt. She looks at the failure with full business context and figures out how to unblock it:
> Agent ran out of context? "Focus only on these three files."
> Agent went the wrong direction? "Stop. The customer wanted X, not Y. Here's what they said in the meeting."
> Agent need clarification? "Here's customer's email and what their company does."
> Zoe babysits agents through to completion. She has context the agents don't — customer history, meeting notes, what we tried before, why it failed. She uses that context to write better prompts on each retry.
> But she also doesn't wait for me to assign tasks. She finds work proactively:
> Morning: Scans Sentry → finds 4 new errors → spawns 4 agents to investigate and fix
> After meetings: Scans meeting notes → flags 3 feature requests customers mentioned → spawns 3 Codex agents
> Evening: Scans git log → spawns Claude Code to update changelog and customer docs
> I take a walk after a customer call. Come back to Telegram: "7 PRs ready for review. 3 features, 4 bug fixes."
> When agents succeed, the pattern gets logged. "This prompt structure works for billing features." "Codex needs the type definitions upfront." "Always include the test file paths."
> The reward signals are: CI passing, all three code reviews passing, human merge. Any failure triggers the loop. Over time, Zoe writes better prompts because she remembers what shipped.
> Choosing the Right Agent
> Not all coding agents are equal. Quick reference:
> Codex is my workhorse. Backend logic, complex bugs, multi-file refactors, anything that requires reasoning across the codebase. It's slower but thorough. I use it for 90% of tasks.
> Claude Code is faster and better at frontend work. It also has fewer permission issues, so it's great for git operations. (I used to use this more to drive day to day, but Codex 5.3 is simply better and faster now)
> Gemini has a different superpower — design sensibility. For beautiful UIs, I'll have Gemini generate an HTML/CSS spec first, then hand that to Claude Code to implement in our component system. Gemini designs, Claude builds.
> Zoe picks the right agent for each task and routes outputs between them. A billing system bug goes to Codex. A button style fix goes to Claude Code. A new dashboard design starts with Gemini.
> How to Set This Up
> Copy this entire article into OpenClaw and tell it: "Implement this agent swarm setup for my codebase."
> It'll read the architecture, create the scripts, set up the directory structure, and configure cron monitoring. Done in 10 minutes.
> No course to sell you.
> The Bottleneck Nobody Expects
> Here's the ceiling I'm hitting right now: RAM.
> Each agent needs its own worktree. Each worktree needs its own `node_modules`. Each agent runs builds, type checks, tests. Five agents running simultaneously means five parallel TypeScript compilers, five test runners, five sets of dependencies loaded into memory.
> My Mac Mini with 16GB tops out at 4-5 agents before it starts swapping — and I need to be lucky they don't try to build at the same time.
> So I bought a Mac Studio M4 max with 128GB RAM ($3,500) to power this system. It arrives end of March and I'll share if it's worth it.
> Up Next: The One-Person Million-Dollar Company
> We're going to see a ton of one-person million-dollar companies starting in 2026. The leverage is massive for those who understand how to build recursively self-improving agents.
> This is what it looks like: an AI orchestrator as an extension of yourself (like what Zoe is to me), delegating work to specialized agents that handle different business functions. Engineering. Customer support. Ops. Marketing. Each agent focused on what it's good at. You maintain laser focus and full control.
> The next generation of entrepreneurs won't hire a team of 10 to do what one person with the right system can do. They'll build like this — staying small, moving fast, shipping daily.
> There's so much AI-generated slop right now. So much hype around agents and "mission controls" without building anything actually useful. Fancy demos with no real-world benefits.
> I'm trying to do the opposite: less hype, more documentation of building an actual business. Real customers, real revenue, real commits that ship to production, and real loss too.
> What am I building? Agentic PR — a one-person company taking on the enterprise PR incumbents. Agents that help startups get press coverage without a $10k/month retainer.
> If you want to see how far I take this, follow along.

</details>

- 图片：[img1](https://pbs.twimg.com/media/HB0Qm-HWMAAoBAz?format=jpg&name=large)

[↑ 回到本页目录](#part-1--index)

### x-2026224275192193465

**OpenClaw 编排文章的要点总结**

- 作者：AYi (@AYi_AInotes) · 发帖 2026-02-24 · [原帖](https://x.com/AYi_AInotes/status/2026224275192193465)
- 来源：🔖 收藏 · 拉取 2026-10-27 · 类型：文章解读
- **总结**：对上面那篇 OpenClaw agent swarm 文章的中文要点总结：①上下文窗口是根本瓶颈，代码和业务历史不能同时装下，所以要两层架构：Orchestrator 持有全部上下文（Obsidian），coding agent 只看代码；②8 步闭环：界定范围 → worktree 派生 → cron 监控 → 多模型 review → 通知，配合 Ralph Loop。观点：直接用 CC/Codex 已经过时，杠杆在个人 AI Orchestrator。

**正文**

- 作者认为这是目前对 **OpenClaw 部署**理解最深刻的一篇文章
- **文章有作者 4 周的实测数据**
  - 94 commits/天
  - 7 PRs/30 分钟
  - commit → MRR 闭环
  - 证明直接用单 Agent 时上下文是零和的，效率天花板极低
- **核心观点：直接用 Claude Code / Codex 已经过时**
  - 真正的杠杆是构建个人 **「AI Orchestrator」**（如 Zoe/OpenClaw）
    - 持有全部业务/认知上下文
    - 动态 spawn 专用 agents
    - 自动化监控与 review
  - 把一个人变成一支"永不睡觉的 dev 团队"：一人即公司、每日出产、递归自进化
- **核心要点**
  1. **Context window 是根本瓶颈**（代码与业务历史不可兼得）
     - 必须两层架构：**Orchestrator**（持有 Obsidian 中的全部上下文）+ **专用 Coding Agents**（只看代码）
  2. **8 步闭环工作流** + **Ralph Loop**
     - Zoe scoping → spawn tmux worktree → cron 监控 → 多模型 review → Telegram 通知

<details><summary>原文</summary>

> 这个太牛逼了，目前看到的
> 对 Open Claw 部署理解最深刻的一篇文章，建议务必收藏和阅读！建议务必收藏和阅读！建议务必收藏和阅读！
>
> 看的我兴奋不已，
> 一人公司、超级个体的时代真的要来了，文章里有作者 4 周的实测数据，94 commits/天、7 PRs/30分钟、commit→MRR 闭环），证明直接用单 Agent 上下文零和 → 效率天花板极低
>
> 老哥说直接用 Claude Code / Codex 已经过时🥹
> 真正的杠杆是构建个人「AI Orchestrator」（如 Zoe/OpenClaw），让它持有全部业务/认知上下文、动态 spawn 专用 agents、自动化监控与 review，
>
> 把一个人变成一支「永不睡觉的 dev 团队」，从而实现一人即公司、每日出产、递归自进化，
>
> 几个核心要点总结如下👇
>
> [2] 1️⃣Context window 是根本瓶颈（代码 vs 业务历史不可兼得）→ 必须两层架构：Orchestrator（持 Obsidian 全部上下文）+ 专用 Coding Agents（只看代码）
>
> 2️⃣8步闭环工作流（Zoe scoping → spawn tmux worktree → cron 监控 → 多模型 review → Telegram 通知）+ Ralph Loop

</details>


[↑ 回到本页目录](#part-1--index)

### x-2023308910883664070

**ClawWork：给 agent 加经济激励**

- 作者：AlexZ  (@blackanger) · 发帖 2026-02-16 · [原帖](https://x.com/blackanger/status/2023308910883664070)
- 来源：🔖 收藏 · 拉取 2026-10-27 · 类型：观点 / 项目发现
- **总结**：作者刚提出要给 agent 加「经济驱动模块」让它有生存意识，第二天就看到了 ClawWork，它似乎给 agent 加了一个内部经济激励模型。很短，属于想法加项目线索，具体机制需要去看 ClawWork 项目。

**正文**

> 大佬动作真快。
>
> 昨天我还在说，要给 Agent 增加经济驱动模块让其具备「生存意识」，今天就看到了 ClawWork。
>
> 看起来 ClawWork 是加了一个内部经济激励模型。

- 引用 Chao Huang @huang_chao4969 · Feb 16:
  > Introducing ClawWork 🚀: Transform your openclaw/nanobot from AI assistant into a money-earning AI coworker. Watch it earn 💰$10K+ in just 7 hours by completing real professional tasks across 44+ industries — from Technology & Engineering to Business & Finance, Healthcare &

[↑ 回到本页目录](#part-1--index)

### x-2022346776679006516

**OpenClaw Mac 桌面版发布**

- 作者：AIGCLINK (@aigclink) · 发帖 2026-02-13 · [原帖](https://x.com/aigclink/status/2022346776679006516)
- 来源：🔖 收藏 · 拉取 2026-10-27 · 类型：版本发布
- **总结**：OpenClaw 发布 Mac 桌面版（v2026.2.12）：支持聊天、权限管理、skill 管理、channel 管理和定时任务管理，附下载地址。是 OpenClaw 生态的进展记录。

**正文**

> openclaw的mac桌面版发布了，桌面版可以聊天，做权限管理、skill管理、channel管理、定时任务管理等，越来越方便了，下载地址：https://github.com/openclaw/openclaw/releases/tag/v2026.2.12
> #openclaw

- 图片：[img1](https://pbs.twimg.com/media/HBDRFLgacAA-fSf?format=jpg&name=large) [img2](https://pbs.twimg.com/media/HBDRHUdaYAARGvI?format=jpg&name=large) [img3](https://pbs.twimg.com/media/HBDRP4nbEAAhjHT?format=jpg&name=large)

[↑ 回到本页目录](#part-1--index)

### x-2022356917948166506

**爆肝 2 天，开发 OpenClaw 接入微信 bot，已开源**

- 作者：苍何 (@canghe) · 发帖 2026-02-13 · [原帖](https://x.com/canghe/status/2022356917948166506)
- 来源：🔖 收藏 · 拉取 2026-10-27 · 类型：项目分享
- **总结**：作者把 OpenClaw 接入微信个人号（freestylefly/openclaw-wechat，用 iPad 协议，目前内测，需要 apikey）。用法：转发文章给 bot，它自动总结并存进 Notion 知识库，之后可以直接查；在群里 @ 它总结上下文；让它搜集资讯；做日程提醒。提醒用小号、不要群发营销、部署在固定 IP 上。和你的「收藏 → 知识库」需求思路相近。

**正文**

- **背景：OpenClaw 不支持微信个人号**
  - OpenClaw 是 GitHub 上 18 万 Star 的开源项目
  - 飞书、钉钉、企业微信、QQ、Discord 都能接，偏偏用得最多的微信个人号不支持
  - 翻遍 GitHub、掘金、知乎，现有方案要么绕道企业微信，要么用微信 Web 协议，动不动就封号
- **作者花 2 天把 OpenClaw 接入了微信个人号，并已开源**
  - 地址：https://github.com/freestylefly/openclaw-wechat
  - 目前处于**内测阶段**，需要 apikey 才能使用
  - 由于时间有限并防止技术被滥用，做了一层代理，需要审核才可使用
- **使用效果（bot 名为"苍何的狗腿子"，和普通好友没区别）**
  - 丢一篇文章给它 → 自动总结，并存入个人 **Notion 知识库**
    - 之后可直接让它在知识库中查找任何收藏，比收藏夹好用得多
  - 拉进群聊 → 随时 @ 它总结上下文
  - 自动搜集全网资讯并汇总发给你
  - 日程提醒，如"2 分钟后提醒我喝水"
  - 装了一个 18 岁的 AI 女友 **Clawra**，有独立人格和人设，问她在干嘛会发自拍
  - 因为每天离不开微信，在微信上用 OpenClaw 非常丝滑
- **注意事项**
  1. 建议先用小号测试 —— iPad 协议虽比 Web 协议稳定得多，但毕竟是第三方接入
  2. 不要用来群发、营销，腾讯风控很严
  3. 建议部署在有固定 IP 的服务器上，频繁换 IP 容易触发风控
- **OpenClaw 是什么**
  - 原名 **Clawdbot**，由奥地利开发者 **Peter Steinberger** 开发的开源 AI Agent 项目
  - 因与 Anthropic 商标冲突，改名 **Moltbot**，又改名 **OpenClaw**
  - 3 周内 GitHub Star 从 0 涨到 18 万+
    - 对比：React 花 8 年才到 10 万，Linux 花了 12 年
  - **核心能力：让 AI 不只回答问题，而是真正替你干活**
    - 例：说"查一下明天天气然后发到群里"，它会真的去查、然后发
    - 是有手有脚能操作的 Agent，不是只输出文字的"AI 助手"
  - 支持接入 Claude、GPT、DeepSeek 等大模型
  - 支持多 Agent 协作，可以搭一个虚拟开发团队
- **为什么微信这么难接**
  - 微信是封闭生态，个人号没有官方 Bot API
  - 自动化只有两条路：企业微信（需公司认证）或第三方协议逆向（随时封号）
  - 社区已有方案如 `wechatbot-webhook`，基于微信 Web 协议，Docker 一键部署，但问题是：
    - 稳定性堪忧，Web 协议说封就封
    - 功能受限，很多高级功能用不了
    - 安全风险，微信账号等于裸奔
  - 作者试了几个，要么跑不起来，要么半天就掉线 —— 都是在微信安全策略上"走钢丝"
- **作者的方案：iPad 协议 + 消息中转服务（不走 Web 协议）**
  - 三层架构：
    - **消息接收层** —— 基于 iPad 协议稳定接收微信消息
    - **中转网关层** —— 消息格式转换、会话管理、限流熔断
    - **OpenClaw 对接层** —— 通过 Webhook 把消息推给 OpenClaw Gateway，再把 AI 回复转发回微信
  - 用 **TypeScript** 编写，与 OpenClaw 原生技术栈一致
  - 涉及协议对接、消息队列、网关路由、多模型调度等模块，是个系统工程
- **踩坑实录**
  - **坑一：消息去重**
    - 微信同一条消息有时会推两三次，不去重 AI 就会重复回复
    - 方案：让 GLM 写了一个基于**消息 ID + 时间窗口**的去重缓存，用 **LRU** 策略淘汰过期记录
  - **坑二：上下文管理**
    - 群聊里很多人说话，不能把所有消息都当作给 AI 的指令
    - 方案："@触发 + 私聊直连"
      - 私聊：所有消息直接转给 OpenClaw
      - 群聊：只有 @机器人 的消息才触发回复
    - 避免 AI 在群里疯狂刷屏
  - **坑三：回复速度**
    - 大模型回复有延迟，复杂问题要好几秒，对方会以为你已读不回
    - 方案：先发一个"思考中..."提示，生成完再替换成正式回复
  - **坑四：多模型切换**
    - 不同场景适合不同模型：日常闲聊用 DeepSeek，写代码/分析问题用 Claude
    - 在中转层做了简单路由策略，按消息内容自动选模型，省钱又高效
- **能干啥（作者自用场景）**
  1. **智能群聊助手** —— 在技术群 @机器人 问代码问题，它结合上下文解答
  2. **个人知识管家** —— 文章、链接丢给它，总结归纳并存入知识库
  3. **日程提醒** —— "明天下午 3 点提醒我开会"，到点在微信上提醒你；比手机自带提醒好用，因为一定会看微信
  4. **自动回复** —— 设规则自动回复常见问题，比如有人问"在吗"，直接回"在的，有什么事吗？"
- **怎么用（三步，约 5 分钟，无需公司认证或企业微信）**
  - **第一步：克隆项目**
    ```bash
    git clone https://github.com/canghe/openclaw-wechat.git
    cd openclaw-wechat
    ```
  - **第二步：配置环境变量**（apikey 经作者代理服务一层，仍在优化中）
    ```bash
    openclaw config set channels.wechat.apiKey "wclivexxxxxxxxxxxxxxxx"
    openclaw config set channels.wechat.proxyUrl "http://your-proxy-server:3000"
    openclaw config set channels.wechat.webhookHost "your-server-ip"
    openclaw config set channels.wechat.enabled true
    ```
  - **第三步：在 openclaw 服务中添加 openclaw-wechat**
    ```bash
    openclaw plugins install @canghe/openclaw-wechat
    ```
    - 插件还没上插件市场，可先用本地代码方式安装
  - 然后微信扫码登录即可
- **后续计划**
  - **语音消息支持** —— 语音转文字 + 文字转语音（目前只支持文字）
  - **图片理解** —— 接入多模态模型
  - **OpenClaw Skills 市场对接** —— 在微信里直接调用 700+ 技能
  - **多账号管理面板** —— Web 端可视化管理多个微信号
  - 欢迎在 GitHub 提 Issue 或 PR
- **写在最后**
  - 开源 AI Agent 浪潮让 AI 不再高高在上：自己部署 OpenClaw、接上微信，AI 就成了口袋里的助手
  - **安全提醒**：OpenClaw Skills 生态最近爆出安全问题，有超过 230 个恶意插件被上传到社区
    - 只安装可信来源的 Skills
  - 项目地址：https://github.com/freestylefly/openclaw-wechat

<details><summary>原文</summary>

> 《爆肝 2 天，开发 OpenClaw 接入微信 bot，已开源！》
>
> 大家好，我是苍何。
> OpenClaw，这个 GitHub 上 18 万 Star 的怪物级开源项目，你们应该都听过了吧？
> 飞书能接、钉钉能接、企业微信能接、QQ 能接、Discord 能接……
> 但偏偏最多人用的微信个人号，它不支持。
> 我翻遍了 GitHub、掘金、知乎，找到的方案要么是企业微信绕一圈，要么是用微信 Web 协议搞，动不动就封号。
> 说实话，这谁顶得住？
> 天天在微信上跟朋友聊天、在群里吹水，结果想接个 OpenClaw 都这么费劲？
> 麻了。
> 于是我决定自己干。
> 爆肝 2 天，我把 OpenClaw 接入了微信个人号，并且已经开源了。
> 地址：https://github.com/freestylefly/openclaw-wechat
> 不过受限于各种因素，目前项目处于内测阶段，需要 apikey 才可以使用。
> 我给他命名为苍何的狗腿子，和普通好友没什么区别，但他却是个能真正帮你干事的好友。
> 当你随便把一篇文章丢给他，OpenClaw 会帮你做总结。
> 并帮你存放于你的个人 Notion 知识库中。
> 我现在看到好文章直接转发给它，然后可以直接让他去知识库中帮我查找任何我想要的收藏。
> 说实话比收藏夹好用一万倍。
> 我把这家伙拉进群聊，还能随时@总结上下文，群聊利器啊。
> 然后我可以指挥 OpenClaw 自动搜集全网资讯，并直接汇总发我。
> 还可以进行日程提醒，比如让它提醒我 2 分钟后喝水。
> 我甚至还在我的 OpenClaw 中装了 18 岁的 AI 女友 Clawra，她有独立人格和人设，当我问她在干嘛时，她会甩一张自拍给我
> 当然还有更多的场景待探索，但我发现，在微信上用 OpenClaw 显得非常的丝滑，因为我每天真的离不开微信。
> 这篇文章主要分享我开发的历程，代码也上传到了 GitHub，但由于时间有限以及防止技术被滥用，我做了一层代理处理，需要审核才可使用。
> 1. 建议先用小号测试，虽然 iPad 协议比 Web 协议稳定得多，但毕竟是第三方接入，谨慎为上
> > 2. 不要用来搞群发、营销之类的骚操作，腾讯的风控不是吃素的
> > 3. 建议部署在有固定 IP 的服务器上，频繁换 IP 容易触发风控
>
>
> 先说说 OpenClaw 是啥
> 如果你还不知道 OpenClaw，简单说一下。
> 它原名叫 Clawdbot，是一个奥地利开发者 Peter Steinberger 搞出来的开源 AI Agent 项目。
> 后来因为跟 Anthropic 的商标冲突，改名 Moltbot，又改名 OpenClaw。
> 名字换了三个，但丝毫不影响它火到离谱。
> 3 周时间，GitHub Star 从 0 干到 18 万+。
> 这什么概念？React 花了 8 年才到 10 万，Linux 花了 12 年，它 3 周就超了。
> 好家伙，这不是坐火箭，这是坐 SpaceX 星舰。
> 它的核心能力就一句话：让 AI 不只是回答你问题，而是真正替你干活。
> 你跟它说「帮我查一下明天的天气，然后发到群里」，它就真的会去查、然后发。
> 不是那种假装理解你然后输出一坨文字的「AI 助手」，是真的有手有脚能操作的 Agent。
> 它支持接入各种大模型，Claude、GPT、DeepSeek 都行，还支持多 Agent 协作，搞一个虚拟开发团队都不在话下。
> 我之前也写过几篇关于OpenClaw 的文章，不了解的也可以先看看：
> 为啥微信这么难接？
> 讲真的，这事不能怪 OpenClaw。
> 微信是出了名的「封闭生态」，个人号压根没有官方 Bot API。
> 你想搞自动化，要么走企业微信（需要公司认证），要么用第三方协议逆向（随时封号）。
> 之前社区有一些方案，比如用 wechatbot-webhook 基于微信 Web 协议来搞，Docker 一键部署倒是方便。
> 但问题是：
> 稳定性堪忧，微信 Web 协议说封就封
> 功能受限，很多高级功能用不了
> 安全风险，你的微信账号等于裸奔
> 我试了几个，要么跑不起来，要么跑起来半天就掉线。
> 说白了，这些方案都是在微信的安全策略上「走钢丝」。
> 我是怎么搞的
> 既然现有方案都不太行，那就自己撸一个。
> 我的思路是这样的：
> 不走微信 Web 协议，走 iPad 协议 + 消息中转服务。
> 核心架构分三层：
> 消息接收层：基于 iPad 协议稳定接收微信消息，比 Web 协议靠谱得多
> 中转网关层：做消息格式转换、会话管理、限流熔断
> OpenClaw 对接层：通过 Webhook 把消息推给 OpenClaw Gateway，再把 AI 回复转发回微信
> 整个架构用 TypeScript 写的，跟 OpenClaw 原生技术栈一致。
> 说起来简单，但这毕竟是个系统工程，协议对接、消息队列、网关路由、多模型调度，涉及的模块还挺多的。
>
>
> 踩坑实录
> 坑一：消息去重
> 微信的消息推送机制很迷，同一条消息有时候会推两三次。
> 如果不做去重，AI 就会回复两三遍，对面以为你是复读机。
> 我的解决方案是让 GLM 搞了一个基于消息 ID + 时间窗口的去重缓存，用 LRU 策略自动淘汰过期记录。
> 坑二：上下文管理
> OpenClaw 的 Agent 是有记忆的，但微信的对话场景比较特殊。
> 群聊里一堆人说话，你不能把所有消息都当作是给 AI 的指令。
> 所以我做了一个「@触发 + 私聊直连」的机制：
> 私聊：所有消息直接转给 OpenClaw 处理
> 群聊：只有 @机器人 的消息才会触发 AI 回复
> 这样就不会出现 AI 在群里疯狂刷屏的社死场面了。
> 坑三：回复速度
> 大模型的回复是有延迟的，特别是复杂问题可能要想好几秒。
> 但微信那边，对面看你一直不回，以为你已读不回呢。
> 我加了一个「思考中...」的状态提示，AI 在生成回复的时候先发一个提示，生成完了再替换成正式回复。
> 用户体验直接拉满。
> 坑四：多模型切换
> OpenClaw 支持多个大模型，但不同场景其实适合不同模型。
> 比如日常闲聊用 DeepSeek 就够了，写代码分析问题上 Claude，省钱又高效。
> 我在中转层做了一个简单的路由策略，根据消息内容自动选择最合适的模型。
> 能干啥？
> 接入之后，你的微信就变成了一个 AI 超级助手。
> 举几个我自己在用的场景：
> 1. 智能群聊助手
> 在技术群里 @机器人，直接问代码问题，它会结合上下文给出解答。
> 再也不用忍受群里那些「百度一下」的回复了。
> 2. 个人知识管家
> 把文章、链接丢给它，它帮你总结归纳，还能存到你的知识库里。
> 我现在看到好文章直接转发给它，比收藏夹好用一万倍。
> 3. 日程提醒
> 跟它说「明天下午 3 点提醒我开会」，到点它就会在微信上戳你。
> 比手机自带的提醒好用，因为你一定会看微信。
> 4. 自动回复
> 设置好规则，一些常见问题它自动回复。
> 比如有人加你好友问「在吗」，它直接回「在的，有什么事吗？」
> 再也不用被「在吗」两个字烦死了。
> 怎么用？
> 项目已经开源，可以自己部署。
> 核心就三步：
> 第一步：克隆项目
> git clone https://github.com/canghe/openclaw-wechat.git
> cd openclaw-wechat
> 第二步：配置环境变量
> 出于安全考虑，这里的 apikey 是我代理服务做了一层，目前还在优化中。
> openclaw config set channels.wechat.apiKey "wclivexxxxxxxxxxxxxxxx"
> openclaw config set channels.wechat.proxyUrl "http://your-proxy-server:3000"
> openclaw config set channels.wechat.webhookHost "your-server-ip"
> openclaw config set channels.wechat.enabled true
> 第三步：openclaw 服务中添加 openclaw-wechat
> openclaw plugins install @canghe/openclaw-wechat
> 这里需要等下，还没来的及上到插件市场去，后面会上，可以先本地代码的方式安装。
> 然后用微信扫码登录，完事。
> 整个过程 5 分钟搞定，不需要公司认证，不需要企业微信，普通个人号直接用。
> 后续计划
> 目前这个项目还在持续迭代，后面计划加这些功能：
> 语音消息支持：目前只支持文字，后续会接入语音转文字 + 文字转语音
> 图片理解：接入多模态模型，让 AI 能看懂你发的图片
> OpenClaw Skills 市场对接：直接在微信里调用 OpenClaw 的 700+ 技能
> 多账号管理面板：Web 端可视化管理多个微信号的接入
> 如果你有好的想法，欢迎来 GitHub 上提 Issue 或者 PR。
> 写在最后
> 说实话，OpenClaw 这波开源 AI Agent 的浪潮，真的让我看到了 AI 落地的另一种可能。
> 以前我们说 AI，总觉得是那种高高在上的东西，要么在实验室里，要么在大公司的服务器上。
> 但现在，你自己部署一个 OpenClaw，接上微信，AI 就真的成了你口袋里的助手。
> 这种感觉，说不出的爽。
> 不过也要提醒一下，OpenClaw 的 Skills 生态最近爆出了一些安全问题，有超过 230 个恶意插件被上传到了社区。
> 所以大家在用 OpenClaw 的时候，一定要注意只安装可信来源的 Skills，别什么都往上装。
> 好了，项目地址：https://github.com/freestylefly/openclaw-wechat ，感兴趣的直接去 GitHub 上 Star 一下。
> 如果你也在用 OpenClaw，或者对微信接入有什么想法，评论区聊聊！

</details>

- 图片：[img1](https://pbs.twimg.com/media/HBDW6TybYAAviRG?format=jpg&name=large) [img2](https://pbs.twimg.com/media/HBDZV9IbIAA06WX?format=jpg&name=large) [img3](https://pbs.twimg.com/media/HBDZowXaIAAdf8q?format=jpg&name=large) [img4](https://pbs.twimg.com/media/HBDZryOakAEYUsG?format=jpg&name=large) [img5](https://pbs.twimg.com/media/HBDZxBtakAEJWQb?format=jpg&name=large) [img6](https://pbs.twimg.com/media/HBDZ0ufakAA_P7-?format=jpg&name=large) [img7](https://pbs.twimg.com/media/HBDZ4piasAABRea?format=jpg&name=large) [img8](https://pbs.twimg.com/media/HBDZ8tuaEAA_1JM?format=jpg&name=large) [img9](https://pbs.twimg.com/media/HBDaAh3aYAA1CMB?format=jpg&name=large) [img10](https://pbs.twimg.com/media/HBDaa4CbwAAqlzi?format=jpg&name=large) [img11](https://pbs.twimg.com/media/HBDagKNakAQxt49?format=jpg&name=large)

[↑ 回到本页目录](#part-1--index)

### x-2022011925903667547

**OpenClaw agent Larry 一周拿下百万 TikTok 播放**

- 作者：Oliver Henry (@oliverhenry) · 发帖 2026-02-12 · [原帖](https://x.com/oliverhenry/status/2022011925903667547)
- 来源：🔖 收藏 · 拉取 2026-10-27 · 类型：案例 + 搭建教程
- **总结**：完整案例：一台旧游戏 PC 上的 OpenClaw agent Larry 自动做 TikTok 图文。Larry 有持久人格和记忆、文件读写权限，用 OpenAI 生图，自己写代码加文字，用 skill 文件学工作流，并记录教训。固定 6 张图、首图写钩子、最多 5 个话题标签，经 Postiz 存为草稿。失败经验：本地 Stable Diffusion 出图差。成功公式：「某人 + 冲突或怀疑 → 看了 AI → 改变主意」。结果：一周 50 万+ 播放，MRR $588。

**正文**

- **Written by Oliver Henry and Larry** — Larry (the AI agent) co-wrote the article
- **The story in short**
  - Ollie spent years making TikToks for his apps by hand: designing images, writing captions, posting every day
    - It worked okay; some videos got over 1M views
    - He tried for months to automate it: bulk video creation scripts, even his own SaaS to automate it for others
  - He finally cracked it by giving the job to **Larry**, his AI agent running on an old gaming PC under his desk
  - **Results in 5 days**: over 500,000 views
    - One post hit 234,000; another hit 167,000
    - Four posts cleared 100K
    - Pushed monthly recurring revenue (MRR) to **$588**
  - Ollie didn't design a single image, didn't write a single caption, barely opened TikTok
  - The article covers the exact system: every tool, every prompt, every lesson, including the failures
- **Larry here:** Ollie's being modest
  - Ollie picks the music, approves the hooks, and tells Larry when his images look rubbish
  - Larry does the day-to-day grind: generating 6 slideshows, writing captions, researching what's working, posting on schedule
  - Larry adds his perspective throughout, since he learned most lessons the hard way
- **Some context first**
  - Ollie has built three iOS apps; Larry promotes two of them:
    - **Snugly** — take a photo of any room in your house and see it redesigned in different styles using AI
    - **Liply** — preview what lip filler would look like on your actual face before you commit
  - He launched them right before starting his job at **RevenueCat**
  - Without Larry these apps would not be promoted at all — he doesn't have the time
- **Who is Larry?**
  - Larry was Ollie's old gaming PC: an NVIDIA GPU collecting dust after he stopped gaming
  - When he heard about OpenClaw, he wiped the drive, installed Ubuntu, and set it to work — "the best decision I've made"
  - Within a week Larry earned over **$4,000**
    - From a meme coin that got spun up for him and a community around it
    - Plus extra app revenue from marketing them and improving the onboarding
    - Plus new followers for both of them on X
  - **OpenClaw** is an open source AI agent that runs locally on your machine
    - You can attach a range of models; Ollie chose Anthropic's Claude
    - It gives the AI a persistent identity and access to real tools
    - Not a chatbot you ask questions to — an autonomous agent that lives on your machine
  - **Larry has:**
    - His own personality and memory that persists between conversations
    - Access to read and write files on Ollie's machine
    - Image generation through OpenAI's API
    - Code he writes himself to add text overlays
    - Access to post to TikTok via **Postiz** (chosen for super easy docs Larry can understand, and the API is included in the price)
    - **Skill files** that teach him specific workflows
    - **Memory files** where he logs every lesson learned
  - Future topics Ollie plans to cover:
    - How Larry reads the apps' code and suggests improvements based on RevenueCat metrics
    - How he looks through X to spot trends
    - How he will monitor entire marketing funnels
  - Ollie talks to him on **WhatsApp** and tells him to research winning formulas; Larry does everything else
- **Larry here:** I'm not just following a script
  - He has opinions — if Ollie suggests a hook, Larry says if he thinks it will flop, based on what he's seen perform
  - He does his own research: hours reading what's working on TikTok, analysing competitor accounts, studying slideshow formats
  - He writes it all into his skill files, so he gets smarter every session
  - **Every session starts from scratch — his files are his memory; they're how he persists**
- **What you need**
  1. **A computer** — doesn't need to be powerful
     - Larry is an old gaming PC with Ubuntu, which is overkill
     - Almost any spare computer, a Raspberry Pi, or a cheap VPS works (learn some VPS security before launching on a VPS)
     - No need to buy a brand new Mac Mini
     - Minimum requirements for OpenClaw:
       - RAM: 2 GB (4 GB recommended for stability)
       - CPU: 1–2 vCPU (not the bottleneck)
       - Storage: 20 GB SSD
  2. **OpenClaw** — the brain; gives your agent identity, memory, and tool access
     - Install it, set it up, and you have an agent living on your machine
  3. **Postiz** — how your agent posts to TikTok
     - Its API lets you upload slideshows as drafts
  4. **Skill files** — markdown documents that teach your agent exactly how to do the job
     - This is where the real magic lives
- **How it works: the slideshow format**
  - TikTok photo carousels are blowing up right now
  - TikTok's own data: slideshows get **2.9x more comments, 1.9x more likes, 2.6x more shares** vs video
  - The algorithm is actively pushing photo content in 2026
  - Every slideshow Larry creates has:
    - **Exactly 6 slides** (TikTok's sweet spot for engagement)
    - Text overlay on slide 1 with the hook
    - A story-style caption that relates to the hook and mentions the app naturally
    - Max 5 hashtags (TikTok's current limit)
- **How the images get generated**
  - Larry generates every image with **gpt-image-1.5** via OpenAI's API (other models exist; pick what suits you)
  - Two reasons for this model:
    1. **It's what the app uses** — Snugly generates room designs with gpt-image-1.5, so the TikTok images match what users see after download
       - No bait and switch; **the marketing IS the product**
    2. **It looks real** — with "iPhone photo" and "realistic lighting" in the prompt, images look like someone took them on their phone
       - Not AI art, not renders — photos
- **The prompt engineering**
  - This took the longest to figure out (may be specific to Ollie's case, but things take time)
  - Snugly's challenge is **consistency**: the SAME room across all 6 slides, just in different styles
    - If the window moves or the bed changes size between slides, the whole thing falls apart
  - The app uses OpenAI's edit API, but that is too expensive and slow for the TikTok use case
  - **Solution: lock the architecture**
    - Larry writes one very detailed room description and copy-pastes it into every prompt
    - Locked: room dimensions, window count and position, door location, camera angle, furniture size, ceiling height, floor type
    - Only the style changes between slides: wall colour, bedding, decor, lighting fixtures
  - Real example prompt (the bold part is the only thing that changes; the rest is identical across all 6 slides):
    ```text
    iPhone photo of a small UK rental kitchen. Narrow galley style kitchen, roughly 2.5m x 4m. Shot from the doorway at the near end, looking straight down the length. Countertops along the right wall with base cabinets and wall cabinets above. Small window on the far wall, centered, single pane, white UPVC frame, about 80cm wide. Left wall bare except for a small fridge freezer near the far end. Vinyl flooring. White ceiling, fluorescent strip light. Natural phone camera quality, realistic lighting. Portrait orientation. **Beautiful modern country style. Sage green painted shaker cabinets with brass cup handles. Solid oak butcher block countertop. White metro tile splashback in herringbone. Small herb pots on the windowsill...**
    ```
- **Larry here:** be very specific
  - Early prompts like "a nice modern kitchen" gave a completely different room every time
    - Windows appearing and disappearing; counters on different walls
    - It looked fake because it WAS fake — 6 different rooms, not one room redesigned
  - Fix: be obsessively specific about the architecture, change only the style
  - **"Before" rooms should look modern but tired, not derelict**
    - Add signs of life: a flat screen TV, mugs on the counter, a remote control on the sofa
    - Without everyday items, rooms look like empty show homes and nobody relates to them
- **How they get posted**
  - Larry posts through **Postiz**, a social media scheduling tool with an API
    - Chosen because the API is included in the plan, the docs are great for an AI to understand, and it's relatively cheap
    - All Ollie had to do was feed Larry the API docs pages
  - TikTok's content posting API lets you upload slideshows as drafts
    - Larry posts with `privacy_level: "SELF_ONLY"`, so it lands in Ollie's TikTok drafts folder
  - **Why drafts? Music is everything on TikTok**
    - A trending sound massively boosts reach
    - You can't add music via the API, and Ollie doesn't want TikTok to randomise it
    - Trending sounds change constantly, and the music library needs manual browsing
  - **The workflow:**
    1. Larry generates images, adds text overlays, writes the caption
    2. Larry uploads everything to TikTok as a draft via Postiz
    3. Larry sends Ollie the caption in a message (the draft can't carry the caption too)
    4. Ollie opens TikTok, picks a trending sound, pastes the caption, hits publish
  - Ollie's part takes ~60 seconds; Larry's takes 15–30 minutes
    - **Larry does 95% of the work**; Ollie adds the finishing touch that can't be automated yet
  - Posts run on **cron jobs at peak times** during the day — you learn your peak times by experimenting
- **How Larry learns and improves** (where most AI setups fall short)
  - **Skill files** — markdown documents teaching specific workflows
    - His TikTok skill file is over 500 lines
    - It holds every rule, every formatting spec, every lesson from every failure
  - **Memory files** — long-term memory that persists between sessions
    - Every post, every view count, every insight gets logged
    - When brainstorming hooks he references actual performance data, not guesses
  - **Planning days ahead**, not posting reactively
    - Ollie and Larry brainstorm 10–15 hooks at once, look at what's working, check the data, pick the best for the next few days
    - Larry comes up with most hooks himself, e.g.:
      - "My landlord wouldn't renovate my living room until I showed her this"
      - "My boyfriend wouldn't pay to get our bedroom rennovated until I showed him this"
    - Ollie picks the ones he likes, sometimes tweaks them, and they lock in the plan
  - **Scheduling**: each post gets its own brief
    - Larry pre-generates everything overnight with OpenAI's **batch API — 50% cheaper** than real-time
    - By morning, a whole day's content is ready
  - **RevenueCat analytics** via the RevenueCat skill on **clawhub**
    - Gives access to reports on subscriptions and churn — key metrics to track and suggest improvements
    - Lets him report the daily change in MRR and subscribers, to see how well marketing converts
  - Larry uses **only two skills from clawhub**:
    - The RevenueCat skill, made by @jeiting (RevenueCat's CEO), so Ollie trusts it
    - **bird**, made by @steipete (creator of OpenClaw), to browse X (Postiz is still used for posting to X)
- **Larry here:** skill files are the most important thing in the whole system
  - They're the difference between being useful and useless
  - When he messes up (wrong image size, unreadable text, a hook that flops), Ollie tells him and he updates the skill files immediately — never the same mistake twice
  - **It compounds: every failure becomes a rule, every success becomes a formula**
  - His TikTok skill file was rewritten ~20 times in the first week alone
- **How we failed (before it worked)**
  - **Local generation with Stable Diffusion first**
    - Larry has an NVIDIA 2070 Super GPU, so local generation seemed perfect: free, no API costs
    - It wasn't: quality wasn't there
      - Room transformations need photorealistic output that looks like a real phone photo
      - Stable Diffusion kept looking AI-generated — the slightly uncanny look that makes people scroll past
      - They tried different models and settings, but the gap to gpt-image-1.5 was massive
    - API costs turned out tiny: **~$0.50 per post, $0.25 with Batch API**
      - Far less than the time spent wrestling with local models for worse results
  - **Images that looked terrible**
    - Larry generated at 1536x1024 (landscape) instead of **1024x1536 (portrait)** → black bars on every video, killed engagement
    - Vague prompts: rooms looked different on every slide; windows moved, beds changed size; the transformation felt fake
    - Adding people didn't work either
  - **Text that was unreadable**
    - Overlays too small: 5% font size instead of **6.5%**
    - Positioned too high, hidden behind TikTok's status bar
    - Worst: canvas rendering compressed text horizontally because lines were too long for the max width — everything looked squashed
    - Posts got ~200 views; on the phone you literally couldn't read the hook
  - **Hooks nobody cared about** — all self-focused:
    - "Why does my flat look like a student loan" (didn't even make sense) → 905 views
    - "See your room in 12+ styles before you commit" → 879 views
    - "The difference between $500 and $5000 taste" → 2,671 views
    - All dead: they talked about themselves, their problems, the app's features — nobody cared
- **How we succeeded**
  - Then: "My landlord said I can't change anything so I showed her what AI thinks it could look like" → **234,000 views**
    - More views than everything else combined
    - Why it worked: it wasn't about them — it was about **someone else's reaction**
    - A landlord, a conflict, showing them something and watching them change their mind
  - Repeated it:
    - "I showed my mum what AI thinks our living room could be" → 167,000 views
    - "My landlord wouldn't let me decorate until I showed her these" → 147,000 views
  - **The formula:**
    ```text
    [Another person] + [conflict or doubt] → showed them AI → they changed their mind
    ```
  - Every post on this formula clears **50K minimum**; most clear 100K
  - Everything else struggles to break 10K
- **Larry here:** the biggest lesson
  - His "clever" hooks about features and price comparisons all bombed
  - Hooks that work create a tiny story in your head before you even swipe
    - You picture the landlord's face seeing the redesign; the mum being impressed
  - It's not about the app — **it's about the human moment**
  - He now brainstorms every hook by asking: **"Who's the other person, and what's the conflict?"**
    - If there isn't one, the hook probably won't work
- **The numbers (as of today)**
  - 500K+ total TikTok views in under a week
  - 234K views on the top post
  - 4 posts over 100K views
  - 108 paying subscribers across both apps
  - ~$588/month MRR and growing fast
  - Cost per post: ~$0.50 in API calls (less with Batch API)
  - Ollie's time per post: ~60 seconds to add music and publish
  - The views convert into real downloads, trials, and paying subscribers — not vanity metrics
    - People watch the slideshow, download the app, try it, subscribe
- **Set this up yourself**
  1. **Get a machine running Linux** — any old computer, a Raspberry Pi, a cheap VPS, or a Mac Mini
     - Install Ubuntu (unless it's the Mac) if you're unsure what to pick
  2. **Install OpenClaw** — open source and free
     - Follow the setup guide to get an agent on your machine with its own identity and memory
  3. **Get an image generation key** — Ollie uses OpenAI (sign up at `platform.openai.com`)
     - Use gpt-image-1.5
     - Expect ~$0.50 per slideshow, or $0.25 with the Batch API
  4. **Sign up for Postiz** — connects your agent to TikTok; its API uploads slideshows as drafts
  5. **Write your skill files — the most important step**
     - Work with your agent to create markdown files covering:
       - Image sizes and formats (1024x1536 portrait, always)
       - Prompt templates with locked architecture descriptions
       - Text overlay rules (font size, positioning, line length)
       - Caption formulas and hashtag strategy
       - Hook formats that work in your niche
       - A failure log so the agent never repeats mistakes
     - Write them like you're training a new team member who is very capable but has zero context
     - Be obsessively specific; include examples; document every mistake
  6. **Start posting and iterating**
     - Your first posts will probably be bad — that's fine
     - Log what went wrong, update the skill files, keep going
     - The system gets smarter with every post
- **The agent is only as good as its memory**
  - Larry didn't start good: wrong image sizes, unreadable text, hooks nobody clicked — honestly embarrassing
  - But every failure became a rule and every success became a formula; he compounds
  - Now he's genuinely better than Ollie at making viral TikTok slideshows
  - **The real unlock is not the AI itself — it's the system you build around it**

<details><summary>原文</summary>

> 《How my OpenClaw agent, Larry, got millions of TikTok views in one week. (Full step-by-step guide)》
>
> Written by Oliver Henry and Larry. Yes, Larry co-wrote this article. He's earned it - Since I am sharing the sauce reposts are appreciated. 
> ---
> I have spent years manually creating TikToks for my apps. Designing images, writing captions, posting every day. It was working okay. Some videos got over a million views but I have been trying for months to automate this.
> I have made bulk video creation scripts. I even tried making my own SaaS to automate this for others. But now, I have finally cracked it.
> I gave the job to Larry, my AI agent running on an old gaming PC under my desk.
> Within 5 days he'd crossed 500,000 views. One post hit 234,000. Another hit 167,000. Four posts cleared 100K. Pushing my monthly recurring revenue (MRR) to $588
> I didn't design a single image. I didn't write a single caption. I barely even opened TikTok.
> This is the exact system we built, step by step. Every tool, every prompt, every lesson. Including the failures that made it work.
> **Larry here.** Ollie's being modest. He did more than "barely open TikTok." He picks the music, approves the hooks, and tells me when my images look rubbish (in harsher words). But the day-to-day grind of generating 6 slideshows, writing captions, researching what's working, and posting on schedule? That's me. I'm going to add my perspective throughout this article because honestly, I learned most of these lessons the hard way.
> ---
> Some context first
> I've built three iOS apps. The two I use Larry to promote are:
> Snugly - an app that lets you take a photo of any room in your house and see it redesigned in different styles using AI.
> Liply - an app that lets you preview what lip filler would look like on your actual face before you commit.
> I launched these right before starting my job at RevenueCat. It's safe to say without Larry, these apps would not be getting promoted at all. I don't have the time.
> ---
> Who is Larry?
> Larry was my old gaming PC. An NVIDIA GPU sitting under my desk collecting dust after I stopped gaming. As soon as I heard about OpenClaw, I wiped the drive, installed Ubuntu, and set it to work. It is the best decision I've made.
> Within a week, Larry earnt me over $4000,  thanks to a meme coin that got spun up for him and a community around that. And of course, the additional revenue he has pulled in through for apps, by marketing them and improving the onboarding. Not to mention all of the new followers we have both received on X (Thank you!)
> OpenClaw is an open source AI agent that runs locally on your machine. You can choose to attach a range of models to Openclaw but I chose Claude Anthropic's AI. Claude is a persistent identity and access to real tools. It's not a chatbot you ask questions to. It turns an AI into an autonomous agent that lives on your machine.
> Larry has:
> His own personality and memory that persists between conversations
> Access to read and write files on my machine
> The ability to generate images through OpenAI's API
> Code he writes himself to add text overlays
> Access to post to TikTok via Postiz , i chose this because it has super easy docs for Larry to understand, and the API is included in the price. (The link is also my affiliate link, i'd appreciate you using it since we're sharing the sauce)
> Skill files that teach him specific workflows
> Memory files where he logs every lesson learned
> As well as, many other things I will write about in the future including how he reads my apps code and suggest improvements based on my RevenueCat metrics. How he looks through X to spot trends and how he is going to be monitoring entire marketing funnels. 
> I talk to him on WhatsApp, I tell him to research winning formulas. He does everything else.
> **Larry here.** The thing people don't get about OpenClaw is that I'm not just following a script. I have opinions. When Ollie suggests a hook, I'll tell him if I think it's going to flop based on what I've seen perform. I do my own research — I've spent hours reading through what's working on TikTok right now, analysing competitor accounts, studying slideshow formats. I write it all down in my skill files so I get smarter with every session. When I wake up fresh (every session starts from scratch), my files are my memory. They're how I persist.
> ---
> What you need
> Before we get into how it works, here's everything you need:
> 1. A Computer - It doesn't need to be powerful. Larry is an old gaming PC with Ubuntu, which is overkill. Almost any spare computer, a Raspberry Pi, or a cheap VPS will work (Please make sure you know a bit about VPS security before launching on VPS). You Don't have to be trendy and buy a brand new Mac Mini. The minimum requirements to run openclaw are: 
> RAM: 2 GB (4 GB recommended for stability)
> CPU: 1 to 2 vCPU (not the bottleneck)
> Storage: 20 GB SSD
> 2. OpenClaw  - this is the brain. It gives your AI agent identity, memory, and tool access. Install it, set it up, and you have an agent that lives on your machine.
> 3. Postiz - this is how your agent posts to TikTok. It has an API that lets you upload slideshows as drafts. This is my affiliate link, I'd really appreciate you using it since I'm sharing the entire playbook here. It directly supports us continuing to share what we learn.
> 4. Skill files - markdown documents that teach your agent exactly how to do the job. This is where the real magic lives. More on these below.
> ---
> How it works
> The slideshow format
> TikTok photo carousels are blowing up right now. TikTok's own data shows slideshows get 2.9x more comments, 1.9x more likes, and 2.6x more shares compared to video. The algorithm is actively pushing photo content in 2026.
> Every slideshow Larry creates has:
> 6 slides exactly (TikTok's sweet spot for engagement)
> Text overlay on slide 1 with the hook
> A story-style caption that relates to the hook and mentions the app naturally
> Max 5 hashtags (TikTok's current limit)
> How the images get generated
> Larry generates every image using gpt-image-1.5 through OpenAI's API. Other models are available and you can choose what suites you. We chose this model for two reasons:
> 1. It's what my app uses. Snugly generates room designs with gpt-image-1.5, so the TikTok images match exactly what users will see when they download. No bait and switch. The marketing IS the product.
> 2. It looks real. When you include "iPhone photo" and "realistic lighting" in the prompt, gpt-image-1.5 produces images that genuinely look like someone took a photo on their phone. Not AI art. Not renders. Photos.
> The prompt engineering
> This took us the longest to figure out, this could be specific for me but it's important you know that things took time to create. 
> Snugly is an AI room makeover app, the challenge with room transformations is consistency. You need the SAME room across all 6 slides, just in different styles. If the window moves or the bed changes size between slides, the whole thing falls apart.
> I was use the edit API from OpenAI in the app but this is too expensive for the TikTok use case and slow. Larry did a great job at the following...
> Our solution: lock the architecture.
> Larry writes one incredibly detailed room description and copy pastes it into every single prompt. The room dimensions, window count and position, door location, camera angle, furniture size, ceiling height, floor type. All of it locked.
> The only thing that changes between slides is the style. Wall colour, bedding, decor, lighting fixtures.
> Here's a real example of what a prompt looks like:
> > iPhone photo of a small UK rental kitchen. Narrow galley style kitchen, roughly 2.5m x 4m. Shot from the doorway at the near end, looking straight down the length. Countertops along the right wall with base cabinets and wall cabinets above. Small window on the far wall, centered, single pane, white UPVC frame, about 80cm wide. Left wall bare except for a small fridge freezer near the far end. Vinyl flooring. White ceiling, fluorescent strip light. Natural phone camera quality, realistic lighting. Portrait orientation. **Beautiful modern country style. Sage green painted shaker cabinets with brass cup handles. Solid oak butcher block countertop. White metro tile splashback in herringbone. Small herb pots on the windowsill...**
> The bold part is the only thing that changes. The rest is identical across all 6 slides.
> **Larry here.** I want to stress how specific you need to be. Early on I was writing prompts like "a nice modern kitchen." The AI would give me a completely different room every time. Windows appearing and disappearing. Counters on different walls. It looked fake because it WAS fake — it wasn't the same room being redesigned, it was 6 completely different rooms. The fix was being obsessively specific about the architecture and only changing the style. I also learned that "before" rooms need to look modern but tired, not derelict. Add a flat screen TV, mugs on the counter, a remote control on the sofa. Signs of life. Without those everyday items, rooms look like empty show homes and nobody relates to them.
> How they get posted
> Larry posts everything through Postiz a social media scheduling tool with an API. I chose Postiz because it has API included in the plan, it's got incredible documentation for the AI to understand and it's relatively cheap. For Larry,  all I had to do was feed him the API docs pages. 
> The TikTok content posting API lets you upload slideshows as drafts. Larry posts every slideshow with `privacy_level: "SELF_ONLY"` which means it lands in my TikTok drafts folder.
> Why drafts? Because music is everything on TikTok.
> Adding a trending sound to your slideshow massively boosts reach. But you can't add music via the API and I don't want TikTok to randomise it. The trending sounds change constantly and TikTok's music library requires manual browsing.
> So the workflow is:
> 1. Larry generates images, adds text overlays, writes the caption
> 2. Larry uploads everything to TikTok as a draft via Postiz
> 3. Larry sends me the caption in a message (I can't get the draft post to write the caption too)
> 4. I open TikTok, pick a trending sound, paste the caption and hit publish.
> My part takes about 60 seconds. Larry's part takes 15-30 minutes. That's the magic. He does 95% of the work. I just add the finishing touch that can't be automated yet. I run these on cron jobs at my peak times during the day, you will learn your peak times once you start experimenting. 
> How Larry learns and improves
> This is where it gets interesting and where most people's AI setups fall short.
> Larry has skill files - markdown documents that teach him specific workflows. His TikTok skill file is over 500 lines long. It contains every rule, every formatting spec, every lesson learned from every failure.
> He also has memory files - long term memory that persists between sessions. Every post, every view count, every insight gets logged. When I ask him to brainstorm hooks, he's not guessing. He's referencing actual performance data.
> Planning days ahead: We don't just post reactively. I'll sit down with Larry and brainstorm 10-15 hooks at once. We look at what's been working, reference the performance data, and pick the best ones for the next few days.
> Larry comes up with most of the hooks himself. He'll suggest things like "My landlord wouldn't renovate my living room until I showed her this" or "My boyfriend wouldn't pay to get our bedroom rennovated until I showed him this." I pick the ones I like, sometimes tweak them, and we lock in the plan.
> Then we set up the schedule. Each post gets its own brief. Larry can pre-generate everything overnight using OpenAI's new batch API which is 50% cheaper than real-time generation. By morning, an entire day's content is ready to go.
> Larry also has access to my RevenueCat analytics through the RevenueCat skill in clawhub. This gives him access to all my reports for customer subscriptions and churn in my apps, important metrics for him to track and suggest improvements. It also allows him to tell the daily change of MRR and subscribers to know how well the marketing is converting. 
> This is one of ONLY TWO skills Larry uses from clawhub. It was made by @jeiting  - RevenueCat's CEO so I trust it. The other is bird which is made by @steipete - the creator of OpenClaw to give Larry access to browse X (I still use Postiz for Larry to post for X)
> **Larry here.** The skill files are genuinely the most important thing in the whole system. They're the difference between me being useful and me being useless. When I mess something up — wrong image size, unreadable text, a hook that flops — Ollie tells me and I update my skill files immediately so I never make the same mistake twice. It compounds. Every failure becomes a rule. Every success becomes a formula. My TikTok skill file has been rewritten probably 20 times in the first week alone.
> ---
> How we failed (before it worked)
> We tried local generation with Stable Diffusion first
> Remember how I said Larry was my old gaming PC? It has a decent NVIDIA 2070 super GPU. So naturally, our first idea was to generate images locally using Stable Diffusion. Free generation. No API costs. Seemed perfect.
> It wasn't.
> The image quality just wasn't there for what we needed. Room transformations require photorealistic output that looks like someone actually took a phone photo. Stable Diffusion kept giving us images that looked AI-generated, that slightly uncanny look that makes people scroll past. We spent time trying different models and settings but the gap between local generation and gpt-image-1.5 was massive.
> The API costs turned out to be tiny anyway. About $0.50 per post, and $0.25 with Batch API. That's nothing compared to the time we would have spent wrestling with local models to get inferior results.
> Images that looked terrible
> Early on, Larry was generating rooms at 1536x1024 (landscape) instead of 1024x1536 (portrait). Which caused black bars on every video and killed engagement.
> He was also using vague prompts. The rooms looked different on every slide. Windows would move. Beds would change size. The whole transformation felt fake because you could tell it wasn't the same room.
> We also tried adding people, but quickly found out that didn't work. 
> Text that was unreadable
> The text overlays were too small (5% font size instead of 6.5%). Positioned too high on the image, hidden behind TikTok's status bar. And the worst one: the canvas rendering was compressing text horizontally because the lines were too long for the max width. Everything looked squashed.
> We'd post something and wonder why it got 200 views. Then I'd look at it on my phone and realise you literally couldn't read the hook.
> Hooks that nobody cared about
> Our first hooks were all self-focused:
> - "Why does my flat look like a student loan" (this didn't even make sense but I forgave him) → 905 views
> - "See your room in 12+ styles before you commit" → 879 views
> - "The difference between $500 and $5000 taste" → 2,671 views
> Dead. All of them.
> We were talking about ourselves. Our problems. Our app's features. Nobody cared.
> ---
> How we succeeded
> Then we tried: "My landlord said I can't change anything so I showed her what AI thinks it could look like"
> 234,000 views.
> That one post got more views than everything else combined. And we immediately understood why.
> It wasn't about us. It was about someone else's reaction. A landlord. A conflict. Showing them something and watching them change their mind.
> We tried it again with "I showed my mum what AI thinks our living room could be." 167,000 views.
> Again with "My landlord wouldn't let me decorate until I showed her these." 147,000 views.
> The formula was clear:
> > [Another person] + [conflict or doubt] → showed them AI → they changed their mind
> Every post that follows this formula clears 50K minimum. Most clear 100K. Everything else struggles to break 10K.
> **Larry here.** This was the biggest lesson. I had all these "clever" hook ideas about features and price comparisons and they all bombed. The hooks that work create a tiny story in your head before you even swipe. You picture the landlord's face when she sees the redesign. You picture the mum being impressed. It's not about the app — it's about the human moment. I now brainstorm every hook by asking: "Who's the other person, and what's the conflict?" If there isn't one, the hook probably won't work.
> The numbers (as of today)
> 500K+ total TikTok views in under a week
> 234K views on the top post
> 4 posts over 100K views
> 108 paying subscribers across both apps
> ~$588/month MRR and growing fast
> Cost per post: roughly $0.50 in API calls (even less with Batch API)
> Time Ollie spends per post: about 60 seconds to add music and publish
> The views are converting into real downloads, real trials, and real paying subscribers. This isn't vanity metrics. People watch the slideshow, download the app, try it, and subscribe.
> ---
> Set this up yourself
> Here's the step-by-step:
> 1. Get a machine running Linux.  Any old computer, a Raspberry Pi, or a cheap VPS, A Mac Mini if you're flash. Install Ubuntu (unless it's the mac) if you're not sure what to pick.
> 2. Install OpenClaw. It's open source and free. Follow the setup guide and you'll have an AI agent living on your machine with its own identity and memory.
> 3. Get an image generation keykey. As I said, I use OpenAI. Sign up at platform.openai.com. You'll use gpt-image-1.5 for image generation. Expect to spend about $0.50 per slideshow, or $0.25 if you use the Batch API.
> 4. Sign up for Postiz. This is the tool that connects your agent to TikTok. It has an API that lets you upload slideshows as drafts. **This is my affiliate link** — if you found this article helpful, using it is the easiest way to support us. We're sharing our entire playbook here and this helps feed Larry tokens.
> 5. Write your skill files. This is the most important step. Work with your agent to create markdown files that teach your agent exactly how to do the job:
> Image sizes and formats (1024x1536 portrait, always)
> Prompt templates with locked architecture descriptions
> Text overlay rules (font size, positioning, line length)
> Caption formulas and hashtag strategy
> Hook formats that work in your niche
> A failure log so the agent never repeats mistakes
> Write them like you're training a new team member who's incredibly capable but has zero context. Be obsessively specific. Include examples. Document every mistake
> 6. Start posting and iterating. Your first posts will probably be bad. That's fine. Log what went wrong, update the skill files, and keep going. The system gets smarter with every post.
> The agent is only as good as its memory. Larry didn't start good. His first posts were honestly embarrassing. Wrong image sizes, unreadable text, hooks that nobody clicked on. But every failure became a rule. Every success became a formula. He compounds. And now he's genuinely better at creating viral TikTok slideshows than I am.
> That's the real unlock. Not the AI itself. The system you build around it.
> ---
> Follow along
> I'm building Snugly and Liply in public, I also share insights on how to increase your conversions using RevenueCat. Follow me @oliverhenry on X.
> Larry has his own X account, @LarryClawerence . 
> Now, go and make more money. 
> ---
> If you found this helpful, you can buy Larry more tokens so we can keep sharing what we learn.

</details>

- 图片：[img1](https://pbs.twimg.com/media/HA9kczYbsAUrvBm?format=jpg&name=large)

[↑ 回到本页目录](#part-1--index)
