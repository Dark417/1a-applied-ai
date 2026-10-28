# Playwright · 本地拉取 X 收藏（不用 AI）

`scripts/x_pw.py pull` 在你自己的电脑上做 RUNBOOK 第 2–4 步（拉列表 → 打开状态页补全 → 落盘），不消耗 token。
第 5 步（中文总结、分类、可读版正文）需要 LLM，仍然由 Cowork 的夜间任务完成。

## 两种方式做的是同一件事

| | Cowork 夜间任务 | `x_pw.py pull` |
|---|---|---|
| 浏览器 | Claude 桌面 app 的内置浏览器 | Playwright 启动的本机 Chrome |
| 抓取代码 | 把 `x_dom.js` 粘贴进页面执行 | 用 `page.evaluate()` 注入同一个 `x_dom.js` |
| 落盘 | `download()` + `save_dialog.ps1` 自动点「另存为」 | Python 直接写文件 |
| 登录状态 | 内置浏览器里的 X cookie | `D:\1AL\x-tw-profile` 里的 X cookie |
| 输出 | `raw\<RUN>\{likes,bookmarks,details}.json` | `raw\<RUN>-pw\` 同样三个文件 + `meta.json` + `api\` |

## x_dom.js 的原理

- **读 DOM，不调 API**：每条帖子是一个 `article[data-testid="tweet"]`
  - `<time>` 外面的链接 `/<handle>/status/<id>` → id 和作者
  - `[data-testid="tweetText"]` → 正文（emoji 取 `<img alt>`，链接取完整 URL）
  - 引用的帖子在 `div[role="link"]` 里，单独取出，不和正文混在一起
- **SPA 跳转**：`history.pushState` + `popstate`，页面不刷新，注入的脚本一直在
- **列表**：滚动、收集，遇到 watermark（上次处理过的 id）就停
- **状态页**：focal 帖子拿全文和 X Article 正文；它上面的第一条是原帖（root）；
  往下只收**同一作者的连续回复**（thread），遇到别人的评论就停，所以不会收集评论

## 第一次使用

```powershell
cd D:\1AL\1a-applied-ai\0x\_sync\scripts
uv run --with playwright python x_pw.py login     # 弹出 Chrome，手动登录 X（含 2FA），10 分钟内
uv run --with playwright python x_pw.py check     # 检查登录状态：输出 LOGGED_IN 即可
uv run --with playwright python x_pw.py pull      # 拉新的 ❤️ / 🔖
uv run --with playwright python x_pw.py pull --all             # 全量（两个列表滚到底）
```

会弹出一个 Chrome 窗口（不能用无界面模式，见下文），可以最小化，不影响加载。

退出码：`0` 成功 · `3` 未登录（重新 `login`）· `4` X 改版了，`x_dom.js` 找不到帖子

## Playwright 怎么管理会话和登录

- **浏览器 vs 上下文（context）**
  - 一个 context 就是一套独立的 cookie / localStorage / 缓存，相当于一个无痕窗口
  - 普通 `browser.new_context()` 每次都是空的，关掉就没了 → 每次都要重新登录
- **持久化 profile（本脚本用的方式）**
  - `chromium.launch_persistent_context(r"D:\1AL\x-tw-profile", channel="chrome")`
  - 这个目录就是一个真正的 Chrome 用户目录：cookie 写在里面，下次启动还在
  - 你手动登录一次，X 下发 `auth_token`（HttpOnly，脚本读不到也不需要读）和 `ct0`（CSRF）cookie
  - 之后的 `pull` / `check` 用同一个目录启动，X 看到的就是「已登录的老浏览器」
  - 密码从不经过脚本；2FA 也是你在窗口里手动完成
- **另一种方式：storage_state**
  - `context.storage_state(path="x_state.json")` 把 cookie + localStorage 导出成 JSON
  - `browser.new_context(storage_state="x_state.json")` 再导入
  - 方便在 CI / 别的机器复用，但这个 JSON 等同于你的登录凭证，**绝不能提交到 git**
- **注意事项**
  - 同一个 profile 目录同一时间只能被一个 Chrome 进程打开（会锁目录）
  - 不要直接用你日常 Chrome 的 profile：Chrome 开着时目录是锁住的，新版 Chrome 也禁止对默认 profile 做自动化
  - 会话会过期，或者 X 让你重新验证 → `pull` 退出码 3 → 重新 `login`
  - `channel="chrome"` 用本机安装的 Chrome，不下载 Playwright 自带浏览器
  - 节奏放慢（每次滚动 1.2s、每个状态页之间 0.6s），每天跑一次，别高频刷，避免账号被风控
  - **x.com 拒绝无界面（headless）Chrome**：它的 User-Agent 里写着 `HeadlessChrome`，X 对每个页面都返回错误
    （2026-10-28 在你电脑上实测）。所以脚本默认开窗口运行；`--headless` 只用于本地模拟站点的测试
  - 窗口被遮挡或最小化也会继续加载：Playwright 启动 Chrome 时默认关掉了后台节流
    （`--disable-backgrounding-occluded-windows` 等），这是比内置浏览器面板稳的地方
  - X 的登录页 2026-10 起变成 `/i/jf/onboarding/web?mode=login`，脚本两种都认

## 每天自动跑（可选，Windows 任务计划）

```powershell
$a = New-ScheduledTaskAction -Execute "$env:LOCALAPPDATA\hermes\bin\uv.exe"   # 任务计划里 PATH 不可靠，用完整路径 -Argument "run --with playwright python x_pw.py pull" `
       -WorkingDirectory "D:\1AL\1a-applied-ai\0x\_sync\scripts"
$t = New-ScheduledTaskTrigger -Daily -At 7:30pm
Register-ScheduledTask -TaskName "x-pull" -Action $a -Trigger $t
```

因为要开窗口，任务计划里选「只在用户登录时运行」。在 Cowork 夜间任务之前跑（比如 19:30），夜间任务看到当天的 `*-pw` 目录就直接用，不再开内置浏览器。

## watermark

- `pull` 读 `../state.json` 判断「从哪里开始算新的」，但**不写它**
- 只有 `build.py apply`（AI 总结写完之后）才更新 `state.json`
- 所以 `pull` 跑几次都没关系；没被处理的帖子下次还会被拉到
- `--all` 忽略 watermark，两个列表滚到底（全量核对用）
