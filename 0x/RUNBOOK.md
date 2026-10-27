# RUNBOOK · 每晚同步 X 收藏

这份文档写给执行定时任务的 Claude 会话。每次运行都是一个全新会话，按顺序执行即可。

## 0. 前提

- 用户的 Windows 电脑开机，Claude 桌面 app 开着
  - 内置浏览器：`mcp__remote-devices__Claude_Browser__*`
  - Windows PowerShell：`mcp__remote-devices__Windows-MCP__PowerShell`
- 内置浏览器里 X 已登录（账号 `@whoheremains`）
- 本地文件夹：`D:\2Alfred\x-twitter`（device_bash 里是 `$HOME/mnt/x-twitter`）
- 仓库：`Dark417/1a-applied-ai`，目录 `0x/`
- 回复用户时用中文
- 任意一步失败：
  - 不要重试超过 2 次
  - 把失败原因写进最终回复后停止
  - 不要 push 半成品

## 1. 准备

1. `add_repo Dark417/1a-applied-ai`（access: push），浅克隆到 `/home/claude/1a-applied-ai`
2. 读 `0x/state.json`，拿到 `likes` 和 `bookmarks` 两个 watermark ID 列表
3. 运行 ID：`RUN=$(date -u +%Y-%m-%dT%H-%M)`

## 2. 拉列表（内置浏览器）

1. 用 `Claude_Browser__navigate` 打开 `https://x.com/i/history/likes`（完整加载）
   - 如果跳到登录页：停止，告诉用户「X 登录已失效，请在 Claude 桌面 app 的浏览器面板里重新登录」
2. 用 `javascript_tool` 粘贴执行 `0x/scripts/x_dom.js` 的全部内容（应返回 `x_dom ready`）
3. Likes：
   - 执行 `__xdom.collectList(50, <state.likes>).then(r => window.__likes = r)`
   - 每 ~40 秒查一次 `window.__likes`，直到有值（单次 tool call 超过 45 秒会超时）
4. Bookmarks：
   - 执行 `await __xdom.go('/i/history')`（SPA 跳转，脚本不会丢）
   - 然后 `__xdom.collectList(50, <state.bookmarks>).then(r => window.__bm = r)`，同样轮询
5. 两个列表都是 0 条新内容：直接跳到第 7 步，汇报「今天没有新收藏」

## 3. 补全详情

- 需要打开状态页的帖子：
  - 所有新 bookmark
  - Like 中满足任一条件的：`is_reply`、`truncated`、`!text`
- 执行 `__xdom.job('detail', [[handle, id], ...])`
- 轮询 `window.__job.done / total` 直到 `finished`

## 4. 落盘（下载 + 自动填写「另存为」）

对 `likes.json`（`__likes.items`）、`bookmarks.json`（`__bm.items`）、`details.json`（`__job.out`）**依次**执行：

1. 浏览器：`__xdom.download('<name>', <obj>)`
2. 紧接着 PowerShell：
   ```powershell
   powershell -NoProfile -ExecutionPolicy Bypass -File "D:\2Alfred\x-twitter\scripts\save_dialog.ps1" -Path "D:\2Alfred\x-twitter\raw\<RUN>\<name>"
   ```
   - 应输出 `SAVED <bytes>`
   - 如果输出 `NO_DIALOG` / `NO_EDIT`：检查有没有残留的 `blob:` 对话框，关掉后重试一次

然后用 `device_stage_files` 把三个文件拉进容器，`cp -r` 到 `/home/claude/work/raw/<RUN>/`。

## 5. LLM 加工

1. `python3 0x/scripts/build.py plan /home/claude/work/raw/<RUN> > plan.json`
   - 只列出还没处理过的帖子
2. 读 `plan.json`，写 `/home/claude/work/raw/<RUN>/enrich.json`（`{id: {...}}`）：
   - **liked**
     - `keywords`：3–5 个，英文专有名词保留原文
     - `gist`：中文；原帖短就一句，原帖长就 2–3 句
   - **note**
     - `title`：原标题够用就用原标题，不够就简短改写
     - `category`：优先用 `0x/categories.json` 里已有的分类
       - 都不合适时新建一个，同时加进 `categories.json`（附一句描述）
       - 某个分类超过 15 篇时，考虑拆分：改相关 `data/note/*.json` 的 `category`，再更新 `categories.json`
     - `kind`：概念介绍 / 搭建教程 / 方法对比 / 工具发布 / 课程推荐 / 案例分享 / 论文解读 / 观点 / 推广
     - `summary`：中文 100–200 字，说清这篇是在讲概念、讲怎么搭建，还是在比较或评价方法，再写特点和重点
   - 原文中英文都保留原样，只有总结用中文
3. `python3 0x/scripts/build.py apply /home/claude/work/raw/<RUN>`（写 `data/`，更新 `state.json`）
4. `python3 0x/scripts/render.py`
5. 自检：
   - 两份 md 里每个 `](#x-<id>)` 都有对应的 `x-<id>` 标题
   - 新增条数和第 2 步拉到的条数一致

## 6. 推送 GitHub

```bash
cd /home/claude/1a-applied-ai
git fetch origin main && git rebase origin/main
git add 0x && git commit -m "chore(0x): sync X likes/bookmarks <RUN> (+N liked, +M notes)"
git push origin HEAD:main
```

## 7. 同步本地文件夹

在 device_bash 里执行（只覆盖文件，不删除；`raw/` 保留）：

```bash
curl -sL https://codeload.github.com/Dark417/1a-applied-ai/tar.gz/main \
  | tar -xz --overwrite --strip-components=2 -C "$HOME/mnt/x-twitter" 1a-applied-ai-main/0x
```

## 8. 汇报（SendUserMessage）

- 新增 ❤️ 多少条、🔖 多少条，以及新分类（如果有）
- 列出新 note 的标题，每条一行
- 任何失败或跳过的项
