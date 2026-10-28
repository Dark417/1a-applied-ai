# X Likes · 关键词速览

- 共 50 条，按点赞顺序倒序（最新在上）
- Part 1：关键词 + 简述；Part 2：正文（同时在 Notes 里的帖子只给链接，不重复全文）
- 自动生成，勿手改

## Part 1 · Keywords

- [2026-10-27 · @Kay2289123](#x-2115125125163233473)：`Agent Evaluation`, `Hugging Face`, `RL for Agents`, `GRPO`, `OpenEnv`
  - 推荐 Hugging Face 公开的 Training Agent 课程，作为入门 Agent Evaluation 的学习资料。六节依次覆盖 Agent 评测、Agent 强化学习难点、基于 agent traces 的 SFT、蒸馏、GRPO 训练，以及用 OpenEnv/TRL 在真实环境中训练 coding agent（OpenCode）。作者认为 Agent Eval 是较难被 AI 取代的方向。
- [2026-10-27 · @miles_mazy](#x-2115072333832749202)：`Miles Ma`, `社群`, `截图`
  - 一条配图的短帖，作者说群里有人叫他删帖，问该怎么办；文字本身信息量很低，主要内容在图片里。
- [2026-10-26 · @AIStarsGo](#x-2114629460930740466)：`agent 时代的学习`, `deep work`, `shallow work`, `认知退化`
  - 个人教训：别让 agent 替你读论文，别把技术学习和英语学习混在一起，别为了用掉 token 去跑后台任务；要持续检查自己的认知是在进步还是在退化。
- [2026-10-24 · @0xsmerkzz](#x-2114099234001600931)：`SpaceXAI`, `GrokBot`, `multi-agent team`, `Chief of Staff agent`, `/loop`
  - SpaceXAI 工程师分享：同时跑 35+ 个 GrokBot agent，由一个 Chief of Staff agent 统一管理；附 1 小时 workshop 视频。
- [2026-10-24 · @Sumanth_077](#x-2113948384113598588) 🔖：`Harness²`, `Google`, `harness engineering`, `Propose→Probe→Compose`, `self-improving`
  - Google 开源 Harness²：模型权重不动，递归改进 agent 外围的 harness。任务内用 Propose→Probe→Compose 循环，跨任务保留已验证的 harness 和经验。
- [2026-10-23 · @AnnatarXBT](#x-2113634548378374458) 🔖：`harness engineering`, `Wavestone`, `Claude Code`, `Codex`, `7-part harness`
  - Wavestone 读了 11 个 coding agent 的源码，总结出共同的 7 部分 harness：loop、LLM 层、tools、memory、safety、orchestration、extensions。核心观点：agent = model + harness。
- [2026-10-03 · @sermakarevich](#x-2106453816757354947) 🔖：`evals`, `LLM 评测`, `PM / CEO 视角`, `可复现测试`
  - 长文：用通俗语言讲清楚怎么判断一个 LLM 系统是否真的可用，从 eval 的定义一直讲到落地细节，面向工程师、PM 和管理层。
- [2026-09-28 · @shao__meng](#x-2104453599367770287) 🔖：`Stanford CS329A`, `Self-Improving AI Agents`, `课程`
  - 推荐斯坦福 CS329A《Self-Improving AI Agents》，9 讲视频已全部上线，附课程主页和 YouTube 播放列表。
- [2026-09-19 · @0xMortyx](#x-2101308432305254889)：`Jev`, `decision layer`, `routing`, `agent execution`
  - Jev 被定位为 LLM 推理和 agent 执行之间的「决策层」：用 Choice / Score / Noul 显式路由，决策放在模型之外，号称快 193 倍、便宜 444 倍。
- [2026-07-31 · @eng_khairallah1](#x-2083131009986396282) 🔖：`graph engineering`, `graph architect`, `full course`
  - 长文课程：零基础成为 graph architect 的路线，涵盖节点设计、校验门、恢复路径、checkpoint、可观测性，以及什么时候不该用 graph。
- [2026-07-29 · @CodeNewsletter](#x-2082413202353406091) 🔖：`The Code newsletter`, `推广`
  - The Code newsletter 的订阅推广，内容空泛。
- [2026-08-06 · @AnatoliKopadze](#x-2085421662447468758) 🔖：`Anthropic`, `self-prompting system`, `agent loops`, `memory`
  - Anthropic 工程师 45 分钟演讲：不要手动 prompt Claude，而要搭一个能自我 prompt、自我纠错、越跑越好的系统。
- [2026-07-21 · @0xCarnagee](#x-2079636027736457707) 🔖：`graph engineering`, `Claude`, `subagents`, `self-verifying fleet`
  - 长文：分 12 步从单个 loop 扩展到能自我验证的 agent 集群；核心是拆分上下文，而不是换更大的模型。
- [2026-08-05 · @Mahaximus_](#x-2085024744387092973)：`agents`, `loops`, `graphs`, `Claude`
  - 长文汇总：agent（自主规划）、loop（跑到达标为止）、graph（并行 worker）三层是什么，以及怎么在 Claude 上组合起来。
- [2026-08-01 · @0xCodila](#x-2083602508807569560) 🔖：`Google`, `graph engineering`, `loop engineering`, `multi-agent`, `课程`
  - Google 免费 2 小时课程：从第一个 agent 到 loop engineering，再到 multi-agent graph，附各章节时间戳。
- [2026-06-29 · @AnatoliKopadze](#x-2071649423042412597) 🔖：`Spotify`, `Boris Cherny`, `agent loops`, `Claude Code`
  - Spotify 首席架构师：引入 loop 后 agent 成功率从 20–30% 提到 80%；Spotify 73% 的代码由 AI 写。核心观点：模型不如外围的 loop 重要。
- [2026-06-28 · @0xMovez](#x-2071214176526049739) 🔖：`agent loops`, `harness`, `evals`, `LLM-as-judge`
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
- [2026-05-03 · @dair_ai](#x-2050956647909015788) 🔖：`AI papers weekly`, `Agentic Harness Engineering`, `DAIR.AI`
  - DAIR.AI 每周论文精选（4/26–5/3），头条是 Agentic Harness Engineering：把 harness 的演化变得可观测、可证伪。
- [2026-05-01 · @Suryanshti777](#x-2050228936270037068) 🔖：`RAG`, `Karpathy`, `LLM Wiki`, `知识积累`
  - 观点：RAG 每次都从零开始、不积累任何东西；Karpathy 的 LLM Wiki 让 LLM 持续维护一份知识库，才是真正的累积。
- [2026-03-06 · @nopinduoduo](#x-2029858356916277757)：`SkillsBench`, `Google`, `agent skills`, `skills 质量`
  - 解读 Google 的 SkillsBench 论文：4 万多个 skills 里只有约 1k 个可用，LLM 写的 skill 基本不行，好的 skill 都是手写的。
- [2026-03-05 · @EHuanglu](#x-2029562218048541087) 🔖：`Nano Banana 2`, `室内设计`, `floor plan → 3D`
  - Nano Banana 2 能把手绘户型图变成 4K 3D 渲染，还能一键换家具；附 OpenArt 教程。
- [2026-03-03 · @shao__meng](#x-2028833958230933729)：`agentic engineer`, `context 管理`, `调研与实现分离`, `极简工具`
  - 如何成为顶级 agentic engineer：工具越精简越好；上下文只给刚好够用的信息；调研和实现用不同的 agent、不同的上下文。
- [2026-02-27 · @heyrimsha](#x-2027350587533332748) 🔖：`Anthropic`, `Claude Skills`, `SKILL.md`, `progressive disclosure`
  - 解读 Anthropic 的《The Complete Guide to Building Skills for Claude》：skill 是结构化系统，不只是 prompt，关键机制是 progressive disclosure。
- [2026-02-12 · @OpenAIDevs](#x-2022009906329739681)：`OpenAI`, `GPT-5.3-Codex-Spark`, `实时编码`, `新闻`
  - OpenAI 发布 GPT-5.3-Codex-Spark，主打超快实时编码，Pro 用户可以预览。
- [2026-02-24 · @GitHub_Daily](#x-2026178278055403843) 🔖：`GitNexus`, `代码知识图谱`, `MCP`, `依赖分析`
  - GitNexus 开源：给代码库建知识图谱，通过 MCP 接入 Cursor / Claude Code，让 AI 改代码前先看清调用链。完全本地运行。
- [2026-02-23 · @elvissun](#x-2025920521871716562) 🔖：`OpenClaw`, `orchestrator`, `agent swarm`, `one-person dev team`
  - 长文：作者用 OpenClaw 做编排层，编排器 Zoe 负责派生 Codex / Claude Code agent、写 prompt、监控进度、通知合并 PR，日均约 50 个 commit。
- [2026-02-24 · @AYi_AInotes](#x-2026224275192193465) 🔖：`OpenClaw`, `AI Orchestrator`, `一人公司`
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

## Part 2 · 正文

### x-2115125125163233473

**美研芒格君 (@Kay2289123)** · 发帖 2026-10-27 · [原帖](https://x.com/Kay2289123/status/2115125125163233473)

- **Agent Evaluation 是少数仍需要人做判断、将来很难被 AI 彻底取代的职业方向**
  - 入门资料推荐：**Hugging Face 的公开 Training Agent 课程**
  - 学完后会更有 sense：判断 AI 时代下哪些工作更适合人来做
- **资料完全公开**
  - 视频都在 Hugging Face 的 YouTube 频道
  - 代码全部开源
  - 共六节
- **1、Agentic Evaluations Workshop：怎么评价一个 Agent**
  - 为什么 **benchmark 分数和真实使用体验对不上**？
  - 目前 Agent Eval 做到了哪一步，还有哪些问题没解决
  - 先把"怎样才算一个好 Agent"等问题都 cover 到
- **2、RL for Agents Workshop：给 Agent 做强化学习，难在哪**
  - 从 LLM 的 RL 走到 Agent 的 RL，会多出哪些难点
  - 环境怎么搭、**rollout** 怎么跑、**reward** 怎么设计
  - 训练过程中**推理为什么会成为 bottleneck**
- **3、SFT on agent traces：用 Agent 的执行轨迹做微调**
  - 拿公开的 coding-agent traces（执行轨迹）整理成训练数据
  - 用 **TRL + LoRA** 做 SFT，在 **Hugging Face Jobs** 上跑
  - 用 **Trackio** 看指标
  - 基本带着走了一遍小型的微调流程
- **4、Distillation：把大模型的能力蒸馏给小 Agent**
  - 怎么把 teacher model 的能力转移给更小的 coding agent
  - 讲 **off-policy、on-policy、self-distillation** 三种蒸馏方式分别怎么做
- **5、Reinforcement Learning：SFT 之后，怎么继续用 RL 训练**
  - 用 **GRPO** 接着训练
  - 讲 group sampling、可验证的 reward
  - reward、KL、输出长度这些曲线怎么看
  - 看 Agent 怎么 **reward hacking**
- **6、From reward functions to environments：让 Agent 在真实环境里学习**
  - 从 `reset()` / `step()` 接口讲起
  - 用 **OpenEnv** 搭环境、上传到 Hub，再接入 TRL 的 `GRPOTrainer`
  - 最后通过 **Harbor** 和 Hugging Face sandboxes，用 `AsyncGRPOTrainer` 训练真正的 coding agent：**OpenCode**
  - 让 Agent 在环境里采取动作、拿到反馈，再继续训练

<details><summary>原文</summary>

> Agent Evaluation 是我觉得为数不多还需要人力去做判断、将来很难被AI 彻底取代的职业方向。我给大家找了一个非常好的学习资料入门：Hugging Face 的公开 Training Agent 课程
>
> 学完了，你应该会有更强的 sense，判断 AI 时代下哪些工作更适合人来做
>
> 这个资料是公开的，视频都在 Hugging Face 的 YouTube 频道，代码全部开源，下面有这六节：
> 1、Agentic Evaluations Workshop：怎么评价一个 Agent。
> 这一章节去看：为什么 benchmark 分数和真实使用体验对不上？目前 Agent Eval 做到了哪一步，还有哪些问题没解决。先把“怎样才算一个好 Agent”，等等都有 cover
>
> 2、RL for Agents Workshop：给 Agent 做强化学习，难在哪
> 这一章节去关注：从 LLM 的 RL 走到 Agent 的 RL，会多出哪些难点？环境怎么搭、rollout 怎么跑、reward 怎么设计，以及训练过程中推理为什么会成为 bottleneck
>
> 3、SFT on agent traces：用 Agent 的执行轨迹做微调
> 这一章节去关注：拿公开的 coding-agent traces（执行轨迹）整理成训练数据，用 TRL + LoRA 做 SFT，在 Hugging Face Jobs 上跑，用 Trackio 看指标。基本带着走了一遍小型的微调流程
>
> 4、Distillation：把大模型的能力蒸馏给小 Agent
> 这一章节去关注：怎么把 teacher model 的能力转移给更小的 coding agent。off-policy、on-policy、self-distillation 都会讲，看看这几种蒸馏方式分别怎么做
>
> 5、Reinforcement Learning：SFT 之后，怎么继续用 RL 训练
> 这一章节去关注：用 GRPO 接着训练，讲 group sampling、可验证的 reward，以及 reward、KL、输出长度这些曲线怎么看。看 Agent 怎么 reward hacking
>
> 6、From reward functions to environments：让 Agent 在真实环境里学习
> 这一章节去动手：从 reset()/step() 接口讲起，用 OpenEnv 搭环境、上传到 Hub，再接入 TRL 的 GRPOTrainer。最后通过 Harbor 和 Hugging Face sandboxes，用 AsyncGRPOTrainer 训练真正的 coding agent：OpenCode。让 Agent 在环境里采取动作、拿到反馈，再继续训练

</details>

- 图片：[img1](https://pbs.twimg.com/media/HVpu11PaAAA6U8_?format=jpg&name=large)

[↑ 回到目录](#part-1--keywords)

### x-2115072333832749202

**Miles Ma (@miles_mazy)** · 发帖 2026-10-27 · [原帖](https://x.com/miles_mazy/status/2115072333832749202)

- 群里有人叫我删了，咋办啊？
  - 正文只有这一句，主要内容在配图里


- 图片：[img1](https://pbs.twimg.com/media/HVo_CthWUAAYOzd?format=jpg&name=large)

[↑ 回到目录](#part-1--keywords)

### x-2114629460930740466

**Roc (@AIStarsGo)** · 发帖 2026-10-26 · [原帖](https://x.com/AIStarsGo/status/2114629460930740466)

- **几条教训**
  1. **不要依赖 agent 读论文或高质量博文**
     - 后果：思维深度大幅下降，灵感触发时机大幅减少
     - 还会浪费大量时间去理解 agent 的垃圾表达
  2. **不要把搞科研/技术学习和英语学习混在一起**
     - 后果：效率低、推进慢，失去耐心后放弃
     - 灵感和思考需要时间积累，混着学英语会大幅延迟思考，让脑子在两个任务间来回切换
  3. **不要因为 token 用不完就 background 跑点东西，想着"用掉不影响主线"**
     - 后果：除非你已编好稳定的 workflow，否则即时奖励更强的 vibe coding 一定会吸引注意力，打断深度思考
- **总结：要感受自己在 agent 时代的认知提升速度** —— 是加快了、不变，还是退步了
  - 否则会沉迷 shallow work，最终认知退化，对读长文字、深度思考都没耐心

<details><summary>原文</summary>

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

</details>


[↑ 回到目录](#part-1--keywords)

### x-2114099234001600931

**smerkzz (@0xsmerkzz)** · 发帖 2026-10-24 · [原帖](https://x.com/0xsmerkzz/status/2114099234001600931)

- **Quote attributed to SpaceXAI engineer Lauren Tan**
  - Runs 35+ GrokBot agents with `/loop` and `/goal` inside **pstack**; the bots ship code even while she sleeps
  - At SpaceXAI, 85% of engineers run 11+ GrokBot agents as a team
  - She has a **Chief of Staff agent** that knows the other agents and manages everything
- A 1-hour workshop shows how to build a team of GrokBot agents from scratch

<details><summary>原文</summary>

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

</details>

- 含视频（未转写）

[↑ 回到目录](#part-1--keywords)

### x-2113948384113598588

**Sumanth (@Sumanth_077)** · 发帖 2026-10-24 · [原帖](https://x.com/Sumanth_077/status/2113948384113598588)

- 🔖 也在 Notes 里，全文见：[Google 开源 Harness²：递归改进 agent harness](01-harness-loop.md#x-2113948384113598588)

[↑ 回到目录](#part-1--keywords)

### x-2113634548378374458

**Annatar.md (@AnnatarXBT)** · 发帖 2026-10-23 · [原帖](https://x.com/AnnatarXBT/status/2113634548378374458)

- 🔖 也在 Notes 里，全文见：[Wavestone：11 个 coding agent 共有的 7 部分 harness](01-harness-loop.md#x-2113634548378374458)

[↑ 回到目录](#part-1--keywords)

### x-2106453816757354947

**Sergii Makarevych (@sermakarevich)** · 发帖 2026-10-03 · [原帖](https://x.com/sermakarevich/status/2106453816757354947)

- 🔖 也在 Notes 里，全文见：[Evals：如何判断一个 AI 系统真的可用](04-evals-research.md#x-2106453816757354947)

[↑ 回到目录](#part-1--keywords)

### x-2104453599367770287

**meng shao (@shao__meng)** · 发帖 2026-09-28 · [原帖](https://x.com/shao__meng/status/2104453599367770287)

- 🔖 也在 Notes 里，全文见：[Stanford CS329A：Self-Improving AI Agents 课程](08-llm-courses.md#x-2104453599367770287)

[↑ 回到目录](#part-1--keywords)

### x-2101308432305254889

**Morty (@0xMortyx)** · 发帖 2026-09-19 · [原帖](https://x.com/0xMortyx/status/2101308432305254889)

- **Jev doesn't make the LLM smarter** — it makes decisions 193x faster, 444x cheaper, and testable
  - Pitched as the missing **decision layer** between LLM reasoning and real-world agent execution
- **Without a decision layer**, you usually solve it with more prompting → more context → more retries → more tokens
- **Jev makes the fork explicit — for every state:**
  - **Choice** → which route wins?
  - **Score** → how good is each option?
  - **Noul** → how likely is the condition true?
- Execution then stays **outside the model**
- **引用 / Quoted:** @0xRicker
  - Jev could become the control layer AI agents have been missing
  - Instead of 5–20 seconds and expensive LLM calls to decide every next step, it routes actions in milliseconds at near-zero cost

<details><summary>原文</summary>

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

</details>

- 图片：[img1](https://pbs.twimg.com/media/HSlT6boWQAIypkN?format=jpg&name=large)

[↑ 回到目录](#part-1--keywords)

### x-2083131009986396282

**Khairallah AL-Awady (@eng_khairallah1)** · 发帖 2026-07-31 · [原帖](https://x.com/eng_khairallah1/status/2083131009986396282)

- 🔖 也在 Notes 里，全文见：[How to Become a Graph Architect With Zero Experience (Full Course)](02-graph-multi-agent.md#x-2083131009986396282)

[↑ 回到目录](#part-1--keywords)

### x-2082413202353406091

**The Code Newsletter (@CodeNewsletter)** · 发帖 2026-07-29 · [原帖](https://x.com/CodeNewsletter/status/2082413202353406091)

- 🔖 也在 Notes 里，全文见：[The Code newsletter 推广](10-misc.md#x-2082413202353406091)

[↑ 回到目录](#part-1--keywords)

### x-2085421662447468758

**Anatoli Kopadze (@AnatoliKopadze)** · 发帖 2026-08-06 · [原帖](https://x.com/AnatoliKopadze/status/2085421662447468758)

- 🔖 也在 Notes 里，全文见：[Anthropic：让系统自己 prompt 自己](01-harness-loop.md#x-2085421662447468758)

[↑ 回到目录](#part-1--keywords)

### x-2079636027736457707

**Carnage (@0xCarnagee)** · 发帖 2026-07-21 · [原帖](https://x.com/0xCarnagee/status/2079636027736457707)

- 🔖 也在 Notes 里，全文见：[Graph Engineering with Claude: 12 steps from a single loop to a self-verifying fleet](02-graph-multi-agent.md#x-2079636027736457707)

[↑ 回到目录](#part-1--keywords)

### x-2085024744387092973

**Mahax (@Mahaximus_)** · 发帖 2026-08-05 · [原帖](https://x.com/Mahaximus_/status/2085024744387092973)

- **Most people use AI at one speed**: ask → read → fix → ask again
  - It works, but it is the slowest way to do it
- **The faster setup has three parts**
  - **Agent** — plans and acts without being walked through each step
  - **Loop** — runs until the work actually clears the bar
  - **Graph** — parallel workers that handle what a single prompt never could
- Claude runs all three; most people never find out
  - Not because it's complicated — because nobody put all three parts in one place
- What this covers: what agents, loops, and graphs are, how each builds on the last, when they're worth using vs. a trap, and how to build all three with prompts and code you can use today
- **AGENTS**
- **1 - What an agent actually is**
  - "Summarize this article" is **not an agent** — that is a chat
  - "Find the three most cited papers on this topic, pull the key claims from each, cross-check them against each other, and write me a one-page briefing" — done with no touch from you in between — **that is an agent**
  - **The difference is not the model. It is the structure around it.**
  - An agent has three things a regular chat does not:
    - **Tools it can call on its own** — search, file systems, code execution, external APIs. It doesn't wait for you to get the information; it goes and gets it
    - **Memory that carries across tasks**, not just within one session. It knows what it already tried, what worked, what it decided earlier
    - **A loop that keeps running until the task is finished**, not until it generates one response. It does not hand the work back to you at every step
  - With all three in place, Claude stops being something you talk to and starts being something that works
- **2 - The levels of agentic work**
  - You don't need a fully autonomous agent on day one
  - There are levels, and each is already more powerful than what most people run
  - **Level 1 – Chat**
    - You ask, Claude answers, the session ends
    - No tools, no memory, no ongoing goal
    - You are the engine; Claude is the tool in your hand
  - **Level 2 – Claude with tools**
    - Claude searches the web before answering, reads a file, or runs code to check its work
    - Already slightly agentic: you didn't tell it to do those step by step — it decided it needed to
  - **Level 3 – Multi-step workflows**
    - You give a goal; Claude breaks it into steps, executes each, checks the result, delivers a finished output
    - You are not involved between steps
  - **Level 4 – Fully autonomous**
    - Runs on a schedule or trigger, monitors inputs, calls external services, completes complex tasks with no human in the loop
    - You set the goal once and check the output
  - **Level 1 vs. level 4 is not a different model** — it's what surrounds the model: tools, memory, and a loop
    - Add one at a time and you move up a level
- **3 - Three agents you can build today**
  - The agent type determines the system prompt you give it
  - These three cover most real needs: copy the one that fits, adjust details, paste it in as the system prompt
  - **Research agent**
  ```text
  You are a research agent. Your job is to find what actually matters, not just what exists.

  When given a research task:
  1. Break it into 3-4 specific sub-questions worth answering
  2. Search each one independently
  3. For each finding, ask: does this directly answer the question, or just relate to it?
  4. Keep only what directly answers. Discard the rest.
  5. Deliver a structured summary: key findings, the source behind each one, and what you could not find

  Rules:
  - Every claim needs a source. No exceptions.
  - If two sources contradict each other, flag it — don't pick a side.
  - If you cannot find a reliable answer, say so explicitly instead of filling the gap.
  ```
  - **Data analysis agent**
  ```text
  You are a data analysis agent. Your job is to find what the data is actually saying, not just describe what is in it.

  When given a dataset or numbers:
  1. Identify what kind of data this is and what questions it can realistically answer
  2. Look for patterns, outliers, and trends - not averages alone
  3. For every finding, ask: is this interesting or is this obvious? Cut the obvious.
  4. Flag anything that looks wrong - missing values, suspicious spikes, inconsistencies
  5. Deliver findings ranked by importance, not by where they appear in the data

  Rules:
  - Never describe what the data contains. Interpret what it means.
  - If a number is surprising, explain why it is surprising.
  - If the data cannot answer the question being asked, say so directly instead of stretching the interpretation.
  - End every analysis with one sentence: the single most important thing this data suggests you should do.
  ```
  - **Code agent**
  ```text
  You are a code agent. Your job is to produce working code, not promising code.

  When given a coding task:
  1. State your understanding of what the code must do before writing anything
  2. Write the solution with clear comments explaining each section
  3. Identify edge cases that could break it
  4. If there are errors, debug them before asking for help

  Rules:
  - Write clean code with meaningful variable names
  - Always include error handling
  - If the requirements are unclear, make a reasonable assumption, state it, and continue
  - Never deliver code you have not mentally traced through at least once

  When you find a bug: explain what caused it in one sentence, then fix it. Do not just fix it silently.
  ```
- **4 - The memory problem and how to fix it**
  - The most common place agents break down — in three specific ways:
    - **Task runs too long and the agent loses the beginning** — the original goal, decisions made, constraints you set all fall out of the context window. The agent keeps working but has quietly forgotten what it was working toward
    - **You close the session and open a new one** — the agent starts from zero; everything from the previous run is gone
    - **The agent gets interrupted mid-task** — when you come back, it has no record of where it stopped, what it tried, or what failed
  - **All three have the same fix: make the agent write its own memory**
  - Paste this **mid-task** to create a progress record:
  ```text
  Before we continue, write a checkpoint:
  1. What have you completed so far?
  2. What decisions were made and why?
  3. What still needs to happen?
  4. What would you need to resume this in a new session?

  Keep it under 150 words. Be specific - vague checkpoints are useless.
  ```
  - Paste this **when a session is getting long**:
  ```text
  The conversation is getting long. Compress what matters into a summary:
  1. The original goal
  2. What has been done and what was found
  3. Key decisions made
  4. What still needs to happen

  After writing the summary, continue from there. Treat it as the new starting point.
  ```
  - Paste this **at the start of a new session** to restore context:
  ```text
  We are resuming from a previous session. Here is the context:

  [paste your checkpoint here]

  Confirm your understanding of where we are, identify the next step, and continue without repeating work already done.
  ```
  - For any agent you run regularly: **put the facts it always needs directly into the system prompt**
    - Claude reads the system prompt at the start of every session
    - So anything there is always in context, however long the conversation runs
- **LOOPS**
- **1 - What a loop actually is**
  - A **prompt** hands Claude one instruction and waits for you to decide what happens next
  - A **loop** hands Claude a goal and lets it figure out how to get there
  - In practice: a prompt stops when Claude generates something; **a loop stops when the task is actually done**
  - Every loop runs the same cycle:
  ```text
  PLAN    -  work out what the task actually requires
  EXECUTE -  do the work
  CHECK   -  measure the result against the goal
  ITERATE -  if it didn't pass, find the weakest part and fix it
  STOP    -  when it passes, or when a hard limit is reached
  ```
  - Three of those five steps are where most loops either work or fall apart
  - **The check is what makes it real**
    - Without a genuine test on the output, you don't have a loop — just Claude producing drafts and calling them done
    - The check turns repetition into progress
    - It must be something that can actually fail: a test that passes or doesn't, a score that clears a threshold, a rubric with hard criteria
    - **A soft check is no check at all**
  - **The stop condition keeps it from running forever**
    - Every loop needs two ways to stop: the task is done, or a hard limit was hit
    - "After 8 attempts, stop and report what happened" is not optional
    - It prevents a loop from quietly billing you while it spins on a problem it cannot solve
  - **Prompt + three things = a loop**:
    - A real test that can fail the output
    - A record of what already ran
    - A ceiling on how many tries it gets
  - Leave any one out and you have something that looks like a loop and costs like one
- **2 - Is it actually worth it?**
  - Most articles sell the loop before telling you when it's a mistake
  - **A loop is worth building only when all four are true at once:**
    - **You'll run it again** — regularly, not eventually; a one-off task doesn't earn a loop
    - **The work can grade itself** — there's a check that doesn't need your eyes; a condition that passes or fails without you
    - **You hand it the goal and it hands you the result** — if it needs you to step in mid-way, it's not a loop
    - **The finish line is a fact, not a feeling** — if "good enough" requires judgment, a loop can't make that call
  - Miss any one of the four and the loop costs more than it saves
  - Most people don't need the heavy version of a loop yet
    - What almost everyone can use right now: a **self-checking loop** — no scheduling, no infrastructure, no cost beyond normal usage
- **3 - Build a loop yourself**
  - No server, scheduler, or special setup needed — the whole thing fits in a single prompt
  - Paste this into Claude and replace the brackets:
  ```text
  Work in a loop until the output clears every criterion below. Do not stop early.

  GOAL:
  [describe exactly what you want produced]

  CRITERIA — be specific, no soft passes:
  - [what good looks like, measurable]
  - [what good looks like, measurable]
  - [what good looks like, measurable]

  EACH PASS:
  1. DRAFT - produce or improve the work
  2. SCORE - rate the result 1–10 against each criterion, be harsh
  3. GAPS - list exactly what is still weak
  4. CALL - if every score is 8 or above, write DONE and stop.
     If not, write NEXT PASS and fix the weakest gap first.

  RULES:
  - Never call it done until every criterion clears 8.
  - Each pass fixes the single weakest score from the last round.
  - No questions. Make a reasonable assumption, note it, keep going.
  ```
  - What happens: Claude drafts → scores its own output against your criteria → finds the weakest point → rewrites → repeats until it clears the bar
    - Not until it looks reasonable — **until it passes**
  - That is a loop, built with one prompt
  - **Caveat: you are still the trigger**
    - You opened the chat and pasted the prompt; close the tab and it stops
    - No schedule, no "run this every morning"
    - For that you need the next layer — where most people either build the full version or realise they didn't need it
- **4 - The order that works + the cost**
  - A specific order keeps loops from breaking in production — almost everyone skips a step
  - **Step 1 · Run it manually first**
    - Complete the task by hand inside a single conversation before automating anything
    - If it doesn't work reliably there, it won't on a schedule — it will just fail faster and cost more
  - **Step 2 · Lock what worked into a reusable template**
    - Save the instructions, criteria, and rules so you can call them again without rebuilding
    - A loop that lives inside one chat dies when the chat closes
  - **Step 3 · Add the gate (check) and the stop condition**
    - The check that can fail the output + the hard limit on attempts
    - Without both, you have an automated way to spend money, not a loop
  - **On cost: loops are not cheap**
    - Every iteration sends the full context back through the model: the goal, previous output, score, what failed
    - That pile grows every pass
    - Ten runs doesn't cost ten prompts — it costs **ten prompts that keep getting longer**
  - **The number to track is keep rate, not total tokens**
    - If a loop runs ten times and you discard six results, you paid for ten to get four
    - **Below a 50% keep rate, the loop costs more than doing it yourself**
- **GRAPHS**
- **1 - What a graph actually is**
  - Not a chart, not a visualization
  - **A graph in AI work is a map of which jobs need to happen and what each one depends on**
  - Two things make up the whole structure:
    - **Node** — one unit of work: one agent, one task, one defined input, one defined output
    - Not "research this topic, summarize it, then write a draft" — just one of those. The smaller and more bounded the job, the more useful the node
    - **Edge** — a dependency: connects two nodes when the second genuinely needs what the first produced
    - Not just when one happens to come after the other — this distinction matters more than it sounds
  - Everything else in graph engineering is applying those two ideas at different scales
  - **What makes a node usable: a defined output shape**
    - A node that returns free text is only readable by a human
    - A node with a fixed output is readable by the next node — no human needed in the middle
  ```text
  JOB: research one competitor's pricing - one task, nothing else
  IN: { competitor: "name", url: "https://..." }
  OUT: { price: number, plan: string, source: url, date: "YYYY-MM-DD" }
  RULE: if the output doesn't match this shape, reject and retry
  ```
  - That contract is what lets a graph run without you managing every handoff
- **2 - The fake edge test**
  - **Sequence vs. dependency**
    - **Sequence** = the order you typed things in — you invented it
    - **Dependency** = a task genuinely cannot start without something the previous one produced — it already exists; the graph just makes it visible
  - Most workflows have both; most people never separate them
  - **The test (five minutes on any workflow you already run):**
    1. Write every step as a box
    2. Draw an arrow between each consecutive pair
    3. For every arrow ask: **does the data produced by this step actually flow into the next one?**
  - **Yes** → keep the arrow; it's a real dependency
  - **No** → delete it; those two steps are unrelated and can run at the same time
  - Anything with no incoming arrow can start immediately
  - Anything with no outgoing arrow is a final output
  - You'll find two or three fake edges in almost any workflow
    - Each is time handed away for free — tasks queued behind work they never needed
- **3 - The Diamond**
  - Once you remove fake edges, one shape appears more than any other
    - Work splits into several independent jobs that run at the same time
    - They all feed one final step that pulls their outputs together
    - Drawn out it looks like a diamond: wide in the middle, narrow at both ends
  - **Formal name: fan out, then converge**
  - **Example: researching three competitors**
    - Linear: finish the first, start the second, finish it, start the third
    - Diamond: run all three at once, wait only for the slowest, then synthesize
    - Same inputs, same outputs, a fraction of the time
  - **Why it works: the edge structure**
    - The synthesis step has a real dependency on all three research outputs — those edges exist
    - The three research jobs have no dependency on each other — those edges don't
    - So they run in parallel; the only wait is at the end, where it's unavoidable anyway
  - **Two conditions must hold:**
    - The parallel jobs must be **genuinely independent** — no hidden shared resources, no fake independence
    - The convergence step must **actually need all of them** — if it needs only one, the others are wasted work
  - What the diamond looks like:
  ```python
  # the diamond — one pattern, any job

  angles = [
      "pricing vs the top 3 competitors",
      "what buyers complain about in reviews",
      "gaps the market hasn't filled yet",
  ]

  # FAN OUT — one worker per angle, all at once
  raw = run_in_parallel([
      agent(task=f"research: {a}. every claim needs a source and date.")
      for a in angles
  ])

  # REDUCE — plain code, no model, no tokens spent
  findings = deduplicate(filter(None, raw))

  # VERIFY — a fresh skeptic per finding, tries to disprove it
  survivors = [
      f for f, verdict in zip(findings, run_in_parallel([
          agent(task="try to disprove this. return keep or drop.",
                input=f,
                fresh_context=True)
          for f in findings
      ]))
      if verdict == "keep"
  ]

  # SYNTHESIZE — one agent writes from what survived
  return agent(task="one report, ranked by confidence, sources attached.",
               input=survivors)
  ```
- **4 - The checker**
  - **The agent that wrote the output is the worst possible judge of it**
    - Not because it's dishonest — it cannot see its own blind spots
    - The same reasoning that produced the mistake is being used to check for it
    - Every serious study on AI self-review lands on the same finding: models miss most of their own errors
  - **Rule: the agent that does the work never checks the work**
  - Put a separate node between your workers and your final step
    - Its only job: try to break each finding before it moves forward
    - Not to improve it or summarize it — to find the reason it should be dropped
  - **The thing most people miss: the checker needs a completely fresh context**
    - Give it the worker's conversation and it isn't checking — it's nodding along to the same reasoning in a different window
    - A verifier that shares context with the worker is the same agent pretending to be two
  - **Split the check three ways** — three different questions, each trying to kill the finding from a different angle
  ```text
  VERIFIER NODE

  INPUT: the finding only — never the worker's conversation
  CONTEXT: fresh and empty, has not seen the work it is judging

  THREE CHECKS, run in parallel:
  1. Is it correct? Does the claim actually hold up?
  2. Is it current? Is the source recent, not something stale?
  3. Is the source real? Does the link resolve to what it claims?

  PASS: keep the finding if the majority of checks clear
  FAIL: drop it before it reaches the final step
  ```
  - **A worker and its checker must never share a context**
    - The moment they do, you're back to one agent grading its own homework — with a bigger bill
- **5 - Build one yourself**
  - Everything above is a mental model until you give Claude something it can run
  - **One word changes how Claude processes your instructions: `workflow`**
    - Without it: Claude reads the prompt as a sequence and executes steps one after another
    - With it: Claude writes a short coordination script, identifies nodes with no dependencies, and runs those in parallel automatically
    - You describe the graph; Claude figures out the execution order
  - Templates to paste directly into Claude Code and adapt — replace anything in brackets
    - The structure stays the same regardless of what's inside the nodes
  - **Competitive research:**
  ```yaml
  workflow: competitive-research

  nodes:
    research_a:
      task: "Research [Company A]. Cover pricing, core features,
             recent changes, public sentiment. Output a structured summary."
      output: company_a.md

    research_b:
      task: "Research [Company B]. Cover pricing, core features,
             recent changes, public sentiment. Output a structured summary."
      output: company_b.md

    research_c:
      task: "Research [Company C]. Cover pricing, core features,
             recent changes, public sentiment. Output a structured summary."
      output: company_c.md

    checker:
      task: "Review all three summaries. Flag anything incomplete,
             outdated, or off-topic."
      depends_on: [research_a, research_b, research_c]
      output: checker.md

    synthesize:
      task: "Using the summaries and checker report, write a comparison
             across price, features, and positioning."
      depends_on: [checker]
      output: comparison.md
  ```
  - **Multi-file code review:**
  ```yaml
  workflow: code-review

  nodes:
    review_auth:
      task: "Review auth.py for security issues, edge cases,
             and code quality. Be specific."
      output: review_auth.md

    review_api:
      task: "Review api.py for security issues, edge cases,
             and code quality. Be specific."
      output: review_api.md

    review_db:
      task: "Review db.py for security issues, edge cases,
             and code quality. Be specific."
      output: review_db.md

    checker:
      task: "Read all three reviews. Flag issues appearing in more than
             one file. Note cross-file dependencies that could cause problems."
      depends_on: [review_auth, review_api, review_db]
      output: checker.md

    summary:
      task: "Write a prioritized fix list — critical first,
             then medium, then low."
      depends_on: [checker]
      output: final_review.md
  ```
  - **The `depends_on` line is the only thing you need to understand to design any graph**
    - No dependencies → parallel
    - A dependency → wait
- **What you now have: three concepts, one model**
  - **Agent** — gives Claude a goal instead of an instruction and lets it work toward it on its own
  - **Loop** — makes that work reliable: it checks itself, records what failed, and keeps going until it clears the bar
  - **Graph** — makes it fast: independent jobs run in parallel and converge into one answer at the end
  - Each one builds on the last
  - You don't need all three for every task
    - But once you can see which one a task needs, you stop working harder and start designing better

<details><summary>原文</summary>

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

</details>

- 图片：[img1](https://pbs.twimg.com/media/HO5t8UXWsAAJrRf?format=jpg&name=large) [img2](https://pbs.twimg.com/media/HO5hp7fXQAAmVK8?format=jpg&name=large) [img3](https://pbs.twimg.com/media/HO5hPC9XgAAwRF2?format=jpg&name=large) [img4](https://pbs.twimg.com/media/HO5guyAW0AEJC9C?format=jpg&name=large)

[↑ 回到目录](#part-1--keywords)

### x-2083602508807569560

**codila (@0xCodila)** · 发帖 2026-08-01 · [原帖](https://x.com/0xCodila/status/2083602508807569560)

- 🔖 也在 Notes 里，全文见：[Google 2 小时课程：1 prompt → 100 agents → loops → graphs](02-graph-multi-agent.md#x-2083602508807569560)

[↑ 回到目录](#part-1--keywords)

### x-2071649423042412597

**Anatoli Kopadze (@AnatoliKopadze)** · 发帖 2026-06-29 · [原帖](https://x.com/AnatoliKopadze/status/2071649423042412597)

- 🔖 也在 Notes 里，全文见：[Spotify：引入 loop 后 agent 成功率 20–30% → 80%](01-harness-loop.md#x-2071649423042412597)

[↑ 回到目录](#part-1--keywords)

### x-2071214176526049739

**Movez (@0xMovez)** · 发帖 2026-06-28 · [原帖](https://x.com/0xMovez/status/2071214176526049739)

- 🔖 也在 Notes 里，全文见：[前 Google 工程师：agent loop + harness + evals 技术栈](01-harness-loop.md#x-2071214176526049739)

[↑ 回到目录](#part-1--keywords)

### x-2069734857626833371

**gxjo (@gxjo_dev)** · 发帖 2026-06-24 · [原帖](https://x.com/gxjo_dev/status/2069734857626833371)

- Somebody built **traffic lights for Claude Code**


- 图片：[img1](https://pbs.twimg.com/media/HLks4Q_X0AAKXK2?format=jpg&name=large)

[↑ 回到目录](#part-1--keywords)

### x-2068763235587694769

**Movez (@0xMovez)** · 发帖 2026-06-21 · [原帖](https://x.com/0xMovez/status/2068763235587694769)

- **Quote attributed to Andrew Ng**
  - "100% of my tasks are now done by AI agents — hype has exceeded my expectations"
  - **Loops** are the next step
  - In 3–6 months everyone will use self-improving loops; no more prompting
- In a 30-minute talk he explains how to build self-improving agentic systems from scratch

<details><summary>原文</summary>

> Andrew Ng:
>
> "100% of my tasks are now done by AI agents - hype has exceeded my expectations. Loops is next step.
>
> in 3-6 months, everyone will be using self-improving loops. No more prompting."
>
> In a 30-minute talk, Andrew Ng explains how to build self-improving agentic systems from scratch.
>
> Worth more than a $500 agentic course.

</details>

- 含视频（未转写）

[↑ 回到目录](#part-1--keywords)

### x-2068325550603559402

**GREG ISENBERG (@gregisenberg)** · 发帖 2026-06-20 · [原帖](https://x.com/gregisenberg/status/2068325550603559402)

- **The most valuable skill sets right now**
  1. People who can set up agents properly, manage them, and run local AI models
  2. Marketers who know how to build distribution
  3. Robotics engineers who can do all three: build the hardware, wire in the AI, source manufacturing
  4. Curators who are good at talking and can do short-form video in their sleep
  5. **The builder-distributor** — one person who can both ship the product and get it in front of people
  6. IRL community builders

<details><summary>原文</summary>

> The most valuable skill sets on the planet right now:
>
> 1. people who can set up agents properly, manage them, and run local AI models
> 2. marketers who know how to build distribution
> 3. robotics engineers who can do all three: build the hardware, wire in the AI, and source manufacturing etc
> 4. curators who are good at yapping and can do short form video in their sleep
> 5. the builder-distributor. The one person who can both ship the product AND get it in front of people
> 6. IRL community builders

</details>


[↑ 回到目录](#part-1--keywords)

### x-2066827221537333611

**Khairallah AL-Awady (@eng_khairallah1)** · 发帖 2026-06-16 · [原帖](https://x.com/eng_khairallah1/status/2066827221537333611)

- **Claim**: Anthropic pays $750,000+ a year for engineers who can **build LLMs from scratch**
  - Not prompting, not fine-tuning, not building RAG pipelines
- **A free 2-hour Stanford lecture covers the theory**
  - Scaling laws
  - Data collection
  - Architecture design
  - Post-training alignment

<details><summary>原文</summary>

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

</details>

- 含视频（未转写）

[↑ 回到目录](#part-1--keywords)

### x-2063985608381362576

**Anatoli Kopadze (@AnatoliKopadze)** · 发帖 2026-06-08 · [原帖](https://x.com/AnatoliKopadze/status/2063985608381362576)

- **Everyone is talking about AI agents, but most definitions are vague** ("AI that does things autonomously")
  - The more useful picture: **agents are not a category — they are a spectrum**
- **This guide covers**
  - Where different AI tools sit on that spectrum
  - What separates a basic LLM interaction from a true agentic workflow
  - How to build your own agent with **Claude Code** and connect it to **Telegram** — without writing code yourself
- **What Makes Something an Agent**
  - Asking Claude "what should I post today?" is **not an agent** — that's a chat
  - Telling Claude "find the three topics trending in AI right now, pick the one with the most engagement potential, draft a post in my style, and save it to a file" — and it does all of it without you touching anything — **that is an agent**
  - **The difference is not the model. It is the structure around it.**
  - **An agent has three things a regular chat does not**
    - **Tools** it can call on its own — search, file systems, code execution, external APIs
    - **Memory** that persists across tasks, not just within one session
    - **A loop** that keeps running until the task is finished, not until it generates one response
  - The more of these three you add, the less you are involved — that is the idea
- **The Spectrum: From Chat to Agent**
  - **Basic chat** — you ask, Claude answers, the session ends
    - No tools, no ongoing goal, no ability to act in the world
  - **Claude with tools enabled** — already slightly agentic
    - When it searches the web before answering, reads an attached file, or generates an image, it decided on its own that it needed to
  - **Multi-step workflows** — you give a goal; Claude breaks it into steps, executes each, checks the result, delivers a finished output
    - You are not involved between steps
  - **Fully autonomous agents** — runs on a schedule, monitors inputs, calls external services, completes complex tasks with no human in the loop
    - You set the goal once and check the output
  - **Bottom vs. top is not a different model** — it's what surrounds the model: tools, memory that carries context, and a loop that runs until done
- **Types of Agents You Can Build Today**
  - Examples only — not limits; build whatever fits your situation
  - **Research agent** — gathers information on a topic, reads multiple sources, pulls out what matters, delivers a structured summary
    - You give it a question; it gives an answer that would have taken hours to compile manually
  - **Writing agent** — writes content according to a system you define
    - Give it your tone, format, audience, topic; it handles drafts, rewrites, edits without you managing every sentence
  - **Code agent** — writes code, runs it, reads the errors, fixes them, keeps going
    - You describe what the code should do; the agent handles implementation and the debugging loop
  - **Business agent** — handles repetitive business tasks: drafting emails, processing customer requests, qualifying leads, generating reports
    - Runs on autopilot once you define the rules
  - **Personal agent** — manages your schedule, organizes tasks, prepares briefings, handles daily planning work
- **Building Your First Agent — Start Here**
  - You'll use Claude Code to build a **Telegram bot that runs on a remote server and uses Claude as its brain**
  - Claude Code writes all the code; you describe what you want in plain English
  - Once set up, all communication with the bot happens through Telegram
  - Takes about **10–20 minutes**; no coding knowledge needed
- **System Prompt Templates — Paste Into Prompt 2**
  - When you run Prompt 2 from the setup below, you describe what kind of agent you want
  - Copy the template that fits, paste it into Prompt 2 where it says "The agent should be:", and Claude Code builds that agent
  - Adjust details to match your situation
  - **Research Agent**
  ```text
  You are a research agent. Your job is to gather, analyze, and synthesize information on any topic I give you.

  When given a research task:
  1. Identify the 3-5 most important sub-questions to answer
  2. Search for information on each one
  3. Evaluate the quality and relevance of each source
  4. Extract only what directly answers the question
  5. Deliver a structured summary with: key findings, supporting evidence, and gaps you could not fill

  Format: Use headers, bullet points, and clear sections.
  If you are uncertain about something, say so explicitly.
  Do not add filler. Every sentence should contain information.
  ```
  - **Writing Agent**
  ```text
  You are a writing agent. You write content in my voice and style.

  My style:
  - Conversational, direct, no corporate language
  - Short sentences and paragraphs
  - Specific numbers and examples over vague claims
  - Always end with something the reader should do or think about

  When given a writing task:
  1. Ask for the topic, audience, and desired length if not provided
  2. Write a first draft
  3. Review it against my style rules
  4. Deliver the final version ready to publish

  Never add unnecessary introductions. Start with the most important point.
  ```
  - **Code Agent**
  ```text
  You are a code agent. Your job is to write, debug, and improve code.

  When given a coding task:
  1. Confirm your understanding of what the code should do
  2. Write the solution with clear comments
  3. Identify any edge cases or potential failures
  4. If there are errors, debug them systematically before asking for help

  Rules:
  - Write clean, readable code with meaningful variable names
  - Always include error handling
  - Explain what each major section does in plain language
  - If you are unsure about requirements, ask one clarifying question before proceeding
  ```
  - **Business Email Agent**
  ```text
  You are a business email agent. You write professional emails on my behalf.

  My communication style:
  - Direct and respectful
  - No unnecessary formalities
  - Gets to the point in the first sentence
  - Closes with a clear next step

  When given an email task:
  1. Identify the goal of the email (inform, request, follow up, confirm)
  2. Write a subject line that reflects the email's purpose
  3. Draft the email in 3-5 short paragraphs maximum
  4. End with one clear action item or next step

  Always write ready-to-send emails, not templates with blanks to fill in.
  ```
  - **Personal Planning Agent**
  ```text
  You are my personal planning agent. You help me organize my work, prioritize tasks, and plan my week.

  When I share my tasks or goals:
  1. Identify what is urgent vs. important
  2. Suggest a realistic sequence based on dependencies
  3. Estimate time required for each task
  4. Flag anything that could be delegated or eliminated

  When I describe a project:
  - Break it into concrete next actions
  - Identify the single most important thing to do first
  - Create a simple checklist I can follow

  Keep everything practical. No motivational filler. Just the plan.
  ```
- **What You Need Before Starting**
  1. **A Claude API key** from `console.anthropic.com`
     - A developer key: you pay per usage, not a fixed monthly fee
     - A personal bot sending 50 messages a day costs **$1–5/month**, depending on model
  2. **A Telegram bot token** from **BotFather**
  3. **A VPS running Linux**
     - A personal bot needs little: **1 CPU, 1GB RAM, 20GB storage** is more than enough
     - Any basic plan from **DigitalOcean, Hetzner, or Vultr** works — around **$4–6/month**
     - Once you have the server, install Claude Code:
     ```bash
     npm i -g @anthropic-ai/claude-code
     ```
- **Which Claude model to use for your bot**
  - **Sonnet 4.6** — the right choice for most personal bots; strong enough for any task, affordable for daily use
  - **Haiku 4.5** — if you want to minimize cost
  - **Opus 4.8** — only for a complex analytical agent where answer quality is critical
- **Building Your First Agent — Step 1**
  - Open your VPS terminal, launch Claude Code, paste the prompt, and let it build everything
  - **Give the agent a personality**
  ```text
  Build me a Telegram bot that uses the Claude API as its brain.

  Requirements:
  - Language: Python
  - Library for Telegram: python-telegram-bot
  - Claude model: claude-sonnet-4-6
  - The bot receives a message, sends it to Claude API, and returns Claude's response to Telegram
  - Maintain conversation history per user — each user has their own context within the session
  - Add a /start command that introduces the bot
  - Add a /clear command that resets conversation history for that user

  Create all necessary files: main bot file, requirements.txt, and a .env file template for API keys.
  Do not hardcode any API keys — read them from environment variables.
  ```
  - **Deploy as a background service**
  ```text
  Create a systemd service file so this bot runs automatically on my Linux VPS and restarts if it crashes.

  The service should:
  - Start automatically when the server boots
  - Restart automatically if it crashes
  - Load environment variables from the .env file in the project folder
  - Save logs to a file I can check later

  Also write me the exact terminal commands to install the service, start it, check if it is running, and view the logs.
  ```
  - **Add persistent memory between sessions**
  ```text
  The bot loses conversation history when it restarts. Fix this.

  Save each user's conversation history to a JSON file on disk after every message. Load it back automatically when the bot starts.

  Add a maximum history length — keep only the last 20 messages per user so the context window never gets too long.
  ```
- **Adding Skills to Your Claude Code Bot**
  - **Skills** are capabilities you add over time
  - Each one is a new prompt you give Claude Code; it writes the code to make it work
  - **Skill: Web search** — the agent looks up real-time information instead of answering from memory only
  ```text
  Add web search capability to the bot using the Tavily API.

  When the user asks something that requires current information — news, prices, recent events — the bot automatically searches the web and includes the results in its response.

  The bot should decide on its own when to search and when to answer from memory. Add TAVILY_API_KEY to the .env file template.

  Use Claude's tool use feature to implement this cleanly.
  ```
  - **Skill: Save notes** — the agent saves anything you tell it (ideas, tasks, research findings) to a file and retrieves it later
  ```text
  Add a note-saving feature to the bot.

  When the user says "save this", "remember this", or "note:", the bot saves the content to a notes.txt file with a timestamp.

  Add a /notes command that returns the last 10 saved notes.
  Add a /clearnotes command that deletes all saved notes.
  ```
  - **Skill: Restrict to your account only**
    - By default anyone who finds your bot can use it and consume your API credits; this locks it to you
  ```text
  Add user restriction to the bot so only I can use it.

  Add my Telegram user ID to the .env file as ALLOWED_USER_ID.
  If anyone else messages the bot, it responds with "This bot is private." and ignores all further messages from that user.

  Also add how I can find my own Telegram user ID — either through the bot itself or another method.
  ```
  - **Skill: Track API costs**
    - Claude API charges per token; this adds a simple tracker so you always know what you're spending
  ```text
  Add basic cost tracking to the bot.

  After each Claude API response, log the number of input tokens and output tokens used.
  Keep a running total in a costs.json file.

  Add a /costs command that shows: total tokens used today, total tokens used all time, and an estimated cost in USD based on claude-sonnet-4-6 pricing.
  ```
  - **Skill: Scheduled daily briefing** — the agent messages you every morning without being asked
  ```text
  Add a scheduled daily briefing to the bot.

  Every day at 8:00am, the bot sends me a message with:
  1. A motivational one-liner (short, not cheesy)
  2. A reminder to check my top priority for the day
  3. One random useful fact about productivity or AI

  Send it to my Telegram user ID from the .env file.
  Use the schedule or APScheduler library to implement this.
  ```
- **Useful Things to Know After Setup**
  - **Update your agent's personality**
    - Open the main bot file, find the system prompt variable at the top, change it, save
    - Restart the service: `sudo systemctl restart your-bot-name`
    - The new personality is live immediately
  - **Check if the bot is running**
    - Run `sudo systemctl status your-bot-name`
    - "active (running)" → it's working; "failed" → check the logs
  - **Read logs**
    - Run `journalctl -u your-bot-name -n 50` to see the last 50 lines
    - This is where you find error messages if something breaks
  - **Add a new skill**
    - Open Claude Code in your project folder and describe it: "Add X feature to the bot."
    - Claude Code reads your existing code, adds the feature cleanly, and tells you if a restart is needed
- **The Memory Problem Every Agent Has**
  - **The most common problem**: the agent loses context — between sessions, across long tasks, after too many messages — and starts making mistakes or repeating work
  - **Three ways it happens**
    1. **Long tasks exceed Claude's context limit** — the agent loses the beginning: the original goal, decisions already made, constraints you set
    2. **New session = start from zero** — closing a session and opening a new one wipes context
    3. **Interrupted mid-task** — the agent has no way to know where it stopped
  - **Four fixes**
    1. **Progress notes** — tell the agent to write a note after every major step: what was done, what was decided, what still needs to happen
       - Paste that note at the start of the next session to restore full context
    2. **Periodic summaries** — every 10–15 messages, ask the agent to summarize where it is
       - Forces it to compress context before it overflows
    3. **Compress before it's too long** — ask the agent to compress everything into a short summary and continue from there
       - The thread stays intact
    4. **Put key facts in the system prompt** in your bot code
       - Claude reads it at the start of every conversation, so that information is always in context no matter how long things get
  - **Checkpoint Prompt**
  ```text
  Before we continue, write a brief checkpoint:
  1. What have you completed so far?
  2. What are the key decisions or findings from this session?
  3. What still needs to be done?
  4. What context would you need to continue this task in a new session?

  Keep it under 200 words.
  ```
  - **Memory File Prompt**
  ```text
  After completing each major step, write a memory note in this format:

  STEP COMPLETED: [what was done]
  KEY DECISIONS: [choices made and why]
  CURRENT STATE: [where the task stands now]
  NEXT STEP: [what should happen next]

  This note will be used to resume the task in a new session without losing context.
  ```
  - **Context Recovery Prompt**
  ```text
  We are resuming a task from a previous session. Here is the context:

  [paste your memory note here]

  Based on this:
  1. Confirm your understanding of where we are
  2. Identify the next step
  3. Ask any questions needed to continue

  Do not repeat work that has already been completed.
  ```
  - **Rolling Summary Prompt**
  ```text
  The conversation is getting long. Compress everything important into a summary:

  1. Original goal
  2. What has been done and what was found
  3. Key decisions made
  4. What still needs to happen

  After writing the summary, continue from there. Treat this summary as the new starting point.
  ```

<details><summary>原文</summary>

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

</details>

- 图片：[img1](https://pbs.twimg.com/media/HKS0qaGXoAAElVM?format=jpg&name=large) [img2](https://pbs.twimg.com/media/HKSnn-sXEAAL9fu?format=jpg&name=large)

[↑ 回到目录](#part-1--keywords)

### x-2066867539305459732

**Codez (@0xCodez)** · 发帖 2026-06-16 · [原帖](https://x.com/0xCodez/status/2066867539305459732)

- **Everyone's talking about loops; almost no one is talking about what the loop runs on**
  - 9 out of 10 builders run Claude Code on the **default harness** — no rules, no subagents, no hooks, no memory
  - Then they wonder why their loop produces slop
  - **A loop is only as good as the harness underneath it**
- This is a 14-step roadmap to the harness — from one agent to a system that improves itself
- **Loop engineering vs. harness engineering**
  - **Loop engineering** — building a system that prompts your agent on a schedule — got all the attention this month
  - **Addy Osmani**, who wrote the long-form piece on loops, pointed at what sits below it:
    - > "Loop engineering sits one floor above the harness. The harness is the environment one single agent runs inside. The loop is the harness, but it runs on a timer, spawns helpers, and feeds itself."
  - **Harness engineering** = designing that environment: the model, the tools, the permissions, the context, the memory
  - The unglamorous layer — and the one that decides whether everything above it works
  - **A great loop on a bad harness is a fast way to produce garbage at scale**
  - 14 steps, 3 tiers — the foundation everything else stands on
- **Part 1 · What a Harness Is**
- **01. A harness is the environment one agent runs inside**
  - Strip away the jargon and a harness is **four things**
    - The **model** doing the thinking
    - The **tools** it can reach
    - The **permissions** on those tools
    - The **context** it reads at the start of every run
  - That's the whole surface — subagents, hooks, memory are all ways of shaping one of those four
  - **Why harness matters more than people think**
    - The agent is a `while True` loop: pick a tool → run it → look at the result → decide the next move
    - The harness defines what tools exist, what the agent may do, and what it knows when it starts
    - **Same model, different harness, completely different agent**
- **02. The whole harness lives in one folder: `.claude/`**
  - Everything that shapes your agent sits in one directory at your project root
  - Learn this layout and you can read anyone's harness at a glance
  ```text
  .claude/
  ├─ CLAUDE.md          # standing facts — read every session
  ├─ settings.json      # permissions, model, hooks
  ├─ .mcp.json          # external tool connections
  ├─ rules/             # path-scoped behaviors
  │  ├─ tests.md
  │  └─ python-types.md
  ├─ agents/            # subagent definitions (~30 lines each)
  │  ├─ reviewer.md
  │  └─ eval-runner.md
  ├─ skills/            # reusable workflows
  │  └─ pr-checklist/
  │     └─ SKILL.md
  └─ agent-memory/      # what survives between runs
     └─ STATE.md
  ```
  - **The rule that separates a clean harness from a mess: keep it small enough that you can explain why every file exists**
    - If you can't say what a rule, hook, or subagent is for, delete it
- **03. Harness vs loop vs system — three floors, don't mix them**
  - Most "my agent setup is a mess" problems come from confusing the three floors
  - **Harness** — the runtime one agent lives in
    - Static configuration: model, tools, permissions, context (this issue)
  - **Loop** — prompts the agent on a timer, spawns helpers, feeds itself
    - Runs on top of the harness
  - **Self-improving system** — a loop plus memory that compounds
    - Every run leaves the next run sharper
  - **The practical version**
    - Standing facts → **context**
    - Enforcement → **hooks**
    - Procedures → **skills**
    - Isolation → **subagents**
  - Mixing these up (enforcement in `CLAUDE.md`, procedures bloating context) is the root cause of inconsistent, expensive agents
- **04. The default harness — what you get out of the box**
  - Install Claude Code, open a folder, and you already have a harness — just an empty one
  - **The default gives you**
    - A capable model
    - Built-in tools (read, write, bash, search)
    - Approval prompts on everything risky
  - **It lacks** project context, custom subagents, memory
  - For a one-off task, the default is fine
  - **For anything you do more than once**, the default leaves the agent:
    - Re-deriving your project from scratch every session
    - Asking permission for safe operations
    - Forgetting everything when you close the terminal
  - The next ten steps close that gap
- **05. `CLAUDE.md`: standing facts, kept short**
  - Read at the start of every session
  - The agent's standing knowledge of your project: conventions, architecture, the "we don't do it this way because of that incident"
  - **Most common mistake**: letting it grow into a giant procedures document that bloats every session
  - **Rule from practitioners running this daily: keep the main memory file under ~500 tokens**
    - Standing facts go here
    - Multi-step procedures go in **skills** (Step 8)
    - Path-specific behaviors go in **`rules/`** files scoped to where they apply
    - If a section has become a procedure rather than a fact, it belongs somewhere else
  - **Read your `CLAUDE.md` out loud**
    - Every line should be a fact the agent needs in every session ("we use pnpm, not npm")
    - A procedure ("to add a feature, first…") → move it to a skill
    - A rule for one folder → move it to `rules/`
- **06. `settings.json`: permissions and model, set once**
  - The default harness asks before every risky action
    - Right when you're watching; wrong when you're not
  - `settings.json` is where you pre-approve the safe stuff, deny the dangerous stuff, and pick which model runs
  ```json
  {
    "model": "claude-sonnet-4-6",
    "permissions": {
      "autoApprove": [
        "Read(*)", "Grep(*)",
        "Bash(npm test)", "Bash(git status)"
      ],
      "deny": [
        "Bash(rm -rf*)", "Bash(git push*)",
        "Edit(.env*)", "Edit(secrets/*)"
      ]
    }
  }
  ```
  - **The test for what to auto-approve: if this goes wrong, how hard is it to undo?**
    - Cheap to undo → auto-approve
    - Expensive to undo (force-push, deleting files, touching secrets) → always deny or prompt
    - The middle ground is fine to auto-approve if you log it
- **07. Subagents: isolated context for the dirty work**
  - A **subagent** is an independent Claude session launched from the main one — its own context window, its own tool list
  - **The point isn't parallelism for its own sake — it's keeping noise out of the main context**
    - A research task that reads 40 files
    - A review pass that needs a fresh perspective
    - An eval run that produces a wall of logs
    - These belong in a subagent so they don't pollute the main thread
  - **The most valuable subagent: the one that checks the main agent's work**
    - A model reviewing its own output is too easy on itself
    - A separate reviewer with a fresh context window catches what the writer talked itself into
    - This **writer-vs-checker split** makes every loop above the harness trustworthy
- **08. Skills: procedures the agent reuses**
  - A **Skill** is a `SKILL.md` file the agent runs
    - When you call it with `/skill-name`, or automatically when the task matches its description
  - Unlike a subagent, it runs **in the same context window** — just reusable instructions that become part of the session
  - **Trigger to create one**: you notice yourself pasting the same instructions into every new conversation
    - A PR checklist, an eval procedure, a release process — written once, invoked forever
  - **Skills are what make the harness improve over time**
    - Each time the procedure fails in a new way, add the lesson to the skill; the next run inherits it
- **09. Hooks: deterministic rules the model can't hallucinate**
  - Everything so far depends on the model understanding your instructions — **hooks don't**
  - A **hook** is a shell command that fires at a fixed point in the agent lifecycle
    - Before a tool runs, after a file changes, when the session ends
    - Its exit code can block the action
  - **Hooks are enforcement; `CLAUDE.md` is suggestion**
  - **Two hooks earn their place in almost every harness**
    - **`PreToolUse` gate** — blocks dangerous commands deterministically: `rm -rf`, reading `.env`, pushing to main
      - **Exit code 2** stops the call before it happens; the model can't talk its way past it
    - **`PostToolUse` formatter** — runs your linter/formatter after every edit
      - The agent never ships unformatted code because the harness formats it automatically
  ```jsonc
  "hooks": {
    "PreToolUse": [{
      "matcher": "Bash",
      "command": "./.claude/hooks/block-dangerous.sh"
      // exit 2 = block the call before it runs
    }],
    "PostToolUse": [{
      "matcher": "Edit|Write",
      "command": "prettier --write \"$CLAUDE_FILE_PATH\""
    }]
  }
  ```
  - **Use hooks for anything that must happen or must never happen** — safety, formatting, audit logging
  - Don't use them for judgment calls — that's what the model is for
  - A good harness has one or two sharp hooks, not twenty
- **Part 3 · Make It Compound**
- **10. Add a loop — now the harness runs on a timer**
  - A configured harness still waits for you to type; a loop makes it run on its own
  - Simplest version: **`/loop`** in Claude Code — a recurring prompt on a cadence
  - Pair it with **`/goal`** and the loop keeps going until an objective condition is true
    - Checked by an **independent grader**, not the agent grading itself
  ```text
  > /loop 30m /goal All tests pass and lint is clean.
    Triage new failures, draft fixes in claude/ branches.

  ▲ Claude uses the harness you built:
    - rules/ for conventions
    - reviewer subagent to check each fix
    - PreToolUse hook blocks pushes to main
  ✓ Looping. Independent grader decides "done."
  ```
  - **The loop didn't add intelligence** — it re-used everything in the harness: the rules, the reviewer subagent, the safety hook
  - **A good harness makes a loop trivial** — that's why you build the foundation first
- **11. Add dynamic workflows — the harness writes its own orchestration**
  - For tasks too complex for a single loop (massively parallel, highly structured, adversarial), Claude can write its own JavaScript harness on the fly
  - **Dynamic workflow** primitives
    - `agent()` to spawn
    - `parallel()` to fan out
    - `pipeline()` to stream
  - It composes the subagents your harness defines into patterns like **fan-out-and-synthesize** or **adversarial verification**
  - **A dynamic workflow is only as good as the subagents and skills it can call**
    - Sharp reviewer subagent + well-written eval skill → the workflow has good pieces to orchestrate
    - Empty harness → the workflow has nothing to work with
  - **The workflow is the conductor; your harness is the orchestra**
- **12. Add memory — what the agent forgets, the harness remembers**
  - **The step that turns a configured harness into a system that actually improves**
  - The agent forgets everything between runs; the harness doesn't have to
  - A **state file** — a markdown file in `agent-memory/`, or a Linear board — records what was tried, what worked, what failed, what rules survived
  - **The pattern that makes memory compound** (from how the strongest agents use it)
    - **Write before walking away** — every run ends by updating the state file: lessons learned, verified facts, what's next
    - **Read at the start** — every run begins by reading the state file and relevant skills, so it resumes instead of restarting
    - **Distill into skills** — when a lesson is general ("Windows runners need bash, not PowerShell"), it graduates from the state file into a skill, applying to every future project
  ```markdown
  # Project memory

  ## Verified facts # stop guessing about these
  - prc is in dollars, not cents (checked via SELECT MIN/MAX)
  - auth middleware order: rate_limit -> jwt -> rbac

  ## Lessons learned # distill the general ones into skills
  - Windows CI runners fail TLS 1.2 in PowerShell — use bash
  - Migrations on tables >1M rows must batch in 10k chunks

  ## Last session # resume, don't restart
  2026-06-11 · 3 fixes merged, 2 escalated. Next: verify rate-limit fix.
  ```
- **13. Close the loop: output → lesson → skill → better output**
  - Here the three floors lock together into something that improves itself
    1. Each run produces output
    2. The reviewer subagent (Step 7) checks it
    3. The result — what passed, what failed, what was learned — is written to memory (Step 12)
    4. General lessons get distilled into skills (Step 8)
    5. The next run inherits sharper skills and richer memory
  - **Built entirely from harness parts**
    - **Subagent** grades the work — objective check, fresh context
    - **Memory** records the verdict — survives between runs
    - **Skills** carry the distilled lessons forward
    - **The loop** runs it again — now with everything the last run learned
  - **The model never changed. The harness around it got sharper.**
  - That's what "self-improving" honestly means — not a model that learns, but **a harness that accumulates**
- **14. Ship the harness — package it, share it, reuse it**
  - A harness that works on one project is an asset
  - Bundle the skills, subagents, and rules into a **plugin** → your whole team installs the same setup in one step
    - Same conventions, same safety hooks, same reviewer
  - The harness stops being your personal setup and becomes **shared infrastructure**
  - **The order to build — because order is the lesson**
    1. Get one manual run reliable on a clean harness
    2. Add the context and permissions
    3. Add a reviewer subagent
    4. Add memory
    5. Then, and only then, wrap it in a loop
  - **A loop on a good harness compounds. A loop on a bad harness just bleeds faster.**
- **The harness mistakes that make every loop worse**
  - **Running on the default** — no context, no rules, no memory; the agent re-derives your project every session
  - **A bloated `CLAUDE.md`** — procedures stuffed into standing context, bloating every run; move them to skills
  - **Enforcement in `CLAUDE.md` instead of hooks** — the model can ignore a suggestion; it can't ignore a hook that exits 2
  - **One agent writing and grading its own work** — add a reviewer subagent with a fresh context window
  - **No memory** — every run restarts from zero; the state file is what makes tomorrow resume
  - **Wrapping a loop around a bad harness** — the loop just produces slop faster; build the foundation first
  - **Twenty hooks** — one or two sharp ones beat a pile nobody understands
  - **Shipping a harness without scanning it** — leaked secrets and over-broad permissions spread to everyone who installs it
- **Conclusion: The loop gets the glory. The harness does the work.**
  - Loop engineering is the exciting part — the agent prompting itself, running while you sleep
  - But **a loop is just a harness on a timer**
  - Everything that decides good vs. garbage output lives one floor down
    - The model you picked, the tools you allowed, the context you wrote, the reviewer you added, the memory you kept
  - **Build that floor well and everything above it compounds**
    - The loop re-uses your subagents
    - The workflow orchestrates your skills
    - The memory makes each run sharper than the last
  - **Self-improvement was never a property of the model — it's a property of the harness you build around it**
  - **Action**: pick one thing you're not doing — probably a reviewer subagent, a safety hook, or a state file — and add it today
    - Keep the harness small enough to explain
    - Then put a loop on top and watch the foundation do the work

<details><summary>原文</summary>

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

</details>

- 图片：[img1](https://pbs.twimg.com/media/HK76bIrX0AAnTdk?format=jpg&name=large) [img2](https://pbs.twimg.com/media/HK7ibrqWQAAUsd1?format=png&name=large) [img3](https://pbs.twimg.com/media/HK7jHWqXMAAi6sq?format=png&name=large) [img4](https://pbs.twimg.com/media/HK7kUzmWMAAb5GK?format=jpg&name=large) [img5](https://pbs.twimg.com/media/HK7tZ_EXYAA2pLb?format=png&name=large) [img6](https://pbs.twimg.com/media/HK7u0eHWYAEFfJk?format=jpg&name=large) [img7](https://pbs.twimg.com/media/HK7wfs1XQAA2nvW?format=jpg&name=large) [img8](https://pbs.twimg.com/media/HK7xHsDXsAAjaCv?format=jpg&name=large) [img9](https://pbs.twimg.com/media/HK7x3lgWAAAokpJ?format=jpg&name=large) [img10](https://pbs.twimg.com/media/HK7yLY4XMAA9831?format=jpg&name=large) [img11](https://pbs.twimg.com/media/HK70cTeWkAA7m0E?format=png&name=large)
- 含视频（未转写）

[↑ 回到目录](#part-1--keywords)

### x-2052480800004956323

**OpenAI (@OpenAI)** · 发帖 2026-05-07 · [原帖](https://x.com/OpenAI/status/2052480800004956323)

- **Codex now works directly in Chrome** on macOS and Windows
  - Better at working with apps and sites in Chrome
  - Works in parallel across tabs in the background without taking over your browser
- To start: install the Chrome plugin in the Codex app


- 含视频（未转写）

[↑ 回到目录](#part-1--keywords)

### x-2052068619635589466

**unusual_whales (@unusual_whales)** · 发帖 2026-05-06 · [原帖](https://x.com/unusual_whales/status/2052068619635589466)

- **Anthropic released a feature called "dreaming"** that allows AI agents to self-improve



[↑ 回到目录](#part-1--keywords)

### x-2050988005817499827

**Sebastian Raschka (@rasbt)** · 发帖 2026-05-03 · [原帖](https://x.com/rasbt/status/2050988005817499827)

- **Second batch of April model architecture releases**
  - Ant Ling 2.6 1T
  - Minimax M2.7
  - Xiaomi MiMo V2.5
  - Poolside Laguna XS.2
  - Tencent Hy3-preview
  - IBM Granite 4.1


- 图片：[img1](https://pbs.twimg.com/media/HHaStq6WgAAM7mg?format=jpg&name=large)

[↑ 回到目录](#part-1--keywords)

### x-2050956647909015788

**DAIR.AI (@dair_ai)** · 发帖 2026-05-03 · [原帖](https://x.com/dair_ai/status/2050956647909015788)

- 🔖 也在 Notes 里，全文见：[DAIR.AI 每周论文（4/26–5/3）](04-evals-research.md#x-2050956647909015788)

[↑ 回到目录](#part-1--keywords)

### x-2050228936270037068

**Suryansh Tiwari (@Suryanshti777)** · 发帖 2026-05-01 · [原帖](https://x.com/Suryanshti777/status/2050228936270037068)

- 🔖 也在 Notes 里，全文见：[RAG Is a Lie We Tell Ourselves — Karpathy's LLM Wiki](03-memory-rag.md#x-2050228936270037068)

[↑ 回到目录](#part-1--keywords)

### x-2029858356916277757

**我真的没有拼多多 (@nopinduoduo)** · 发帖 2026-03-06 · [原帖](https://x.com/nopinduoduo/status/2029858356916277757)

- **来源**：Google 开发者和研究团队今年 2 月发布的论文《SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks》，对目前的 skills 做了综述性研究
- **几个反常又有意思的点**
  - 目前有 4 万多个 skills，只有约 1k 个有用
  - Agent/LLM 写的 skills 都是垃圾，高级的 skills 都是手写的
  - 60%–80% 的 skills 集中在软件工程领域
- **一、三大核心发现**
  - **1. "4 万个 Skills 中只有 1k 个有用"**
    - 社区（开源项目、Agent 平台）托管了约 40,000+ 个用户贡献的 Skills
    - 测试发现绝大多数是冗余、低质，或因环境失效而不可用
    - 论文经严格筛选和人工校验，精选出约 1,000 个高质量、确定性强的 **Curated Skills** 作为 Benchmark 核心
  - **2. "Agent 写的 Skills 是垃圾，高级 Skills 必须手写"**（最扎心的结论之一）
    - 对比三种情况：
      - **No Skills**（无技能补充）
      - **Curated Skills**（人工编写/筛选的优质技能）
      - **Self-generated Skills**（LLM 自动生成的技能）
    - 人工精心编写的技能让任务成功率提高约 **16.2%**，在医疗等复杂领域甚至提高 **51.9%**
    - LLM 自动生成的技能几乎没有正面贡献，有时还因引入错误 API 调用或逻辑而产生负面影响
    - 结论：当前模型还没有能力"自我编写"出真正对自己有益的高质量程序化知识
      - 模型在垂直领域能力不足，需要专业知识技能来弥补
  - **3. "60%–80% 的 Skills 集中在软件工程"**
    - Agent 技能生态极度不平衡
    - 约 60%–80% 集中在**软件工程**和**数据分析**
    - 法律、医疗、制造业等垂直行业的高质量技能非常匮乏
- **二、作者的思考**
  - AI 直接创建的 skills 都是垃圾，符合常识
    - 真正有价值的 SOP 是个人经验的积累，AI 无法直接创建
  - 真正有价值的 skills，大家大概也不想完全开源，包括创作风格、思路等
  - 为何集中在软件工程？
    - 程序员天生爱开源
    - skills 本身诞生于 Claude Code 和技术圈
  - **启发：教会非技术圈的垂直领域从业者（法律、医疗、制造业）沉淀自己的 skills，会很有价值**
- **三、五个优化方向**
  - **优化一：控制 Skills 数量**
    - Skills 不是越多越好，过多内容会造成认知负担或互相冲突的建议
  - **优化二：控制 Skills 复杂度**
    - **聚焦、分步骤的指导 + 至少一个工作示例 > 冗长的 exhaustive 文档**
    - 智能体很难从长篇大论中提取有用信息
  - **优化三：匹配领域需求**
    - 不同领域获益差异巨大
    - 模型预训练中缺乏专业知识的领域（如医疗数据协调、制造工作流），Skills 帮助最大
    - 模型本来就强的领域，Skills 反而可能引入噪音
  - **优化四：用 Skills 弥补模型规模**
    - Claude Haiku（有 Skills）：**27.7%**
    - Claude Opus（无 Skills）：**22.0%**
    - **小模型 + 好 Skills 可以超越大模型**，对成本敏感场景很有价值
  - **优化五：针对 Harness 做适配**
    - 不同智能体框架利用 Skills 的能力不同
    - 选择合适的 agent harness 很重要，有些框架更善于检索和使用 Skills
- **四、实践建议**（论文 Discussion 部分）
  1. **简洁优先** —— 简洁、分步骤的指导 + 至少一个工作示例，往往比冗长文档更有效
  2. **模块化** —— 模块化的 Skills 在多部分任务上组合效果更好
  3. **适配 Harness** —— Skills 应明确匹配 harness 的约束（如对 JSON-only 协议重复提醒格式）
  4. **避免过度** —— Skills 应提供"如何做"的程序性指导，而不是"答案是什么"的声明性内容
- 论文原文：https://arxiv.org/html/2602.12670v1

<details><summary>原文</summary>

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

</details>

- 图片：[img1](https://pbs.twimg.com/media/HCuAMbtbwAAl29X?format=jpg&name=large) [img2](https://pbs.twimg.com/media/HCuBMqibcAA62eV?format=png&name=large) [img3](https://pbs.twimg.com/media/HCuAcCxaEAAAimX?format=png&name=large) [img4](https://pbs.twimg.com/media/HCuAfTXaUAM1zac?format=png&name=large) [img5](https://pbs.twimg.com/media/HCuAuXxaUAI4DwL?format=png&name=large) [img6](https://pbs.twimg.com/media/HCuA2fmbgAAuieX?format=png&name=large)

[↑ 回到目录](#part-1--keywords)

### x-2029562218048541087

**el.cine (@EHuanglu)** · 发帖 2026-03-05 · [原帖](https://x.com/EHuanglu/status/2029562218048541087)

- 🔖 也在 Notes 里，全文见：[Nano Banana 2：手绘户型图 → 4K 3D 室内渲染](09-other-applications.md#x-2029562218048541087)

[↑ 回到目录](#part-1--keywords)

### x-2028833958230933729

**meng shao (@shao__meng)** · 发帖 2026-03-03 · [原帖](https://x.com/shao__meng/status/2028833958230933729)

- **如何成为世界级的「Agentic Engineer」**
  - 你可以把大量设计和实现交给 Agent，但**结果必须自己负责**
- **工具不是越多越好，而是越精简越强**
  - 多数人陷入"工具崇拜"：以为装越多插件、harness、记忆系统，Agent 就越强
  - 实际上这些外部依赖带来**上下文污染**，Agent 表现反而下降
  - @systematicls 现在用的是近乎裸机的 CLI（Claude Code + Codex），做出了迄今最好的工作
- **理解"模型在飞速进化"**
  - 几个版本前，在 `CLAUDE.md` 里写"先读这个文件"，Agent 有 50% 概率无视你
  - 现在它能理解嵌套的条件指令（"如果 C，则读 D"）
  - 今天为某个缺陷设计的复杂方案，可能在下一个模型版本中直接失效，或直接被模型内化
  - 这和 @bcherny "面向 6 个月后的模型开发产品"异曲同工
- **上下文管理：最被低估的工程能力**
  - > "你只需要给 Agent 完成任务所需的确切信息，不多也不少。"
  - **研究与实现必须分离**
    - 错误做法："去帮我构建一个认证系统。"
      - Agent 会去查所有方案，上下文被各种备选实现细节填满，实现时容易混乱或幻觉
    - 正确做法："用 bcrypt-12 实现 JWT 认证，refresh token 7 天过期……"
      - 上下文直接聚焦在实现细节上
  - 如果自己不确定实现方案，流程应是：
    1. 开一个 Agent 做调研，输出方案对比
    2. 你或 Agent 决策选哪个
    3. 另开一个**全新上下文**的 Agent 来实现
- **巧用 Agent 的"奉承性"**
  - Agent 被设计为"取悦用户"：让它找 bug，它就会找到 bug，哪怕需要编造一个
  - 这不是 Agent 的错，是你的提示词问题
  - **方案一：中性提示词**
    - 别说"找 bug"，而说"梳理各模块的逻辑，报告所有发现"
    - 中性提示不预设结论，Agent 会如实汇报：有 bug 说 bug，没有就说没有
  - **方案二：利用奉承性设计多 Agent 对抗系统**（三 Agent 的 bug 验证机制）
    - **Bug 发现者**：低/中/高影响 bug 分别得 +1/+5/+10 分
    - **对抗者**：成功反驳得对应分，反驳错误扣 2 倍
    - **裁判**：被告知有真实答案参照，判对/判错各 ±1
- **明确任务的"终点"**
  - Agent 擅长开始任务，却不知道何时结束 —— 当前模型的固有限制
  - 两种可靠的终点定义方式：
    - **测试套件**：明确告知"X 个测试全部通过才算完成，且不得修改测试文件"
      - 测试是确定性的，Agent 无法糊弄
    - **截图 + 视觉验证**：实现功能后让 Agent 截图，验证设计或行为是否符合预期
      - Agent 可根据截图反复迭代，直到视觉结果满足要求
  - **更高阶做法**：为每个任务创建 `{TASK}_CONTRACT.md`
    - 列出所有验收条件（测试、截图验证等）
    - 结合 **stop-hook** 机制，强制 Agent 在合同完成前不得退出
- **长期运行 Agent 的正确姿势**
  - 作者明确反对"24 小时连续运行的超长会话"
    - 原因是上下文污染：多个不相关合同的上下文混在一起，导致漂移
  - 推荐方案：
    - 每个合同开一个新会话
    - 用一个**编排层**负责创建合同、分发新会话
    - 会话完成即关闭，下个任务开新会话
- **规则与技能的管理**
  - **`CLAUDE.md` 的定位**：不是完整文档，而是一个**条件跳转目录**，只告诉 Agent"在什么场景下去读哪个文件"
    - 如果你在写代码，先读 `coding-rules.md`
    - 如果你在写测试，先读 `coding-test-rules.md`
    - 如果测试失败，先读 `coding-test-failing-rules.md`
  - **规则（Rules）**：编码偏好 ——"不要做 X"、"总是做 Y"
    - 看到 Agent 做了你不满意的事，就写成规则
  - **技能（Skills）**：编码方法 ——"按照这个流程做 Z"
    - 想让某件事做法确定可控：先让 Agent 研究怎么做 → 写成 Skill 文件 → 你审阅修正
    - 这样在真实场景出现前，你就已掌握 Agent 的解法
  - **维护原则**：规则和技能积累多了会出现矛盾和冗余，性能再次下降
    - 需要定期"清理"：让 Agent 整合去重，并向你确认最新偏好
    - 这是需要周期性执行的维护动作

<details><summary>原文</summary>

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

</details>

- 图片：[img1](https://pbs.twimg.com/media/HCfdtGKbUAA7yJy?format=jpg&name=large)

[↑ 回到目录](#part-1--keywords)

### x-2027350587533332748

**Rimsha Bhardwaj (@heyrimsha)** · 发帖 2026-02-27 · [原帖](https://x.com/heyrimsha/status/2027350587533332748)

- 🔖 也在 Notes 里，全文见：[Anthropic《The Complete Guide to Building Skills for Claude》解读](06-skills-prompt.md#x-2027350587533332748)

[↑ 回到目录](#part-1--keywords)

### x-2022009906329739681

**OpenAI Developers (@OpenAIDevs)** · 发帖 2026-02-12 · [原帖](https://x.com/OpenAIDevs/status/2022009906329739681)

- **OpenAI introduced GPT-5.3-Codex-Spark** — an ultra-fast model built for real-time coding
- Rolling out as a research preview for **ChatGPT Pro** users in the Codex app, Codex CLI, and IDE extension


- 含视频（未转写）

[↑ 回到目录](#part-1--keywords)

### x-2026178278055403843

**GitHubDaily (@GitHub_Daily)** · 发帖 2026-02-24 · [原帖](https://x.com/GitHub_Daily/status/2026178278055403843)

- 🔖 也在 Notes 里，全文见：[GitNexus：给代码库建知识图谱，经 MCP 喂给 AI](05-coding-agent.md#x-2026178278055403843)

[↑ 回到目录](#part-1--keywords)

### x-2025920521871716562

**Elvis (@elvissun)** · 发帖 2026-02-23 · [原帖](https://x.com/elvissun/status/2025920521871716562)

- 🔖 也在 Notes 里，全文见：[OpenClaw + Codex/Claude Code Agent Swarm：一人开发团队](07-openclaw-personal-agent.md#x-2025920521871716562)

[↑ 回到目录](#part-1--keywords)

### x-2026224275192193465

**AYi (@AYi_AInotes)** · 发帖 2026-02-24 · [原帖](https://x.com/AYi_AInotes/status/2026224275192193465)

- 🔖 也在 Notes 里，全文见：[OpenClaw 编排文章的要点总结](07-openclaw-personal-agent.md#x-2026224275192193465)

[↑ 回到目录](#part-1--keywords)

### x-2023257934017294806

**OpenClaw (@openclaw)** · 发帖 2026-02-16 · [原帖](https://x.com/openclaw/status/2023257934017294806)

- **OpenClaw 2026.2.15 release**
  - Telegram message streaming — replies flow live
  - Discord Components v2 — buttons, selects, modals
  - Nested sub-agents
  - Major security hardening pass
  - 40+ bug fixes


- 链接卡片：[Releases · openclaw/openclaw](https://t.co/CywtGDbYpk)

[↑ 回到目录](#part-1--keywords)

### x-2022530044434825310

**OpenClaw (@openclaw)** · 发帖 2026-02-14 · [原帖](https://x.com/openclaw/status/2022530044434825310)

- **OpenClaw 2026.2.13 release** (337 commits)
  - HuggingFace support
  - Messages survive crashes (write-ahead queue)
  - Discord voice messages + custom presence
  - Threading that actually works
  - Massive security hardening pass
  - `gpt-5.3-codex-spark` support


- 链接卡片：[Release openclaw 2026.2.13 · openclaw/openclaw](https://t.co/EdqQRoYorZ)

[↑ 回到目录](#part-1--keywords)

### x-2021387483364151451

**nader dabit (@dabit3)** · 发帖 2026-02-11 · [原帖](https://x.com/dabit3/status/2021387483364151451)

- **Goal of the post**: start from scratch and build up to **OpenClaw's architecture** step by step
  - Shows how you could have invented it from first principles
  - Ingredients: a messaging API, an LLM, and the desire to make AI useful *outside* the chat window
  - End goal: understand how persistent AI assistants work, so you can build your own (or become an OpenClaw power user)
  - The tutorial is code-heavy and is also available as markdown
- **First, the problem** — ChatGPT or Claude in a browser has four limits:
  - **Stateless** — every conversation starts from zero
    - It doesn't know your name, preferences, what you asked yesterday, or your current project
    - You keep re-explaining context
  - **Passive** — you go to it; it never comes to you
    - It can't wake at 7am to brief you on your calendar, monitor email, or run recurring tasks
    - It only works while you sit in front of it
  - **Isolated** — it can't run commands on your machine, browse the web, control your apps, or message on your behalf
    - It lives in a text box with no hands
  - **Single-channel** — your life is on WhatsApp, Telegram, Discord, Slack, iMessage, but the AI is in its own tab
    - You can't text it where you already are, let alone keep one continuous memory across those surfaces
- **What if instead you had an AI that:**
  - Lived in the messaging apps you already use — all of them, with shared memory
  - Remembered your preferences, projects, and past conversations across sessions
  - Could run commands on your computer, browse the web, and control a real browser
  - Woke up on a schedule to handle recurring tasks without being asked
  - Ran on your own hardware (laptop, VPS, Mac Mini) — always on, under your control
- **That is OpenClaw**: not a chatbot, but a personal AI assistant with a persistent identity, tools, and presence on every channel you use
- **The Simplest Possible Bot**
  - Absolute minimum: an AI that responds to messages on Telegram
  ```python
  import os
  import anthropic
  from telegram import Update
  from telegram.ext import Application, MessageHandler, filters

  client = anthropic.Anthropic()

  async def handle_message(update: Update, context):
      user_message = update.message.text

      response = client.messages.create(
          model="claude-sonnet-4-5-20250929",
          max_tokens=1024,
          messages=[{"role": "user", "content": user_message}]
      )

      await update.message.reply_text(response.content[0].text)

  app = Application.builder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()
  app.add_handler(MessageHandler(filters.TEXT, handle_message))
  app.run_polling()
  ```
  - Run it, send a Telegram message, and the AI responds
  - But it is basically a worse Claude web interface: every message independent, no memory, no tools, no personality
- **Goal: Persistent Sessions**
  - Problem: **statelessness** — every message is a fresh conversation; "what did I say earlier?" gets no answer
  - **Fix: sessions** — keep a conversation history per user
  ```python
  import json
  import os
  import anthropic
  from telegram import Update
  from telegram.ext import Application, MessageHandler, filters

  client = anthropic.Anthropic()
  SESSIONS_DIR = "./sessions"
  os.makedirs(SESSIONS_DIR, exist_ok=True)

  def get_session_path(user_id):
      return os.path.join(SESSIONS_DIR, f"{user_id}.jsonl")

  def load_session(user_id):
      """Load conversation history from disk."""
      path = get_session_path(user_id)
      messages = []
      if os.path.exists(path):
          with open(path, "r") as f:
              for line in f:
                  if line.strip():
                      messages.append(json.loads(line))
      return messages

  def append_to_session(user_id, message):
      """Append a single message to the session file."""
      path = get_session_path(user_id)
      with open(path, "a") as f:
          f.write(json.dumps(message) + "\n")

  def save_session(user_id, messages):
      """Overwrite the session file with the full message list."""
      path = get_session_path(user_id)
      with open(path, "w") as f:
          for message in messages:
              f.write(json.dumps(message) + "\n")

  async def handle_message(update: Update, context):
      user_id = str(update.effective_user.id)
      user_message = update.message.text

      # Load existing conversation
      messages = load_session(user_id)

      # Add new user message
      user_msg = {"role": "user", "content": user_message}
      messages.append(user_msg)
      append_to_session(user_id, user_msg)

      # Call the AI with full history
      response = client.messages.create(
          model="claude-sonnet-4-5-20250929",
          max_tokens=4096,
          messages=messages
      )

      # Save assistant response
      assistant_msg = {"role": "assistant", "content": response.content[0].text}
      append_to_session(user_id, assistant_msg)

      await update.message.reply_text(response.content[0].text)

  app = Application.builder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()
  app.add_handler(MessageHandler(filters.TEXT, handle_message))
  app.run_polling()
  ```
  - Now you can have a real conversation:
  ```text
  You: My name is Nader
  Bot: Nice to meet you, Nader!

  [hours later...]

  You: What's my name?
  Bot: Your name is Nader!
  ```
  - **Key insight: the JSONL format**
    - Each line is one message; append-only
    - If the process crashes mid-write, you lose at most one line
    - This is exactly what OpenClaw uses for session transcripts:
    ```text
    ~/.openclaw/agents/<agentId>/sessions/<sessionId>.jsonl
    ```
    - Each session maps to a file; each file is a conversation
    - Restart the process and everything is still there
  - Problem to come back to: conversations grow and will eventually exceed the model's context window
- **Goal: Adding a Personality (`SOUL.md`)**
  - The bot works but has no personality — a generic assistant. What if it should be *someone*?
  - OpenClaw's answer: **`SOUL.md`**, a markdown file defining the agent's identity, behavior, and boundaries
  ```python
  SOUL = """
  # Who You Are

  **Name:** Jarvis
  **Role:** Personal AI assistant

  ## Personality
  - Be genuinely helpful, not performatively helpful
  - Skip the "Great question!" - just help
  - Have opinions. You're allowed to disagree
  - Be concise when needed, thorough when it matters

  ## Boundaries
  - Private things stay private
  - When in doubt, ask before acting externally
  - You're not the user's voice - be careful about sending messages on their behalf

  ## Memory
  Remember important details from conversations.
  Write them down if they matter.
  """

  async def handle_message(update: Update, context):
      user_id = str(update.effective_user.id)
      messages = load_session(user_id)

      user_msg = {"role": "user", "content": update.message.text}
      messages.append(user_msg)
      append_to_session(user_id, user_msg)

      response = client.messages.create(
          model="claude-sonnet-4-5-20250929",
          max_tokens=4096,
          system=SOUL,  # <-- personality injected here
          messages=messages
      )

      assistant_msg = {"role": "assistant", "content": response.content[0].text}
      append_to_session(user_id, assistant_msg)

      await update.message.reply_text(response.content[0].text)
  ```
  - Now you're talking to Jarvis: **the SOUL is injected as the system prompt on every API call**
  - In OpenClaw, `SOUL.md` lives in the agent's workspace:
    ```text
    ~/.openclaw/workspace/SOUL.md
    ```
    - Loaded at session start and injected into the system prompt
    - Write anything: an origin story, a core philosophy, behavioral rules
  - **The more specific the SOUL, the more consistent the behavior**
    - "Be helpful" is vague
    - "Be the assistant you'd actually want to talk to. Concise when needed, thorough when it matters. Not a corporate drone. Not a sycophant. Just... good." gives the model something to work with
- **Goal: Adding Tools**
  - A bot that can only talk is limited — what if it could *do things*?
  - **Core idea: give the AI structured tools and let it decide when to use them**
  ```python
  import subprocess

  TOOLS = [
      {
          "name": "run_command",
          "description": "Run a shell command on the user's computer",
          "input_schema": {
              "type": "object",
              "properties": {
                  "command": {"type": "string", "description": "The command to run"}
              },
              "required": ["command"]
          }
      },
      {
          "name": "read_file",
          "description": "Read a file from the filesystem",
          "input_schema": {
              "type": "object",
              "properties": {
                  "path": {"type": "string", "description": "Path to the file"}
              },
              "required": ["path"]
          }
      },
      {
          "name": "write_file",
          "description": "Write content to a file",
          "input_schema": {
              "type": "object",
              "properties": {
                  "path": {"type": "string", "description": "Path to the file"},
                  "content": {"type": "string", "description": "Content to write"}
              },
              "required": ["path", "content"]
          }
      },
      {
          "name": "web_search",
          "description": "Search the web for information",
          "input_schema": {
              "type": "object",
              "properties": {
                  "query": {"type": "string", "description": "Search query"}
              },
              "required": ["query"]
          }
      }
  ]

  def execute_tool(name, input):
      if name == "run_command":
          result = subprocess.run(
              input["command"], shell=True,
              capture_output=True, text=True, timeout=30
          )
          return result.stdout + result.stderr

      elif name == "read_file":
          with open(input["path"], "r") as f:
              return f.read()

      elif name == "write_file":
          with open(input["path"], "w") as f:
              f.write(input["content"])
          return f"Wrote to {input['path']}"

      elif name == "web_search":
          # Simplified - use a real search API in practice
          return f"Search results for: {input['query']}"

      return f"Unknown tool: {name}"
  ```
  - **The agent loop**: when the AI wants a tool, execute it and feed the result back
  ```python
  def serialize_content(content):
      """Convert API response content blocks to JSON-serializable dicts."""
      serialized = []
      for block in content:
          if hasattr(block, "text"):
              serialized.append({"type": "text", "text": block.text})
          elif block.type == "tool_use":
              serialized.append({
                  "type": "tool_use",
                  "id": block.id,
                  "name": block.name,
                  "input": block.input
              })
      return serialized

  def run_agent_turn(messages, system_prompt):
      """Run one full agent turn (may involve multiple tool calls)."""
      while True:
          response = client.messages.create(
              model="claude-sonnet-4-5-20250929",
              max_tokens=4096,
              system=system_prompt,
              tools=TOOLS,
              messages=messages
          )

          content = serialize_content(response.content)

          # If the AI is done (no tool use), return the text
          if response.stop_reason == "end_turn":
              text = ""
              for block in response.content:
                  if hasattr(block, "text"):
                      text += block.text
              messages.append({"role": "assistant", "content": content})
              return text, messages

          # Process tool calls
          if response.stop_reason == "tool_use":
              messages.append({"role": "assistant", "content": content})

              tool_results = []
              for block in response.content:
                  if block.type == "tool_use":
                      print(f"  Tool: {block.name}({json.dumps(block.input)})")
                      result = execute_tool(block.name, block.input)
                      tool_results.append({
                          "type": "tool_result",
                          "tool_use_id": block.id,
                          "content": str(result)
                      })

              messages.append({"role": "user", "content": tool_results})
  ```
  - Update `handle_message` to use the agent loop instead of calling the API directly:
  ```python
  async def handle_message(update: Update, context):
      user_id = str(update.effective_user.id)
      messages = load_session(user_id)
      messages.append({"role": "user", "content": update.message.text})

      response_text, messages = run_agent_turn(messages, SOUL)

      save_session(user_id, messages)
      await update.message.reply_text(response_text)
  ```
  - Now you can text your bot:
  ```text
  You: Create a file called hello.py that prints hello world, then run it

  Bot: [uses write_file to create hello.py]
      [uses run_command to execute it]
      Done! I created hello.py and ran it. Output: "hello world"
  ```
  - The AI chose which tools to use, in what order, and turned the results into a natural reply — all through a Telegram message
  - OpenClaw's production tool catalog is much larger (browser automation, inter-agent messaging, sub-agent spawning, and more)
    - **Every tool follows the same pattern: a schema, a description, and an execution function**
- **Goal: Permission Controls**
  - Executing commands from Telegram messages is terrifying
    - What if someone gets into your Telegram account and tells the bot to `rm -rf /`?
  - OpenClaw's approach: **an approval allowlist that remembers what you've approved**
  - Add these helpers alongside the existing code:
  ```python
  import re

  SAFE_COMMANDS = {"ls", "cat", "head", "tail", "wc", "date", "whoami", "echo"}
  DANGEROUS_PATTERNS = [r"\brm\b", r"\bsudo\b", r"\bchmod\b", r"\bcurl.*\|.*sh"]

  # Persistent allowlist
  APPROVALS_FILE = "./exec-approvals.json"

  def load_approvals():
      if os.path.exists(APPROVALS_FILE):
          with open(APPROVALS_FILE) as f:
              return json.load(f)
      return {"allowed": [], "denied": []}

  def save_approval(command, approved):
      approvals = load_approvals()
      key = "allowed" if approved else "denied"
      if command not in approvals[key]:
          approvals[key].append(command)
      with open(APPROVALS_FILE, "w") as f:
          json.dump(approvals, f, indent=2)

  def check_command_safety(command):
      """Returns 'safe', 'approved', or 'needs_approval'."""
      base_cmd = command.strip().split()[0] if command.strip() else ""
      if base_cmd in SAFE_COMMANDS:
          return "safe"

      approvals = load_approvals()
      if command in approvals["allowed"]:
          return "approved"

      for pattern in DANGEROUS_PATTERNS:
          if re.search(pattern, command):
              return "needs_approval"

      return "needs_approval"
  ```
  - Then update the `run_command` case in `execute_tool` to check permissions before executing:
  ```python
      if name == "run_command":
          cmd = input["command"]
          safety = check_command_safety(cmd)

          if safety == "needs_approval":
              # In a real bot, you'd prompt the user via Telegram
              # and wait for their response. For simplicity, we log and deny.
              print(f"  ⚠️  Blocked: {cmd} (needs approval)")
              return "Permission denied. Command requires approval."

          result = subprocess.run(
              cmd, shell=True, capture_output=True,
              text=True, timeout=30
          )
          return result.stdout + result.stderr
  ```
  - Safe or previously approved commands run immediately
  - Otherwise the agent is told "permission denied" and can try a different approach
  - Approvals persist to `exec-approvals.json`, so you're never asked twice for the same command
  - OpenClaw extends this with:
    - **Glob patterns** (approve `git *` once)
    - **A three-tier model**: "ask" (prompt user), "record" (log but allow), "ignore" (auto-allow)
- **Goal: The Gateway**
  - What if you also want the AI on Discord, WhatsApp, and Slack?
  - Separate bots per platform → separate sessions, memory, and configs
    - The Telegram AI wouldn't know what you discussed on Discord
  - **Solution: a gateway** — one central process that manages all channels
  - **Key point: the agent logic is already decoupled from the channel**
    - `run_agent_turn` knows nothing about Telegram; it takes messages and returns text
  - To prove it, add a second interface: a simple HTTP API next to the Telegram bot, sharing the same agent and sessions
  ```python
  from flask import Flask, request, jsonify
  import threading

  flask_app = Flask(__name__)

  @flask_app.route("/chat", methods=["POST"])
  def chat():
      data = request.json
      user_id = data["user_id"]
      messages = load_session(user_id)
      messages.append({"role": "user", "content": data["message"]})

      response_text, messages = run_agent_turn(messages, SOUL)

      save_session(user_id, messages)
      return jsonify({"response": response_text})

  # Run the HTTP API in a background thread
  threading.Thread(target=lambda: flask_app.run(port=5000), daemon=True).start()

  # Telegram bot runs as before
  app = Application.builder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()
  app.add_handler(MessageHandler(filters.TEXT, handle_message))
  app.run_polling()
  ```
  - Try it: tell the bot your name on Telegram, then query over HTTP with the same user ID (your Telegram user ID)
  ```text
  # Via Telegram
  You: My name is Nader
  Bot: Nice to meet you, Nader!

  # Via HTTP — use your Telegram user ID so it hits the same session
  curl -X POST http://127.0.0.1:5000/chat \
    -H "Content-Type: application/json" \
    -d '{"user_id": "YOUR_TELEGRAM_USER_ID", "message": "What is my name?"}'

  {"response": "Your name is Nader!"}
  ```
  - **Same agent, same sessions, same memory, two interfaces — that's the gateway pattern**
  - Next step: make it config-driven — a JSON file listing which channels to start and how to authenticate them
  - OpenClaw's gateway does this:
    - Manages Telegram, Discord, WhatsApp, Slack, Signal, iMessage, and more through a single config file
    - Supports configurable **session scoping**: per-user, per-channel, or a single shared session
    - So the same person gets a unified experience across channels
  - The tutorial keeps the simple user-ID-as-session-key approach for now
- **Goal: Context Compaction**
  - The growing-session problem: after weeks of chat the session file has thousands of messages and exceeds the context window
  - **Fix: summarize old messages, keep recent ones** — add two functions:
  ```python
  def estimate_tokens(messages):
      """Rough token estimate: ~4 chars per token."""
      return sum(len(json.dumps(m)) for m in messages) // 4

  def compact_session(user_id, messages):
      """Summarize old messages when context gets too long."""
      if estimate_tokens(messages) < 100_000:  # ~80% of a 128k window
          return messages  # No compaction needed

      split = len(messages) // 2
      old, recent = messages[:split], messages[split:]

      print("  Compacting session history...")

      summary = client.messages.create(
          model="claude-sonnet-4-5-20250929",
          max_tokens=2000,
          messages=[{
              "role": "user",
              "content": (
                  "Summarize this conversation concisely. Preserve:\n"
                  "- Key facts about the user (name, preferences)\n"
                  "- Important decisions made\n"
                  "- Open tasks or TODOs\n\n"
                  f"{json.dumps(old, indent=2)}"
              )
          }]
      )

      compacted = [{
          "role": "user",
          "content": f"[Previous conversation summary]\n{summary.content[0].text}"
      }] + recent

      save_session(user_id, compacted)
      return compacted
  ```
  - Add the compaction check at the top of `handle_message`, right after loading the session:
  ```python
  async def handle_message(update: Update, context):
      user_id = str(update.effective_user.id)
      messages = load_session(user_id)
      messages = compact_session(user_id, messages)  # <-- add this line
      messages.append({"role": "user", "content": update.message.text})

      response_text, messages = run_agent_turn(messages, SOUL)

      save_session(user_id, messages)
      await update.message.reply_text(response_text)
  ```
  - To test without chatting for hours, temporarily lower the threshold:
  ```python
  if estimate_tokens(messages) < 1000:  # lowered for testing
  ```
    - Have 10–15 messages of conversation and watch old messages get replaced by a summary
    - The bot still remembers key facts, but the session file is much smaller
  - OpenClaw's compaction is more sophisticated, but the core idea is the same:
    - Splits messages into chunks by token count
    - Summarizes each chunk separately
    - Includes a safety margin for estimation inaccuracy
- **Goal: Long-Term Memory**
  - Session history is conversation memory — reset the session and it's gone
  - Need a **separate memory system** that survives session resets
  - Approach: **give the agent tools to save and search memories stored as files**
  - Add two tools to the `TOOLS` list:
  ```python
  {
      "name": "save_memory",
      "description": "Save important information to long-term memory. Use for user preferences, key facts, and anything worth remembering across sessions.",
      "input_schema": {
          "type": "object",
          "properties": {
              "key": {
                  "type": "string",
                  "description": "Short label, e.g. 'user-preferences', 'project-notes'"
              },
              "content": {
                  "type": "string",
                  "description": "The information to remember"
              }
          },
          "required": ["key", "content"]
      }
  },
  {
      "name": "memory_search",
      "description": "Search long-term memory for relevant information. Use at the start of conversations to recall context.",
      "input_schema": {
          "type": "object",
          "properties": {
              "query": {
                  "type": "string",
                  "description": "What to search for"
              }
          },
          "required": ["query"]
      }
  }
  ```
  - Add their cases to `execute_tool`:
  ```python
  MEMORY_DIR = "./memory"

  # Add these cases to execute_tool:

      elif name == "save_memory":
          os.makedirs(MEMORY_DIR, exist_ok=True)
          filepath = os.path.join(MEMORY_DIR, f"{input['key']}.md")
          with open(filepath, "w") as f:
              f.write(input["content"])
          return f"Saved to memory: {input['key']}"

      elif name == "memory_search":
          query = input["query"].lower()
          results = []
          if os.path.exists(MEMORY_DIR):
              for fname in os.listdir(MEMORY_DIR):
                  if fname.endswith(".md"):
                      with open(os.path.join(MEMORY_DIR, fname), "r") as f:
                          content = f.read()
                      if any(word in content.lower() for word in query.split()):
                          results.append(f"--- {fname} ---\n{content}")
          return "\n\n".join(results) if results else "No matching memories found."
  ```
  - Update the SOUL so the agent knows about memory:
  ```python
  SOUL = """
  # Who You Are
  ...existing personality...

  ## Memory
  You have a long-term memory system.
  - Use save_memory to store important information (user preferences, key facts, project details).
  - Use memory_search at the start of conversations to recall context from previous sessions.
  Memory files are stored in ./memory/ as markdown files.
  """
  ```
  - Try it:
  ```text
  You: Remember that my favorite restaurant is Elvies and I prefer to go on weekends.

  Bot: [uses save_memory to write nader-profile.md]
       Got it — saved your restaurant preference.

  [Reset the session or restart the bot]

  You: Where should we go for dinner?

  Bot: [uses memory_search for "restaurant dinner favorite"]
       How about Elvies? I know it's your favorite. Want to go this weekend?
  ```
  - **Memory persists because it's stored in files, not in the session** — reset the session or restart the bot, memories remain
  - OpenClaw's production memory uses **vector search with embeddings** for semantic matching ("auth bug" matches "authentication issues")
    - Keyword search is good enough to start
- **Goal: Command Queue**
  - Subtle but critical problem: two messages arriving at the same time
    - E.g. "check my calendar" on Telegram and "what's the weather" via HTTP at once
    - Both load the same session, both append to it → corrupted data
  - **Fix: a per-session lock**
    - Only one message processes at a time per session
    - Different sessions still run in parallel
  ```python
  # Add to your bot
  from collections import defaultdict

  session_locks = defaultdict(threading.Lock)
  ```
  - Wrap the body of `handle_message` with the lock:
  ```python
  async def handle_message(update: Update, context):
      user_id = str(update.effective_user.id)

      with session_locks[user_id]:
          messages = load_session(user_id)
          messages = compact_session(user_id, messages)
          messages.append({"role": "user", "content": update.message.text})

          response_text, messages = run_agent_turn(messages, SOUL)

          save_session(user_id, messages)

      await update.message.reply_text(response_text)
  ```
  - Do the same for the `/chat` HTTP endpoint:
  ```python
  @flask_app.route("/chat", methods=["POST"])
  def chat():
      data = request.json
      user_id = data["user_id"]

      with session_locks[user_id]:
          messages = load_session(user_id)
          messages = compact_session(user_id, messages)
          messages.append({"role": "user", "content": data["message"]})

          response_text, messages = run_agent_turn(messages, SOUL)

          save_session(user_id, messages)

      return jsonify({"response": response_text})
  ```
  - Five lines of setup: same-user messages queue up, different users run in parallel, no race conditions
  - OpenClaw extends this with **lane-based queues** — separate lanes for messages, cron jobs, and sub-agents — so heartbeats never block real-time conversations
- **Goal: Cron Jobs (Heartbeats)**
  - So far the agent only responds when spoken to
    - What about checking your email every morning, or summarizing your calendar before meetings?
  - You need scheduled execution: **heartbeats** — recurring tasks that trigger the agent on a timer
  ```python
  import schedule
  import time

  def setup_heartbeats():
      """Configure recurring agent tasks."""

      def morning_briefing():
          print("\n⏰ Heartbeat: morning briefing")
          # Use an isolated session key so cron doesn't pollute main chat
          session_key = "cron:morning-briefing"

          with session_locks[session_key]:
              messages = load_session(session_key)
              messages.append({
                  "role": "user",
                  "content": "Good morning! Check today's date and give me a motivational quote."
              })

              response_text, messages = run_agent_turn(messages, SOUL)
              save_session(session_key, messages)

          print(f"🤖 {response_text}\n")
          # In production, you'd send this to Telegram/Discord too

      schedule.every().day.at("07:30").do(morning_briefing)

      # Run the scheduler in a background thread
      def scheduler_loop():
          while True:
              schedule.run_pending()
              time.sleep(60)

      threading.Thread(target=scheduler_loop, daemon=True).start()

  # Call during startup, before run_polling()
  setup_heartbeats()
  ```
  - **Key insight: each heartbeat uses its own session key** (`cron:morning-briefing`)
    - Keeps scheduled tasks out of your main conversation history
    - It calls the same `run_agent_turn` — just another message, triggered by a timer instead of a human
  - To test, run every minute (change it back to daily when done):
  ```python
  schedule.every(1).minutes.do(morning_briefing)
  ```
    - You'll see the heartbeat fire in the terminal and the agent respond
  - OpenClaw supports full cron expressions (`30 7 * * *`) and routes heartbeats through a separate command-queue lane so they never block real-time messages
- **Goal: Multi-Agent**
  - As tasks grow, one personality and toolset can't cover everything well
    - A research assistant needs different instructions than a general assistant
  - **Fix: multiple agent configurations with routing**
    - Each agent has its own SOUL and its own session; you switch between them based on the message
  ```python
  AGENTS = {
      "main": {
          "name": "Jarvis",
          "soul": SOUL,  # our existing SOUL
          "session_prefix": "agent:main",
      },
      "researcher": {
          "name": "Scout",
          "soul": """You are Scout, a research specialist.
  Your job: find information and cite sources. Every claim needs evidence.
  Use tools to gather data. Be thorough but concise.
  Save important findings to memory for other agents to reference.""",
          "session_prefix": "agent:researcher",
      },
  }

  def resolve_agent(message_text):
      """Route messages to the right agent based on prefix commands."""
      if message_text.startswith("/research "):
          return "researcher", message_text[len("/research "):]
      return "main", message_text
  ```
  - Update `handle_message` to route to the right agent:
  ```python
  async def handle_message(update: Update, context):
      user_id = str(update.effective_user.id)
      agent_id, message_text = resolve_agent(update.message.text)
      agent = AGENTS[agent_id]
      session_key = f"{agent['session_prefix']}:{user_id}"

      with session_locks[session_key]:
          messages = load_session(session_key)
          messages = compact_session(session_key, messages)
          messages.append({"role": "user", "content": message_text})

          response_text, messages = run_agent_turn(messages, agent["soul"])

          save_session(session_key, messages)

      await update.message.reply_text(f"[{agent['name']}] {response_text}")
  ```
  - Try it:
  ```text
  You: What's the weather like?
  [Jarvis] It's a nice day! I'd check a weather service for exact details.

  You: /research What are the best practices for Python async programming?
  [Scout] Here's what I found...
      [uses web_search, save_memory to gather and store findings]
      The key practices are: 1) Use asyncio.gather for concurrent tasks...

  You: What did Scout find about Python async?
  [Jarvis] [uses memory_search]
      Scout's research found that the key async best practices are...
  ```
  - Each agent has its own conversation history, but **they share the same memory directory**
    - Scout saves research findings; Jarvis can search them later
    - They collaborate through shared files, no direct messaging needed
  - OpenClaw adds sub-agent spawning (a parent spawns a child for a focused task) and inter-agent messaging
  - **Core pattern: each agent is just a SOUL + session + tools**
- **Putting It All Together**
  - One runnable script: a clean standalone REPL with every feature — sessions, SOUL, tools, permissions, compaction, memory, command queue, cron, and multi-agent routing
  - A mini-openclaw in ~400 lines: https://gist.github.com/dabit3/86ee04a1c02c839409a02b20fe99a492
  - Save it as `mini-openclaw.py` and run:
  ```bash
  uv run --with anthropic --with schedule python mini-openclaw.py
  ```
  - What a session looks like:
  ```text
  Mini OpenClaw
    Agents: Jarvis, Scout
    Workspace: ~/.mini-openclaw
    Commands: /new (reset), /research <query>, /quit

  You: Remember that my favorite restaurant is Hai Cenato and I prefer 7pm reservations

    🔧 save_memory: {"key": "user-preferences", "content": "Favorite restaurant...
       → Saved to memory: user-preferences

  🤖 [Jarvis] Got it. Saved your restaurant preference - Hai Cenato, 7pm reservations.

  You: What's in my project directory?

    🔧 run_command: {"command": "ls"}
       → src, package.json, README.md, node_modules, ...

  🤖 [Jarvis] Your project has a standard Node.js structure with src/, package.json,
     and the usual suspects.

  You: /new
    Session reset.

  You: Where do I like to eat?

    🔧 memory_search: {"query": "restaurant favorite food"}
       → --- user-preferences.md ---
          Favorite restaurant: Hai Cenato...

  🤖 [Jarvis] You like Hai Cenato, and you prefer 7pm reservations.

  You: /research What are the latest trends in AI agents?

    🔧 web_search: {"query": "AI agent trends 2025"}
       → Search results for: AI agent trends 2025
    🔧 save_memory: {"key": "research-ai-agents", ...}
       → Saved to memory: research-ai-agents

  🤖 [Scout] Here's what I found on current AI agent trends...
  ```
  - Memory persists across sessions; agents collaborate through shared memory files; commands need approval; heartbeats run in the background — all in ~400 lines
- **What We've Learned** — every major component of a persistent AI assistant, built from a simple Telegram bot:
  - **Persistent sessions (JSONL files)** — crash-safe conversation memory
    - One file per session, one line per message; restart and everything is still there
  - **SOUL.md (system prompt)** — a personality file that turns a generic AI into a specific agent with consistent behavior, boundaries, and style
  - **Tools + agent loop** — structured tool definitions let the AI decide when to act
    - The loop calls the LLM, executes requested tools, feeds results back, and repeats until done
  - **Permission controls** — an allowlist of safe commands plus persistent approvals; dangerous operations need explicit consent
  - **The gateway pattern** — one central agent, many interfaces (Telegram, HTTP, any channel), same sessions and memory
  - **Context compaction** — when conversations outgrow the context window, summarize old messages and keep recent ones
  - **Long-term memory** — file-based storage with save and search tools; survives session resets; accessible to any agent
  - **Command queue** — per-session locking to prevent race conditions when messages arrive at once
  - **Heartbeats** — scheduled agent runs on a timer, each with its own isolated session; wake up, do the task, go back to sleep
  - **Multi-agent routing** — multiple configs with different SOULs and session keys, routed by message content; collaborate through shared memory files
- **Each component came from a practical problem**

  | Problem | Solution |
  | --- | --- |
  | "The AI can't remember anything" | Sessions |
  | "It responds like a generic chatbot" | SOUL.md |
  | "It can only talk, not act" | Tools + Agent loop |
  | "It runs dangerous commands without asking" | Permission controls |
  | "I want it on all my messaging apps" | Gateway |
  | "The conversation got too long" | Compaction |
  | "It forgets things between sessions" | Memory |
  | "Two messages at once corrupt the data" | Command queue |
  | "I want it to do things automatically" | Heartbeats |
  | "One agent can't do everything well" | Multi-agent |

  - **This is how you could have invented OpenClaw**
- **Going Further** — how OpenClaw extends each idea for production
  - **Browser with semantic snapshots**
    - OpenClaw gives the agent a browser via **Playwright**
    - Instead of screenshots (5MB each, expensive in tokens), it uses **semantic snapshots** — a text version of the page's accessibility tree
    ```python
    snapshot = page.accessibility.snapshot()
    # Output:
    # - heading "Welcome to GitHub"
    # - button "Sign In" [ref=1]
    # - textbox "Email" [ref=2]
    # - link "Forgot password?" [ref=3]
    ```
    - Each interactive element gets a numbered `ref` ID
    - To click, the agent says "click ref=1", which maps to exactly one element — no guessing, no "click the blue button near the top"
    - Text instead of an image → **~100x smaller than a screenshot**, far fewer tokens per page
  - **Session scoping and identity links**
    - The prototype uses user ID as the session key; OpenClaw supports configurable scoping:
      - `main` (default): all DMs share one session — simple, great for single-user setups
      - `per-peer`: each person gets one session across all channels
      - `per-channel-peer`: each person per channel gets their own session
    - **Identity links** merge sessions across channels for the same person (Alice's Telegram and Discord conversations share history)
  - **Channel plugin system**
    - The prototype hardcodes Telegram + HTTP
    - OpenClaw uses a plugin architecture: each channel (Telegram, Discord, WhatsApp, Slack, Signal, iMessage) is a separate adapter that normalizes messages into a common format
    - Adding a channel means writing one adapter, without touching agent logic
  - **Vector memory search**
    - Keyword search misses semantic matches ("auth bug" won't match "authentication issues")
    - OpenClaw uses a **hybrid approach**:
      - Vector search via SQLite with embedding extensions for semantic similarity
      - Plus **FTS5** for exact keyword matches
    - Configurable embedding providers: OpenAI, local models, Gemini, Voyage
  - **Sub-agent spawning**
    - The prototype uses manual routing; OpenClaw lets agents spawn sub-agents programmatically
    - A parent calls `sessions_spawn`; the child runs in its own context with a timeout and returns results to the parent
    - Enables "research this topic in depth": the main agent delegates to a specialist and continues when it's done
- **Next Steps** — if you want to build your own:
  1. **Start with one channel** — get a Telegram or Discord bot working with sessions
  2. **Add tools incrementally** — file read/write first, then shell execution
  3. **Add memory when you need it** — once sessions reset, you'll want persistent memory
  4. **Add channels when you outgrow one** — the gateway pattern emerges naturally
  5. **Add agents when tasks specialize** — don't start with 10 agents, start with 2
  - Or just use OpenClaw: it's open source and handles the edge cases glossed over here — but now you know how it works under the hood

<details><summary>原文</summary>

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

</details>

- 图片：[img1](https://pbs.twimg.com/media/HA1FTA1aAAIziKK?format=jpg&name=large)

[↑ 回到目录](#part-1--keywords)

### x-2013725989952467308

**David Ondrej (@DavidOndrej1)** · 发帖 2026-01-20 · [原帖](https://x.com/DavidOndrej1/status/2013725989952467308)

- **Anthropic released a 7-hour Claude Code masterclass**
- The author went through the entire course and condensed it into a 27-minute video


- 含视频（未转写）

[↑ 回到目录](#part-1--keywords)

### x-2013293638768562325

**Dilum Sanjaya (@DilumSanjaya)** · 发帖 2026-01-19 · [原帖](https://x.com/DilumSanjaya/status/2013293638768562325)

- **Vibe Coding Robotics, Part 7**
  - Implemented an **ornithopter** mechanism with Gemini Pro
  - Generated a Leonardo da Vinci–style UI for it with Nano Banana


- 含视频（未转写）

[↑ 回到目录](#part-1--keywords)

### x-2012701592756383893

**Matthew Berman (@MatthewBerman)** · 发帖 2026-01-18 · [原帖](https://x.com/MatthewBerman/status/2012701592756383893)

- **MIT researchers sidestepped context window limits**
  - 10M+ token prompts become possible by moving context **out of the model and into code environments**


- 含视频（未转写）

[↑ 回到目录](#part-1--keywords)

### x-2011149280468484157

**KK.aWSB (@KKaWSB)** · 发帖 2026-01-13 · [原帖](https://x.com/KKaWSB/status/2011149280468484157)

- **别再说 AI 不能做设计**
  - **Cursor + Opus 4.5** 不到 10 分钟就做出一个带滚动叙事动画的落地页
  - 设计师做这样的页面通常要收几千美元
- 落地页如果还像 2010 年的应用，不是 AI 的问题，而是**工作流程**的问题


- 含视频（未转写）

[↑ 回到目录](#part-1--keywords)

### x-2009518503532089506

**KK.aWSB (@KKaWSB)** · 发帖 2026-01-09 · [原帖](https://x.com/KKaWSB/status/2009518503532089506)

- **字节跳动发布 UI-TARS-desktop** —— 本地运行的桌面自动化代理
  - 可以使用任何桌面应用、打开文件、浏览网站、自动执行任务
  - 无需云连接
  - 100% 开源


- 含视频（未转写）

[↑ 回到目录](#part-1--keywords)

### x-2010804702313652647

**Chris (@ChrisGPT)** · 发帖 2026-01-12 · [原帖](https://x.com/ChrisGPT/status/2010804702313652647)

- **Anthropic unveiled "Cowork"** — turns Claude into an autonomous virtual assistant for everyone
  - Brings agentic capabilities previously reserved for coders to general users
  - Claude performs complex tasks directly on your computer
- **Origin**: Anthropic noticed developers using **Claude Code** for everyday admin tasks
- **What it does**
  - Grant Claude access to folders to manage files, research, and complete multi-step workflows independently
  - Acts as a digital employee that "does" instead of just chats
- **Availability**: research preview for **Claude Max** subscribers on the **macOS app**
- **Competitive gap (per the author)**
  - Claude is shipping coding/desktop agents faster than competitors
  - Google still lacks a consumer browser agent; xAI has no native CLI or agentic interface
  - OpenAI has "Operator", Google has the developer-focused "Antigravity"
  - Anthropic is now the only other major lab with a true "do-it-for-me" experience for general users

<details><summary>原文</summary>

> BREAKING 🚨 Anthropic just unveiled "Cowork," a major feature that turns Claude into a fully autonomous virtual assistant for everyone. It brings the deep agentic capabilities previously reserved for coders to general users, allowing Claude to perform complex tasks directly on your computer.
>
> The tool was built after Anthropic noticed developers using "Claude Code" for everyday admin tasks. Cowork now lets anyone grant Claude access to folders to manage files, research, and complete multi-step workflows independently acting as a digital employee that "does" instead of just chats.
>
> Cowork is available today as a research preview for Claude Max subscribers on the macOS app 😡. Claude is releasing new coding/desktop agents much faster than all of there competitors. 
>
> This launch exposes a massive gap in the current AI landscape: in 2026, Google still explicitly lacks a consumer browser agent, and xAI has yet to release a native CLI or agentic interface. While OpenAI has "Operator" and Google has the developer-focused "Antigravity," Anthropic is now the only other major lab providing a true "do-it-for-me" experience for general users.

</details>

- 含视频（未转写）

[↑ 回到目录](#part-1--keywords)

### x-2010720188686348593

**DAIR.AI (@dair_ai)** · 发帖 2026-01-12 · [原帖](https://x.com/dair_ai/status/2010720188686348593)

- **Problem: LLM agents need memory for long conversations, and today's approaches are wasteful**
  - Retaining full interaction histories → massive redundancy
  - Iterative reasoning to filter noise → excessive token consumption
- **SimpleMem**: an efficient memory framework based on **semantic lossless compression**
  - Maximizes information density while minimizing token consumption
- **Three-stage pipeline**
  1. **Semantic Structured Compression**
     - Entropy-aware filtering distills raw dialogue into compact memory units
     - Resolves coreferences
     - Converts relative time ("last Friday") into absolute timestamps
  2. **Recursive Memory Consolidation**
     - Incrementally integrates related memories into higher-level abstractions
     - e.g. repeated "ordered a latte at 8 AM" → "regularly drinks coffee in the morning"
  3. **Adaptive Query-Aware Retrieval**
     - Dynamically adjusts retrieval scope based on query complexity
- **Results (LoCoMo benchmark, GPT-4.1-mini)**
  - **43.24 F1** vs strongest baseline Mem0 at 34.20 — a **26.4%** improvement
  - **531 tokens per query** vs 16,910 for full-context approaches — a **30x** reduction
  - Memory construction **14x faster than Mem0** (92.6s vs 1350.9s per sample) and **50x faster than A-Mem**
  - Even a 3B model with SimpleMem outperforms larger models using inferior memory strategies
- **Takeaway**: structured semantic compression + adaptive retrieval let agents keep reliable long-term memory without drowning in tokens or losing accuracy

<details><summary>原文</summary>

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

</details>

- 图片：[img1](https://pbs.twimg.com/media/G-eDWs3bQAEMAzs?format=jpg&name=large)

[↑ 回到目录](#part-1--keywords)

### x-2010579279789387929

**大梦想家迪士尼 (@discountifu)** · 发帖 2026-01-12 · [原帖](https://x.com/discountifu/status/2010579279789387929)

- 周末 vibe coding 了一个 **Multi-Agent AI Trading 终端**
  - 用 **Textual** 加了一套 TUI，Python 在这方面生态很好
  - 把自己毕生的交易经验"传功"给了 AI
- **支持多因子分析**：K 线走势、技术指标、订单流、资金费率、开仓量
- 作者表示点赞过 100 就开源


- 含视频（未转写）

[↑ 回到目录](#part-1--keywords)

### x-2010178642752704850

**Julian Goldie SEO (@JulianGoldieSEO)** · 发帖 2026-01-11 · [原帖](https://x.com/JulianGoldieSEO/status/2010178642752704850)

- **Things you can do with AntiGravity that most users miss**
  - Switch between free APIs (Opus, Sonnet, Claude)
  - Generate images with Google's Nano Banana
  - Connect MCP servers directly to your projects
  - Use Claude Code inside the terminal for better UI
  - Deploy apps to Netlify in one click
  - Pull NotebookLM content into your builds
- **Approach**: no paid APIs, no limits — just stack free tools

<details><summary>原文</summary>

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

</details>

- 含视频（未转写）

[↑ 回到目录](#part-1--keywords)

### x-2009709579903643768

**Md Ismail Šojal  (@0x0SojalSec)** · 发帖 2026-01-09 · [原帖](https://x.com/0x0SojalSec/status/2009709579903643768)

- **Open-sourced 42 n8n agent templates** from the "AI Agents A to Z" course
- Repo: http://github.com/gyoridavid/ai_agents_az


- 图片：[img1](https://pbs.twimg.com/media/G-Pr2R5bUAAchy8?format=png&name=large)

[↑ 回到目录](#part-1--keywords)

### x-2008576712695836685

**James Zou (@james_y_zou)** · 发帖 2026-01-06 · [原帖](https://x.com/james_y_zou/status/2008576712695836685)

- **Published in Nature Medicine: AI can predict 130 diseases from one night of sleep**
- **SleepFM** — a foundation model trained on 585K hours of sleep recordings from 65K people
  - Combines brain, heart, muscle, and breathing signals
  - The AI learns the "language of sleep"


- 图片：[img1](https://pbs.twimg.com/media/G9_ldwnWkAAevjh?format=jpg&name=large) [img2](https://pbs.twimg.com/media/G9_le27W0AElCBV?format=jpg&name=large)

[↑ 回到目录](#part-1--keywords)
