# 0x · X (Twitter) 收藏 → 笔记

把 X 上 ❤️ Likes 和 🔖 Bookmarks 增量拉下来，生成两份可读文档。

- [`x-new.md`](./x-new.md)：❤️ Likes
  - 上半部分：关键词 + 简述
  - 下半部分：原帖全文
- [`x-note.md`](./x-note.md)：🔖 Bookmarks，加上 ❤️ 过的评论所对应的原帖
  - 上半部分：Index，按分类分组，组内最新在上
  - 下半部分：总结 + 原文

## 规则

- 同一条帖子既 ❤️ 又 🔖：两份文档各算一次，是独立的两个任务
- ❤️ 的是一条评论：取它的原帖（conversation root），放进 `x-note.md`
- 🔖 的是作者自己的连续 thread：整个 thread 一起拉
- 排序：按你点 ❤️ / 🔖 的顺序，最新在上
  - X 不提供点击时间，所以用「拉取批次 + 列表位置」来排
- 增量：`state.json` 记录每个列表最近 30 个 ID，下次拉到其中任意一个就停

## 目录

```
0x/
├── x-new.md, x-note.md     # 生成的文档（不要手改）
├── categories.json         # x-note 的分类和顺序（由 LLM 维护）
├── state.json              # watermark
├── data/liked/<id>.json    # 每条 Like：原文 + keywords + gist
├── data/note/<id>.json     # 每条 Note：原文 + title + category + kind + summary
├── RUNBOOK.md              # 每次运行的步骤（给定时任务读）
└── scripts/
    ├── x_dom.js            # 注入 x.com 页面：滚动列表、读状态页
    ├── save_dialog.ps1     # 自动填写浏览器下载的「另存为」对话框
    ├── build.py            # raw 数据 + LLM 结果 → data/*.json + state.json
    └── render.py           # data/*.json → 两份 .md
```

## 设计取舍

- **数据和展示分开**
  - LLM 只产出字段（summary、category…），`render.py` 负责排版
  - 重新分组 = 改 `category` 字段再 render，不用重写整份文档
- **为什么读 DOM，不拦截 GraphQL**
  - X 在页面启动时就保存了 `fetch` / `XHR` 的引用，加载后再挂 hook 拦不到请求
  - MVP1 改用 Playwright 后，可以用 `page.on('response')` 拿完整 JSON
- **为什么经过下载对话框**
  - 浏览器面板里的数据要落到磁盘，又不能整段经过 LLM 复述（每次几百 KB）
  - 所以页面触发下载，`save_dialog.ps1` 直接把文件名框填成目标路径
