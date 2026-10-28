# RUNBOOK · 每晚同步 X 收藏

这份文档写给执行定时任务的 Claude 会话。每次运行都是一个全新会话，按顺序执行即可。

## 0. 前提

- 用户的 Windows 电脑开机，Claude 桌面 app 开着
  - 内置浏览器：`mcp__remote-devices__Claude_Browser__*`
  - Windows PowerShell：`mcp__remote-devices__Windows-MCP__PowerShell`
- 内置浏览器里 X 已登录（账号 `@whoheremains`）
- 仓库：`Dark417/1a-applied-ai`，目录 `0x/`
  - `0x/` 下只放阅读内容：`NN-<主题>.md`、`x-new.md`、`x-note.md`、`x-log.md`、`README.md`
  - 流水线（脚本、数据、本文件、`PLAYWRIGHT.md`）放在 `0x/_sync/`
- 本地 repo clone：`D:\1AL\1a-applied-ai`；它的 `0x\` 是用户看的本地副本
  - 只用 `sync_local.ps1` 同步 `0x\`，**不要对这个 repo 做 git pull**（用户要求时才 pull）
- 原始抓取数据：`D:\2Alfred\x-twitter\raw\`（device_bash 里是 `$HOME/mnt/x-twitter/raw`；不进 git）
- 回复用户时用中文
- 任意一步失败：
  - 不要重试超过 2 次
  - 把失败原因写进最终回复后停止
  - 不要 push 半成品

## 1. 准备

1. `add_repo Dark417/1a-applied-ai`（access: push），浅克隆到 `/home/claude/1a-applied-ai`
2. 读 `0x/_sync/state.json`，拿到 `likes` 和 `bookmarks` 两个 watermark ID 列表
3. 运行 ID：`RUN=$(date -u +%Y-%m-%dT%H-%M)`

## 2. 拉列表（内置浏览器）

0. 先看本地 Playwright 有没有已经拉好今天的数据（见 `PLAYWRIGHT.md`）：
   - PowerShell：`Get-ChildItem D:\2Alfred\x-twitter\raw -Directory -Filter *-pw | Sort Name -Desc | Select -First 1`，再读它的 `meta.json`
   - 如果是今天（美西时间）的，并且 `meta.json` 存在：直接 stage 它的三个 json 到 `/home/claude/work/raw/<那个目录名>/`，用目录名当 `<RUN>`，跳到第 5 步
   - 否则照常用内置浏览器走第 2–4 步

1. 用 `Claude_Browser__navigate` 打开 `https://x.com/i/history/likes`（完整加载）
   - 如果跳到登录页：停止，告诉用户「X 登录已失效，请在 Claude 桌面 app 的浏览器面板里重新登录」
2. 用 `javascript_tool` 粘贴执行 `0x/_sync/scripts/x_dom.js` 的全部内容（应返回 `x_dom ready`）
3. Likes：
   - 执行 `__xdom.collectList(50, <state.likes>).then(r => window.__likes = r)`
   - 每 ~40 秒查一次 `window.__likes`，直到有值（单次 tool call 超过 45 秒会超时）
4. Bookmarks：
   - 执行 `await __xdom.go('/i/history')`（SPA 跳转，脚本不会丢）
   - 然后 `__xdom.collectList(50, <state.bookmarks>).then(r => window.__bm = r)`，同样轮询
5. 两个列表都是 0 条新内容：
   - `python3 0x/_sync/scripts/build.py empty <RUN>` 记一条空批次，再 `python3 0x/_sync/scripts/render.py`
   - 做第 6、7 步（只推 `runs.json` 和 `x-log.md`），然后第 8 步汇报「今天没有新收藏」
6. 定期全量核对（每周日，或者用户要求时）：`collectList(3000, [])` 不带 watermark 把两个列表滚到底，
   和 `data/liked`、`data/note` 对比，漏掉的帖子一起走第 3–5 步（`build.py plan` 只会列出没处理过的）

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
   powershell -NoProfile -ExecutionPolicy Bypass -File "D:\1AL\1a-applied-ai\0x\_sync\scripts\save_dialog.ps1" -Path "D:\2Alfred\x-twitter\raw\<RUN>\<name>"
   ```
   - 应输出 `SAVED <bytes>`
   - 如果输出 `NO_DIALOG` / `NO_EDIT`：检查有没有残留的 `blob:` 对话框，关掉后重试一次

然后用 `device_stage_files` 把三个文件拉进容器，`cp -r` 到 `/home/claude/work/raw/<RUN>/`。

## 5. LLM 加工

1. `python3 0x/_sync/scripts/build.py plan /home/claude/work/raw/<RUN> > plan.json`
   - 只列出还没处理过的帖子
2. 读 `plan.json`，写 `/home/claude/work/raw/<RUN>/enrich.json`（`{id: {...}}`）：
   - **liked**
     - `keywords`：3–5 个，英文专有名词保留原文
     - `gist`：中文；原帖短就一句，原帖长就 2–3 句
   - **note**
     - `title`：原标题够用就用原标题，不够就简短改写
     - `category`：优先用 `0x/_sync/categories.json` 里已有的分类
       - 都不合适时新建一个，同时加进 `categories.json`（附一句描述）
       - 某个分类超过 15 篇时，考虑拆分：改相关 `_sync/data/note/*.json` 的 `category`，再更新 `categories.json`
     - `kind`：概念介绍 / 搭建教程 / 方法对比 / 工具发布 / 课程推荐 / 案例分享 / 论文解读 / 观点 / 推广
     - `summary`：中文 100–200 字，说清这篇是在讲概念、讲怎么搭建，还是在比较或评价方法，再写特点和重点
   - 原文中英文都保留原样，只有总结用中文
3. `python3 0x/_sync/scripts/build.py apply /home/claude/work/raw/<RUN> [备注]`（写 `data/`，更新 `state.json`，在 `runs.json` 追加本批次）
4. **可读版正文**：每篇新帖子（liked 和 note 去重后按 id 算）都要按 `0x/_sync/STYLE.md` 写一份 `0x/_sync/data/readable/<id>.md`
   - 使用 strong bullet style，保留原语言；不是摘要，是重新排版
   - 已经存在的不要重写
   - 新的长文超过 3 篇时，按篇拆给并行 subagent，每个 subagent 都先读 `STYLE.md`
5. `python3 0x/_sync/scripts/render.py`
   - 输出到 `0x/`：`x-new.md`、`x-note.md`（只有总目录）、`NN-<slug>.md`（每个主题一个文件）、`x-log.md`（每日日志）
     - `NN` 是 `categories.json` 里的重要性顺序；新分类要按重要性插到合适的位置
   - 结尾打印的 `readable missing` 应该是 0
6. 自检：
   - `x-new.md` 和每个 `NN-*.md` 里的每个 `](#x-<id>)` 都有对应的 `### x-<id>` 标题
   - `x-note.md` 里的每个 `NN-<slug>.md#x-<id>` 都能在对应文件里找到
   - 新增条数和第 2 步拉到的条数一致
   - `x-log.md` 顶部是今天的日期，本批次的条数正确

## 6. 推送 GitHub

```bash
cd /home/claude/1a-applied-ai
git fetch origin main && git rebase origin/main
git add 0x && git commit -m "chore(0x): sync X likes/bookmarks <RUN> (+N liked, +M notes)"
git push origin HEAD:main
```

## 7. 同步本地文件夹（尽力而为）

- 用户电脑在线时才做这一步；离线就跳过，不算失败（用户之后自己从 GitHub pull）
- 先在容器里取 `SHA=$(git rev-parse HEAD)`，也就是第 6 步 push 后的那个 commit
- 再用 Windows PowerShell 执行：

```powershell
# 把那个 commit 的 0x/ 镜像到本地 repo 的 0x\（会删掉已改名的旧主题文件）
# 用固定的 SHA，不用 main：codeload 上 main 的压缩包有缓存
$s = "$env:TEMP\sync_local.ps1"
Invoke-WebRequest -UseBasicParsing "https://raw.githubusercontent.com/Dark417/1a-applied-ai/<SHA>/0x/_sync/scripts/sync_local.ps1" -OutFile $s
powershell -NoProfile -ExecutionPolicy Bypass -File $s -Sha <SHA>
```

- 输出应该是 `SYNCED <sha7> -> D:\1AL\1a-applied-ai\0x`

## 8. 汇报（SendUserMessage）

- 新增 ❤️ 多少条、🔖 多少条，以及新分类（如果有）
- 列出新 note 的标题，每条一行
- 任何失败或跳过的项
