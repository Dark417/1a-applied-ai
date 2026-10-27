# Coding Agent 实践

- [← 返回总目录](x-note.md)
- Claude Code / Codex 的用法、工作流与配套工具
- 共 8 篇，按收藏顺序倒序（最新在上）

## Part 1 · Index

- [VS Code Agent Debug Logs：看清每次 prompt 背后发生了什么](#x-2050341770609750297) · @code · 2026-05-01 · 工具发布
- [How to Become a Claude Code Power User (Full Course)](#x-2047245243503050997) · @eng_khairallah1 · 2026-04-23 · 使用教程（长文）
- [Anthropic 团队演示他们如何用 Claude Code](#x-2047331926143619428) · @eng_khairallah1 · 2026-04-23 · 视频推荐
- [Google 发布全栈 vibe coding 系统](#x-2034718045550051489) · @__Inty__ · 2026-03-19 · 新闻 / 观点
- [Boris Cherny 30 分钟分享 Claude Code 技巧](#x-2046264877703102753) · @cnyzgkc · 2026-04-20 · 视频推荐
- [OpenAI 用 Codex 维护 Agents SDK 的四层结构](#x-2031347640630165525) · @chenchengpro · 2026-03-10 · 方法介绍
- [GitNexus：给代码库建知识图谱，经 MCP 喂给 AI](#x-2026178278055403843) · @GitHub_Daily · 2026-02-24 · 工具介绍
- [离不开 Claude Code 的三个场景](#x-2022157972613300368) · @yanhua1010 · 2026-02-13 · 工作流分享

## Part 2 · Details

### x-2050341770609750297

**VS Code Agent Debug Logs：看清每次 prompt 背后发生了什么**

- 作者：Visual Studio Code (@code) · 发帖 2026-05-01 · [原帖](https://x.com/code/status/2050341770609750297)
- 来源：🔖 收藏 · 拉取 2026-10-27 · 类型：工具发布
- **总结**：VS Code 官方介绍 Copilot 的 Agent Debug Logs 视图：可以检查对话交互、tool call、模型请求、prompt 发现过程和 agent 流程。对调试 agent 行为、理解 harness 实际往上下文里放了什么很有用。附官方文档链接。

**正文**

- **Agent Debug Logs** (VS Code Copilot Chat) show what happens behind each prompt
  - Inspect chat interactions, tool calls, model requests, prompt discovery, agent flows, and more
- Docs: https://code.visualstudio.com/docs/copilot/chat/chat-debug-view


- 含视频（未转写）

[↑ 回到本页目录](#part-1--index)

### x-2047245243503050997

**How to Become a Claude Code Power User (Full Course)**

- 作者：Khairallah AL-Awady (@eng_khairallah1) · 发帖 2026-04-23 · [原帖](https://x.com/eng_khairallah1/status/2047245243503050997)
- 来源：🔖 收藏 · 拉取 2026-10-27 · 类型：使用教程（长文）
- **总结**：按 6 个等级讲 Claude Code 的进阶用法：L1 写好 CLAUDE.md（技术栈、规范、禁止事项）并理解层级；L2 用「模式」而不是「单条消息」思考，区分 Plan Mode 和直接执行；L3 内置工具和自定义 slash command；L4 Skills 和 CLAUDE.md 的区别、按路径生效的规则；L5 接入 CI/CD；L6 完整的 power user 工作流。核心论点：普通用户和 power user 的差距在配置和工作流，不在天赋。

**正文**

- **Most users treat Claude Code like a fancy autocomplete**
  - Paste a bug → get a fix; paste a feature request → get some code
  - One question, one answer, over and over — never building on anything
  - Like buying a Ferrari and only driving it in first gear
- **Claude Code is an autonomous engineering partner, not a code-suggestion tool**
  - It can read your entire codebase, understand your architecture, execute multi-step plans, run tests, debug failures, and ship features end to end
  - Only if you know how to use it properly
- **The gap between casual and power user isn't talent — it's configuration and workflow**
  - Knowing the 20% of features that deliver 80% of the results
  - This course: everything learned from months of daily use
- **Level 1: The foundation most people skip**
  - **`CLAUDE.md` is your secret weapon** — the most important file in your project, and most people never create it
    - Sits in the project root and tells Claude Code how your codebase works: conventions, patterns, rules, preferences
    - **Without it, Claude Code is guessing.** It doesn't know that:
      - Your team uses camelCase
      - You prefer functional components over class components
      - Your API naming convention is verb-first
      - You never use any-typed variables
    - **With a good one, it follows your team's standards automatically** — every file, function, and test it writes
  - **What belongs in `CLAUDE.md`**
    - Tech stack and versions
    - Coding conventions and naming patterns
    - File structure and where things go
    - Testing requirements and what makes a good test
    - Preferred error-handling patterns
    - Common pitfalls specific to your codebase
    - Things Claude should never do in this project
  - Spend 30 minutes writing it — saves thousands of corrections over the next year
  - **The `CLAUDE.md` hierarchy — three levels**
    - **User-level** — `~/.claude/CLAUDE.md`
      - Personal: your preferences, shortcuts, style
      - Not version-controlled; teammates never see it
    - **Project-level** — `.claude/CLAUDE.md` in your repo root
      - Shared with the whole team via git
      - Team standards, architectural decisions, universal rules
    - **Directory-level** — inside specific directories
      - Applies only when Claude Code works on files in that directory
      - Good for sub-projects or modules with different conventions
    - **Most common mistake**: putting team-wide rules in user-level config
      - Then the new developer's Claude Code doesn't follow the same standards
      - **Fix: move shared rules to project-level**
- **Level 2: Think in modes, not messages**
  - **Plan mode vs direct execution**
    - **Direct execution** — clear, limited scope
      - Fix this bug, add this validation, rename this variable across the codebase
      - Claude Code handles these immediately, no planning needed
    - **Plan mode** — everything bigger
      - Refactoring a module, a feature touching multiple files, migrating patterns, restructuring the test suite
      - Claude Code first outlines which files it will touch, what changes, and in what order
      - You review the plan before any code is written
  - **Rule: if the task touches more than 2 files or needs architectural decisions, use plan mode**
    - Skipping planning on complex tasks means more time undoing damage than you saved
- **Level 3: Tools that make Claude Code dangerous**
  - **Built-in tools most people never discover**
    - **Grep vs Glob**
      - **Grep** searches file contents → use it to find where a function is called
      - **Glob** matches file paths → use it to find all test files
      - Most people use the wrong one and waste time
      - The Claude Certified Architect exam literally tests this distinction
    - **Read, Write, Edit**
      - **Edit** — targeted modifications via unique text matching; fast and precise
      - When Edit fails because the match isn't unique → fall back to **Read + Write**: read the full file, write the complete modified version
    - **The `/memory` command**
      - Shows which memory files Claude Code has loaded
      - Your debugging tool when behavior is inconsistent — check the right context is actually loaded
  - **Custom slash commands** — for tasks you run repeatedly
    - Shared team commands: `.claude/commands/`
    - Personal commands: `~/.claude/commands/`
    - Examples:
      - `/review` — runs your team's code review checklist
      - `/test` — generates tests following your patterns
      - `/deploy-check` — verifies everything is ready for deployment
    - 10 minutes to create; saves hours of repetitive prompting
- **Level 4: Skills and context engineering**
  - **Skills vs `CLAUDE.md`**
    - **`CLAUDE.md` is always loaded** — every session, every task → universal standards
    - **Skills are on-demand** — activate when invoked → task-specific workflows
    - Common mistake: putting task-specific procedures in `CLAUDE.md`
      - The file bloats
      - Claude Code gets confused by irrelevant context
      - You burn tokens on instructions that don't apply
    - **Rule: applies to every task → `CLAUDE.md`; applies to a specific type of work → make it a skill**
  - **Path-specific rules** — teams discover this and wonder how they lived without it
    - Create rule files in `.claude/rules/` with YAML frontmatter specifying glob patterns:
    ```yaml
    ---
    paths: ["**/*.test.tsx"]
    ---
    All tests must use the arrange-act-assert pattern.
    Never mock the database layer directly.
    ```
    - Rules load only when Claude Code edits files matching the pattern
    - Every test file in the codebase, in any directory, gets the same testing conventions automatically
    - **Far more powerful than directory-level `CLAUDE.md`** because it works across the whole project structure
- **Level 5: CI/CD integration**
  - **The `-p` flag runs Claude Code in non-interactive mode**
    - Without it, your CI job hangs forever waiting for input
    - Described as the single most tested concept in the Claude Certified Architect exam
  - Use `--output-format json` with `--json-schema` for machine-parseable structured output
    - CI can then post findings as inline PR comments automatically
  - **Critical insight: the session that generated code is worse at reviewing its own changes**
    - It keeps reasoning context that biases it toward its own decisions
    - **Always use an independent review instance for code review in CI**
- **Level 6: The power-user workflow** — a typical day
  - **Morning**
    - Open terminal; Claude Code auto-loads `CLAUDE.md` and relevant path-specific rules
    - Describe the first feature in plain language → Claude Code creates a plan
    - You review, adjust one step, approve
    - It executes across 8 files, writes tests, runs them, fixes two failures, and commits
  - **Afternoon**
    - Reviewing a PR: run your custom `/review` command instead of reading every line
    - Claude Code checks against team standards, flags 3 issues, explains why each matters
    - You fix the one real issue and approve the rest
  - **End of day**
    - CI runs Claude Code with `-p` on every new PR
    - Automated security review, test generation for uncovered paths, documentation updates
    - All posted as PR comments
  - This is what power users do now, not the future
- **The certification path**
  - Anthropic offers the **Claude Certified Architect Foundations** exam
  - Tests everything here: `CLAUDE.md` hierarchy, tool usage, plan mode, path-specific rules, CI/CD integration, prompt engineering, MCP configuration
  - **Format**: scenario-based multiple choice
    - Wrong answers are designed to sound like good engineering
    - Right answers require knowing exactly which technique fits which problem
  - If you've built real projects with Claude Code and understand these concepts, you're ready
- **The bottom line**
  - Claude Code is the most powerful developer tool most developers barely use
  - Going from casual to power user takes **a few days of intentional setup and practice**, not months
  - **The five things to do**:
    1. Configure your `CLAUDE.md`
    2. Learn plan mode
    3. Build custom commands
    4. Use path-specific rules
    5. Integrate it into CI
  - Do those and you'll ship more code in a week than most developers ship in a month
  - Most people will keep getting one-off answers to one-off questions; those who build a real system around it will be at a different level within 30 days

<details><summary>原文</summary>

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

</details>

- 图片：[img1](https://pbs.twimg.com/media/HGiv5cPbUAEfC8E?format=jpg&name=large)

[↑ 回到本页目录](#part-1--index)

### x-2047331926143619428

**Anthropic 团队演示他们如何用 Claude Code**

- 作者：Khairallah AL-Awady (@eng_khairallah1) · 发帖 2026-04-23 · [原帖](https://x.com/eng_khairallah1/status/2047331926143619428)
- 来源：🔖 收藏 · 拉取 2026-10-27 · 类型：视频推荐
- **总结**：推荐 Anthropic 团队 30 分钟的 Claude Code workshop，提到 Claude Code 负责人已经好几个月没手写代码。thread 里附了另一篇《40 个 Claude Cowork 命令、工作流和自动化》的链接。帖子本身没有技术细节，价值在视频。

**正文**

- **Anthropic's team showed how they actually use Claude Code** in a free 30-minute workshop
  - The head of Claude Code hasn't written code by hand in months
- If one feature takes you 3 hours in Claude Code, it's likely because nobody taught you to use it properly
- Related: 40 Claude Cowork commands, workflows & automations most users don't know — https://x.com/eng_khairallah1/status/2047609433489035739?s=46

<details><summary>原文</summary>

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

</details>

- 含视频（未转写）

[↑ 回到本页目录](#part-1--index)

### x-2034718045550051489

**Google 发布全栈 vibe coding 系统**

- 作者：Inty News (@__Inty__) · 发帖 2026-03-19 · [原帖](https://x.com/__Inty__/status/2034718045550051489)
- 来源：❤️ 点赞的评论 → 原帖（via [2034822429894406502](https://x.com/i/status/2034822429894406502)） · 拉取 2026-10-27 · 类型：新闻 / 观点
- **总结**：你点赞的评论所在的原帖，只有一句话：Google 发布了自己的全栈「氛围编码」系统，作者断言很多后端程序员会因此失业。帖子没有具体产品细节或技术说明，属于情绪化快讯，信息量低。可以当作「Google 进入全栈 AI 编码赛道」的一个时间点来记。

**正文**

- **谷歌发布了自己的全栈氛围编码（vibe coding）系统**
- 作者认为大部分后端程序员也将受到冲击


- 含视频（未转写）

[↑ 回到本页目录](#part-1--index)

### x-2046264877703102753

**Boris Cherny 30 分钟分享 Claude Code 技巧**

- 作者：木马人 (@cnyzgkc) · 发帖 2026-04-20 · [原帖](https://x.com/cnyzgkc/status/2046264877703102753)
- 来源：🔖 收藏 · 拉取 2026-10-27 · 类型：视频推荐
- **总结**：推荐 Claude Code 创始人 Boris Cherny 的 30 分钟视频，内容是 Claude Code 的使用技巧和工作流。帖子本身只有推荐语，没有展开要点。

**正文**

- **Claude Code 创始人 Boris Cherny** 用 30 分钟分享了 Claude Code 的使用技巧和工作流
- 作者认为看这一个视频胜过看 100 个 YouTube 教程


- 含视频（未转写）

[↑ 回到本页目录](#part-1--index)

### x-2031347640630165525

**OpenAI 用 Codex 维护 Agents SDK 的四层结构**

- 作者：陈成 (@chenchengpro) · 发帖 2026-03-10 · [原帖](https://x.com/chenchengpro/status/2031347640630165525)
- 来源：🔖 收藏 · 拉取 2026-10-27 · 类型：方法介绍
- **总结**：拆解 OpenAI 用 Codex 维护 Agents SDK 的做法，核心是四层：①AGENTS.md 用 if/then 写强制触发规则；②.agents/skills/ 封装工作流，一个 skill 只做一件事，一个触发条件、一个输出；③scripts/ 放固定顺序的 shell 操作，不让模型每次重新猜；④本地稳定后搬进 Codex GitHub Action。关键细节：skill 的 description 是路由信号而不是注释，路由不准先改 description。附示例仓库。

**正文**

- **OpenAI 公开了用 Codex 维护 Agents SDK 的完整方案**
- **核心结构只有四层**
  1. **`AGENTS.md`** —— 强制触发规则，用 if/then 写清楚什么情况必须调用哪个 workflow
  2. **`.agents/skills/`** —— 封装具体工作流；每个 skill 一件事、一个触发条件、一个输出
  3. **`scripts/`** —— 固定顺序的 shell 操作放这里，不让模型每次重新猜
  4. **Codex GitHub Action** —— 本地跑稳定了就搬进 CI，逻辑完全复用
- **容易忽视的细节：skill 的 `description` 字段是路由信号，不是注释**
  - 写模糊了，agent 就不知道该用哪个 skill
  - 建议：路由不准先改 description，别加代码
- **推广开来**：任何项目，只要把工程规范显式编码进仓库，agent 的行为就会稳定得多
- 示例仓库：https://github.com/openai/openai-agents-python
- 原文：https://developers.openai.com/blog/skills-agents-sdk

<details><summary>原文</summary>

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

</details>

- 链接卡片：[GitHub - openai/openai-agents-python: A lightweight, powerful framework for mult](https://t.co/OhaQYxkm93)

[↑ 回到本页目录](#part-1--index)

### x-2026178278055403843

**GitNexus：给代码库建知识图谱，经 MCP 喂给 AI**

- 作者：GitHubDaily (@GitHub_Daily) · 发帖 2026-02-24 · [原帖](https://x.com/GitHub_Daily/status/2026178278055403843)
- 来源：🔖 收藏 · 拉取 2026-10-27 · 类型：工具介绍
- **总结**：GitNexus 解决「AI 修一个 bug 引出三个新 bug」的问题：给代码库建知识图谱，让 AI 理解架构、依赖和调用链；通过 MCP 接入 Cursor 或 Claude Code，改代码前先查上下游；能生成架构图，也能在 Web 端可视化。支持 TS、Python、Java，索引完全本地。属于给 coding agent 补上下文的工具。

**正文**

- **痛点**：用 AI 写代码最怕修好一个 Bug，却在不知名的地方引爆三个新 Bug
  - 多数 AI 编程助手只是指哪改哪，无法理解代码间的深层依赖
- **GitNexus**：给项目代码建立**知识图谱**，让 AI 理解整个项目的架构、依赖和调用链
  - GitHub：http://github.com/abhigyanpatwari/GitNexus
- **功能**
  - 通过 **MCP** 接入 Cursor 或 Claude Code，让 AI 改代码前先看清函数间的上下游关系
  - 可生成架构图，或在 Web 端可视化查看整个代码库的逻辑脉络
  - 提供 **CLI** 和 **Web** 两种模式
  - 支持 TypeScript、Python、Java 等主流语言
  - 所有索引和分析都在本地完成，数据不上传服务器，隐私性好
- 适合担心 AI 改动破坏原有代码的人，作为增强上下文的工具整合进工作流

<details><summary>原文</summary>

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

</details>

- 含视频（未转写）

[↑ 回到本页目录](#part-1--index)

### x-2022157972613300368

**离不开 Claude Code 的三个场景**

- 作者：Yanhua (@yanhua1010) · 发帖 2026-02-13 · [原帖](https://x.com/yanhua1010/status/2022157972613300368)
- 来源：🔖 收藏 · 拉取 2026-10-27 · 类型：工作流分享
- **总结**：作者的三个 Claude Code 使用场景：①在 OpenClaw 里配 Claude Code，做 7×24 的个人助理（邮件、查资料、翻译）；②Obsidian + Claudian 插件做内容生产流水线，16 个自定义 skill 覆盖写作、配图、发布；③在 Antigravity 里用 Claude 管架构、Gemini 管迭代。详细拆解在原文链接里。

**正文**

- **作者 2026 年已离不开 Claude Code，三个场景覆盖几乎所有工作**
  1. **日常 AI 助理** —— 在 OpenClaw 里配好 Claude Code：写邮件、查资料、翻译、头脑风暴，7x24 全能助手
  2. **内容创作超级大脑** —— Obsidian + **Claudian** 插件：写文章、生成配图、一键发布，全在笔记库里完成
  3. **编程搭子** —— 在 Antigravity 里用 CC CLI 搭配 Gemini Pro：Claude 管架构，Gemini 管迭代，双模型取长补短
- **场景二投入最深**
  - 用 Obsidian + Claude 搭了一套完整的内容生产流水线，从信息源到成品发布
  - 16 个自定义 Skills 覆盖写作、配图、发布全流程

<details><summary>原文</summary>

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

</details>


[↑ 回到本页目录](#part-1--index)
