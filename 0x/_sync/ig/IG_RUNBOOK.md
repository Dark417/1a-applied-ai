# IG_RUNBOOK · 每天 8:00 / 18:00 收集 IG 广告里的报告 PDF

写给执行定时任务的 Claude 会话。每次都是新会话，按顺序执行。回复用户用中文。

## 0. 前提

- 仓库 `Dark417/1a-applied-ai`
  - 成品：`0x/ig/NN.<slug>.pdf`（PDF）和 `0x/ig-catalog.md`（目录：分组 index + details）
  - 流水线：`0x/_sync/ig/`
    - `ig_dom.js`：在内置浏览器里读 IG 私信里的 URL
    - `ig_fill.py`：云端填表
    - `ig_build.py`：去重、编号、渲染目录
    - `config.json`：私信对话 URL（`thread_url`）、填表身份
    - `state.json`：去重状态
    - `categories.json`：分类，按重要性排序
- 用户电脑（Windows，Claude 桌面 app）
  - IG 账号 `xlei___`，在**内置浏览器**（`mcp__remote-devices__Claude_Browser__*`）里保持登录
  - 唯一检查的地方：xlei___ 自己给自己发的私信对话（`config.json` 的 `thread_url`）
  - 原始数据放 `D:\2Alfred\x-sync\ig\raw\`
  - 本地 repo 副本：`D:\1AL\1a-applied-ai\0x\`，只用 `sync_local.ps1` 同步
- 邮箱
  - 填表用 `ig-user@xiaoxiaolei.com`
  - Squarespace 把它转发到 xiaoxiaoleijobapp@gmail.com
  - 用 Gmail connector 读（`mcp__Gmail__*`，登录的就是这个账号）
- 填表规则
  - 只填必填项，email 总是填
  - 不填电话、地址（有必填电话就记 `blocked`，跳过这篇）
  - 只勾必填的同意框，不勾营销订阅
  - cookie 横幅选拒绝 / 仅必要
- 失败处理
  - 任意一步失败，最多重试 2 次
  - 不要 push 半成品
  - 用 SendUserMessage 说明原因

## 1. 准备（云端）

```bash
cd /home/claude/1a-applied-ai && git pull -q   # 浅克隆已在任务 prompt 里做
pip list 2>/dev/null | grep -qi playwright || pip install playwright --break-system-packages
RUN=$(date -u +%Y-%m-%dT%H-%M); W=/home/claude/work/ig/$RUN; mkdir -p $W
```

## 2. 读 IG 私信（用户电脑，内置浏览器）

- **只收消息文字里的 URL**
  - 没有 URL 的消息跳过
  - 分享的帖子、reel、story 也跳过（`ig_dom.js` 已经排除了）
- 先打开对话：`Claude_Browser__navigate` 到 `config.json` 的 `thread_url`
  - 调用失败（电脑不在线）：跳过第 2、3 步，只做第 4 步（邮件），然后在汇报里说明
  - 跳到 `/accounts/login`：停下这条线，继续第 4 步；汇报和 PushNotification 里写「IG 登录失效，请在 Claude 桌面 app 的浏览器面板里重新登录 xlei___」
- 等页面加载，然后用 `javascript_tool` 执行 `ig_dom.js` 的全部内容（应返回 `ig_dom ready`）
- 再执行：`await __igdom.collect(8)`
  - 返回 `{thread, urls: [{url, text}]}`
  - 单次调用接近 45 秒会超时；超时就改成 `.then(r => window.__ig = r)`，再轮询 `window.__ig`
- 把结果写到 `$W/links.json`，执行 `python3 0x/_sync/ig/ig_build.py new $W/links.json`
  - 只留下没处理过的 URL（去掉 utm / fbclid 后按 host+path 去重），每条带 `key`

## 3. 打开链接，填表（云端 Playwright）

逐条处理新条目：

1. 执行 `python3 0x/_sync/ig/ig_fill.py "<landing>" $W/<n>`，读它输出的 JSON：
   - 先看落地页是不是报告 / 白皮书 / 电子书的领取页（看 `title` 和截图）
     - 不是（普通商品页、文章、视频）：`ig_build.py mark <key> skip --landing <url>`
     - `ig_fill.py` 只会在发现 email 表单时提交，所以不是表单的页面不会被误提交
   - `pdf`：用 Read 看 PDF 第 1–2 页，拿到标题、发布方、主题，然后走第 5 步收录
   - `email`、`submitted`：执行 `mark <key> email --landing <url> --org <公司>`，等邮件
   - `no_form` 但有 `pdf_url`：脚本已经下载好了，同 `pdf`
   - `blocked`、`error`：
     - 先看 `shot` 截图
     - 能判断的话，可以写一小段 Playwright 补上（例如多步表单、"Next" 按钮），规则不变
     - 还不行就 `mark <key> failed`，在汇报里列出原因

## 4. 读邮件（云端 Gmail connector）

1. `search_threads`：`to:ig-user@xiaoxiaolei.com newer_than:14d`
   - 也搜 `deliveredto:ig-user@xiaoxiaolei.com`，因为转发后 To 可能被改写
2. 跳过 `state.json.gmail_done` 里已有的 message id
3. 对每封新邮件用 `get_message`（`PLAIN_TEXT`）判断：
   - 是不是我们要的报告：标题或正文含 report / whitepaper / ebook / guide / download，或者发件公司在 `pending` 里
     - 是：找下载链接（`.pdf`，或者 "Download" / "Access the report" 按钮链接）。用 `ig_fill.py "<链接>" $W/mail-<id>` 打开，它会自动跟随跳转、存 PDF。有附件但拿不到时，在汇报里说明
     - 拿到 PDF 后走第 5 步，`--key` 用 pending 里对应的 key（按公司或域名对上），对不上就用 `gmail:<id>`，`--via email`
     - 营销 newsletter 或确认邮件等不相关的邮件：只记 `gmail-done <id> --note skip`
4. 每封处理完都要执行 `ig_build.py gmail-done <id>`，保证下次不重复处理
5. `ig_build.py pending` 里超过 7 天还没等到邮件的：在汇报里提一句

## 5. 收录 PDF

```bash
python3 0x/_sync/ig/ig_build.py add <pdf> --key <key> --title "<报告原标题>" --category "<分类>" \
  --org "<发布方>" --kind "<类型>" --summary "<中文 80–150 字>" --url "<落地页>" --via form|email|direct
```

- `title`：用 PDF 封面上的原标题（英文就保留英文）
- `slug` 默认由标题生成（英文小写加连字符），也可以用 `--slug` 指定，要短
- 文件名会是 `NN.<slug>.pdf`
- `category`：优先用 `categories.json` 里已有的
  - 都不合适就新建：在 `categories.json` 合适的位置（按重要性）插入 `{"name","desc"}`，再 `add`
  - 某类超过 15 份时考虑拆分：改相关 `data/NN.json` 的 `category`，再更新 `categories.json`
- `kind`：行业报告 / 白皮书 / 电子书 / 调研数据 / 技术指南 / 案例集 / 其他
- `summary`：说清楚这份报告讲什么、基于什么数据、主要结论或亮点
- 输出 `DUP of ...` 表示同一份 PDF 已经收过（按 sha256），不会重复存

## 6. 渲染、推送、本地同步

```bash
python3 0x/_sync/ig/ig_build.py render
git add 0x/ig 0x/ig-catalog.md 0x/_sync/ig
git diff --cached --quiet || { git commit -m "chore(0x): ig-sync $RUN (+N pdf, M pending)"; git pull --rebase -q; git push origin HEAD:main; }
```

- 没有任何变化（没新 PDF、没新状态）就不 commit
- 有 push 而且电脑在线：照 `0x/_sync/RUNBOOK.md` 第 7 步执行 `sync_local.ps1 -Sha <SHA>`，输出应该是 `SYNCED ...`
- 电脑离线：跳过本地同步。下次在线的运行会同步最新 commit，`sync_local` 是整体镜像

## 7. 汇报（SendUserMessage，中文）

- 新增 PDF：每条一行，格式是 `NN. 标题 · 发布方 · 分类`
- 有没有新分类
- 等邮件中的链接数；跳过 / 失败的条目和原因
- 什么都没有：一句话，比如「IG 报告：没有新链接，也没有新邮件」
- 有需要用户处理的事（IG 登录失效、电脑离线太久）时，还要发 PushNotification
