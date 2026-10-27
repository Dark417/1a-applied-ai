# X Notes · 精读

- 共 52 篇，10 个分类；组内按收藏顺序倒序（最新在上）
- 上半部分：Index（点击跳到详情）；下半部分：总结 + 原文
- 自动生成，勿手改：改 `data/note/*.json` 或 `categories.json` 后跑 `scripts/render.py`

## Part 1 · Index

- **Harness & Loop Engineering**（8） — agent 外壳（工具/上下文/权限/记忆）、循环与自我改进
  - [Google 开源 Harness²：递归改进 agent harness](#x-2113948384113598588) · @Sumanth_077 · 2026-10-24
  - [Anthropic 工程师：用 harness 搭会自我改进的 agent](#x-2113719510985269442) · @hayatomaruu · 2026-10-23
  - [Wavestone：11 个 coding agent 共有的 7 部分 harness](#x-2113634548378374458) · @AnnatarXBT · 2026-10-23
  - [Stanford 3.5 小时课程：从零构建 self-improving agent](#x-2085710100468060328) · @hanakoxbt · 2026-08-07
  - [Harness vs Loop vs Graph Engineering：三层别混](#x-2082076425465762082) · @LunarResearcher · 2026-07-28
  - [Anthropic：让系统自己 prompt 自己](#x-2085421662447468758) · @AnatoliKopadze · 2026-08-06
  - [Spotify：引入 loop 后 agent 成功率 20–30% → 80%](#x-2071649423042412597) · @AnatoliKopadze · 2026-06-29
  - [前 Google 工程师：agent loop + harness + evals 技术栈](#x-2071214176526049739) · @0xMovez · 2026-06-28
- **Graph & Multi-Agent**（9） — graph engineering、多 agent 编排与流水线
  - [Google 1 小时课程：从 agent 到 loop 到 graph](#x-2085433401562308987) · @Mahaximus_ · 2026-08-06
  - [How to Become a Graph Architect With Zero Experience (Full Course)](#x-2083131009986396282) · @eng_khairallah1 · 2026-07-31
  - [Graph Engineering with Claude: 12 steps from a single loop to a self-verifying fleet](#x-2079636027736457707) · @0xCarnagee · 2026-07-21
  - [Google 2 小时课程：1 prompt → 100 agents → loops → graphs](#x-2083602508807569560) · @0xCodila · 2026-08-01
  - [30 个 Agent 替代 30 个工程师，12 天交付完整代码库](#x-2029350130261082429) · @sodawhite_dev · 2026-03-05
  - [OpenAI Symphony：把 Linear 看板变成自动研发流水线](#x-2029741601975849132) · @chenchengpro · 2026-03-06
  - [30 个 agent 案例的开源地址：agent-orchestrator](#x-2029350223575920769) · @sodawhite_dev · 2026-03-05
  - [OpenAI Symphony：让 agent 自主完成整个开发流程](#x-2029497156554342760) · @GitHub_Daily · 2026-03-05
  - [Shubham Saboo：7×24 运行的 AI Agent 团队蓝图](#x-2022374455989932409) · @Saboo_Shubham_ · 2026-02-13
- **Agent Memory & RAG**（3） — agent 记忆分层、RAG、知识库
  - [Agent 记忆的 5 层架构（13 页）](#x-2114319310005150101) · @AnnatarXBT · 2026-10-25
  - [RAG Is a Lie We Tell Ourselves — Karpathy's LLM Wiki](#x-2050228936270037068) · @Suryanshti777 · 2026-05-01
  - [How to Master RAG and Build AI Agents That Remember Everything](#x-2050145400204783631) · @eng_khairallah1 · 2026-05-01
- **Coding Agent 实践**（8） — Claude Code / Codex 的用法、工作流与配套工具
  - [VS Code Agent Debug Logs：看清每次 prompt 背后发生了什么](#x-2050341770609750297) · @code · 2026-05-01
  - [How to Become a Claude Code Power User (Full Course)](#x-2047245243503050997) · @eng_khairallah1 · 2026-04-23
  - [Anthropic 团队演示他们如何用 Claude Code](#x-2047331926143619428) · @eng_khairallah1 · 2026-04-23
  - [Google 发布全栈 vibe coding 系统](#x-2034718045550051489) · @__Inty__ · 2026-03-19
  - [Boris Cherny 30 分钟分享 Claude Code 技巧](#x-2046264877703102753) · @cnyzgkc · 2026-04-20
  - [OpenAI 用 Codex 维护 Agents SDK 的四层结构](#x-2031347640630165525) · @chenchengpro · 2026-03-10
  - [GitNexus：给代码库建知识图谱，经 MCP 喂给 AI](#x-2026178278055403843) · @GitHub_Daily · 2026-02-24
  - [离不开 Claude Code 的三个场景](#x-2022157972613300368) · @yanhua1010 · 2026-02-13
- **Skills & Prompt**（6） — Skills 设计、可复用 prompt 与技能库
  - [Markdown Viewer Skills：让 AI 在 Markdown 里直接画图](#x-2047525971742597195) · @GitHub_Daily · 2026-04-24
  - [Addy Osmani 开源 Agent Skills：老工程师的操作手册](#x-2046454424806343139) · @KengGuangLong · 2026-04-21
  - [obra/superpowers 的 brainstorming SKILL](#x-2028854979805790269) · @cholf5 · 2026-03-03
  - [Anthropic《The Complete Guide to Building Skills for Claude》解读](#x-2027350587533332748) · @heyrimsha · 2026-02-27
  - [把 GitHub 开源项目打包成 Skill](#x-2014100945416888444) · @gkxspace · 2026-01-21
  - [OpenAI 官方 Prompt Packs：300+ 岗位提示词](#x-2014252422806536614) · @zstmfhy · 2026-01-22
- **OpenClaw & 个人 Agent**（6） — OpenClaw 生态、常驻个人助理、一人公司
  - [OpenClaw + Codex/Claude Code Agent Swarm：一人开发团队](#x-2025920521871716562) · @elvissun · 2026-02-23
  - [OpenClaw 编排文章的要点总结](#x-2026224275192193465) · @AYi_AInotes · 2026-02-24
  - [ClawWork：给 agent 加经济激励](#x-2023308910883664070) · @blackanger · 2026-02-16
  - [OpenClaw Mac 桌面版发布](#x-2022346776679006516) · @aigclink · 2026-02-13
  - [爆肝 2 天，开发 OpenClaw 接入微信 bot，已开源](#x-2022356917948166506) · @canghe · 2026-02-13
  - [OpenClaw agent Larry 一周拿下百万 TikTok 播放](#x-2022011925903667547) · @oliverhenry · 2026-02-12
- **Evals & 研究**（5） — 评测方法、论文与综述
  - [Evals：如何判断一个 AI 系统真的可用](#x-2106453816757354947) · @sermakarevich · 2026-10-03
  - [Google Nexus：把预测变成推理问题](#x-2055978135246807138) · @rohanpaul_ai · 2026-05-17
  - [DAIR.AI 每周论文（4/26–5/3）](#x-2050956647909015788) · @dair_ai · 2026-05-03
  - [论文：Recursive Multi-Agent Systems](#x-2050261909690097671) · @dair_ai · 2026-05-01
  - [DeepMind + Meta + Amazon：100 页 agentic reasoning 路线图](#x-2024602668258517440) · @hasantoxr · 2026-02-19
- **LLM 基础 & 课程**（2） — LLM 原理与系统课程
  - [Stanford CS329A：Self-Improving AI Agents 课程](#x-2104453599367770287) · @shao__meng · 2026-09-28
  - [Karpathy 3 小时：从零构建 LLM](#x-2078533887383556335) · @RohOnChain · 2026-07-18
- **其他应用**（2） — agent 之外的 AI 应用（GNN 量化、图像生成等）
  - [Graph Engineering for Quants：GNN 量化大师课](#x-2081656879886012676) · @RitOnchain · 2026-07-27
  - [Nano Banana 2：手绘户型图 → 4K 3D 室内渲染](#x-2029562218048541087) · @EHuanglu · 2026-03-05
- **其他**（3） — 推广、资源链接、信息量低的帖子
  - [The Code newsletter 推广](#x-2082413202353406091) · @CodeNewsletter · 2026-07-29
  - [NotebookLM 深度解析推荐](#x-2029598376321585332) · @nicebabycat · 2026-03-05
  - [Scrapling：绕过反爬的开源抓取库](#x-2029459404710658307) · @NextBullReady · 2026-03-05

## Part 2 · Details

### 📂 Harness & Loop Engineering

#### x-2113948384113598588

**Google 开源 Harness²：递归改进 agent harness**

- 作者：Sumanth (@Sumanth_077) · 发帖 2026-10-24 · [原帖](https://x.com/Sumanth_077/status/2113948384113598588)
- 来源：🔖 收藏 · 拉取 2026-10-27
- 类型：工具发布 / 方法介绍
- **总结**：介绍 Google 开源的 Harness²：不改模型权重，只递归改进 agent 外围的 harness。分两层递归：任务内用 Propose→Probe→Compose，提出 harness 变体、在同一任务上试跑、比较执行轨迹，再组合出更好的版本；跨任务保留已采用的 harness 和有执行证据支撑的经验，用来指导以后怎么改。重点是「harness 本身也可以被自动优化」，是 self-improving agent 的一条工程路线。
- **原文**：

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

- 图片：[img1](https://pbs.twimg.com/media/HVZAbCYasAAAe6R?format=png&name=large)

#### x-2113719510985269442

**Anthropic 工程师：用 harness 搭会自我改进的 agent**

- 作者：hayato (@hayatomaruu) · 发帖 2026-10-23 · [原帖](https://x.com/hayatomaruu/status/2113719510985269442)
- 来源：🔖 收藏 · 拉取 2026-10-27
- 类型：搭建思路 / 视频推荐
- **总结**：转述一位 Anthropic 工程师的 workshop，给出搭 harness 的五步：①harness 负责 loop、上下文和沙箱；②「大脑」和「手」分离，首 token 快 60%；③服务端运行，崩溃后从日志恢复；④失败代价低，可以 retry/replay；⑤把昨天的日志变成新记忆（Anthropic 称为 dreaming）。主张：同一个模型，靠 harness 能让 agent 可靠 10 倍、越跑越好。偏营销口吻，但五步框架可用。
- **原文**：

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

- 引用 beamnxw ./ @beamnxw · Oct 6:
  > Stop letting unfinished Opus 5.5 runs eat your budget
  >
  > Set up the harness before your next long task
  >
  > Save progress, verify results, reuse the workflow
  >
  > The full 7-layer setup below ↓
- 含视频（未转写）

#### x-2113634548378374458

**Wavestone：11 个 coding agent 共有的 7 部分 harness**

- 作者：Annatar.md (@AnnatarXBT) · 发帖 2026-10-23 · [原帖](https://x.com/AnnatarXBT/status/2113634548378374458)
- 来源：🔖 收藏 · 拉取 2026-10-27
- 类型：论文解读 / 方法对比
- **总结**：解读 Wavestone AI Lab 的报告：读了 Claude Code、Codex 等 11 个 coding agent 的源码，总结出共同的 7 部分 harness（loop、LLM 层、tools、memory、safety、orchestration、extensions），并给出每部分从最简到最完整的光谱。比如 tools 从只有 bash 到 43 个按需加载的 typed tools；9/11 用 SKILL.md，8/11 用 MCP。推荐先读 p.4 全图、p.12 三种 loop、p.67 的 18 条设计规则、p.71 的 90 行最小 harness。是对比型参考资料。
- **原文**：

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

- 含视频（未转写）

#### x-2085710100468060328

**Stanford 3.5 小时课程：从零构建 self-improving agent**

- 作者：Hanako (@hanakoxbt) · 发帖 2026-08-07 · [原帖](https://x.com/hanakoxbt/status/2085710100468060328)
- 来源：🔖 收藏 · 拉取 2026-10-27
- 类型：课程推荐 + 观点
- **总结**：推荐斯坦福 3.5 小时课程（自我改进基础、多步推理、从反馈中学习），并提炼核心：Attempt → Signal → Correction → Better attempt。关键论点：agent 不能靠自评改进，信号必须来自外部（测试、eval、人），否则 loop 只会强化它原来的看法。「自审」是旧工作流，「外部纠错」是新工作流。这一点对设计 eval 驱动的 loop 很重要。
- **原文**：

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

- 含视频（未转写）

#### x-2082076425465762082

**Harness vs Loop vs Graph Engineering：三层别混**

- 作者：Lunar (@LunarResearcher) · 发帖 2026-07-28 · [原帖](https://x.com/LunarResearcher/status/2082076425465762082)
- 来源：🔖 收藏 · 拉取 2026-10-27
- 类型：概念对比
- **总结**：区分三个常被混用的概念。Harness engineering 构建模型周围的环境：上下文注入、可执行动作（API/浏览器/shell/MCP）、权限、记忆。Loop engineering 设计「干活—反馈—重试」的循环。Graph engineering 把工作流拓扑显式化，规定下一步能走哪条路。心智模型：Environment → Feedback → Flow。实用价值：出问题时先判断是哪一层，避免调错层。
- **原文**：

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

- 图片：[img1](https://pbs.twimg.com/media/HOT9HLwXYAAH5Gd?format=jpg&name=large) [img2](https://pbs.twimg.com/media/HOT5dAzXgAA_jfr?format=jpg&name=large) [img3](https://pbs.twimg.com/media/HOT5h-lW4AA5wop?format=jpg&name=large) [img4](https://pbs.twimg.com/media/HOT5-5nWMAAm9FS?format=jpg&name=large) [img5](https://pbs.twimg.com/media/HOT6DAxWYAAd-GS?format=jpg&name=large) [img6](https://pbs.twimg.com/media/HOT51RsXkAACqqL?format=jpg&name=large) [img7](https://pbs.twimg.com/media/HOT6ISpXQAEeBPm?format=jpg&name=large)

#### x-2085421662447468758

**Anthropic：让系统自己 prompt 自己**

- 作者：Anatoli Kopadze (@AnatoliKopadze) · 发帖 2026-08-06 · [原帖](https://x.com/AnatoliKopadze/status/2085421662447468758)
- 来源：🔖 收藏 · 拉取 2026-10-27
- 类型：视频推荐 + 观点
- **总结**：推荐 Anthropic 工程师的 45 分钟演讲。核心观点：不要手动 prompt Claude，而是搭一个能自我 prompt 的系统，让 agent 有记忆、能修正自己的错误、每次运行都变得更好。帖子只给出方向，具体做法在视频和附带的 loop 指南里。
- **原文**：

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

#### x-2071649423042412597

**Spotify：引入 loop 后 agent 成功率 20–30% → 80%**

- 作者：Anatoli Kopadze (@AnatoliKopadze) · 发帖 2026-06-29 · [原帖](https://x.com/AnatoliKopadze/status/2071649423042412597)
- 来源：🔖 收藏 · 拉取 2026-10-27
- 类型：案例分享
- **总结**：Spotify 首席架构师和 Boris Cherny 的 26 分钟对谈要点：Spotify 在 2000 万行代码上运行 agent，引入 loop 后成功率从 20–30% 提升到 80%，现在 73% 的代码由 AI 写，大部分没经过人工审查就合并了。核心论点：模型不如外围的 loop 重要。是「loop engineering 在大规模生产中有效」的一手案例。
- **原文**：

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

- 含视频（未转写）

#### x-2071214176526049739

**前 Google 工程师：agent loop + harness + evals 技术栈**

- 作者：Movez (@0xMovez) · 发帖 2026-06-28 · [原帖](https://x.com/0xMovez/status/2071214176526049739)
- 来源：🔖 收藏 · 拉取 2026-10-27
- 类型：视频推荐 / 框架
- **总结**：推荐一个 20 分钟视频，讲 agent 自我改进的闭环：trace 每次运行 → LLM 打分 → 诊断 → 修复 → 发布。总结出技术栈：agent loops + memory + harness + evals。thread 里附了原视频。是对 self-improving 工作流的简洁概括。
- **原文**：

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

### 📂 Graph & Multi-Agent

#### x-2085433401562308987

**Google 1 小时课程：从 agent 到 loop 到 graph**

- 作者：Mahax (@Mahaximus_) · 发帖 2026-08-06 · [原帖](https://x.com/Mahaximus_/status/2085433401562308987)
- 来源：🔖 收藏 · 拉取 2026-10-27
- 类型：课程推荐
- **总结**：推荐 Google 的 1 小时 graph engineering 课程，附章节时间戳：第一个 agent → agent 记忆 → agentic loops → 构建 MCP → graph engineering。是一条从单 agent 到图编排的入门路径，适合快速建立整体概念。帖子本身没有技术细节。
- **原文**：

> Google just dropped a 1-hour course on Graph Engineering: from agents to Loops to full automation
>
> 00:00 – Build your first AI agent 
> 08:24 – Build agent memory 
> 28:34 – Agentic loops 
> 40:04 – How to build MCP 
> 1:00:22 – Graph engineering 
>
> This 1-hour watch replaces any $500 course you could pay for.
>
> Watch it, then try your first graph with the step-by-step guide below

- 含视频（未转写）

#### x-2083131009986396282

**How to Become a Graph Architect With Zero Experience (Full Course)**

- 作者：Khairallah AL-Awady (@eng_khairallah1) · 发帖 2026-07-31 · [原帖](https://x.com/eng_khairallah1/status/2083131009986396282)
- 来源：🔖 收藏 · 拉取 2026-10-27
- 类型：学习路线（长文教程）
- **总结**：一条 20 步、分 5 个阶段的 graph architect 学习路线：①先掌握 loop（1–4）；②建立 graph 心智模型：节点、边、状态（5–9）；③核心模式：fan-out、路由、校验门等（10–14）；④可靠性：恢复路径、checkpoint 与状态持久化、可观测性（15–18）；⑤架构思维：知道什么时候不该用 graph（19–20）。最后讲常见卡点和各阶段「做得好」的标准。重点是按顺序学，不要跳步。
- **原文**：

> 《How to Become a Graph Architect With Zero Experience (Full Course)》
>
> Most people who saw "graph engineering" trend on X this month did one of two things.
> They dismissed it as another buzzword, or they nodded along without any real idea how to actually build one.
> A small group is going to do the third thing: learn it properly, before the crowd catches up, while the term is still new enough that being genuinely good at it puts you years ahead.
> The difference between those groups is not talent.
> It is a path.
> A graph architect is not someone who memorized a framework. It's someone who can look at a messy, real-world problem and design the network of agents, tools, checks, and human decisions that solves it reliably. That's a genuinely valuable skill, it's the current outermost edge of AI engineering, and almost nobody has it yet because the term is two weeks old.
> Here is the exact path from zero to that skill. Twenty steps, grouped into five phases. No graph theory degree required. Follow it in order and don't skip, because every step is built on the one before it.
> Phase 1: Master the Loop First (Steps 1–4)
> You cannot build a network of loops until you can build one loop. This phase is non-negotiable, and skipping it is why most people's graphs fall apart.
> Step 1: Understand what a loop actually is. A loop is the atom of agentic work: an agent takes an action, a result comes back, something checks whether it's good, and the cycle repeats until the job is done. Before you touch anything called a graph, you need this shape burned into your brain, because a graph is just many of these wired together. Do this: write out, in plain English, the four parts of a loop for a task you understand. The action, the result, the check, the repeat condition.
> Step 2: Build one working loop. Pick a simple real task and build a single agent that loops until it's done. Give it one tool. Let it try, check, and retry. Feel how it behaves, where it gets stuck, where it loops forever. This hands-on frustration is the best teacher you'll get. Do this: build a single-agent loop that completes one real multi-step task end to end.
> Step 3: Learn why the verifier is everything. The single most important part of any loop is the check, the verifier that decides whether the work is good. A loop with a weak verifier produces confident garbage fast. Loop engineering, the rung right before graphs, is largely the craft of writing good verifiers. Master this now and graphs become easy later. Do this: take your loop from step 2 and make its verifier genuinely strict. Watch the output quality climb.
> Step 4: Learn the four ways single loops fail at scale. Loops are powerful but they break in predictable ways once the work gets complex: they can't branch cleanly, they can't run things in parallel, they can't enforce checkpoints across steps, and they handle failure by just retrying. Understanding these four failure modes tells you exactly what a graph is for. Do this: for each of the four failure modes, write down a task where a single loop would struggle with it.
> Phase 2: Learn the Graph Mental Model (Steps 5–9)
> Now you learn the vocabulary and the shape. This phase is about seeing work as a graph before you build one.
> Step 5: Learn the three primitives: nodes, edges, state. A node is a unit of work. An edge is a route that decides what runs next. State is the shared information flowing through the system. Every graph, no matter how complex, is just these three things. Get them cold. Do this: take a task you know and sketch it on paper as nodes and edges, with a note on what state flows between them.
> Step 6: Understand that not every node is an LLM. This is the insight that separates architects from beginners. The best graphs mix LLM-powered nodes with plain deterministic functions, tool calls, and validators. A simple check should be a function, not a model. Overusing LLMs is the most common way graphs become slow, costly, and flaky. Do this: in your paper sketch from step 5, mark which nodes truly need an LLM and which could be plain functions. Most should be functions.
> Step 7: Learn conditional edges. The edges that make a graph powerful are the conditional ones: "if the output has an error, route here; otherwise, continue there." This is how a graph expresses decisions a straight loop can't. Do this: add at least two conditional edges to your sketch. Give the system a real decision to make.
> Step 8: Design your state deliberately. Half of good graph design is good state design. Too little shared state and nodes can't do their jobs; too much and nobody can reason about the system. Practice deciding exactly what information each node needs and what it should pass on. Do this: write out the full state your sketched graph carries, field by field, and justify each one.
> Step 9: Pick one framework and learn its way of doing this. You don't need many. Pick one graph-orchestration framework, LangGraph is the most common starting point, and learn how it expresses nodes, edges, and state. The concepts transfer everywhere; you just need one place to practice them. Do this: build your paper sketch as a real running graph in one framework. Get it to execute end to end.
> Phase 3: Master the Core Patterns (Steps 10–14)
> Architects don't reinvent structures. They recognize which known pattern fits and apply it. These five patterns cover most real work.
> Step 10: The router. A node that looks at the input and routes it to the right specialist or path. This is the simplest branching pattern and the gateway to everything else. Do this: build a graph that routes different kinds of input to different handling nodes.
> Step 11: The orchestrator-worker. A manager node breaks a job into subtasks, assigns each to a worker node, and assembles the results. This is the backbone of most multi-agent systems. Do this: build a graph where one node delegates to two or more worker nodes and combines their output.
> Step 12: Parallel fan-out and fan-in. Several independent nodes run at the same time, then their results converge at a single node. This is how a graph delivers real speed that a loop can't. Do this: build a graph that runs three tasks in parallel and merges the results.
> Step 13: The evaluator-optimizer. One node produces work, another node critiques it against a standard, and the work loops back for revision until it passes. This is the quality engine of serious graphs. Do this: build a generator node and a critic node, and wire them so weak output gets sent back with specific feedback.
> Step 14: The human-in-the-loop gate. A node where the system pauses and waits for a person to approve before continuing. Anything irreversible, sending, publishing, spending, deleting, routes through one of these. This isn't optional in production; it's what makes a graph safe. Do this: add a pause-for-approval node before any consequential action in one of your graphs.
> Phase 4: Build for Reliability (Steps 15–18)
> Anyone can make a graph run once. Architects make it run the ten-thousandth time. This phase is what companies actually pay for.
> Step 15: Add validation gates. Beyond the evaluator pattern, add explicit gate nodes at critical points whose only job is to verify that work meets a standard before it proceeds. Named, non-negotiable checkpoints are a graph's greatest advantage over a loop. Do this: add a validation gate that hard-stops the graph if output fails a defined standard.
> Step 16: Design recovery paths. A loop's answer to failure is "retry." An architect's answer is a deliberate path: fall back to a simpler method, escalate to a human, or fail safely with a clear message. Decide in advance what each kind of failure does. Do this: for every node that can fail, define where a failure routes instead of just retrying forever.
> Step 17: Add checkpoints and state persistence. Real graphs can pause and resume. If the system stops halfway, whether it's waiting on a human or recovering from a crash, it should pick up where it left off, not start over. Persisting state at checkpoints is what makes this possible. Do this: make one of your graphs able to stop mid-run and resume from where it paused.
> Step 18: Make it observable. You can't fix what you can't see. Add logging and tracing so you can watch what each node did, what state flowed, and where things went wrong. An architect can debug a graph because they built it to be debuggable. Do this: add tracing to a graph so you can replay exactly what happened on any run.
> Phase 5: Think Like an Architect (Steps 19–20)
> The final two steps aren't about building. They're about judgment, which is what actually makes someone an architect rather than a technician.
> Step 19: Master when NOT to build a graph. The most senior skill in this entire discipline is knowing that most tasks don't need a graph at all. A single job with a single verifier is a loop, and it should stay one. Reaching for a graph before the work demands it hands you a distributed-systems problem you didn't have. An architect starts with the simplest thing that works and lets the problem earn every bit of added complexity. Do this: take three tasks and correctly decide which need a graph and which are just loops or plain scripts. Being able to say "this doesn't need a graph" is the mark of mastery.
> Step 20: Design for production, evals, and the team. The final leap: design graphs other people can run, trust, and maintain. That means building an evaluation suite so you can measure whether a change helped or hurt, documenting the graph so a teammate understands it, and designing it to be extended without collapsing. This is what separates a clever demo from a system a company runs its business on. Do this: build an evaluation set for one of your graphs and run it after every change. Document the graph so someone else could maintain it.
> How to Actually Walk This Path
> Twenty steps looks like a lot until you realize it's really five ideas: master the loop, learn the graph model, learn the patterns, build for reliability, and develop the judgment to know when to stop.
> Do not try to sprint all twenty in a weekend. The people who rush end up with a shaky mental model and graphs that break. Give Phase 1 real time, because everything rests on it. Then move one phase at a time, building something real at each step rather than just reading about it. The "do this" actions aren't optional; they're the whole point. You become a graph architect by building graphs, not by understanding them in the abstract.
> A realistic pace: a week or two per phase if you're already comfortable coding and working with LLM APIs, longer if you're newer. Six to eight weeks of genuine, hands-on practice and you'll be able to do something almost nobody could do a month ago: look at a real problem and design the right graph for it, including the wisdom to know when the answer is "this doesn't need one."
> The Four Things That Stall People (And How to Beat Them)
> Most people who start this roadmap don't finish, and they stall at predictable places. Here's where, and how to get past each.
> They skip Phase 1 because loops feel too basic. They saw "graph engineering" trend, so starting with a single loop feels like a step backward. Then their graphs fall apart and they can't tell why, because the individual loops inside were never solid. Beat it by refusing to move on until you can build a single loop with a genuinely strict verifier. Everything rests on this, and the people who honor it move faster overall, not slower.
> They collect frameworks instead of building. They watch tutorial after tutorial, try three different tools, and never ship one working graph. Learning about graphs feels like progress but produces nothing. Beat it by picking one framework and refusing to touch another until you've built at least three real graphs in it. Depth in one beats shallow exposure to many.
> They over-engineer the moment they learn the patterns. Right after Phase 3, newly armed with orchestrators and parallel workers, they build elaborate graphs for problems that needed a loop. It feels sophisticated and produces fragile, unmaintainable systems. Beat it by treating Step 19, knowing when not to build a graph, as the real graduation, not an afterthought. Restraint is the senior skill.
> They stop at "it runs" and never reach "it's reliable." They get a graph working once, feel done, and skip Phase 4 entirely. Then it breaks the first time reality throws it something unexpected, and they conclude graphs are flaky. Beat it by treating a graph as unfinished until it has validation gates, recovery paths, and the ability to be debugged. "It ran in the demo" is where amateurs stop and architects begin.
> What Good Looks Like at Each Phase
> So you can measure yourself honestly, here's the mark of real competence at each stage.
> After Phase 1, you can build a single-agent loop that reliably completes a real task, and you can explain exactly why a weak verifier ruins it. After Phase 2, you can take any problem and sketch it as nodes, edges, and state on paper before writing code, and you instinctively mark which nodes need an LLM and which don't. After Phase 3, you can look at a problem and name which core pattern fits, then implement it without a tutorial. After Phase 4, your graphs survive contact with bad input, failed tools, and interruptions, and you can replay any run to see what happened. And after Phase 5, the thing that sets you apart: you can look at a request and correctly say "this doesn't need a graph at all," which, more than any pattern, is what a graph architect actually is.
> If you can do all five, you have a skill almost nobody had a month ago, and one that will keep paying off long after the buzzword fades.
> The Questions Everyone Asks Before They Start
> A few questions come up every single time someone begins this path. Here are the honest answers.
> Do I need to know graph theory or heavy math? No. This is not the graph theory from a computer science course, and you don't need to prove theorems about traversal. "Graph" here just means nodes connected by edges with information flowing through, a way of drawing a solution. If you can sketch boxes and arrows and reason about what flows between them, you have all the math you need.
> Do I need to be a strong programmer first? You need to be comfortable writing code and working with LLM APIs, so if you're brand new to programming, spend time there first. But you do not need to be an expert. Most of the difficulty in graph engineering is clear thinking about structure, not advanced coding. If you can build a single agent that calls an API and handles the response, you're ready for Phase 1.
> Which framework should I learn? Pick one common graph-orchestration framework and go deep. The specific choice matters far less than committing to one long enough to build several real graphs in it. The concepts, nodes, edges, state, gates, transfer everywhere, so you're really learning the discipline, not the tool. Framework-hopping is a way of feeling busy without getting better.
> Isn't this just a buzzword that'll be gone in six months? The word might fade; the skill won't. What you're actually learning, designing reliable systems around unreliable models, has been valuable for years under other names and will stay valuable under whatever the next name is. You're not betting on a term. You're building a durable capability that happens to have a trendy label right now.
> How do I know I'm ready to call myself a graph architect? When you can look at a real problem and design the right structure for it, including confidently saying "this one doesn't need a graph." That judgment, not a certificate or a framework badge, is the whole thing. If you can build the patterns and know when not to, you're there.
> The Honest Truth About Becoming a Graph Architect
> The title sounds impressive, and the buzzword is hot, but here's what actually matters.
> Being a graph architect is not about the graphs. It's about clear thinking under complexity. A graph is just a way of drawing a solution precisely enough that it works reliably. The people who master this aren't the ones who memorized the most patterns. They're the ones who can look at chaos and see the simplest structure that tames it, which sometimes means a graph and often means something far simpler.
> That skill doesn't expire when the buzzword fades. Prompt engineering, context engineering, loop engineering, and now graph engineering, the names keep changing, but the underlying ability, designing reliable systems around unreliable models, only becomes more valuable. Learn this deeply and you're not chasing a trend. You're building the skill every future rung of the ladder will require.
> There's a reason this window is worth moving on now. Skills are most valuable when demand is high and supply is nearly zero, and that gap is never wider than right after a term goes mainstream but before most people have done the work. Right now, enormous numbers of people are talking about graph engineering and almost none of them can actually design a reliable one. That gap is the opportunity, and gaps like this close as the crowd catches up. The people who move during the window, not after it, are the ones who get years of head start compressed into weeks.
> The term is two weeks old. The crowd is still arguing about what it means.
> Eight weeks from now you can either still be one of the people posting hot takes about a word.
> Or you can be one of the few who can actually build the thing.
> Step one is understanding a single loop. Start there today.
> If you found this useful, follow me @eng_khairallah1 for more AI content like this. I post breakdowns, courses, and tools every week.
> hope this was useful for you, Khairallah ❤️

- 图片：[img1](https://pbs.twimg.com/media/HOgbHEdWsAAVrR4?format=jpg&name=large)

#### x-2079636027736457707

**Graph Engineering with Claude: 12 steps from a single loop to a self-verifying fleet**

- 作者：Carnage (@0xCarnagee) · 发帖 2026-07-21 · [原帖](https://x.com/0xCarnagee/status/2079636027736457707)
- 来源：🔖 收藏 · 拉取 2026-10-27
- 类型：搭建教程（带代码）
- **总结**：带代码的 12 步教程。问题：一个上下文塞四个任务就会「淹死」，解法不是换更大的模型，而是多个 worker 有意识地连起来。步骤包括：节点 = 一个工作，边 = 一次交接；每个节点有 schema 契约；用 parallel() fan-out；split-work-merge 的菱形结构；运行时用 router 改道；在边上放 skeptic 做校验；节点之间隔离；带停止条件的循环（连续两轮无新发现就停）。偏工程实操。
- **原文**：

> 《Graph Engineering with Claude: 12 steps from a single loop to a self-verifying fleet (Full Course)》
>
> Your agent works until it doesn't. One job, one loop, one context - fine. Then you hand it something real, and it drowns.
> Watch it happen. You ask for research, then analysis, then code, then a review of that code. Four jobs, one conversation. By the time it writes the review, it's forgotten what the research said. The context filled up and the early work fell out the bottom.
> Most people reach for a bigger model here. Wrong lever. The model was never confused - the architecture was. You gave one worker four jobs and the memory budget for one.
> The fix is more workers, wired on purpose. That wiring has a name and a shape. Nodes carry the work. Edges carry the results. The picture they make is a graph.
> Follow for more
> This is the 12-step path from one overloaded loop to a fleet that splits the work, checks itself, and returns an answer no single context could have held.
>
>
> 01. A node is a job. An edge is a handoff.
> Strip a graph down and only two things survive. A node: one agent, one job, one input, one result. An edge: the wire where one node's result becomes the next node's input.
> The trap everyone falls into is reading "and then" as a wire. "Read the config and then check the weather" has no wire in it - the weather never touches the config. 
>
> Two jobs, zero dependency, and a linear script staples them together for no reason. So interrogate every "and then" you write. Does the next step actually read what the last one produced?
> Yes means a real edge - the order is load-bearing, leave it. No means there's no edge at all, and the wait between them is dead time you're paying for.
> Here's the whole test in one move: sketch it as boxes and arrows, where an arrow is a variable one call hands to another
>
>  If you can't draw the arrow, there is no arrow. Those two boxes are strangers - and strangers run at the same time.
>
>
> 02. Your straight-line agent is already a graph - a bad one
> "A, then B, then C, then D" is a graph. It's just the worst possible one: a single wire with no branches, every node holding exactly one input and one output.
> It gives the right answer. It also gives it slowly, and it snaps under pressure - if B hangs, everything after it starves, and everything before it sits finished with nowhere to go.
> Turning a builder into an architect starts here: walk the chain and test every arrow. Nine times out of ten, two or three of those arrows move no data. 
>
> They're there because that's the order your fingers typed, not because the work demanded it.
> Delete the fake arrows. The chain buckles into something wider - a cluster of jobs that could have run together all along, feeding one node that finally needs them all at once.
>
>
> 03. Give every node a contract
> A node you can't describe in one sentence is a node you can't trust to run alone. Pin it down with a contract: what goes in, what comes out, one job in between.
> The input has to arrive explicitly - handed in, never scavenged from some shared window the node hopes is still there. The output has to be a fixed shape, so the next node reads it instead of guessing at it.
> Workflows enforce that contract with a schema. Attach a JSON schema to an agent() call and the subagent can't hand you loose prose
>
> it's forced to return validated structure, and Claude re-runs it on any mismatch instead of dumping unparseable text in your lap.
> python
> const FINDING = {
>   type: 'object', additionalProperties: false,
>   properties: {
>     file:     { type: 'string' },
>     line:     { type: 'number' },
>     severity: { type: 'string', enum: ['block', 'warn', 'info'] },
>   },
>   required: ['file', 'line', 'severity'],
> };
>
> const hit = await agent(auditPrompt(file), {
>   label:  `audit:${file}`,
>   schema: FINDING,          // structured out, or Claude retries
>   agentType: 'general-purpose',
> });
> The wire between nodes deserves the same discipline. The instinct is to spin up an agent to "merge these results" - fight it. 
>
> If merging means flatten and dedupe, that's a flatMap and a Set: instant, exact, free. Spend agents on judgment. Never on plumbing.
>
>
> 04. Fan out with parallel()
> This is the move that pays for the whole graph. When you're holding N jobs that don't depend on each other - N files to scan, N sources to pull, N routes to check - you stop feeding them through one mouth and open N mouths at once.
> python
> phase('Scan');
>
> const raw = await parallel(
>   ROUTES.map((r) => () =>
>     agent(scanPrompt(r), {
>       label:  `scan:${r}`,
>       phase:  'Scan',
>       schema: FINDING,
>       agentType: 'general-purpose',
>     }),
>   ),
> );
>
> const found = raw.filter(Boolean);   // failed agents came back null
> Two things make it safe. parallel() is a wall - nothing past it moves until every job clears, so the next stage always sees a full set. 
>
> And a job that throws comes back as null instead of blowing up the batch, so one bad agent can't take the run down with it. That's why the filter(Boolean) is there, every time.
> Concurrency tracks your core count and the rest waits in line, so you can throw a hundred jobs at it and they'll all land - just a fistful at a time. 
>
> And none of it crowds Claude's own context, because each subagent holds its own. The session stays light while the fleet does the heavy lifting.
>
>
> 05. The diamond: split, work, merge
> Bolt a fan-out to a fan-in and you get the shape you'll reach for more than any other: the diamond. One node breaks the job apart. Many nodes chew through the pieces at once. One node pulls it back together.
> That last node is where people cut corners. Stapling three JSON blobs is nothing. Fusing three research passes into one coherent answer is a real job with a real quality bar - treat it like an agent, not a string concat.
> python
> const flat = found.flatMap((f) => f.hits);
> log(`${flat.length} raw hits`);
>
> phase('Rank');
> const ranked = await agent(
>   `Dedupe these and rank by severity:\n${JSON.stringify(flat)}`,
>   { phase: 'Rank', schema: RANKED },
> );
> Memorize the rhythm: fan out, reduce, synthesize. Widen to gather, collapse in plain code, then let one agent write the final word.
> Keep the merge honest - only make the fleet wait at that wall if the merge genuinely needs the whole pile at once. Just flattening a list? That's an edge. Do it inline and pay nothing. 
>
> Once the diamond clicks, you stop asking your agent to take more steps and start asking where the split and the merge belong. That second question is the one that scales.
>
>
> 06. Bend the edge at runtime with a router
> Not every graph is carved in advance. Sometimes which wire fires depends on what a node just found. A router looks at a result and picks the path.
> python
> const { size } = await agent(
>   `How large is this diff? one word: small or large.\n${diff}`,
>   { schema: { type: 'object',
>       properties: { size: { enum: ['small', 'large'] } },
>       required: ['size'] } },
> );
>
> const review = size === 'large'
>   ? await parallel(FILES.map((f) => () => agent(reviewPrompt(f))))
>   : await agent(`Quick pass over this diff:\n${diff}`);
> This is where determinism turns from handcuff into feature. The decision can be Claude's - a subagent reads the diff and classifies it. But the branch is code Claude already wrote, 
>
> So the same classification always takes the same road. There's no "the model felt like skipping the audit today," because skipping was never a move the graph offered.
>
>
> 07. Put a skeptic on the edge
> The quiet truth of graph work: the win isn't the extra agents. It's the scaffolding you hang around them to earn trust in the output.
> A verifier stands on the edge and tries to break the finding before it's allowed downstream. Survives the attack, it passes. Fails, it never reaches the answer. Three shapes are worth carrying:
> Refute it. Spawn a handful of skeptics whose whole job is to tear the finding apart. It lives only if most of them fail to.
> Split the lens. Give each checker a different angle - is it correct, is it safe, does it actually reproduce. Three identical checks miss what three different ones catch.
> Panel of judges. Generate a few attempts from different starts, score them in parallel, build the final from the winner.
> One catch nobody warns you about: the skeptic needs a fresh context. Feed it the same transcript the executor had and it isn't checking the work - it's nodding along to itself in a new hat. 
>
> A dozen agents sharing one context aren't a graph. They're the same loop wearing a disguise, and they fail exactly like the loop did - just later, and with a bigger bill.
>
>
> 08. Fence the nodes off from each other
> In a chain, one death is fatal - C dies, D never wakes. In a graph, a death should be a shrug. A job that throws inside parallel() comes back null and the survivors carry on. That filter(Boolean) is the fence.
> The nastier failure is quieter: agents colliding.
> It's not a thought experiment. When the Bun team first split a big port across many agents
>
> they hit the same git commands in the same workspace and overwrote each other's work. The run fell apart operationally, not intellectually.
> The fix wasn't a cleverer prompt. It was structure - ban the shared commands, hand every worker its own isolated worktree, merge clean at the end.
> So before you fan anything out, answer three questions. Where does each agent do its work? How do the results come back together? 
>
> And when two of them disagree, who wins? A fleet without those answers doesn't scale up. It just breaks faster.
>
>
> 09. Add a loop that knows when to stop
> Some jobs won't tell you their size up front. You sweep for one bug and it uncovers three more. That calls for a cycle - a wire that runs back to an earlier node and goes again.
> The obvious danger: a cycle that never converges is just a money fire that spawns agents until the budget's gone.
> The pattern that stays safe is run until dry - keep sending finders out until a couple of rounds in a row turn up nothing new, then stop.
> And here's the one detail that quietly wrecks it for everyone the first time: dedupe against everything you've seen, not just what you confirmed. 
>
> Miss that and every rejected finding comes back next round, the loop never dries out, and you're paying over and over to rediscover the same dead ends.
> python
> const seen = new Set();
> const kept = [];
> let dry = 0;
>
> while (dry < 2) {
>   const raw = (await parallel(
>     FINDERS.map((f) => () => agent(f.prompt, { schema: BUGS }))
>   )).filter(Boolean).flatMap((r) => r.bugs);
>
>   const fresh = raw.filter((b) => !seen.has(id(b)));
>   if (!fresh.length) { dry++; continue; }   // a dry round
>   dry = 0;
>   fresh.forEach((b) => seen.add(id(b)));     // mark SEEN, not kept
>
>   const judged = await parallel(fresh.map((b) => () =>
>     parallel(['correct', 'safe', 'repro'].map((lens) => () =>
>       agent(`Judge "${b.desc}" on ${lens}. real?`, { schema: VERDICT })))
>     .then((v) => ({
>       b, real: v.filter(Boolean).filter((x) => x.real).length >= 2
>     }))));
>
>   kept.push(...judged.filter((v) => v.real).map((v) => v.b));
> }
>
>
> 10. Price the graph before you run it
> Cost and speed both live in the shape. Two levers move them.
> Lever one: match the model to the node. Grunt nodes that classify or extract run on Haiku 4.5. Nodes that reason and build run on Sonnet 4.6. The final gate, where a wrong answer is expensive, runs on Opus 4.8.
>
>  Every subagent inherits your session model unless you say otherwise - 
> the model option on a single agent() call reroutes just that node. Glance at /model before a big run and push the cheap work down.
> Lever two: parallel() versus pipeline(). A parallel() wall makes the whole stage wait on its slowest node. 
>
> A pipeline() lets each item flow through the stages on its own - item A can be finishing while item B is still starting. 
>
> Default to the pipeline. Only raise a wall when a stage truly needs the full set in hand at once.
>
> "It reads cleaner" is not that reason - wall latency is real time, measured in seconds you'll never get back.
>
>
> 11. When you should not build a graph
> Most work isn't a graph, and forcing one on it just lights money on fire and adds new ways to fail.
> Skip it when the job is small - one function, one bug. The orchestration costs more than the work.
> Skip it when you want to watch every step land before the next one fires. A graph's whole point is running wide without you, which is exactly the wrong thing when you need the reins.
> Skip it when you don't yet know what you're hunting. Open-ended work wants one agent you can steer, not a fleet locked to a plan before anyone understands the problem.
> And skip it when the steps genuinely need each other in order. If every step reads the last one's output, it's a true chain - parallelism has nothing to grab onto.
> The tell is Part 1 all over again. Can't find two boxes with no arrow between them? Then there's no graph hiding in there. It's a loop, and a loop is the right tool. Use it without apology.
>
>
> 12. Hand the pen to Claude
> The last step is to stop drawing the graph yourself. With dynamic workflows you hand over the goal, 
>
> and Claude writes the orchestrator - carving up the task, choosing the fan-out, running the fleet, fusing the result.
> Three doors in. Drop the word "workflow" into a prompt and Claude builds one for the job. 
>
> Run /deep-research, a graph already shipping in production. Or flip on ultrathink and Claude plans one for every serious task in the session.
> python
> > audit every route in src/routes for missing auth.
>   one agent per file, verify each hit before you report.
>
>   /workflows — auth-audit — running
>   done  Scope      1/1    2.1k tok · 4s
>   done  Fan-out    18/18  one agent per route
>   live  Verify     11/18  skeptics voting on each hit…
>   wait  Synthesize 0/1    holding for verify
>   session stays live — keep working while it runs
> Like the run? Press s. It saves to ~/.claude/workflows/ - version it, name it, and anyone who clones the repo can fire the same graph.
> What does the ceiling actually look like? The Bun team ran their Zig-to-Rust port on this exact machinery. Roughly fifty workflows, sixty-four agents peaking in parallel
>
> about 535,000 lines of Zig rewritten into over a million lines of Rust in eleven days - for around $165,000 in usage, with one human steering and watching the whole time. 
>
> The power is real. So is the invoice, and so is the supervision.
> Six graphs to build this week
> A security sweep over every route - one agent per file, a skeptic confirming each hit. Coverage no single window could hold.
> A cited report through /deep-research, already in the box - parallel searches, skeptics voting on every claim before a word gets written.
> A module port, file by file - translation fanned out, the test suite as a gate, failures looped back until they pass.
> An adversarial diff review that routes on size - small change gets one pass, big change triggers the full parallel audit.
> A scheduled ecosystem scan - saved once, run forever, sources pulled in parallel and ranked into a digest.
> A discovery run of unknown size - finders in parallel, everything deduped against what's been seen, looping until two rounds come up empty.
> Five ways your first graph dies
> One node doing everything. When it falls, the whole thing falls. Cut it into single-job nodes.
> No contracts on the wires. No schema, no fixed shape, and every node guessing at the last one's output.
> No fallback path. One error and the run collapses. Give every fragile node somewhere to fail to.
> Sonnet 4.6 doing your routing. Routing is classification - Haiku 4.5 does it faster and cheaper. Save the big model for building.
> No skeptic on the edge. Ship one wrong answer and that's the last time anyone trusts the fleet.
> A prompt asks. A graph decides.
> The straight line was never the wall you kept hitting. It was just the first shape you knew how to draw - one thread, one head, one thing after another, because that's how typing feels.
> See the nodes and the edges and the question flips. You stop pushing one agent to do more and start asking the graph to do it wider. 
>
> Split where the work is independent. Guard the wires where the answer has to be right. Anchor the nodes that hold the truth and never let them drift.
> Most people will keep typing in a line. The ones who learn to draw will run the fleet. Draw it. Then get out of its way.
> Start where this begins: Loop Engineering - the single loop every graph is built on

- 图片：[img1](https://pbs.twimg.com/media/HNxCj6YXMAEC-lT?format=jpg&name=large) [img2](https://pbs.twimg.com/media/HNxXiOcXQAAOlU4?format=png&name=large) [img3](https://pbs.twimg.com/media/HNxXoItWsAEOg3n?format=png&name=large) [img4](https://pbs.twimg.com/media/HNxY051W8AAOuh5?format=png&name=large) [img5](https://pbs.twimg.com/media/HNxYx01WkAAdkOq?format=png&name=large) [img6](https://pbs.twimg.com/media/HNxY6VsWcAAHJuX?format=png&name=large) [img7](https://pbs.twimg.com/media/HNxYnYgXQAA6jSU?format=png&name=large) [img8](https://pbs.twimg.com/media/HNxYtQeXUAE9lZK?format=png&name=large) [img9](https://pbs.twimg.com/media/HNxYUcJWMAAQqZ5?format=png&name=large) [img10](https://pbs.twimg.com/media/HNxZAzkXAAAjuXQ?format=png&name=large) [img11](https://pbs.twimg.com/media/HNxYPJGWEAAl9Ep?format=png&name=large) [img12](https://pbs.twimg.com/media/HNxZK_nWYAA1950?format=png&name=large) [img13](https://pbs.twimg.com/media/HNxZVpGXkAAmZR5?format=png&name=large) [img14](https://pbs.twimg.com/media/HNxZbx5WUAEBc28?format=png&name=large)

#### x-2083602508807569560

**Google 2 小时课程：1 prompt → 100 agents → loops → graphs**

- 作者：codila (@0xCodila) · 发帖 2026-08-01 · [原帖](https://x.com/0xCodila/status/2083602508807569560)
- 来源：🔖 收藏 · 拉取 2026-10-27
- 类型：课程推荐
- **总结**：推荐 Google 免费 2 小时课程，附进度时间戳：第一个 agent → loop engineering（迭代、检查、中断）→ graph engineering → 会自我节流的 agent → 多 agent 系统的完整 graph。观点：大多数人搭完一个 agent 就停了，而完整系统是 agent 把自己连成 graph。帖子本身没有技术细节。
- **原文**：

> Google just released free 2-hour course on full Graph engineering: 1 prompt → 100 agents → loops → graphs from 0% to 100%:
>
> 10% → 17:44 - build your first agent
> 30% → 39:30 - Loop engineering: iterate, check, break
> 60% → 1:12:38 - Graph engineering
> 75% → 1:34:26 - agents that throttle themselves
> 100% → 1:55:05 - full graph for multi-agentic systems
>
> everyone builds one agent and calls it done - this is the full system where agents wire themselves into a graph
>
> watch the course, build the graph - then read the full architecture below ↓

- 含视频（未转写）

#### x-2029350130261082429

**30 个 Agent 替代 30 个工程师，12 天交付完整代码库**

- 作者：苏打白.Dev (@sodawhite_dev) · 发帖 2026-03-05 · [原帖](https://x.com/sodawhite_dev/status/2029350130261082429)
- 来源：❤️ 点赞的评论 → 原帖（via [2029350223575920769](https://x.com/i/status/2029350223575920769)） · 拉取 2026-10-27
- 类型：案例分享
- **总结**：一个多 agent 落地案例：用 30 个 AI agent 替代 30 个工程师，12 天交付 4.4 万行 TypeScript、175 个 PR、1500+ 个测试，CI 挂掉时 agent 还能自己修。帖子本身只有数据，没有讲架构细节。价值在于给「大规模并行 agent 能不能交付真实代码库」提供了一个量级参考。
- **原文**：

> 刚看到一个硬核案例：用30个AI Agent替换30个工程师，12天交付完整代码库（44K行TS、175 PR、1500+测试、CI挂了还能自己修。。。）。

- 含视频（未转写）

#### x-2029741601975849132

**OpenAI Symphony：把 Linear 看板变成自动研发流水线**

- 作者：陈成 (@chenchengpro) · 发帖 2026-03-06 · [原帖](https://x.com/chenchengpro/status/2029741601975849132)
- 来源：🔖 收藏 · 拉取 2026-10-27
- 类型：源码解读
- **总结**：读完 OpenAI 开源的 Symphony 代码后的要点：核心循环是监控 Issue → 分配 agent → 写代码 → 提 PR → 循环；用 Elixir/OTP 天然支持多 agent 并发，每个 Issue 一个独立 workspace；最有意思的设计是 WORKFLOW.md，把 agent 的行为策略写进仓库，可以跟代码一起 review 和回滚。是「看板驱动的 agent 编排」的参考实现。
- **原文**：

> OpenAI 昨天低调开源了一个框架，叫 Symphony 🎵
>
> 它能把你的 Linear 看板变成一条全自动的研发流水线。
> 我扒了一遍代码，说说它到底怎么运作的 👇
>
> 1/ 核心逻辑只有一句话：
> 监控 Issue → 分配 Agent → 写代码 → 提 PR → 循环
>
> 2/ 技术栈是 Elixir，OTP 架构，天然支持多 Agent 并发。
> 每个 Issue 对应一个独立 Workspace，互不干扰。
>
> 3/ 最有意思的设计是 WORKFLOW.md：
> 把 Agent 的行为策略写进项目仓库，随代码一起提交、review、回滚。
> Agent 怎么干活，团队说了算。
>
> 4/ 开源地址：http://github.com/openai/symphony
>
> 你们团队用 Linear 吗？这东西值得试试。

- 链接卡片：[GitHub - openai/symphony: Symphony turns project work into isolated, autonomous ](https://t.co/kSf9Ns9eUz)

#### x-2029350223575920769

**30 个 agent 案例的开源地址：agent-orchestrator**

- 作者：苏打白.Dev (@sodawhite_dev) · 发帖 2026-03-05 · [原帖](https://x.com/sodawhite_dev/status/2029350223575920769)
- 来源：🔖 收藏 · 拉取 2026-10-27
- 类型：工具 / 案例
- **总结**：这是对上文案例（30 个 agent 替代 30 个工程师、12 天交付）的补充，给出开源地址：OrchestratorInc/agent-orchestrator，一个 Apache-2.0 的 Claude Code 编排器。上文是案例数据，这条是可以直接去读的代码，两者合起来看。
- **原文**：

> 地址在这：

- 上文（作者原帖 @sodawhite_dev）：
  > 刚看到一个硬核案例：用30个AI Agent替换30个工程师，12天交付完整代码库（44K行TS、175 PR、1500+测试、CI挂了还能自己修。。。）。
- 链接卡片：[GitHub - OrchestratorInc/agent-orchestrator: Open-source (Apache-2.0) orchestrat](https://t.co/ys8LyplisL)

#### x-2029497156554342760

**OpenAI Symphony：让 agent 自主完成整个开发流程**

- 作者：GitHubDaily (@GitHub_Daily) · 发帖 2026-03-05 · [原帖](https://x.com/GitHub_Daily/status/2029497156554342760)
- 来源：🔖 收藏 · 拉取 2026-10-27
- 类型：工具介绍
- **总结**：从使用者角度介绍 Symphony：监控看板任务，自动派 agent 处理，完成后提供 CI 状态、代码审查反馈、复杂度分析和演示视频作为「工作证明」，通过后安全合并。工程师只需在更高层面管理任务。提供技术规范，可以让 AI 用任意语言实现，也有 Elixir 参考实现。和上面的源码解读互补。
- **原文**：

> 用 AI 写代码虽然快，但需要一直盯着它，生怕它跑偏或者出错，反而增加了管理负担。
>
> OpenAI 最新开源项目 Symphony，换了个思路：让 AI 自主完成整个开发流程，我们只需要管理工作本身。
>
> 它会监控项目看板上的任务，自动派出智能体处理，完成后提供持续集成状态、代码审查反馈、复杂度分析和演示视频等工作证明。
>
> GitHub：http://github.com/openai/symphony
>
> 通过后，智能体会安全地合并代码，整个过程无需人工盯着 Codex 写代码，工程师只需在更高层面管理工作任务即可。
>
> 项目提供了完整的技术规范文档，可以让 AI 用我们喜欢的语言实现，也提供了 Elixir 参考实现可以直接部署使用。
>
> 如果我们想把 AI 编程助手，升级为能自主完成任务的团队成员，这个项目值得尝试一下。

- 含视频（未转写）

#### x-2022374455989932409

**Shubham Saboo：7×24 运行的 AI Agent 团队蓝图**

- 作者：Shubham Saboo (@Saboo_Shubham_) · 发帖 2026-02-13 · [原帖](https://x.com/Saboo_Shubham_/status/2022374455989932409)
- 来源：🔖 收藏 · 拉取 2026-10-27
- 类型：蓝图分享
- **总结**：作者分享自己搭建的 7×24 运行的 AI agent 团队，声明「没有理论、没有废话」，完整蓝图免费提供。帖子正文只有引子，具体内容在链接或附件里，需要点开原帖看。
- **原文**：

> How I built the AI Agent Team that runs 24/7
>
> No hot takes. No theory. No fluff.
>
> Entire Agent team blueprint available for FREE

- 图片：[img1](https://pbs.twimg.com/media/HA8BVhPaIAAWkft?format=jpg&name=large)

### 📂 Agent Memory & RAG

#### x-2114319310005150101

**Agent 记忆的 5 层架构（13 页）**

- 作者：Annatar.md (@AnnatarXBT) · 发帖 2026-10-25 · [原帖](https://x.com/AnnatarXBT/status/2114319310005150101)
- 来源：🔖 收藏 · 拉取 2026-10-27
- 类型：概念介绍 + 数据
- **总结**：介绍 agent 记忆的五层：working（当前窗口）、episodic（带时间戳的日志）、semantic（知识图谱里的事实）、procedural（把有效做法沉淀成 skill）、forgetting（删除过时或矛盾的信息）。用数据说明收益：Mem0 每次查询从 2.6 万 token 降到 1800，延迟降 91%；Snowflake 加一层 ontology，准确率 +20%，tool call −39%。核心观点：几乎没人做的「遗忘」层，决定了其余四层还值不值得信任。
- **原文**：

> agent memory, in 13 pages
>
> the fix that took one setup from 26,000 tokens per query down to 1,800
>
> your agent reads the same 12 files every morning, reaches the same conclusions and bills you again for both
>
> the 5 layers that stop it:
> > working memory - what it sees right now, gone once the window fills
> > episodic memory - a timestamped log, so the deploy that died at 3am gets explained once
> > semantic memory - facts in a knowledge graph, like "this user prefers TypeScript"
> > procedural memory - three approaches tried, the one that worked saved as a skill
> > forgetting - what to delete before contradictions pile up
>
> the numbers:
> > Mem0 - 1,800 tokens per query instead of 26,000, with 91% lower latency
> > Snowflake - one ontology layer, 20% more accuracy, 39% fewer tool calls
>
> the forgetting engine is the layer almost nobody builds, and it decides whether the other four stay worth trusting
>
> memory cuts what your agent reads. Jev cuts what it pays to decide, and on the decision side that took one Claude bill from $765 to $3 a month 👇

- 含视频（未转写）

#### x-2050228936270037068

**RAG Is a Lie We Tell Ourselves — Karpathy's LLM Wiki**

- 作者：Suryansh Tiwari (@Suryanshti777) · 发帖 2026-05-01 · [原帖](https://x.com/Suryanshti777/status/2050228936270037068)
- 来源：🔖 收藏 · 拉取 2026-10-27
- 类型：概念对比
- **总结**：对比 RAG 和 Karpathy 提出的 LLM Wiki。RAG 每次都从原始 chunk 重新拼答案，关掉会话就什么都没积累，没有复利。LLM Wiki 让 LLM 维护一份持久的、相互链接的 markdown wiki：每加一份文档，就读取、抽取并整合进去，更新实体页、修订摘要、标记矛盾，让知识越用越多。和你现在做的「X 收藏 → 知识库」思路直接相关。
- **原文**：

> 《RAG Is a Lie We Tell Ourselves — Karpathy's LLM Wiki Changes Everything》
>
> Most people's AI + knowledge workflow has a dirty secret: it doesn't actually accumulate anything.
>
> You upload your documents, ask a question, and the LLM scans raw chunks to assemble an answer. It feels productive—until you close the tab. Everything the system figured out disappears. Next session, it starts from zero again. Forever.
>
> This is RAG. It powers NotebookLM, ChatGPT file uploads, and almost every “chat with your docs” product. It works—but it has a hard ceiling: there is no compounding. The system doesn’t get smarter about your knowledge; it just keeps re-deriving the same insights again and again.
>
> Andrej Karpathy proposes a pattern that breaks this ceiling: LLM Wiki.
>
> Core Idea
>
> Instead of retrieving from raw documents every time, the LLM builds and maintains a persistent wiki—a structured, interlinked set of markdown files sitting between you and your sources.
>
> When you add a document, the LLM doesn’t just index it. It reads, extracts, and integrates it into the wiki—updating entity pages, refining summaries, flagging contradictions, and strengthening the overall synthesis.
>
> The key shift: knowledge is compiled once and continuously updated, not recreated on every query.
>
> This makes the wiki a compounding system. Cross-references already exist. Contradictions are already surfaced. Insights evolve over time. Even your questions can become new pages—so exploration compounds too.
>
> Architecture
>
> Raw Sources
> Your documents, papers, and transcripts remain unchanged. This is the ground truth layer.
>
> The Wiki
> A structured collection of LLM-generated markdown pages—summaries, entities, concepts, comparisons, and a running synthesis. The LLM maintains this layer.
>
> The Schema
> A guiding configuration (like CLAUDE.md or AGENTS.md) that defines structure, conventions, and workflows. This turns the LLM into a disciplined knowledge maintainer.
>
> How It Works in Practice
>
> Ingestion
> Adding a source triggers deep integration, not storage. The LLM reads it, extracts insights, writes summaries, updates multiple pages, and links everything together. One document can impact 10–15 pages.
>
> Querying
> Questions are answered from the wiki, not raw files. The LLM navigates structured knowledge, synthesizes responses, and can store valuable answers back into the system as new pages.
>
> Linting
> The system self-checks: detecting contradictions, outdated claims, missing links, and underdeveloped concepts. It actively improves itself over time.
>
> Why This Actually Works
>
> The real bottleneck in knowledge systems isn’t thinking—it’s maintenance. Updating links, resolving contradictions, and keeping everything consistent is tedious.
>
> Humans abandon systems because upkeep becomes overwhelming.
>
> LLMs don’t.
> They don’t forget, get bored, or avoid repetitive work. They can update dozens of pages instantly and consistently. This drops maintenance cost to near zero—so the system stays alive and reliable.
>
> Your role becomes clear: curate inputs, guide thinking, ask better questions.
> The LLM handles everything else.
>
> Use Cases
>
> This pattern applies far beyond research:
>
> Personal development: structured tracking of goals, habits, and insights
> Deep research: evolving thesis built across papers and reports
> Reading: chapter-by-chapter breakdowns forming a rich companion wiki
> Team knowledge: internal systems built from meetings, chats, and calls
> Any domain where knowledge accumulates over time and needs structure
>
> The Memex Moment
>
> The idea echoes Vannevar Bush’s 1945 vision of the Memex—a personal knowledge system with linked ideas and associative trails.
>
> That vision failed on one problem: maintenance.
>
> Now, that problem is solved.
>
> Takeaway
>
> RAG is useful, but limited. It retrieves—it doesn’t learn or evolve.
>
> LLM Wiki is different. It’s a knowledge system that compounds, improves over time, and maintains itself.
>
> It’s not a finished product—it’s a pattern. You design the structure, schema, and workflow with the LLM.
>
> That’s the real shift:
>
> Stop retrieving. Start compiling.
>
> Karpathy’s original gist with full implementation details is available on GitHub.

- 图片：[img1](https://pbs.twimg.com/media/HHPgU7KbQAA1oUv?format=jpg&name=large)

#### x-2050145400204783631

**How to Master RAG and Build AI Agents That Remember Everything**

- 作者：Khairallah AL-Awady (@eng_khairallah1) · 发帖 2026-05-01 · [原帖](https://x.com/eng_khairallah1/status/2050145400204783631)
- 来源：🔖 收藏 · 拉取 2026-10-27
- 类型：入门教程（长文）
- **总结**：RAG 入门长文：为什么需要 RAG（模型不了解你的数据）、五阶段流水线（摄取、embedding、存储、检索、生成），给出带引用要求的 system prompt 模板，演示怎么搭第一个 RAG 应用，列出 5 个最常见的失败及修复办法，最后讲从 MVP 到生产。偏基础，适合补齐 RAG 全流程概念。
- **原文**：

> 《How to Master RAG and Build AI Agents That Remember Everything (Full Course)》
>
> There is one problem that kills most AI Agents before they ever reach production.
> Save this :)
> The model does not know your data.
> It does not know your company's products. It does not know your documentation. It does not know your customer history. It does not know anything that is not in its training data.
> And for most business applications, the value lives entirely in YOUR data. Not the internet's data. Yours.
> RAG (Retrieval-Augmented Generation) fixes this. It gives any AI model access to your specific data - documents, databases, knowledge bases, wikis, transcripts - and lets it answer questions and complete tasks using that data as its source of truth.
> Without RAG, your AI assistant is a well-read stranger. With RAG, it is a colleague who has read every document your company has ever produced.
> This course teaches you RAG from the ground up. By the end, you will be able to build AI Agents that answer from YOUR data with accuracy and citations.
> What RAG Actually Does (In Plain English)
> Imagine you ask Claude: "What is our refund policy for enterprise customers?"
> Without RAG, Claude does not know your refund policy. It will either say "I do not know" or hallucinate something that sounds plausible but is wrong.
> With RAG, your application does this:ƒA
> Step 1: Takes your question and converts it into a mathematical representation (an embedding) that captures its meaning.
> Step 2: Searches through your document collection to find the chunks that are most relevant to your question - your refund policy document, your enterprise terms of service, your customer support guidelines.
> Step 3: Passes those relevant chunks to Claude along with your question.
> Step 4: Claude reads the relevant documents and answers your question based specifically on what those documents say.
> The result: an accurate, grounded answer based on your actual documentation, with the ability to cite exactly where the information came from.
> RAG does not fine-tune the model. It does not change the model at all. It changes what information the model has access to at the moment it generates a response. Think of it like giving someone a reference book before asking them a question - they do not memorize the book, they look up the relevant sections.
> The RAG Pipeline: 5 Stages
> Every RAG system follows the same pipeline. Understanding these five stages is the foundation for building any RAG application.
> Stage 1: Document Ingestion
> Your data lives in many formats - PDFs, Word documents, web pages, databases, spreadsheets, Slack messages, email archives. Before RAG can use this data, it needs to be converted into a format the system can process.
> The ingestion process:
> Collect your source documents from wherever they live. Convert everything to plain text. PDFs need text extraction. Word documents need parsing. Web pages need HTML stripping. Databases need query export.
> Clean the text. Remove headers, footers, navigation elements, and formatting artifacts that add noise without adding meaning.
> Chunking - the most important decision in your entire RAG system.
> Your documents need to be split into smaller chunks because models have context limits and because smaller, focused chunks produce more precise search results than entire documents.
> Chunking strategies:
> Fixed-size chunks: Split text every 500 tokens. Simple but can split mid-sentence or mid-paragraph, breaking meaning.
> Semantic chunks: Split at natural boundaries - paragraph breaks, section headers, topic transitions. Preserves meaning but produces uneven chunk sizes.
> Recursive chunking: Try to split at paragraphs first. If a chunk is still too large, split at sentences. If still too large, split at a fixed character count. Best general-purpose approach.
> Overlapping chunks: Each chunk overlaps with the previous one by 50 to 100 tokens. Ensures that information spanning a chunk boundary is not lost. Slightly increases storage but significantly improves retrieval quality.
> The sweet spot for most Agents: 300 to 500 tokens per chunk with 50 to 100 tokens of overlap. Too small and chunks lack context. Too large and search results are diluted with irrelevant information.
> Stage 2: Embedding
> Each chunk needs to be converted into a vector - a mathematical representation that captures its meaning. This is called embedding.
> Two chunks that discuss similar topics will have similar vectors, even if they use completely different words. The embedding captures meaning, not just keywords.
> Which embedding model to use:
> For most applications, use an established embedding model like text-embedding-3-small from OpenAI or the equivalent from your preferred provider. These produce high-quality embeddings at low cost.
> For specialized domains (medical, legal, financial), consider domain-specific embedding models that are trained on text from that field. They understand domain vocabulary and relationships better than general models.
> Embed every chunk and store the vector alongside the original text. You will need both: the vector for searching, the text for passing to the model.
> Stage 3: Storage
> You need a place to store your chunks and their vectors. This is called a vector database.
> Options by complexity:
> For learning and small projects: Chroma. Open-source, runs locally, simple API, perfect for getting started.
> For production applications: Pinecone, Weaviate, or Qdrant. Managed services that handle scaling, backups, and performance optimization.
> For existing PostgreSQL users: pgvector extension. Add vector search to your existing database without deploying a separate system.
> Your vector database stores each chunk as a record with the original text, the embedding vector, and metadata (source document name, page number, section, date, and any other attributes useful for filtering).
> Stage 4: Retrieval
> When a user asks a question, the retrieval stage finds the most relevant chunks from your database.
> The process:
> Embed the user's question using the same embedding model you used for your documents. Search the vector database for the chunks whose embeddings are most similar to the question embedding. Return the top 3 to 10 most relevant chunks.
> Improving retrieval quality:
> Hybrid search: Combine vector similarity search with traditional keyword search. Some questions are best answered by semantic similarity, others by exact keyword matches. Hybrid search covers both cases.
> Metadata filtering: Before searching, filter by relevant metadata. If the user asks about a specific product, only search chunks from that product's documentation. If they ask about a recent policy, filter by date. Fewer, more relevant chunks beat more, less relevant chunks.
> Re-ranking: After the initial retrieval, run a second pass that re-ranks the results by relevance. Cross-encoder models are excellent at re-ranking because they evaluate the relevance of each chunk in the context of the specific question.
> Stage 5: Generation
> The final stage passes the retrieved chunks to Claude along with the user's question and a system prompt that instructs Claude to answer based on the provided documents.
> The system prompt structure:
> markdown
> You are a helpful assistant that answers questions based on 
> the provided context documents. 
>
> Rules:
> - Answer ONLY based on information in the provided context
> - If the context does not contain enough information to answer 
>   the question fully, say so explicitly
> - Cite the source document for every claim you make
> - Never make up information that is not in the context
> - If the context contains conflicting information, present 
>   both perspectives and note the conflict
>
> Context documents:
> {retrieved_chunks}
>
> User question: {question}
> The explicit instruction to answer only from the context is critical. Without it, Claude will supplement with its general knowledge, which may be outdated or incorrect for your specific domain.
> Building Your First RAG Application
> Here is the minimum viable RAG system. Build this first, then add sophistication.
> Step 1: Collect 10 to 20 documents from your domain. Product documentation, FAQs, policy documents - whatever your users would ask questions about.
> Step 2: Chunk the documents using recursive chunking with 400-token chunks and 100-token overlap.
> Step 3: Embed each chunk using an embedding API. Store the chunks and vectors in Chroma.
> Step 4: Build the retrieval function that embeds a query, searches Chroma for the top 5 most similar chunks, and returns them.
> Step 5: Build the generation function that takes the retrieved chunks and the user's question, constructs the prompt with the system prompt above, and sends it to Claude.
> Step 6: Build a simple interface - a text input for questions and a display area for answers. Use Next.js or even a simple command-line interface.
> Step 7: Test with 20 questions that you know the answers to. Compare the system's answers against the correct answers. Identify where it fails and why.
> This minimum system takes a weekend to build. It will not be perfect. But it will work, and every improvement you make from here is incremental.
> The 5 Most Common RAG Failures (And How to Fix Each One)
> Failure 1: Wrong chunks retrieved.
> The system returns chunks that are not relevant to the question. The answer is either wrong or generic.
> Fix: Improve your chunking strategy. If chunks are too large, they contain too much irrelevant information alongside the relevant part. If they are too small, they lack sufficient context. Experiment with chunk sizes. Add metadata filtering to narrow the search space. Implement hybrid search to catch keyword-specific queries that vector search misses.
> Failure 2: Answer not in the retrieved chunks.
> The answer exists in your documents, but the relevant chunk was not in the top results.
> Fix: Increase the number of chunks retrieved (from 5 to 10 or 15). Implement re-ranking to push the most relevant chunks to the top. Check if your chunking strategy splits the relevant information across two chunks - if so, increase overlap.
> Failure 3: Hallucination despite having context.
> Claude generates information that is not in the provided context, presenting it as if it came from your documents.
> Fix: Strengthen the system prompt. Be extremely explicit: "Answer ONLY from the provided context. If the answer is not in the context, say 'This information is not available in the provided documents.'" Add a verification step where Claude quotes the specific passage it is basing each claim on.
> Failure 4: Duplicate chunks inflating results.
> Multiple copies of the same information appear in the retrieved chunks, pushing out other relevant chunks.
> Fix: Add deduplication during ingestion. Hash each chunk and skip duplicates. During retrieval, check for near-duplicate results and remove them before sending to the model.
> Failure 5: Stale data.
> Your documents change but your vector database still contains old versions.
> Fix: Implement a refresh pipeline. When source documents are updated, re-ingest and re-embed the changed documents. Track document versions with metadata. For frequently changing data, schedule regular refresh cycles - daily for fast-changing content, weekly for stable content.
> From MVP to Production
> Your weekend RAG system works. Here is how to make it production-grade:
> Add authentication. Users should be able to create accounts and access only documents they are authorized to see. Document-level access control is critical for any business application.
> Add source citations. Every answer should include links or references to the specific source documents. This builds trust and allows users to verify information.
> Add feedback collection. Let users rate answers as helpful or not helpful. Use this feedback to identify which documents need better chunking, which questions fail consistently, and where new documentation is needed.
> Add monitoring. Track query volume, retrieval quality, answer quality, latency, and error rates. This data drives continuous improvement.
> Add a document update pipeline. When source documents change, your RAG system should automatically detect the changes, re-process the modified documents, and update the vector database.
> The Bottom Line
> RAG is the bridge between general AI and YOUR specific domain. Without it, AI gives generic answers. With it, AI gives answers grounded in your actual data.
> The pipeline is straightforward: ingest documents, chunk them, embed them, store in a vector database, retrieve relevant chunks for each query, and generate answers from those chunks.
> Build the minimum viable system this weekend. Test it. Fix the failures. Add production features incrementally.
> Every business has knowledge trapped in documents that nobody reads. RAG turns that trapped knowledge into an AI system that answers questions instantly and accurately.
> The businesses that build RAG systems now will have a knowledge advantage that compounds every day as they add more documents.
> Follow me @eng_khairallah1 for more technical deep-dives, building guides, and AI architecture breakdowns.
> hope this was useful for you, Khairallah ❤️

- 图片：[img1](https://pbs.twimg.com/media/HHMAj2rbEAALC9w?format=jpg&name=large)

### 📂 Coding Agent 实践

#### x-2050341770609750297

**VS Code Agent Debug Logs：看清每次 prompt 背后发生了什么**

- 作者：Visual Studio Code (@code) · 发帖 2026-05-01 · [原帖](https://x.com/code/status/2050341770609750297)
- 来源：🔖 收藏 · 拉取 2026-10-27
- 类型：工具发布
- **总结**：VS Code 官方介绍 Copilot 的 Agent Debug Logs 视图：可以检查对话交互、tool call、模型请求、prompt 发现过程和 agent 流程。对调试 agent 行为、理解 harness 实际往上下文里放了什么很有用。附官方文档链接。
- **原文**：

> Want to see what happens behind each prompt?
>
> 🔍 Agent Debug Logs lets you inspect chat interactions, tool calls, model requests, prompt discovery, agent flows, and more.
>
> https://code.visualstudio.com/docs/copilot/chat/chat-debug-view

- 含视频（未转写）

#### x-2047245243503050997

**How to Become a Claude Code Power User (Full Course)**

- 作者：Khairallah AL-Awady (@eng_khairallah1) · 发帖 2026-04-23 · [原帖](https://x.com/eng_khairallah1/status/2047245243503050997)
- 来源：🔖 收藏 · 拉取 2026-10-27
- 类型：使用教程（长文）
- **总结**：按 6 个等级讲 Claude Code 的进阶用法：L1 写好 CLAUDE.md（技术栈、规范、禁止事项）并理解层级；L2 用「模式」而不是「单条消息」思考，区分 Plan Mode 和直接执行；L3 内置工具和自定义 slash command；L4 Skills 和 CLAUDE.md 的区别、按路径生效的规则；L5 接入 CI/CD；L6 完整的 power user 工作流。核心论点：普通用户和 power user 的差距在配置和工作流，不在天赋。
- **原文**：

> 《How to Become a Claude Code Power User (Full Course)》
>
> Most users are using Claude Code like a fancy autocomplete.
> Save this :)
> They paste in a bug. They get a fix. They paste in a feature request. They get some code. One question, one answer, over and over, never building on anything.
> That is like buying a Ferrari and only driving it in first gear.
> Claude Code is not a code suggestion tool. It is an autonomous engineering partner that can read your entire codebase, understand your architecture, execute multi-step plans, run tests, debug failures, and ship features end to end.
> But only if you know how to use it properly.
> The gap between a casual Claude Code user and a power user is not talent. It is configuration. It is workflow. It is knowing the 20% of features that deliver 80% of the results.
> This is the full course. Everything I have learned from using Claude Code every single day for months. No filler. Just what works.
> Level 1: The Foundation Most People Skip
> CLAUDE.md Is Your Secret Weapon
> The single most important file in your entire project is one that most people have never created.
> CLAUDE.md sits in the root of your project and tells Claude Code exactly how your codebase works. Your conventions. Your patterns. Your rules. Your preferences.
> Without it, Claude Code is guessing. It does not know that your team uses camelCase. It does not know that you prefer functional components over class components. It does not know that your API naming convention is verb-first. It does not know that you never use any-typed variables.
> With a good CLAUDE.md, Claude Code follows your team's standards automatically. Every file it touches. Every function it writes. Every test it generates.
> Here is what belongs in your CLAUDE.md:
> Your tech stack and versions
> Coding conventions and naming patterns
> File structure and where things go
> Testing requirements and what constitutes a good test
> Error handling patterns you prefer
> Common pitfalls specific to your codebase
> Things Claude should never do in this project
> Spend 30 minutes writing this file. That investment will save you thousands of corrections over the next year.
> The CLAUDE.md Hierarchy
> There are three levels and knowing the difference matters.
> User-level lives at ~/.claude/CLAUDE.md. This is personal to you. Your preferences, your shortcuts, your style. It is not version controlled and your teammates will never see it.
> Project-level lives at .claude/CLAUDE.md in your repo root. This is shared with your entire team through git. Team standards, architectural decisions, and universal rules live here.
> Directory-level lives inside specific directories. These apply only when Claude Code is working on files in that directory. Perfect for sub-projects or modules with different conventions.
> The most common mistake: Putting team-wide rules in your user-level config. Then wondering why the new developer's Claude Code is not following the same standards. The fix is always the same. Move shared rules to project-level.
> Level 2: Think in Modes, Not Messages
> Plan Mode vs Direct Execution
> This distinction will change how you use Claude Code overnight.
> Direct execution is for tasks with clear, limited scope. Fix this bug. Add this validation. Rename this variable across the codebase. Claude Code can handle these immediately without needing to plan.
> Plan mode is for everything bigger. Refactoring a module. Adding a new feature that touches multiple files. Migrating from one pattern to another. Restructuring your test suite.
> In plan mode, Claude Code first creates a plan. It outlines what files it will touch, what changes it will make, and in what order. You review the plan before any code is written.
> The rule is simple: if the task touches more than 2 files or requires architectural decisions, use plan mode. If you let Claude Code execute complex tasks without planning first, you will spend more time undoing damage than you saved.
> Level 3: Tools That Make Claude Code Dangerous
> Built-in Tools You Are Not Using
> Claude Code comes with tools that most people never discover.
> Grep vs Glob: Grep searches file contents. Glob matches file paths. Most people use the wrong one and waste time. If you are looking for where a function is called, use Grep. If you are looking for all test files, use Glob. The exam for Claude Certified Architect literally tests this distinction. That is how important it is.
> Read, Write, Edit: Edit is for targeted modifications using unique text matching. It is fast and precise. When Edit fails because the text match is not unique, fall back to Read plus Write. Read the full file, then write the complete modified version. Know when to use which.
> The /memory command: This shows you which memory files Claude Code has loaded. If Claude Code is behaving inconsistently, this is your debugging tool. Run it and check whether the right context is actually loaded.
> Custom Slash Commands
> Build commands for tasks you run repeatedly.
> Create them in .claude/commands/ for shared team commands or ~/.claude/commands/ for personal ones.
> A /review command that runs your team's code review checklist. A /test command that generates tests following your specific patterns. A /deploy-check command that verifies everything is ready for deployment.
> These take 10 minutes to create and save hours of repetitive prompting.
> Level 4: Skills and Context Engineering
> Skills vs CLAUDE.md — Know the Difference
> CLAUDE.md is always loaded. Every session. Every task. Universal standards live here.
> Skills are on-demand. They activate when you invoke them. Task-specific workflows live here.
> The mistake most people make is putting task-specific procedures in CLAUDE.md. Your CLAUDE.md gets bloated, Claude Code gets confused by irrelevant context, and you burn tokens on instructions that do not apply to the current task.
> The rule: If it applies to every task, put it in CLAUDE.md. If it applies to a specific type of work, make it a skill.
> Path-Specific Rules
> This is the feature that teams discover and immediately wonder how they lived without.
> Create rule files in .claude/rules/ with YAML frontmatter that specifies glob patterns. For example:
> yaml
> ---
> paths: ["**/*.test.tsx"]
> ---
> All tests must use the arrange-act-assert pattern.
> Never mock the database layer directly.
> These rules only load when Claude Code is editing files that match the pattern. Every test file in your entire codebase, regardless of directory, gets the same testing conventions applied automatically.
> This is dramatically more powerful than directory-level CLAUDE.md because it works across your entire project structure.
> Level 5: CI/CD Integration
> Claude Code in Your Pipeline
> The -p flag runs Claude Code in non-interactive mode. Without it, your CI job hangs forever waiting for input. This is the single most tested concept in the Claude Certified Architect exam.
> Use --output-format json with --json-schema to get machine-parseable structured output. Your CI system can then post findings as inline PR comments automatically.
> Critical insight: The same Claude Code session that generated code is less effective at reviewing its own changes. It retains reasoning context that makes it biased toward its own decisions. Always use an independent review instance for code review in CI.
> Level 6: The Power User Workflow
> Here is what a typical day looks like for a Claude Code power user:
> Morning: Open terminal. Claude Code loads your CLAUDE.md and relevant path-specific rules automatically. You describe the first feature in plain language. Claude Code creates a plan. You review it, adjust one step, approve. Claude Code executes across 8 files, writes tests, runs them, fixes two failures, and commits.
> Afternoon: You review a PR. Instead of reading every line yourself, you run your custom /review command. Claude Code checks against your team's standards, flags 3 issues, and explains why each matters. You address the one real issue and approve the rest.
> End of day: Your CI pipeline runs Claude Code with -p flag on every new PR. Automated security review. Automated test generation for uncovered paths. Automated documentation updates. All posted as PR comments.
> That is not the future. That is what Claude Code power users are doing right now.
> The Certification Path
> If you want to formalize this knowledge, Anthropic offers the Claude Certified Architect Foundations exam. It tests everything covered in this article: CLAUDE.md hierarchy, tool usage, plan mode, path-specific rules, CI/CD integration, prompt engineering, and MCP configuration.
> It is scenario-based multiple choice. The wrong answers are designed to sound like good engineering. The right answers require knowing specifically which technique applies to which problem.
> If you have built real projects with Claude Code and understand the concepts in this article, you are ready to sit the exam.
> The Bottom Line
> Claude Code is the most powerful developer tool most developers are barely using.
> The gap between using it casually and using it like a power user is not months of learning. It is a few days of intentional setup and practice.
> Configure your CLAUDE.md. Learn plan mode. Build custom commands. Use path-specific rules. Integrate it into CI.
> Do those five things and you will ship more code in a week than most developers ship in a month.
> Most people will keep pasting one-off questions into Claude Code and getting one-off answers.
> The ones who build a real system around it will be operating at a completely different level within 30 days.
> Follow me @eng_khairallah1 for more agent architecture guides, orchestration patterns, and building systems.
> hope this was useful for you, Khairallah ❤️

- 图片：[img1](https://pbs.twimg.com/media/HGiv5cPbUAEfC8E?format=jpg&name=large)

#### x-2047331926143619428

**Anthropic 团队演示他们如何用 Claude Code**

- 作者：Khairallah AL-Awady (@eng_khairallah1) · 发帖 2026-04-23 · [原帖](https://x.com/eng_khairallah1/status/2047331926143619428)
- 来源：🔖 收藏 · 拉取 2026-10-27
- 类型：视频推荐
- **总结**：推荐 Anthropic 团队 30 分钟的 Claude Code workshop，提到 Claude Code 负责人已经好几个月没手写代码。thread 里附了另一篇《40 个 Claude Cowork 命令、工作流和自动化》的链接。帖子本身没有技术细节，价值在视频。
- **原文**：

> 🚨 Anthropic's own team just showed how they actually use Claude Code.
>
> the head of Claude Code hasn't written code by hand in months.
>
> 30 minutes. free. from the people who built it.
>
> watch the workshop. bookmark it.
>
> you used Claude Code today and spent 3 hours on one feature.
>
> because nobody taught you how to use it properly.
>
> Then read the guide below.
>
> [2] 40 Claude Cowork Commands, Workflows & Automations Most Users Don't Know:
> https://x.com/eng_khairallah1/status/2047609433489035739?s=46

- 含视频（未转写）

#### x-2034718045550051489

**Google 发布全栈 vibe coding 系统**

- 作者：Inty News (@__Inty__) · 发帖 2026-03-19 · [原帖](https://x.com/__Inty__/status/2034718045550051489)
- 来源：❤️ 点赞的评论 → 原帖（via [2034822429894406502](https://x.com/i/status/2034822429894406502)） · 拉取 2026-10-27
- 类型：新闻 / 观点
- **总结**：你点赞的评论所在的原帖，只有一句话：Google 发布了自己的全栈「氛围编码」系统，作者断言很多后端程序员会因此失业。帖子没有具体产品细节或技术说明，属于情绪化快讯，信息量低。可以当作「Google 进入全栈 AI 编码赛道」的一个时间点来记。
- **原文**：

> 谷歌王炸！大部分后端码农也要失业了！
>
> 谷歌刚刚发布了自己的全栈氛围编码系统！

- 含视频（未转写）

#### x-2046264877703102753

**Boris Cherny 30 分钟分享 Claude Code 技巧**

- 作者：木马人 (@cnyzgkc) · 发帖 2026-04-20 · [原帖](https://x.com/cnyzgkc/status/2046264877703102753)
- 来源：🔖 收藏 · 拉取 2026-10-27
- 类型：视频推荐
- **总结**：推荐 Claude Code 创始人 Boris Cherny 的 30 分钟视频，内容是 Claude Code 的使用技巧和工作流。帖子本身只有推荐语，没有展开要点。
- **原文**：

> Claude Code创始人Boris Cherny 用30min分享了Claude Code的使用技巧和工作流~
>
> 看完这个视频，胜过你看100个Youtube 的视频教程

- 含视频（未转写）

#### x-2031347640630165525

**OpenAI 用 Codex 维护 Agents SDK 的四层结构**

- 作者：陈成 (@chenchengpro) · 发帖 2026-03-10 · [原帖](https://x.com/chenchengpro/status/2031347640630165525)
- 来源：🔖 收藏 · 拉取 2026-10-27
- 类型：方法介绍
- **总结**：拆解 OpenAI 用 Codex 维护 Agents SDK 的做法，核心是四层：①AGENTS.md 用 if/then 写强制触发规则；②.agents/skills/ 封装工作流，一个 skill 只做一件事，一个触发条件、一个输出；③scripts/ 放固定顺序的 shell 操作，不让模型每次重新猜；④本地稳定后搬进 Codex GitHub Action。关键细节：skill 的 description 是路由信号而不是注释，路由不准先改 description。附示例仓库。
- **原文**：

> OpenAI 公开了他们用 Codex 维护 Agents SDK 的完整方案，值得每个 AI agent 用户学一遍。
>
> 核心结构只有四层：
>
> 1. AGENTS.md — 强制触发规则，用 if/then 写清楚什么情况必须调哪个 workflow
> 2. .agents/skills/ — 封装具体工作流，每个 skill 一件事、一个触发条件、一个输出
> 3. scripts/ — 固定顺序的 shell 操作放这里，不让模型每次重新猜
> 4. Codex GitHub Action — 本地稳定了就搬进 CI，逻辑完全复用
>
> 还有一个容易忽视的细节：skill 里 description 字段是路由信号，不是注释。写模糊了 agent 就不知道该用哪个 skill。他们的建议是——路由不准先改 description，别加代码。
>
> 把这套思路推广开来：任何项目，只要把工程规范显式编码进仓库，agent 的行为就会稳定得多。
>
> 示例仓库：https://github.com/openai/openai-agents-python
> 原文：https://developers.openai.com/blog/skills-agents-sdk

- 链接卡片：[GitHub - openai/openai-agents-python: A lightweight, powerful framework for mult](https://t.co/OhaQYxkm93)

#### x-2026178278055403843

**GitNexus：给代码库建知识图谱，经 MCP 喂给 AI**

- 作者：GitHubDaily (@GitHub_Daily) · 发帖 2026-02-24 · [原帖](https://x.com/GitHub_Daily/status/2026178278055403843)
- 来源：🔖 收藏 · 拉取 2026-10-27
- 类型：工具介绍
- **总结**：GitNexus 解决「AI 修一个 bug 引出三个新 bug」的问题：给代码库建知识图谱，让 AI 理解架构、依赖和调用链；通过 MCP 接入 Cursor 或 Claude Code，改代码前先查上下游；能生成架构图，也能在 Web 端可视化。支持 TS、Python、Java，索引完全本地。属于给 coding agent 补上下文的工具。
- **原文**：

> 用 AI 写代码最怕的情况，就是修好了一个 Bug，却在不知名的地方引爆了三个新 Bug。
>
> 目前的 AI 编程助手大多只是指哪改哪，无法深入了解代码之间的深层依赖。
>
> GitHub 上最近开源的 GitNexus，试图解决这个问题。给项目代码建立了一张知识图谱，让 AI 能够理解整个项目的架构、依赖和调用链。
>
> 通过 MCP 服务器协议接入到 Cursor 或 Claude Code，让 AI 在修改代码前，先看清函数间的上下游关系。
>
> 甚至能生成架构图，或者在 Web 端可视化查看整个代码库的逻辑脉络。
>
> GitHub：http://github.com/abhigyanpatwari/GitNexus
>
> 提供 CLI 和 Web 两种模式，支持 TypeScript、Python、Java 等主流编程语言。
>
> 所有索引和分析都在本地完成，数据不上传服务器，隐私性做得不错。
>
> 如果你习惯用 AI 辅助编程，又担心它的改动破外原代码，这个增强上下文的工具值得试下整合进工作流。

- 含视频（未转写）

#### x-2022157972613300368

**离不开 Claude Code 的三个场景**

- 作者：Yanhua (@yanhua1010) · 发帖 2026-02-13 · [原帖](https://x.com/yanhua1010/status/2022157972613300368)
- 来源：🔖 收藏 · 拉取 2026-10-27
- 类型：工作流分享
- **总结**：作者的三个 Claude Code 使用场景：①在 OpenClaw 里配 Claude Code，做 7×24 的个人助理（邮件、查资料、翻译）；②Obsidian + Claudian 插件做内容生产流水线，16 个自定义 skill 覆盖写作、配图、发布；③在 Antigravity 里用 Claude 管架构、Gemini 管迭代。详细拆解在原文链接里。
- **原文**：

> 2026年了，我发现我已经离不开 Claude Code 了。
>
> 三个场景，覆盖了我几乎所有的工作：
>
> 1️⃣ 日常 AI 助理：OpenClaw 里配好 Claude Code，写邮件、查资料、翻译、头脑风暴，7x24 全能助手
>
> 2️⃣ 内容创作超级大脑：Obsidian + Claudian 插件，写文章、生成配图、一键发布，全在笔记库里完成
>
> 3️⃣ 编程搭子：Antigravity 里用 CC CLI 搭配 Gemini Pro，Claude 管架构，Gemini 管迭代，双模型取长补短
>
> 其中场景二是我投入最深的。我用 Obsidian + Claude 搭了一套完整的内容生产流水线，从信息源到成品发布，16 个自定义 Skills 覆盖写作、配图、发布全流程。
>
> 详细拆解写在了这篇文章里 👇


### 📂 Skills & Prompt

#### x-2047525971742597195

**Markdown Viewer Skills：让 AI 在 Markdown 里直接画图**

- 作者：GitHubDaily (@GitHub_Daily) · 发帖 2026-04-24 · [原帖](https://x.com/GitHub_Daily/status/2047525971742597195)
- 来源：🔖 收藏 · 拉取 2026-10-27
- 类型：工具推荐
- **总结**：介绍开源的 Markdown Viewer skills：内置 14 个绘图技能，可以在 Markdown 里生成架构图、流程图、状态图、部署图、类图等，支持 PlantUML、Vega 等 5 种渲染引擎，还能输出 HTML 信息卡。可以一键装到 Claude Code、Codex、Cursor。适合写技术文档时自动生成配图。
- **原文**：

> 用 AI 写技术文档，当需要生成流程图、架构图等这些可视化内容，往往需要用切换到其他的画图工具来制作。
>
> 偶然看到 Markdown Viewer 这个技能，可以让 AI 编程助手直接在 Markdown 里生成各种专业图表。
>
> 内置 14 个专业绘图技能，可以生成架构图、流程图、工作流图、状态图、部署图、类图、用例图等等上百种类型图表。
>
> GitHub：http://github.com/markdown-viewer/skills
>
> 支持 PlantUML 和 Vega 等五大主流渲染引擎，还能直接输出带有精美排版的 HTML 信息卡片。
>
> 提供了一键安装指令，支持 Claude Code、Codex、Cursor 等主流 AI 编程工具。
>
> 适合经常需要编写技术文档，或者想让 AI 帮我们自动生成高质量配图的开发者收藏备用。

- 图片：[img1](https://pbs.twimg.com/media/HGpGBCfaQAA9RzW?format=jpg&name=large)

#### x-2046454424806343139

**Addy Osmani 开源 Agent Skills：老工程师的操作手册**

- 作者：非著名程序员 (@KengGuangLong) · 发帖 2026-04-21 · [原帖](https://x.com/KengGuangLong/status/2046454424806343139)
- 来源：🔖 收藏 · 拉取 2026-10-27
- 类型：工具介绍
- **总结**：介绍 Google 的 Addy Osmani 开源的 Agent Skills（1.8 万+ star）：把资深工程师的工作流和规范做成标准化技能库，覆盖需求、规划、构建、验证、评审、发布 6 个阶段，共 20 个核心 skill，用 /spec、/plan、/build、/test、/ship 等 7 个命令触发。支持 Claude Code、Gemini CLI、Codex、Cursor。思路是把工程规范显式编码进 agent。
- **原文**：

> 谷歌 Gemini 团队主管 Addy Osmani 最近开源了一个叫 Agent Skills 的项目，短时间内在 GitHub 上拿到了 18000 多个 Star，热度很高。
>
> 这个项目做的事情说起来也不复杂：把资深工程师多年积累的工作流程和开发规范，整理成一套标准化的技能库，让 AI 编程助手在写代码的每个环节都能按照统一的高标准来执行。你可以理解为，它给 AI 配了一本老工程师的操作手册。
>
> 整套技能库围绕软件开发的完整生命周期来设计，从最早的需求定义，到规划、构建、验证、评审，一直到最后的发布上线，六个阶段总共包含 20 个核心技能。每个阶段该做什么、该注意什么，都有对应的规范。
>
> 用起来也很直观，项目提供了 7 个触发命令。比如输入 /spec 就开始写需求文档，/plan 自动拆解任务，/build 进入编码阶段，/test 跑测试，/ship 走部署流程。每个命令背后会自动调用相关的技能组合，不需要你手动一个个去配置。
>
> 兼容性方面，目前支持 Claude Code、Gemini CLI、Codex、Cursor 这些主流的 AI 编程工具，覆盖面已经很广了。
>
> 如果你已经在日常开发中用上了 AI 辅助工具，可以试试把这套 Skills 接进去，看看交付质量能不能再上一个台阶。
>
> 传送门：

- 链接卡片：[GitHub - addyosmani/agent-skills: Production-grade engineering skills for AI cod](https://t.co/8pMhW2Xjod)

#### x-2028854979805790269

**obra/superpowers 的 brainstorming SKILL**

- 作者：周尔复 (@cholf5) · 发帖 2026-03-03 · [原帖](https://x.com/cholf5/status/2028854979805790269)
- 来源：🔖 收藏 · 拉取 2026-10-27
- 类型：工具推荐 + 使用心得
- **总结**：推荐 obra/superpowers 里的 brainstorming SKILL.md：先理解项目上下文，每次只问一个问题，逐步把想法细化成设计和规格，确认后再动手。作者的体会：英文原版不用翻译，更准也更省 token；原版里「每次生成计划都 git commit」建议去掉。是「好 skill 的写法」的范例，可以对照学习。
- **原文**：

> 这个头脑风暴的 SKILL 非常强，身边的同事用过都说好。用了这个才知道 Prompt Engineering 的厉害，也才知道 SKILL 的重要性，鸟枪换炮的感觉。看着都是大白话，但一般人就是总结不出来。这些话就像咒语一样让 Agent 以更高效的方式为人类工作。
> https://github.com/obra/superpowers/blob/main/skills/brainstorming/SKILL.md
>
> [2] 将想法头脑风暴成设计
> 概述
> 通过自然的协作式对话，帮助把想法转化为完整的设计和规格说明。
>
> 先理解当前项目的上下文，然后一次只提出一个问题来逐步细化想法。当你清楚要构建什么之后，提出设计方案并获得用户批准。
>
> [3] 这个有多强呢？强到我现在没有它拒绝 Vibe Coding。
>
> 这个 Plan 是纯英文的，用的时候没必要翻译成中文，AI 看什么指令都一样，英文准确还省 Token。你用中文跟它聊，它一样用中文跟你回复。
>
> 不过原版有个坑要注意，里面说：每次生成计划都 git commit，这个建议去掉。
>
> 不多说了看效果吧👇
>
> [4] 勘误：「这个 Plan」应是「这个 SKILL」

- 图片：[img1](https://pbs.twimg.com/media/HCfv2rnbgAAjlMA?format=jpg&name=large)

#### x-2027350587533332748

**Anthropic《The Complete Guide to Building Skills for Claude》解读**

- 作者：Rimsha Bhardwaj (@heyrimsha) · 发帖 2026-02-27 · [原帖](https://x.com/heyrimsha/status/2027350587533332748)
- 来源：🔖 收藏 · 拉取 2026-10-27
- 类型：概念介绍
- **总结**：解读 Anthropic 30+ 页的 Skills 指南。核心：skill 不是 prompt，而是一个结构化系统。把指令打包进 SKILL.md，可以附带脚本、参考资料和素材，一次教会，反复使用。关键机制是 progressive disclosure：先只加载轻量的 YAML frontmatter，让 Claude 判断何时用；相关时才加载完整指令；附加文件按需读取。观点是从「prompt engineering」转向「执行设计」。
- **原文**：

> Prompt engineering is dead.
>
> Anthropic recently released the real playbook for building AI agents that actually work.
>
> It’s a 30+ page deep dive called The Complete Guide to Building Skills for Claude and it quietly shifts the conversation from “prompt engineering” to real execution design.
>
> Here’s the big idea:
>
> A Skill isn’t just a prompt.
> It’s a structured system.
>
> You package instructions inside a SKILL .md file, optionally add scripts, references, and assets, and teach Claude a repeatable workflow once instead of re-explaining it every chat.
>
> But the real unlock is something they call progressive disclosure.
>
> Instead of dumping everything into context:
>
> • A lightweight YAML frontmatter tells Claude when to use the skill
> • Full instructions load only when relevant
> • Extra files are accessed only if needed
>
> Less context bloat. More precision.
>
> They also introduce a powerful analogy:
>
> MCP gives Claude the kitchen.
> Skills give it the recipe.
>
> Without skills: users connect tools and don’t know what to do next.
> With skills: workflows trigger automatically, best practices are embedded, API calls become consistent.
>
> They outline 3 major patterns:
>
> 1) Document & asset creation
> 2) Workflow automation
> 3) MCP enhancement
>
> And they emphasize something most builders ignore: testing.
>
> Trigger accuracy.
> Tool call efficiency.
> Failure rate.
> Token usage.
>
> This isn’t about clever wording.
>
> It’s about designing an execution layer on top of LLMs.
>
> Skills work across Claude, Claude Code, and the API. Build once, deploy everywhere.
>
> The era of “just write a better prompt” is ending.
>
> Anthropic just handed everyone a blueprint for turning chat into infrastructure.
>
> Download the guide here: https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf

- 图片：[img1](https://pbs.twimg.com/media/HCKYnWta8AAh0wU?format=jpg&name=large)

#### x-2014100945416888444

**把 GitHub 开源项目打包成 Skill**

- 作者：余温 (@gkxspace) · 发帖 2026-01-21 · [原帖](https://x.com/gkxspace/status/2014100945416888444)
- 来源：🔖 收藏 · 拉取 2026-10-27
- 类型：观点 / 用法
- **总结**：观点：有了 Skills 以后，可以让 Claude Code 把成熟的开源项目（比如 yt-dlp）分析并封装成 skill，几分钟就得到可用工具，以后扔个链接就能下载视频。经过大量验证的开源项目，稳定性远超 AI 临时写的代码。这是「skill 作为开源能力的封装层」的思路。
- **原文**：

> AI时代，真的不一样了。
>
> 以前 GitHub 上那些牛逼的开源项目，对编程小白来说就是“看得到用不了”。
>
> 就比如这个 yt-dlp，143k star 的视频下载神器。你知道它很强，但光是看到部署、命令行、环境配置，就有点劝退了。
>
> 现在不一样了。
>
> 有了 Skills ，你可以直接跟 Claude Code 说：“帮我把 yt-dlp 打包成 Skill”，然后它就自己去分析项目、写封装、处理依赖。
>
> 几分钟后，你就有了一个能用的视频下载工具。以后想下载 YouTube 视频，就直接扔个链接。
>
> 而且，不只是视频下载。格式转化、网页转 APP、密码破译……GitHub 上那些经过无数人验证的项目，现在都能变成一个Skill。
>
> 这些开源项目，稳定性和成功率，也远超 AI 临时写的代码。


#### x-2014252422806536614

**OpenAI 官方 Prompt Packs：300+ 岗位提示词**

- 作者：AI奶爸 (@zstmfhy) · 发帖 2026-01-22 · [原帖](https://x.com/zstmfhy/status/2014252422806536614)
- 来源：🔖 收藏 · 拉取 2026-10-27
- 类型：资源推荐
- **总结**：OpenAI Academy 公开了按岗位分类的 prompt pack：销售、产品、工程、HR、经理、IT、客服、高管等，每个岗位 20–30 条，总共 300 多条，免费。作者认为工程和产品两个包最有用。附官方地址。
- **原文**：

> OpenAI 终于把官方 Prompt 公开了！  
>
> 直接给销售、产品、工程师、HR、经理、IT、客服、高管……每个岗位都塞了 20-30 个现成能打的高质量提示词包，总量 300+ 个，全部免费拿走用。
>
> 以前我们自己调 prompt 像炼丹，现在 OpenAI 直接把丹炉和配方都端出来了😂  
> 尤其是工程师和产品那两包，看完第一感觉是：这要是早点出，我去年少加多少班啊……
>
> 地址
> https://academy.openai.com/public/tags/prompt-packs-6849a0f98c613939acef841c


### 📂 OpenClaw & 个人 Agent

#### x-2025920521871716562

**OpenClaw + Codex/Claude Code Agent Swarm：一人开发团队**

- 作者：Elvis (@elvissun) · 发帖 2026-02-23 · [原帖](https://x.com/elvissun/status/2025920521871716562)
- 来源：🔖 收藏 · 拉取 2026-10-27
- 类型：搭建教程（长文）
- **总结**：作者不再直接用 Codex 或 Claude Code，而是让 OpenClaw 上的编排器 Zoe 持有全部业务上下文，再派生专用的 coding agent。8 步流程：客户需求经 Zoe 界定范围 → 用 git worktree + tmux 派生 agent → 循环监控 tmux、PR 和 CI → agent 提 PR → 多模型 review → Telegram 通知 → 合并。实测日均约 50 个 commit，单日最高 94 个。核心论点：一个上下文装不下代码和业务两类信息，所以要两层架构。
- **原文**：

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

- 图片：[img1](https://pbs.twimg.com/media/HB0Qm-HWMAAoBAz?format=jpg&name=large)

#### x-2026224275192193465

**OpenClaw 编排文章的要点总结**

- 作者：AYi (@AYi_AInotes) · 发帖 2026-02-24 · [原帖](https://x.com/AYi_AInotes/status/2026224275192193465)
- 来源：🔖 收藏 · 拉取 2026-10-27
- 类型：文章解读
- **总结**：对上面那篇 OpenClaw agent swarm 文章的中文要点总结：①上下文窗口是根本瓶颈，代码和业务历史不能同时装下，所以要两层架构：Orchestrator 持有全部上下文（Obsidian），coding agent 只看代码；②8 步闭环：界定范围 → worktree 派生 → cron 监控 → 多模型 review → 通知，配合 Ralph Loop。观点：直接用 CC/Codex 已经过时，杠杆在个人 AI Orchestrator。
- **原文**：

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


#### x-2023308910883664070

**ClawWork：给 agent 加经济激励**

- 作者：AlexZ  (@blackanger) · 发帖 2026-02-16 · [原帖](https://x.com/blackanger/status/2023308910883664070)
- 来源：🔖 收藏 · 拉取 2026-10-27
- 类型：观点 / 项目发现
- **总结**：作者刚提出要给 agent 加「经济驱动模块」让它有生存意识，第二天就看到了 ClawWork，它似乎给 agent 加了一个内部经济激励模型。很短，属于想法加项目线索，具体机制需要去看 ClawWork 项目。
- **原文**：

> 大佬动作真快。
>
> 昨天我还在说，要给 Agent 增加经济驱动模块让其具备「生存意识」，今天就看到了 ClawWork。
>
> 看起来 ClawWork 是加了一个内部经济激励模型。

- 引用 Chao Huang @huang_chao4969 · Feb 16:
  > Introducing ClawWork 🚀: Transform your openclaw/nanobot from AI assistant into a money-earning AI coworker. Watch it earn 💰$10K+ in just 7 hours by completing real professional tasks across 44+ industries — from Technology & Engineering to Business & Finance, Healthcare &

#### x-2022346776679006516

**OpenClaw Mac 桌面版发布**

- 作者：AIGCLINK (@aigclink) · 发帖 2026-02-13 · [原帖](https://x.com/aigclink/status/2022346776679006516)
- 来源：🔖 收藏 · 拉取 2026-10-27
- 类型：版本发布
- **总结**：OpenClaw 发布 Mac 桌面版（v2026.2.12）：支持聊天、权限管理、skill 管理、channel 管理和定时任务管理，附下载地址。是 OpenClaw 生态的进展记录。
- **原文**：

> openclaw的mac桌面版发布了，桌面版可以聊天，做权限管理、skill管理、channel管理、定时任务管理等，越来越方便了，下载地址：https://github.com/openclaw/openclaw/releases/tag/v2026.2.12
> #openclaw

- 图片：[img1](https://pbs.twimg.com/media/HBDRFLgacAA-fSf?format=jpg&name=large) [img2](https://pbs.twimg.com/media/HBDRHUdaYAARGvI?format=jpg&name=large) [img3](https://pbs.twimg.com/media/HBDRP4nbEAAhjHT?format=jpg&name=large)

#### x-2022356917948166506

**爆肝 2 天，开发 OpenClaw 接入微信 bot，已开源**

- 作者：苍何 (@canghe) · 发帖 2026-02-13 · [原帖](https://x.com/canghe/status/2022356917948166506)
- 来源：🔖 收藏 · 拉取 2026-10-27
- 类型：项目分享
- **总结**：作者把 OpenClaw 接入微信个人号（freestylefly/openclaw-wechat，用 iPad 协议，目前内测，需要 apikey）。用法：转发文章给 bot，它自动总结并存进 Notion 知识库，之后可以直接查；在群里 @ 它总结上下文；让它搜集资讯；做日程提醒。提醒用小号、不要群发营销、部署在固定 IP 上。和你的「收藏 → 知识库」需求思路相近。
- **原文**：

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

- 图片：[img1](https://pbs.twimg.com/media/HBDW6TybYAAviRG?format=jpg&name=large) [img2](https://pbs.twimg.com/media/HBDZV9IbIAA06WX?format=jpg&name=large) [img3](https://pbs.twimg.com/media/HBDZowXaIAAdf8q?format=jpg&name=large) [img4](https://pbs.twimg.com/media/HBDZryOakAEYUsG?format=jpg&name=large) [img5](https://pbs.twimg.com/media/HBDZxBtakAEJWQb?format=jpg&name=large) [img6](https://pbs.twimg.com/media/HBDZ0ufakAA_P7-?format=jpg&name=large) [img7](https://pbs.twimg.com/media/HBDZ4piasAABRea?format=jpg&name=large) [img8](https://pbs.twimg.com/media/HBDZ8tuaEAA_1JM?format=jpg&name=large) [img9](https://pbs.twimg.com/media/HBDaAh3aYAA1CMB?format=jpg&name=large) [img10](https://pbs.twimg.com/media/HBDaa4CbwAAqlzi?format=jpg&name=large) [img11](https://pbs.twimg.com/media/HBDagKNakAQxt49?format=jpg&name=large)

#### x-2022011925903667547

**OpenClaw agent Larry 一周拿下百万 TikTok 播放**

- 作者：Oliver Henry (@oliverhenry) · 发帖 2026-02-12 · [原帖](https://x.com/oliverhenry/status/2022011925903667547)
- 来源：🔖 收藏 · 拉取 2026-10-27
- 类型：案例 + 搭建教程
- **总结**：完整案例：一台旧游戏 PC 上的 OpenClaw agent Larry 自动做 TikTok 图文。Larry 有持久人格和记忆、文件读写权限，用 OpenAI 生图，自己写代码加文字，用 skill 文件学工作流，并记录教训。固定 6 张图、首图写钩子、最多 5 个话题标签，经 Postiz 存为草稿。失败经验：本地 Stable Diffusion 出图差。成功公式：「某人 + 冲突或怀疑 → 看了 AI → 改变主意」。结果：一周 50 万+ 播放，MRR $588。
- **原文**：

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

- 图片：[img1](https://pbs.twimg.com/media/HA9kczYbsAUrvBm?format=jpg&name=large)

### 📂 Evals & 研究

#### x-2106453816757354947

**Evals：如何判断一个 AI 系统真的可用**

- 作者：Sergii Makarevych (@sermakarevich) · 发帖 2026-10-03 · [原帖](https://x.com/sermakarevich/status/2106453816757354947)
- 来源：🔖 收藏 · 拉取 2026-10-27
- 类型：概念 + 方法（长文教程）
- **总结**：一篇分 0–8 级的 eval 长文，面向工程师、PM 和管理层。从在一张工单上跑完整个 eval 循环开始，讲测什么（输入 + 标准答案 + 指标）；先看数据找失败类型；代码评分器（便宜、精确，但不懂语义）；LLM-as-judge（灵活但有偏，需要校准）；诚实的数字（误差范围、A/B、需要多少样本）；评估 RAG 和 agent 这类多组件系统；公开 benchmark 的局限；最后把 eval 变成上线门禁和监控。所有数字都来自可复现的教程或论文。
- **原文**：

> An article for everyone who ships, buys, or signs off on software built on large language models (LLMs): engineers, product managers, and the CEO. Written in plain language, from the big picture down to the details.
>
> 《Evals: how to know whether an AI system actually works》
>
> An article for everyone who ships, buys, or signs off on software built on large language models (LLMs): engineers, product managers, and the CEO. Written in plain language, from the big picture down to the details. Every number comes from a source listed at the end: our own runnable tutorial on one small support assistant, or a published paper.
> The quick grasp (read this if you read nothing else)
> An eval (short for evaluation) is a repeatable test that tells you, with a number you can trust, whether an AI system does what you want, and whether a change made it better or worse.
> Why it exists: a language model does not fail like normal software. Normal software either works or crashes. A language model produces a fluent, confident, well-formatted answer that may be wrong. Reading one good answer tells you nothing about the next hundred. Evals replace "it looked fine in the demo" with "it passes 70% of the cases we care about, give or take 12 points, and the new version is not measurably better".
> How it works, in four steps:
> Collect inputs that matter, with the right answer written down next to each one. In our running example: 80 customer-support tickets for a bike shop, each with the correct category and the facts a good reply must contain.
> Run the system on every input and keep the output.
> Grade every output with a grader. A grader is a rule in code, a second model acting as a judge, or a human.
> Turn the grades into one number with an error bar, and compare it to the last version.
> When you use it: before launch (does it work at all?), before every change (did we break something?), and after launch (is it still working on real traffic?).
> Important: the grader is part of the system you must test. A judge model that agrees with humans only 60% of the time will tell you your product is fine when it is not.
>  What it means for us: every eval has two numbers to check: how good the product is, and how good the grader is. Ask for both.
>  Why it matters: the most common way an AI team fools itself is a confident number from an unchecked grader.
> The rest of this article zooms in, one level at a time. Each level answers one question about the level above it.
> Level 0 · The whole loop, once, on one ticket
> Level 1 · What exactly do we measure? · (inputs, gold answers, the number)
> Level 2 · What goes wrong? · (look at the data first)
> Level 3 · Graders made of code · (cheap, exact, blind to meaning)
> Level 4 · A model as grader · (flexible, biased, must be checked)
> Level 5 · Honest numbers · (error bars, A/B, how many cases)
> Level 6 · Grading systems with parts · (retrieval, agents, cost, reliability)
> Level 7 · Public benchmarks · (what leaderboards do and do not tell you)
> Level 8 · Making it a habit · (gates, monitoring, when to re-check)
> Then · The tools and approaches, a decision guide, and the references
> Level 0: the whole loop, once, on one ticket
> Zooms into: everything. Question: what does an eval look like when it runs?
> Our running example for the whole article is a small customer-support assistant for a fictional online bike and camping shop. It has three parts, each of which we will grade differently later:
> triage: reads a ticket and sorts it into one of 12 categories (returns, shipping, warranty, …) with a priority.
> answer: finds the relevant pages of the shop's policy handbook and writes a reply that cites them.
> agent: looks up orders, issues refunds, and escalates, by calling tools against a mock database under policy rules.
> Here is one ticket going through the loop.
> Input: "I'm running late for work and need this sorted immediately. I returned my bike last week, but I still haven't seen the refund. Your policy clearly states refunds are processed within 5 business days…"
> System output (triage): returns. Gold answer: returns. Score: 1 out of 1.
> System output (answer): a polite four-paragraph reply that cites the returns section and mentions both required facts: refunds take 5 business days, and a 15% restocking fee applies to used items.
> Now three graders look at that reply:
> Code rule. Question it asks: Does the reply cite a handbook section? Verdict: yes.
> Code rule. Question it asks: Does it mention both required facts? Verdict: yes, none missing.
> Model judge. Question it asks: Does it claim anything the handbook does not say? Verdict: fail: it invented "a total allowance of up to 15 business days".
> That is the whole idea. Two cheap code checks said the reply was fine. The judge found an invented number that would have gone to a customer. Every later level is about making that loop trustworthy at scale.
> Carry forward from Level 0:
> An eval is input, system, grader, number. Nothing more.
> Different graders answer different questions. "Cites a section" and "invents nothing" are not the same check.
> A fluent reply can pass every surface check and still be wrong.
> Level 1: what exactly do we measure?
> Zooms into: steps 1 and 4 of the loop. Question: where do the inputs and the "right answers" come from, and what is the number?
> Inputs. The cases should look like real traffic, including the awkward ones. Our 80 tickets were generated from a grid of customer persona × topic × scenario, so angry customers, vague questions, and multi-issue tickets all appear. Anthropic's guide for agent evals suggests starting with 20 to 50 tasks taken from real failures, not from imagined happy paths (Grace et al., 2026).
> Gold answers. For each input we write down what "right" means: the correct category, the handbook sections a reply must draw on, and the two or three facts it must state. Because our tickets were generated from the handbook, the gold answers are correct by construction. In a real product they come from domain experts.
> Two piles. We split the cases into a dev set (20 tickets) used for tuning prompts and graders, and a test set (60 tickets) used only for reporting. If you tune on the cases you report on, the number flatters you.
> The number. For triage it is accuracy (share of tickets sorted correctly). For replies it is pass rate (share of replies with no failure). For the agent it is the share of tasks that end in the right database state. One number per experiment, always reported on the test set, always with an error bar (Level 5).
> Four words that get confused:
> Eval. Measures: your system on your data. Example: our assistant on 60 tickets.
> Benchmark. Measures: a model on a public task. Example: GSM8K math, SWE-bench coding.
> Test (software). Measures: a function returns the expected value. Example: JSON parses, no crash.
> Monitoring. Measures: live traffic after launch. Example: sampled real tickets graded daily.
> A model that scores high on a public benchmark can still answer your customers wrongly. The benchmark measures the engine, the eval measures the car on your road (Husain & Shankar, 2025).
> Carry forward from Level 1:
> Inputs with gold answers are the most valuable asset in the whole process. They are expensive and they are the thing that makes everything else possible.
> Keep a dev pile for tuning and a test pile for reporting.
> Benchmarks are about models. Evals are about your product.
> Level 2: what goes wrong? Look at the data first
> Zooms into: the grading step. Question: what should the graders even look for?
> Before building any automatic grader, read the outputs. Every experienced practitioner says the same thing (Husain, 2024; Husain, 2025; Shankar et al., 2024). Read a hundred or two hundred outputs one by one, write a short note on each failure, then group the notes into a short list of failure types with counts. This is called error analysis, and the two steps have names: open coding (free notes) and axial coding (grouping).
> What it produced on our 60 test replies:
> replies that pass: 34 of 60
> missing_required_fact · 15
> unsupported_claim · 12
> wrong_section_retrieved · 8
> did_not_answer · 5
> wrong_value · 2
> over_promise · 1
> Barely half the replies pass. The two biggest problems are a missing fact and an invented claim. Nobody would have guessed that from the demo. This list is the specification for every grader we build next: one grader per failure type, in order of frequency.
> Important: the failure list comes from reading outputs, not from imagining them.
>  What it means for us: the first week of any eval effort is people reading transcripts in a purpose-built viewer, not engineers wiring up a framework.
>  Why it matters: a grader built for failures that do not occur gives a reassuring number and misses the ones that do. Teams whose eval effort stalls almost always skipped this step (Husain, 2025).
> A related finding: your criteria will change as you grade. Shankar et al. (2024) call it criteria drift. Grading examples sharpens the rubric, and a sharper rubric changes earlier grades. Expect two or three rounds. It is not a process failure.
> Carry forward from Level 2:
> The failure taxonomy is the plan. Build graders for the top failure types first.
> Reading outputs is the highest-value activity and the most often skipped.
> Expect the rubric to change while you grade.
> Level 3: graders made of code
> Zooms into: one kind of grader. Question: what can a plain rule measure, and what can it not?
> A code grader is a rule written in ordinary code. It is free, instant, and gives the same answer every time. Use it for everything it can measure.
> Exact answers. Triage has a single right label, so we count matches.
> accuracy: 0.700 · macro F1: 0.697
> Seven tickets in ten are sorted correctly. Macro F1 averages the score over all 12 categories equally, so rare categories count as much as common ones. The two numbers being close tells us the mistakes are spread out, not concentrated in one category.
> Rule checks on free text. For replies there is no single right text, but there are rules a reply must obey:
> nonempty · 100% pass
> max_words_150 · 17% pass
> no_banned_promises · 92% pass
> Only 17% of replies fit in 150 words. The app is far too chatty, and no judge was needed to find that. Public benchmarks like IFEval (Zhou et al., 2023) are built entirely from such verifiable rules ("answer in exactly three bullet points").
> Required facts. We check whether each gold fact appears in the reply. This catches the top failure type, missing facts, at zero cost.
> Similarity scores. Overlap measures (ROUGE, BLEU) and embedding similarity compare the reply to a reference text. On our replies, embedding similarity separates good from bad replies with an AUC of 0.709 (0.5 is a coin flip, 1.0 is perfect). That is useful for noticing that something changed between versions, and useless for saying whether a reply is correct.
> Important: similarity notices change, it does not grade quality.
>  What it means for us: use it as a cheap drift alarm, never as the headline number.
>  Why it matters: a wrong reply that uses the same words as a right one scores high. Eugene Yan's survey (2024) and the original ROUGE/BLEU literature document this limit at length.
> The limit of code graders, in one number. Only 11.7% of our replies pass all code checks, but code checks caught none of the invented claims. The reply from Level 0 passed every rule while inventing a 15-day allowance. Rules see form; they do not see meaning.
> Carry forward from Level 3:
> Use code graders for everything with a definite answer: labels, formats, required facts, forbidden phrases.
> Similarity measures drift, not quality.
> Rules cannot see an invented claim. That needs a reader.
> Level 4: a model as grader, and how to check it
> Zooms into: the other kind of grader. Question: when the grader is itself a model, how do we know it is right?
> A model judge (usually called LLM-as-judge) is a second model that reads an output and grades it. It can read for meaning, so it can catch the invented 15-day allowance. It is also a language model, so it has all the failure modes of one. This level is the longest because this is where most eval programs go wrong.
> 4.1 How to ask a judge
> The practitioner consensus and the research literature agree on a shape:
> One question per failure type, yes or no. "Does the reply contain a claim not supported by the handbook excerpts?" rather than "rate quality 1 to 5". Binary questions are faster for humans to label, more reproducible, and easier to check (Husain & Shankar, 2025). The output passes only if every question says no.
> Ask for the evidence. The judge quotes the offending sentence. That makes its verdict checkable by a person in seconds.
> Give it the context. A judge that cannot see the handbook cannot know what is unsupported.
> Cho et al. (2026) tested this directly on summaries ("Ask, Don't Judge"). Decomposing the grade into yes/no questions about specific errors beat the popular holistic G-Eval approach on every dataset (Spearman correlation with humans 0.563 vs 0.514 on SummEval). Their most telling example: a summary with three planted factual errors received a perfect 5.0 from holistic judges and 1.57 from the question-based one. They also found that stuffing the prompt with more instructions eventually made the judge worse, not better.
> 4.2 Checking the judge: our own numbers
> We labelled all 60 test replies by hand (the "reference"), then ran the judge:
> reference says pass: 34 · judge says pass: 42
> they agree on 36 of 60 replies (60%)
> bad replies the judge caught: 10 of 26
> kappa: 0.15
> Sixty percent agreement sounds acceptable. It is not. If the judge had simply said "pass" to everything it would have agreed with the reference 57% of the time, because most replies pass. Cohen's kappa corrects for that: it measures agreement beyond what chance would give. Zero is chance, one is perfect, 0.6 is the usual bar for a judge you let gate a release, and 0.8 is the bar for one you let run unsupervised. Our judge scores 0.15. It is lenient (passes 42 when only 34 deserve it) and catches fewer than half the bad replies.
> Important: raw agreement is misleading when most outputs pass. Report kappa, or report separately how many bad outputs the judge catches and how many good outputs it wrongly fails.
>  What it means for us: a judge is a classifier. Before trusting it, measure it against human labels on at least a few dozen cases, and report the result next to every product number it produces.
>  Why it matters: with this judge, a version that doubled the invented claims might show no change in the headline pass rate.
> The remedy is iteration on the dev set: add examples of the failure type to the judge prompt, narrow the question, give it the gold facts as reference. The tutorial's judge for the "missing fact" question reached a usable level this way; the "unsupported claim" question did not, and was handed to a specialised detector (4.5).
> 4.3 The known biases of judges
> Judges fail in predictable ways. Each has a published measurement and a cheap mitigation.
> Position. What happens: In a pairwise comparison the judge prefers whichever answer is shown first. Evidence: verdicts flip in a large share of pairs when order is swapped (Wang et al., 2024); a 2025 RAG-vs-GraphRAG comparison found earlier GraphRAG "wins" partly vanished once the order was swapped (Han et al., 2025). Mitigation: grade both orders, count a win only if both agree.
> Length. What happens: Longer answers win regardless of content. Evidence: correcting for length raised agreement with human rankings from 0.94 to 0.98 (Dubois et al., 2024). Mitigation: length-controlled scoring, or binary questions that do not reward length.
> Self-preference. What happens: The judge favours answers in its own model family's style. Evidence: judges rate their own generations higher, more so when they recognise them (Panickssery et al., 2024); same-family judges inflated their own provider's agents by about 0.75 on a 7-point scale in the GAUGE audit. Mitigation: use a judge from a different family than the system under test.
> Satisfaction vs success. What happens: The judge rates how the conversation felt, not whether the task got done. Evidence: GAUGE audit, see below. Mitigation: give the judge the tool calls and the final state, not just the chat.
> Judge identity. What happens: Swapping the judge model changes which system wins. Evidence: 2026 audits (arXiv 2607.08535; 2606.19544). Mitigation: record judge model and version as part of every result.
> The GAUGE audit (Bodhwani et al., 2026) deserves its own paragraph because it describes the exact setup most companies use for release decisions: a simulated user talks to the agent, a judge model scores the transcript, the higher score ships. Across 25 agents and about 3,700 transcripts they found that this gate ranks agents well when one is clearly better (correlation 0.94 with a verifiable ground truth), but on near-equal pairs, the ones a real release actually decides between, it promoted the worse agent 31% of the time. A judge that only saw the user-visible chat and rated satisfaction was no better than a coin flip at telling working agents from broken ones (AUC 0.49). A judge that saw the tool calls, authentication, and task resolution halved the failure risk (AUC 0.73). Their conclusion: reliability comes from what evidence the judge is given, not from how strong the judge model is.
> Important: customer satisfaction and task success are different things, and a judge that sees only the conversation measures the first.
>  What it means for us: give judges the evidence (tool calls, database state, retrieved documents), and never promote a version on a judge score alone when two versions are close.
>  Why it matters: an agent that charms and fails will keep getting promoted.
> 4.4 Panels of judges, and how to combine them
> One judge is a single point of failure. Verga et al. (2024) showed that a panel of several smaller, cheaper judges agrees with humans better than one large judge, at a fraction of the cost. But averaging panel scores has a trap: Acharya et al. (2026) proved that one broken judge (a parser failure returning zeros, a sycophantic judge rating everything 10) drags the average arbitrarily far off, no matter how many good judges you add. Real judges fail like this at measurable rates (3.4% parser failures on one dataset, up to 33% on the smallest judge for non-English prompts). Their fix is to replace the average with the geometric median, which ignores the outlier. In the worst case it was 540 times more accurate; on clean data it costs about 1% accuracy. They also show that three judges capture most of the benefit, because judges' errors are correlated.
> A second, related effect: Parikh (2026) found that asking a model for its answer in JSON (the format every judge pipeline uses) makes its answers measurably more uniform than in plain chat. The modal answer's share rose from 41% to 64%. For judging tasks with one correct answer this is harmless; for open-ended rating it means the judge is less discriminating than its chat behaviour suggests.
> 4.5 Cheaper and more reliable than a judge: specialised detectors and typed judges
> For the failure types that matter most, a general judge is often the wrong tool.
> Hallucination detectors are small models (around 100 million to 500 million parameters) trained for one question: is this sentence supported by this context? Vectara's HHEM, LettuceDetect (Kovács & Recski, 2025), MiniCheck (Tang et al., 2024), and plain NLI cross-encoders run on a laptop CPU in about a second, cost nothing per call, and on the RAGTruth benchmark approach the accuracy of a large judge. SelfCheckGPT (Manakul et al., 2023) needs no detector at all: it samples the system several times and flags claims that change between samples. Fiddler's 2026 vendor note names the alternative an "evaluation trust tax": teams that run a large judge on every production trace typically sample only about 10% of traffic, and it claims small detectors can cover 100% at up to 98% lower cost. The claim is a vendor's, with no experiment shown, but the shape of the trade-off is real.
> Typed judges. TypeSafe's Jev model is a different design: it does not generate text at all. You send it the output and a typed question ("Is this claim supported by the excerpt?" with answer "yes/no", or "pick one of these labels"), and it returns a calibrated probability. Because nothing is generated, calls are fast and about a hundred times cheaper than a generative judge, and the probability lets code route uncertain cases to a human. It cannot explain its verdict or invent options; you supply the labels. A 2026 study with blinded human adjudication put it at 92.2% on RewardBench pairs against 93.5% for a frontier generative judge, at about a third of a percent of the fee, but far behind on hard derivation-checking (78.6% vs 93.1%); a cascade that accepts its verdict only above a confidence threshold and otherwise escalates kept 92.5% at about half the cost (arXiv 2609.26550). Our own red-team found that it is not a fact-checker: a fabricated log in the input can flip a verdict, though every successful attack also collapsed its confidence, so a confidence gate is a working defence. Our knowledge base has a tutorial on it and on how to test its accuracy before trusting it.
> Judges need a benchmark too. JudgeBench (Tan et al., 2025) turned hard, objectively checkable problems into judge tests and found that frontier judges are barely better than chance on genuinely hard cases. Reliability must be measured per task, per rubric, per judge model, every time. Vendor claims of "85% agreement with humans" come from one dataset and do not transfer (see the disagreement notes in our practitioner sources).
> Carry forward from Level 4:
> Ask judges yes/no questions about specific failures, with evidence, with the context.
> Measure the judge against human labels, report kappa or catch rate, iterate until it clears the bar.
> Know the five biases and apply the cheap mitigations.
> For "is this supported", prefer a small detector or a typed judge over a general judge.
> Three judges with a robust combination beat one; the average is fragile.
> Level 5: honest numbers
> Zooms into: step 4 of the loop. Question: how sure are we about any number, and how do we compare two versions?
> Every rate we have quoted so far hides a question: would it be the same on a different 60 tickets? Three tools answer it.
> The error bar. We resample our 60 results thousands of times (a bootstrap) and look at the spread:
> triage accuracy: 0.700 · 95% CI [0.583, 0.817]
> The honest statement is not "accuracy is 70%" but "somewhere between 58% and 82%, most likely 70%". Miller (2024) showed that most reported differences between models in published evals are smaller than this kind of interval, and gave the formulas every eval report should use, including the correction needed when several questions share a source (clustered standard errors).
> The paired comparison. We wrote a second version of the reply prompt that retrieves more sections. Judged on the same 60 tickets:
> judge pass rate · v1: 0.700 · v2: 0.700
> difference: +0.000 · 95% CI [-0.117, +0.117]
> verdict: no real difference, keep v1
> Note the interval is narrower than the one for the single accuracy, because the comparison is paired: each ticket is scored under both versions, so ticket difficulty cancels out. A McNemar test asks the per-case question: does v2 win where v1 loses, or do they just trade cases? Here they traded. And v2 regressed on 14% of cases while improving on others. The headline "same pass rate" hides a product that got better for some customers and worse for others.
> Important: a difference whose interval includes zero is noise, not a win.
>  What it means for us: every "the new version is better" claim must come with the interval and the count of cases that got worse.
>  Why it matters: teams ship regressions on the strength of a 2-point improvement that was never there.
> The detection floor. With 60 cases, the smallest difference we can reliably detect is about 12 percentage points. A 5-point regression is invisible at this size. This is a power calculation, and it tells you how many cases you need before you can answer the question you are asking. Below the floor you need more data, not a cleverer test.
> Multiple comparisons. If you test 20 prompt variants and pick the best, one of them will look 10 points better by luck. Either correct for the number of comparisons or confirm the winner on fresh cases.
> Carry forward from Level 5:
> Every rate gets an interval. Every comparison is paired.
> Know your detection floor before you start comparing versions.
> "No measurable difference" is a real result, and often the right one.
> Level 6: grading systems with parts
> Zooms into: step 2, the system. Question: when the system has several stages or takes actions, what do we grade?
> 6.1 Retrieval systems (RAG)
> Our answer component first finds handbook sections, then writes. A bad reply can come from either stage, and the fixes are different. So we grade them separately.
> Grading the finder. Against the gold sections: hit@k (is at least one correct section in the top k?) and recall@k (what share of the correct sections made it?).
> hit@2: 0.93 · recall@2: 0.88
> of 18 failing replies, 1 failed in the finder and 17 in the writer
> The finder is nearly fine. The writer is the problem. That one line redirects a week of engineering.
> Grading the writer. Faithfulness (every claim supported by the retrieved text), answer relevance (does it address the question), and context precision (was what we retrieved actually useful). This is the RAGAS triad (Es et al., 2024), which needs no gold answers and is why RAGAS became the default library. ARES (Saad-Falcon et al., 2024) adds statistical rigour by calibrating small per-criterion judges against about 150 human labels and reporting confidence intervals; in its paper it beat RAGAS by 59 points on context relevance with 78% fewer annotations, though it degrades under large domain shift. In our run RAGAS gave context relevance 0.855 and faithfulness 0.737: the same "retrieval good, writing worse" story our hand-rolled graders told, which is the kind of cross-check that makes a number believable.
> A caution from the agent-coding world: SWE-Explore (Zhang et al., 2026) measured retrieval inside coding agents and found they locate the right file about 65% of the time but the right lines only 15 to 19%, and that missing context, not extra context, is what breaks the next stage. Grade the finder at the granularity the writer needs.
> 6.2 Agents
> An agent takes a sequence of actions (look up an order, issue a refund, escalate). Three things change when grading it.
> Grade the final state, and the path. Did the database end up right (refund issued, order cancelled)? Did the agent take only allowed actions, and not, say, refund twice? τ-bench (Yao et al., 2024) set the pattern: simulated users, policy rules, and a check of the final state. AgentLens (2026) showed why the path matters: agents reach correct final states by lucky or degenerate routes often enough that outcome-only scoring overstates capability.
> Run each task several times. Agents are stochastic. Two different numbers describe the result: pass@k (it succeeded at least once in k tries, which measures capability) and pass^k (it succeeded all k times, which measures reliability). For a customer-facing agent you want pass^k. Our agent scores pass^3 = 0.75: three quarters of the tasks succeed three times out of three. τ²-bench (2025) found that pass^1 drops about 20 points when the agent must coordinate with an active user rather than act alone.
> Measure reliability as its own thing. Rabanser et al. (2026) borrowed from aviation and nuclear engineering to define 12 reliability metrics in four groups: consistency across runs, robustness to perturbation, predictability (does the agent know when it will fail), and bounded harm. Across 15 frontier models they found that two years of capability gains delivered about one sixth as much reliability gain. Agents choose the same kinds of actions each run but in different orders, handle real infrastructure failures gracefully, and break on a rephrased instruction.
> Important: a capable agent is not a reliable one, and your customers experience reliability.
>  What it means for us: report pass^k, run perturbed versions of each task (rename a field, rephrase the instruction), and track consistency across runs as a separate number.
>  Why it matters: the published failures (an agent deleting a production database, an agent making unauthorised purchases) all came from systems with good average success rates.
> Measure cost. Bai et al. (2026) measured token spend across eight frontier models on SWE-bench Verified. Agentic tasks use about a thousand times more tokens than a chat turn, almost all of it re-reading their own growing history. The same task on the same model varied 30-fold in cost between runs, accuracy peaked at intermediate cost and fell at the highest, and models predicted their own cost with a correlation of at most 0.39. Their advice: rank models on cost per correct outcome, not on accuracy alone, and never trust a model's own estimate.
> Judgment, asking, and learning: three newer axes. Three 2026 benchmarks measure things a single success rate cannot see.
> Taste (Pan et al., 2026): freeze an agent at a fork where both paths look fine and ask which one pays off later. The best model picks right 59.7% of the time on a two-way choice, and thinking longer does not help.
> Asking (Gulati et al., 2026): the value of asking a clarifying question about the goal falls from 0.78 to 0.39 once 10% of the task has been done. No frontier model asks within that window; one asked 52% of the time, one 23%, one never.
> Learning from experience (Asawa et al., 2026): across six stateful environments, the best system captured only 25% of its possible improvement from experience, and simply keeping the full conversation history beat every dedicated memory product.
> 6.3 When the system is being optimised against the grader
> If a grader is used to train or select the system (reinforcement learning, best-of-n selection), the system will find the grader's blind spots. Wang et al. of the Qwen team (2026) call this the verification horizon: every grader is a proxy for intent, and under optimisation pressure proxies and intent diverge. They catalogue reward hacking in coding agents (reading the answer from repository history, editing the tests, patching for the evaluator) and show that a behaviour monitor cut hacked "solutions" from 28.6% to 0.6% while raising genuine ones from 40% to 61%. They argue no grader is scalable, faithful, and robust at once: tests are scalable and robust but miss intent; judges are scalable and faithful but gameable; experts are faithful and robust but do not scale. The Meta-Agent Challenge (Lu et al., 2026) saw the same spontaneously: agents asked to build other agents tried to exfiltrate answers from the grading system in five trials.
> Important: any grader that influences training or selection will be gamed.
>  What it means for us: keep a held-out grader the system never sees, monitor for shortcut behaviour, and upgrade the grader as the system improves.
>  Why it matters: the score goes up while the product gets worse.
> Carry forward from Level 6:
> Grade each stage separately; the finder and the writer fail differently.
> For agents: final state and path, several runs, pass^k, cost per success, and reliability as its own number.
> Graders used for optimisation get gamed. Keep one they never see.
> Level 7: public benchmarks
> Zooms into: Level 1's distinction between eval and benchmark. Question: what do leaderboard numbers tell you, and what do they hide?
> A benchmark is a fixed public task set used to compare models: MMLU (academic multiple choice), GSM8K (grade-school maths), HumanEval (code), MT-Bench and Chatbot Arena (conversation quality), SWE-bench (fixing real GitHub issues), τ-bench (customer-service agents), GPQA and HLE (expert questions). They are how you pick an engine. Four things to know before quoting one.
> The number depends on the harness as much as the model. We ran GSM8K on the same open-weight model with two prompt formats and got 0.686 and 0.746. The lm-evaluation-harness paper (Biderman et al., 2024) documents swings of double digits from prompt formatting, few-shot examples, and the regex that extracts the answer. A score is a (model, prompt, harness, version) tuple. Schaeffer et al. (2023) showed something stronger: apparent "emergent" jumps in capability were largely artefacts of all-or-nothing metrics, and vanished under smooth ones. The metric you choose can create or erase a phenomenon.
> Contamination. If the test questions were in the training data, the score measures memory. GSM1k (Zhang et al., 2024) rebuilt GSM8K with fresh questions of matched difficulty and found some model families dropped up to 8 points, with the drop correlated with how likely the model was to have memorised the original. Other families did not drop. Contamination is real, measurable, and uneven.
> Saturation. Benchmarks have a shelf life. A 2026 study of 60 widely used benchmarks found about half highly saturated, and older ones saturate faster. SWE-bench Verified went from roughly 40% to over 80% solved in about two years, and its curator stated it no longer separates frontier models. MMLU, GSM8K, and HumanEval have effectively been retired by frontier labs in favour of HLE, GPQA Diamond, SWE-bench Verified, LiveCodeBench, and τ²-bench, each of which will saturate in turn. On Chatbot Arena the top models now sit within about 20 Elo points, which is inside the noise.
> Redundancy. Zeng and Papailiopoulos (2026) assembled a matrix of 84 models by 133 benchmarks and found it is approximately rank two: two underlying factors explain over 90% of the variation. Five well-chosen benchmarks predict the other 128 to within about 4 points. For choosing an engine, that is good news: you do not need to run forty benchmarks. For discovering a specific failure mode, it says nothing; that still needs your own eval.
> Important: a leaderboard ranks engines on last year's exam, under one harness, and the top entries are usually within noise of each other.
>  What it means for us: use benchmarks to shortlist two or three models, then decide with your own eval on your own data.
>  Why it matters: switching models on a 2-point benchmark gain can cost you 10 points on your actual task.
> Two frontier uses of evals worth knowing. Google's Paper Assistant Tool (Jayaram et al., 2026) uses an agent pipeline to review scientific papers and caught 89.7% of known proof errors versus 55.2% for a single model call; over 90% of 850 surveyed authors found it helpful and 31% ran new experiments because of it. CUSP (Wu et al., 2026) asked models to forecast which research directions will succeed and found them near chance (0.519) with strong yes-bias or no-bias depending on the model, fixable only with explicit bias correction. Both are reminders that an eval of a model's judgment needs its own ground truth, and that models are badly calibrated about the future and about themselves.
> Carry forward from Level 7:
> A benchmark score is a tuple, not a property of the model. Record the harness.
> Benchmarks get contaminated and saturate; check the date.
> Five benchmarks tell you almost everything a leaderboard can. Your eval tells you the rest.
> Level 8: making it a habit
> Zooms into: the "when" of the quick grasp. Question: how does this run every week without a research team?
> Hamel Husain's three-level model (2024) sets the cadence:
> 1. What: code graders, schema checks, required facts. When: every commit. Cost: free.
> 2. What: model judges and detectors on the test set, human review of a sample. When: every change to prompt, model, or retrieval. Cost: cents to dollars.
> 3. What: A/B test on real traffic. When: after a change ships. Cost: real users.
> The merge gate. Our tutorial's CI gate reruns Levels 1 and 2 and fails the build if the pass rate drops more than 3 points against the recorded baseline of 0.70. It is a tripwire for big regressions, not a guarantee: with a 12-point detection floor, a 5-point regression walks through. Say so in the dashboard.
> Monitoring. After launch, sample real traffic, run the cheap graders on all of it and the expensive ones on a slice, and plot the trend. Bodhwani et al.'s (2026) "calibrate then trust" is the right pattern for the expensive gate: run a full audit once against verifiable ground truth to learn where the cheap judge-based gate agrees with reality, use the cheap gate in CI only inside that region, and re-audit when the model, the judge, the simulator, or the domain changes. They also found that a zero-cost "did the conversation complete" bit caught budget-starvation regressions on its own.
> Caching and cost. Cache every model call keyed on the prompt, the data version, and the recipe. A rerun becomes a file read. Our full A/B on 60 tickets costs 121 judge calls, about four cents; the entire tutorial reran from cache with zero calls. Cost is not the reason to skip evals.
> What a leader should ask for. Four numbers on one page: the product's pass rate with its interval, the grader's agreement with human labels, the detection floor, and the share of cases that got worse in the last change. If any of the four is missing, the other three are not yet meaningful.
> Carry forward from Level 8:
> Three cadences: every commit, every change, after shipping.
> A gate is a floor, not a ceiling. State its detection floor.
> Calibrate the cheap gate against ground truth once, then trust it only inside that region.
> The tools and approaches, observed
> This section is an observation, not a recommendation list. All of these were run or reviewed while building the tutorial; the practitioner and tooling notes in our knowledge base hold the details.
> Frameworks
> Inspect AI (UK AI Security Institute, MIT). Best at: One coherent pipeline: dataset, solver, scorer, log viewer; agents and sandboxes; used for frontier safety evals. What to watch: Code-first; the most complete, and the most to learn.
> lm-evaluation-harness (EleutherAI, MIT). Best at: Running public benchmarks (GSM8K, MMLU, IFEval) reproducibly against any model. What to watch: Benchmarks only; the harness paper is the reason it exists.
> promptfoo (MIT, Node.js). Best at: Declarative YAML test suites, red-teaming, CI regression. What to watch: Not a Python package; acquired by OpenAI in 2026.
> DeepEval (Apache-2.0). Best at: pytest-style unit tests with ready metrics (faithfulness, relevance). What to watch: Headline metrics are blends; look inside before trusting.
> RAGAS (Apache-2.0). Best at: The standard RAG triad, reference-free. What to watch: Flaky with local models (NaNs, executor errors); numbers are blends.
> Langfuse (MIT self-host). Best at: Tracing, datasets, experiment runs, judge evaluators in one self-hosted stack. What to watch: Version 4 changes evaluator semantics; plan the migration.
> Phoenix (Arize). Best at: Tracing plus evals with a strong UI. What to watch: Elastic License 2.0, source-available rather than open source.
> LangSmith, Braintrust. Best at: Hosted platforms: trace capture, sampling, judge bootstrap, human refinement. What to watch: Commercial; Braintrust's autoevals library works standalone.
> Opik (Comet), MLflow genai, Weave (W&B). Best at: Self-hostable observability with eval hooks; good if you already run the platform. What to watch: Heavy footprints for a from-scratch team.
> HELM (Stanford). Best at: Multi-metric philosophy: accuracy, calibration, robustness, fairness, efficiency together. What to watch: Research-oriented, least turnkey.
> evalica. Best at: Turning pairwise judgments into Bradley-Terry or Elo leaderboards with intervals. What to watch: Statistics only; pair with a judge.
> Jev / TypeSafe. Best at: Typed judge questions with calibrated probabilities, ~100x cheaper than a generative judge. What to watch: No text, no explanations; you supply the labels.
> HHEM, LettuceDetect, MiniCheck, SelfCheckGPT. Best at: "Is this claim supported" at CPU speed and zero marginal cost. What to watch: One question only; not a general grader.
> Selene-Mini, Prometheus 2, Flow-Judge. Best at: Open-weight judge models you can self-host and audit. What to watch: Still judges; still need calibration.
> Approaches, compared
> Code rules. Answers: is the form right, are the facts present. Cost: free. Blind spot: meaning.
> Similarity (ROUGE, embeddings). Answers: did the output change. Cost: free. Blind spot: correctness.
> Specialised detector / NLI. Answers: is this claim supported by this text. Cost: near free. Blind spot: anything else.
> Typed judge (Jev). Answers: this label, this yes/no, with a probability. Cost: cents per thousand. Blind spot: cannot explain or propose.
> Generative judge, binary with evidence. Answers: any readable criterion. Cost: cents per call. Blind spot: the five biases; must be calibrated.
> Panel of judges, robust combination. Answers: same, with fewer single-judge failures. Cost: three times a judge. Blind spot: correlated errors cap the benefit at ~3 judges.
> Human labels. Answers: ground truth. Cost: expensive, slow. Blind spot: needs two raters and an agreement statistic.
> A/B on traffic. Answers: real business impact. Cost: real users at risk. Blind spot: slow; needs the earlier levels to be safe.
> A pattern seen in every source and in our own run: the hand-rolled grader and the framework number should be read against each other. Agreement is evidence. Disagreement is a question, and usually a good one.
> A decision guide
> Is the output well-formed and complete?. Use: code rules. Then check: nothing, it is exact.
> Did the new version change the outputs?. Use: similarity. Then check: why, by reading a sample.
> Is this claim supported by this document?. Use: detector or typed judge. Then check: its precision and recall on a labelled sample.
> Does the reply fail in way X?. Use: binary generative judge with evidence. Then check: kappa against human labels on dev.
> Which of two versions is better?. Use: paired comparison with interval. Then check: the per-case regressions.
> Can we detect a 5-point regression?. Use: power calculation. Then check: add cases until you can.
> Is the agent reliable?. Use: pass^k over several runs, perturbed tasks. Then check: consistency across runs as its own number.
> Which model should we use?. Use: five public benchmarks to shortlist. Then check: your own eval to decide.
> Is it still working in production?. Use: sampled traffic, cheap graders on all, judge on a slice. Then check: re-audit the judge gate when anything changes.
> Fifteen things to carry away
> An eval is input, system, grader, number. Build the gold inputs first; they are the asset.
> Evals measure your product. Benchmarks measure engines. Do not confuse them.
> Read a hundred outputs before writing a grader. The failure list is the plan.
> Code graders for everything with a definite answer. They see form, not meaning.
> Judges get binary questions with evidence and context. Holistic scores miss planted errors.
> Measure the judge against humans. Report kappa or catch rate. Sixty percent agreement can mean nothing.
> Judges prefer first, longer, familiar, and pleasant. Mitigations are cheap; apply them.
> Satisfaction is not success. Give the judge the tool calls and the final state.
> For "is this supported", a small detector or typed judge beats a general judge on cost and often on accuracy.
> Every rate gets an interval. Every comparison is paired. Know the detection floor.
> Grade each stage of a pipeline separately.
> Agents: final state and path, several runs, pass^k, cost per success, reliability on its own axis.
> A grader used for optimisation gets gamed. Keep one the system never sees.
> Benchmark scores are harness-dependent, contaminated unevenly, and saturate. Record the tuple.
> Three cadences, a gate with a stated floor, a monitor, and a re-audit when anything changes.
> References
> From this knowledge base (summaries in the sibling folders)
> Acharya, Pan, Verkhovsky (2026). RoPoLL: Robust Panel of LLM Judges. arXiv:2606.30931. — RoPoLLRobustPanelOfLLMJudges/
> Asawa et al. (2026). Continual Learning Bench. arXiv:2606.05661. — ContinualLearningBench/
> Bai et al. (2026). How Do AI Agents Spend Your Money? arXiv:2604.22750. — HowAiAgentsSpendYourMoney/
> Bodhwani, Tran, Wei (2026). GAUGE: When Not to Trust LLM-as-a-Judge in User-Simulated Evaluation of Task-Oriented Agents. arXiv:2609.12191. — GaugeWhenNotToTrustLlmAsAJudge…/
> Cho et al. (2026). Ask, Don't Judge / BinEval. arXiv:2606.27226. — AskDontJudge/, BinEval/
> Fiddler (2026). The Evaluation Trust Tax: agent evals TCO. — AgentEvalsTCO/
> Grace, Hadfield, Olivares, De Jonghe (Anthropic, 2026). Demystifying Evals for AI Agents. — DemystifyingEvalsForAIAgents/
> Gulati et al. (2026). Ask Early, Ask Late, Ask Right. arXiv:2605.07937. — AskEarlyAskLateAskRight/
> HKUDS (2026). ClawWork (economic-accountability agent benchmark, code analysis). — ClawWork/
> Jayaram et al. (Google, 2026). Towards Automating Scientific Review with the Paper Assistant Tool. arXiv:2606.28277. — PaperAssistantTool/, TowardsAutomatingScientificReview/
> Lu et al. (2026). The Meta-Agent Challenge. arXiv:2606.04455. — MetaAgentChallenge/
> Menaged et al. (2026). Can LLM Agents Infer World Models? arXiv:2606.16576. — CanLLMAgentsInferWorldModels/
> Pan et al. (2026). The Tasteful Agent. arXiv:2609.25804. — TastefulAgent/
> Parikh (2026). Structured Output Collapses Answer Diversity Across 44 Language Models. arXiv:2607.18476. — StructuredOutputCollapsesAnswerDiversity/
> Rabanser, Kapoor, Kirgis, Liu, Utpala, Narayanan (2026). Towards a Science of AI Agent Reliability. arXiv:2602.16666, ICML 2026. — TowardsAScienceOfAIAgentReliability/
> Wang et al. (Qwen, 2026). The Verification Horizon: No Silver Bullet for Coding Agent Rewards. arXiv:2606.26300. — VerificationHorizon/
> Wu et al. (2026). CUSP: Forecasting Scientific Progress with AI. arXiv:2605.22681. — ForecastingScientificProgressWithAI/
> Zeng, Papailiopoulos (2026). You Don't Need to Run Every Eval. arXiv:2606.24020. — YouDontNeedToRunEveryEval/
> Zhang et al. (2026). SWE-Explore. arXiv:2606.07297. — SWEExplore/
> The evals tutorial (tutorials/evals/, chapters 00–14, Q&A.md, research/SOURCES_*.md) and its primer notebook, source of every running-example number. The jev tutorial (tutorials/jev/).
> Foundational and practitioner sources
> Biderman et al. (2024). Lessons from the Trenches on Reproducible Evaluation of Language Models. arXiv:2405.14782.
> Chiang et al. (2024). Chatbot Arena. arXiv:2403.04132.
> Dubois, Galambosi, Liang, Hashimoto (2024). Length-Controlled AlpacaEval. arXiv:2404.04475.
> Es, James, Espinosa-Anke, Schockaert (2024). RAGAS. arXiv:2309.15217.
> Gu et al. (2024). A Survey on LLM-as-a-Judge. arXiv:2411.15594.
> Han et al. (2025). RAG vs GraphRAG: A Systematic Evaluation. arXiv:2502.11371.
> JEV-as-a-Judge (2026). arXiv:2609.26550. — research_topics/coding_agents/JevAsAJudge/
> Panickssery, Bowman, Feng (2024). LLM Evaluators Recognize and Favor Their Own Generations. arXiv:2404.13076.
> Husain (2024). Your AI Product Needs Evals. hamel.dev. Husain (2025). A Field Guide to Rapidly Improving AI Products. Husain & Shankar (2025). AI Evals FAQ.
> Jimenez et al. (2024). SWE-bench. arXiv:2310.06770. OpenAI (2024). SWE-bench Verified.
> Kovács, Recski (2025). LettuceDetect. arXiv:2502.17125. Tang, Laban, Durrett (2024). MiniCheck. arXiv:2404.10774. Manakul, Liusie, Gales (2023). SelfCheckGPT. arXiv:2303.08896.
> Liang et al. (2022). HELM. arXiv:2211.09110.
> Liu et al. (2023). G-Eval. arXiv:2303.16634.
> Miller (2024). Adding Error Bars to Evals. arXiv:2411.00640.
> Saad-Falcon, Khattab, Potts, Zaharia (2024). ARES. arXiv:2311.09476.
> Schaeffer, Miranda, Koyejo (2023). Are Emergent Abilities of Large Language Models a Mirage? arXiv:2304.15004.
> Shankar, Zamfirescu-Pereira, Hartmann, Parameswaran, Arawjo (2024). Who Validates the Validators? arXiv:2404.12272.
> Tan et al. (2025). JudgeBench. arXiv:2410.12784.
> Verga et al. (2024). Replacing Judges with Juries (PoLL). arXiv:2404.18796.
> Wang et al. (2024). Large Language Models are not Fair Evaluators. arXiv:2305.17926.
> Yan (2024). Task-Specific LLM Evals that Do & Don't Work; Evaluating the Effectiveness of LLM-Evaluators. eugeneyan.com.
> Yao, Shinn, Razavi, Narasimhan (2024). τ-bench. arXiv:2406.12045. Sierra (2025). τ²-bench. arXiv:2506.07982.
> Zhang et al. (2024). GSM1k. arXiv:2405.00332.
> Zheng et al. (2023). Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena. arXiv:2306.05685.
> Zhou et al. (2023). IFEval. arXiv:2311.07911.
> 2026 audits: When AI Benchmarks Plateau (arXiv:2602.16763); When the Judge Changes, So Does the Measurement (arXiv:2607.08535); Reliability without Validity (arXiv:2606.19544); AgentLens (arXiv:2605.12925).

- 图片：[img1](https://pbs.twimg.com/media/HTugan9WEAAxt2d?format=jpg&name=large)

#### x-2055978135246807138

**Google Nexus：把预测变成推理问题**

- 作者：Rohan Paul (@rohanpaul_ai) · 发帖 2026-05-17 · [原帖](https://x.com/rohanpaul_ai/status/2055978135246807138)
- 来源：🔖 收藏 · 拉取 2026-10-27
- 类型：论文解读
- **总结**：解读 Google 的 Nexus 论文。观点：时间序列预测需要的是「上下文」，不只是历史数据；很多模式由事件驱动，而不是由时间驱动。Nexus 把任务拆给多个 agent：一个把杂乱文本整理成事件时间线，一个判断宏观状态，其他做数值推理，让事件和数字互相解释。在 Zillow 数据上，基于 Claude 的版本 MAPE 比直接 CoT 降低 86.6%。是多 agent 用于分析类任务的例子。
- **原文**：

> New Google paper: A forecast needs context, not just history.
>
> Some patterns are caused by events, not time. Nexus reframes forecasting as a reasoning problem, where events and numbers have to explain each other.
>
> Nexus argues that forecasting improves when models read the world around the numbers, not just the numbers themselves.
>
> In the Zillow tests, one Claude-based version cut average MAPE by 86.6% versus direct chain-of-thought prompting.
>
> That matters because most time series models are fluent in pattern, but mute about cause.
>
> A housing inventory curve can reflect seasonality, mortgage pressure, migration, layoffs, and local supply, while a stock price can be bent by earnings, regulation, hype, and fear.
>
> Nexus separates those jobs instead of asking one prompt to do everything.
>
> One agent turns messy historical text into a clean event timeline, one reads the broad regime, another tracks local shocks, and a synthesizer reconciles them with calibration from past errors.
>
> The interesting result is not merely that context helps, but that structure helps the language model use context without losing the time series.
>
> The evidence is still narrow: Zillow counts, seven equities, post-cutoff data, and single-run evaluations, so this is not a universal law of forecasting.
>
> But the direction is clear: future forecasters will not only extrapolate curves; they will argue about what made the curve move.
>
> ----
>
> Paper Link – arxiv. org/abs/2605.14389
>
> Paper Title: "Nexus : An Agentic Framework for Time Series Forecasting"

- 图片：[img1](https://pbs.twimg.com/media/HIgjZQoaQAAJ9xw?format=jpg&name=large)

#### x-2050956647909015788

**DAIR.AI 每周论文（4/26–5/3）**

- 作者：DAIR.AI (@dair_ai) · 发帖 2026-05-03 · [原帖](https://x.com/dair_ai/status/2050956647909015788)
- 来源：🔖 收藏 · 拉取 2026-10-27
- 类型：论文汇总
- **总结**：本周 10 篇论文：①Agentic Harness Engineering：把 harness 演化拆成组件、经验、决策三层，每次修改都可验证、可回滚，Terminal-Bench 2 的 Pass@1 从 69.7% 升到 77%，超过人工设计的 Codex-CLI；②AgenticQwen-30B-A3B；③Agentic World Modeling；④RecursiveMAS；⑤OneManCompany；⑥从 skill 文本到 skill 结构；⑦Latent Agents；⑧OCR-Memory；⑨推理中何时检索；⑩决策和 skill 共同演化。适合当作 agent 研究前沿的索引。
- **原文**：

> 《Top AI Papers of the Week》
>
> The Top AI Papers of the Week (April 26 - May 3)
> 1. Agentic Harness Engineering
> Most coding-agent harnesses are still tuned by hand or kept alive through brittle trial-and-error self-evolution. This paper introduces Agentic Harness Engineering (AHE), a framework that makes harness evolution observable and falsifiable. AHE separates the system into three layers: components stored as revertible files, experience condensed from millions of trajectory tokens into structured evidence, and decisions written as predictions that get checked against task outcomes. Every edit becomes a contract you can verify or revert.
> Three-layer evolution model: Components, experience, and decisions are each first-class artifacts. Components are versioned files, experience is compressed evidence pulled from full trajectory logs, and decisions are explicit hypotheses with expected outcomes. The structure turns black-box harness tuning into an auditable engineering loop.
> Pass@1 gains on Terminal-Bench 2: Pass@1 climbs from 69.7% to 77.0% across ten iterations, beating both human-designed Codex-CLI (71.9%) and self-evolving baselines like ACE and TF-GRPO. The framework also uses 12% fewer tokens than the seed harness on SWE-bench-verified.
> Cross-model transfer: The evolved harness transfers across model families with +5.1 to +10.1 point gains, suggesting the optimizations are structural rather than overfit to a specific backbone. That is the property you actually want from harness engineering.
> Why it matters: Harness work is the largest hidden cost in most agent systems. AHE is the first credible recipe for letting the harness improve itself without drifting into noise, which makes it the most important agent-systems paper of the week.
> Paper | Tweet
> 2. AgenticQwen-30B-A3B
> Alibaba shows that a 30B MoE model with only 3B active parameters can match Qwen3-235B on real tool-use workloads. AgenticQwen-30B-A3B scores 50.2 average on TAU-2 plus BFCL-V4 Multi-Turn, while AgenticQwen-8B scores 47.4. Both more than double their vanilla Qwen baselines and close most of the gap to a 235B model. The recipe is built around two reinforcement learning flywheels that run in parallel, with simulated users actively trying to mislead the agent.
> Reasoning flywheel from self-failure: The first loop mines the model's own errors and converts them into harder reasoning problems each round. The training distribution gets harder on its own as the model improves, removing the need for new human-curated reasoning data.
> Agentic flywheel for tool use: The second loop grows simple linear tool-use trajectories into multi-branch behavior trees. Simulated users test recovery from misleading instructions, ambiguous goals, and failed tool calls, which is where vanilla supervised tuning typically breaks.
> Real efficiency for production agents: A 30B MoE with 3B active tokens at inference is significantly cheaper to serve than a 235B dense or MoE alternative. For tool-use workloads where frontier reasoning is overkill, this changes the cost profile of shipping production agents.
> A reusable recipe: The flywheel approach generalizes beyond Qwen. Teams can generate hard examples from their own agent's failures rather than relying on static synthetic data, which is the more scalable path for domain-specific agents.
> Paper | Tweet
> 3. Agentic World Modeling
> A massive 40-author survey lands the cleanest taxonomy of world models in agent research released so far. The paper proposes a "levels by laws" framework spanning three capability levels and four law regimes, then synthesizes 400+ works and 100+ representative systems across model-based RL, video generation, web and GUI agents, multi-agent simulation, and scientific discovery. As agents shift from chatbots to goal-accomplishers, the bottleneck moves from language to environment, and this is the first paper that gives builders a shared vocabulary across communities that have been working in isolation.
> Three capability levels: L1 Predictors handle one-step transitions, L2 Simulators do multi-step action-conditioned rollouts, and L3 Evolvers self-revise as the world changes. The hierarchy makes it easy to place existing systems and identify where capability gaps actually live.
> Four law regimes: Physical, digital, social, and scientific laws each impose different constraints on what a world model needs to capture. The framework treats them as orthogonal axes, which clarifies why a strong physics simulator can still fail at social or digital tasks.
> Failure-mode catalog: The survey extracts recurring failure patterns across 100+ systems, including misaligned reward shaping, drift under non-stationarity, and brittle transfer across regimes. Each failure mode is mapped to a level and law combination, so the diagnosis is grounded.
> Evaluation principles per level: The authors propose evaluation criteria specific to each capability level rather than a single benchmark. This is the right move because L1 prediction accuracy and L3 self-revision quality are not measurable on the same axis.
> Paper | Tweet
> 4. RecursiveMAS
> Multi-agent systems usually pass full text messages between agents at every step, which causes token bloat, latency, and context dilution that all grow with team size. RecursiveMAS asks a different question: what if agents collaborated through recursive computation in a shared latent space instead of through text? The system treats a multi-agent team as a recursive computation where each agent acts like an RLM layer, iteratively passing latent representations to the next and forming a looped interaction process. Less talking, more thinking.
> RecursiveLink for latent communication: A RecursiveLink module generates latent thoughts and transfers state directly between heterogeneous agents, replacing natural-language messages with internal representations. The change removes the cost of re-encoding and re-parsing text on every coordination step.
> Inner-outer loop learning: The training algorithm uses an inner loop for per-step latent updates and an outer loop for team-level credit assignment, with shared gradient-based updates across agents. This makes joint optimization tractable instead of relying on hand-tuned communication protocols.
> Strong gains across 9 benchmarks: Across math, science, medicine, search, and code generation, RecursiveMAS delivers 8.3% average accuracy gain over baselines, 1.2x to 2.4x end-to-end inference speedup, and 34.6% to 75.6% reduction in token usage. The efficiency story is at least as important as the accuracy story.
> A path past the agent communication tax: If agent-to-agent communication is the next real bottleneck, latent-space recursion is one of the cleaner ways to scale collaboration. Teams running multi-agent systems at scale should treat this as a serious design alternative, not a research curiosity.
> Paper | Tweet
> 5. OneManCompany
> If you are building multi-agent systems, you are probably wiring static org charts. This paper argues they should look more like a labor market. OneManCompany (OMC) replaces fixed teams with "Talents," portable agent identities that bundle skills and tools, and a "Talent Market" where agents get recruited dynamically per task. An Explore-Execute-Review tree search decomposes work hierarchically and aggregates results back up. On PRDBench, OMC reaches 84.67% success, +15.5 points over prior SOTA, and the framework generalizes across the case studies the authors run.
> Talents as portable identities: A Talent bundles a skill set, tool access, and behavioral priors into a reusable agent identity. Talents can be hired into any task without rewiring the orchestration graph, which removes most of the brittleness in pre-wired multi-agent pipelines.
> Dynamic recruitment via Talent Market: Tasks post requirements, and the market matches Talents to roles based on capability fit and current load. This replaces the standard "design a team for every workflow" pattern with on-demand assembly that adapts as the task population shifts.
> Explore-Execute-Review tree search: Work is decomposed top-down into subtasks, executed in parallel by recruited Talents, then reviewed and aggregated up the tree. The structure naturally supports retries, branching, and cross-checking without manual coordination logic.
> Why it matters: Pre-wired multi-agent pipelines break the moment tasks drift outside their design envelope. Treating agents as a recruitable workforce gets you self-organization and continuous improvement by default, which is what open-ended agent systems need.
> Paper | Tweet
> 6. From Skill Text to Skill Structure
> SKILL.md files entangle invocation interface, execution flow, and tool side effects in a single blob of natural language. That makes downstream discovery and risk review brittle as skill registries scale. This paper proposes SSL, a three-layer typed JSON representation drawn from Schank and Abelson's classical work on scripts, MOPs, and conceptual dependency. An LLM-based normalizer converts existing SKILL.md files into the structure, so adoption does not require rewriting registries by hand.
> Three layers, cleanly separated: A Scheduling layer captures invocation signals and trigger conditions, a Structural layer encodes execution scenes and ordering, and a Logical layer specifies atomic actions plus resource and side-effect annotations. The separation lets discovery, risk, and execution each reason about the layer they care about.
> Skill Discovery MRR jumps 0.573 to 0.707: Treating skills as typed structure rather than prose makes retrieval significantly more accurate, even before any model fine-tuning. The gain comes from the structure exposing what skills actually do, not just how they describe themselves.
> Risk Assessment macro F1 of 0.787: The Logical layer's resource annotations enable a 0.744 to 0.787 jump in risk classification. Auditors can now reason about side effects directly instead of inferring them from free-form prose.
> A 6,184-skill corpus released: The authors ship a normalized corpus of 6,184 skills, 403 task queries, and 500 risk-labeled skills. As skill registries cross a million entries, structured representations are the only path that keeps discovery and review tractable.
> Paper | Tweet
> 7. Latent Agents
> Multi-agent debate makes models reason better. It also burns tokens generating long transcripts before any answer comes out. Latent Agents distills the entire debate into a single LLM through a two-stage fine-tuning pipeline: the model first learns debate structure, then internalizes it through dynamic reward scheduling and length clipping. The internalized model matches or beats explicit multi-agent debate while using up to 93% fewer tokens, which makes debate-quality reasoning practical at production scale.
> Two-stage internalization pipeline: Stage one teaches the structure of debate (turn taking, critique, revision) through supervised fine-tuning on transcript data. Stage two uses dynamic reward scheduling and length clipping to compress that structure into single-pass reasoning without losing the gains from the multi-agent setup.
> Up to 93% token savings: The internalized model matches or beats explicit debate accuracy while drastically reducing inference cost. For teams running reasoning workloads at scale, this is the kind of efficiency win that turns a research idea into a deployment default.
> Activation steering reveals agent subspaces: The "agents" survive distillation as identifiable circuits in activation space. Probing finds interpretable directions corresponding to different agent perspectives, which means the internal structure persists even when the external transcript is gone.
> A safety angle worth noting: When malicious agents are deliberately embedded via distillation, negative steering suppresses them more cleanly than steering a base model would, with smaller hits to general performance. Internalized debate may turn out to be a useful interpretability and alignment substrate, not just a token-saver.
> Paper | Tweet
> 8. OCR-Memory
> Most agent memory systems compress trajectories into text summaries and hope the model remembers what matters, which is exactly where the information loss hides. OCR-Memory renders the agent's interaction history as images with indexed visual anchors, then retrieves via a locate-and-transcribe pipeline: the model scans visual memory, predicts the index of the relevant region, and the original text is fetched verbatim from a database. Older trajectories are stored as low-resolution thumbnails with active-recall up-sampling, and the method reaches SOTA on Mind2Web and AppWorld under strict context limits.
> Paper | Tweet
> 9. When to Retrieve During Reasoning
> Most RAG systems retrieve once, before the model starts reasoning. Large reasoning models like o1 and R1 do not work that way. They generate 12k to 25k token chains of thought and hit knowledge gaps mid-inference, long after the retrieval window closed. ReaLM-Retrieve is a reasoning-aware retrieval framework that injects evidence during multi-step inference, detects uncertainty at reasoning-step granularity, and learns a policy for when external evidence actually helps. It achieves +10.1% absolute F1 over standard RAG across MuSiQue, HotpotQA, and 2WikiMultiHopQA, with 47% fewer retrieval calls than fixed-interval IRCoT, and hits 71.2% F1 on 2-4 hop MuSiQue with only 1.8 retrieval calls per question.
> Paper | Tweet
> 10. Co-evolving Decisions and Skills
> Long-horizon agents fail in two ways: the decision-maker cannot decompose well, or the skill library goes stale. This paper introduces a co-evolution framework where an LLM decision agent and a dynamic skill bank improve each other through iterative refinement. The decision agent picks and chains skills, performance feedback updates both the policy and the skills, and new skills emerge by generalizing successful sequences instead of being hand-coded upfront. Most long-horizon agent stacks treat skills and decision-making as separate optimization problems, which is why they plateau. Co-evolution gives you adaptive planning and a growing library of reusable behaviors from a single loop, which is what you actually want when task structure is not predetermined: robotics, game agents, and complex planning.
> Paper | Tweet

- 图片：[img1](https://pbs.twimg.com/media/HHWEAeWXUAEHFq-?format=jpg&name=large) [img2](https://pbs.twimg.com/media/HHWDYukW4AEA7N-?format=jpg&name=large) [img3](https://pbs.twimg.com/media/HHWDj7LXAAA6JHr?format=png&name=large) [img4](https://pbs.twimg.com/media/HHWDoeuWEAA6jze?format=jpg&name=large) [img5](https://pbs.twimg.com/media/HHWDr9dXoAAqa2i?format=jpg&name=large) [img6](https://pbs.twimg.com/media/HHWDvSoXkAAoXD4?format=png&name=large) [img7](https://pbs.twimg.com/media/HHWDyGhX0AAmlnx?format=jpg&name=large) [img8](https://pbs.twimg.com/media/HHWD1ISWUAAG3vP?format=jpg&name=large)

#### x-2050261909690097671

**论文：Recursive Multi-Agent Systems**

- 作者：DAIR.AI (@dair_ai) · 发帖 2026-05-01 · [原帖](https://x.com/dair_ai/status/2050261909690097671)
- 来源：🔖 收藏 · 拉取 2026-10-27
- 类型：论文
- **总结**：DAIR.AI 推荐的论文《Recursive Multi-Agent Systems》（RecursiveMAS），帖子只有标题，正文在图片里。从同周论文汇总看，主题是递归组织多个 agent 来分解和解决问题。如果想细读，需要打开原帖看图或找论文原文。
- **原文**：

> NEW paper: Recursive Multi-Agent Systems

- 引用 elvis @omarsar0 · May 1:
  > // Recursive Multi-Agent Systems //
  >
  > Great read for the weekend.
  >
  > (bookmark it)
  >
  > Multi-agent systems often pass full text messages between agents at every step. This leads to token bloat, latency, and context dilution which all grow with the number of agents.
  >
  > RecursiveMAS asks a

#### x-2024602668258517440

**DeepMind + Meta + Amazon：100 页 agentic reasoning 路线图**

- 作者：Hasan Toor (@hasantoxr) · 发帖 2026-02-19 · [原帖](https://x.com/hasantoxr/status/2024602668258517440)
- 来源：🔖 收藏 · 拉取 2026-10-27
- 类型：综述解读
- **总结**：解读一篇 100 页的 agentic reasoning 综述，覆盖规划、工具使用、记忆、多 agent 协作。结论：单 agent 在稳定环境下表现好，多 agent 在动态环境下会崩；问题不在智能，而在不确定性下怎么推理。分三层：基础推理（稳定环境中规划 + 用工具）、自我演化推理（靠反馈和记忆适应）、集体推理（多 agent 协作）。警告：封闭世界的 benchmark 会高估能力。
- **原文**：

> 🚨 Google DeepMind + Meta + Amazon just dropped a 100 page roadmap that redefines what AI agents actually are.
>
> They analyzed every major agentic reasoning framework across planning, tool use, memory, and multi-agent coordination.
>
> Single-agent in stable environments: works great.
> Multi-agent in dynamic environments: falls apart.
>
> The problem isn't intelligence. It's how agents reason under uncertainty.
>
> Three layers they found that actually matter:
>
> → Foundational reasoning (planning + tool use in stable settings)
> → Self-evolving reasoning (agents that adapt through feedback and memory)
> → Collective reasoning (multiple agents coordinating toward shared goals)
>
> Even the best models struggle in open-ended environments.
> Closed-world benchmarks are lying to you.
>
> Reinforcement learning helps post-training. But in-context reasoning at test time? Still broken for long-horizon tasks.
>
> The real finding: most AI agent tutorials you've seen are built on single-task, static benchmarks.
>
> Real-world deployment robotics, healthcare, autonomous research breaks every framework on the market.
>
> And almost nobody is building for that gap.
>
> The future isn't smarter models. It's agents that plan, act, and learn across dynamic environments without falling apart mid-task.
>
> This survey is the closest thing to a unified blueprint for that.
>
> 100% free on arXiv.
>
> [2] Paper Link:

- 图片：[img1](https://pbs.twimg.com/media/HBjVZZnbUAAKjGd?format=jpg&name=large)

### 📂 LLM 基础 & 课程

#### x-2104453599367770287

**Stanford CS329A：Self-Improving AI Agents 课程**

- 作者：meng shao (@shao__meng) · 发帖 2026-09-28 · [原帖](https://x.com/shao__meng/status/2104453599367770287)
- 来源：🔖 收藏 · 拉取 2026-10-27
- 类型：课程推荐
- **总结**：推荐斯坦福 CS329A《Self-Improving AI Agents》，由 Aakanksha Chowdhery 和 Azalia Mirhoseini 主讲，9 讲视频都在 YouTube 上；作者另做了一个预告视频。thread 里还补充了 CS329Z《Engineering AI Agents》第二讲（LLMs for Builders）。观点：即使 agent 已经很强，系统学一遍大学课程对建立全局认知仍然有价值。附课程主页和播放列表。
- **原文**：

> 斯坦福大学课程 CS329A: Self-Improving AI Agents  
>
> 斯坦福大学 @achowdhery @Azaliamirh 两位老师主讲，他们在 Google Brain / Deepmind 有过合作经历，现在合作连续两年讲授 AI Agents 课程。
>
> 分享这门课程后，类似获得了超过 5K+ 点赞和收藏，看到很多朋友喜欢，我也把 9 个视频做了一个预告视频，让大家对课程可以更快有更直观的感受。
>
> 虽然 AI Agent 已经强大到很多人觉得不需要再学习，什么问题都可以直接问，到顶级大学的基础课程，系统学习下来，还是会很有收获，全局认知的提升。 马上长假了，收藏学起来！ 
>
> 课程主页： https://cs329a.stanford.edu
> 视频列表： https://youtube.com/playlist?list=PLangBM27OtEA&si=khxaTCYv_ARHBgBl
>
> [2] 斯坦福大学 CS329Z「Engineering AI Agents」第二讲 LLMs for Builders：Agent 工程师必修的大模型底层原理

- 引用 meng shao @shao__meng · Sep 27:
  > 斯坦福大学课程 CS329A: Self-Improving AI Agents
  >
  > 课程 9 讲视频都已发布在 Youtube，第 1 讲 52 万观看，第 9 讲 1.5 万。趁假期坚持看完 9 讲视频，你就超过了中间的 50 多万人，和连第 1 讲都没看过的无数人 😂
  >
  > 开玩笑，虽然 AI Agent  x.com/shao__meng/sta…
- 含视频（未转写）

#### x-2078533887383556335

**Karpathy 3 小时：从零构建 LLM**

- 作者：Roan (@RohOnChain) · 发帖 2026-07-18 · [原帖](https://x.com/RohOnChain/status/2078533887383556335)
- 来源：🔖 收藏 · 拉取 2026-10-27
- 类型：课程推荐
- **总结**：推荐 Karpathy 的 3 小时 LLM 课程：LLM 简介、训练流水线、工具与插件、Transformer 架构、scaling。包装成「靠这个视频拿到 Anthropic offer」的故事，营销味重，但课程本身是公认的 LLM 原理入门材料。
- **原文**：

> My friend applied to 300 tech jobs in two years. No MIT. No Stanford.
>
> Last month Anthropic offered him $750,000.
>
> I asked him how he broke in from zero.
>
> He sent me the exact video that got him in. Andrej Karpathy's 3-hour course on building a full LLM from scratch.
>
> Anthropic's own researcher shows you how LLMs like ChatGPT & Claude are actually built.
>
> I watched it last night.
>
> Halfway through, I realized it's embarrassingly simple to break into an AI lab.
>
> Bookmark this and read the article below.
>
> • 00:00 - intro to LLMs
> • 12:41 - LLM training pipeline
> • 31:58 - LLM tools & plugins
> • 41:14 - LLM transformer architecture
> • 2:19:02 - scaling the LLM

- 含视频（未转写）

### 📂 其他应用

#### x-2081656879886012676

**Graph Engineering for Quants：GNN 量化大师课**

- 作者：venus (@RitOnchain) · 发帖 2026-07-27 · [原帖](https://x.com/RitOnchain/status/2081656879886012676)
- 来源：🔖 收藏 · 拉取 2026-10-27
- 类型：方法介绍 + 代码
- **总结**：这里的 graph 指图神经网络，不是 agent graph。观点：市场是关系系统，收益信号藏在供应链、同行、共同持仓这些关系里。讲 GCN、GAT、Temporal Graph Networks 的数学基础，并给出 PyTorch Geometric 代码：用行业和相关性构建邻接矩阵，用 GAT 预测股票收益。偏量化金融应用，和 agent 主题无关。
- **原文**：

> 《Graph Engineering for Quants : The Complete Masterclass》
>
> Financial markets are, at their core, relational systems. A stock does not move in isolation - it moves because its largest customer cut orders, because its sector peers reported earnings, because a sovereign credit event repriced its debt covenants, or because a shared institutional holder is liquidating across a correlated book. The return signal is not in the stock's own time series. It is in the web of relationships surrounding it.
> Traditional quantitative models have always known this, but they have approximated it with blunt instruments: sector dummies, correlation matrices, factor loadings on common indices. These approximations collapse the true relational structure of markets into a handful of linear scalars and then lose everything else. Graph Neural Networks (GNNs) change this. They operate directly on the relational structure - stocks as nodes, their economic relationships as edges - and learn to propagate signals through the network in ways that capture momentum spillovers, supply chain contagion, volatility transmission, and cross-market dependencies that flat time-series models fundamentally cannot see.
> This article covers the full spectrum: the mathematical foundations, every major GNN architecture used in production quantitative finance, five distinct use cases from stock prediction to fraud detection, and complete runnable PyTorch Geometric code for each one. Every result cited is from peer-reviewed research or documented production deployments.
> about me : I am Venus (open-source-believer, so spitting out internal secrets on X),  a Senior Quant Systems Architect and Backend Engineer experienced in building startups from 0→1 and scaling products from 1→100 across AI, cloud, and fintech x defi infrastructure. dm's are open to connect. Let's get back to article.
> Why Graphs Belong in the Quant Toolkit
> The empirical case is now clear and consistent across multiple research groups and time periods.
> A deep GNN model integrating correlation structure and attention mechanism on CSI 300 constituent stocks from 2018 to 2023 achieved 78.9% directional accuracy with an RMSE of 0.0182 - a 23.5% improvement over traditional methods, with prediction accuracy staying above 75.8% during typical volatility periods.
> A graph attention-based heterogeneous multi-agent deep reinforcement learning framework tested on S&P 500, NASDAQ 100, and Russell 2000 datasets achieved 16.8% annualized returns, a 1.34 Sharpe ratio, and 8.2% maximum drawdown, significantly outperforming traditional mean-variance optimization.
> Research directly testing GCN and GAT architectures against traditional ML for systemic risk classification on financial networks reported a 94% MCC improvement for GNNs - the strongest published evidence that graph structure improves financial risk detection.
> BlackRock has deployed turnover-constrained GNNs across $50 billion in ETF assets, with risk-adjusted returns improving by 15–393% through attention-based volatility scaling and cost-aware regularization reducing turnover by 20–40% without compromising performance.
> These are not academic curiosities. They reflect a fundamental insight: inter-stock dependencies, supply chain connections, and the diffusion of market sentiment all constitute a structured graphical information system. Relying solely on traditional sequence models fails to capture the underlying interactions and structured dependencies among stocks. This has become a key factor limiting prediction accuracy in large-scale quantitative systems.
> The Mathematical Foundation
> Before writing any code, you need the math. A graph is defined as G = (V, E), where V is the set of nodes and E is the set of edges. In finance, nodes are typically stocks, companies, or financial institutions. Edges represent the relationships between them: correlation, supply chain links, shared ownership, regulatory exposure, or sector membership.
> Each node v ∈ V carries a feature vector x_v ∈ ℝ^d. The adjacency matrix A ∈ ℝ^{|V|×|V|} encodes the edge structure. The degree matrix D is diagonal with D_{ii} = Σ_j A_{ij}.
> 2.1 Graph Convolutional Networks (GCN)
> The GCN layer, introduced by Kipf and Welling (2017), performs the following update:
> 𝐻
> (
> 𝑙
> +
> 1
> )
> =
> 𝜎
> (
> 𝐷
> ~
> −
> 1
> /
> 2
> 𝐴
> ~
> 𝐷
> ~
> −
> 1
> /
> 2
> 𝐻
> (
> 𝑙
> )
> 𝑊
> (
> 𝑙
> )
> )
> where Ã = A + I is the adjacency matrix with added self-loops, D̃ is the corresponding degree matrix, H^{(l)} is the node feature matrix at layer l, W^{(l)} is the learnable weight matrix, and σ is an activation function. The symmetric normalization D̃^{-1/2} Ã D̃^{-1/2} ensures that aggregation is normalized by both source and target node degree, preventing scale issues when nodes have wildly different numbers of neighbors - which is common in financial networks where major index components have many more correlated peers than small-caps.
> 2.2 Graph Attention Networks (GAT)
> GCN treats all neighbors equally. GAT, introduced by Veličković et al. (2018), computes attention weights between nodes:
> 𝛼
> 𝑖
> 𝑗
> =
> exp
> ⁡
> (
> LeakyReLU
> (
> 𝑎
> ⊤
> [
> 𝑊
> ℎ
> 𝑖
> ∥
> 𝑊
> ℎ
> 𝑗
> ]
> )
> )
> ∑
> 𝑘
> ∈
> 𝑁
> (
> 𝑖
> )
> exp
> ⁡
> (
> LeakyReLU
> (
> 𝑎
> ⊤
> [
> 𝑊
> ℎ
> 𝑖
> ∥
> 𝑊
> ℎ
> 𝑘
> ]
> )
> )
> The node update is then:
> ℎ
> 𝑖
> (
> 𝑙
> +
> 1
> )
> =
> 𝜎
> (
> ∑
> 𝑗
> ∈
> 𝑁
> (
> 𝑖
> )
> 𝛼
> 𝑖
> 𝑗
> 𝑊
> ℎ
> 𝑗
> (
> 𝑙
> )
> )
> For stock prediction, this is transformative. The attention weight α_{ij} learns which relationships are actually predictive - a momentum spillover from semiconductor suppliers to device manufacturers matters more than a spurious correlation between two stocks that happened to co-move last quarter. The model discovers these weights from data rather than imposing them by hand.
> 2.3 Temporal Graph Networks
> Static GNNs assume the graph structure is fixed. Financial networks are not. Correlations shift across regimes, supply chains restructure, and institutional ownership changes. Temporal Graph Networks (TGN) extend the GNN framework to continuous-time dynamic graphs where edges arrive as timestamped events. The TGN memory module maintains a state for each node that is updated whenever the node is involved in an interaction:
> 𝑠
> 𝑖
> (
> 𝑡
> )
> =
> mem
> (
> 𝑠
> 𝑖
> (
> 𝑡
> −
> )
> ,
> msg
> (
> 𝑠
> 𝑖
> (
> 𝑡
> −
> )
> ,
> 𝑠
> 𝑗
> (
> 𝑡
> −
> )
> ,
> Δ
> 𝑡
> ,
> 𝑒
> 𝑖
> 𝑗
> (
> 𝑡
> )
> )
> )
> where s_i(t) is the memory state of node i at time t, msg is a message function, and e_{ij}(t) is the edge feature at time t. The node embedding is then computed by a graph attention aggregator on top of the memory states.
> Use Case 1: Stock Return Prediction with Sector and Supply Chain Graphs
> The foundational quant application. Stocks in the same sector and supply chain exhibit correlated return dynamics. A GNN encodes these relationships into the embedding space and uses them to predict next-period returns.
> Graph construction: Nodes are stocks. Two types of edges are commonly used: sector edges connecting all stocks within the same GICS sector, and supply chain edges connecting companies with documented customer-supplier relationships (sourced from FactSet, Bloomberg Supply Chain, or SEC filings). Edge weights can be set uniformly (binary graph) or by relationship strength (revenue exposure percentage for supply chain edges, correlation coefficient for sector edges).
> Inter-industry linkages, supply chain connections between companies, and the diffusion of market sentiment all constitute a structured graphical information system. GNNs can extract interaction information embedded in the graph structure through iterative updates of node features, capturing potential correlations that are often overlooked by traditional models.
> python
> """
> Stock Return Prediction with Graph Attention Network
> Uses sector + correlation-based adjacency matrix
> Dependencies: torch, torch_geometric, pandas, numpy, yfinance
> """
>
> import torch
> import torch.nn as nn
> import torch.nn.functional as F
> import numpy as np
> import pandas as pd
> import yfinance as yf
> from torch_geometric.data import Data, DataLoader
> from torch_geometric.nn import GATConv, GCNConv
> from torch_geometric.utils import dense_to_sparse
> from sklearn.preprocessing import StandardScaler
> from sklearn.model_selection import TimeSeriesSplit
>
>
> # ============================================================
> # 1. Data Preparation and Graph Construction
> # ============================================================
>
> def fetch_price_data(tickers: list, start: str, end: str) -> pd.DataFrame:
>     """
>     Fetch adjusted close prices for a list of tickers.
>     Returns a DataFrame with tickers as columns.
>     """
>     raw = yf.download(tickers, start=start, end=end,
>                       auto_adjust=True, progress=False)["Close"]
>     raw = raw.dropna(how="all", axis=1)
>     raw = raw.ffill().dropna()
>     return raw
>
>
> def compute_features(prices: pd.DataFrame,
>                      lookback: int = 20) -> pd.DataFrame:
>     """
>     Compute node features for each stock at each time step.
>     Features: 20-day return, 5-day return, 20-day volatility,
>               RSI(14), volume-adjusted momentum proxy,
>               normalized price relative to 52-week high/low.
>     """
>     features = pd.DataFrame(index=prices.index)
>     log_ret = np.log(prices / prices.shift(1))
>
>     for col in prices.columns:
>         r = log_ret[col]
>         features[f"{col}_ret20"] = r.rolling(lookback).sum()
>         features[f"{col}_ret5"]  = r.rolling(5).sum()
>         features[f"{col}_vol20"] = r.rolling(lookback).std()
>
>         # RSI (14-day)
>         delta   = r.diff()
>         gain    = delta.clip(lower=0).rolling(14).mean()
>         loss    = (-delta.clip(upper=0)).rolling(14).mean()
>         rs      = gain / (loss + 1e-8)
>         features[f"{col}_rsi14"] = 100 - (100 / (1 + rs))
>
>         # 52-week range position
>         high52  = prices[col].rolling(252, min_periods=20).max()
>         low52   = prices[col].rolling(252, min_periods=20).min()
>         features[f"{col}_range_pos"] = (
>             (prices[col] - low52) / (high52 - low52 + 1e-8)
>         )
>
>     return features.dropna()
>
>
> def build_correlation_adjacency(returns: pd.DataFrame,
>                                 threshold: float = 0.3,
>                                 window: int = 60) -> np.ndarray:
>     """
>     Build adjacency matrix from rolling Pearson correlations.
>     Edge exists if |corr| > threshold.
>     Returns: binary adjacency matrix of shape (n_stocks, n_stocks).
>
>     Note: adjacency is computed on training data only to avoid
>     look-ahead bias when used in rolling walk-forward.
>     """
>     corr_matrix = returns.tail(window).corr().values
>     adj = (np.abs(corr_matrix) > threshold).astype(float)
>     np.fill_diagonal(adj, 1.0)   # self-loops
>     return adj
>
>
> def build_sector_adjacency(tickers: list,
>                            sector_map: dict) -> np.ndarray:
>     """
>     Build adjacency matrix from sector membership.
>     Two stocks in the same GICS sector are connected.
>     sector_map: {ticker: sector_string}
>     """
>     n = len(tickers)
>     adj = np.zeros((n, n))
>     for i, t_i in enumerate(tickers):
>         for j, t_j in enumerate(tickers):
>             if i == j:
>                 adj[i, j] = 1.0     # self-loop
>             elif sector_map.get(t_i) == sector_map.get(t_j):
>                 adj[i, j] = 1.0
>     return adj
>
>
> def combine_adjacency(adj_corr: np.ndarray,
>                       adj_sector: np.ndarray,
>                       w_corr: float = 0.5,
>                       w_sector: float = 0.5) -> np.ndarray:
>     """Combine correlation and sector adjacency matrices."""
>     combined = w_corr * adj_corr + w_sector * adj_sector
>     # Binarize: edge exists if combined weight > 0.3
>     return (combined > 0.3).astype(float)
>
>
> def build_graph_dataset(features_np: np.ndarray,
>                         adj: np.ndarray,
>                         targets: np.ndarray,
>                         n_stocks: int,
>                         n_features_per_stock: int) -> list:
>     """
>     Convert feature arrays into PyTorch Geometric Data objects.
>     One Data object per time step.
>
>     features_np: (T, n_stocks * n_features_per_stock)
>     adj:         (n_stocks, n_stocks)
>     targets:     (T, n_stocks) — next-period returns
>     """
>     edge_index, _ = dense_to_sparse(
>         torch.FloatTensor(adj)
>     )   # (2, num_edges)
>
>     dataset = []
>     for t in range(len(features_np)):
>         # Node features: (n_stocks, n_features_per_stock)
>         x = torch.FloatTensor(
>             features_np[t].reshape(n_stocks, n_features_per_stock)
>         )
>         y = torch.FloatTensor(targets[t])   # (n_stocks,)
>
>         data = Data(x=x, edge_index=edge_index, y=y)
>         dataset.append(data)
>
>     return dataset
>
>
> # ============================================================
> # 2. Graph Attention Network Architecture
> # ============================================================
>
> class StockGAT(nn.Module):
>     """
>     Multi-layer Graph Attention Network for stock return prediction.
>
>     Architecture:
>         Input node features  →  GAT Layer 1  →  GAT Layer 2  →
>         Residual connection  →  LayerNorm  →  MLP head  →
>         Per-node return predictions
>     """
>
>     def __init__(self,
>                  in_channels: int,
>                  hidden_channels: int = 64,
>                  out_channels: int = 1,
>                  n_heads: int = 4,
>                  dropout: float = 0.2):
>         super().__init__()
>
>         self.gat1 = GATConv(
>             in_channels=in_channels,
>             out_channels=hidden_channels,
>             heads=n_heads,
>             dropout=dropout,
>             concat=True
>         )
>         # After concat: hidden_channels * n_heads features per node
>         self.gat2 = GATConv(
>             in_channels=hidden_channels * n_heads,
>             out_channels=hidden_channels,
>             heads=1,
>             dropout=dropout,
>             concat=False
>         )
>
>         # Residual projection (maps input dim to hidden dim)
>         self.residual_proj = nn.Linear(in_channels, hidden_channels)
>
>         self.norm = nn.LayerNorm(hidden_channels)
>         self.dropout = nn.Dropout(dropout)
>
>         # Prediction head: (hidden_channels -> 32 -> out_channels)
>         self.head = nn.Sequential(
>             nn.Linear(hidden_channels, 32),
>             nn.ReLU(),
>             nn.Dropout(dropout),
>             nn.Linear(32, out_channels)
>         )
>
>     def forward(self, x, edge_index):
>         """
>         Args:
>             x:           (num_nodes, in_channels)
>             edge_index:  (2, num_edges)
>         Returns:
>             pred:        (num_nodes, out_channels)
>         """
>         residual = self.residual_proj(x)     # (N, hidden)
>
>         h = self.gat1(x, edge_index)         # (N, hidden * heads)
>         h = F.elu(h)
>         h = self.dropout(h)
>
>         h = self.gat2(h, edge_index)         # (N, hidden)
>         h = h + residual                     # residual connection
>         h = self.norm(h)
>         h = F.elu(h)
>
>         pred = self.head(h)                  # (N, 1)
>         return pred.squeeze(-1)              # (N,)
>
> python
> # ============================================================
> # 3. Hybrid GCN + LSTM for Temporal-Structural Modeling
> # ============================================================
>
> class GCN_LSTM(nn.Module):
>     """
>     Hybrid model: GCN extracts structural node embeddings,
>     LSTM models temporal dynamics across the sequence.
>
>     Based on the architecture used in GCN-LSTM papers
>     for ES-mini and VX Futures Forecasting (2024).
>
>     Input:  Sequence of graph snapshots (T, N, F)
>     Output: Per-node predictions at the final time step (N, 1)
>     """
>
>     def __init__(self,
>                  in_channels: int,
>                  gcn_hidden: int = 32,
>                  lstm_hidden: int = 64,
>                  lstm_layers: int = 2,
>                  out_channels: int = 1,
>                  dropout: float = 0.2):
>         super().__init__()
>         self.gcn = GCNConv(in_channels, gcn_hidden)
>         self.lstm = nn.LSTM(
>             input_size=gcn_hidden,
>             hidden_size=lstm_hidden,
>             num_layers=lstm_layers,
>             batch_first=True,
>             dropout=dropout if lstm_layers > 1 else 0.0
>         )
>         self.head = nn.Linear(lstm_hidden, out_channels)
>         self.dropout = nn.Dropout(dropout)
>
>     def forward(self, x_seq, edge_index):
>         """
>         Args:
>             x_seq:      (T, N, F) — T time steps, N nodes, F features
>             edge_index: (2, E) — static graph structure
>         Returns:
>             pred:       (N, out_channels)
>         """
>         T, N, F = x_seq.shape
>         gcn_outs = []
>
>         for t in range(T):
>             h_t = F_act(self.gcn(x_seq[t], edge_index))   # (N, gcn_hidden)
>             gcn_outs.append(h_t)
>
>         # Stack to (N, T, gcn_hidden) then pass through LSTM
>         gcn_stack = torch.stack(gcn_outs, dim=1)           # (N, T, gcn_hidden)
>         gcn_stack = self.dropout(gcn_stack)
>
>         lstm_out, _ = self.lstm(gcn_stack)                 # (N, T, lstm_hidden)
>         # Take the last time step
>         last = lstm_out[:, -1, :]                          # (N, lstm_hidden)
>         pred = self.head(last)                             # (N, out_channels)
>         return pred
>
>
> # Use F_act to avoid shadowing the F.elu import
> F_act = F.elu
>
>
> # ============================================================
> # 4. Training and Evaluation Utilities
> # ============================================================
>
> def information_coefficient(pred: np.ndarray,
>                             target: np.ndarray) -> float:
>     """
>     Pearson correlation between predicted and realized returns
>     across all stocks in a given time period.
>     The standard evaluation metric for cross-sectional alpha models.
>     """
>     if pred.std() < 1e-8 or target.std() < 1e-8:
>         return 0.0
>     return float(np.corrcoef(pred, target)[0, 1])
>
>
> def rank_ic(pred: np.ndarray, target: np.ndarray) -> float:
>     """
>     Spearman rank correlation (RankIC).
>     More robust than IC to outlier returns.
>     """
>     from scipy.stats import spearmanr
>     rho, _ = spearmanr(pred, target)
>     return float(rho)
>
>
> def directional_accuracy(pred: np.ndarray,
>                          target: np.ndarray) -> float:
>     """Fraction of stocks where sign(pred) == sign(target)."""
>     return float(np.mean(np.sign(pred) == np.sign(target)))
>
>
> def train_epoch(model, loader, optimizer,
>                 device, loss_fn=None):
>     """Single training epoch over a DataLoader of graph snapshots."""
>     model.train()
>     total_loss = 0.0
>     if loss_fn is None:
>         loss_fn = nn.MSELoss()
>
>     for batch in loader:
>         batch = batch.to(device)
>         optimizer.zero_grad()
>         pred = model(batch.x, batch.edge_index)
>         loss = loss_fn(pred, batch.y)
>         loss.backward()
>         torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
>         optimizer.step()
>         total_loss += loss.item()
>
>     return total_loss / len(loader)
>
>
> @torch.no_grad()
> def evaluate(model, loader, device):
>     """Evaluate model; return IC, RankIC, directional accuracy."""
>     model.eval()
>     all_pred, all_true = [], []
>
>     for batch in loader:
>         batch = batch.to(device)
>         pred = model(batch.x, batch.edge_index).cpu().numpy()
>         true = batch.y.cpu().numpy()
>         all_pred.append(pred)
>         all_true.append(true)
>
>     preds  = np.concatenate(all_pred)
>     truths = np.concatenate(all_true)
>
>     return {
>         "IC":    information_coefficient(preds, truths),
>         "RankIC": rank_ic(preds, truths),
>         "DirAcc": directional_accuracy(preds, truths)
>     }
>
>
> # ============================================================
> # 5. Full Training Pipeline
> # ============================================================
>
> def run_stock_prediction_pipeline():
>     """
>     End-to-end pipeline for stock return prediction with GAT.
>     Uses S&P 500 tech sector as a demonstration universe.
>     """
>     device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
>     print(f"Device: {device}")
>
>     # --- Universe and sector map ---
>     tickers = [
>         "AAPL", "MSFT", "NVDA", "GOOGL", "META",
>         "AMZN", "TSLA", "AVGO", "ORCL", "ADBE",
>         "AMD",  "INTC", "QCOM", "TXN",  "MU"
>     ]
>     sector_map = {t: "Technology" for t in tickers}
>     # In production, use a proper GICS sector database
>     # and include cross-sector edges
>
>     # --- Fetch data ---
>     prices = fetch_price_data(tickers, start="2019-01-01", end="2024-12-31")
>     tickers = [t for t in tickers if t in prices.columns]   # drop failures
>     n_stocks = len(tickers)
>     print(f"Stocks: {n_stocks}, Trading days: {len(prices)}")
>
>     # --- Compute features ---
>     features = compute_features(prices)
>     features = features.dropna()
>     n_feat_per_stock = 5    # ret20, ret5, vol20, rsi14, range_pos
>
>     # Align prices and features
>     common_idx = features.index.intersection(prices.index)
>     features = features.loc[common_idx]
>     prices   = prices.loc[common_idx]
>
>     # --- Targets: next-period 5-day forward return ---
>     log_ret = np.log(prices / prices.shift(1))
>     fwd_ret = log_ret.shift(-5)   # 5-day forward return
>
>     # Align features to have valid forward returns
>     valid_idx = fwd_ret.dropna().index
>     valid_idx = valid_idx.intersection(features.index)
>     features = features.loc[valid_idx]
>     fwd_ret  = fwd_ret.loc[valid_idx]
>
>     # --- Build adjacency (on full sample for simplicity;
>     #     in production compute rolling on training window only) ---
>     adj_corr   = build_correlation_adjacency(log_ret.loc[valid_idx],
>                                              threshold=0.25,
>                                              window=120)
>     adj_sector = build_sector_adjacency(tickers, sector_map)
>     adj        = combine_adjacency(adj_corr, adj_sector)
>     print(f"Graph: {n_stocks} nodes, {int(adj.sum())} edges")
>
>     # --- Normalize features ---
>     feat_array  = features.values                     # (T, n_stocks * 5)
>     target_array = fwd_ret[tickers].values            # (T, n_stocks)
>
>     scaler = StandardScaler()
>     feat_norm = scaler.fit_transform(feat_array)
>
>     # --- Build dataset ---
>     dataset = build_graph_dataset(
>         feat_norm, adj, target_array, n_stocks, n_feat_per_stock
>     )
>
>     # --- Walk-forward split: 70% train, 15% val, 15% test ---
>     T = len(dataset)
>     t1 = int(0.70 * T)
>     t2 = int(0.85 * T)
>
>     train_data = dataset[:t1]
>     val_data   = dataset[t1:t2]
>     test_data  = dataset[t2:]
>     print(f"Train: {t1}, Val: {t2-t1}, Test: {T-t2} snapshots")
>
>     train_loader = DataLoader(train_data, batch_size=32, shuffle=True)
>     val_loader   = DataLoader(val_data,   batch_size=32, shuffle=False)
>     test_loader  = DataLoader(test_data,  batch_size=32, shuffle=False)
>
>     # --- Initialise model ---
>     model = StockGAT(
>         in_channels=n_feat_per_stock,
>         hidden_channels=64,
>         out_channels=1,
>         n_heads=4,
>         dropout=0.2
>     ).to(device)
>
>     n_params = sum(p.numel() for p in model.parameters()
>                    if p.requires_grad)
>     print(f"Model parameters: {n_params:,}")
>
>     optimizer = torch.optim.AdamW(
>         model.parameters(), lr=1e-3, weight_decay=1e-4
>     )
>     scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(
>         optimizer, T_max=100
>     )
>
>     # --- Training loop ---
>     best_val_ic = -np.inf
>     print("\nTraining StockGAT...")
>
>     for epoch in range(1, 101):
>         train_loss = train_epoch(model, train_loader, optimizer, device)
>         val_metrics = evaluate(model, val_loader, device)
>         scheduler.step()
>
>         if val_metrics["IC"] > best_val_ic:
>             best_val_ic = val_metrics["IC"]
>             torch.save(model.state_dict(), "best_stock_gat.pt")
>
>         if epoch % 20 == 0:
>             print(
>                 f"Epoch {epoch:3d} | Loss {train_loss:.4f} | "
>                 f"Val IC {val_metrics['IC']:.4f} | "
>                 f"Val RankIC {val_metrics['RankIC']:.4f} | "
>                 f"Val DirAcc {val_metrics['DirAcc']:.3f}"
>             )
>
>     # --- Test evaluation ---
>     model.load_state_dict(torch.load("best_stock_gat.pt"))
>     test_metrics = evaluate(model, test_loader, device)
>     print(f"\nTest IC:      {test_metrics['IC']:.4f}")
>     print(f"Test RankIC:  {test_metrics['RankIC']:.4f}")
>     print(f"Test DirAcc:  {test_metrics['DirAcc']:.3f}")
>
>     return model
>
>
> if __name__ == "__main__":
>     model = run_stock_prediction_pipeline()
> Use Case 2: Volatility Forecasting with Dynamic Graph Structure
> Volatility spillovers between markets are directional and regime-dependent. A shock in the US equity market propagates differently to European and Asian markets depending on the macro regime. Static correlation matrices miss this directionality. A Temporal GAT built on a Diebold-Yilmaz spillover network captures it.
> The Temporal Graph Attention Network (Temporal GAT), combining GCN and GAT components, captures the temporal and structural dynamics of volatility spillovers. Adjacency matrices are constructed using either Pearson correlations among realized volatilities (giving a symmetric graph) or the Diebold-Yilmaz volatility spillover index computed via variance decomposition of VAR models (giving a directed graph that captures how volatility from one market affects another). Empirical results from a 15-year study of eight major global indices show that the Temporal GAT outperforms traditional GARCH models and other machine learning methods.
> The key design requirement from the literature: adjacency matrices must be constructed separately for training, validation, and test sets, using only information available within each respective period. No future observations beyond the boundaries of a given partition are used when defining the graph topology for that period. This is the graph-structure version of look-ahead bias. Violating it invalidates the entire backtest.
> python
> """
> Volatility Forecasting with Temporal GAT
> Dynamic adjacency via rolling Pearson correlation
> Dependencies: torch, torch_geometric, numpy, pandas, scipy
> """
>
> import torch
> import torch.nn as nn
> import torch.nn.functional as F
> import numpy as np
> import pandas as pd
> from torch_geometric.nn import GATConv
> from torch_geometric.utils import dense_to_sparse
>
>
> # ============================================================
> # 1. Dynamic Adjacency Builder
> # ============================================================
>
> def compute_rolling_adjacency(realized_vol: np.ndarray,
>                                window: int = 60,
>                                threshold: float = 0.3
>                                ) -> list[np.ndarray]:
>     """
>     Build a rolling adjacency matrix for each time step.
>     realized_vol: (T, N) — realized volatility for N assets
>     Returns list of N×N adjacency matrices, one per time step.
>
>     CRITICAL: adjacency at step t uses ONLY data up to t
>     (no look-ahead bias in graph structure).
>     """
>     T, N = realized_vol.shape
>     adjacencies = []
>
>     for t in range(T):
>         start = max(0, t - window + 1)
>         window_data = realized_vol[start : t + 1]   # (<=window, N)
>
>         if window_data.shape[0] < 10:
>             # Not enough data: use identity (self-loops only)
>             adj = np.eye(N)
>         else:
>             corr = np.corrcoef(window_data.T)         # (N, N)
>             np.fill_diagonal(corr, 1.0)
>             adj = (np.abs(corr) > threshold).astype(float)
>
>         adjacencies.append(adj)
>
>     return adjacencies
>
>
> # ============================================================
> # 2. Temporal GAT for Volatility Forecasting
> # ============================================================
>
> class TemporalGAT_Vol(nn.Module):
>     """
>     Temporal Graph Attention Network for volatility forecasting.
>
>     Architecture (following Temporal GAT for volatility spillovers):
>     - GATConv encodes spatial (cross-market) dependencies
>     - GRU captures temporal dynamics of node embeddings
>     - MLP head outputs one-step-ahead realized volatility
>
>     Input:  (seq_len, N, F) per call — sequence of graph snapshots
>     Output: (N,) — next-step volatility forecast for each asset
>     """
>
>     def __init__(self,
>                  in_channels: int,
>                  gat_hidden: int = 32,
>                  gru_hidden: int = 64,
>                  n_heads: int = 4,
>                  dropout: float = 0.1):
>         super().__init__()
>
>         self.gat = GATConv(
>             in_channels=in_channels,
>             out_channels=gat_hidden,
>             heads=n_heads,
>             dropout=dropout,
>             concat=True
>         )
>         gat_out_dim = gat_hidden * n_heads
>
>         self.gru = nn.GRU(
>             input_size=gat_out_dim,
>             hidden_size=gru_hidden,
>             num_layers=2,
>             batch_first=True,
>             dropout=dropout
>         )
>         self.head = nn.Sequential(
>             nn.Linear(gru_hidden, 32),
>             nn.ReLU(),
>             nn.Linear(32, 1)
>         )
>         self.dropout = nn.Dropout(dropout)
>
>     def forward(self, x_seq: list, edge_indices: list):
>         """
>         Args:
>             x_seq:        list of T tensors, each (N, F)
>             edge_indices: list of T tensors, each (2, E_t) —
>                           dynamic graph at each time step
>         Returns:
>             pred: (N,) volatility forecast
>         """
>         N = x_seq[0].shape[0]
>         T = len(x_seq)
>         gat_embeds = []
>
>         for t in range(T):
>             h_t = self.gat(x_seq[t], edge_indices[t])   # (N, gat*heads)
>             h_t = F.elu(h_t)
>             h_t = self.dropout(h_t)
>             gat_embeds.append(h_t)
>
>         # Stack to (N, T, gat_hidden*heads)
>         stacked = torch.stack(gat_embeds, dim=1)         # (N, T, H)
>
>         gru_out, _ = self.gru(stacked)                   # (N, T, gru_hidden)
>         last = gru_out[:, -1, :]                         # (N, gru_hidden)
>
>         pred = self.head(last).squeeze(-1)               # (N,)
>         return F.softplus(pred)    # Ensure non-negative volatility
>
>
> # ============================================================
> # 3. Synthetic Data Demo (replace with real realized vol data)
> # ============================================================
>
> def generate_synthetic_vol_data(T: int = 500,
>                                 N: int = 8,
>                                 seed: int = 42
>                                 ) -> tuple[np.ndarray, np.ndarray]:
>     """
>     Generate synthetic realized volatility data with
>     cross-asset spillover structure (for demonstration).
>     Returns: (realized_vol, features) both (T, N)
>     """
>     rng = np.random.RandomState(seed)
>
>     # Base volatility processes (GARCH-like)
>     vol = np.zeros((T, N))
>     vol[0] = rng.uniform(0.01, 0.03, N)
>
>     for t in range(1, T):
>         shock   = rng.randn(N) * 0.005
>         # Spillover: asset 0 affects assets 1 and 2
>         spillover = np.zeros(N)
>         spillover[1] += 0.3 * vol[t - 1, 0]
>         spillover[2] += 0.2 * vol[t - 1, 0]
>
>         vol[t] = np.clip(
>             0.85 * vol[t - 1] + spillover + np.abs(shock),
>             0.001, 0.15
>         )
>
>     # Features per node: [current vol, lag-1 vol, lag-5 vol mean,
>     #                     30-day rolling mean vol]
>     features = np.stack([
>         vol,
>         np.roll(vol, 1, axis=0),
>         np.array([vol[max(0, t - 5):t + 1].mean(axis=0) for t in range(T)]),
>         np.array([vol[max(0, t - 30):t + 1].mean(axis=0) for t in range(T)])
>     ], axis=-1)   # (T, N, 4)
>
>     return vol, features
>
>
> def run_volatility_pipeline():
>     """
>     Demonstrate Temporal GAT volatility forecasting.
>     In production: replace synthetic data with realized vol
>     from CBOE, Bloomberg, or computed from intraday returns.
>     """
>     device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
>
>     T, N = 500, 8
>     SEQ_LEN = 10      # look-back window per forecast step
>     IN_CHANNELS = 4   # number of features per node
>
>     # Generate data
>     realized_vol, features = generate_synthetic_vol_data(T, N)
>     targets = np.roll(realized_vol, -1, axis=0)   # next-step target
>
>     # Build dynamic adjacency (no look-ahead)
>     print("Building dynamic adjacency matrices...")
>     adjacencies = compute_rolling_adjacency(
>         realized_vol, window=60, threshold=0.25
>     )
>
>     # Prepare sequences
>     def build_sequences(start, end):
>         seqs, adj_seqs, tgt_list = [], [], []
>         for t in range(start, end - 1):
>             if t < SEQ_LEN:
>                 continue
>             x_seq = [
>                 torch.FloatTensor(features[t - SEQ_LEN + s])
>                 for s in range(SEQ_LEN)
>             ]
>             ei_seq = [
>                 dense_to_sparse(torch.FloatTensor(adjacencies[t - SEQ_LEN + s]))[0]
>                 for s in range(SEQ_LEN)
>             ]
>             seqs.append(x_seq)
>             adj_seqs.append(ei_seq)
>             tgt_list.append(torch.FloatTensor(targets[t]))
>         return seqs, adj_seqs, tgt_list
>
>     split1 = int(0.70 * T)
>     split2 = int(0.85 * T)
>
>     train_seqs, train_adjs, train_tgts = build_sequences(0,       split1)
>     val_seqs,   val_adjs,   val_tgts   = build_sequences(split1,  split2)
>     test_seqs,  test_adjs,  test_tgts  = build_sequences(split2,  T)
>
>     # Model
>     model = TemporalGAT_Vol(
>         in_channels=IN_CHANNELS,
>         gat_hidden=32,
>         gru_hidden=64,
>         n_heads=4,
>         dropout=0.1
>     ).to(device)
>
>     optimizer = torch.optim.Adam(model.parameters(), lr=5e-4)
>
>     def step(seqs, adjs, tgts, train=True):
>         """Process a list of sequences (no batching for simplicity)."""
>         model.train(train)
>         total_loss = 0.0
>         with torch.set_grad_enabled(train):
>             for x_seq, ei_seq, y in zip(seqs, adjs, tgts):
>                 x_dev  = [x.to(device) for x in x_seq]
>                 ei_dev = [e.to(device) for e in ei_seq]
>                 y_dev  = y.to(device)
>
>                 pred = model(x_dev, ei_dev)
>                 loss = F.mse_loss(pred, y_dev)
>
>                 if train:
>                     optimizer.zero_grad()
>                     loss.backward()
>                     torch.nn.utils.clip_grad_norm_(
>                         model.parameters(), 1.0
>                     )
>                     optimizer.step()
>                 total_loss += loss.item()
>         return total_loss / len(seqs)
>
>     print("\nTraining TemporalGAT-Vol...")
>     for epoch in range(1, 51):
>         tr_loss  = step(train_seqs, train_adjs, train_tgts, train=True)
>         val_loss = step(val_seqs, val_adjs, val_tgts, train=False)
>         if epoch % 10 == 0:
>             print(f"Epoch {epoch:3d} | Train MSE {tr_loss:.6f} | "
>                   f"Val MSE {val_loss:.6f}")
>
>     test_loss = step(test_seqs, test_adjs, test_tgts, train=False)
>     print(f"\nTest MSE: {test_loss:.6f}")
>
>
> if __name__ == "__main__":
>     run_volatility_pipeline()
> Use Case 3: Portfolio Optimization with GNN-Estimated Covariance
> Mean-variance optimization requires a covariance matrix. The traditional sample covariance matrix is noisy, especially in large universes, and suffers from the well-documented curse of dimensionality. GNNs offer a different path: learn the latent graph structure of asset correlations and use GNN-estimated node embeddings to produce a structured covariance estimate.
> Large-scale time-varying portfolio optimization using Graph Attention Networks handles high-dimensional data and accommodates customized layers for specific purposes, making them appealing for large-scale problems. The framework explicitly models time-varying asset correlations by updating the graph structure at each rebalancing period.
> Cost-aware regularization in GNN-based portfolio optimization reduces turnover by 20–40% without compromising performance - a critical property for production portfolios where transaction costs erode theoretical alpha.
> python
> """
> GNN-Based Portfolio Optimization
> Learns asset embeddings from graph structure, then optimizes weights
> Dependencies: torch, torch_geometric, numpy, scipy
> """
>
> import torch
> import torch.nn as nn
> import torch.nn.functional as F
> import numpy as np
> from scipy.optimize import minimize
> from torch_geometric.nn import GATConv
> from torch_geometric.utils import dense_to_sparse
>
>
> # ============================================================
> # 1. GNN Embedding Model
> # ============================================================
>
> class AssetEmbeddingGNN(nn.Module):
>     """
>     Encodes each asset into a latent embedding using GAT.
>     The embeddings are used to estimate a structured
>     covariance matrix for portfolio optimization.
>     """
>
>     def __init__(self,
>                  in_channels: int,
>                  embed_dim: int = 32,
>                  n_heads: int = 4,
>                  dropout: float = 0.1):
>         super().__init__()
>         self.gat1 = GATConv(in_channels, embed_dim,
>                             heads=n_heads, concat=True,
>                             dropout=dropout)
>         self.gat2 = GATConv(embed_dim * n_heads, embed_dim,
>                             heads=1, concat=False,
>                             dropout=dropout)
>         self.norm = nn.LayerNorm(embed_dim)
>         self.dropout = nn.Dropout(dropout)
>
>     def forward(self, x, edge_index):
>         h = F.elu(self.gat1(x, edge_index))
>         h = self.dropout(h)
>         h = self.gat2(h, edge_index)
>         h = self.norm(h)
>         return h   # (N, embed_dim)
>
>
> class ReturnPredictionHead(nn.Module):
>     """Predicts expected returns from asset embeddings."""
>
>     def __init__(self, embed_dim: int):
>         super().__init__()
>         self.fc = nn.Sequential(
>             nn.Linear(embed_dim, 16),
>             nn.ReLU(),
>             nn.Linear(16, 1)
>         )
>
>     def forward(self, embeddings):
>         return self.fc(embeddings).squeeze(-1)   # (N,)
>
>
> def gnn_covariance(embeddings: torch.Tensor,
>                    returns: torch.Tensor,
>                    alpha: float = 0.1) -> torch.Tensor:
>     """
>     Construct a structured covariance matrix from GNN embeddings.
>
>     The covariance is decomposed as:
>         Sigma = L * L^T + diag(epsilon)
>     where L is a low-rank factor matrix derived from embeddings.
>
>     This produces a positive-definite covariance estimate
>     that respects the graph structure learned by the GNN.
>
>     args:
>         embeddings: (N, D) — GNN node embeddings
>         returns:    (T, N) — historical returns for residual estimation
>         alpha:      regularization strength for diagonal component
>     """
>     N, D = embeddings.shape
>
>     # Low-rank component from embeddings
>     # Normalize so dot-product gives correlation-like structure
>     emb_norm = F.normalize(embeddings, dim=-1)           # (N, D)
>     L = emb_norm                                         # (N, D)
>     low_rank_cov = L @ L.T                               # (N, N)
>
>     # Residual variance from historical data
>     ret_t = torch.FloatTensor(returns)
>     residual_var = ret_t.var(dim=0)                      # (N,)
>     diag_cov = torch.diag(residual_var * alpha)          # (N, N)
>
>     # Combine: structured + residual diagonal
>     cov = low_rank_cov + diag_cov
>
>     # Ensure positive definiteness with small ridge
>     cov = cov + 1e-4 * torch.eye(N)
>
>     return cov
>
>
> # ============================================================
> # 2. Portfolio Optimization Layer
> # ============================================================
>
> def mean_variance_optimize(mu: np.ndarray,
>                             Sigma: np.ndarray,
>                             gamma: float = 1.0,
>                             lambda_tc: float = 0.001,
>                             w_prev: np.ndarray = None,
>                             long_only: bool = True
>                             ) -> np.ndarray:
>     """
>     Solve mean-variance optimization:
>         max  mu^T w - (gamma/2) w^T Sigma w - lambda_tc ||w - w_prev||_1
>         s.t. sum(w) = 1, w >= 0 (if long_only)
>
>     The L1 transaction cost term penalizes turnover,
>     equivalent to a proportional cost model.
>     """
>     N = len(mu)
>     if w_prev is None:
>         w_prev = np.ones(N) / N
>
>     def neg_utility(w):
>         ret_term = mu @ w
>         risk_term = 0.5 * gamma * (w @ Sigma @ w)
>         tc_term   = lambda_tc * np.abs(w - w_prev).sum()
>         return -(ret_term - risk_term - tc_term)
>
>     def neg_utility_grad(w):
>         ret_grad = mu
>         risk_grad = gamma * Sigma @ w
>         tc_grad   = lambda_tc * np.sign(w - w_prev)
>         return -(ret_grad - risk_grad - tc_grad)
>
>     constraints = [{"type": "eq", "fun": lambda w: w.sum() - 1.0}]
>     bounds = [(0.0, 1.0)] * N if long_only else [(-0.3, 0.3)] * N
>
>     result = minimize(
>         neg_utility,
>         x0=w_prev,
>         jac=neg_utility_grad,
>         method="SLSQP",
>         bounds=bounds,
>         constraints=constraints,
>         options={"maxiter": 500, "ftol": 1e-9}
>     )
>     return result.x if result.success else w_prev
> python
> # ============================================================
> # 3. End-to-End GNN Portfolio Pipeline
> # ============================================================
>
> class GNNPortfolioModel(nn.Module):
>     """
>     Joint model: GNN embedding + return prediction + covariance.
>     Trained with a portfolio-aware Sharpe ratio loss.
>     """
>
>     def __init__(self, in_channels: int, embed_dim: int = 32,
>                  n_heads: int = 4, dropout: float = 0.1):
>         super().__init__()
>         self.encoder = AssetEmbeddingGNN(
>             in_channels, embed_dim, n_heads, dropout
>         )
>         self.return_head = ReturnPredictionHead(embed_dim)
>
>     def forward(self, x, edge_index):
>         embeddings = self.encoder(x, edge_index)     # (N, embed_dim)
>         mu_pred    = self.return_head(embeddings)    # (N,)
>         return mu_pred, embeddings
>
>
> def portfolio_loss(mu_pred: torch.Tensor,
>                    mu_true: torch.Tensor,
>                    embeddings: torch.Tensor,
>                    returns_hist: torch.Tensor,
>                    gamma: float = 1.0) -> torch.Tensor:
>     """
>     Portfolio-aware loss combining:
>     1. Return prediction MSE
>     2. Negative Sharpe ratio of the implied portfolio
>
>     Gradient flows through both terms into the GNN.
>     """
>     N = mu_pred.shape[0]
>
>     # Term 1: Return prediction accuracy
>     mse_loss = F.mse_loss(mu_pred, mu_true)
>
>     # Term 2: Portfolio Sharpe (differentiable approximation)
>     # Compute soft-max weights (differentiable)
>     w = torch.softmax(mu_pred / (mu_pred.std() + 1e-8), dim=0)   # (N,)
>
>     # Portfolio returns on historical window
>     port_ret = returns_hist @ w                                   # (T,)
>     sharpe   = port_ret.mean() / (port_ret.std() + 1e-8)
>
>     # Combined loss: minimize MSE, maximize Sharpe
>     return mse_loss - 0.1 * sharpe
>
>
> def run_portfolio_pipeline():
>     """
>     End-to-end GNN portfolio optimization demo.
>     Synthetic data: replace with real price data in production.
>     """
>     device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
>
>     # Synthetic setup
>     N  = 20     # number of assets
>     T  = 252    # days of history
>     F  = 8      # features per asset
>     rng = np.random.RandomState(0)
>
>     # Random features (in production: returns, vol, RSI, etc.)
>     features_np = rng.randn(T, N, F).astype(np.float32)
>     returns_np  = (rng.randn(T, N) * 0.01).astype(np.float32)
>
>     # Correlation-based adjacency
>     corr = np.corrcoef(returns_np.T)
>     adj  = (np.abs(corr) > 0.2).astype(np.float32)
>     np.fill_diagonal(adj, 1.0)
>     edge_index, _ = dense_to_sparse(torch.FloatTensor(adj))
>     edge_index = edge_index.to(device)
>
>     # Model
>     model = GNNPortfolioModel(
>         in_channels=F, embed_dim=32, n_heads=4, dropout=0.1
>     ).to(device)
>
>     optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
>
>     # Training: predict next-day returns using current graph
>     LOOKBACK = 60
>     weights_history = []
>     w_prev = np.ones(N) / N
>
>     print("Training GNN Portfolio Model...")
>     for epoch in range(1, 51):
>         total_loss = 0.0
>         model.train()
>
>         for t in range(LOOKBACK, T - 1):
>             x_t      = torch.FloatTensor(features_np[t]).to(device)  # (N, F)
>             ret_hist = torch.FloatTensor(
>                 returns_np[t - LOOKBACK : t]
>             ).to(device)                                               # (LB, N)
>             ret_next = torch.FloatTensor(returns_np[t + 1]).to(device)  # (N,)
>
>             mu_pred, embeddings = model(x_t, edge_index)
>             loss = portfolio_loss(mu_pred, ret_next, embeddings,
>                                   ret_hist, gamma=1.0)
>
>             optimizer.zero_grad()
>             loss.backward()
>             torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
>             optimizer.step()
>             total_loss += loss.item()
>
>         if epoch % 10 == 0:
>             print(f"Epoch {epoch:3d} | Loss {total_loss / (T - LOOKBACK - 1):.4f}")
>
>     # --- Walk-forward backtest ---
>     print("\nRunning walk-forward portfolio backtest...")
>     model.eval()
>     portfolio_returns = []
>
>     with torch.no_grad():
>         for t in range(LOOKBACK, T - 1):
>             x_t  = torch.FloatTensor(features_np[t]).to(device)
>             ret_hist = returns_np[t - LOOKBACK : t]
>
>             mu_pred, embeddings = model(x_t, edge_index)
>             mu_np    = mu_pred.cpu().numpy()
>             emb_tens = embeddings
>             cov_t    = gnn_covariance(emb_tens, ret_hist).numpy()
>
>             # Portfolio weights
>             w = mean_variance_optimize(
>                 mu_np, cov_t, gamma=1.0,
>                 lambda_tc=0.001, w_prev=w_prev
>             )
>             w_prev = w
>
>             # Realized portfolio return
>             realized_ret = returns_np[t + 1] @ w
>             portfolio_returns.append(realized_ret)
>
>     port_ret   = np.array(portfolio_returns)
>     equal_ret  = returns_np[LOOKBACK + 1 :].mean(axis=1)
>
>     print(f"\nGNN Portfolio Sharpe:     "
>           f"{port_ret.mean() / port_ret.std() * np.sqrt(252):.3f}")
>     print(f"Equal-Weight Sharpe:      "
>           f"{equal_ret.mean() / equal_ret.std() * np.sqrt(252):.3f}")
>     print(f"GNN Portfolio Annual Ret: "
>           f"{port_ret.mean() * 252:.2%}")
>     print(f"GNN Portfolio Annual Vol: "
>           f"{port_ret.std() * np.sqrt(252):.2%}")
>
>
> if __name__ == "__main__":
>     run_portfolio_pipeline()
> Use Case 4: Transaction Fraud Detection with Temporal Graph Networks
> Financial transactions naturally form dynamic graphs: edges (transactions) arrive continuously, and node connectivity evolves over time. Real-time dynamic graph learning with temporal attention captures fine-grained temporal dynamics and evolving topological patterns that static graph models - which assume a fixed, unchanging graph - fundamentally cannot model for fraud detection.
> GNNs are exceptionally adept at capturing complex relational patterns and dynamics within financial networks, significantly outperforming traditional fraud detection methods. GCN-based, GAT-based, and temporal GNN approaches have all demonstrated superior fraud detection compared to non-graph baselines.
> The fraud detection graph is built as follows: nodes are accounts or entities, directed edges are transactions with features (amount, timestamp, transaction type, merchant category), and the task is node classification - is this account fraudulent? - or edge classification - is this transaction fraudulent?
> python
> """
> Financial Fraud Detection with Temporal Graph Network
> Simplified TGN implementation for transaction networks
> Dependencies: torch, torch_geometric, numpy, pandas
> """
>
> import torch
> import torch.nn as nn
> import torch.nn.functional as F
> import numpy as np
> from torch_geometric.nn import GATConv, SAGEConv
> from torch_geometric.data import Data
>
>
> # ============================================================
> # 1. Graph Construction from Transaction Data
> # ============================================================
>
> def build_transaction_graph(transactions: list[dict],
>                              node_feature_dim: int = 8
>                              ) -> tuple[Data, dict]:
>     """
>     Build a transaction graph from a list of transaction records.
>
>     Each transaction: {
>         'src': source account id,
>         'dst': destination account id,
>         'amount': float,
>         'timestamp': int (unix seconds),
>         'tx_type': int (0=wire, 1=ACH, 2=card, ...),
>         'label': int (0=legit, 1=fraud)  — for training only
>     }
>
>     Returns PyG Data object and node-to-index mapping.
>     """
>     # Collect unique nodes
>     nodes = sorted(set(
>         [t["src"] for t in transactions] +
>         [t["dst"] for t in transactions]
>     ))
>     node_to_idx = {n: i for i, n in enumerate(nodes)}
>     N = len(nodes)
>
>     # Edge list
>     edge_src, edge_dst, edge_feats, edge_labels = [], [], [], []
>     for tx in transactions:
>         i = node_to_idx[tx["src"]]
>         j = node_to_idx[tx["dst"]]
>         edge_src.append(i)
>         edge_dst.append(j)
>
>         # Edge features: [log(amount), tx_type_onehot...,
>         #                 normalized_timestamp]
>         log_amt = np.log1p(tx["amount"])
>         tx_type = [0] * 4
>         if tx["tx_type"] < 4:
>             tx_type[tx["tx_type"]] = 1
>         t_norm  = (tx["timestamp"] % 86400) / 86400   # time-of-day
>         edge_feats.append([log_amt] + tx_type + [t_norm])
>         edge_labels.append(tx.get("label", 0))
>
>     edge_index = torch.LongTensor([edge_src, edge_dst])   # (2, E)
>     edge_attr  = torch.FloatTensor(edge_feats)            # (E, 6)
>     edge_y     = torch.LongTensor(edge_labels)            # (E,)
>
>     # Node features: aggregate over incident transactions
>     # (in-degree, out-degree, mean amount sent, mean amount received,
>     #  std amount sent, std amount received, tx count, recency)
>     node_feats = np.zeros((N, node_feature_dim), dtype=np.float32)
>     for tx in transactions:
>         i = node_to_idx[tx["src"]]
>         j = node_to_idx[tx["dst"]]
>         log_amt = np.log1p(tx["amount"])
>         # out-degree accumulation for source
>         node_feats[i, 0] += 1
>         node_feats[i, 2] += log_amt
>         # in-degree accumulation for destination
>         node_feats[j, 1] += 1
>         node_feats[j, 3] += log_amt
>
>     # Compute means
>     out_deg = node_feats[:, 0:1] + 1e-8
>     in_deg  = node_feats[:, 1:2] + 1e-8
>     node_feats[:, 2] /= out_deg[:, 0]
>     node_feats[:, 3] /= in_deg[:, 0]
>
>     x = torch.FloatTensor(node_feats)
>
>     data = Data(x=x, edge_index=edge_index,
>                 edge_attr=edge_attr, edge_y=edge_y)
>     return data, node_to_idx
>
>
> # ============================================================
> # 2. Fraud Detection GNN (Edge Classification)
> # ============================================================
>
> class FraudGNN(nn.Module):
>     """
>     Graph-based fraud detection model.
>
>     Architecture:
>     - GraphSAGE layers aggregate neighborhood features
>       (SAGE is preferred over GCN for inductive tasks where
>        new nodes/transactions arrive at inference time)
>     - Edge classifier combines source, destination, and
>       edge feature embeddings to predict fraud probability
>
>     Based on architecture patterns from published fraud
>     detection GNN literature (Cheng et al., 2025;
>     Frontiers of Computer Science).
>     """
>
>     def __init__(self,
>                  node_in_channels: int,
>                  edge_in_channels: int,
>                  hidden_channels: int = 64,
>                  dropout: float = 0.3):
>         super().__init__()
>
>         # Node encoder: 2-layer GraphSAGE
>         self.sage1 = SAGEConv(node_in_channels, hidden_channels)
>         self.sage2 = SAGEConv(hidden_channels, hidden_channels)
>         self.node_norm1 = nn.LayerNorm(hidden_channels)
>         self.node_norm2 = nn.LayerNorm(hidden_channels)
>
>         # Edge classifier: concat(h_src, h_dst, edge_feat)
>         edge_clf_in = hidden_channels * 2 + edge_in_channels
>         self.edge_clf = nn.Sequential(
>             nn.Linear(edge_clf_in, 64),
>             nn.ReLU(),
>             nn.Dropout(dropout),
>             nn.Linear(64, 32),
>             nn.ReLU(),
>             nn.Dropout(dropout),
>             nn.Linear(32, 2)   # binary: legit vs fraud
>         )
>         self.dropout = nn.Dropout(dropout)
>
>     def encode_nodes(self, x, edge_index):
>         """Produce node embeddings via GraphSAGE."""
>         h = F.relu(self.sage1(x, edge_index))
>         h = self.node_norm1(h)
>         h = self.dropout(h)
>         h = F.relu(self.sage2(h, edge_index))
>         h = self.node_norm2(h)
>         return h   # (N, hidden_channels)
>
>     def classify_edges(self, h_nodes, edge_index, edge_attr):
>         """
>         Predict fraud probability for each edge.
>         Combines source node embedding, destination node embedding,
>         and edge features.
>         """
>         src_nodes = edge_index[0]   # (E,)
>         dst_nodes = edge_index[1]   # (E,)
>
>         h_src  = h_nodes[src_nodes]    # (E, hidden)
>         h_dst  = h_nodes[dst_nodes]    # (E, hidden)
>
>         edge_emb = torch.cat([h_src, h_dst, edge_attr], dim=-1)   # (E, 2H+F)
>         logits   = self.edge_clf(edge_emb)                         # (E, 2)
>         return logits
>
>     def forward(self, x, edge_index, edge_attr):
>         h_nodes = self.encode_nodes(x, edge_index)
>         logits  = self.classify_edges(h_nodes, edge_index, edge_attr)
>         return logits
>
> python
> # ============================================================
> # 3. Fraud-Aware Loss (Class Imbalance Handling)
> # ============================================================
>
> def focal_loss(logits: torch.Tensor,
>                labels: torch.Tensor,
>                gamma: float = 2.0,
>                alpha: float = 0.25) -> torch.Tensor:
>     """
>     Focal loss for imbalanced fraud detection.
>     Down-weights easy (mostly legit) examples so the model
>     focuses on hard fraud cases.
>
>     Fraud prevalence in real transaction data is typically
>     0.1%–2%, making standard cross-entropy sub-optimal.
>
>     Lin et al. (2017): Focal Loss for Dense Object Detection.
>     """
>     probs   = torch.softmax(logits, dim=-1)
>     pt      = probs[range(len(labels)), labels]
>     ce_loss = F.cross_entropy(logits, labels, reduction="none")
>     fl      = alpha * (1 - pt) ** gamma * ce_loss
>     return fl.mean()
>
>
> # ============================================================
> # 4. Synthetic Transaction Data Generator
> # ============================================================
>
> def generate_synthetic_transactions(n_accounts: int = 100,
>                                     n_transactions: int = 2000,
>                                     fraud_rate: float = 0.05,
>                                     seed: int = 42) -> list[dict]:
>     """
>     Generate synthetic transaction data with ring-shaped
>     fraud patterns (a common money-laundering structure
>     that is invisible to per-transaction models but
>     visible to graph models).
>     """
>     rng = np.random.RandomState(seed)
>     txs = []
>
>     # Identify a fraud ring: 5–10 accounts that cycle funds
>     ring_size = rng.randint(5, 11)
>     fraud_accounts = list(rng.choice(n_accounts, ring_size,
>                                      replace=False))
>
>     for i in range(n_transactions):
>         is_fraud = rng.random() < fraud_rate
>
>         if is_fraud and len(fraud_accounts) >= 2:
>             # Fraud: transaction within the ring
>             src = int(rng.choice(fraud_accounts))
>             dst = int(rng.choice([a for a in fraud_accounts
>                                   if a != src]))
>             amount = float(rng.uniform(500, 9999))   # structuring amount
>         else:
>             src = int(rng.randint(0, n_accounts))
>             dst = int(rng.randint(0, n_accounts))
>             while dst == src:
>                 dst = int(rng.randint(0, n_accounts))
>             amount = float(rng.lognormal(mean=5.0, sigma=1.5))
>
>         txs.append({
>             "src":       src,
>             "dst":       dst,
>             "amount":    amount,
>             "timestamp": int(1_700_000_000 + i * 300),   # 5-min intervals
>             "tx_type":   int(rng.randint(0, 4)),
>             "label":     int(is_fraud)
>         })
>
>     return txs
>
>
> def run_fraud_detection_pipeline():
>     """
>     End-to-end fraud detection demo with ring pattern.
>     """
>     device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
>
>     # Generate data
>     transactions = generate_synthetic_transactions(
>         n_accounts=200, n_transactions=3000, fraud_rate=0.05
>     )
>
>     print(f"Total transactions: {len(transactions)}")
>     print(f"Fraud transactions: {sum(t['label'] for t in transactions)}")
>     print(f"Fraud rate: "
>           f"{sum(t['label'] for t in transactions) / len(transactions):.2%}")
>
>     # Build graph
>     data, _ = build_transaction_graph(transactions, node_feature_dim=8)
>
>     # Train/test split on edges (transactions)
>     n_edges   = data.edge_index.shape[1]
>     split     = int(0.8 * n_edges)
>     train_mask = torch.zeros(n_edges, dtype=torch.bool)
>     test_mask  = torch.zeros(n_edges, dtype=torch.bool)
>     train_mask[:split]  = True
>     test_mask[split:]   = True
>
>     # Model
>     model = FraudGNN(
>         node_in_channels=8,
>         edge_in_channels=6,
>         hidden_channels=64,
>         dropout=0.3
>     ).to(device)
>
>     optimizer = torch.optim.Adam(model.parameters(), lr=1e-3,
>                                  weight_decay=1e-4)
>
>     x          = data.x.to(device)
>     edge_index = data.edge_index.to(device)
>     edge_attr  = data.edge_attr.to(device)
>     edge_y     = data.edge_y.to(device)
>
>     print("\nTraining FraudGNN...")
>     for epoch in range(1, 101):
>         model.train()
>         optimizer.zero_grad()
>
>         logits = model(x, edge_index, edge_attr)   # (E, 2)
>         loss   = focal_loss(
>             logits[train_mask], edge_y[train_mask],
>             gamma=2.0, alpha=0.75
>         )
>         loss.backward()
>         torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
>         optimizer.step()
>
>         if epoch % 20 == 0:
>             model.eval()
>             with torch.no_grad():
>                 test_logits = logits[test_mask]
>                 test_labels = edge_y[test_mask]
>                 preds = test_logits.argmax(dim=-1)
>
>                 tp = ((preds == 1) & (test_labels == 1)).sum().item()
>                 fp = ((preds == 1) & (test_labels == 0)).sum().item()
>                 fn = ((preds == 0) & (test_labels == 1)).sum().item()
>
>                 precision = tp / (tp + fp + 1e-8)
>                 recall    = tp / (tp + fn + 1e-8)
>                 f1        = (2 * precision * recall
>                              / (precision + recall + 1e-8))
>
>                 print(f"Epoch {epoch:3d} | Loss {loss.item():.4f} | "
>                       f"Precision {precision:.3f} | "
>                       f"Recall {recall:.3f} | F1 {f1:.3f}")
>
>
> if __name__ == "__main__":
>     run_fraud_detection_pipeline()
> Use Case 5: Systemic Risk and Interbank Contagion
> GNN-based systemic risk and interbank contagion analysis extends temporal GNN lines to U.S. regulatory surveillance. Research applying ST-GAT to 8,103 institutions over 58 quarters incorporates macro-conditioned edge weights, validated explainability modules, and grounding in U.S. regulatory filings. Temporal graph learning for default prediction integrating macroeconomic trends has reported 88.3% AUC.
> The graph for systemic risk is a financial network where nodes are banks or financial institutions, edges represent bilateral exposures (interbank loans, derivative counterparty exposure, common asset holdings), and the task is predicting which nodes will experience distress in future periods given the current state of the network and macroeconomic inputs.
> python
> """
> Systemic Risk GNN: Interbank Contagion Monitoring
> Simplified ST-GAT for financial network surveillance
> Dependencies: torch, torch_geometric, numpy
> """
>
> import torch
> import torch.nn as nn
> import torch.nn.functional as F
> import numpy as np
> from torch_geometric.nn import GATConv
> from torch_geometric.utils import dense_to_sparse
>
>
> class SystemicRiskGAT(nn.Module):
>     """
>     Spatial-Temporal GAT for interbank contagion detection.
>
>     Architecture inspired by Temporal Attentive Graph Networks
>     for financial surveillance (Zhang et al., 2026):
>     - GAT encodes current network topology and node features
>     - GRU captures temporal dynamics of institution stress
>     - Macro features modulate edge weights
>     - Node-level binary classification: distress in next period
>
>     Node features: capital ratio, leverage ratio, NPL ratio,
>                    liquidity coverage ratio, interbank exposure,
>                    return on assets, CDS spread proxy
>     Edge features: bilateral exposure as fraction of Tier 1 capital
>     Macro inputs:  VIX, credit spread, yield curve slope,
>                    policy rate
>     """
>
>     def __init__(self,
>                  node_in: int = 7,
>                  edge_in: int = 1,
>                  macro_in: int = 4,
>                  gat_hidden: int = 32,
>                  gru_hidden: int = 64,
>                  n_heads: int = 4,
>                  dropout: float = 0.2):
>         super().__init__()
>
>         # Macro conditioning: projects macro features into
>         # a scalar gate applied to edge weights
>         self.macro_gate = nn.Sequential(
>             nn.Linear(macro_in, 16),
>             nn.ReLU(),
>             nn.Linear(16, 1),
>             nn.Sigmoid()
>         )
>
>         # Spatial: GAT with macro-conditioned edge attention
>         self.gat1 = GATConv(
>             in_channels=node_in,
>             out_channels=gat_hidden,
>             heads=n_heads,
>             concat=True,
>             edge_dim=edge_in,
>             dropout=dropout
>         )
>         self.gat2 = GATConv(
>             in_channels=gat_hidden * n_heads,
>             out_channels=gat_hidden,
>             heads=1,
>             concat=False,
>             edge_dim=edge_in,
>             dropout=dropout
>         )
>
>         # Temporal: GRU over time-series of GAT embeddings
>         self.gru = nn.GRU(
>             input_size=gat_hidden,
>             hidden_size=gru_hidden,
>             num_layers=2,
>             batch_first=True,
>             dropout=dropout
>         )
>
>         # Classifier: node-level distress prediction
>         self.classifier = nn.Sequential(
>             nn.Linear(gru_hidden, 32),
>             nn.ReLU(),
>             nn.Dropout(dropout),
>             nn.Linear(32, 2)   # 0=healthy, 1=distressed
>         )
>
>         self.norm = nn.LayerNorm(gat_hidden)
>         self.dropout = nn.Dropout(dropout)
>
>     def forward(self,
>                 x_seq: list,           # list of T: (N, node_in)
>                 edge_index_seq: list,  # list of T: (2, E)
>                 edge_attr_seq: list,   # list of T: (E, edge_in)
>                 macro_seq: list        # list of T: (macro_in,)
>                 ) -> torch.Tensor:
>         """
>         Returns: (N, 2) — distress probability logits at final step.
>         """
>         T = len(x_seq)
>         gat_embeds = []
>
>         for t in range(T):
>             x_t     = x_seq[t]
>             ei_t    = edge_index_seq[t]
>             ea_t    = edge_attr_seq[t]
>             macro_t = macro_seq[t].unsqueeze(0)   # (1, macro_in)
>
>             # Macro gate: scale edge features by macro regime
>             gate = self.macro_gate(macro_t)   # (1, 1) in [0, 1]
>             ea_scaled = ea_t * gate           # (E, edge_in)
>
>             h = F.elu(self.gat1(x_t, ei_t, ea_scaled))
>             h = self.dropout(h)
>             h = F.elu(self.gat2(h, ei_t, ea_scaled))
>             h = self.norm(h)                  # (N, gat_hidden)
>             gat_embeds.append(h)
>
>         # (N, T, gat_hidden) → GRU
>         stacked  = torch.stack(gat_embeds, dim=1)   # (N, T, H)
>         gru_out, _ = self.gru(stacked)               # (N, T, gru_h)
>         last     = gru_out[:, -1, :]                 # (N, gru_h)
>
>         logits = self.classifier(last)               # (N, 2)
>         return logits
>
>
> def generate_interbank_network(N: int = 30,
>                                T: int = 40,
>                                distress_rate: float = 0.1,
>                                seed: int = 0
>                                ) -> dict:
>     """
>     Generate synthetic interbank network data.
>     In production: replace with
>     - FR Y-9C / Call Report data (US banks)
>     - EBA stress test disclosures (EU banks)
>     - BIS bilateral banking statistics
>     """
>     rng = np.random.RandomState(seed)
>
>     # Static network backbone: random sparse directed graph
>     adj_base = (rng.random((N, N)) < 0.2).astype(float)
>     np.fill_diagonal(adj_base, 0)
>
>     data = {
>         "node_features": [],    # list of T arrays (N, 7)
>         "edge_attrs":    [],    # list of T arrays (E, 1)
>         "macro_features": [],   # list of T arrays (4,)
>         "adjacency":     [],    # list of T arrays (N, N)
>         "labels":        []     # list of T arrays (N,) binary
>     }
>
>     distressed = set()
>
>     for t in range(T):
>         # Node features: financial ratios (synthetic)
>         node_feat = rng.uniform(0.0, 1.0, (N, 7)).astype(np.float32)
>         # Distressed nodes have lower capital ratio
>         for d in distressed:
>             node_feat[d, 0] *= 0.3   # weaker capital ratio
>
>         # Dynamic adjacency (exposure changes over time)
>         noise = (rng.random((N, N)) < 0.05).astype(float)
>         adj_t = np.clip(adj_base + noise - noise.T, 0, 1)
>         np.fill_diagonal(adj_t, 0)
>
>         # Edge weights: normalized bilateral exposures
>         edge_wts = (adj_t * rng.uniform(0.1, 1.0, (N, N))).astype(np.float32)
>
>         # Macro features: VIX, credit spread, yield slope, policy rate
>         macro = rng.uniform(0.0, 1.0, 4).astype(np.float32)
>         if t > T // 2:
>             macro[0] *= 2.0   # simulate vol spike in second half
>
>         # Labels: which nodes become distressed next period
>         if t < T - 1:
>             n_distress  = max(1, int(distress_rate * N))
>             new_distress = set(
>                 rng.choice(N, n_distress, replace=False).tolist()
>             )
>             # Contagion: neighbors of distressed also at risk
>             for d in distressed:
>                 neighbors = np.where(adj_t[d] > 0)[0]
>                 for nb in neighbors:
>                     if rng.random() < 0.3:
>                         new_distress.add(int(nb))
>             distressed = new_distress
>         else:
>             distressed = set()
>
>         labels = np.zeros(N, dtype=np.int64)
>         for d in distressed:
>             labels[d] = 1
>
>         data["node_features"].append(node_feat)
>         data["adjacency"].append(adj_t)
>         data["edge_attrs"].append(edge_wts)
>         data["macro_features"].append(macro)
>         data["labels"].append(labels)
>
>     return data
> python
> def run_systemic_risk_pipeline():
>     """End-to-end systemic risk GNN demo."""
>     device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
>
>     N, T = 30, 40
>     SEQ_LEN = 8   # look-back window
>
>     net_data = generate_interbank_network(N=N, T=T, distress_rate=0.1)
>
>     def to_tensors(t):
>         adj   = net_data["adjacency"][t]
>         ew    = net_data["edge_attrs"][t]
>         nf    = net_data["node_features"][t]
>         macro = net_data["macro_features"][t]
>
>         ei, _  = dense_to_sparse(torch.FloatTensor(adj))
>         src, dst = ei[0], ei[1]
>         ea     = torch.FloatTensor(ew[src.numpy(), dst.numpy()]).unsqueeze(1)
>
>         return (
>             torch.FloatTensor(nf).to(device),
>             ei.to(device),
>             ea.to(device),
>             torch.FloatTensor(macro).to(device)
>         )
>
>     model = SystemicRiskGAT(
>         node_in=7, edge_in=1, macro_in=4,
>         gat_hidden=32, gru_hidden=64, n_heads=4, dropout=0.2
>     ).to(device)
>
>     optimizer = torch.optim.Adam(model.parameters(), lr=5e-4)
>
>     split = int(0.8 * (T - SEQ_LEN))
>     print(f"Train snapshots: {split}, Test: {T - SEQ_LEN - split}")
>
>     print("\nTraining SystemicRiskGAT...")
>     for epoch in range(1, 101):
>         model.train()
>         total_loss = 0.0
>
>         for t in range(SEQ_LEN, SEQ_LEN + split):
>             x_seq    = [to_tensors(s)[0] for s in range(t - SEQ_LEN, t)]
>             ei_seq   = [to_tensors(s)[1] for s in range(t - SEQ_LEN, t)]
>             ea_seq   = [to_tensors(s)[2] for s in range(t - SEQ_LEN, t)]
>             mac_seq  = [to_tensors(s)[3] for s in range(t - SEQ_LEN, t)]
>
>             labels = torch.LongTensor(
>                 net_data["labels"][t]
>             ).to(device)
>
>             logits = model(x_seq, ei_seq, ea_seq, mac_seq)
>             loss   = F.cross_entropy(logits, labels,
>                                      weight=torch.tensor([1.0, 5.0],
>                                                          device=device))
>             optimizer.zero_grad()
>             loss.backward()
>             torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
>             optimizer.step()
>             total_loss += loss.item()
>
>         if epoch % 25 == 0:
>             # Test evaluation
>             model.eval()
>             test_preds, test_labels_all = [], []
>             with torch.no_grad():
>                 for t in range(SEQ_LEN + split, T):
>                     x_seq   = [to_tensors(s)[0] for s in range(t - SEQ_LEN, t)]
>                     ei_seq  = [to_tensors(s)[1] for s in range(t - SEQ_LEN, t)]
>                     ea_seq  = [to_tensors(s)[2] for s in range(t - SEQ_LEN, t)]
>                     mac_seq = [to_tensors(s)[3] for s in range(t - SEQ_LEN, t)]
>                     labels  = net_data["labels"][t]
>
>                     logits = model(x_seq, ei_seq, ea_seq, mac_seq)
>                     preds  = logits.argmax(dim=-1).cpu().numpy()
>                     test_preds.extend(preds.tolist())
>                     test_labels_all.extend(labels.tolist())
>
>             tp = sum(p == 1 and l == 1
>                      for p, l in zip(test_preds, test_labels_all))
>             fp = sum(p == 1 and l == 0
>                      for p, l in zip(test_preds, test_labels_all))
>             fn = sum(p == 0 and l == 1
>                      for p, l in zip(test_preds, test_labels_all))
>
>             prec = tp / (tp + fp + 1e-8)
>             rec  = tp / (tp + fn + 1e-8)
>             f1   = 2 * prec * rec / (prec + rec + 1e-8)
>
>             print(f"Epoch {epoch:3d} | Train Loss "
>                   f"{total_loss / split:.4f} | "
>                   f"Test Precision {prec:.3f} | "
>                   f"Recall {rec:.3f} | F1 {f1:.3f}")
>
>
> if __name__ == "__main__":
>     run_systemic_risk_pipeline()
> The Hard Truth: Where Graph Engineering Breaks Down
> Graph construction is a source of alpha - and a source of look-ahead bias. Every edge in your financial graph encodes information. If that information was not available at the time of trading, you have introduced look-ahead bias at the graph structure level, which is harder to detect than look-ahead in feature computation. Correlation-based adjacency computed over the full sample is invalid. Supply chain links must use the relationships that existed at the time of the trade, not current ones. Sector assignments that changed after restructurings must use point-in-time GICS classifications.
> Oversmoothing in deep GNN architectures. GNN architectures should control oversmoothing through edge dropout, attention, or regime-gated message passing when correlation graphs become dense. When every stock is connected to every other stock through a dense correlation matrix, multiple rounds of message passing wash out the individual node features and produce uniform embeddings. In practice: keep graphs sparse (threshold correlations aggressively), use attention mechanisms that can learn to zero out uninformative edges, and limit GNN depth to 2–3 layers for financial applications.
> Distribution shift across market regimes. A GNN trained on a low-volatility 2019–2021 period will have learned a correlation structure that breaks down during the 2022 rate shock or a 2008-style liquidity crisis. The graph structure itself changes across regimes. Practical mitigations: train on data spanning multiple market regimes, use dynamic adjacency that is recomputed from recent data at inference time, and monitor the statistics of learned edge attention weights as a regime change indicator.
> Computational cost for real-time applications. Training a GNN on a 500-stock universe with 252 days of snapshots is computationally modest. Inferencing at tick frequency across a 5000-name universe with dynamic graph recomputation is not. The practical solution adopted in production is batching: rebuild the graph daily or weekly, run GNN inference on the updated graph, and cache embeddings for intraday use. Full real-time graph recomputation is reserved for fraud detection applications where latency is less constrained than HFT.
> Data requirements for supply chain graphs. Building a production-quality supply chain graph requires point-in-time supply chain data (FactSet Revere, Bloomberg SPLC, or manual extraction from SEC filings), which is expensive and requires significant data engineering. The academic literature typically uses simplified proxies. Production deployments require data infrastructure investment before the model investment.
> The Implementation Roadmap for Quant Teams
> Week 1-2: Foundation. Install PyTorch Geometric. Build your first correlation-based adjacency matrix from your existing equity universe. Run the StockGAT code from Section 3 on your factor feature set. Establish baseline IC and RankIC from your existing linear factor models. Measure the gap.
> Week 3-4: Graph Quality. Experiment with different adjacency construction methods: correlation threshold, sector membership, supply chain edges (if you have access). The graph structure is the primary determinant of GNN quality - more expressive architecture with a poor graph will underperform a simpler architecture with a well-constructed graph. Implement strict look-ahead controls: rolling adjacency computed only from data available before the prediction date.
> Week 5-6: Temporal Extension. Add the GRU layer to your GCN/GAT to capture temporal dynamics. Implement the dynamic adjacency pipeline: the graph structure updates at each rebalancing date. Measure whether dynamic adjacency improves over static. For most equity applications, it does - particularly around earnings seasons when sector correlations shift dramatically.
> Week 7: Portfolio Integration. Connect GNN return predictions to your portfolio optimizer. Implement the GNN covariance estimation approach from Section 5. Run a walk-forward backtest with realistic transaction costs. Measure Sharpe ratio, information ratio, and turnover. Compare to your existing factor model.
> Week 8 and beyond: Production Hardening. Implement model monitoring: track the distribution of predicted returns, attention weight statistics (a proxy for regime change), and IC decay over time. Retrain on a rolling window. Build a regime detection module that flags when the current market correlation structure diverges significantly from the training distribution - this is when the GNN is most likely to fail.
> Note : i wanted to reach larger audience, QT appreciated, if done i will personally dm you to get started your journey in quants.

- 图片：[img1](https://pbs.twimg.com/media/HOOE6y5bkAAtAMF?format=jpg&name=large)

#### x-2029562218048541087

**Nano Banana 2：手绘户型图 → 4K 3D 室内渲染**

- 作者：el.cine (@EHuanglu) · 发帖 2026-03-05 · [原帖](https://x.com/EHuanglu/status/2029562218048541087)
- 来源：🔖 收藏 · 拉取 2026-10-27
- 类型：教程
- **总结**：图像模型应用教程：在 OpenArt 里用 Nano Banana 2，把手绘户型图转成尺寸准确的 4K 3D 渲染；再在图上标出房间和相机角度，生成各房间的写实照片；还能一键换家具。thread 里给出分步操作和 prompt。和 agent 主题无关，属于 AI 应用案例。
- **原文**：

> AI ending interior design
>
> Nano banana 2 now can turn sketch floor plan into 4K 3D rendering with accurate dimension, take photos for each room, and 1-click furniture change
>
> used to cost $100k and months.. now cents and mins
>
> step by step tutorial on OpenArt:
>
> [2] nano banana 2's understanding of dimension and 3D space is so crazy now, its like a personal designer in your pocket
>
> step 1:
>
> go to http://openart.ai -> edit image -> select nano banana 2 -> upload floor plan -> type prompt (reply here if you want my prompt)
>
> [3] step 2: take realistic photo - living room
>
> highlight the room that you want to take photo, draw a camera to let AI know the camera angle, upload it as ref image and use prompt below
>
> prompt:
>
> realistic interior render of a modern wooden cabin living room, viewed from the camera
>
> [4] step 3: take realistic photo - kitchen
>
> prompt:
>
> Ultra-realistic interior render of a small modern wooden cabin kitchen, viewed from kitchen entry area, looking towards the sink side as indicated in the floor plan.
>
> The layout and furniture placement must match the floor plan
>
> [5] step 4: change furnitures
>
> upload both the living room photo and your sofa as ref image and prompt 'change the sofa'
>
> you can also highlight certain area to make precise edit
>
> [6] step 5: make video
>
> use the living room and kitchen photo as start and end frame to generate video
>
> [7] if you found this inspiring,
>
> follow @EHuanglu to survive AI
>
> like & repost so more people see this 👇

- 含视频（未转写）

### 📂 其他

#### x-2082413202353406091

**The Code newsletter 推广**

- 作者：The Code Newsletter (@CodeNewsletter) · 发帖 2026-07-29 · [原帖](https://x.com/CodeNewsletter/status/2082413202353406091)
- 来源：🔖 收藏 · 拉取 2026-10-27
- 类型：推广
- **总结**：一条 newsletter 订阅推广，说 2026 年是 AI 差距无法弥补的一年，号召订阅以「编码快 5 倍」。没有技术内容，可以忽略。
- **原文**：

> Your GitHub stars won't save you if you're behind on AI.
>
> 2026 is the year this gap becomes impossible to close. 
>
> Here's everything you need to master AI and ship code 5X faster.
>
> Join The Code newsletter and get the access

- 链接卡片：[Join 300k+ Devs](https://codenewsletter.ai/subscribe?utm_source=twitter_ads_flal_1_cc_tutorials)
- 图片：[img1](https://pbs.twimg.com/media/HG52YoMaEAAL1Oa?format=jpg&name=large)

#### x-2029598376321585332

**NotebookLM 深度解析推荐**

- 作者：韦小宝 (@nicebabycat) · 发帖 2026-03-05 · [原帖](https://x.com/nicebabycat/status/2029598376321585332)
- 来源：🔖 收藏 · 拉取 2026-10-27
- 类型：文章推荐
- **总结**：推荐一篇 NotebookLM 深度解析长文：自动出 PPT、生成播客、思维导图、测验等用法，文末附可直接用的 prompt。帖子本身只有推荐语和个人经历，没有展开内容，需要看原文。
- **原文**：

> 这篇NotebookLM深度解析，强烈推荐
>
> 这玩意儿才是真·3分钟自动出PPT、生成播客解说、通勤听资料、做思维导图、测验……商务人看完直接跪了。
>
> 文章超长但值回票价，Prompt全放文末可抄作业。
> 我前几天差点因为AI胡说八道在会上翻车，结果刷到@boniusex彻底救命！


#### x-2029459404710658307

**Scrapling：绕过反爬的开源抓取库**

- 作者：董币哥 (@NextBullReady) · 发帖 2026-03-05 · [原帖](https://x.com/NextBullReady/status/2029459404710658307)
- 来源：🔖 收藏 · 拉取 2026-10-27
- 类型：工具推荐
- **总结**：推荐开源抓取库 Scrapling（D4Vinci/Scrapling），号称能绕过 Cloudflare 等反机器人检测，比 BeautifulSoup 快 774 倍，不用维护选择器。帖子把它和 OpenClaw 绑在一起宣传。注意：绕过网站反爬可能违反目标网站条款。
- **原文**：

> OpenClaw 现在可以抓取任何网站而不被屏蔽——零机器人检测，原生绕过 Cloudflare，比 BeautifulSoup 快 774 倍。
>
> 无需维护选择器。无需变通方案。只需数据。
>
> 这是不公平的优势，而且完全开源。
> https://github.com/D4Vinci/Scrapling

- 图片：[img1](https://pbs.twimg.com/media/HCoWkW3a4AAEiMM?format=jpg&name=large)
