# 0x · X (Twitter) 收藏 → 学习笔记

这是一个用 AI 自动化学习的 demo：把我在 X 上 ❤️ 和 🔖 的帖子增量拉下来，整理成可以直接读的笔记。

## 怎么读

- [`x-note.md`](./x-note.md)：🔖 精读总目录
  - 按主题分组，编号就是重要性顺序
  - 点主题名 → 打开主题文件；点标题 → 跳到那篇的详情
- `01-…md` ~ `10-…md`：每个主题一个文件
  - 上半部分：Index
  - 下半部分：总结 + strong bullet 版正文 + 折叠的原文
- [`x-new.md`](./x-new.md)：❤️ 速览
  - 上半部分：关键词 + 简述
  - 下半部分：正文；同时在精读里的帖子只给链接

| 编号 | 主题 |
|---|---|
| 01 | Harness & Loop Engineering |
| 02 | Graph & Multi-Agent |
| 03 | Agent Memory & RAG |
| 04 | Evals & 研究 |
| 05 | Coding Agent 实践 |
| 06 | Skills & Prompt |
| 07 | OpenClaw & 个人 Agent |
| 08 | LLM 基础 & 课程 |
| 09 | 其他应用 |
| 10 | 其他 |

## 规则

- ❤️ 进 `x-new.md`；🔖 进精读
- 既 ❤️ 又 🔖：两边都算，但 `x-new.md` 不重复贴全文
- ❤️ 的是一条评论：取它的原帖，放进精读
- 只收作者本人的内容：原帖和作者自己连续发的 thread，不收评论
- 排序：按我点 ❤️ / 🔖 的顺序，最新在上
- 每篇帖子按 id 只存一份，多次运行不会重复

## 流水线（`_sync/`）

```
_sync/
├── RUNBOOK.md            # 每次运行的步骤（定时任务读这份）
├── STYLE.md              # 正文改写成 strong bullet 的规则
├── categories.json       # 主题、顺序（= 文件编号）、描述
├── state.json            # 增量 watermark：每个列表最近 30 个 id
├── data/liked|note/      # 每篇帖子一个 JSON（原文 + LLM 字段）
├── data/readable/        # 每篇帖子的 bullet 版正文
└── scripts/
    ├── x_dom.js          # 注入 x.com：滚动列表、读状态页
    ├── save_dialog.ps1   # 自动填写浏览器下载的「另存为」对话框
    ├── build.py          # 原始数据 + LLM 字段 → data/
    ├── render.py         # data/ → 0x/*.md
    └── sync_local.ps1    # 把某个 commit 的 0x/ 镜像到本地 clone
```

## 同步流程

- **现在（本地流程）**
  - Cowork 抓取并生成内容 → push 到 GitHub → 用 `sync_local.ps1` 把同一个 commit 的 `0x/` 镜像到 `D:\1AL\1a-applied-ai\0x`
  - 本地 `0x\` 是生成内容，不要手改，改动都通过 Cowork 做
  - 本地 repo 的其他部分不动；需要时我会自己 `git pull`
- **以后（云端流程）**
  - 云端抓取并生成 → push 到 GitHub（source of truth）→ 本地从 GitHub 同步
  - 从 GitHub 拿，不从 Cowork 沙箱拿：沙箱是临时的，会话结束就没了
