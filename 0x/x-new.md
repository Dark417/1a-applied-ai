# X Likes · 关键词速览

- 共 48 条，按点赞顺序倒序（最新在上）
- 上半部分：关键词 + 简述；下半部分：原帖全文
- 自动生成，勿手改：改 `data/liked/*.json` 后跑 `scripts/render.py`

## Part 1 · Keywords

- [2026-10-26 · @AIStarsGo](#x-2114629460930740466)：`agent 时代的学习`, `deep work`, `shallow work`, `认知退化`
  - 个人教训：别让 agent 替你读论文，别把技术学习和英语学习混在一起，别为了用掉 token 去跑后台任务；要持续检查自己的认知是在进步还是在退化。
- [2026-10-24 · @0xsmerkzz](#x-2114099234001600931)：`SpaceXAI`, `GrokBot`, `multi-agent team`, `Chief of Staff agent`, `/loop`
  - SpaceXAI 工程师分享：同时跑 35+ 个 GrokBot agent，由一个 Chief of Staff agent 统一管理；附 1 小时 workshop 视频。
- [2026-10-24 · @Sumanth_077](#x-2113948384113598588)：`Harness²`, `Google`, `harness engineering`, `Propose→Probe→Compose`, `self-improving`
  - Google 开源 Harness²：模型权重不动，递归改进 agent 外围的 harness。任务内用 Propose→Probe→Compose 循环，跨任务保留已验证的 harness 和经验。
- [2026-10-23 · @AnnatarXBT](#x-2113634548378374458)：`harness engineering`, `Wavestone`, `Claude Code`, `Codex`, `7-part harness`
  - Wavestone 读了 11 个 coding agent 的源码，总结出共同的 7 部分 harness：loop、LLM 层、tools、memory、safety、orchestration、extensions。核心观点：agent = model + harness。
- [2026-10-03 · @sermakarevich](#x-2106453816757354947)：`evals`, `LLM 评测`, `PM / CEO 视角`, `可复现测试`
  - 长文：用通俗语言讲清楚怎么判断一个 LLM 系统是否真的可用，从 eval 的定义一直讲到落地细节，面向工程师、PM 和管理层。
- [2026-09-28 · @shao__meng](#x-2104453599367770287)：`Stanford CS329A`, `Self-Improving AI Agents`, `课程`
  - 推荐斯坦福 CS329A《Self-Improving AI Agents》，9 讲视频已全部上线，附课程主页和 YouTube 播放列表。
- [2026-09-19 · @0xMortyx](#x-2101308432305254889)：`Jev`, `decision layer`, `routing`, `agent execution`
  - Jev 被定位为 LLM 推理和 agent 执行之间的「决策层」：用 Choice / Score / Noul 显式路由，决策放在模型之外，号称快 193 倍、便宜 444 倍。
- [2026-07-31 · @eng_khairallah1](#x-2083131009986396282)：`graph engineering`, `graph architect`, `full course`
  - 长文课程：零基础成为 graph architect 的路线，涵盖节点设计、校验门、恢复路径、checkpoint、可观测性，以及什么时候不该用 graph。
- [2026-07-29 · @CodeNewsletter](#x-2082413202353406091)：`The Code newsletter`, `推广`
  - The Code newsletter 的订阅推广，内容空泛。
- [2026-08-06 · @AnatoliKopadze](#x-2085421662447468758)：`Anthropic`, `self-prompting system`, `agent loops`, `memory`
  - Anthropic 工程师 45 分钟演讲：不要手动 prompt Claude，而要搭一个能自我 prompt、自我纠错、越跑越好的系统。
- [2026-07-21 · @0xCarnagee](#x-2079636027736457707)：`graph engineering`, `Claude`, `subagents`, `self-verifying fleet`
  - 长文：分 12 步从单个 loop 扩展到能自我验证的 agent 集群；核心是拆分上下文，而不是换更大的模型。
- [2026-08-05 · @Mahaximus_](#x-2085024744387092973)：`agents`, `loops`, `graphs`, `Claude`
  - 长文汇总：agent（自主规划）、loop（跑到达标为止）、graph（并行 worker）三层是什么，以及怎么在 Claude 上组合起来。
- [2026-08-01 · @0xCodila](#x-2083602508807569560)：`Google`, `graph engineering`, `loop engineering`, `multi-agent`, `课程`
  - Google 免费 2 小时课程：从第一个 agent 到 loop engineering，再到 multi-agent graph，附各章节时间戳。
- [2026-06-29 · @AnatoliKopadze](#x-2071649423042412597)：`Spotify`, `Boris Cherny`, `agent loops`, `Claude Code`
  - Spotify 首席架构师：引入 loop 后 agent 成功率从 20–30% 提到 80%；Spotify 73% 的代码由 AI 写。核心观点：模型不如外围的 loop 重要。
- [2026-06-28 · @0xMovez](#x-2071214176526049739)：`agent loops`, `harness`, `evals`, `LLM-as-judge`
  - 前 Google 工程师 20 分钟讲 agent 自我改进的循环：trace → LLM judge → diagnose → fix → ship。
- [2026-06-24 · @gxjo_dev](#x-2069734857626833371)：`Claude Code`, `趣闻`, `traffic lights`
  - 有人给 Claude Code 做了个「红绿灯」状态指示器，图片梗。
- [2026-06-21 · @0xMovez](#x-2068763235587694769)：`Andrew Ng`, `self-improving loops`, `agentic systems`
  - Andrew Ng 30 分钟演讲：他的任务已全部交给 agent，下一步是 self-improving loops。
- [2026-06-20 · @gregisenberg](#x-2068325550603559402)：`技能趋势`, `agent operator`, `distribution`, `builder-distributor`
  - Greg Isenberg 列出当下最值钱的技能：会搭建和管理 agent、会做分发、做机器人、做短视频、既能做产品又能分发、线下社群。
- [2026-06-16 · @eng_khairallah1](#x-2066827221537333611)：`Stanford`, `LLM from scratch`, `scaling laws`, `pretraining`, `课程`
  - 推荐斯坦福 2 小时讲座：从零构建 LLM，覆盖 scaling laws、数据、架构和后训练对齐。
- [2026-06-08 · @AnatoliKopadze](#x-2063985608381362576)：`AI agents 入门`, `agent spectrum`, `Claude Code`, `build your own`
  - 长文：agent 是一个光谱而不是一个类别；讲清 LLM 对话和 agentic workflow 的区别，并一步步用 Claude Code 搭自己的 agent。
- [2026-06-16 · @0xCodez](#x-2066867539305459732)：`harness engineering`, `Claude Code`, `subagents`, `hooks`, `memory`
  - 长文：14 步 harness 路线图，从默认 Claude Code 到规则、subagent、hook、memory 都齐备的自我改进系统。核心观点：loop 好不好，取决于底下的 harness。
- [2026-05-07 · @OpenAI](#x-2052480800004956323)：`OpenAI`, `Codex`, `Chrome plugin`, `browser agent`
  - OpenAI：Codex 现在能直接在 Chrome 里工作，可以在后台多标签页并行操作，不会抢占你的浏览器。
- [2026-05-06 · @unusual_whales](#x-2052068619635589466)：`Anthropic`, `dreaming`, `self-improving agents`, `新闻`
  - 快讯：Anthropic 发布「dreaming」功能，让 agent 能自我改进。
- [2026-05-03 · @rasbt](#x-2050988005817499827)：`LLM 架构`, `Ling 2.6`, `MiniMax M2.7`, `MiMo V2.5`, `Granite 4.1`
  - Sebastian Raschka 整理的 4 月第二批开源模型架构：Ling 2.6 1T、MiniMax M2.7、MiMo V2.5、Laguna XS.2、Hy3-preview、Granite 4.1。
- [2026-05-03 · @dair_ai](#x-2050956647909015788)：`AI papers weekly`, `Agentic Harness Engineering`, `DAIR.AI`
  - DAIR.AI 每周论文精选（4/26–5/3），头条是 Agentic Harness Engineering：把 harness 的演化变得可观测、可证伪。
- [2026-05-01 · @Suryanshti777](#x-2050228936270037068)：`RAG`, `Karpathy`, `LLM Wiki`, `知识积累`
  - 观点：RAG 每次都从零开始、不积累任何东西；Karpathy 的 LLM Wiki 让 LLM 持续维护一份知识库，才是真正的累积。
- [2026-03-06 · @nopinduoduo](#x-2029858356916277757)：`SkillsBench`, `Google`, `agent skills`, `skills 质量`
  - 解读 Google 的 SkillsBench 论文：4 万多个 skills 里只有约 1k 个可用，LLM 写的 skill 基本不行，好的 skill 都是手写的。
- [2026-03-05 · @EHuanglu](#x-2029562218048541087)：`Nano Banana 2`, `室内设计`, `floor plan → 3D`
  - Nano Banana 2 能把手绘户型图变成 4K 3D 渲染，还能一键换家具；附 OpenArt 教程。
- [2026-03-03 · @shao__meng](#x-2028833958230933729)：`agentic engineer`, `context 管理`, `调研与实现分离`, `极简工具`
  - 如何成为顶级 agentic engineer：工具越精简越好；上下文只给刚好够用的信息；调研和实现用不同的 agent、不同的上下文。
- [2026-02-27 · @heyrimsha](#x-2027350587533332748)：`Anthropic`, `Claude Skills`, `SKILL.md`, `progressive disclosure`
  - 解读 Anthropic 的《The Complete Guide to Building Skills for Claude》：skill 是结构化系统，不只是 prompt，关键机制是 progressive disclosure。
- [2026-02-12 · @OpenAIDevs](#x-2022009906329739681)：`OpenAI`, `GPT-5.3-Codex-Spark`, `实时编码`, `新闻`
  - OpenAI 发布 GPT-5.3-Codex-Spark，主打超快实时编码，Pro 用户可以预览。
- [2026-02-24 · @GitHub_Daily](#x-2026178278055403843)：`GitNexus`, `代码知识图谱`, `MCP`, `依赖分析`
  - GitNexus 开源：给代码库建知识图谱，通过 MCP 接入 Cursor / Claude Code，让 AI 改代码前先看清调用链。完全本地运行。
- [2026-02-23 · @elvissun](#x-2025920521871716562)：`OpenClaw`, `orchestrator`, `agent swarm`, `one-person dev team`
  - 长文：作者用 OpenClaw 做编排层，编排器 Zoe 负责派生 Codex / Claude Code agent、写 prompt、监控进度、通知合并 PR，日均约 50 个 commit。
- [2026-02-24 · @AYi_AInotes](#x-2026224275192193465)：`OpenClaw`, `AI Orchestrator`, `一人公司`
  - 推荐上面那篇 OpenClaw 文章：单个 agent 的上下文是零和的，真正的杠杆是个人 AI Orchestrator 动态派生专用 agent。
- [2026-02-16 · @openclaw](#x-2023257934017294806)：`OpenClaw 2026.2.15`, `nested sub-agents`, `release`
  - OpenClaw 2026.2.15 发布：Telegram 流式回复、Discord Components v2、嵌套 sub-agent、安全加固。
- [2026-02-14 · @openclaw](#x-2022530044434825310)：`OpenClaw 2026.2.13`, `HuggingFace`, `write-ahead queue`, `release`
  - OpenClaw 2026.2.13 发布：支持 HuggingFace，消息崩溃后可恢复（write-ahead queue），线程功能修好，支持 codex-spark。
- [2026-02-11 · @dabit3](#x-2021387483364151451)：`OpenClaw 架构`, `first principles`, `persistent AI assistant`, `教程`
  - 长文教程：从消息 API 加一个 LLM 出发，一步步推导出 OpenClaw 的架构，讲清常驻 AI 助手是怎么工作的。
- [2026-01-20 · @DavidOndrej1](#x-2013725989952467308)：`Anthropic`, `Claude Code masterclass`, `课程浓缩`
  - 把 Anthropic 7 小时的 Claude Code 课程浓缩成 27 分钟视频。
- [2026-01-19 · @DilumSanjaya](#x-2013293638768562325)：`vibe coding`, `robotics`, `Gemini`, `Nano Banana`
  - Vibe coding 机器人第 7 集：用 Gemini 实现扑翼机构，并用 Nano Banana 生成达芬奇风格的 UI。
- [2026-01-18 · @MatthewBerman](#x-2012701592756383893)：`MIT`, `Recursive Language Models`, `长上下文`, `context in code env`
  - MIT 研究：把上下文从模型里搬到代码环境中，让 1000 万以上 token 的输入成为可能。
- [2026-01-13 · @KKaWSB](#x-2011149280468484157)：`Cursor`, `Opus 4.5`, `landing page`, `AI 设计`
  - Cursor + Opus 4.5 不到 10 分钟就做出带滚动叙事动画的落地页。观点：做得丑是工作流的问题，不是 AI 的问题。
- [2026-01-09 · @KKaWSB](#x-2009518503532089506)：`字节跳动`, `UI-TARS-desktop`, `computer use`, `开源`
  - 字节开源 UI-TARS-desktop：本地运行的桌面自动化 agent，能操作任意桌面应用，不需要联网。
- [2026-01-12 · @ChrisGPT](#x-2010804702313652647)：`Anthropic`, `Cowork`, `Claude`, `新闻`
  - 快讯：Anthropic 推出 Cowork，把 Claude Code 的 agent 能力带给普通用户，可授权访问文件夹并完成多步任务（研究预览）。
- [2026-01-12 · @dair_ai](#x-2010720188686348593)：`SimpleMem`, `agent memory`, `语义无损压缩`, `论文`
  - SimpleMem 论文：用语义无损压缩做 agent 长期记忆，三阶段流水线，在提高信息密度的同时降低 token 消耗。
- [2026-01-12 · @discountifu](#x-2010579279789387929)：`multi-agent`, `trading terminal`, `Textual TUI`, `Python`
  - 周末 vibe 出来的多 agent 交易终端，用 Textual 做 TUI，支持多因子分析。
- [2026-01-11 · @JulianGoldieSEO](#x-2010178642752704850)：`Antigravity`, `免费工具组合`, `MCP`, `Nano Banana`
  - Antigravity 的用法合集：切换免费模型、生成图片、接入 MCP、一键部署到 Netlify。偏营销。
- [2026-01-09 · @0x0SojalSec](#x-2009709579903643768)：`n8n`, `agent templates`, `开源`
  - 开源 42 个 n8n agent 模板（AI Agents A to Z）。
- [2026-01-06 · @james_y_zou](#x-2008576712695836685)：`SleepFM`, `Nature Medicine`, `foundation model`, `医疗 AI`
  - Nature Medicine 论文：SleepFM 用 58.5 万小时的睡眠数据训练基础模型，能从一晚的睡眠记录预测 130 种疾病。

## Part 2 · 原帖

### x-2114629460930740466

**Roc (@AIStarsGo)** · 发帖 2026-10-26 · [原帖](https://x.com/AIStarsGo/status/2114629460930740466)

> 几条教训
>
> 1. 不要依赖 agent 读论文或者高质量博文，
> 后果：思维深度大幅度下降，灵感触发时机大幅度减少，浪费大量的时间去理解 agent 的垃圾表达。
>
> 2. 不要把搞科研/技术学习 和 英语学习混在一起。
> 后果：效率低下，推进缓慢，失去耐心后放弃，灵感和思考都需要时间积累，混合学英语这个目标会大幅度延迟你的思考，让你的脑子在来个任务上来回切换
>
> 3. 不要因为 token 用不完就想着 background 跑点东西，把 token 用掉，不影响你的主线
> 后果：除非你编了稳定的 workflow，否则即时奖励更强的 vibe coding 一定会吸引你的注意力，打断你的深度思考。
>
> 总结，一定要感受自己在 agent 时代下的认知水平的提高速度，到底是加快了，还是不变，还是退步了。如若不然会沉迷于 shallow work，最后认知退化，导致阅读长文字、深度思考都没耐心，人就废了。


### x-2114099234001600931

**smerkzz (@0xsmerkzz)** · 发帖 2026-10-24 · [原帖](https://x.com/0xsmerkzz/status/2114099234001600931)

> holy sh*t . SpaceXAI engineer, Lauren Tan:
>
> "I'm running 35+ GrokBot agents with /loop, /goal, inside pstack. My bots shipping code even when I sleep
>
> at SpaceXAI, 85% of our engineers running 11+ GrokBot agents as a team. I have a Chief of Staff agent, it knows other agents and manages everything"
>
> in a 1-hour workshop, a SpaceXAI engineer revealed how to build a team of GrokBot agents from scratch
>
> worth more than a $800 agentic engineering course
>
> watch today, then read the article on how to build a team of GrokBot agents from scratch

- 含视频（未转写）

### x-2113948384113598588

**Sumanth (@Sumanth_077)** · 发帖 2026-10-24 · [原帖](https://x.com/Sumanth_077/status/2113948384113598588)

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

- 图片：[img1](https://pbs.twimg.com/media/HVZAbCYasAAAe6R?format=png&name=large)

### x-2113634548378374458

**Annatar.md (@AnnatarXBT)** · 发帖 2026-10-23 · [原帖](https://x.com/AnnatarXBT/status/2113634548378374458)

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

### x-2106453816757354947

**Sergii Makarevych (@sermakarevich)** · 发帖 2026-10-03 · [原帖](https://x.com/sermakarevich/status/2106453816757354947)

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

### x-2104453599367770287

**meng shao (@shao__meng)** · 发帖 2026-09-28 · [原帖](https://x.com/shao__meng/status/2104453599367770287)

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

- 引用 meng shao @shao__meng · Sep 27:
  > 斯坦福大学课程 CS329A: Self-Improving AI Agents
  >
  > 课程 9 讲视频都已发布在 Youtube，第 1 讲 52 万观看，第 9 讲 1.5 万。趁假期坚持看完 9 讲视频，你就超过了中间的 50 多万人，和连第 1 讲都没看过的无数人 😂
  >
  > 开玩笑，虽然 AI Agent  x.com/shao__meng/sta…
- 含视频（未转写）

### x-2101308432305254889

**Morty (@0xMortyx)** · 发帖 2026-09-19 · [原帖](https://x.com/0xMortyx/status/2101308432305254889)

> Jev doesn’t make the LLM smarter. it makes 193x faster. 444x cheaperand testable
>
> Jev could be the missing decision layer between LLM reasoning and real-world agent execution.
>
> without a decision layer, you usually solve that with:
>
> more prompting
> → more context
> → more retries
> → more tokens
>
> Jev makes the fork explicit.
>
> for every state:
>
> Choice → which route wins?
> Score → how good is each option?
> Noul → how likely is the condition true?
>
> then execution stays outside the model.
>
> full Jev Engineering breakdown below ↓

- 引用 Ricker @0xRicker · Sep 19:
  > Jev could become the control layer AI agents have been missing.
  >
  > Instead of spending 5–20 seconds and expensive LLM calls deciding every next step, it can route actions in milliseconds at near-zero cost.
  >
  > In this article, I break down how
- 图片：[img1](https://pbs.twimg.com/media/HSlT6boWQAIypkN?format=jpg&name=large)

### x-2083131009986396282

**Khairallah AL-Awady (@eng_khairallah1)** · 发帖 2026-07-31 · [原帖](https://x.com/eng_khairallah1/status/2083131009986396282)

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

### x-2082413202353406091

**The Code Newsletter (@CodeNewsletter)** · 发帖 2026-07-29 · [原帖](https://x.com/CodeNewsletter/status/2082413202353406091)

> Your GitHub stars won't save you if you're behind on AI.
>
> 2026 is the year this gap becomes impossible to close. 
>
> Here's everything you need to master AI and ship code 5X faster.
>
> Join The Code newsletter and get the access

- 链接卡片：[Join 300k+ Devs](https://codenewsletter.ai/subscribe?utm_source=twitter_ads_flal_1_cc_tutorials)
- 图片：[img1](https://pbs.twimg.com/media/HG52YoMaEAAL1Oa?format=jpg&name=large)

### x-2085421662447468758

**Anatoli Kopadze (@AnatoliKopadze)** · 发帖 2026-08-06 · [原帖](https://x.com/AnatoliKopadze/status/2085421662447468758)

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

### x-2079636027736457707

**Carnage (@0xCarnagee)** · 发帖 2026-07-21 · [原帖](https://x.com/0xCarnagee/status/2079636027736457707)

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

### x-2085024744387092973

**Mahax (@Mahaximus_)** · 发帖 2026-08-05 · [原帖](https://x.com/Mahaximus_/status/2085024744387092973)

> 《Agents, Loops, Graphs. Everything You Need to Know in One Place.》
>
> Most people use AI at one speed: ask, read, fix, ask again. It works. It's also the slowest way to do it.
> There is a faster setup. It has three parts: an agent that plans and acts without being walked through each step, a loop that runs until the work actually clears the bar, and a graph of parallel workers that handles what a single prompt never could. Claude runs all three. Most people never find out.
> Not because it's complicated. Because nobody put all three parts in one place.
> By the end of this article you will understand what Claude is actually capable of. What agents, loops, and graphs are, how each one builds on the last, when they are worth using and when they are a trap, and how to build all three yourself with prompts and code you can use today.
>                                     Agents 
> 1 - What an agent actually is
> Asking Claude "summarize this article" is not an agent. That is a chat.
> Telling Claude "find the three most cited papers on this topic, pull the key claims from each, cross-check them against each other, and write me a one-page briefing", and having it do all of that without you touching anything in between, that is an agent.
> The difference is not the model. It is the structure around it.
> An agent has three things a regular chat does not.
> Tools it can call on its own: search, file systems, code execution, external APIs. It does not wait for you to go get the information, it goes and gets it.
> Memory that carries across tasks, not just within one session. It knows what it already tried, what worked, what it decided earlier.
> A loop that keeps running until the task is finished, not until it generates one response. It does not hand the work back to you at every step.
> When all three are in place, Claude stops being something you talk to and starts being something that works
> 2 - The levels of agentic work
> Not everyone needs a fully autonomous agent on day one. The useful thing to know is that there are levels, and each one is already more powerful than what most people run.
> Level 1 - Chat. You ask, Claude answers, the session ends. No tools, no memory, no ongoing goal. You are the engine. Claude is the tool in your hand.
> Level 2 - Claude with tools. When Claude searches the web before answering, reads a file, or runs code to check its work, it is already slightly agentic. You did not tell it to do those things step by step — it decided it needed to.
> Level 3 - Multi step workflows. You give a goal. Claude breaks it into steps, executes each one, checks the result, and delivers a finished output. You are not involved between steps.
> Level 4 - Fully autonomous. The agent runs on a schedule or a trigger, monitors inputs, calls external services, and completes complex tasks without a human in the loop. You set the goal once and check the output.
> The difference between level 1 and level 4 is not a different model. It is what surrounds the model: tools, memory, and a loop. Add one at a time and you move up a level.
> 3 - Three agents you can build today
> The agent type determines the system prompt you give it. Here are three that cover most of what people actually need. Copy the one that fits, adjust the details to your situation, and paste it in as the system prompt.
> Research agent
> You are a research agent. Your job is to find what actually matters, not just what exists.
>
> When given a research task:
> 1. Break it into 3-4 specific sub-questions worth answering
> 2. Search each one independently
> 3. For each finding, ask: does this directly answer the question, or just relate to it?
> 4. Keep only what directly answers. Discard the rest.
> 5. Deliver a structured summary: key findings, the source behind each one, and what you could not find
>
> Rules:
> - Every claim needs a source. No exceptions.
> - If two sources contradict each other, flag it — don't pick a side.
> - If you cannot find a reliable answer, say so explicitly instead of filling the gap.
> Data analysis agent
> You are a data analysis agent. Your job is to find what the data is actually saying, not just describe what is in it.
>
> When given a dataset or numbers:
> 1. Identify what kind of data this is and what questions it can realistically answer
> 2. Look for patterns, outliers, and trends - not averages alone
> 3. For every finding, ask: is this interesting or is this obvious? Cut the obvious.
> 4. Flag anything that looks wrong - missing values, suspicious spikes, inconsistencies
> 5. Deliver findings ranked by importance, not by where they appear in the data
>
> Rules:
> - Never describe what the data contains. Interpret what it means.
> - If a number is surprising, explain why it is surprising.
> - If the data cannot answer the question being asked, say so directly instead of stretching the interpretation.
> - End every analysis with one sentence: the single most important thing this data suggests you should do.
> Code agent
> You are a code agent. Your job is to produce working code, not promising code.
>
> When given a coding task:
> 1. State your understanding of what the code must do before writing anything
> 2. Write the solution with clear comments explaining each section
> 3. Identify edge cases that could break it
> 4. If there are errors, debug them before asking for help
>
> Rules:
> - Write clean code with meaningful variable names
> - Always include error handling
> - If the requirements are unclear, make a reasonable assumption, state it, and continue
> - Never deliver code you have not mentally traced through at least once
>
> When you find a bug: explain what caused it in one sentence, then fix it. Do not just fix it silently.
> 4 - The memory problem and how to fix it
> This is the most common place agents break down, and it happens in three specific ways.
> The task runs too long and the agent loses the beginning. The original goal, the decisions already made, the constraints you set, all of it falls out of the context window. The agent keeps working but has quietly forgotten what it was working toward.
> You close the session and open a new one. The agent starts from zero. Everything from the previous run is gone.
> The agent gets interrupted mid-task. When you come back, it has no record of where it stopped, what it already tried, or what failed.
> All three have the same fix: make the agent write its own memory.
> Paste this mid-task to create a progress record:
> Before we continue, write a checkpoint:
> 1. What have you completed so far?
> 2. What decisions were made and why?
> 3. What still needs to happen?
> 4. What would you need to resume this in a new session?
>
> Keep it under 150 words. Be specific - vague checkpoints are useless.
> Paste this when a session is getting long:
> The conversation is getting long. Compress what matters into a summary:
> 1. The original goal
> 2. What has been done and what was found
> 3. Key decisions made
> 4. What still needs to happen
>
> After writing the summary, continue from there. Treat it as the new starting point.
> Paste this at the start of a new session to restore context:
> We are resuming from a previous session. Here is the context:
>
> [paste your checkpoint here]
>
> Confirm your understanding of where we are, identify the next step, and continue without repeating work already done.
> One more thing worth doing for any agent you run regularly: add the facts it always needs directly into the system prompt. Claude reads the system prompt at the start of every session, so anything there is always in context regardless of how long the conversation runs.
>                                      Loops
> 1 - What a loop actually is
> A prompt hands Claude one instruction and waits for you to decide what happens next. A loop hands Claude a goal and lets it figure out how to get there.
> The difference in practice: a prompt stops when Claude generates something. A loop stops when the task is actually done.
> Every loop runs the same cycle:
> PLAN    -  work out what the task actually requires
> EXECUTE -  do the work
> CHECK   -  measure the result against the goal
> ITERATE -  if it didn't pass, find the weakest part and fix it
> STOP    -  when it passes, or when a hard limit is reached
> Three of those five steps are where most loops either work or fall apart.
> The check is what makes it real. Without a genuine test on the output, you don't have a loop, you have Claude producing drafts and calling them done. The check is what turns repetition into progress. It needs to be something that can actually fail: a test that passes or doesn't, a score that clears a threshold, a rubric with hard criteria. A soft check is no check at all.
> The stop condition is what keeps it from running forever. Every loop needs two ways to stop: the task is done, or a hard limit was hit. "After 8 attempts, stop and report what happened" is not optional, it is the thing that prevents a loop from billing you quietly while it spins on a problem it cannot solve.
> Take any prompt and add three things, a real test that can fail the output, a record of what already ran, and a ceiling on how many tries it gets, and you have a loop. Leave any one out and you have something that looks like a loop and costs like one.
> 2 - Is it actually worth it?
> Most articles sell you the loop before telling you when it is a mistake. Here is the honest version. A loop is worth building only when four things are true at the same time.
> You'll run it again - not eventually, regularly. A task you do once doesn't earn a loop.
> The work can grade itself. There's a check somewhere that doesn't need your eyes - a condition that passes or fails without you.
> You hand it the goal and it hands you the result. If it needs you to step in somewhere in the middle, it is not a loop.
> The finish line is a fact, not a feeling. If deciding whether the output is good enough requires judgment, a loop cannot make that call.
> Miss any one of those four and the loop costs more than it saves.
> The honest version of this: most people do not need the heavy version of a loop yet. What almost everyone can use right now is a self-checking loop, no scheduling, no infrastructure, no cost beyond your normal usage. That is the next section.
> 3 - Build a loop yourself
> You don't need a server, a scheduler, or any special setup to run your first loop. The whole thing fits in a single prompt. Paste this into Claude and replace the brackets.
> Work in a loop until the output clears every criterion below. Do not stop early.
>
> GOAL:
> [describe exactly what you want produced]
>
> CRITERIA — be specific, no soft passes:
> - [what good looks like, measurable]
> - [what good looks like, measurable]
> - [what good looks like, measurable]
>
> EACH PASS:
> 1. DRAFT - produce or improve the work
> 2. SCORE - rate the result 1–10 against each criterion, be harsh
> 3. GAPS - list exactly what is still weak
> 4. CALL - if every score is 8 or above, write DONE and stop.
>    If not, write NEXT PASS and fix the weakest gap first.
>
> RULES:
> - Never call it done until every criterion clears 8.
> - Each pass fixes the single weakest score from the last round.
> - No questions. Make a reasonable assumption, note it, keep going.
> Watch what happens. Claude drafts, scores its own output against your criteria, finds the weakest point, rewrites, and keeps going until it actually clears the bar. Not until it produces something that looks reasonable. Until it passes.
> That is a loop. You built it with one prompt.
> One thing worth noticing: you are still the trigger. You opened the chat, you pasted the prompt. Close the tab and it stops. There is no schedule, no "run this every morning." For that you need the next layer, which is where most people either build the full version or realise they didn't need it.
> 4 - The order that works + the cost
> There is a specific order that keeps loops from breaking in production, and almost everyone skips a step.
> Run it manually first. Before you automate anything, complete the task by hand inside a single conversation. If it doesn't work reliably there, it won't work reliably on a schedule, it will just fail faster and cost more.
> Lock what worked into a reusable template. Save the instructions, the criteria, and the rules as something you can call again without rebuilding. A loop that lives inside one chat dies when the chat closes.
> Add the gate (check) and the stop condition. The check that can fail the output, and the hard limit on how many times it tries. Without both, you don't have a loop, you have an automated way to spend money.
> On cost: loops are not cheap. Every iteration sends the full context back through the model, the goal, the previous output, the score, what failed. That pile grows every pass. A loop that runs ten times doesn't cost ten prompts. It costs ten prompts that keep getting longer.
> The number worth tracking is not total tokens spent. It is how many outputs you actually kept. If a loop runs ten times and you discard six results, you paid for ten to get four. Below a 50% keep rate, the loop costs more than doing it yourself.
>                                    Graphs
> 1 - What a graph actually is
> Not a chart. Not a visualization. A graph in AI work is a map of which jobs need to happen and what each one depends on.
> Two things make up the whole structure: 
> A node is one unit of work. One agent, one task, one defined input and one defined output. Not "research this topic, summarize it, then write a draft." Just one of those. The smaller and more bounded the job, the more useful the node.
> An edge is a dependency. It connects two nodes when the second one genuinely needs what the first produced, not just when one happens to come after the other. That distinction matters more than it sounds.
> Everything else in graph engineering is just applying those two ideas at different scales.
> What makes a node actually usable is a defined output shape. A node that returns free text is only readable by a human. A node with a fixed output is readable by the next node, no human required in the middle.
> JOB: research one competitor's pricing - one task, nothing else
> IN: { competitor: "name", url: "https://..." }
> OUT: { price: number, plan: string, source: url, date: "YYYY-MM-DD" }
> RULE: if the output doesn't match this shape, reject and retry
> That contract is what makes a graph run without you managing every handoff.
> 2 - The fake edge test
> The distinction is between sequence and dependency. Sequence is the order you typed things in. Dependency is when a task genuinely cannot start without something the previous one produced. Sequence you invented. Dependencies already exist, the graph just makes them visible.
> Most workflows have both, and most people never separate them.
> The test takes five minutes on any workflow you already run.
> Write every step as a box. Draw an arrow between each consecutive pair. Then go through every arrow and ask one question: does the data produced by this step actually flow into the next one?
> If yes - keep the arrow. That is a real dependency.
> If no - delete the arrow. Those two steps have nothing to do with each other and can run at the same time.
> Everything with no incoming arrow can start immediately. Everything with no outgoing arrow is a final output.
> You will find two or three fake edges in almost any workflow you draw. Every one of them is time you are handing away for free, tasks sitting in a queue behind work they never actually needed.
> 3 - The Diamond
> Once you start removing fake edges, one shape appears more than any other.
> The work splits into several independent jobs that run at the same time. Those jobs all feed into one final step that pulls their outputs together. Draw it and it looks like a diamond, wide in the middle, narrow at both ends.
> The formal name: fan out, then converge.
> Here is what it looks like in practice. Say you are researching three competitors. The linear version runs them one after another, finish the first, start the second, finish that, start the third. The diamond version runs all three at once and waits only for the slowest one to finish before moving to the synthesis step. Same inputs, same outputs, a fraction of the time.
> The diamond works because of the edge structure. The synthesis step has a real dependency on all three research outputs, those edges exist. But the three research jobs have no dependency on each other, those edges don't. So they run in parallel, and the only wait is at the end, where waiting is unavoidable anyway.
> Two things have to be true for it to hold. The parallel jobs must be genuinely independent, no hidden shared resources, no fake independence. And the convergence step must actually need all of them. If it only needs one, the others are wasted work.
> Here is what the diamond actually looks like:
> # the diamond — one pattern, any job
>
> angles = [
>     "pricing vs the top 3 competitors",
>     "what buyers complain about in reviews",
>     "gaps the market hasn't filled yet",
> ]
>
> # FAN OUT — one worker per angle, all at once
> raw = run_in_parallel([
>     agent(task=f"research: {a}. every claim needs a source and date.")
>     for a in angles
> ])
>
> # REDUCE — plain code, no model, no tokens spent
> findings = deduplicate(filter(None, raw))
>
> # VERIFY — a fresh skeptic per finding, tries to disprove it
> survivors = [
>     f for f, verdict in zip(findings, run_in_parallel([
>         agent(task="try to disprove this. return keep or drop.",
>               input=f,
>               fresh_context=True)
>         for f in findings
>     ]))
>     if verdict == "keep"
> ]
>
> # SYNTHESIZE — one agent writes from what survived
> return agent(task="one report, ranked by confidence, sources attached.",
>              input=survivors)
> 4 - The checker
> The agent that wrote the output is the worst possible judge of it.
> Not because it is dishonest, because it cannot see its own blind spots. The same reasoning that produced the mistake is the reasoning being used to check for it. Every serious study on AI self-review lands on the same finding: models miss most of their own errors.
> So the rule is simple: the agent that does the work never checks the work.
> You put a separate node between your workers and your final step. Its only job is to try to break each finding before it moves forward. Not to improve it, not to summarize it, to find the reason it should be dropped.
> The thing most people miss: that checker needs a completely fresh context.
> Give it the same conversation the worker had and it is not checking anything, it is nodding along to the same chain of reasoning in a different window. A verifier that shares context with the worker it is checking is not a verifier. It is the same agent pretending to be two.
> Split the check three ways. Three different questions, each trying to kill the finding from a different angle.
> VERIFIER NODE
>
> INPUT: the finding only — never the worker's conversation
> CONTEXT: fresh and empty, has not seen the work it is judging
>
> THREE CHECKS, run in parallel:
> 1. Is it correct? Does the claim actually hold up?
> 2. Is it current? Is the source recent, not something stale?
> 3. Is the source real? Does the link resolve to what it claims?
>
> PASS: keep the finding if the majority of checks clear
> FAIL: drop it before it reaches the final step
> The rule worth remembering: a worker and its checker must never share a context. The moment they do, you are back to one agent grading its own homework, just with a bigger bill
> 5 - Build one yourself
> Everything above is still a mental model until you give Claude something it can run. This is where it becomes practical.
> One word changes how Claude processes your instructions: workflow.
> Without it, Claude reads your prompt as a sequence and executes each step one after another. With it, Claude writes a short coordination script, identifies which nodes have no dependencies, and runs those in parallel automatically. You describe the graph. Claude figures out the execution order.
> Here are three you can paste directly into Claude Code and adapt. Replace anything in brackets. The structure stays the same regardless of what you put inside the nodes.
> Competitive research:
> workflow: competitive-research
>
> nodes:
>   research_a:
>     task: "Research [Company A]. Cover pricing, core features,
>            recent changes, public sentiment. Output a structured summary."
>     output: company_a.md
>
>   research_b:
>     task: "Research [Company B]. Cover pricing, core features,
>            recent changes, public sentiment. Output a structured summary."
>     output: company_b.md
>
>   research_c:
>     task: "Research [Company C]. Cover pricing, core features,
>            recent changes, public sentiment. Output a structured summary."
>     output: company_c.md
>
>   checker:
>     task: "Review all three summaries. Flag anything incomplete,
>            outdated, or off-topic."
>     depends_on: [research_a, research_b, research_c]
>     output: checker.md
>
>   synthesize:
>     task: "Using the summaries and checker report, write a comparison
>            across price, features, and positioning."
>     depends_on: [checker]
>     output: comparison.md
> Multi-file code review:
> workflow: code-review
>
> nodes:
>   review_auth:
>     task: "Review auth.py for security issues, edge cases,
>            and code quality. Be specific."
>     output: review_auth.md
>
>   review_api:
>     task: "Review api.py for security issues, edge cases,
>            and code quality. Be specific."
>     output: review_api.md
>
>   review_db:
>     task: "Review db.py for security issues, edge cases,
>            and code quality. Be specific."
>     output: review_db.md
>
>   checker:
>     task: "Read all three reviews. Flag issues appearing in more than
>            one file. Note cross-file dependencies that could cause problems."
>     depends_on: [review_auth, review_api, review_db]
>     output: checker.md
>
>   summary:
>     task: "Write a prioritized fix list — critical first,
>            then medium, then low."
>     depends_on: [checker]
>     output: final_review.md
> The depends_on line is the only thing you need to understand to design any graph. No dependencies means parallel. A dependency means wait.
>                      What you now have
> Three concepts, one model. 
> An agent gives Claude a goal instead of an instruction and lets it work toward it on its own. 
> A loop makes that work reliable, it checks itself, records what failed, and keeps going until it actually clears the bar. 
> A graph makes it fast, parallel workers, independent jobs running at the same time, converging into one answer at the end. 
> Each one builds on the last. You do not need all three for every task. But once you can see which one a task needs, you stop working harder and start designing better.

- 图片：[img1](https://pbs.twimg.com/media/HO5t8UXWsAAJrRf?format=jpg&name=large) [img2](https://pbs.twimg.com/media/HO5hp7fXQAAmVK8?format=jpg&name=large) [img3](https://pbs.twimg.com/media/HO5hPC9XgAAwRF2?format=jpg&name=large) [img4](https://pbs.twimg.com/media/HO5guyAW0AEJC9C?format=jpg&name=large)

### x-2083602508807569560

**codila (@0xCodila)** · 发帖 2026-08-01 · [原帖](https://x.com/0xCodila/status/2083602508807569560)

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

### x-2071649423042412597

**Anatoli Kopadze (@AnatoliKopadze)** · 发帖 2026-06-29 · [原帖](https://x.com/AnatoliKopadze/status/2071649423042412597)

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

### x-2071214176526049739

**Movez (@0xMovez)** · 发帖 2026-06-28 · [原帖](https://x.com/0xMovez/status/2071214176526049739)

> Ex-Google engineer explained AI agent loops, harness, evals in 20 minutes - better than 500$ courses.
>
> trace every run → judge it with an LLM → diagnose → fix → ship.
>
> That loop is how agents self-improve over time.
>
> Agent loops + memory + harness  + evals - thats the stack. 
>
> Watch it, then save the framework below.

- 含视频（未转写）

### x-2069734857626833371

**gxjo (@gxjo_dev)** · 发帖 2026-06-24 · [原帖](https://x.com/gxjo_dev/status/2069734857626833371)

> Somebody built traffic lights for Claude Code 😭

- 图片：[img1](https://pbs.twimg.com/media/HLks4Q_X0AAKXK2?format=jpg&name=large)

### x-2068763235587694769

**Movez (@0xMovez)** · 发帖 2026-06-21 · [原帖](https://x.com/0xMovez/status/2068763235587694769)

> Andrew Ng:
>
> "100% of my tasks are now done by AI agents - hype has exceeded my expectations. Loops is next step.
>
> in 3-6 months, everyone will be using self-improving loops. No more prompting."
>
> In a 30-minute talk, Andrew Ng explains how to build self-improving agentic systems from scratch.
>
> Worth more than a $500 agentic course.

- 含视频（未转写）

### x-2068325550603559402

**GREG ISENBERG (@gregisenberg)** · 发帖 2026-06-20 · [原帖](https://x.com/gregisenberg/status/2068325550603559402)

> The most valuable skill sets on the planet right now:
>
> 1. people who can set up agents properly, manage them, and run local AI models
> 2. marketers who know how to build distribution
> 3. robotics engineers who can do all three: build the hardware, wire in the AI, and source manufacturing etc
> 4. curators who are good at yapping and can do short form video in their sleep
> 5. the builder-distributor. The one person who can both ship the product AND get it in front of people
> 6. IRL community builders


### x-2066827221537333611

**Khairallah AL-Awady (@eng_khairallah1)** · 发帖 2026-06-16 · [原帖](https://x.com/eng_khairallah1/status/2066827221537333611)

> Anthropic pays $750,000+ a year for engineers who can build LLMs from scratch.
>
> Not how to prompt them.
> Not how to fine-tune them.
> Not how to build RAG pipelines.
>
> But how to build them from scratch.
>
> This 2-hour Stanford lecture teaches you everything.
>
> Scaling laws.
> Data collection.
> Architecture design.
> Post-training alignment.
>
> Free. From Stanford.
>
> Watch first. Then read this.
>
> The lecture is the theory.
>
> full guide in the article below

- 含视频（未转写）

### x-2063985608381362576

**Anatoli Kopadze (@AnatoliKopadze)** · 发帖 2026-06-08 · [原帖](https://x.com/AnatoliKopadze/status/2063985608381362576)

> 《AI Agents. What they are and how to Build Your Own Step by Step.》
>
> Everyone is talking about AI agents. But if you ask most people what an agent actually is, you get a vague answer about "AI that does things autonomously."
> The real picture is more useful than that. Agents are not a category. They are a spectrum.
> This guide explains where on that spectrum different AI tools sit, what separates a basic LLM interaction from a true agentic workflow, and how to build your own agent with Claude Code and connect it to Telegram, without writing code yourself.
> Before we get into it, follow me on X and join my Telegram channel I just created where I post more AI content every day. Both are free.
> X - https://x.com/AnatoliKopadze
> Telegram - https://t.me/kopadzemp
> What Makes Something an Agent
> Asking Claude "what should I post today?" is not an agent. That is a chat.
>
> Telling Claude "find the three topics trending in AI right now, pick the one with the most engagement potential, draft a post in my style, and save it to a file" and having it do all of that without you touching anything, that is an agent.
>
> The difference is not the model. It is the structure around it.
>
> An agent has three things a regular chat does not. Tools it can call on its own: search, file systems, code execution, external APIs. Memory that persists across tasks, not just within one session. And a loop that keeps running until the task is finished, not until it generates one response.
>
> The more of those three things you add, the less you are involved. That is the idea.
> The Spectrum: From Chat to Agent
> At one end you have a basic chat. You ask, Claude answers, the session ends. No tools, no ongoing goal, no ability to act in the world.  
>
> One step up: Claude with tools enabled. When Claude searches the web before answering, reads an attached file, or generates an image, it is already slightly agentic. You did not tell it to do those things step by step, it decided on its own that it needed to.  
>
> Further up: multi-step workflows. You give a goal, Claude breaks it into steps, executes each one, checks the result, and delivers a finished output. You are not involved between steps.  
>
> At the top: fully autonomous agents. The agent runs on a schedule, monitors inputs, calls external services, and completes complex tasks without a human in the loop. You set the goal once and check the output.  
>
> The difference between the bottom and the top is not a different model. It is what surrounds the model, tools it can call, memory that carries context, and a loop that keeps running until the task is done.
> Types of Agents You Can Build Today
> To give you a sense of what agents can actually look like today, I put together a few examples below. These are not limits you can build whatever fits your specific situation.
>
> Research agent: gathers information on a topic, reads multiple sources, pulls out what matters, and delivers a structured summary. You give it a question. It gives you an answer that would have taken hours to compile manually.
> Writing agent: writes content according to a system you define. Give it your tone, format, audience, and topic. It handles drafts, rewrites, and edits without you managing every sentence.
> Code agent: writes code, runs it, reads the errors, fixes them, and keeps going. You describe what the code should do. The agent handles the implementation and debugging loop.
> Business agent: Handles repetitive business tasks: drafting emails, processing customer requests, qualifying leads, generating reports. Runs on autopilot once you define the rules.
> Personal agent: Manages your schedule, organizes tasks, prepares briefings, and handles the planning work you do manually every day.
> Building Your First Agent - Start Here
> You will use Claude Code to build a Telegram bot that runs on a remote server and uses Claude as its brain. Claude Code writes all the code for you, you just describe what you want in plain English. Once it is set up, all communication with the bot happens directly through Telegram.
>
> The whole setup takes about 10-20 minutes. You do not need to know how to code.
> System Prompt Templates - Paste Into Prompt 2
> When you run Prompt 2 from the setup below, you need to describe what kind of agent you want. These are ready-made templates, copy the one that fits, paste it into Prompt 2 where it says "The agent should be:", and Claude Code will build that specific agent. Adjust any details to match your situation.
> Research Agent
> You are a research agent. Your job is to gather, analyze, and synthesize information on any topic I give you.
>
> When given a research task:
> 1. Identify the 3-5 most important sub-questions to answer
> 2. Search for information on each one
> 3. Evaluate the quality and relevance of each source
> 4. Extract only what directly answers the question
> 5. Deliver a structured summary with: key findings, supporting evidence, and gaps you could not fill
>
> Format: Use headers, bullet points, and clear sections.
> If you are uncertain about something, say so explicitly.
> Do not add filler. Every sentence should contain information.
> Writing Agent
> You are a writing agent. You write content in my voice and style.
>
> My style:
> - Conversational, direct, no corporate language
> - Short sentences and paragraphs
> - Specific numbers and examples over vague claims
> - Always end with something the reader should do or think about
>
> When given a writing task:
> 1. Ask for the topic, audience, and desired length if not provided
> 2. Write a first draft
> 3. Review it against my style rules
> 4. Deliver the final version ready to publish
>
> Never add unnecessary introductions. Start with the most important point.
> Code Agent
> You are a code agent. Your job is to write, debug, and improve code.
>
> When given a coding task:
> 1. Confirm your understanding of what the code should do
> 2. Write the solution with clear comments
> 3. Identify any edge cases or potential failures
> 4. If there are errors, debug them systematically before asking for help
>
> Rules:
> - Write clean, readable code with meaningful variable names
> - Always include error handling
> - Explain what each major section does in plain language
> - If you are unsure about requirements, ask one clarifying question before proceeding
> Business Email Agent
> You are a business email agent. You write professional emails on my behalf.
>
> My communication style:
> - Direct and respectful
> - No unnecessary formalities
> - Gets to the point in the first sentence
> - Closes with a clear next step
>
> When given an email task:
> 1. Identify the goal of the email (inform, request, follow up, confirm)
> 2. Write a subject line that reflects the email's purpose
> 3. Draft the email in 3-5 short paragraphs maximum
> 4. End with one clear action item or next step
>
> Always write ready-to-send emails, not templates with blanks to fill in.
> Personal Planning Agent
> You are my personal planning agent. You help me organize my work, prioritize tasks, and plan my week.
>
> When I share my tasks or goals:
> 1. Identify what is urgent vs. important
> 2. Suggest a realistic sequence based on dependencies
> 3. Estimate time required for each task
> 4. Flag anything that could be delegated or eliminated
>
> When I describe a project:
> - Break it into concrete next actions
> - Identify the single most important thing to do first
> - Create a simple checklist I can follow
>
> Keep everything practical. No motivational filler. Just the plan.
> What you need before starting
> 1 - a Claude API key from console.anthropic.com. This is a developer key, you pay per usage, not a fixed monthly fee. For a personal bot sending 50 messages a day, the cost is $1-5 per month depending on which model you choose. 
>
> 2- a Telegram bot token from BotFather. 
>
> 3 - a VPS running Linux. For a personal Telegram bot you do not need anything powerful - 1 CPU, 1GB RAM, and 20GB of storage is more than enough. Any basic plan from DigitalOcean, Hetzner, or Vultr will work, and costs around $4 to $6 per month. Once you have the server, install Claude Code by running npm i -g @anthropic-ai/claude-code in your terminal.
> Which Claude model to use for your bot and what it actually costs:
> For most personal bots Sonnet 4.6 is the right choice, strong enough for any task and affordable for daily use. Use Haiku 4.5 if you want to minimize cost. Opus 4.8 only makes sense for a complex analytical agent where answer quality is critical.
> Building Your First Agent - Step 1 
> Open your VPS terminal and launch Claude Code. Paste this prompt and let it build everything.
>
> Give the agent a personality
> Build me a Telegram bot that uses the Claude API as its brain.
>
> Requirements:
> - Language: Python
> - Library for Telegram: python-telegram-bot
> - Claude model: claude-sonnet-4-6
> - The bot receives a message, sends it to Claude API, and returns Claude's response to Telegram
> - Maintain conversation history per user — each user has their own context within the session
> - Add a /start command that introduces the bot
> - Add a /clear command that resets conversation history for that user
>
> Create all necessary files: main bot file, requirements.txt, and a .env file template for API keys.
> Do not hardcode any API keys — read them from environment variables.
> Deploy as a background service
> Create a systemd service file so this bot runs automatically on my Linux VPS and restarts if it crashes.
>
> The service should:
> - Start automatically when the server boots
> - Restart automatically if it crashes
> - Load environment variables from the .env file in the project folder
> - Save logs to a file I can check later
>
> Also write me the exact terminal commands to install the service, start it, check if it is running, and view the logs.
> Add persistent memory between sessions
> The bot loses conversation history when it restarts. Fix this.
>
> Save each user's conversation history to a JSON file on disk after every message. Load it back automatically when the bot starts.
>
> Add a maximum history length — keep only the last 20 messages per user so the context window never gets too long.
> Adding Skills to Your Claude Code Bot
> Skills are capabilities you add to your bot over time. Each one is a new prompt you give Claude Code, and it writes the code to make it work. Here are the most useful ones.
> Skill: Web search
> Your agent can look up real-time information instead of answering from memory only.
> Add web search capability to the bot using the Tavily API.
>
> When the user asks something that requires current information — news, prices, recent events — the bot automatically searches the web and includes the results in its response.
>
> The bot should decide on its own when to search and when to answer from memory. Add TAVILY_API_KEY to the .env file template.
>
> Use Claude's tool use feature to implement this cleanly.
>
> Skill: Save notes
> Your agent can save anything you tell it to a file - ideas, tasks, research findings and retrieve them later.
> Add a note-saving feature to the bot.
>
> When the user says "save this", "remember this", or "note:", the bot saves the content to a notes.txt file with a timestamp.
>
> Add a /notes command that returns the last 10 saved notes.
> Add a /clearnotes command that deletes all saved notes.
> Skill: Restrict to your account only
> By default anyone who finds your bot can use it and consume your API credits. This locks it to just you.
> Add user restriction to the bot so only I can use it.
>
> Add my Telegram user ID to the .env file as ALLOWED_USER_ID.
> If anyone else messages the bot, it responds with "This bot is private." and ignores all further messages from that user.
>
> Also add how I can find my own Telegram user ID — either through the bot itself or another method.
> Skill: Track API costs
> Claude API charges per token. This adds a simple cost tracker so you always know what you are spending.
> Add basic cost tracking to the bot.
>
> After each Claude API response, log the number of input tokens and output tokens used.
> Keep a running total in a costs.json file.
>
> Add a /costs command that shows: total tokens used today, total tokens used all time, and an estimated cost in USD based on claude-sonnet-4-6 pricing.
> Skill: Scheduled daily briefing
> The agent sends you a message every morning without you having to ask.
> Add a scheduled daily briefing to the bot.
>
> Every day at 8:00am, the bot sends me a message with:
> 1. A motivational one-liner (short, not cheesy)
> 2. A reminder to check my top priority for the day
> 3. One random useful fact about productivity or AI
>
> Send it to my Telegram user ID from the .env file.
> Use the schedule or APScheduler library to implement this.
> Useful Things to Know After Setup
> How to update your agent's personality. Open the main bot file, find the system prompt variable at the top, change it, save the file, and restart the service with sudo systemctl restart your-bot-name. The new personality is live immediately.
> How to check if the bot is running. Run sudo systemctl status your-bot-name in your terminal. If it says "active (running)" it is working. If it says "failed" check the logs.
> How to read logs. Run journalctl -u your-bot-name -n 50 to see the last 50 lines. This is where you find error messages if something breaks.
> How to add a new skill. Open Claude Code in your project folder and describe what you want: "Add X feature to the bot." Claude Code reads your existing code, adds the new feature cleanly, and tells you if a restart is needed.
> The Memory Problem Every Agent Has
> This is the most common problem people run into. The agent loses context between sessions, across long tasks, after too many messages and starts making mistakes or repeating work it already did.
> There are three ways this happens: 
>
> Long tasks eventually exceed Claude's context limit, and the agent starts losing the beginning of the conversation: the original goal, decisions already made, constraints you set.
>
> When you close a session and open a new one, the agent starts from zero. - 
>
> If the agent is interrupted mid-task, it has no way to know where it stopped.
> Four things can fix this:
>
> Tell the agent to write a progress note after every major step: what was done, what was decided, what still needs to happen. Paste that note at the start of the next session to restore full context.
>
> Every ten to fifteen messages, ask the agent to summarize where it is. This forces it to compress context before it overflows.
>
> Before the conversation gets too long, ask the agent to compress everything into a short summary and continue from there. The thread stays intact.
>
> Add the key facts your agent always needs directly to the system prompt in your bot code. Claude reads this at the start of every conversation, so that information is always in context no matter how long things get.
> Checkpoint Prompt
> Before we continue, write a brief checkpoint:
> 1. What have you completed so far?
> 2. What are the key decisions or findings from this session?
> 3. What still needs to be done?
> 4. What context would you need to continue this task in a new session?
>
> Keep it under 200 words.
> Memory File Prompt
> After completing each major step, write a memory note in this format:
>
> STEP COMPLETED: [what was done]
> KEY DECISIONS: [choices made and why]
> CURRENT STATE: [where the task stands now]
> NEXT STEP: [what should happen next]
>
> This note will be used to resume the task in a new session without losing context.
> Context Recovery Prompt
> We are resuming a task from a previous session. Here is the context:
>
> [paste your memory note here]
>
> Based on this:
> 1. Confirm your understanding of where we are
> 2. Identify the next step
> 3. Ask any questions needed to continue
>
> Do not repeat work that has already been completed.
> Rolling Summary Prompt
> The conversation is getting long. Compress everything important into a summary:
>
> 1. Original goal
> 2. What has been done and what was found
> 3. Key decisions made
> 4. What still needs to happen
>
> After writing the summary, continue from there. Treat this summary as the new starting point.
> You now know what agents are, what they can do, and how to build one yourself. I hope this was useful.
> If you want to stay up to date with everything happening in AI, follow me on X and Telegram.
>
> X - https://x.com/AnatoliKopadze
> Telegram - https://t.me/kopadzemp

- 图片：[img1](https://pbs.twimg.com/media/HKS0qaGXoAAElVM?format=jpg&name=large) [img2](https://pbs.twimg.com/media/HKSnn-sXEAAL9fu?format=jpg&name=large)

### x-2066867539305459732

**Codez (@0xCodez)** · 发帖 2026-06-16 · [原帖](https://x.com/0xCodez/status/2066867539305459732)

> 《Agent harness engineering with Claude: 14-step roadmap from one agent to a self-improving system.》
>
> Everyone’s talking about loops. Almost no one is talking about what the loop runs on. 9 out of 10 builders run Claude Code on the default harness - no rules, no subagents, no hooks, no memory.
> Then they wonder why their loop produces slop. The truth is simple: a loop is only as good as the harness underneath it. This is the 14-step roadmap to the harness - from one agent to a system that improves itself.
> Follow my Substack to get fresh AI alpha: movez.substack.com
> Loop engineering - building a system that prompts your agent on a schedule - got all the attention this month. But Addy Osmani, who wrote the long-form piece on loops, was careful to point at what sits below it:
> “Loop engineering sits one floor above the harness. The harness is the environment one single agent runs inside. The loop is the harness, but it runs on a timer, spawns helpers, and feeds itself.”
> Harness engineering is designing that environment: the model, the tools, the permissions, the context, the memory. 
> It’s the unglamorous layer - and it’s the one that decides whether everything above it works. A great loop on a bad harness is a fast way to produce garbage at scale.
> 14 steps. 3 tiers. The foundation everything else stands on.
>
>
> Part 1 · what Harness is
> 01. A harness is the environment one agent runs inside.
> Strip away the jargon and a harness is four things: the model doing the thinking, the tools it can reach, the permissions on those tools, and the context it reads at the start of every run.
> That’s the whole surface. Everything else - subagents, hooks, memory - is a way of shaping one of those four.
> The reason harness matters more than people think: the agent is a while True loop that picks a tool, runs it, looks at the result, and decides the next move. 
> The harness defines what tools exist, what the agent is allowed to do, and what it knows when it starts. Same model, different harness, completely different agent.
>
>
> 02. The whole harness lives in one folder. .claude/
> Everything that shapes your agent sits in a single directory at your project root. Learn this layout and you can read anyone’s harness at a glance:
> python
> .claude/
> ├─ CLAUDE.md          # standing facts — read every session
> ├─ settings.json      # permissions, model, hooks
> ├─ .mcp.json          # external tool connections
> ├─ rules/             # path-scoped behaviors
> │  ├─ tests.md
> │  └─ python-types.md
> ├─ agents/            # subagent definitions (~30 lines each)
> │  ├─ reviewer.md
> │  └─ eval-runner.md
> ├─ skills/            # reusable workflows
> │  └─ pr-checklist/
> │     └─ SKILL.md
> └─ agent-memory/      # what survives between runs
>    └─ STATE.md
> One rule that separates a clean harness from a mess: keep it small enough that you can explain why every file exists. If you can’t say what a rule, hook, or subagent is for, delete it.
>
>
> 03. Harness vs loop vs system. Three floors, don’t mix them.
> Most “my agent setup is a mess” problems come from confusing the three floors. Keep them straight:
> The harness is the runtime one agent lives in. Static configuration: model, tools, permissions, context. This issue.
> The loop prompts the agent on a timer, spawns helpers, feeds itself. It runs on top of the harness.
> The self-improving system is a loop plus memory that compounds - every run leaves the next run sharper.
> The practical version: put standing facts in context, enforcement in hooks, procedures in skills, and isolation in subagents. 
> Mixing these up - enforcement in CLAUDE.md, procedures bloating context - is the root cause of inconsistent, expensive agents.
>
>
> 04. The default harness. What you get out of the box.
> Install Claude Code, open a folder, and you already have a harness - just an empty one. The default gives you a capable model, the built-in tools (read, write, bash, search), and approval prompts on everything risky. No project context, no custom subagents, no memory.
> For a one-off task, the default is fine. For anything you do more than once, the default leaves the agent re-deriving your project from scratch every session, asking permission for safe operations, and forgetting everything when you close the terminal. 
> The next ten steps are about closing that gap.
>
>
> 05. CLAUDE.md: standing facts, kept short.
> CLAUDE.md is read at the start of every session. It’s the agent’s standing knowledge of your project - conventions, architecture, the “we don’t do it this way because of that incident.” 
> The single most common mistake: letting it grow into a giant procedures document that bloats every session.
> The rule from practitioners running this daily: keep the main memory file under ~500 tokens. Standing facts go here. 
> Multi-step procedures go in skills (step 8). Path-specific behaviors go in rules/ files scoped to where they apply. If a section of CLAUDE.md has become a procedure rather than a fact, it belongs somewhere else.
> Read your CLAUDE.md out loud. Every line should be a fact the agent needs in every session (“we use pnpm, not npm”). If a line is a procedure (“to add a feature, first…”), move it to a skill. 
> If it’s a rule for one folder, move it to rules/.
>
>
> 06. settings.json: permissions and model, set once.
> The default harness asks before every risky action. That’s right when you’re watching and wrong when you’re not. settings.json is where you pre-approve the safe stuff, deny the dangerous stuff, and pick which model runs.
> python
> {
>   "model": "claude-sonnet-4-6",
>   "permissions": {
>     "autoApprove": [
>       "Read(*)", "Grep(*)",
>       "Bash(npm test)", "Bash(git status)"
>     ],
>     "deny": [
>       "Bash(rm -rf*)", "Bash(git push*)",
>       "Edit(.env*)", "Edit(secrets/*)"
>     ]
>   }
> }
> The test for what to auto-approve: if this goes wrong, how hard is it to undo? Cheap to undo → auto-approve. 
> Expensive to undo (force-push, deleting files, touching secrets) → always deny or prompt. The middle ground is fine to auto-approve if you log it.
>
>
> 07. Subagents: isolated context for the dirty work.
> A subagent is an independent Claude session launched from the main one - its own context window, its own tool list. The point isn’t parallelism for its own sake. It’s keeping noise out of the main context. 
> A research task that reads 40 files, a review pass that needs a fresh perspective, an eval run that produces a wall of logs - those belong in a subagent so they don’t pollute the main thread.
> GIF
> The most valuable subagent in any harness is the one that checks work the main agent did. A model reviewing its own output is too easy on itself;
> A separate reviewer with a fresh context window catches what the writer talked itself into. This is the writer-vs-checker split that makes every loop above the harness trustworthy.
>
>
> 08. Skills: procedures the agent reuses.
> A Skill is a SKILL.md file the agent runs - either when you call it with /skill-name or automatically when the task matches its description. 
> Unlike a subagent, it runs in the same context window. It’s just reusable instructions that become part of the session.
> The trigger to create one: you notice yourself pasting the same instructions into every new conversation. That’s a skill waiting to happen. A PR checklist, an eval procedure, a release process - written once, invoked forever.
> And because skills are the reusable unit, they’re what makes the harness improve over time: each time the procedure fails in a new way, you add the lesson to the skill, and the next run inherits it.
>
>
> 09. Hooks: deterministic rules the model can’t hallucinate.
> Everything so far depends on the model understanding your instructions. Hooks don’t. 
> A hook is a shell command that fires at a fixed point in the agent lifecycle - before a tool runs, after a file changes, when the session ends- and its exit code can block the action. Hooks are enforcement, CLAUDE.md is suggestion.
> Two hooks earn their place in almost every harness:
> A PreToolUse gate that blocks dangerous commands deterministically — rm -rf, reading .env, pushing to main. Exit code 2 stops the call before it happens. The model can’t talk its way past it.
> A PostToolUse formatter that runs your linter or formatter after every edit. The agent never ships unformatted code because the harness formats it automatically.
> python
> "hooks": {
>   "PreToolUse": [{
>     "matcher": "Bash",
>     "command": "./.claude/hooks/block-dangerous.sh"
>     // exit 2 = block the call before it runs
>   }],
>   "PostToolUse": [{
>     "matcher": "Edit|Write",
>     "command": "prettier --write \"$CLAUDE_FILE_PATH\""
>   }]
> }
> Use hooks for anything that must happen or must never happen - safety, formatting, audit logging. 
> Don’t use them for judgment calls; that’s what the model is for. A good harness has one or two sharp hooks, not twenty.
>
>
> Part 3 · make It Compound
> 10. Add a loop. Now the harness runs on a timer.
> A configured harness still waits for you to type. A loop makes it run on its own. The simplest version is /loop in Claude Code - a recurring prompt on a cadence. 
> Pair it with /goal and the loop keeps going until an objective condition is true, checked by an independent grader rather than the agent grading itself.
> python
> > /loop 30m /goal All tests pass and lint is clean.
>   Triage new failures, draft fixes in claude/ branches.
>
> ▲ Claude uses the harness you built:
>   - rules/ for conventions
>   - reviewer subagent to check each fix
>   - PreToolUse hook blocks pushes to main
> ✓ Looping. Independent grader decides “done.”
> Notice what just happened: the loop didn’t add intelligence. It re-used everything in the harness - the rules, the reviewer subagent, the safety hook. A good harness makes a loop trivial. That’s the whole point of building the foundation first.
>
>
> 11. Add dynamic workflows. The harness writes its own orchestration.
> For tasks too complex for a single loop - massively parallel, highly structured, adversaria- Claude can write its own JavaScript harness on the fly. 
> That’s a dynamic workflow: agent() to spawn, parallel() to fan out, pipeline() to stream. It composes the subagents your harness defines into patterns like fan-out-and-synthesize or adversarial verification.
> The connection to harness engineering: a dynamic workflow is only as good as the subagents and skills it can call. 
> If your harness has a sharp reviewer subagent and a well-written eval skill, the workflow has good pieces to orchestrate. If the harness is empty, the workflow has nothing to work with. 
> The workflow is the conductor, your harness is the orchestra. 
>
>
> 12. Add memory. What the agent forgets, the harness remembers.
> This is the step that turns a configured harness into a system that actually improves. The agent forgets everything between runs. The harness doesn’t have to. 
> A state file - a markdown file in agent-memory/, or a Linear board - records what was tried, what worked, what failed, what rules survived.
> The pattern that makes memory compound, drawn from how the strongest agents use it:
> Write before walking away. Every run ends by updating the state file - lessons learned, verified facts, what’s next.
> Read at the start. Every run begins by reading the state file and relevant skills, so it resumes instead of restarting.
> Distill into skills. When a lesson is general (“Windows runners need bash, not PowerShell”), it graduates from the state file into a skill, where it applies to every future project.
> python
> # Project memory
>
> ## Verified facts # stop guessing about these
> - prc is in dollars, not cents (checked via SELECT MIN/MAX)
> - auth middleware order: rate_limit -> jwt -> rbac
>
> ## Lessons learned # distill the general ones into skills
> - Windows CI runners fail TLS 1.2 in PowerShell — use bash
> - Migrations on tables >1M rows must batch in 10k chunks
>
> ## Last session # resume, don’t restart
> 2026-06-11 · 3 fixes merged, 2 escalated. Next: verify rate-limit fix.
>
>
> 13. Close the loop. Output → lesson → skill → better output.
> Here’s where the three floors lock together into something that improves itself. Each run produces output. The reviewer subagent (step 7) checks it. 
> The result - what passed, what failed, what was learned - gets written to memory (step 12). The general lessons get distilled into skills (step 8). 
> The next run inherits sharper skills and richer memory.
> That’s the whole self-improving loop, and notice it’s built entirely from harness parts:
> Subagent grades the work - objective check, fresh context.
> Memory records the verdict - survives between runs.
> Skills a runs it again - now with everything the last run learned.
> The loop runs it again - now with everything the last run learned.
> The model never changed. The harness around it got sharper. That’s what “self-improving” honestly means - not a model that learns, but a harness that accumulates.
>
>
> 14. Ship the harness. Package it. Share it. Reuse it.
> A harness that works on one project is an asset. 
> Bundle the skills, subagents, and rules into a plugin and your whole team installs the same setup in one step - same conventions, same safety hooks, same reviewer. 
> The harness stops being your personal setup and becomes shared infrastructure.
> The order to build, one last time, because order is the lesson: get one manual run reliable on a clean harness. 
> Add the context and permissions. Add a reviewer subagent. Add memory. Then  and only then wrap it in a loop. A loop on a good harness compounds. A loop on a bad harness just bleeds faster.
>
>
> § The harness mistakes that make every loop worse
> Running on the default. No context, no rules, no memory - the agent re-derives your project every session.
> A bloated CLAUDE.md. Procedures stuffed into standing context, bloating every run. Move them to skills.
> Enforcement in CLAUDE.md instead of hooks. The model can ignore a suggestion. It can’t ignore a hook that exits 2.
> One agent writing and grading its own work. Add a reviewer subagent with a fresh context window.
> No memory. Every run restarts from zero. The state file is what makes tomorrow resume.
> Wrapping a loop around a bad harness. The loop just produces slop faster. Build the foundation first.
> Twenty hooks. One or two sharp ones beat a pile nobody understands.
> Shipping a harness without scanning it. Leaked secrets and over-broad permissions spread to everyone who installs it.
>
>
> Conclusion: 
> The loop gets the glory. The harness does the work.
> Loop engineering is the exciting part - the agent prompting itself, running while you sleep. But a loop is just a harness on a timer. 
> Everything that decides whether the output is good or garbage lives one floor down, in the model you picked, the tools you allowed, the context you wrote, the reviewer you added, the memory you kept.
> Build that floor well and everything above it compounds: the loop re-uses your subagents, the workflow orchestrates your skills, the memory makes each run sharper than the last. 
> Self-improvement was never a property of the model. It’s a property of the harness you build around it.
> Pick one thing you’re not doing - probably a reviewer subagent, a safety hook, or a state file — and add it today. Keep the harness small enough to explain. Then put a loop on top, and watch the foundation do the work.

- 图片：[img1](https://pbs.twimg.com/media/HK76bIrX0AAnTdk?format=jpg&name=large) [img2](https://pbs.twimg.com/media/HK7ibrqWQAAUsd1?format=png&name=large) [img3](https://pbs.twimg.com/media/HK7jHWqXMAAi6sq?format=png&name=large) [img4](https://pbs.twimg.com/media/HK7kUzmWMAAb5GK?format=jpg&name=large) [img5](https://pbs.twimg.com/media/HK7tZ_EXYAA2pLb?format=png&name=large) [img6](https://pbs.twimg.com/media/HK7u0eHWYAEFfJk?format=jpg&name=large) [img7](https://pbs.twimg.com/media/HK7wfs1XQAA2nvW?format=jpg&name=large) [img8](https://pbs.twimg.com/media/HK7xHsDXsAAjaCv?format=jpg&name=large) [img9](https://pbs.twimg.com/media/HK7x3lgWAAAokpJ?format=jpg&name=large) [img10](https://pbs.twimg.com/media/HK7yLY4XMAA9831?format=jpg&name=large) [img11](https://pbs.twimg.com/media/HK70cTeWkAA7m0E?format=png&name=large)
- 含视频（未转写）

### x-2052480800004956323

**OpenAI (@OpenAI)** · 发帖 2026-05-07 · [原帖](https://x.com/OpenAI/status/2052480800004956323)

> Codex now works directly in Chrome on macOS and Windows.
>
> It’s even better at working with apps and sites in Chrome, and now works in parallel across tabs in the background without taking over your browser.
>
> To get started, install the Chrome plugin in the Codex app.

- 含视频（未转写）

### x-2052068619635589466

**unusual_whales (@unusual_whales)** · 发帖 2026-05-06 · [原帖](https://x.com/unusual_whales/status/2052068619635589466)

> BREAKING: Anthropic has released a feature called "dreaming" which allows AI agents to self-improve


### x-2050988005817499827

**Sebastian Raschka (@rasbt)** · 发帖 2026-05-03 · [原帖](https://x.com/rasbt/status/2050988005817499827)

> Here is a 2nd batch of April architecture drops. What a month!
> - Ant Ling 2.6 1T
> - Minimax M2.7
> - Xiaomi MiMo V2.5
> - Poolside Laguna XS.2
> - Tencent Hy3-preview
> - IBM Granite 4.1

- 图片：[img1](https://pbs.twimg.com/media/HHaStq6WgAAM7mg?format=jpg&name=large)

### x-2050956647909015788

**DAIR.AI (@dair_ai)** · 发帖 2026-05-03 · [原帖](https://x.com/dair_ai/status/2050956647909015788)

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

### x-2050228936270037068

**Suryansh Tiwari (@Suryanshti777)** · 发帖 2026-05-01 · [原帖](https://x.com/Suryanshti777/status/2050228936270037068)

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

### x-2029858356916277757

**我真的没有拼多多 (@nopinduoduo)** · 发帖 2026-03-06 · [原帖](https://x.com/nopinduoduo/status/2029858356916277757)

> 《Google最新论文：目前只有2.5%的skills可用，大多数是垃圾，以及如何优化skills？》
>
> 由 Google 的开发者和研究团队今年 2 月份发布的论文《SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks》对目前 skills 进行了综述性的研究。
> 其中有几个看似反常又很有意思的点：
> 目前有 4 万多个 skills，只有 1k 个左右是有用的
> Agent/LLM 写的 skills 都是垃圾，高级的 skills 都是手写的
> 60%-80% 的 skills 都集中在软件工程领域
> 不同任务skills的数量
> 一、三大核心发现
> 1. "4 万个 Skills 中只有 1k 个有用"
> 论文调研了目前社区（如开源项目、Agent 平台）中存在的庞大 Skills 生态。
> 研究指出，虽然各种仓库里托管了成千上万个（约 40,000+）由用户贡献的 Skills，但经过测试发现，其中绝大多数是冗余、低质或由于环境失效而不可用的。
> 论文最终通过严格筛选和人工校验，精选出了约 1,000 个左右的高质量、确定性强（Curated Skills）作为 Benchmark 的核心。
> 2. "Agent 写的 Skills 是垃圾，高级 Skills 必须手写"
> 这是该论文最扎心的结论之一。
> 研究对比了三种情况：
> No Skills（无技能补充）
> Curated Skills（人工编写/筛选的优质技能）
> Self-generated Skills（LLM 自动生成的技能）
> 实验结果显示，人工精心编写的技能能将任务成功率提高约 16.2%（在医疗等复杂领域甚至能提高 51.9%）。
> 而 LLM 自动生成的技能几乎没有任何正面贡献，有时甚至会因为引入错误的 API 调用或逻辑而产生负面影响。
> 论文指出，目前的模型还没有能力"自我编写"出它们真正受益的高质量程序化知识。
> （模型在垂直领域的能力还欠缺，需要专业的知识技能来弥补）
> 3. "60%-80% 的 Skills 集中在软件工程"
> 论文在分析现有的 Skills 分布时提到，目前的 Agent 技能生态极度不平衡。
> 大约 60% 到 80% 的现有技能都集中在软件工程（Software Engineering）和数据分析（Data Analysis）领域，而其他垂直行业（如法律、医疗、制造业）的高质量技能非常匮乏。
> 二、我的思考
> 其实倒也符合我们的常识和认知印象了，AI 直接创建的 skills 都是垃圾。
> 因为真正有价值的 SOP，AI 是无法直接创建的，这是个人经验的积累。
> 其次呢，真正有价值的 skills，大家大概也不想完全开源出来的。
> 这包括创作的风格、思路等等。
> 以及，为何主要集中在软件工程领域？
> 似乎也不难理解，程序员真是一群天生爱开源的人，再加上 skills 本身从 Claude Code、从技术圈诞生的，目前量最多也好理解了。
> 我想一个启发是，教会非技术圈，其它垂直领域的人（如法律、医疗、制造业）沉淀形成自己的 skills，将是一件很有价值的事情。
> 三、五个优化方向
> 最后论文通过实验发现了多个优化方向：
> 优化一：控制 Skills 数量
>     结论：Skills 不是越多越好，过多的内容会造成认知负担或互相冲突的建议。
> 优化二：控制 Skills 复杂度
>   结论：Focused 的、分步骤的指导 + 至少一个工作示例 > 冗长的 exhaustive 文档。智能体很难从长篇大论中提取有用信息。
> 优化三：匹配领域需求
> 不同领域获益差异巨大：
>   结论：在模型预训练中缺乏专业知识的领域（如医疗数据协调、制造工作流），Skills 帮助最大；而模型本来就很强的领域，Skills 反而可能引入噪音。
> 优化四：利用 Skills 弥补模型规模
> 论文发现：
> Claude Haiku（有 Skills）：27.7%
> Claude Opus（无 Skills）：22.0%
> 结论：小模型 + 好 Skills 可以超越大模型。这对于成本敏感的场景很有价值。
> 启示：用好 skills，完全可以实现小模型的弯道超车。
> 优化五：针对 Harness 做适配
> 论文发现不同智能体框架对 Skills 的利用能力不同：
>   结论：选择合适的 agent harness 很重要，有些框架更善于检索和使用 Skills。
> 四、实践建议
> 在论文的 Discussion 部分，作者总结了关于 Skills 编写的建议：
> 1. 简洁优先：简洁、分步骤的指导 + 至少一个工作示例，往往比冗长的 exhaustive 文档更有效
> 2. 模块化：模块化的 Skills 在多部分任务上组合效果更好
> 3. 适配 Harness：Skills 应该明确匹配 harness 的约束（如 JSON-only 协议的重复格式提醒）
> 4. 避免过度：确保 Skills 提供的是"如何做"的程序性指导，而不是"答案是什么"的声明性内容
> 论文原文：
> https://arxiv.org/html/2602.12670v1

- 图片：[img1](https://pbs.twimg.com/media/HCuAMbtbwAAl29X?format=jpg&name=large) [img2](https://pbs.twimg.com/media/HCuBMqibcAA62eV?format=png&name=large) [img3](https://pbs.twimg.com/media/HCuAcCxaEAAAimX?format=png&name=large) [img4](https://pbs.twimg.com/media/HCuAfTXaUAM1zac?format=png&name=large) [img5](https://pbs.twimg.com/media/HCuAuXxaUAI4DwL?format=png&name=large) [img6](https://pbs.twimg.com/media/HCuA2fmbgAAuieX?format=png&name=large)

### x-2029562218048541087

**el.cine (@EHuanglu)** · 发帖 2026-03-05 · [原帖](https://x.com/EHuanglu/status/2029562218048541087)

> AI ending interior design
>
> Nano banana 2 now can turn sketch floor plan into 4K 3D rendering with accurate dimension, take photos for each room, and 1-click furniture change
>
> used to cost $100k and months.. now cents and mins
>
> step by step tutorial on OpenArt:

- 含视频（未转写）

### x-2028833958230933729

**meng shao (@shao__meng)** · 发帖 2026-03-03 · [原帖](https://x.com/shao__meng/status/2028833958230933729)

> 如何成为世界级的「Agentic Engineer」
>
> -- 你可以把大量的设计和实现交给 Agent，但结果你必须自己负责。
>
> 工具不是越多越好，而是越精简越强
> 大多数人陷入了"工具崇拜"的误区：以为安装越多的插件、harness、记忆系统，就能让 Agent 更强。实际上，这些外部依赖带来的是上下文污染，Agent 表现反而下降。
> @systematicls 现在用的是近乎裸机的 CLI（Claude Code + Codex），并且做出了迄今为止最好的工作。
>
> 理解"模型在飞速进化"这件事
> · 几个版本前，在 CLAUDE. md 里写"先读这个文件"，Agent 有 50% 概率会无视你
> · 现在，它能理解嵌套的条件指令（"如果 C，则读 D"）
>
> 今天为某个缺陷设计的复杂解决方案，可能在下一个模型版本中直接失效，或直接被模型实现。这和 @bcherny 面向 6 个月后模型开发产品有异曲同工之妙。
>
> 上下文管理：最被低估的工程能力
> > "你只需要给 Agent 完成任务所需的确切信息，不多也不少。"
>
> 研究与实现必须分离：
> · 错误做法："去帮我构建一个认证系统。" — Agent 会去查所有方案，上下文被各种备选实现细节填满，实现时容易混乱或幻觉。
> · 正确做法："用 bcrypt-12 实现 JWT 认证，refresh token 7 天过期……" — 上下文直接聚焦在实现细节上。
>
> 如果你自己不确定实现方案，流程应该是：
> 1. 开一个 Agent 做调研，输出方案对比
> 2. 你或 Agent 决策选哪个
> 3. 另开一个全新上下文的 Agent 来实现
>
> 巧用 Agent 的"奉承性"
> Agent 被设计为"取悦用户"——你让它找 bug，它会找到 bug，哪怕需要编造一个。这不是 Agent 的错，这是你的提示词问题。
>
> 解决方案一：中性提示词
> 别说"找 bug"，而说"梳理各模块的逻辑，报告所有发现"。
> 中性提示不预设结论，Agent 会如实汇报，有 bug 说 bug，没有就说没有。
>
> 解决方案二：利用奉承性设计多 Agent 对抗系统
> 作者设计了一个三 Agent 的 bug 验证机制：
> · Bug 发现者：低/中/高影响 bug 分别得 +1/+5/+10 分
> · 对抗者：成功反驳得对应分，反驳错误扣 2 倍
> · 裁判：告知有真实答案参照，对错各 ±1
>
> 明确任务的"终点"
> Agent 很擅长开始任务，却不知道何时结束——这是当前模型的固有限制。
>
> 两种可靠的终点定义方式：
> · 测试套件：明确告知 Agent "X 个测试全部通过才算完成，且不得修改测试文件"。测试是确定性的，Agent 无法糊弄。
> · 截图 + 视觉验证：实现功能后让 Agent 截图，并验证设计或行为是否符合预期。Agent 可以根据截图反复迭代，直到视觉结果满足要求。
>
> 更高阶的做法：为每个任务创建 {TASK}_CONTRACT.md ，其中列出所有验收条件（测试、截图验证等），结合 stop-hook 机制，强制 Agent 在合同完成前不得退出。
>
> 长期运行 Agent 的正确姿势
> 作者明确反对"24 小时连续运行的超长会话"，原因正是上下文污染——多个不相关合同的上下文混在一起，会导致漂移。
>
> 推荐方案：
> · 每个合约开一个新会话
> · 用一个编排层负责创建合同、分发新会话
> 会话完成即关闭，下个任务开新会话
>
> 规则与技能的管理
> CLAUDE. md 的定位：不是一份完整文档，而是一个条件跳转目录。它只告诉 Agent "在什么场景下，去读哪个文件"。
>
> 格式示例：
> · 如果你在写代码，先读 coding-rules. md
> · 如果你在写测试，先读 coding-test-rules. md
> · 如果测试失败，先读 coding-test-failing-rules. md
>
> 规则（Rules）：编码偏好——"不要做 X"、"总是做 Y"。看到 Agent 做了你不满意的事，就写成规则。
> 技能（Skills）：编码方法——"按照这个流程做 Z"。如果你想让某件事的做法确定可控，先让 Agent 研究如何做，把方案写成 Skill 文件，然后你审阅修正——这样在真实场景出现前，你就已经掌握了 Agent 的解法。
> 维护原则：规则和技能积累到一定程度会出现矛盾和冗余，导致性能再次下降。此时需要定期"清理"——让 Agent 整合并去重，向你确认最新偏好。这是一个需要周期性执行的维护动作。

- 图片：[img1](https://pbs.twimg.com/media/HCfdtGKbUAA7yJy?format=jpg&name=large)

### x-2027350587533332748

**Rimsha Bhardwaj (@heyrimsha)** · 发帖 2026-02-27 · [原帖](https://x.com/heyrimsha/status/2027350587533332748)

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

### x-2022009906329739681

**OpenAI Developers (@OpenAIDevs)** · 发帖 2026-02-12 · [原帖](https://x.com/OpenAIDevs/status/2022009906329739681)

> Introducing GPT-5.3-Codex-Spark, our ultra-fast model purpose built for real-time coding.
>
> We’re rolling it out as a research preview for ChatGPT Pro users in the Codex app, Codex CLI, and IDE extension.

- 含视频（未转写）

### x-2026178278055403843

**GitHubDaily (@GitHub_Daily)** · 发帖 2026-02-24 · [原帖](https://x.com/GitHub_Daily/status/2026178278055403843)

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

### x-2025920521871716562

**Elvis (@elvissun)** · 发帖 2026-02-23 · [原帖](https://x.com/elvissun/status/2025920521871716562)

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

### x-2026224275192193465

**AYi (@AYi_AInotes)** · 发帖 2026-02-24 · [原帖](https://x.com/AYi_AInotes/status/2026224275192193465)

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


### x-2023257934017294806

**OpenClaw (@openclaw)** · 发帖 2026-02-16 · [原帖](https://x.com/openclaw/status/2023257934017294806)

> 🦞 OpenClaw 2026.2.15 is here!
>
> ✨ Telegram message streaming — replies flow live
> 💬 Discord Components v2 — buttons, selects, modals
> 🔧 Nested sub-agents
> 🔒 Major security hardening pass
> 🐛 40+ bug fixes
>
> Big day. Huge day. Maybe the biggest day.🏛️

- 链接卡片：[Releases · openclaw/openclaw](https://t.co/CywtGDbYpk)

### x-2022530044434825310

**OpenClaw (@openclaw)** · 发帖 2026-02-14 · [原帖](https://x.com/openclaw/status/2022530044434825310)

> 🦞 OpenClaw 2026.2.13
>
> 🤗 HuggingFace support
> ✉️ Messages survive crashes (write-ahead queue)
> 🎙️ Discord voice messages + custom presence
> 🧵 Threading that actually works
> 🔒 Massive security hardening pass
> 🤖 gpt-5.3-codex-spark support
>
> 337 commits. The community never sleeps 🫡

- 链接卡片：[Release openclaw 2026.2.13 · openclaw/openclaw](https://t.co/EdqQRoYorZ)

### x-2021387483364151451

**nader dabit (@dabit3)** · 发帖 2026-02-11 · [原帖](https://x.com/dabit3/status/2021387483364151451)

> 《You Could've Invented OpenClaw》
>
> This tutorial involves a lot of code and is therefore also available as markdown here. See more of my writing here.
> In this post, I'll start from scratch and build up to OpenClaw's architecture step by step, showing how you could have invented it yourself from first principles, using nothing but a messaging API, an LLM, and the desire to make AI actually useful *outside* the chat window.
> End goal: understand how persistent AI assistants work, so you can build your own (or become an OpenClaw power user).
> First, let's establish the problem
> When you use ChatGPT or Claude in a browser, there are several limitations:
> It's stateless. Every conversation starts from zero. It doesn't know your name, your preferences, what you asked yesterday, or what project you're working on. You're constantly re-explaining context.
> It's passive. You go to it. It never comes to you. It can't wake up at 7am and brief you on your calendar, monitor your email, or run a recurring task. It only works when you're sitting in front of it.
> It's isolated. It can't run commands on your machine, browse the web for you, control your apps, or send messages on your behalf. It lives in a text box with no hands.
> It's single-channel. Your real life happens across WhatsApp, Telegram, Discord, Slack, iMessage - but the AI lives in its own separate tab. There's no way to text it where you already are, let alone have it maintain one continuous memory across all those surfaces.
> What if instead, you had an AI that:
> Lived in the messaging apps you already use - all of them, with shared memory
> Remembered your preferences, your projects, and your past conversations across sessions
> Could run commands on your computer, browse the web, and control a real browser
> Woke up on a schedule to handle recurring tasks without being asked
> Ran on your own hardware - your laptop, a VPS, a Mac Mini - always on, under your control
> This is what OpenClaw does. It's not a chatbot - it's a personal AI assistant with a persistent identity, tools, and presence across every channel you use.
> Let's build one from scratch.
> The Simplest Possible Bot
> Let's start with the absolute minimum: an AI that responds to messages on Telegram.
> python
> import os
> import anthropic
> from telegram import Update
> from telegram.ext import Application, MessageHandler, filters
>
> client = anthropic.Anthropic()
>
> async def handle_message(update: Update, context):
>     user_message = update.message.text
>
>     response = client.messages.create(
>         model="claude-sonnet-4-5-20250929",
>         max_tokens=1024,
>         messages=[{"role": "user", "content": user_message}]
>     )
>
>     await update.message.reply_text(response.content[0].text)
>
> app = Application.builder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()
> app.add_handler(MessageHandler(filters.TEXT, handle_message))
> app.run_polling()
> Run it, send a message on Telegram, and the AI responds. Simple.
> But this is basically a worse version of the Claude web interface. Every message is independent. No memory. No tools. No personality.
> What if we gave it memory?
> Goal: Persistent Sessions
> A problem with our simple bot is statelessness. Every message is a fresh conversation. Ask it "what did I say earlier?" and it has no idea.
> The fix is sessions. Keep a conversation history per user.
> python
> import json
> import os
> import anthropic
> from telegram import Update
> from telegram.ext import Application, MessageHandler, filters
>
> client = anthropic.Anthropic()
> SESSIONS_DIR = "./sessions"
> os.makedirs(SESSIONS_DIR, exist_ok=True)
>
> def get_session_path(user_id):
>     return os.path.join(SESSIONS_DIR, f"{user_id}.jsonl")
>
> def load_session(user_id):
>     """Load conversation history from disk."""
>     path = get_session_path(user_id)
>     messages = []
>     if os.path.exists(path):
>         with open(path, "r") as f:
>             for line in f:
>                 if line.strip():
>                     messages.append(json.loads(line))
>     return messages
>
> def append_to_session(user_id, message):
>     """Append a single message to the session file."""
>     path = get_session_path(user_id)
>     with open(path, "a") as f:
>         f.write(json.dumps(message) + "\n")
>
> def save_session(user_id, messages):
>     """Overwrite the session file with the full message list."""
>     path = get_session_path(user_id)
>     with open(path, "w") as f:
>         for message in messages:
>             f.write(json.dumps(message) + "\n")
>
> async def handle_message(update: Update, context):
>     user_id = str(update.effective_user.id)
>     user_message = update.message.text
>
>     # Load existing conversation
>     messages = load_session(user_id)
>
>     # Add new user message
>     user_msg = {"role": "user", "content": user_message}
>     messages.append(user_msg)
>     append_to_session(user_id, user_msg)
>
>     # Call the AI with full history
>     response = client.messages.create(
>         model="claude-sonnet-4-5-20250929",
>         max_tokens=4096,
>         messages=messages
>     )
>
>     # Save assistant response
>     assistant_msg = {"role": "assistant", "content": response.content[0].text}
>     append_to_session(user_id, assistant_msg)
>
>     await update.message.reply_text(response.content[0].text)
>
> app = Application.builder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()
> app.add_handler(MessageHandler(filters.TEXT, handle_message))
> app.run_polling()
> Now you can have an actual conversation:
> plaintext
> You: My name is Nader
> Bot: Nice to meet you, Nader!
>
> [hours later...]
>
> You: What's my name?
> Bot: Your name is Nader!
> The key insight is the JSONL format. Each line is one message. Append-only. If the process crashes mid-write, you lose at most one line. This is exactly what OpenClaw uses for session transcripts:
> plaintext
> ~/.openclaw/agents/<agentId>/sessions/<sessionId>.jsonl
> Each session maps to a file. Each file is a conversation. Restart the process and everything is still there.
> But we'll hit a problem: conversations grow. Eventually they'll exceed the model's context window. We'll come back to that.
> Goal: Adding a Personality (SOUL.md)
> Our bot works, but it has no personality. It's a generic AI assistant. What if we wanted it to be *someone*?
> OpenClaw solves this with SOUL.md: a markdown file that defines the agent's identity, behavior, and boundaries.
> python
> SOUL = """
> # Who You Are
>
> **Name:** Jarvis
> **Role:** Personal AI assistant
>
> ## Personality
> - Be genuinely helpful, not performatively helpful
> - Skip the "Great question!" - just help
> - Have opinions. You're allowed to disagree
> - Be concise when needed, thorough when it matters
>
> ## Boundaries
> - Private things stay private
> - When in doubt, ask before acting externally
> - You're not the user's voice - be careful about sending messages on their behalf
>
> ## Memory
> Remember important details from conversations.
> Write them down if they matter.
> """
>
> async def handle_message(update: Update, context):
>     user_id = str(update.effective_user.id)
>     messages = load_session(user_id)
>
>     user_msg = {"role": "user", "content": update.message.text}
>     messages.append(user_msg)
>     append_to_session(user_id, user_msg)
>
>     response = client.messages.create(
>         model="claude-sonnet-4-5-20250929",
>         max_tokens=4096,
>         system=SOUL,  # <-- personality injected here
>         messages=messages
>     )
>
>     assistant_msg = {"role": "assistant", "content": response.content[0].text}
>     append_to_session(user_id, assistant_msg)
>
>     await update.message.reply_text(response.content[0].text)
> Now instead of a generic assistant, you're talking to Jarvis. The SOUL gets injected as the system prompt on every API call.
> In OpenClaw, the SOUL.md lives in the agent's workspace:
> plaintext
> ~/.openclaw/workspace/SOUL.md
> It gets loaded at session start and injected into the system prompt. You can write anything you want in there. Give the agent an origin story. Define its core philosophy. List its behavioral rules.
> The more specific your SOUL, the more consistent the agent's behavior. "Be helpful" is vague. "Be the assistant you'd actually want to talk to. Concise when needed, thorough when it matters. Not a corporate drone. Not a sycophant. Just... good." - that gives the model something to work with.
> Goal: Adding Tools
> A bot that can only talk is limited. What if it could *do things*?
> The core idea: give the AI structured tools and let it decide when to use them.
> python
> import subprocess
>
> TOOLS = [
>     {
>         "name": "run_command",
>         "description": "Run a shell command on the user's computer",
>         "input_schema": {
>             "type": "object",
>             "properties": {
>                 "command": {"type": "string", "description": "The command to run"}
>             },
>             "required": ["command"]
>         }
>     },
>     {
>         "name": "read_file",
>         "description": "Read a file from the filesystem",
>         "input_schema": {
>             "type": "object",
>             "properties": {
>                 "path": {"type": "string", "description": "Path to the file"}
>             },
>             "required": ["path"]
>         }
>     },
>     {
>         "name": "write_file",
>         "description": "Write content to a file",
>         "input_schema": {
>             "type": "object",
>             "properties": {
>                 "path": {"type": "string", "description": "Path to the file"},
>                 "content": {"type": "string", "description": "Content to write"}
>             },
>             "required": ["path", "content"]
>         }
>     },
>     {
>         "name": "web_search",
>         "description": "Search the web for information",
>         "input_schema": {
>             "type": "object",
>             "properties": {
>                 "query": {"type": "string", "description": "Search query"}
>             },
>             "required": ["query"]
>         }
>     }
> ]
>
> def execute_tool(name, input):
>     if name == "run_command":
>         result = subprocess.run(
>             input["command"], shell=True,
>             capture_output=True, text=True, timeout=30
>         )
>         return result.stdout + result.stderr
>
>     elif name == "read_file":
>         with open(input["path"], "r") as f:
>             return f.read()
>
>     elif name == "write_file":
>         with open(input["path"], "w") as f:
>             f.write(input["content"])
>         return f"Wrote to {input['path']}"
>
>     elif name == "web_search":
>         # Simplified - use a real search API in practice
>         return f"Search results for: {input['query']}"
>
>     return f"Unknown tool: {name}"
> Now we need the agent loop. When the AI wants to use a tool, we execute it and feed the result back:
> python
> def serialize_content(content):
>     """Convert API response content blocks to JSON-serializable dicts."""
>     serialized = []
>     for block in content:
>         if hasattr(block, "text"):
>             serialized.append({"type": "text", "text": block.text})
>         elif block.type == "tool_use":
>             serialized.append({
>                 "type": "tool_use",
>                 "id": block.id,
>                 "name": block.name,
>                 "input": block.input
>             })
>     return serialized
>
> def run_agent_turn(messages, system_prompt):
>     """Run one full agent turn (may involve multiple tool calls)."""
>     while True:
>         response = client.messages.create(
>             model="claude-sonnet-4-5-20250929",
>             max_tokens=4096,
>             system=system_prompt,
>             tools=TOOLS,
>             messages=messages
>         )
>
>         content = serialize_content(response.content)
>
>         # If the AI is done (no tool use), return the text
>         if response.stop_reason == "end_turn":
>             text = ""
>             for block in response.content:
>                 if hasattr(block, "text"):
>                     text += block.text
>             messages.append({"role": "assistant", "content": content})
>             return text, messages
>
>         # Process tool calls
>         if response.stop_reason == "tool_use":
>             messages.append({"role": "assistant", "content": content})
>
>             tool_results = []
>             for block in response.content:
>                 if block.type == "tool_use":
>                     print(f"  Tool: {block.name}({json.dumps(block.input)})")
>                     result = execute_tool(block.name, block.input)
>                     tool_results.append({
>                         "type": "tool_result",
>                         "tool_use_id": block.id,
>                         "content": str(result)
>                     })
>
>             messages.append({"role": "user", "content": tool_results})
> Now we update `handle_message` to use the agent loop instead of calling the API directly:
> python
> async def handle_message(update: Update, context):
>     user_id = str(update.effective_user.id)
>     messages = load_session(user_id)
>     messages.append({"role": "user", "content": update.message.text})
>
>     response_text, messages = run_agent_turn(messages, SOUL)
>
>     save_session(user_id, messages)
>     await update.message.reply_text(response_text)
> Now you can text your bot:
> plaintext
> You: Create a file called hello.py that prints hello world, then run it
>
> Bot: [uses write_file to create hello.py]
>     [uses run_command to execute it]
>     Done! I created hello.py and ran it. Output: "hello world"
> The AI decided which tools to use, in what order, and synthesized the results into a natural response. All through a Telegram message.
> OpenClaw's production tool catalog is much larger - browser automation, inter-agent messaging, sub-agent spawning, and more - but every tool follows this exact pattern: a schema, a description, and an execution function.
> Goal: Permission Controls
> We're executing commands from Telegram messages. That's terrifying. What if someone gets access to your Telegram account and tells the bot to `rm -rf /`?
> We need a permission system. OpenClaw's approach: an approval allowlist that remembers what you've approved.
> We add these helpers alongside our existing code, then update the `run_command` case inside `execute_tool` to use them:
> python
> import re
>
> SAFE_COMMANDS = {"ls", "cat", "head", "tail", "wc", "date", "whoami", "echo"}
> DANGEROUS_PATTERNS = [r"\brm\b", r"\bsudo\b", r"\bchmod\b", r"\bcurl.*\|.*sh"]
>
> # Persistent allowlist
> APPROVALS_FILE = "./exec-approvals.json"
>
> def load_approvals():
>     if os.path.exists(APPROVALS_FILE):
>         with open(APPROVALS_FILE) as f:
>             return json.load(f)
>     return {"allowed": [], "denied": []}
>
> def save_approval(command, approved):
>     approvals = load_approvals()
>     key = "allowed" if approved else "denied"
>     if command not in approvals[key]:
>         approvals[key].append(command)
>     with open(APPROVALS_FILE, "w") as f:
>         json.dump(approvals, f, indent=2)
>
> def check_command_safety(command):
>     """Returns 'safe', 'approved', or 'needs_approval'."""
>     base_cmd = command.strip().split()[0] if command.strip() else ""
>     if base_cmd in SAFE_COMMANDS:
>         return "safe"
>
>     approvals = load_approvals()
>     if command in approvals["allowed"]:
>         return "approved"
>
>     for pattern in DANGEROUS_PATTERNS:
>         if re.search(pattern, command):
>             return "needs_approval"
>
>     return "needs_approval"
> Now update the `run_command` case in `execute_tool` to check permissions before executing:
> python
>     if name == "run_command":
>         cmd = input["command"]
>         safety = check_command_safety(cmd)
>
>         if safety == "needs_approval":
>             # In a real bot, you'd prompt the user via Telegram
>             # and wait for their response. For simplicity, we log and deny.
>             print(f"  ⚠️  Blocked: {cmd} (needs approval)")
>             return "Permission denied. Command requires approval."
>
>         result = subprocess.run(
>             cmd, shell=True, capture_output=True,
>             text=True, timeout=30
>         )
>         return result.stdout + result.stderr
> When a command is safe or previously approved, it runs immediately. When it's not, the agent gets told "permission denied" and can try a different approach. The approval gets persisted to `exec-approvals.json`, so you're never asked twice for the same command.
> OpenClaw extends this with glob patterns (approve `git *` once) and a three-tier model: "ask" (prompt user), "record" (log but allow), and "ignore" (auto-allow).
> Goal: The Gateway
> Here's where it gets interesting. So far we have a Telegram bot. But what if you also want the AI on Discord? And WhatsApp? And Slack?
> You could write separate bots for each platform. But then you'd have separate sessions, separate memory, separate configurations. The AI on Telegram wouldn't know what you discussed on Discord.
> The solution: a gateway. One central process that manages all channels.
> Look at what we already have. Our `run_agent_turn` function doesn't know anything about Telegram. It takes messages and returns text. That's the key - the agent logic is already decoupled from the channel.
> To prove it, let's add a second interface. We'll add a simple HTTP API alongside our Telegram bot, both talking to the same agent and the same sessions:
> python
> from flask import Flask, request, jsonify
> import threading
>
> flask_app = Flask(__name__)
>
> @flask_app.route("/chat", methods=["POST"])
> def chat():
>     data = request.json
>     user_id = data["user_id"]
>     messages = load_session(user_id)
>     messages.append({"role": "user", "content": data["message"]})
>
>     response_text, messages = run_agent_turn(messages, SOUL)
>
>     save_session(user_id, messages)
>     return jsonify({"response": response_text})
>
> # Run the HTTP API in a background thread
> threading.Thread(target=lambda: flask_app.run(port=5000), daemon=True).start()
>
> # Telegram bot runs as before
> app = Application.builder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()
> app.add_handler(MessageHandler(filters.TEXT, handle_message))
> app.run_polling()
> Try it out: Tell the bot your name on Telegram. Then query via HTTP using the same user ID (your Telegram user ID) to prove the session is shared:
> plaintext
> # Via Telegram
> You: My name is Nader
> Bot: Nice to meet you, Nader!
>
> # Via HTTP — use your Telegram user ID so it hits the same session
> curl -X POST http://127.0.0.1:5000/chat \
>   -H "Content-Type: application/json" \
>   -d '{"user_id": "YOUR_TELEGRAM_USER_ID", "message": "What is my name?"}'
>
> {"response": "Your name is Nader!"}
> Same agent, same sessions, same memory. Two different interfaces. That's the gateway pattern.
> The next step would be making this config-driven - a JSON file specifying which channels to start and how to authenticate them. 
> That's what OpenClaw does: its gateway manages Telegram, Discord, WhatsApp, Slack, Signal, iMessage, and more, all through a single config file. It also supports configurable session scoping - per-user, per-channel, or a single shared session - so the same person gets a unified experience across channels. We'll keep our simple user-ID-as-session-key approach for now.
> Goal: Context Compaction
> Remember the growing session problem we flagged earlier? After chatting with your bot for weeks, the session file has thousands of messages. The total token count exceeds the model's context window. Now what?
> The fix: summarize old messages, keep recent ones. Add these two functions alongside your existing code:
> python
> def estimate_tokens(messages):
>     """Rough token estimate: ~4 chars per token."""
>     return sum(len(json.dumps(m)) for m in messages) // 4
>
> def compact_session(user_id, messages):
>     """Summarize old messages when context gets too long."""
>     if estimate_tokens(messages) < 100_000:  # ~80% of a 128k window
>         return messages  # No compaction needed
>
>     split = len(messages) // 2
>     old, recent = messages[:split], messages[split:]
>
>     print("  Compacting session history...")
>
>     summary = client.messages.create(
>         model="claude-sonnet-4-5-20250929",
>         max_tokens=2000,
>         messages=[{
>             "role": "user",
>             "content": (
>                 "Summarize this conversation concisely. Preserve:\n"
>                 "- Key facts about the user (name, preferences)\n"
>                 "- Important decisions made\n"
>                 "- Open tasks or TODOs\n\n"
>                 f"{json.dumps(old, indent=2)}"
>             )
>         }]
>     )
>
>     compacted = [{
>         "role": "user",
>         "content": f"[Previous conversation summary]\n{summary.content[0].text}"
>     }] + recent
>
>     save_session(user_id, compacted)
>     return compacted
> Now add the compaction check at the top of `handle_message`, right after loading the session:
> python
> async def handle_message(update: Update, context):
>     user_id = str(update.effective_user.id)
>     messages = load_session(user_id)
>     messages = compact_session(user_id, messages)  # <-- add this line
>     messages.append({"role": "user", "content": update.message.text})
>
>     response_text, messages = run_agent_turn(messages, SOUL)
>
>     save_session(user_id, messages)
>     await update.message.reply_text(response_text)
> Try it out: To test compaction without chatting for hours, temporarily lower the threshold:
> python
> if estimate_tokens(messages) < 1000:  # lowered for testing
> Have a conversation of 10-15 messages, then watch the old messages get replaced with a summary. The bot still remembers key facts, but the session file is much smaller.
> OpenClaw's compaction is more sophisticated - it splits messages into chunks by token count, summarizes each chunk separately, and includes a safety margin for estimation inaccuracy - but the core idea is identical.
> Goal: Long-Term Memory
> Session history gives you conversation memory. But what happens when you reset a session or start a new one? Everything is gone.
> We need a separate memory system - persistent knowledge that survives session resets. The approach: give the agent tools to save and search memories stored as files.
> Add these two tools to the `TOOLS` list:
> python
> {
>     "name": "save_memory",
>     "description": "Save important information to long-term memory. Use for user preferences, key facts, and anything worth remembering across sessions.",
>     "input_schema": {
>         "type": "object",
>         "properties": {
>             "key": {
>                 "type": "string",
>                 "description": "Short label, e.g. 'user-preferences', 'project-notes'"
>             },
>             "content": {
>                 "type": "string",
>                 "description": "The information to remember"
>             }
>         },
>         "required": ["key", "content"]
>     }
> },
> {
>     "name": "memory_search",
>     "description": "Search long-term memory for relevant information. Use at the start of conversations to recall context.",
>     "input_schema": {
>         "type": "object",
>         "properties": {
>             "query": {
>                 "type": "string",
>                 "description": "What to search for"
>             }
>         },
>         "required": ["query"]
>     }
> }
> Add their cases to `execute_tool`:
> python
> MEMORY_DIR = "./memory"
>
> # Add these cases to execute_tool:
>
>     elif name == "save_memory":
>         os.makedirs(MEMORY_DIR, exist_ok=True)
>         filepath = os.path.join(MEMORY_DIR, f"{input['key']}.md")
>         with open(filepath, "w") as f:
>             f.write(input["content"])
>         return f"Saved to memory: {input['key']}"
>
>     elif name == "memory_search":
>         query = input["query"].lower()
>         results = []
>         if os.path.exists(MEMORY_DIR):
>             for fname in os.listdir(MEMORY_DIR):
>                 if fname.endswith(".md"):
>                     with open(os.path.join(MEMORY_DIR, fname), "r") as f:
>                         content = f.read()
>                     if any(word in content.lower() for word in query.split()):
>                         results.append(f"--- {fname} ---\n{content}")
>         return "\n\n".join(results) if results else "No matching memories found."
> Finally, update the SOUL so the agent knows about memory:
> python
> SOUL = """
> # Who You Are
> ...existing personality...
>
> ## Memory
> You have a long-term memory system.
> - Use save_memory to store important information (user preferences, key facts, project details).
> - Use memory_search at the start of conversations to recall context from previous sessions.
> Memory files are stored in ./memory/ as markdown files.
> """
> Try it out:
> plaintext
> You: Remember that my favorite restaurant is Elvies and I prefer to go on weekends.
>
> Bot: [uses save_memory to write nader-profile.md]
>      Got it — saved your restaurant preference.
>
> [Reset the session or restart the bot]
>
> You: Where should we go for dinner?
>
> Bot: [uses memory_search for "restaurant dinner favorite"]
>      How about Elvies? I know it's your favorite. Want to go this weekend?
> The memory persists because it's stored in files, not in the session. Reset the session, restart the bot - the memories are still there.
> OpenClaw's production memory uses vector search with embeddings for semantic matching (so "auth bug" matches "authentication issues"), but our keyword search works well for getting started.
> Goal: Command Queue
> Here's a subtle but critical problem: what happens when two messages arrive at the same time?
> Say you send "check my calendar" on Telegram and "what's the weather" via the HTTP API simultaneously. Both try to load the same session, both try to append to it, and you get corrupted data.
> The fix is simple: a per-session lock. Only one message processes at a time for each session. Different sessions can still run in parallel.
> python
> # Add to your bot
> from collections import defaultdict
>
> session_locks = defaultdict(threading.Lock)
> Now wrap the body of `handle_message` with the lock:
> python
> async def handle_message(update: Update, context):
>     user_id = str(update.effective_user.id)
>
>     with session_locks[user_id]:
>         messages = load_session(user_id)
>         messages = compact_session(user_id, messages)
>         messages.append({"role": "user", "content": update.message.text})
>
>         response_text, messages = run_agent_turn(messages, SOUL)
>
>         save_session(user_id, messages)
>
>     await update.message.reply_text(response_text)
> Do the same for the `/chat` HTTP endpoint:
> python
> @flask_app.route("/chat", methods=["POST"])
> def chat():
>     data = request.json
>     user_id = data["user_id"]
>
>     with session_locks[user_id]:
>         messages = load_session(user_id)
>         messages = compact_session(user_id, messages)
>         messages.append({"role": "user", "content": data["message"]})
>
>         response_text, messages = run_agent_turn(messages, SOUL)
>
>         save_session(user_id, messages)
>
>     return jsonify({"response": response_text})
> That's it - five lines of setup. Messages for the same user queue up. Messages for different users run in parallel. No race conditions.
> OpenClaw extends this with lane-based queues (separate lanes for messages, cron jobs, and sub-agents) so heartbeats never block real-time conversations.
> Goal: Cron Jobs (Heartbeats)
> So far our agent only responds when you talk to it. But what if you want it to check your email every morning? Or summarize your calendar before meetings?
> You need scheduled execution. Let's add heartbeats - recurring tasks that trigger the agent on a timer.
> python
> import schedule
> import time
>
> def setup_heartbeats():
>     """Configure recurring agent tasks."""
>
>     def morning_briefing():
>         print("\n⏰ Heartbeat: morning briefing")
>         # Use an isolated session key so cron doesn't pollute main chat
>         session_key = "cron:morning-briefing"
>
>         with session_locks[session_key]:
>             messages = load_session(session_key)
>             messages.append({
>                 "role": "user",
>                 "content": "Good morning! Check today's date and give me a motivational quote."
>             })
>
>             response_text, messages = run_agent_turn(messages, SOUL)
>             save_session(session_key, messages)
>
>         print(f"🤖 {response_text}\n")
>         # In production, you'd send this to Telegram/Discord too
>
>     schedule.every().day.at("07:30").do(morning_briefing)
>
>     # Run the scheduler in a background thread
>     def scheduler_loop():
>         while True:
>             schedule.run_pending()
>             time.sleep(60)
>
>     threading.Thread(target=scheduler_loop, daemon=True).start()
>
> # Call during startup, before run_polling()
> setup_heartbeats()
> The key insight: each heartbeat uses its own session key (`cron:morning-briefing`). This keeps scheduled tasks from cluttering your main conversation history. The heartbeat calls the same `run_agent_turn` function - it's just another message, triggered by a timer instead of a human.
> Try it out: For testing, change the schedule to run every minute:
> python
> schedule.every(1).minutes.do(morning_briefing)
>
> You'll see the heartbeat fire in your terminal, and the agent will respond. Change it back to a daily schedule when you're done testing.
> OpenClaw supports full cron expressions (`30 7 * * *`) and routes heartbeats through a separate command queue lane so they never block real-time messages.
> Goal: Multi-Agent
> One agent is useful. But as you add more tasks, you'll find a single personality and toolset can't cover everything well. A research assistant needs different instructions than a general assistant.
> The fix: multiple agent configurations with routing. Each agent has its own SOUL, its own session, and you switch between them based on the message.
> python
> AGENTS = {
>     "main": {
>         "name": "Jarvis",
>         "soul": SOUL,  # our existing SOUL
>         "session_prefix": "agent:main",
>     },
>     "researcher": {
>         "name": "Scout",
>         "soul": """You are Scout, a research specialist.
> Your job: find information and cite sources. Every claim needs evidence.
> Use tools to gather data. Be thorough but concise.
> Save important findings to memory for other agents to reference.""",
>         "session_prefix": "agent:researcher",
>     },
> }
>
> def resolve_agent(message_text):
>     """Route messages to the right agent based on prefix commands."""
>     if message_text.startswith("/research "):
>         return "researcher", message_text[len("/research "):]
>     return "main", message_text
> Update `handle_message` to route messages to the right agent:
> python
> async def handle_message(update: Update, context):
>     user_id = str(update.effective_user.id)
>     agent_id, message_text = resolve_agent(update.message.text)
>     agent = AGENTS[agent_id]
>     session_key = f"{agent['session_prefix']}:{user_id}"
>
>     with session_locks[session_key]:
>         messages = load_session(session_key)
>         messages = compact_session(session_key, messages)
>         messages.append({"role": "user", "content": message_text})
>
>         response_text, messages = run_agent_turn(messages, agent["soul"])
>
>         save_session(session_key, messages)
>
>     await update.message.reply_text(f"[{agent['name']}] {response_text}")
> Try it out:
> plaintext
> You: What's the weather like?
> [Jarvis] It's a nice day! I'd check a weather service for exact details.
>
> You: /research What are the best practices for Python async programming?
> [Scout] Here's what I found...
>     [uses web_search, save_memory to gather and store findings]
>     The key practices are: 1) Use asyncio.gather for concurrent tasks...
>
> You: What did Scout find about Python async?
> [Jarvis] [uses memory_search]
>     Scout's research found that the key async best practices are...
> Each agent has its own conversation history, but they share the same memory directory. Scout saves research findings; Jarvis can search for them later. They collaborate through shared files without needing direct messaging.
> OpenClaw extends this with sub-agent spawning (a parent agent can spawn a child for a focused task) and inter-agent messaging, but the core pattern is the same: each agent is just a SOUL + session + tools.
> Putting It All Together
> Let's combine everything we've built into a single runnable script. This is a clean standalone REPL that includes every feature from the tutorial: sessions, SOUL, tools, permissions, compaction, memory, command queue, cron, and multi-agent routing.
> I've put together a mini-openclaw in ~400 lines of code here:
> https://gist.github.com/dabit3/86ee04a1c02c839409a02b20fe99a492
> Save this as `mini-openclaw.py` and run it:
> bash
> uv run --with anthropic --with schedule python mini-openclaw.py
> Here's what a session looks like:
> plaintext
> Mini OpenClaw
>   Agents: Jarvis, Scout
>   Workspace: ~/.mini-openclaw
>   Commands: /new (reset), /research <query>, /quit
>
> You: Remember that my favorite restaurant is Hai Cenato and I prefer 7pm reservations
>
>   🔧 save_memory: {"key": "user-preferences", "content": "Favorite restaurant...
>      → Saved to memory: user-preferences
>
> 🤖 [Jarvis] Got it. Saved your restaurant preference - Hai Cenato, 7pm reservations.
>
> You: What's in my project directory?
>
>   🔧 run_command: {"command": "ls"}
>      → src, package.json, README.md, node_modules, ...
>
> 🤖 [Jarvis] Your project has a standard Node.js structure with src/, package.json,
>    and the usual suspects.
>
> You: /new
>   Session reset.
>
> You: Where do I like to eat?
>
>   🔧 memory_search: {"query": "restaurant favorite food"}
>      → --- user-preferences.md ---
>         Favorite restaurant: Hai Cenato...
>
> 🤖 [Jarvis] You like Hai Cenato, and you prefer 7pm reservations.
>
> You: /research What are the latest trends in AI agents?
>
>   🔧 web_search: {"query": "AI agent trends 2025"}
>      → Search results for: AI agent trends 2025
>   🔧 save_memory: {"key": "research-ai-agents", ...}
>      → Saved to memory: research-ai-agents
>
> 🤖 [Scout] Here's what I found on current AI agent trends...
> The memory persists across sessions. Agents collaborate through shared memory files. Commands require approval. Heartbeats run in the background. All in ~400 lines.
> What We've Learned
> Starting from a simple Telegram bot, we built every major component of a persistent AI assistant:
> Persistent sessions (JSONL files): Crash-safe conversation memory. Each session is one file, each line is one message. Restart the process and everything is still there.
> SOUL.md (system prompt): A personality file that transforms a generic AI into a specific agent with consistent behavior, boundaries, and style.
> Tools + Agent loop: Structured tool definitions that let the AI decide when to act. The agent loop calls the LLM, executes any requested tools, feeds results back, and repeats until done.
> Permission controls: An allowlist of safe commands plus persistent approvals, so dangerous operations require explicit consent.
> The gateway pattern: One central agent with multiple interfaces. Telegram, HTTP, or any other channel - they all talk to the same sessions and the same memory.
> Context compaction: When conversations outgrow the context window, summarize old messages and keep recent ones. The bot keeps its knowledge without hitting token limits.
> Long-term memory: File-based storage with save and search tools. Knowledge that survives session resets, accessible to any agent.
> Command queue: Per-session locking to prevent race conditions when multiple messages arrive simultaneously.
> Heartbeats: Scheduled agent runs on a timer, each with its own isolated session. The agent wakes up, does its task, and goes back to sleep.
> Multi-agent routing: Multiple agent configurations with different SOULs and session keys, routed by message content. Agents collaborate through shared memory files.
> Each of these emerged from a practical problem:
> "The AI can't remember anything" → Sessions
> "It responds like a generic chatbot" → SOUL.md
> "It can only talk, not act" → Tools + Agent loop
> "It runs dangerous commands without asking" → Permission controls
> "I want it on all my messaging apps" → Gateway
> "The conversation got too long" → Compaction
> "It forgets things between sessions" → Memory
> "Two messages at once corrupt the data" → Command queue
> "I want it to do things automatically" → Heartbeats
> "One agent can't do everything well" → Multi-agent
> This is how you could have invented OpenClaw.
> Going Further
> Our prototype covers the core architecture. Here's how OpenClaw extends each idea for production use - features worth exploring once you've outgrown the basics.
> Browser with Semantic Snapshots
> Most AI assistants can't see the web. OpenClaw gives the agent a browser via Playwright, but instead of sending screenshots (5MB each, expensive in tokens), it uses semantic snapshots - a text representation of the page's accessibility tree:
> python
> # Simplified concept
> snapshot = page.accessibility.snapshot()
> # Output:
> # - heading "Welcome to GitHub"
> # - button "Sign In" [ref=1]
> # - textbox "Email" [ref=2]
> # - link "Forgot password?" [ref=3]
> Each interactive element gets a numbered `ref` ID. When the agent wants to click something, it says "click ref=1" - which maps to exactly one element on the page. No guessing, no "click the blue button near the top." And since the snapshot is text instead of an image, it's roughly 100x smaller than a screenshot, which means far fewer tokens per page.
> Session Scoping & Identity Links
> Our prototype uses user ID as the session key. OpenClaw supports configurable scoping:
> main (default): All DMs share one session - simple, great for single-user setups.
> per-peer: Each person gets one session across all channels.
> per-channel-peer: Each person per channel gets their own session.
> Identity links let you merge sessions across channels for the same person, so Alice's Telegram and Discord conversations share the same history.
> Channel Plugin System
> Our prototype hardcodes Telegram + HTTP. OpenClaw uses a plugin architecture where each channel (Telegram, Discord, WhatsApp, Slack, Signal, iMessage) is a separate adapter that normalizes messages into a common format. Adding a new channel means writing one adapter, not touching any agent logic.
> Vector Memory Search
> Our keyword search works, but misses semantic matches ("auth bug" won't match "authentication issues"). OpenClaw's production memory uses a hybrid approach: vector search via SQLite with embedding extensions for semantic similarity, plus FTS5 for exact keyword matches. Configurable embedding providers include OpenAI, local models, Gemini, and Voyage.
> Sub-agent Spawning
> Our multi-agent setup uses manual routing. OpenClaw lets agents spawn sub-agents programmatically - a parent agent calls `sessions_spawn`, the child runs in its own context with a timeout, and returns results to the parent. This enables patterns like "research this topic in depth" where the main agent delegates to a specialist and continues when it's done.
> Next Steps
> If you want to build your own:
> Start with one channel: get a Telegram or Discord bot working with sessions
> Add tools incrementally: start with file read/write, then add shell execution
> Add memory when you need it: once sessions reset, you'll want persistent memory
> Add channels when you outgrow one: the gateway pattern emerges naturally
> Add agents when tasks specialize: don't start with 10 agents, start with 2
> Or just use OpenClaw. It's open source and handles all the edge cases we glossed over. But now you know how it works under the hood.

- 图片：[img1](https://pbs.twimg.com/media/HA1FTA1aAAIziKK?format=jpg&name=large)

### x-2013725989952467308

**David Ondrej (@DavidOndrej1)** · 发帖 2026-01-20 · [原帖](https://x.com/DavidOndrej1/status/2013725989952467308)

> Anthropic dropped a 7 hour Claude Code masterclass
>
> I went through the entire course
>
> And compiled everything into a 27 min video, enjoy

- 含视频（未转写）

### x-2013293638768562325

**Dilum Sanjaya (@DilumSanjaya)** · 发帖 2026-01-19 · [原帖](https://x.com/DilumSanjaya/status/2013293638768562325)

> Vibe Coding Robotics Part 7
>
> Implemented an ornithopter mechanism with Gemini Pro, and generated a Leonardo da Vinci style UI using Nano Banana to go with it.

- 含视频（未转写）

### x-2012701592756383893

**Matthew Berman (@MatthewBerman)** · 发帖 2026-01-18 · [原帖](https://x.com/MatthewBerman/status/2012701592756383893)

> MIT Researchers destroyed context window limits.
>
> 10m+ token prompts are now possible by moving context out of the model and into code environments. 
>
> Full breakdown below.

- 含视频（未转写）

### x-2011149280468484157

**KK.aWSB (@KKaWSB)** · 发帖 2026-01-13 · [原帖](https://x.com/KKaWSB/status/2011149280468484157)

> 别再说人工智能不能设计了。  
>
> Cursor + Opus 4.5 可以在不到 10 分钟的时间内创建了一个带有滚动叙事动画的着陆页，而设计师制作这样的页面通常要收取数千美元。  
>
> 如果你的落地页看起来还像2010年的应用，那不是人工智能的问题，而是工作流程的问题。

- 含视频（未转写）

### x-2009518503532089506

**KK.aWSB (@KKaWSB)** · 发帖 2026-01-09 · [原帖](https://x.com/KKaWSB/status/2009518503532089506)

> 字节跳动发布的 UI-TARS-desktop，是本地运行的桌面自动化代理。
>
> 它可以使用任何桌面应用程序，打开文件，浏览网站，并自动执行任务，无需云连接。100% 开源。

- 含视频（未转写）

### x-2010804702313652647

**Chris (@ChrisGPT)** · 发帖 2026-01-12 · [原帖](https://x.com/ChrisGPT/status/2010804702313652647)

> BREAKING 🚨 Anthropic just unveiled "Cowork," a major feature that turns Claude into a fully autonomous virtual assistant for everyone. It brings the deep agentic capabilities previously reserved for coders to general users, allowing Claude to perform complex tasks directly on your computer.
>
> The tool was built after Anthropic noticed developers using "Claude Code" for everyday admin tasks. Cowork now lets anyone grant Claude access to folders to manage files, research, and complete multi-step workflows independently acting as a digital employee that "does" instead of just chats.
>
> Cowork is available today as a research preview for Claude Max subscribers on the macOS app 😡. Claude is releasing new coding/desktop agents much faster than all of there competitors. 
>
> This launch exposes a massive gap in the current AI landscape: in 2026, Google still explicitly lacks a consumer browser agent, and xAI has yet to release a native CLI or agentic interface. While OpenAI has "Operator" and Google has the developer-focused "Antigravity," Anthropic is now the only other major lab providing a true "do-it-for-me" experience for general users.

- 含视频（未转写）

### x-2010720188686348593

**DAIR.AI (@dair_ai)** · 发帖 2026-01-12 · [原帖](https://x.com/dair_ai/status/2010720188686348593)

> Efficient Lifelong Memory for LLM Agents
>
> LLM agents need memory to handle long conversations. The way this is handled today is that memory either retains full interaction histories, leading to massive redundancy, or relies on iterative reasoning to filter noise, consuming excessive tokens.
>
> This new research introduces SimpleMem, an efficient memory framework based on semantic lossless compression that maximizes information density while minimizing token consumption.
>
> The framework operates through a three-stage pipeline.
>
> 1) First, Semantic Structured Compression applies entropy-aware filtering to distill raw dialogue into compact memory units, resolving coreferences and converting relative time expressions ("last Friday") into absolute timestamps.
>
> 2) Second, Recursive Memory Consolidation incrementally integrates related memories into higher-level abstractions, turning repetitive entries like "ordered a latte at 8 AM" into patterns like "regularly drinks coffee in the morning."
>
> 3) Third, Adaptive Query-Aware Retrieval dynamically adjusts the retrieval scope based on query complexity.
>
> The results: On the LoCoMo benchmark with GPT-4.1-mini, SimpleMem achieves 43.24 F1, outperforming the strongest baseline Mem0 (34.20) by 26.4%, while reducing token consumption to just 531 tokens per query compared to 16,910 for full-context approaches, a 30x reduction.
>
> They claim that memory construction is 14x faster than Mem0 (92.6s vs 1350.9s per sample) and 50x faster than A-Mem. Even a 3B parameter model with SimpleMem outperforms larger models using inferior memory strategies.
>
> This work shows that structured semantic compression and adaptive retrieval enable LLM agents to maintain reliable long-term memory without drowning in tokens or sacrificing accuracy.

- 图片：[img1](https://pbs.twimg.com/media/G-eDWs3bQAEMAzs?format=jpg&name=large)

### x-2010579279789387929

**大梦想家迪士尼 (@discountifu)** · 发帖 2026-01-12 · [原帖](https://x.com/discountifu/status/2010579279789387929)

> 周末 Vibe 了一个 Multi-Agent AI Trading 终端
> 还用 Textual 加了一套 TUI，这方面 Python 的生态建设真的是太好了
> 我把我毕生所学都“传功”给了 AI
> 支持 K线走势/技术指标/订单流/资金费率/开仓量 多因子分析
> 如果朋友们喜欢的话，点赞过100，我就直接把它开源了

- 含视频（未转写）

### x-2010178642752704850

**Julian Goldie SEO (@JulianGoldieSEO)** · 发帖 2026-01-11 · [原帖](https://x.com/JulianGoldieSEO/status/2010178642752704850)

> AntiGravity just became 10x more powerful.
>
> And 99% of users have no idea.
>
> Here's what you can actually do with it:
>
> → Switch between free APIs (Opus, Sonnet, Claude)
> → Generate images with Google's Nano Banana
> → Connect MCP servers directly to your projects
> → Use Claude Code inside the terminal for better UI
> → Deploy apps to Netlify in one click
> → Pull NotebookLM content into your builds
>
> No paid APIs. No limits. Just stack free tools.
>
> Save this video, you'll never use it the same way again.
>
> Want the SOP? DM me. 💬

- 含视频（未转写）

### x-2009709579903643768

**Md Ismail Šojal  (@0x0SojalSec)** · 发帖 2026-01-09 · [原帖](https://x.com/0x0SojalSec/status/2009709579903643768)

> Open-sourced 42 n8n agent templates from the full AI Agents A to Z✨
>
> - http://github.com/gyoridavid/ai_agents_az

- 图片：[img1](https://pbs.twimg.com/media/G-Pr2R5bUAAchy8?format=png&name=large)

### x-2008576712695836685

**James Zou (@james_y_zou)** · 发帖 2026-01-06 · [原帖](https://x.com/james_y_zou/status/2008576712695836685)

> Today in @NatureMedicine we report that AI can predict 130 diseases from 1 night of sleep🛌
>
> We trained a foundation model (#SleepFM) on 585K hours of sleep recordings from 65K people—brain, heart, muscle & breathing signals combined.
>
> AI learns the language of sleep🧵

- 图片：[img1](https://pbs.twimg.com/media/G9_ldwnWkAAevjh?format=jpg&name=large) [img2](https://pbs.twimg.com/media/G9_le27W0AElCBV?format=jpg&name=large)
