# Graph & Multi-Agent

- [← 返回总目录](../x-note.md)
- graph engineering、多 agent 编排与流水线
- 共 9 篇，按收藏顺序倒序（最新在上）

## Part 1 · Index

- [Google 1 小时课程：从 agent 到 loop 到 graph](#x-2085433401562308987) · @Mahaximus_ · 2026-08-06 · 课程推荐
- [How to Become a Graph Architect With Zero Experience (Full Course)](#x-2083131009986396282) · @eng_khairallah1 · 2026-07-31 · 学习路线（长文教程）
- [Graph Engineering with Claude: 12 steps from a single loop to a self-verifying fleet](#x-2079636027736457707) · @0xCarnagee · 2026-07-21 · 搭建教程（带代码）
- [Google 2 小时课程：1 prompt → 100 agents → loops → graphs](#x-2083602508807569560) · @0xCodila · 2026-08-01 · 课程推荐
- [30 个 Agent 替代 30 个工程师，12 天交付完整代码库](#x-2029350130261082429) · @sodawhite_dev · 2026-03-05 · 案例分享
- [OpenAI Symphony：把 Linear 看板变成自动研发流水线](#x-2029741601975849132) · @chenchengpro · 2026-03-06 · 源码解读
- [30 个 agent 案例的开源地址：agent-orchestrator](#x-2029350223575920769) · @sodawhite_dev · 2026-03-05 · 工具 / 案例
- [OpenAI Symphony：让 agent 自主完成整个开发流程](#x-2029497156554342760) · @GitHub_Daily · 2026-03-05 · 工具介绍
- [Shubham Saboo：7×24 运行的 AI Agent 团队蓝图](#x-2022374455989932409) · @Saboo_Shubham_ · 2026-02-13 · 蓝图分享

## Part 2 · Details

### x-2085433401562308987

**Google 1 小时课程：从 agent 到 loop 到 graph**

- 作者：Mahax (@Mahaximus_) · 发帖 2026-08-06 · [原帖](https://x.com/Mahaximus_/status/2085433401562308987)
- 来源：🔖 收藏 · 拉取 2026-10-27 · 类型：课程推荐
- **总结**：推荐 Google 的 1 小时 graph engineering 课程，附章节时间戳：第一个 agent → agent 记忆 → agentic loops → 构建 MCP → graph engineering。是一条从单 agent 到图编排的入门路径，适合快速建立整体概念。帖子本身没有技术细节。

**正文**

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

[↑ 回到本页目录](#part-1--index)

### x-2083131009986396282

**How to Become a Graph Architect With Zero Experience (Full Course)**

- 作者：Khairallah AL-Awady (@eng_khairallah1) · 发帖 2026-07-31 · [原帖](https://x.com/eng_khairallah1/status/2083131009986396282)
- 来源：🔖 收藏 · 拉取 2026-10-27 · 类型：学习路线（长文教程）
- **总结**：一条 20 步、分 5 个阶段的 graph architect 学习路线：①先掌握 loop（1–4）；②建立 graph 心智模型：节点、边、状态（5–9）；③核心模式：fan-out、路由、校验门等（10–14）；④可靠性：恢复路径、checkpoint 与状态持久化、可观测性（15–18）；⑤架构思维：知道什么时候不该用 graph（19–20）。最后讲常见卡点和各阶段「做得好」的标准。重点是按顺序学，不要跳步。

**正文**

- **"Graph engineering" trended on X this month — people reacted in one of three ways**
  - Dismissed it as another buzzword
  - Nodded along with no real idea how to build one
  - A small group will **learn it properly, before the crowd catches up**
    - The term is still new, so being genuinely good at it puts you years ahead
  - The difference between these groups is not talent — **it is a path**
- **What a graph architect is**
  - Not someone who memorized a framework
  - Someone who can look at a messy, real-world problem and **design the network of agents, tools, checks, and human decisions that solves it reliably**
  - A valuable skill and the current outermost edge of AI engineering
  - Almost nobody has it yet — the term is two weeks old
- **The path: 20 steps in 5 phases**
  - No graph theory degree required
  - Follow in order and don't skip — every step builds on the one before
- **Phase 1: Master the Loop First (Steps 1–4)**
  - You cannot build a network of loops until you can build one loop
  - Non-negotiable — skipping it is why most people's graphs fall apart
  - **Step 1 · Understand what a loop actually is**
    - A loop is **the atom of agentic work**: an agent takes an action → a result comes back → something checks whether it's good → repeat until the job is done
    - A graph is just many of these wired together, so burn this shape into your brain first
    - **Do this:** for a task you understand, write out the four parts of a loop in plain English — the action, the result, the check, the repeat condition
  - **Step 2 · Build one working loop**
    - Pick a simple real task; build a single agent that loops until done
    - Give it one tool. Let it try, check, and retry
    - Feel how it behaves — where it gets stuck, where it loops forever
    - This hands-on frustration is the best teacher you'll get
    - **Do this:** build a single-agent loop that completes one real multi-step task end to end
  - **Step 3 · Learn why the verifier is everything**
    - The most important part of any loop is **the check — the verifier** that decides whether the work is good
    - A loop with a weak verifier **produces confident garbage fast**
    - **Loop engineering** (the rung right before graphs) is largely the craft of writing good verifiers
    - Master this now and graphs become easy later
    - **Do this:** make the verifier from Step 2 genuinely strict; watch output quality climb
  - **Step 4 · Learn the four ways single loops fail at scale**
    - Loops break in predictable ways once work gets complex:
      1. They can't branch cleanly
      2. They can't run things in parallel
      3. They can't enforce checkpoints across steps
      4. They handle failure by just retrying
    - These four failure modes tell you exactly **what a graph is for**
    - **Do this:** for each failure mode, write down a task where a single loop would struggle with it
- **Phase 2: Learn the Graph Mental Model (Steps 5–9)**
  - Learn the vocabulary and the shape — see work as a graph before you build one
  - **Step 5 · Learn the three primitives: nodes, edges, state**
    - **Node** — a unit of work
    - **Edge** — a route that decides what runs next
    - **State** — the shared information flowing through the system
    - Every graph, however complex, is just these three things — get them cold
    - **Do this:** sketch a task you know on paper as nodes and edges, noting what state flows between them
  - **Step 6 · Understand that not every node is an LLM**
    - **The insight that separates architects from beginners**
    - The best graphs mix LLM-powered nodes with plain deterministic functions, tool calls, and validators
    - A simple check should be a function, not a model
    - Overusing LLMs is the most common way graphs become slow, costly, and flaky
    - **Do this:** in your Step 5 sketch, mark which nodes truly need an LLM and which could be plain functions — most should be functions
  - **Step 7 · Learn conditional edges**
    - The edges that make a graph powerful are conditional: "if the output has an error, route here; otherwise, continue there"
    - This is how a graph expresses decisions a straight loop can't
    - **Do this:** add at least two conditional edges to your sketch; give the system a real decision to make
  - **Step 8 · Design your state deliberately**
    - **Half of good graph design is good state design**
    - Too little shared state → nodes can't do their jobs
    - Too much → nobody can reason about the system
    - Practice deciding exactly what each node needs and what it should pass on
    - **Do this:** write out the full state your graph carries, field by field, and justify each one
  - **Step 9 · Pick one framework and learn its way of doing this**
    - You don't need many — pick one graph-orchestration framework
    - **LangGraph** is the most common starting point
    - Learn how it expresses nodes, edges, and state
    - The concepts transfer everywhere; you just need one place to practice
    - **Do this:** build your paper sketch as a real running graph in one framework; get it to execute end to end
- **Phase 3: Master the Core Patterns (Steps 10–14)**
  - Architects don't reinvent structures — they recognize which known pattern fits and apply it
  - These five patterns cover most real work
  - **Step 10 · The router**
    - A node that looks at the input and routes it to the right specialist or path
    - The simplest branching pattern and the gateway to everything else
    - **Do this:** build a graph that routes different kinds of input to different handling nodes
  - **Step 11 · The orchestrator-worker**
    - A manager node breaks a job into subtasks, assigns each to a worker node, and assembles the results
    - **The backbone of most multi-agent systems**
    - **Do this:** build a graph where one node delegates to two or more workers and combines their output
  - **Step 12 · Parallel fan-out and fan-in**
    - Several independent nodes run at the same time, then results converge at a single node
    - This is how a graph delivers real speed a loop can't
    - **Do this:** build a graph that runs three tasks in parallel and merges the results
  - **Step 13 · The evaluator-optimizer**
    - One node produces work; another critiques it against a standard; the work loops back for revision until it passes
    - **The quality engine of serious graphs**
    - **Do this:** build a generator node and a critic node, wired so weak output gets sent back with specific feedback
  - **Step 14 · The human-in-the-loop gate**
    - A node where the system pauses and waits for a person to approve before continuing
    - Anything irreversible — sending, publishing, spending, deleting — routes through one
    - Not optional in production; **it's what makes a graph safe**
    - **Do this:** add a pause-for-approval node before any consequential action in one of your graphs
- **Phase 4: Build for Reliability (Steps 15–18)**
  - Anyone can make a graph run once; architects make it run the ten-thousandth time
  - **This phase is what companies actually pay for**
  - **Step 15 · Add validation gates**
    - Beyond the evaluator pattern: explicit gate nodes at critical points whose only job is to verify work meets a standard before it proceeds
    - **Named, non-negotiable checkpoints are a graph's greatest advantage over a loop**
    - **Do this:** add a validation gate that hard-stops the graph if output fails a defined standard
  - **Step 16 · Design recovery paths**
    - A loop's answer to failure: "retry"
    - An architect's answer: a deliberate path
      - Fall back to a simpler method
      - Escalate to a human
      - Fail safely with a clear message
    - Decide in advance what each kind of failure does
    - **Do this:** for every node that can fail, define where a failure routes instead of retrying forever
  - **Step 17 · Add checkpoints and state persistence**
    - Real graphs can pause and resume
    - If the system stops halfway (waiting on a human or recovering from a crash), it should pick up where it left off, not start over
    - Persisting state at checkpoints makes this possible
    - **Do this:** make one of your graphs able to stop mid-run and resume from where it paused
  - **Step 18 · Make it observable**
    - You can't fix what you can't see
    - Add logging and tracing: what each node did, what state flowed, where things went wrong
    - An architect can debug a graph because they built it to be debuggable
    - **Do this:** add tracing so you can replay exactly what happened on any run
- **Phase 5: Think Like an Architect (Steps 19–20)**
  - These steps aren't about building — they're about **judgment**, which makes someone an architect rather than a technician
  - **Step 19 · Master when NOT to build a graph**
    - **The most senior skill: knowing most tasks don't need a graph at all**
    - A single job with a single verifier is a loop, and should stay one
    - Reaching for a graph before the work demands it hands you a distributed-systems problem you didn't have
    - Start with the simplest thing that works; let the problem earn every bit of added complexity
    - **Do this:** take three tasks and correctly decide which need a graph and which are just loops or plain scripts
    - Being able to say "this doesn't need a graph" is the mark of mastery
  - **Step 20 · Design for production, evals, and the team**
    - Design graphs other people can run, trust, and maintain
      - Build an **evaluation suite** to measure whether a change helped or hurt
      - **Document** the graph so a teammate understands it
      - Design it to be **extended without collapsing**
    - This separates a clever demo from a system a company runs its business on
    - **Do this:** build an eval set for one graph and run it after every change; document it so someone else could maintain it
- **How to Actually Walk This Path**
  - Twenty steps is really five ideas: master the loop → learn the graph model → learn the patterns → build for reliability → develop the judgment to know when to stop
  - **Don't sprint all twenty in a weekend**
    - People who rush end up with a shaky mental model and graphs that break
  - Give Phase 1 real time — everything rests on it
  - Move one phase at a time, building something real at each step rather than just reading
  - The "do this" actions aren't optional — they're the whole point
  - **You become a graph architect by building graphs**, not by understanding them in the abstract
  - **Realistic pace**
    - A week or two per phase if you're comfortable coding and with LLM APIs; longer if newer
    - **6–8 weeks of hands-on practice** → you can look at a real problem and design the right graph for it, including knowing when "this doesn't need one"
- **The Four Things That Stall People (And How to Beat Them)**
  - Most people who start don't finish, and they stall at predictable places
  - **1. They skip Phase 1 because loops feel too basic**
    - After seeing "graph engineering" trend, a single loop feels like a step backward
    - Then their graphs fall apart and they can't tell why — the loops inside were never solid
    - **Beat it:** don't move on until you can build a single loop with a genuinely strict verifier
    - People who honor this move faster overall, not slower
  - **2. They collect frameworks instead of building**
    - Tutorial after tutorial, three different tools, never one working graph
    - Learning about graphs feels like progress but produces nothing
    - **Beat it:** pick one framework; don't touch another until you've built at least three real graphs in it
    - Depth in one beats shallow exposure to many
  - **3. They over-engineer the moment they learn the patterns**
    - Right after Phase 3, armed with orchestrators and parallel workers, they build elaborate graphs for problems that needed a loop
    - Feels sophisticated; produces fragile, unmaintainable systems
    - **Beat it:** treat Step 19 (knowing when not to build a graph) as the real graduation
    - **Restraint is the senior skill**
  - **4. They stop at "it runs" and never reach "it's reliable"**
    - They get a graph working once, feel done, skip Phase 4
    - It breaks the first time reality throws something unexpected → they conclude graphs are flaky
    - **Beat it:** a graph is unfinished until it has validation gates, recovery paths, and debuggability
    - "It ran in the demo" is where amateurs stop and architects begin
- **What Good Looks Like at Each Phase**
  - **After Phase 1** — you can build a single-agent loop that reliably completes a real task, and explain exactly why a weak verifier ruins it
  - **After Phase 2** — you can sketch any problem as nodes, edges, and state on paper before writing code, and instinctively mark which nodes need an LLM and which don't
  - **After Phase 3** — you can name which core pattern fits a problem and implement it without a tutorial
  - **After Phase 4** — your graphs survive bad input, failed tools, and interruptions, and you can replay any run to see what happened
  - **After Phase 5** — you can look at a request and correctly say **"this doesn't need a graph at all"**
    - More than any pattern, this is what a graph architect actually is
  - Do all five → a skill almost nobody had a month ago, one that keeps paying off after the buzzword fades
- **The Questions Everyone Asks Before They Start**
  - **Do I need graph theory or heavy math?** No
    - This isn't CS-course graph theory; no proving theorems about traversal
    - "Graph" just means nodes connected by edges with information flowing through — a way of drawing a solution
    - If you can sketch boxes and arrows and reason about what flows between them, that's all the math you need
  - **Do I need to be a strong programmer first?**
    - You need to be comfortable writing code and working with LLM APIs — if brand new to programming, spend time there first
    - You don't need to be an expert
    - Most of the difficulty is clear thinking about structure, not advanced coding
    - If you can build a single agent that calls an API and handles the response, you're ready for Phase 1
  - **Which framework should I learn?**
    - Pick one common graph-orchestration framework and go deep
    - The specific choice matters far less than committing long enough to build several real graphs
    - The concepts (nodes, edges, state, gates) transfer everywhere — you're learning the discipline, not the tool
    - **Framework-hopping is a way of feeling busy without getting better**
  - **Isn't this a buzzword that'll be gone in six months?**
    - The word might fade; the skill won't
    - What you're learning — **designing reliable systems around unreliable models** — has been valuable for years under other names and will stay valuable under the next one
    - You're building a durable capability that happens to have a trendy label right now
  - **How do I know I'm ready to call myself a graph architect?**
    - When you can design the right structure for a real problem, including confidently saying "this one doesn't need a graph"
    - That judgment — not a certificate or framework badge — is the whole thing
- **The Honest Truth About Becoming a Graph Architect**
  - **Being a graph architect is not about the graphs — it's about clear thinking under complexity**
    - A graph is just a way of drawing a solution precisely enough that it works reliably
    - Masters aren't the ones who memorized the most patterns
    - They can look at chaos and see the simplest structure that tames it — sometimes a graph, often something far simpler
  - **The skill doesn't expire with the buzzword**
    - Prompt engineering → context engineering → loop engineering → graph engineering: the names keep changing
    - The underlying ability — designing reliable systems around unreliable models — only becomes more valuable
    - It's the skill every future rung of the ladder will require
  - **Why move now**
    - Skills are most valuable when demand is high and supply is nearly zero
    - That gap is widest right after a term goes mainstream, before most people have done the work
    - Many people are talking about graph engineering; almost none can design a reliable one
    - Gaps like this close as the crowd catches up — people who move during the window get years of head start compressed into weeks
  - The term is two weeks old; the crowd is still arguing about what it means
  - Eight weeks from now: still posting hot takes about a word, or one of the few who can actually build the thing
  - **Step one is understanding a single loop — start there today**

<details><summary>原文</summary>

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

</details>

- 图片：[img1](https://pbs.twimg.com/media/HOgbHEdWsAAVrR4?format=jpg&name=large)

[↑ 回到本页目录](#part-1--index)

### x-2079636027736457707

**Graph Engineering with Claude: 12 steps from a single loop to a self-verifying fleet**

- 作者：Carnage (@0xCarnagee) · 发帖 2026-07-21 · [原帖](https://x.com/0xCarnagee/status/2079636027736457707)
- 来源：🔖 收藏 · 拉取 2026-10-27 · 类型：搭建教程（带代码）
- **总结**：带代码的 12 步教程。问题：一个上下文塞四个任务就会「淹死」，解法不是换更大的模型，而是多个 worker 有意识地连起来。步骤包括：节点 = 一个工作，边 = 一次交接；每个节点有 schema 契约；用 parallel() fan-out；split-work-merge 的菱形结构；运行时用 router 改道；在边上放 skeptic 做校验；节点之间隔离；带停止条件的循环（连续两轮无新发现就停）。偏工程实操。

**正文**

- **Your agent works until it doesn't**
  - One job, one loop, one context — fine
  - Hand it something real and it drowns
- **Watch it happen**
  - You ask for research → analysis → code → a review of that code
  - Four jobs, one conversation
  - By the time it writes the review, it's forgotten what the research said
  - The context filled up and the early work fell out the bottom
- **Most people reach for a bigger model — wrong lever**
  - The model was never confused; **the architecture was**
  - You gave one worker four jobs and the memory budget for one
- **The fix is more workers, wired on purpose**
  - **Nodes** carry the work; **edges** carry the results
  - The picture they make is a **graph**
- This is a 12-step path from one overloaded loop to a fleet that splits the work, checks itself, and returns an answer no single context could have held
- **01. A node is a job. An edge is a handoff.**
  - Strip a graph down and only two things survive
    - **Node** — one agent, one job, one input, one result
    - **Edge** — the wire where one node's result becomes the next node's input
  - **The trap: reading "and then" as a wire**
    - "Read the config and then check the weather" has no wire — the weather never touches the config
    - Two jobs, zero dependency; a linear script staples them together for no reason
  - **Interrogate every "and then"**: does the next step actually read what the last one produced?
    - **Yes** → a real edge; the order is load-bearing, leave it
    - **No** → no edge at all; the wait between them is dead time you're paying for
  - **The whole test in one move**: sketch it as boxes and arrows, where an arrow is a variable one call hands to another
    - If you can't draw the arrow, there is no arrow
    - Those two boxes are strangers — **and strangers run at the same time**
- **02. Your straight-line agent is already a graph — a bad one**
  - "A, then B, then C, then D" is a graph — the worst possible one
    - A single wire, no branches, every node with exactly one input and one output
  - It gives the right answer, but slowly, and it snaps under pressure
    - If B hangs, everything after it starves
    - Everything before it sits finished with nowhere to go
  - **Builder → architect starts here: walk the chain and test every arrow**
    - Nine times out of ten, two or three arrows move no data
    - They're there because that's the order your fingers typed, not because the work demanded it
  - **Delete the fake arrows**
    - The chain buckles into something wider: a cluster of jobs that could have run together all along, feeding one node that finally needs them all at once
- **03. Give every node a contract**
  - A node you can't describe in one sentence is a node you can't trust to run alone
  - **Contract**: what goes in, what comes out, one job in between
    - **Input arrives explicitly** — handed in, never scavenged from some shared window the node hopes is still there
    - **Output has a fixed shape** — so the next node reads it instead of guessing at it
  - **Workflows enforce the contract with a schema**
    - Attach a JSON schema to an `agent()` call and the subagent can't hand you loose prose
    - It's forced to return validated structure
    - Claude re-runs it on any mismatch instead of dumping unparseable text in your lap
  ```javascript
  const FINDING = {
    type: 'object', additionalProperties: false,
    properties: {
      file:     { type: 'string' },
      line:     { type: 'number' },
      severity: { type: 'string', enum: ['block', 'warn', 'info'] },
    },
    required: ['file', 'line', 'severity'],
  };

  const hit = await agent(auditPrompt(file), {
    label:  `audit:${file}`,
    schema: FINDING,          // structured out, or Claude retries
    agentType: 'general-purpose',
  });
  ```
  - **The wire between nodes deserves the same discipline**
    - The instinct is to spin up an agent to "merge these results" — fight it
    - If merging means flatten and dedupe, that's a `flatMap` and a `Set`: instant, exact, free
    - **Spend agents on judgment. Never on plumbing.**
- **04. Fan out with `parallel()`**
  - **The move that pays for the whole graph**
  - When you hold N jobs that don't depend on each other (N files to scan, N sources to pull, N routes to check), stop feeding them through one mouth — open N mouths at once
  ```javascript
  phase('Scan');

  const raw = await parallel(
    ROUTES.map((r) => () =>
      agent(scanPrompt(r), {
        label:  `scan:${r}`,
        phase:  'Scan',
        schema: FINDING,
        agentType: 'general-purpose',
      }),
    ),
  );

  const found = raw.filter(Boolean);   // failed agents came back null
  ```
  - **Two things make it safe**
    - **`parallel()` is a wall** — nothing past it moves until every job clears, so the next stage always sees a full set
    - **A job that throws comes back as `null`** instead of blowing up the batch — one bad agent can't take the run down
      - That's why `filter(Boolean)` is there, every time
  - **Concurrency tracks your core count**; the rest waits in line
    - Throw a hundred jobs at it and they'll all land — just a fistful at a time
  - **None of it crowds Claude's own context** — each subagent holds its own
    - The session stays light while the fleet does the heavy lifting
- **05. The diamond: split, work, merge**
  - Fan-out + fan-in = **the diamond**, the shape you'll reach for more than any other
    - One node breaks the job apart
    - Many nodes chew through the pieces at once
    - One node pulls it back together
  - **The last node is where people cut corners**
    - Stapling three JSON blobs is nothing
    - Fusing three research passes into one coherent answer is a real job with a real quality bar — treat it like an agent, not a string concat
  ```javascript
  const flat = found.flatMap((f) => f.hits);
  log(`${flat.length} raw hits`);

  phase('Rank');
  const ranked = await agent(
    `Dedupe these and rank by severity:\n${JSON.stringify(flat)}`,
    { phase: 'Rank', schema: RANKED },
  );
  ```
  - **The rhythm: fan out → reduce → synthesize**
    - Widen to gather, collapse in plain code, then let one agent write the final word
  - **Keep the merge honest**
    - Only make the fleet wait at the wall if the merge genuinely needs the whole pile at once
    - Just flattening a list? That's an edge — do it inline and pay nothing
  - Once the diamond clicks, you stop asking your agent to take more steps and start asking **where the split and the merge belong** — the question that scales
- **06. Bend the edge at runtime with a router**
  - Not every graph is carved in advance — sometimes which wire fires depends on what a node just found
  - **A router looks at a result and picks the path**
  ```javascript
  const { size } = await agent(
    `How large is this diff? one word: small or large.\n${diff}`,
    { schema: { type: 'object',
        properties: { size: { enum: ['small', 'large'] } },
        required: ['size'] } },
  );

  const review = size === 'large'
    ? await parallel(FILES.map((f) => () => agent(reviewPrompt(f))))
    : await agent(`Quick pass over this diff:\n${diff}`);
  ```
  - **Determinism turns from handcuff into feature**
    - The decision can be Claude's — a subagent reads the diff and classifies it
    - But the branch is code Claude already wrote, so the same classification always takes the same road
    - No "the model felt like skipping the audit today" — skipping was never a move the graph offered
- **07. Put a skeptic on the edge**
  - **The quiet truth: the win isn't the extra agents — it's the scaffolding around them that earns trust in the output**
  - A **verifier** stands on the edge and tries to break the finding before it's allowed downstream
    - Survives the attack → passes
    - Fails → never reaches the answer
  - **Three shapes worth carrying**
    - **Refute it** — spawn a handful of skeptics whose whole job is to tear the finding apart; it lives only if most of them fail to
    - **Split the lens** — give each checker a different angle: is it correct, is it safe, does it actually reproduce
      - Three identical checks miss what three different ones catch
    - **Panel of judges** — generate a few attempts from different starts, score them in parallel, build the final from the winner
  - **The catch nobody warns you about: the skeptic needs a fresh context**
    - Feed it the same transcript the executor had and it isn't checking — it's nodding along to itself in a new hat
    - A dozen agents sharing one context aren't a graph
    - They're the same loop in disguise, and they fail exactly like the loop did — just later, with a bigger bill
- **08. Fence the nodes off from each other**
  - **In a chain, one death is fatal** — C dies, D never wakes
  - **In a graph, a death should be a shrug**
    - A job that throws inside `parallel()` comes back `null`; the survivors carry on
    - `filter(Boolean)` is the fence
  - **The nastier failure is quieter: agents colliding**
    - Real example: when the **Bun team** first split a big port across many agents, they hit the same git commands in the same workspace and overwrote each other's work
    - The run fell apart operationally, not intellectually
    - **The fix was structure, not a cleverer prompt**
      - Ban the shared commands
      - Give every worker its own isolated worktree
      - Merge clean at the end
  - **Before you fan anything out, answer three questions**
    1. Where does each agent do its work?
    2. How do the results come back together?
    3. When two of them disagree, who wins?
  - A fleet without those answers doesn't scale up — it just breaks faster
- **09. Add a loop that knows when to stop**
  - Some jobs won't tell you their size up front — you sweep for one bug and it uncovers three more
  - That calls for a **cycle**: a wire that runs back to an earlier node and goes again
  - **The danger**: a cycle that never converges is a money fire that spawns agents until the budget's gone
  - **The safe pattern: run until dry**
    - Keep sending finders out until a couple of rounds in a row turn up nothing new, then stop
  - **The detail that wrecks it for everyone the first time: dedupe against everything you've seen, not just what you confirmed**
    - Miss that and every rejected finding comes back next round
    - The loop never dries out; you pay over and over to rediscover the same dead ends
  ```javascript
  const seen = new Set();
  const kept = [];
  let dry = 0;

  while (dry < 2) {
    const raw = (await parallel(
      FINDERS.map((f) => () => agent(f.prompt, { schema: BUGS }))
    )).filter(Boolean).flatMap((r) => r.bugs);

    const fresh = raw.filter((b) => !seen.has(id(b)));
    if (!fresh.length) { dry++; continue; }   // a dry round
    dry = 0;
    fresh.forEach((b) => seen.add(id(b)));     // mark SEEN, not kept

    const judged = await parallel(fresh.map((b) => () =>
      parallel(['correct', 'safe', 'repro'].map((lens) => () =>
        agent(`Judge "${b.desc}" on ${lens}. real?`, { schema: VERDICT })))
      .then((v) => ({
        b, real: v.filter(Boolean).filter((x) => x.real).length >= 2
      }))));

    kept.push(...judged.filter((v) => v.real).map((v) => v.b));
  }
  ```
- **10. Price the graph before you run it**
  - Cost and speed both live in the shape — two levers move them
  - **Lever one: match the model to the node**
    - Grunt nodes that classify or extract → **Haiku 4.5**
    - Nodes that reason and build → **Sonnet 4.6**
    - The final gate, where a wrong answer is expensive → **Opus 4.8**
    - Every subagent inherits your session model unless you say otherwise
    - The `model` option on a single `agent()` call reroutes just that node
    - Glance at `/model` before a big run and push the cheap work down
  - **Lever two: `parallel()` vs `pipeline()`**
    - A `parallel()` wall makes the whole stage wait on its slowest node
    - A `pipeline()` lets each item flow through the stages on its own — item A can be finishing while item B is still starting
    - **Default to the pipeline**; only raise a wall when a stage truly needs the full set in hand at once
    - "It reads cleaner" is not that reason — wall latency is real time, in seconds you'll never get back
- **11. When you should not build a graph**
  - Most work isn't a graph; forcing one lights money on fire and adds new ways to fail
  - **Skip it when:**
    - **The job is small** — one function, one bug; orchestration costs more than the work
    - **You want to watch every step land before the next fires** — a graph's point is running wide without you, exactly wrong when you need the reins
    - **You don't yet know what you're hunting** — open-ended work wants one agent you can steer, not a fleet locked to a plan before anyone understands the problem
    - **The steps genuinely need each other in order** — if every step reads the last one's output, it's a true chain; parallelism has nothing to grab onto
  - **The tell is Part 1 all over again**
    - Can't find two boxes with no arrow between them? There's no graph hiding in there
    - It's a loop, and a loop is the right tool — use it without apology
- **12. Hand the pen to Claude**
  - The last step: stop drawing the graph yourself
  - With **dynamic workflows** you hand over the goal and Claude writes the orchestrator — carving up the task, choosing the fan-out, running the fleet, fusing the result
  - **Three doors in**
    - Drop the word **"workflow"** into a prompt and Claude builds one for the job
    - Run **`/deep-research`** — a graph already shipping in production
    - Flip on **ultrathink** and Claude plans one for every serious task in the session
  ```text
  > audit every route in src/routes for missing auth.
    one agent per file, verify each hit before you report.

    /workflows — auth-audit — running
    done  Scope      1/1    2.1k tok · 4s
    done  Fan-out    18/18  one agent per route
    live  Verify     11/18  skeptics voting on each hit…
    wait  Synthesize 0/1    holding for verify
    session stays live — keep working while it runs
  ```
  - **Like the run? Press `s`**
    - It saves to `~/.claude/workflows/`
    - Version it, name it — anyone who clones the repo can fire the same graph
  - **What the ceiling looks like: the Bun team's Zig-to-Rust port on this exact machinery**
    - Roughly **50 workflows**, **64 agents** peaking in parallel
    - About **535,000 lines of Zig** rewritten into **over a million lines of Rust** in **eleven days**
    - Around **$165,000** in usage
    - One human steering and watching the whole time
    - The power is real — so is the invoice, and so is the supervision
- **Six graphs to build this week**
  1. **Security sweep over every route** — one agent per file, a skeptic confirming each hit; coverage no single window could hold
  2. **Cited report through `/deep-research`** (already in the box) — parallel searches, skeptics voting on every claim before a word gets written
  3. **Module port, file by file** — translation fanned out, the test suite as a gate, failures looped back until they pass
  4. **Adversarial diff review that routes on size** — small change gets one pass; big change triggers the full parallel audit
  5. **Scheduled ecosystem scan** — saved once, run forever; sources pulled in parallel and ranked into a digest
  6. **Discovery run of unknown size** — finders in parallel, everything deduped against what's been seen, looping until two rounds come up empty
- **Five ways your first graph dies**
  1. **One node doing everything** — when it falls, everything falls; cut it into single-job nodes
  2. **No contracts on the wires** — no schema, no fixed shape, every node guessing at the last one's output
  3. **No fallback path** — one error and the run collapses; give every fragile node somewhere to fail to
  4. **Sonnet 4.6 doing your routing** — routing is classification; Haiku 4.5 does it faster and cheaper; save the big model for building
  5. **No skeptic on the edge** — ship one wrong answer and that's the last time anyone trusts the fleet
- **A prompt asks. A graph decides.**
  - The straight line was never the wall you kept hitting
    - It was just the first shape you knew how to draw — one thread, one head, one thing after another, because that's how typing feels
  - See the nodes and edges and the question flips
    - Stop pushing one agent to do more; ask the graph to do it wider
  - **Split** where the work is independent
  - **Guard the wires** where the answer has to be right
  - **Anchor the nodes** that hold the truth and never let them drift
  - Most people will keep typing in a line; the ones who learn to draw will run the fleet
  - **Draw it. Then get out of its way.**
  - Start where this begins: **Loop Engineering** — the single loop every graph is built on

<details><summary>原文</summary>

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

</details>

- 图片：[img1](https://pbs.twimg.com/media/HNxCj6YXMAEC-lT?format=jpg&name=large) [img2](https://pbs.twimg.com/media/HNxXiOcXQAAOlU4?format=png&name=large) [img3](https://pbs.twimg.com/media/HNxXoItWsAEOg3n?format=png&name=large) [img4](https://pbs.twimg.com/media/HNxY051W8AAOuh5?format=png&name=large) [img5](https://pbs.twimg.com/media/HNxYx01WkAAdkOq?format=png&name=large) [img6](https://pbs.twimg.com/media/HNxY6VsWcAAHJuX?format=png&name=large) [img7](https://pbs.twimg.com/media/HNxYnYgXQAA6jSU?format=png&name=large) [img8](https://pbs.twimg.com/media/HNxYtQeXUAE9lZK?format=png&name=large) [img9](https://pbs.twimg.com/media/HNxYUcJWMAAQqZ5?format=png&name=large) [img10](https://pbs.twimg.com/media/HNxZAzkXAAAjuXQ?format=png&name=large) [img11](https://pbs.twimg.com/media/HNxYPJGWEAAl9Ep?format=png&name=large) [img12](https://pbs.twimg.com/media/HNxZK_nWYAA1950?format=png&name=large) [img13](https://pbs.twimg.com/media/HNxZVpGXkAAmZR5?format=png&name=large) [img14](https://pbs.twimg.com/media/HNxZbx5WUAEBc28?format=png&name=large)

[↑ 回到本页目录](#part-1--index)

### x-2083602508807569560

**Google 2 小时课程：1 prompt → 100 agents → loops → graphs**

- 作者：codila (@0xCodila) · 发帖 2026-08-01 · [原帖](https://x.com/0xCodila/status/2083602508807569560)
- 来源：🔖 收藏 · 拉取 2026-10-27 · 类型：课程推荐
- **总结**：推荐 Google 免费 2 小时课程，附进度时间戳：第一个 agent → loop engineering（迭代、检查、中断）→ graph engineering → 会自我节流的 agent → 多 agent 系统的完整 graph。观点：大多数人搭完一个 agent 就停了，而完整系统是 agent 把自己连成 graph。帖子本身没有技术细节。

**正文**

- **Google released a free 2-hour course on graph engineering**: 1 prompt → 100 agents → loops → graphs
- **Course map**
  - 10% → 17:44 — build your first agent
  - 30% → 39:30 — **loop engineering**: iterate, check, break
  - 60% → 1:12:38 — **graph engineering**
  - 75% → 1:34:26 — agents that throttle themselves
  - 100% → 1:55:05 — full graph for multi-agent systems
- **Point**: most people build one agent and call it done; this covers the full system where agents wire themselves into a graph

<details><summary>原文</summary>

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

</details>

- 含视频（未转写）

[↑ 回到本页目录](#part-1--index)

### x-2029350130261082429

**30 个 Agent 替代 30 个工程师，12 天交付完整代码库**

- 作者：苏打白.Dev (@sodawhite_dev) · 发帖 2026-03-05 · [原帖](https://x.com/sodawhite_dev/status/2029350130261082429)
- 来源：❤️ 点赞的评论 → 原帖（via [2029350223575920769](https://x.com/i/status/2029350223575920769)） · 拉取 2026-10-27 · 类型：案例分享
- **总结**：一个多 agent 落地案例：用 30 个 AI agent 替代 30 个工程师，12 天交付 4.4 万行 TypeScript、175 个 PR、1500+ 个测试，CI 挂掉时 agent 还能自己修。帖子本身只有数据，没有讲架构细节。价值在于给「大规模并行 agent 能不能交付真实代码库」提供了一个量级参考。

**正文**

> 刚看到一个硬核案例：用30个AI Agent替换30个工程师，12天交付完整代码库（44K行TS、175 PR、1500+测试、CI挂了还能自己修。。。）。

- 含视频（未转写）

[↑ 回到本页目录](#part-1--index)

### x-2029741601975849132

**OpenAI Symphony：把 Linear 看板变成自动研发流水线**

- 作者：陈成 (@chenchengpro) · 发帖 2026-03-06 · [原帖](https://x.com/chenchengpro/status/2029741601975849132)
- 来源：🔖 收藏 · 拉取 2026-10-27 · 类型：源码解读
- **总结**：读完 OpenAI 开源的 Symphony 代码后的要点：核心循环是监控 Issue → 分配 agent → 写代码 → 提 PR → 循环；用 Elixir/OTP 天然支持多 agent 并发，每个 Issue 一个独立 workspace；最有意思的设计是 WORKFLOW.md，把 agent 的行为策略写进仓库，可以跟代码一起 review 和回滚。是「看板驱动的 agent 编排」的参考实现。

**正文**

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

[↑ 回到本页目录](#part-1--index)

### x-2029350223575920769

**30 个 agent 案例的开源地址：agent-orchestrator**

- 作者：苏打白.Dev (@sodawhite_dev) · 发帖 2026-03-05 · [原帖](https://x.com/sodawhite_dev/status/2029350223575920769)
- 来源：🔖 收藏 · 拉取 2026-10-27 · 类型：工具 / 案例
- **总结**：这是对上文案例（30 个 agent 替代 30 个工程师、12 天交付）的补充，给出开源地址：OrchestratorInc/agent-orchestrator，一个 Apache-2.0 的 Claude Code 编排器。上文是案例数据，这条是可以直接去读的代码，两者合起来看。

**正文**

> 地址在这：

- 上文（作者原帖 @sodawhite_dev）：
  > 刚看到一个硬核案例：用30个AI Agent替换30个工程师，12天交付完整代码库（44K行TS、175 PR、1500+测试、CI挂了还能自己修。。。）。
- 链接卡片：[GitHub - OrchestratorInc/agent-orchestrator: Open-source (Apache-2.0) orchestrat](https://t.co/ys8LyplisL)

[↑ 回到本页目录](#part-1--index)

### x-2029497156554342760

**OpenAI Symphony：让 agent 自主完成整个开发流程**

- 作者：GitHubDaily (@GitHub_Daily) · 发帖 2026-03-05 · [原帖](https://x.com/GitHub_Daily/status/2029497156554342760)
- 来源：🔖 收藏 · 拉取 2026-10-27 · 类型：工具介绍
- **总结**：从使用者角度介绍 Symphony：监控看板任务，自动派 agent 处理，完成后提供 CI 状态、代码审查反馈、复杂度分析和演示视频作为「工作证明」，通过后安全合并。工程师只需在更高层面管理任务。提供技术规范，可以让 AI 用任意语言实现，也有 Elixir 参考实现。和上面的源码解读互补。

**正文**

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

[↑ 回到本页目录](#part-1--index)

### x-2022374455989932409

**Shubham Saboo：7×24 运行的 AI Agent 团队蓝图**

- 作者：Shubham Saboo (@Saboo_Shubham_) · 发帖 2026-02-13 · [原帖](https://x.com/Saboo_Shubham_/status/2022374455989932409)
- 来源：🔖 收藏 · 拉取 2026-10-27 · 类型：蓝图分享
- **总结**：作者分享自己搭建的 7×24 运行的 AI agent 团队，声明「没有理论、没有废话」，完整蓝图免费提供。帖子正文只有引子，具体内容在链接或附件里，需要点开原帖看。

**正文**

> How I built the AI Agent Team that runs 24/7
>
> No hot takes. No theory. No fluff.
>
> Entire Agent team blueprint available for FREE

- 图片：[img1](https://pbs.twimg.com/media/HA8BVhPaIAAWkft?format=jpg&name=large)

[↑ 回到本页目录](#part-1--index)
