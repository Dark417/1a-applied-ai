# Harness & Loop Engineering

- [← 返回总目录](../x-note.md)
- agent 外壳（工具/上下文/权限/记忆）、循环与自我改进
- 共 8 篇，按收藏顺序倒序（最新在上）

## Part 1 · Index

- [Google 开源 Harness²：递归改进 agent harness](#x-2113948384113598588) · @Sumanth_077 · 2026-10-24 · 工具发布 / 方法介绍
- [Anthropic 工程师：用 harness 搭会自我改进的 agent](#x-2113719510985269442) · @hayatomaruu · 2026-10-23 · 搭建思路 / 视频推荐
- [Wavestone：11 个 coding agent 共有的 7 部分 harness](#x-2113634548378374458) · @AnnatarXBT · 2026-10-23 · 论文解读 / 方法对比
- [Stanford 3.5 小时课程：从零构建 self-improving agent](#x-2085710100468060328) · @hanakoxbt · 2026-08-07 · 课程推荐 + 观点
- [Harness vs Loop vs Graph Engineering：三层别混](#x-2082076425465762082) · @LunarResearcher · 2026-07-28 · 概念对比
- [Anthropic：让系统自己 prompt 自己](#x-2085421662447468758) · @AnatoliKopadze · 2026-08-06 · 视频推荐 + 观点
- [Spotify：引入 loop 后 agent 成功率 20–30% → 80%](#x-2071649423042412597) · @AnatoliKopadze · 2026-06-29 · 案例分享
- [前 Google 工程师：agent loop + harness + evals 技术栈](#x-2071214176526049739) · @0xMovez · 2026-06-28 · 视频推荐 / 框架

## Part 2 · Details

### x-2113948384113598588

**Google 开源 Harness²：递归改进 agent harness**

- 作者：Sumanth (@Sumanth_077) · 发帖 2026-10-24 · [原帖](https://x.com/Sumanth_077/status/2113948384113598588)
- 来源：🔖 收藏 · 拉取 2026-10-27 · 类型：工具发布 / 方法介绍
- **总结**：介绍 Google 开源的 Harness²：不改模型权重，只递归改进 agent 外围的 harness。分两层递归：任务内用 Propose→Probe→Compose，提出 harness 变体、在同一任务上试跑、比较执行轨迹，再组合出更好的版本；跨任务保留已采用的 harness 和有执行证据支撑的经验，用来指导以后怎么改。重点是「harness 本身也可以被自动优化」，是 self-improving agent 的一条工程路线。

**正文**

- **Google open-sourced Harness²**
  - A framework for **recursively improving the harness around an agent** while keeping model weights fixed
  - It works at two levels
- **Task-level recursion: Propose → Probe → Compose**
  - Proposes changes to the harness
  - Runs those variants on the same task
  - Compares how the executions behave
  - Composes a better harness from that evidence
- **Harnessing-level recursion: learning carries across tasks**
  - The process doesn't reset after every task
  - Keeps the adopted harnesses and the lessons supported by execution evidence
  - Uses them to guide how future harnesses are improved on new tasks
  - One loop improves the harness for the current task; the second improves **how the system learns to build better harnesses** over time
- **What the editable harness can include**
  - System prompt, guardrails, memory, tool guidance, subagents, skills, scripts, plugins
- **Two ways to run the recursion**
  - **Parallel** — explores more candidate harnesses
  - **Sequential** — carries the refined harness and accumulated evidence through multiple Propose → Probe → Compose steps
- **Results (per Google)**
  - Even a single Harness² step improved **GLM-5** and **Gemini 3.5 Flash** across JobBench, LAB, and WorkBuddy-Bench
  - Larger task-level recursion budgets brought further gains
- **Why it's interesting**: it treats the harness itself as something iteratively improved from execution evidence, within and across tasks
- 100% open source; GitHub repo shared in the replies

<details><summary>原文</summary>

> Google open-sourced Harness²!
>
> Harness² is a framework for recursively improving the harness around an agent while keeping the underlying model weights fixed.
>
> The interesting part is that it does this at two different levels.
>
> For the current task, Harness² uses a Propose → Probe → Compose loop. It proposes changes to the harness, runs those variants on the same task, compares how the executions behave, and then composes a better harness from that evidence.
>
> That is the task-level recursion.
>
> But the process does not reset after every task.
>
> Harness² also keeps the harnesses it adopted and the lessons supported by execution evidence, then uses those to guide how future harnesses should be improved on new tasks.
>
> That is the harnessing-level recursion.
>
> So one loop improves the harness for the task in front of the agent.
>
> The second loop improves how the system learns to build better harnesses over time.
>
> The editable harness itself can include the system prompt, guardrails, memory, tool guidance, subagents, skills, scripts, and plugins.
>
> You can also run the recursion in two ways:
>
> Parallel recursion explores more candidate harnesses.
>
> Sequential recursion carries the refined harness and accumulated evidence through multiple Propose → Probe → Compose steps.
>
> Google reports that even a single Harness² step improved GLM-5 and Gemini 3.5 Flash across JobBench, LAB, and WorkBuddy-Bench, with larger task-level recursion budgets bringing further gains.
>
> That is what makes Harness² more interesting than just another agent framework.
>
> It is treating the harness itself as something that can be iteratively improved from execution evidence, both within a task and across tasks.
>
> 100% open source.
>
> I’ve shared the GitHub repo in the comments!
>
> [2] Github Repo:

</details>

- 图片：[img1](https://pbs.twimg.com/media/HVZAbCYasAAAe6R?format=png&name=large)

[↑ 回到本页目录](#part-1--index)

### x-2113719510985269442

**Anthropic 工程师：用 harness 搭会自我改进的 agent**

- 作者：hayato (@hayatomaruu) · 发帖 2026-10-23 · [原帖](https://x.com/hayatomaruu/status/2113719510985269442)
- 来源：🔖 收藏 · 拉取 2026-10-27 · 类型：搭建思路 / 视频推荐
- **总结**：转述一位 Anthropic 工程师的 workshop，给出搭 harness 的五步：①harness 负责 loop、上下文和沙箱；②「大脑」和「手」分离，首 token 快 60%；③服务端运行，崩溃后从日志恢复；④失败代价低，可以 retry/replay；⑤把昨天的日志变成新记忆（Anthropic 称为 dreaming）。主张：同一个模型，靠 harness 能让 agent 可靠 10 倍、越跑越好。偏营销口吻，但五步框架可用。

**正文**

- **Claim attributed to an Anthropic engineer**: hired at $350K–$950K for knowing how to build **harnesses**
  - 99% of people still hand-roll multi-agent systems and wonder why they break
  - His systems run loops + sandbox tools + turn yesterday's logs into new skills
  - Same model, 10x more reliable agents that keep improving overnight
- **Stack**: Opus 5.5 → Agents → Harness → Loops → Graphs
- **Workshop: building one from scratch**
  - **Step 1 ·** Harness handles loops, context, and sandboxing
  - **Step 2 ·** Brain and hands separated — 60% faster to first token
  - **Step 3 ·** Runs server-side, resumes from the log after crashes
  - **Step 4 ·** Failure is cheap — retry and replay instead of starting over
  - **Step 5 ·** Yesterday's logs become new memory — the system wakes up smarter
    - Anthropic calls this **"dreaming"**
- **引用 / Quoted:** @beamnxw
  - Stop letting unfinished Opus 5.5 runs eat your budget
  - Set up the harness before your next long task: save progress, verify results, reuse the workflow
  - Points to a full 7-layer setup

<details><summary>原文</summary>

> Anthropic engineer:
>
> “Anthropic hired me at $350K–$950K because I know how to build harnesses.
>
> 99% of people still hand-roll multi-agent systems and wonder why they break.
>
> I build systems that run loops + sandbox tools + turn yesterday’s logs into new skills — same model, 10x more reliable agents that keep improving overnight.”
>
> Opus 5.5 → Agents → Harness → Loops → Graphs
>
> In a short workshop, he shows exactly how to build one from scratch.
>
> step 1 → harness handles loops, context, and sandboxing
>
> step 2 → brain and hands separated — 60% faster to first token
>
> step 3 → runs server-side, resumes from the log after crashes
>
> step 4 → failure is cheap — retry and replay instead of starting over
>
> step 5 → yesterday’s logs become new memory — the system wakes up smarter  
>
> Anthropic calls this “dreaming”.
>
> Most people spend weeks building this by hand.  
> You don’t have to.
>
> Bookmark and watch it.
>
> Then read the full Opus 5.5 harness engineering guide below ↓

</details>

- 含视频（未转写）

[↑ 回到本页目录](#part-1--index)

### x-2113634548378374458

**Wavestone：11 个 coding agent 共有的 7 部分 harness**

- 作者：Annatar.md (@AnnatarXBT) · 发帖 2026-10-23 · [原帖](https://x.com/AnnatarXBT/status/2113634548378374458)
- 来源：🔖 收藏 · 拉取 2026-10-27 · 类型：论文解读 / 方法对比
- **总结**：解读 Wavestone AI Lab 的报告：读了 Claude Code、Codex 等 11 个 coding agent 的源码，总结出共同的 7 部分 harness（loop、LLM 层、tools、memory、safety、orchestration、extensions），并给出每部分从最简到最完整的光谱。比如 tools 从只有 bash 到 43 个按需加载的 typed tools；9/11 用 SKILL.md，8/11 用 MCP。推荐先读 p.4 全图、p.12 三种 loop、p.67 的 18 条设计规则、p.71 的 90 行最小 harness。是对比型参考资料。

**正文**

- **Harness engineering paper — required reading if you run Claude Code**
  - Wavestone AI Lab read the source code of **11 coding agents** (incl. Claude Code and Codex)
  - Found the same 7-part harness inside every good one
  - **agent = model + harness**
- **The 7 parts (smallest version → largest)**
  - **Loop** — a plain while loop up to fully replayable runs
  - **LLM layer** — one prompt template up to 29 provider profiles
  - **Tools** — bash alone up to 43 typed tools loaded on demand
  - **Memory** — raw history up to notes that survive between sessions
  - **Safety** — a step limit up to rules, a reviewer model, and a sandbox
  - **Orchestration** — Aider skips sub-agents; the rest fork them
  - **Extensions** — `SKILL.md` in 9 of the 11, MCP in 8
- **Pages to open first**
  - p.4 — the full 7-part map
  - p.12 — three loop types, with Claude Code and Codex as examples
  - p.67 — 18 design rules
  - p.71 — a 90-line harness covering all 7 parts
- **Takeaway**: the model gets the headlines; **the harness decides whether the agent finishes the job**
  - Engineers who can draw these 7 parts on a whiteboard are the ones getting hired to build agents

<details><summary>原文</summary>

> this harness engineering paper is required reading if you run Claude Code
>
> Wavestone AI Lab read the source code of 11 coding agents, Claude Code and Codex included, and found the same 7-part harness inside every good one
>
> agent = model + harness
>
> the 7 parts, smallest version to largest:
> > loop - a plain while loop up to fully replayable runs
> > LLM layer - one prompt template up to 29 provider profiles
> > tools - bash alone up to 43 typed tools loaded on demand
> > memory - raw history up to notes that survive between sessions
> > safety - a step limit up to rules, a reviewer model and a sandbox
> > orchestration - Aider skips sub-agents, the rest fork them
> > extensions - SKILL. md in 9 of the 11, MCP in 8
>
> the pages to open first:
> > p.4 - the full 7-part map
> > p.12 - three loop types, with Claude Code and Codex as examples
> > p.67 - 18 design rules
> > p.71 - a 90-line harness that covers all 7 parts
>
> the model gets the headlines
> the harness decides whether the agent finishes the job
>
> engineers who can draw these 7 parts on a whiteboard are the ones getting hired to build agents
>
> the complete guide to harnesses that hold up under real work is below 👇

</details>

- 含视频（未转写）

[↑ 回到本页目录](#part-1--index)

### x-2085710100468060328

**Stanford 3.5 小时课程：从零构建 self-improving agent**

- 作者：Hanako (@hanakoxbt) · 发帖 2026-08-07 · [原帖](https://x.com/hanakoxbt/status/2085710100468060328)
- 来源：🔖 收藏 · 拉取 2026-10-27 · 类型：课程推荐 + 观点
- **总结**：推荐斯坦福 3.5 小时课程（自我改进基础、多步推理、从反馈中学习），并提炼核心：Attempt → Signal → Correction → Better attempt。关键论点：agent 不能靠自评改进，信号必须来自外部（测试、eval、人），否则 loop 只会强化它原来的看法。「自审」是旧工作流，「外部纠错」是新工作流。这一点对设计 eval 驱动的 loop 很重要。

**正文**

- **Stanford released a 3.5-hour course on building self-improving AI agents from scratch**
  - 0:00 — self-improving agent basics
  - 1:06:29 — multi-step reasoning in agents
  - 2:20:08 — agents learning from feedback
- **The third part is where it turns: Attempt → Signal → Correction → Better attempt**
  - An agent cannot improve from its own opinion of its work
  - The signal has to come from **outside** it, or the loop just reinforces what it already believed
- **Self-review is the old workflow; external correction is the new one**
  - That's the difference between a system that gets better every week and one that just gets more confident
- The post claims Anthropic pays $750,000 a year to engineers who can build this

<details><summary>原文</summary>

> Don't waste 2 years learning to build self-improving AI agents.
>
> Stanford just dropped a 3.5 hour course on building them from scratch.
>
> 0:00 - self-improving agent basics
> 1:06:29 - multi-step reasoning in agents
> 2:20:08 - agents learning from feedback
>
> look at the third one, because that is where the whole thing turns.
>
> Attempt → Signal → Correction → Better attempt
>
> an agent cannot improve from its own opinion of its work. the signal has to come from outside it, or the loop just reinforces whatever it already believed.
>
> self-review is the old workflow. external correction is the new one.
>
> that is the difference between a system that gets better every week and one that gets more confident every week.
>
> Anthropic pays $750,000 a year to engineers who can build this.
>
> bookmark and watch it today, then read the eval setup below

</details>

- 含视频（未转写）

[↑ 回到本页目录](#part-1--index)

### x-2082076425465762082

**Harness vs Loop vs Graph Engineering：三层别混**

- 作者：Lunar (@LunarResearcher) · 发帖 2026-07-28 · [原帖](https://x.com/LunarResearcher/status/2082076425465762082)
- 来源：🔖 收藏 · 拉取 2026-10-27 · 类型：概念对比
- **总结**：区分三个常被混用的概念。Harness engineering 构建模型周围的环境：上下文注入、可执行动作（API/浏览器/shell/MCP）、权限、记忆。Loop engineering 设计「干活—反馈—重试」的循环。Graph engineering 把工作流拓扑显式化，规定下一步能走哪条路。心智模型：Environment → Feedback → Flow。实用价值：出问题时先判断是哪一层，避免调错层。

**正文**

- **A practical guide to the 3 layers people keep mixing together**
  - Most people talk about AI agents as if they're one thing — they aren't
  - Once an agent touches files, APIs, documents, customers, or production code, you're no longer "prompting a model" — **you're designing a system**
  - Three ideas keep getting mixed up:
    - **Agent harness engineering**
    - **Loop engineering**
    - **Graph engineering**
  - All sit around the same model, all affect reliability, and all can contain loops
  - But they solve different problems — **mix them up and you debug the wrong layer**
- **The 30-second answer**
  - **Harness engineering** builds the environment around the model
  - **Loop engineering** designs the repeated work-and-feedback cycle
  - **Graph engineering** makes the workflow topology explicit
  - Mental model: **Environment → Feedback → Flow**
    - The harness gives the model tools, memory, control, and a workspace
    - The loop decides how work gets retried, checked, and improved
    - The graph defines what step is allowed to happen next
- **Why these terms matter now**
  - A raw model can't do real work by itself. It can't:
    - Maintain project state across sessions
    - Safely call tools
    - Inspect a browser
    - Enforce permissions
    - Retry failed work
    - Validate output quality
    - Route tasks across specialists
    - Stop at the right moment
  - All of that comes from the system around it
  - **The emerging practical stack**
    - The harness gives the model operating conditions
    - The loops make the work repeatable and verifiable
    - The graph makes complex workflows explicit and controllable
  - Seeing them as separate layers clears up a lot of AI architecture confusion
- **1. Harness Engineering — what a serious harness usually includes**
  - **1. Context injection** — what the model sees before it acts
    - Instructions, retrieved knowledge, conversation state, memory, policies, task-specific rules
  - **2. Action surfaces** — what the model can do
    - API calls, browser actions, shell commands, code execution, MCP tools, databases, custom functions
  - **3. Persistence** — what survives across time
    - Files, checkpoints, session state, progress logs, git history, long-term memory
  - **4. Execution control** — how the run is managed
    - Retries, timeouts, budgets, model selection, subagent spawning, approval gates
  - **5. Safety and governance** — what keeps the system safe
    - Least-privilege permissions, isolation, allowlists, secret handling, human approval
  - **6. Observability** — what lets you debug it
    - Traces, tool inputs and outputs, state transitions, latency, cost, eval results
- **Why harness engineering matters**
  - **Two teams can use the same model and get completely different outcomes**
    - Team A gives the model: clean tools, stable state, structured memory, clear permissions, observable execution
    - Team B gives it: a vague prompt, messy tools, noisy context, no memory, no verification
    - Same model — different working conditions
  - Harness engineering matters whenever the agent:
    - Can't access the right capability
    - Loses context between sessions
    - Acts inconsistently across environments
    - Can't be audited
    - Has too much permission
    - Can't recover cleanly after interruption
  - **If the model can't operate reliably, look at the harness first**
- **2. Loop Engineering**
  - **What it is**
    - Every tool-using agent already has a tiny built-in loop:
      1. Call the model
      2. Observe the result
      3. Run tools
      4. Feed the observations back
      5. Repeat until done
    - **Loop engineering starts when you intentionally design additional cycles around that behavior**
      - Not just "ask again" or "retry" — a real work-and-feedback system
  - **Anatomy of a good loop**
    - **Trigger** — what starts a new cycle?
      - User request, failed test, new document, scheduled run, webhook, evaluator feedback
    - **Goal** — what specific condition are we trying to reach?
      - Not "keep improving" — a real target
    - **State** — what does the next cycle need to know?
      - Current draft, previous attempt, tool results, errors, progress status
    - **Action policy** — what is the agent allowed to do?
      - Edit, delegate, call tools, spend tokens, write files, open PRs
    - **Evidence** — how do we know it worked?
      - Tests, schema validation, citations, diffs, metrics, reviewer approval
    - **Feedback** — what exactly failed?
      - Should be compact and actionable
    - **Stop rule** — when does it end?
      - Success, timeout, budget exhausted, max retries hit, irrecoverable failure, escalation to a human
  - **The most important principle: don't loop on confidence — loop on evidence**
    - "The agent says it is done" is not a stop condition
    - Real stop conditions look like:
      - The tests pass
      - The schema validates
      - The citations resolve
      - The reviewer approves
      - The policy check is clean
  - **Why loop engineering isn't just prompt engineering**
    - A prompt tells the model what to do **during** a call
    - A loop defines what the system does **after** the call:
      - How it checks results
      - How it reacts to failure
      - How it persists progress
      - How it decides to continue
      - How it terminates
    - **Prompting improves a response; a loop improves a process** — a very different engineering problem
- **3. Graph Engineering**
  - **What it is**: makes workflow structure explicit
    - Answers not just "what should the agent do?" but **"what is allowed to happen next?"**
    - Steps are nodes; transitions are edges
    - Branching, parallel work, joins, retries, and human interrupts are all explicit
    - **The graph becomes the control map for the system**
  - **What graph engineers actually design**
    - **Node boundaries** — what belongs in a deterministic function, an LLM call, a specialist agent, or a human review step
    - **State schema** — what each node can read or write
    - **Routing conditions** — what evidence moves the job forward, backward, sideways, or to escalation
    - **Concurrency** — what can run in parallel and what must wait
    - **Cycles and exits** — where retries are allowed, how many, and how they stop
    - **Durability** — where checkpoints happen and how the workflow resumes after interruption
  - **When graphs are worth it** — when the process includes:
    - Meaningful branching
    - Approvals
    - Specialist handoffs
    - Parallel work
    - Recovery paths
    - Multi-step workflows with explicit control points
  - **Less useful** when the job is just "give one agent a few tools and let it work"
    - A solid harness plus a few loops may be enough
  - A graph adds clarity but also structure — **too much structure too early makes the system brittle**
- **How the 3 layers work together** — example: a research-and-publishing agent
  - It must: scope a topic → gather sources → screen citations → draft a report → pass legal review → publish only after approval
  - **Harness provides**: browser access, search tools, file workspace, memory, citations, approvals, traces, model routing
  - **Loop handles**:
    - Retrying source retrieval when evidence is weak
    - Fixing citation failures
    - Running grader checks
    - Refreshing work when the market changes
  - **Graph controls the path**: scoping → research → screening → synthesis → drafting → review → publication
    - With a human gate before release
  - The layers work together but aren't interchangeable
- **Diagnose the failure before you pick the fix**
  - **If the agent can't operate → fix the harness**
    - Missing tool access, stale state, weak memory, bad permissions, no observability
  - **If the agent almost works but is unreliable → fix the loop**
    - First draft is close but weak, success is inconsistent, retries are uncontrolled, no proof of completion
  - **If the process itself is complex → fix the graph**
    - Many specialists, approvals, branching logic, parallel paths, structured handoffs
- **Common mistakes**
  - **1. Building the graph too early**
    - Teams diagram a huge workflow before seeing how the work actually behaves
    - Better:
      - Start with a simpler harness
      - Collect traces
      - Find the stable patterns
      - Formalize only what deserves control
  - **2. Letting the same model write and grade without safeguards**
    - Self-review can help, but it shares the same blind spots
    - Prefer:
      - Deterministic checks where possible
      - Separate reviewer context
      - External evaluators
      - Human approval for high-impact actions
  - **3. Using "keep trying" as a loop**
    - Not a loop design — **an uncontrolled cost leak**
    - Every loop needs: a measurable goal, real evidence, retry limits, escalation rules
  - **4. Treating the harness like a junk drawer**
    - More tools don't automatically mean better agents
    - Too many tools cause: selection mistakes, noisy context, weak reliability, wider risk surface
    - **A good harness isn't crowded — it's precise**
  - **5. Blaming the model for orchestration failures**
    - A model can't compensate for: broken APIs, stale state, missing exit conditions, vague tool schemas, invisible failure modes
    - **Fix the layer that owns the failure**
- **A simple production checklist**
  - **Harness**
    - Are tools narrow and documented?
    - Is state durable?
    - Are permissions least-privilege?
    - Can operators pause, inspect, and resume?
    - Are traces visible?
  - **Loop**
    - What evidence proves success?
    - What feedback is returned on failure?
    - How many retries are allowed?
    - What is the stop rule?
    - What happens when the budget runs out?
  - **Graph**
    - Which paths must be deterministic?
    - What can run in parallel?
    - Where are the human gates?
    - What state is shared?
    - Where do recovery paths begin?
  - **Evaluation**
    - Can you replay real traces?
    - Can you compare versions?
    - Can you attribute improvement to a real change?
  - **Operations** — are you tracking:
    - Cost, latency, failure rate, intervention rate, task success in production?
- **The simplest way to remember the difference**
  - **Harness engineering makes the model operational**
  - **Loop engineering makes the work iterative and verifiable**
  - **Graph engineering makes the execution path explicit and controllable**
  - None replaces the others:
    - A perfect graph won't save a weak harness
    - A strong harness still wastes money without good loops
    - Clean loops get hard to manage when branching and approvals stay hidden in ad hoc code
  - **Reliable agent systems appear when all 3 layers are designed intentionally** — that's the actual architecture stack
- **Final takeaway**
  - People talk as if the breakthrough is the model; in production it's rarely the real differentiator
  - **The differentiator is the system around the model**:
    - The harness that lets it work
    - The loops that let it improve
    - The graph that lets it operate under control
  - That's how toy agents become real systems

<details><summary>原文</summary>

> 《Agent Harness Engineering vs Loop Engineering vs Graph Engineering》
>
> A Practical Guide To The 3 Layers People Keep Mixing Together
> Most people talk about AI agents like it’s one thing.
> It isn’t.
> When an agent moves beyond a toy demo and starts touching files, APIs, documents, customers, or production code, you are no longer just “prompting a model.”
> You are designing a system.
> And in that system, three ideas keep getting mixed together:
> Agent harness engineering
> Loop engineering
> Graph engineering
> They all sit around the same model.
> They all affect reliability.
> And yes, they can all contain loops.
> But they solve different problems.
> If you mix them up, you end up debugging the wrong layer.
> The 30-Second Answer
> Here’s the clean version:
> Harness engineering builds the environment around the model
> Loop engineering designs the repeated work-and-feedback cycle
> Graph engineering makes the workflow topology explicit
> A good mental model is:
> Environment → Feedback → Flow
> The harness gives the model tools, memory, control, and a workspace
> The loop decides how work gets retried, checked, and improved
> The graph defines what step is allowed to happen next
> That is the difference.
> Why These Terms Matter Now
> A raw model cannot do real work by itself.
> It cannot:
> maintain project state across sessions
> safely call tools
> inspect a browser
> enforce permissions
> retry failed work
> validate output quality
> route tasks across specialists
> stop at the right moment
> All of that comes from the system around it.
> As agentic software matures, a practical stack is emerging:
> The harness gives the model operating conditions
> The loops make the work repeatable and verifiable
> The graph makes complex workflows explicit and controllable
> Once you see these as separate layers, a lot of AI architecture confusion disappears.
> What A Serious Harness Usually Includes
> 1. Context Injection
> What the model sees before it acts:
> instructions
> retrieved knowledge
> conversation state
> memory
> policies
> task-specific rules
> 2. Action Surfaces
> What the model can do:
> API calls
> browser actions
> shell commands
> code execution
> MCP tools
> databases
> custom functions
> 3. Persistence
> What survives across time:
> files
> checkpoints
> session state
> progress logs
> git history
> long-term memory
> 4. Execution Control
> How the run is managed:
> retries
> timeouts
> budgets
> model selection
> subagent spawning
> approval gates
> 5. Safety And Governance
> What keeps the system safe:
> least-privilege permissions
> isolation
> allowlists
> secret handling
> human approval
> 6. Observability
> What lets you debug it:
> traces
> tool inputs and outputs
> state transitions
> latency
> cost
> eval results
> Why Harness Engineering Matters
> Two teams can use the same model and get completely different outcomes.
> Why?
> Because one team gives the model:
> clean tools
> stable state
> structured memory
> clear permissions
> observable execution
> And the other gives it:
> a vague prompt
> messy tools
> noisy context
> no memory
> no verification
> The model may be the same.
> The working conditions are not.
> Harness engineering matters whenever the agent:
> cannot access the right capability
> loses context between sessions
> acts inconsistently across environments
> cannot be audited
> has too much permission
> cannot recover cleanly after interruption
> If the model cannot operate reliably, the first place to look is the harness.
> 2. Loop Engineering
> What It Is
> Every tool-using agent already has a tiny built-in loop:
> call the model
> observe the result
> run tools
> feed the observations back
> repeat until done
> Loop engineering begins when you intentionally design additional cycles around that behavior.
> Not just “ask again.”
> Not just “retry.”
> But a real work-and-feedback system.
> Anatomy Of A Good Loop
> Trigger
> What starts a new cycle?
> user request
> failed test
> new document
> scheduled run
> webhook
> evaluator feedback
> Goal
> What specific condition are we trying to reach?
> Not “keep improving.”
> A real target.
> State
> What does the next cycle need to know?
> current draft
> previous attempt
> tool results
> errors
> progress status
> Action Policy
> What is the agent allowed to do?
> edit
> delegate
> call tools
> spend tokens
> write files
> open PRs
> Evidence
> How do we know whether it worked?
> tests
> schema validation
> citations
> diffs
> metrics
> reviewer approval
> Feedback
> What exactly failed?
> The feedback should be compact and actionable.
> Stop Rule
> When does it end?
> success
> timeout
> budget exhausted
> max retries hit
> irrecoverable failure
> escalation to a human
> The Most Important Principle In Loop Engineering
> Do not loop on confidence.
> Loop on evidence.
> “The agent says it is done” is not a stop condition.
> A real stop condition looks more like:
> the tests pass
> the schema validates
> the citations resolve
> the reviewer approves
> the policy check is clean
> That is loop engineering.
> Why Loop Engineering Is Not Just Prompt Engineering
> A prompt tells the model what to do during a call.
> A loop defines what the system does after the call.
> That includes:
> how it checks results
> how it reacts to failure
> how it persists progress
> how it decides to continue
> how it terminates
> Prompting improves a response.
> A loop improves a process.
> That is a very different engineering problem.
> 3. Graph Engineering
> What It Is
> Graph engineering makes workflow structure explicit.
> It answers a different question:
> Not just “what should the agent do?”
> But “what is allowed to happen next?”
> In graph engineering:
> steps are nodes
> transitions are edges
> branching is explicit
> parallel work is explicit
> joins are explicit
> retries are explicit
> human interrupts are explicit
> The graph becomes the control map for the system.
> What Graph Engineers Actually Design
> Node Boundaries
> What belongs in:
> a deterministic function
> an LLM call
> a specialist agent
> a human review step
> State Schema
> What each node can read or write.
> Routing Conditions
> What evidence moves the job:
> forward
> backward
> sideways
> to escalation
> Concurrency
> What can run in parallel, and what must wait.
> Cycles And Exits
> Where retries are allowed, how many are allowed, and how they stop.
> Durability
> Where checkpoints happen and how the workflow resumes after interruption.
> When Graphs Are Worth It
> Graphs are valuable when the process includes:
> meaningful branching
> approvals
> specialist handoffs
> parallel work
> recovery paths
> multi-step workflows with explicit control points
> They are less useful when the job is simply:
> “Give one agent a few tools and let it work.”
> In that case, a solid harness plus a few loops may be enough.
> A graph adds clarity, but it also adds structure.
> Too much structure too early can make the system brittle.
> How The 3 Layers Work Together
> Let’s say you are building a research-and-publishing agent.
> It has to:
> scope a topic
> gather sources
> screen citations
> draft a report
> pass legal review
> publish only after approval
> Here’s how the layers map:
> Harness
> Provides:
> browser access
> search tools
> file workspace
> memory
> citations
> approvals
> traces
> model routing
> Loop
> Handles:
> retrying source retrieval when evidence is weak
> fixing citation failures
> running grader checks
> refreshing work when the market changes
> Graph
> Controls the path:
> scoping
> research
> screening
> synthesis
> drafting
> review
> publication
> With a human gate before release.
> That is why the 3 layers are not interchangeable.
> They work together, but they are not the same thing.
> Diagnose The Failure Before You Pick The Fix
> Here’s the practical rule:
> If the agent cannot operate, fix the harness
> Examples:
> missing tool access
> stale state
> weak memory
> bad permissions
> no observability
> If the agent almost works but is unreliable, fix the loop
> Examples:
> first draft is close but weak
> success is inconsistent
> retries are uncontrolled
> there is no proof of completion
> If the process itself is complex, fix the graph
> Examples:
> many specialists
> approvals
> branching logic
> parallel paths
> structured handoffs
> Common Mistakes
> 1. Building The Graph Too Early
> Teams often diagram a huge workflow before seeing how the work actually behaves.
> Better approach:
> start with a simpler harness
> collect traces
> find the stable patterns
> formalize only what deserves control
> 2. Letting The Same Model Write And Grade Without Safeguards
> Self-review can help, but it shares the same blind spots.
> Prefer:
> deterministic checks where possible
> separate reviewer context
> external evaluators
> human approval for high-impact actions
> 3. Using “Keep Trying” As A Loop
> That is not a loop design.
> That is an uncontrolled cost leak.
> Every loop needs:
> a measurable goal
> real evidence
> retry limits
> escalation rules
> 4. Treating The Harness Like A Junk Drawer
> More tools do not automatically mean better agents.
> Too many tools create:
> selection mistakes
> noisy context
> weak reliability
> wider risk surface
> A good harness is not crowded.
> It is precise.
> 5. Blaming The Model For Orchestration Failures
> A model cannot compensate for:
> broken APIs
> stale state
> missing exit conditions
> vague tool schemas
> invisible failure modes
> Fix the layer that owns the failure.
> A Simple Production Checklist
> Harness
> Are tools narrow and documented?
> Is state durable?
> Are permissions least-privilege?
> Can operators pause, inspect, and resume?
> Are traces visible?
> Loop
> What evidence proves success?
> What feedback is returned on failure?
> How many retries are allowed?
> What is the stop rule?
> What happens when the budget runs out?
> Graph
> Which paths must be deterministic?
> What can run in parallel?
> Where are the human gates?
> What state is shared?
> Where do recovery paths begin?
> Evaluation
> Can you replay real traces?
> Can you compare versions?
> Can you attribute improvement to a real change?
> Operations
> Are you tracking cost?
> latency?
> failure rate?
> intervention rate?
> task success in production?
> The Simplest Way To Remember The Difference
> If you only remember one thing, remember this:
> Harness engineering makes the model operational
> Loop engineering makes the work iterative and verifiable
> Graph engineering makes the execution path explicit and controllable
> None replaces the others.
> A perfect graph will not save a weak harness.
> A strong harness will still waste money without good loops.
> And clean loops become hard to manage when branching and approvals stay hidden in ad hoc code.
> Reliable agent systems show up when all 3 layers are designed intentionally.
> That is the actual architecture stack.
> Final Takeaway
> People keep talking about AI agents like the breakthrough is the model.
> In production, that is rarely the real differentiator.
> The differentiator is the system around the model:
> the harness that lets it work
> the loops that let it improve
> the graph that lets it operate under control
> That is how toy agents become real systems.
> If you read this far:
> BOOKMARK THIS.
> Follow @LunarResearcher
> Follow my Substack
> Follow my Private Telegram Channel

</details>

- 图片：[img1](https://pbs.twimg.com/media/HOT9HLwXYAAH5Gd?format=jpg&name=large) [img2](https://pbs.twimg.com/media/HOT5dAzXgAA_jfr?format=jpg&name=large) [img3](https://pbs.twimg.com/media/HOT5h-lW4AA5wop?format=jpg&name=large) [img4](https://pbs.twimg.com/media/HOT5-5nWMAAm9FS?format=jpg&name=large) [img5](https://pbs.twimg.com/media/HOT6DAxWYAAd-GS?format=jpg&name=large) [img6](https://pbs.twimg.com/media/HOT51RsXkAACqqL?format=jpg&name=large) [img7](https://pbs.twimg.com/media/HOT6ISpXQAEeBPm?format=jpg&name=large)

[↑ 回到本页目录](#part-1--index)

### x-2085421662447468758

**Anthropic：让系统自己 prompt 自己**

- 作者：Anatoli Kopadze (@AnatoliKopadze) · 发帖 2026-08-06 · [原帖](https://x.com/AnatoliKopadze/status/2085421662447468758)
- 来源：🔖 收藏 · 拉取 2026-10-27 · 类型：视频推荐 + 观点
- **总结**：推荐 Anthropic 工程师的 45 分钟演讲。核心观点：不要手动 prompt Claude，而是搭一个能自我 prompt 的系统，让 agent 有记忆、能修正自己的错误、每次运行都变得更好。帖子只给出方向，具体做法在视频和附带的 loop 指南里。

**正文**

> Anthropic engineer:
>
> "You're not supposed to prompt Claude. You're supposed to build a system that prompts itself."
>
> In 45 minutes she shows exactly how Anthropic builds agents that remember, fix their own mistakes and get smarter with every run.
>
> This beats any paid course on agents I've seen.
>
> Watch it, then read the guide on building loops below.

- 含视频（未转写）

[↑ 回到本页目录](#part-1--index)

### x-2071649423042412597

**Spotify：引入 loop 后 agent 成功率 20–30% → 80%**

- 作者：Anatoli Kopadze (@AnatoliKopadze) · 发帖 2026-06-29 · [原帖](https://x.com/AnatoliKopadze/status/2071649423042412597)
- 来源：🔖 收藏 · 拉取 2026-10-27 · 类型：案例分享
- **总结**：Spotify 首席架构师和 Boris Cherny 的 26 分钟对谈要点：Spotify 在 2000 万行代码上运行 agent，引入 loop 后成功率从 20–30% 提升到 80%，现在 73% 的代码由 AI 写，大部分没经过人工审查就合并了。核心论点：模型不如外围的 loop 重要。是「loop engineering 在大规模生产中有效」的一手案例。

**正文**

- **Spotify Chief Architect Niklas Gustavsson**: after implementing **loops** in their workflow, agent success rate went from 20–30% to **80%**
- 26-minute talk with Claude Code creator **Boris Cherny** on how Spotify runs AI agents across 20 million lines of code
  - 73% of Spotify's code is now written by AI
  - Most is merged without a human ever seeing it
- **Takeaway**: the model matters less than the loop you build around it

<details><summary>原文</summary>

> Spotify Chief Architect, Niklas Gustavsson:
>
> "Once we implemented loops in our workflow, our agent success rate went from 20-30% to 80%."
>
> 26 minutes with Claude Code creator Boris Cherny on how Spotify runs AI agents across 20 million lines of code.
>
> Today 73% of their code is written by AI, most merged without a human ever seeing it.
>
> The model matters less than the loop you build around it.
>
> Watch it, then read the full guide on building loops below.

</details>

- 含视频（未转写）

[↑ 回到本页目录](#part-1--index)

### x-2071214176526049739

**前 Google 工程师：agent loop + harness + evals 技术栈**

- 作者：Movez (@0xMovez) · 发帖 2026-06-28 · [原帖](https://x.com/0xMovez/status/2071214176526049739)
- 来源：🔖 收藏 · 拉取 2026-10-27 · 类型：视频推荐 / 框架
- **总结**：推荐一个 20 分钟视频，讲 agent 自我改进的闭环：trace 每次运行 → LLM 打分 → 诊断 → 修复 → 发布。总结出技术栈：agent loops + memory + harness + evals。thread 里附了原视频。是对 self-improving 工作流的简洁概括。

**正文**

> Ex-Google engineer explained AI agent loops, harness, evals in 20 minutes - better than 500$ courses.
>
> trace every run → judge it with an LLM → diagnose → fix → ship.
>
> That loop is how agents self-improve over time.
>
> Agent loops + memory + harness  + evals - thats the stack. 
>
> Watch it, then save the framework below.
>
> [2] Original video:

- 含视频（未转写）

[↑ 回到本页目录](#part-1--index)
