# IG Reports · 目录

- 共 5 份 PDF，2 个分类；文件在 [`ig/`](ig/)，编号越大越新
- 等邮件中：0 个链接
- 点标题 → 跳到详情；点文件名 → 打开 PDF
- 自动生成，勿手改

## Part 1 · Index

- **01 · AI & Agents**（4） — 生成式 AI、agent、LLM 落地与平台
  - [The Agentic Performance Management Playbook](#ig-05) · Nominal · `05.nominal-apm-playbook.pdf`
  - [A Practical Guide to AI Agents](#ig-03) · Snowflake · `03.snowflake-practical-guide-ai-agents.pdf`
  - [The Developer's Guide to RAG with Data Streaming](#ig-02) · Confluent · `02.confluent-rag-data-streaming.pdf`
  - [Evaluating Production-Grade AI Agents: Best Practices Guide](#ig-01) · Datadog · `01.datadog-evaluating-ai-agents.pdf`
- **04 · Security**（1） — 网络安全、身份、合规
  - [Model Context Protocol (MCP) Security Best Practices](#ig-04) · Wiz · `04.wiz-mcp-security-best-practices.pdf`

## Part 2 · Details

### ig-05

**The Agentic Performance Management Playbook**

- 文件：[05.nominal-apm-playbook.pdf](ig/05.nominal-apm-playbook.pdf) · 4881 KB
- 发布方：Nominal · 分类：AI & Agents · 类型：技术指南
- 来源：IG 分享帖 · 获取方式：form · 收录 2026-11-01 · [落地页](https://nominal.so/resources/the-agentic-performance-management-playbook/)
- **总结**：Nominal 出的 39 页指南，讲如何在财务团队里用 AI agent 落地「Agentic Performance Management（APM）」：由多个专职 agent 协同完成结账、对账、合并报表等多步财务流程，并保留审计留痕和控制。内容包括财务团队面临的人才与复杂度压力、APM 的四条核心原则、按场景的应用和效果、护栏与治理，以及一套区分真正 agent 执行系统和「AI 加持」类工具的评估清单。

### ig-04

**Model Context Protocol (MCP) Security Best Practices**

- 文件：[04.wiz-mcp-security-best-practices.pdf](ig/04.wiz-mcp-security-best-practices.pdf) · 6498 KB
- 发布方：Wiz · 分类：Security · 类型：技术指南
- 来源：IG 分享帖 · 获取方式：form · 收录 2026-11-01 · [落地页](https://www.wiz.io/lp/model-context-protocol-mcp-security-best-practices-cheat-sheet)
- **总结**：Wiz 的 MCP 安全 cheat sheet（6 页）。先说明 MCP 让 LLM agent 接入实时数据和工具的同时，也带来供应链攻击、prompt 注入导致远程代码执行、静默窃取数据等风险。给出 7 条实操建议：服务器和供应链安全、上下文和工具的最小权限（短期自动轮换、限定 audience 的 token）、人在回路和输出校验（写/执行操作前给出动作预览让用户确认）、隔离和沙箱（非 root 容器、出站白名单、系统调用过滤、资源配额）、用 MCP 网关集中管控、挑选安全的 MCP 服务器、用指标衡量效果。条目短、可直接照做。

### ig-03

**A Practical Guide to AI Agents**

- 文件：[03.snowflake-practical-guide-ai-agents.pdf](ig/03.snowflake-practical-guide-ai-agents.pdf) · 6198 KB
- 发布方：Snowflake · 分类：AI & Agents · 类型：电子书
- 来源：IG 私信链接 · 获取方式：form · 收录 2026-11-01 · [落地页](https://www.snowflake.com/resource/a-practical-guide-to-ai-agents/)
- **总结**：Snowflake 电子书（21 页），面向业务和技术决策者讲 AI agent 落地。先区分生成式 AI 和能处理多步交互的 agent，再分五章讲：agent 的商业价值、实现所需的平台（含可扩展性等五条 agentic AI 架构原则和 AI 应用框架图）、伦理和偏见、落地路线图（先评估数据基础、对齐业务目标、兼顾安全合规），最后介绍 Snowflake 的数据 agent。附客服、媒体、金融等行业用例，如某呼叫中心用 agent 每小时多解决 14% 的问题。偏入门和厂商视角。

### ig-02

**The Developer's Guide to RAG with Data Streaming**

- 文件：[02.confluent-rag-data-streaming.pdf](ig/02.confluent-rag-data-streaming.pdf) · 15800 KB
- 发布方：Confluent · 分类：AI & Agents · 类型：技术指南
- 来源：IG 分享帖 · 获取方式：form · 收录 2026-11-01 · [落地页](https://www.confluent.io/resources/ebook/developers-guide-to-rag/)
- **总结**：Confluent 电子书（22 页），讲怎么用数据流平台（Kafka + Flink）给生成式 AI 应用做实时 RAG。以虚构航空公司客服机器人 Conflyent 为例，指出 LLM 需要新鲜、可信、带上下文的数据。把 RAG 拆成四步：数据增强、推理、工作流、后处理，逐步讲 connector、Flink SQL、AI 模型推理、Table API/UDF 和流治理怎么用。最后给出商品推荐、实时情感分析、招聘门户三套参考架构和客户案例。偏厂商方案，但架构拆解清楚。

### ig-01

**Evaluating Production-Grade AI Agents: Best Practices Guide**

- 文件：[01.datadog-evaluating-ai-agents.pdf](ig/01.datadog-evaluating-ai-agents.pdf) · 1820 KB
- 发布方：Datadog · 分类：AI & Agents · 类型：技术指南
- 来源：IG 私信链接 · 获取方式：direct · 收录 2026-11-01 · [落地页](https://lp.datadoghq.com/rs/875-UVY-685/images/eBook-2026AIAgentsBestPractices.pdf?version=1)
- **总结**：Datadog「Best Practice Series」电子书（9 页），讲 LLM 应用和 agent 的离线评估（offline evaluation），重点是上线前怎么验证改动，偏方法指南。拆成三个部分：带标注的数据集（Data）、组装 prompt 和上下文的应用逻辑（Tasks）、给输出打分的评估器（Evaluators，确定性规则或 LLM-as-a-judge）。还讲了数据集要覆盖多轮对话、跑题和对抗性 prompt，以及用元数据给实验结果切片。全程以示例应用 Contract Redliner 演示，最后落到在 CI/CD 里做回归测试。
