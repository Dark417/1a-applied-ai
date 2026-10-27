#!/usr/bin/env python3
"""Render x-new.md (Likes) and x-note.md (Bookmarks + roots of liked replies)
from the per-post JSON files in data/. Stdlib only.

Ordering = "the order you liked/saved it", newest first:
  sort by pulled_at desc (run time), then rank asc (position in X's list).

Anchors: every detail heading is `### x-<tweetId>`. That exact text is a valid
anchor on both GitHub (slug) and Obsidian (heading link), so index links
`[title](#x-<id>)` jump in both.
"""
from __future__ import annotations

import json
import sys
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"


def load(kind: str) -> list[dict]:
    items = [json.loads(p.read_text(encoding="utf-8")) for p in sorted((DATA / kind).glob("*.json"))]
    items.sort(key=lambda t: (t.get("pulled_at", ""), -t.get("rank", 0)), reverse=True)
    return items


def day(iso: str | None) -> str:
    return (iso or "")[:10]


def quote_block(text: str) -> list[str]:
    if not text:
        return ["> _(无正文)_"]
    return ["> " + line if line.strip() else ">" for line in text.splitlines()]


def full_text(t: dict) -> str:
    """Post text + self-thread + X Article body."""
    parts = []
    if t.get("text"):
        parts.append(t["text"])
    for i, th in enumerate(t.get("thread") or [], 2):
        if th.get("text"):
            parts.append(f"[{i}] {th['text']}")
    art = t.get("x_article")
    if art:
        if art.get("title"):
            parts.append(f"《{art['title']}》")
        if art.get("body"):
            parts.append(art["body"])
    return "\n\n".join(parts)


def extras(t: dict) -> list[str]:
    out = []
    par = t.get("parent")
    if par and par.get("text"):
        out.append(f"- 上文（作者原帖 @{par.get('handle', '')}）：")
        out += ["  " + l for l in quote_block(par["text"])]
    q = t.get("quote")
    if q and q.get("text"):
        out.append(f"- 引用 {q.get('name', '')}:")
        out += ["  " + l for l in quote_block(q["text"])]
    c = t.get("card")
    if c and c.get("href"):
        out.append(f"- 链接卡片：[{c.get('text', '').splitlines()[0][:80] or c['href']}]({c['href']})")
    if t.get("media"):
        out.append("- 图片：" + " ".join(f"[img{i}]({m})" for i, m in enumerate(t["media"], 1)))
    if t.get("has_video"):
        out.append("- 含视频（未转写）")
    return out


def author(t: dict) -> str:
    return f"{t.get('name') or t['handle']} (@{t['handle']})"


# ---------------------------------------------------------------- x-new.md
def render_new(items: list[dict]) -> str:
    L = [
        "# X Likes · 关键词速览",
        "",
        f"- 共 {len(items)} 条，按点赞顺序倒序（最新在上）",
        "- 上半部分：关键词 + 简述；下半部分：原帖全文",
        "- 自动生成，勿手改：改 `data/liked/*.json` 后跑 `scripts/render.py`",
        "",
        "## Part 1 · Keywords",
        "",
    ]
    for t in items:
        kw = ", ".join(f"`{k}`" for k in t.get("keywords", []))
        L.append(f"- [{day(t['created_at'])} · @{t['handle']}](#x-{t['id']})：{kw}")
        if t.get("gist"):
            L.append(f"  - {t['gist']}")
    L += ["", "## Part 2 · 原帖", ""]
    for t in items:
        L += [
            f"### x-{t['id']}",
            "",
            f"**{author(t)}** · 发帖 {day(t['created_at'])} · [原帖]({t['url']})",
            "",
            *quote_block(full_text(t)),
            "",
            *extras(t),
            "",
        ]
    return "\n".join(L).rstrip() + "\n"


# ---------------------------------------------------------------- x-note.md
def render_note(items: list[dict], categories: dict) -> str:
    groups: "OrderedDict[str, list[dict]]" = OrderedDict()
    order = list(categories.keys())
    for t in items:
        groups.setdefault(t.get("category") or "Uncategorized", []).append(t)
    names = sorted(groups, key=lambda c: (order.index(c) if c in order else len(order), c))

    L = [
        "# X Notes · 精读",
        "",
        f"- 共 {len(items)} 篇，{len(names)} 个分类；组内按收藏顺序倒序（最新在上）",
        "- 上半部分：Index（点击跳到详情）；下半部分：总结 + 原文",
        "- 自动生成，勿手改：改 `data/note/*.json` 或 `categories.json` 后跑 `scripts/render.py`",
        "",
        "## Part 1 · Index",
        "",
    ]
    for c in names:
        desc = categories.get(c, "")
        L.append(f"- **{c}**（{len(groups[c])}）" + (f" — {desc}" if desc else ""))
        for t in groups[c]:
            L.append(f"  - [{t.get('title') or t['id']}](#x-{t['id']}) · @{t['handle']} · {day(t['created_at'])}")
    L += ["", "## Part 2 · Details", ""]
    for c in names:
        L += [f"### 📂 {c}", ""]
        for t in groups[c]:
            src = "🔖 收藏" if t.get("source") == "bookmark" else f"❤️ 点赞的评论 → 原帖（via [{t.get('via_id')}](https://x.com/i/status/{t.get('via_id')})）"
            L += [
                f"#### x-{t['id']}",
                "",
                f"**{t.get('title') or ''}**",
                "",
                f"- 作者：{author(t)} · 发帖 {day(t['created_at'])} · [原帖]({t['url']})",
                f"- 来源：{src} · 拉取 {day(t.get('pulled_at'))}",
                f"- 类型：{t.get('kind', '')}",
                f"- **总结**：{t.get('summary', '')}",
                "- **原文**：",
                "",
                *quote_block(full_text(t)),
                "",
                *extras(t),
                "",
            ]
    return "\n".join(L).rstrip() + "\n"


def main() -> int:
    cats_path = ROOT / "categories.json"
    categories = json.loads(cats_path.read_text(encoding="utf-8")) if cats_path.exists() else {}
    liked, notes = load("liked"), load("note")
    (ROOT / "x-new.md").write_text(render_new(liked), encoding="utf-8")
    (ROOT / "x-note.md").write_text(render_note(notes, categories), encoding="utf-8")
    print(f"x-new.md: {len(liked)} · x-note.md: {len(notes)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
