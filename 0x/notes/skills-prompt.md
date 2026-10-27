# Skills & Prompt

- [← 返回总目录](../x-note.md)
- Skills 设计、可复用 prompt 与技能库
- 共 6 篇，按收藏顺序倒序（最新在上）

## Part 1 · Index

- [Markdown Viewer Skills：让 AI 在 Markdown 里直接画图](#x-2047525971742597195) · @GitHub_Daily · 2026-04-24 · 工具推荐
- [Addy Osmani 开源 Agent Skills：老工程师的操作手册](#x-2046454424806343139) · @KengGuangLong · 2026-04-21 · 工具介绍
- [obra/superpowers 的 brainstorming SKILL](#x-2028854979805790269) · @cholf5 · 2026-03-03 · 工具推荐 + 使用心得
- [Anthropic《The Complete Guide to Building Skills for Claude》解读](#x-2027350587533332748) · @heyrimsha · 2026-02-27 · 概念介绍
- [把 GitHub 开源项目打包成 Skill](#x-2014100945416888444) · @gkxspace · 2026-01-21 · 观点 / 用法
- [OpenAI 官方 Prompt Packs：300+ 岗位提示词](#x-2014252422806536614) · @zstmfhy · 2026-01-22 · 资源推荐

## Part 2 · Details

### x-2047525971742597195

**Markdown Viewer Skills：让 AI 在 Markdown 里直接画图**

- 作者：GitHubDaily (@GitHub_Daily) · 发帖 2026-04-24 · [原帖](https://x.com/GitHub_Daily/status/2047525971742597195)
- 来源：🔖 收藏 · 拉取 2026-10-27 · 类型：工具推荐
- **总结**：介绍开源的 Markdown Viewer skills：内置 14 个绘图技能，可以在 Markdown 里生成架构图、流程图、状态图、部署图、类图等，支持 PlantUML、Vega 等 5 种渲染引擎，还能输出 HTML 信息卡。可以一键装到 Claude Code、Codex、Cursor。适合写技术文档时自动生成配图。

**正文**

- **痛点**：用 AI 写技术文档时，流程图、架构图等可视化内容往往要切到其他画图工具
- **Markdown Viewer 技能**：让 AI 编程助手直接在 Markdown 里生成专业图表
  - GitHub：http://github.com/markdown-viewer/skills
- **能力**
  - 内置 **14 个专业绘图技能**
  - 可生成架构图、流程图、工作流图、状态图、部署图、类图、用例图等上百种图表
  - 支持 **PlantUML**、**Vega** 等五大主流渲染引擎
  - 能直接输出排版精美的 HTML 信息卡片
  - 提供一键安装指令，支持 Claude Code、Codex、Cursor 等
- 适合经常写技术文档、或想让 AI 自动生成高质量配图的开发者

<details><summary>原文</summary>

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

</details>

- 图片：[img1](https://pbs.twimg.com/media/HGpGBCfaQAA9RzW?format=jpg&name=large)

[↑ 回到本页目录](#part-1--index)

### x-2046454424806343139

**Addy Osmani 开源 Agent Skills：老工程师的操作手册**

- 作者：非著名程序员 (@KengGuangLong) · 发帖 2026-04-21 · [原帖](https://x.com/KengGuangLong/status/2046454424806343139)
- 来源：🔖 收藏 · 拉取 2026-10-27 · 类型：工具介绍
- **总结**：介绍 Google 的 Addy Osmani 开源的 Agent Skills（1.8 万+ star）：把资深工程师的工作流和规范做成标准化技能库，覆盖需求、规划、构建、验证、评审、发布 6 个阶段，共 20 个核心 skill，用 /spec、/plan、/build、/test、/ship 等 7 个命令触发。支持 Claude Code、Gemini CLI、Codex、Cursor。思路是把工程规范显式编码进 agent。

**正文**

- **Google Gemini 团队主管 Addy Osmani 开源了 Agent Skills 项目**，短时间在 GitHub 拿到 18000+ Star
- **做的事**：把资深工程师多年积累的工作流程和开发规范，整理成标准化技能库
  - 让 AI 编程助手在写代码的每个环节都按统一的高标准执行
  - 相当于给 AI 配了一本老工程师的操作手册
- **围绕软件开发完整生命周期设计**
  - 六个阶段：需求定义 → 规划 → 构建 → 验证 → 评审 → 发布上线
  - 共 **20 个核心技能**，每个阶段该做什么、注意什么都有规范
- **7 个触发命令**，每个命令自动调用相关技能组合，无需手动配置，例如：
  - `/spec` —— 开始写需求文档
  - `/plan` —— 自动拆解任务
  - `/build` —— 进入编码阶段
  - `/test` —— 跑测试
  - `/ship` —— 走部署流程
- **兼容性**：支持 Claude Code、Gemini CLI、Codex、Cursor 等主流 AI 编程工具
- 已在用 AI 辅助开发的话，可以接入这套 Skills，看交付质量能否再上一个台阶

<details><summary>原文</summary>

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

</details>

- 链接卡片：[GitHub - addyosmani/agent-skills: Production-grade engineering skills for AI cod](https://t.co/8pMhW2Xjod)

[↑ 回到本页目录](#part-1--index)

### x-2028854979805790269

**obra/superpowers 的 brainstorming SKILL**

- 作者：周尔复 (@cholf5) · 发帖 2026-03-03 · [原帖](https://x.com/cholf5/status/2028854979805790269)
- 来源：🔖 收藏 · 拉取 2026-10-27 · 类型：工具推荐 + 使用心得
- **总结**：推荐 obra/superpowers 里的 brainstorming SKILL.md：先理解项目上下文，每次只问一个问题，逐步把想法细化成设计和规格，确认后再动手。作者的体会：英文原版不用翻译，更准也更省 token；原版里「每次生成计划都 git commit」建议去掉。是「好 skill 的写法」的范例，可以对照学习。

**正文**

- **推荐一个很强的头脑风暴 SKILL**：https://github.com/obra/superpowers/blob/main/skills/brainstorming/SKILL.md
  - 同事用过都说好，用了才体会到 Prompt Engineering 和 SKILL 的重要性
  - 看着都是大白话，但一般人总结不出来；这些话像咒语一样让 Agent 更高效地工作
- **SKILL 内容概要：将想法头脑风暴成设计**
  - 通过自然的协作式对话，把想法转化为完整的设计和规格说明
  - 先理解当前项目上下文，然后**一次只提一个问题**，逐步细化想法
  - 清楚要构建什么之后，提出设计方案并获得用户批准
- **使用心得**
  - 作者现在没有它就拒绝 Vibe Coding
  - SKILL 是纯英文的，没必要翻译成中文：英文更准确还省 Token；你用中文聊，它一样用中文回复
  - **坑**：原版要求每次生成计划都 `git commit`，建议去掉

<details><summary>原文</summary>

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

</details>

- 图片：[img1](https://pbs.twimg.com/media/HCfv2rnbgAAjlMA?format=jpg&name=large)

[↑ 回到本页目录](#part-1--index)

### x-2027350587533332748

**Anthropic《The Complete Guide to Building Skills for Claude》解读**

- 作者：Rimsha Bhardwaj (@heyrimsha) · 发帖 2026-02-27 · [原帖](https://x.com/heyrimsha/status/2027350587533332748)
- 来源：🔖 收藏 · 拉取 2026-10-27 · 类型：概念介绍
- **总结**：解读 Anthropic 30+ 页的 Skills 指南。核心：skill 不是 prompt，而是一个结构化系统。把指令打包进 SKILL.md，可以附带脚本、参考资料和素材，一次教会，反复使用。关键机制是 progressive disclosure：先只加载轻量的 YAML frontmatter，让 Claude 判断何时用；相关时才加载完整指令；附加文件按需读取。观点是从「prompt engineering」转向「执行设计」。

**正文**

- **Anthropic released a 30+ page guide: _The Complete Guide to Building Skills for Claude_**
  - Shifts the conversation from "prompt engineering" to **execution design**
- **A Skill isn't just a prompt — it's a structured system**
  - Instructions packaged in a `SKILL.md` file
  - Optionally add scripts, references, and assets
  - Teach Claude a repeatable workflow once instead of re-explaining it every chat
- **The real unlock: progressive disclosure** — instead of dumping everything into context:
  - Lightweight **YAML frontmatter** tells Claude when to use the skill
  - Full instructions load only when relevant
  - Extra files are accessed only if needed
  - Result: less context bloat, more precision
- **Analogy: MCP gives Claude the kitchen; Skills give it the recipe**
  - Without skills: users connect tools and don't know what to do next
  - With skills: workflows trigger automatically, best practices are embedded, API calls become consistent
- **3 major patterns**
  1. Document & asset creation
  2. Workflow automation
  3. MCP enhancement
- **Testing — what most builders ignore**
  - Trigger accuracy
  - Tool call efficiency
  - Failure rate
  - Token usage
- **It's about designing an execution layer on top of LLMs, not clever wording**
  - Skills work across Claude, Claude Code, and the API — build once, deploy everywhere
- Guide: https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf

<details><summary>原文</summary>

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

</details>

- 图片：[img1](https://pbs.twimg.com/media/HCKYnWta8AAh0wU?format=jpg&name=large)

[↑ 回到本页目录](#part-1--index)

### x-2014100945416888444

**把 GitHub 开源项目打包成 Skill**

- 作者：余温 (@gkxspace) · 发帖 2026-01-21 · [原帖](https://x.com/gkxspace/status/2014100945416888444)
- 来源：🔖 收藏 · 拉取 2026-10-27 · 类型：观点 / 用法
- **总结**：观点：有了 Skills 以后，可以让 Claude Code 把成熟的开源项目（比如 yt-dlp）分析并封装成 skill，几分钟就得到可用工具，以后扔个链接就能下载视频。经过大量验证的开源项目，稳定性远超 AI 临时写的代码。这是「skill 作为开源能力的封装层」的思路。

**正文**

- **以前**：GitHub 上的牛逼开源项目对编程小白来说"看得到用不了"
  - 例：**yt-dlp**，143k star 的视频下载神器，但部署、命令行、环境配置就很劝退
- **现在有了 Skills**：直接跟 Claude Code 说"帮我把 yt-dlp 打包成 Skill"
  - 它会自己分析项目、写封装、处理依赖
  - 几分钟后就有一个能用的视频下载工具，以后下载 YouTube 视频直接扔链接
- **不只是视频下载**：格式转换、网页转 APP、密码破译……经过无数人验证的 GitHub 项目都能变成 Skill
- 这些开源项目的稳定性和成功率，远超 AI 临时写的代码

<details><summary>原文</summary>

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

</details>


[↑ 回到本页目录](#part-1--index)

### x-2014252422806536614

**OpenAI 官方 Prompt Packs：300+ 岗位提示词**

- 作者：AI奶爸 (@zstmfhy) · 发帖 2026-01-22 · [原帖](https://x.com/zstmfhy/status/2014252422806536614)
- 来源：🔖 收藏 · 拉取 2026-10-27 · 类型：资源推荐
- **总结**：OpenAI Academy 公开了按岗位分类的 prompt pack：销售、产品、工程、HR、经理、IT、客服、高管等，每个岗位 20–30 条，总共 300 多条，免费。作者认为工程和产品两个包最有用。附官方地址。

**正文**

> OpenAI 终于把官方 Prompt 公开了！  
>
> 直接给销售、产品、工程师、HR、经理、IT、客服、高管……每个岗位都塞了 20-30 个现成能打的高质量提示词包，总量 300+ 个，全部免费拿走用。
>
> 以前我们自己调 prompt 像炼丹，现在 OpenAI 直接把丹炉和配方都端出来了😂  
> 尤其是工程师和产品那两包，看完第一感觉是：这要是早点出，我去年少加多少班啊……
>
> 地址
> https://academy.openai.com/public/tags/prompt-packs-6849a0f98c613939acef841c


[↑ 回到本页目录](#part-1--index)
