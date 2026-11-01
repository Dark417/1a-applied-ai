# IG Reports · 目录

- 共 1 份 PDF，1 个分类；文件在 [`ig/`](ig/)，编号越大越新
- 等邮件中：0 个链接
- 点标题 → 跳到详情；点文件名 → 打开 PDF
- 自动生成，勿手改

## Part 1 · Index

- **01 · AI & Agents**（1） — 生成式 AI、agent、LLM 落地与平台
  - [Evaluating Production-Grade AI Agents: Best Practices Guide](#ig-01) · Datadog · `01.datadog-evaluating-ai-agents.pdf`

## Part 2 · Details

### ig-01

**Evaluating Production-Grade AI Agents: Best Practices Guide**

- 文件：[01.datadog-evaluating-ai-agents.pdf](ig/01.datadog-evaluating-ai-agents.pdf) · 1820 KB
- 发布方：Datadog · 分类：AI & Agents · 类型：技术指南
- 来源：IG 私信链接 · 获取方式：direct · 收录 2026-11-01 · [落地页](https://lp.datadoghq.com/rs/875-UVY-685/images/eBook-2026AIAgentsBestPractices.pdf?version=1)
- **总结**：Datadog「Best Practice Series」电子书（9 页），讲 LLM 应用和 agent 的离线评估（offline evaluation），重点是上线前怎么验证改动，偏方法指南。拆成三个部分：带标注的数据集（Data）、组装 prompt 和上下文的应用逻辑（Tasks）、给输出打分的评估器（Evaluators，确定性规则或 LLM-as-a-judge）。还讲了数据集要覆盖多轮对话、跑题和对抗性 prompt，以及用元数据给实验结果切片。全程以示例应用 Contract Redliner 演示，最后落到在 CI/CD 里做回归测试。
