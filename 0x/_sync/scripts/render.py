#!/usr/bin/env python3
"""Render the reading views from data/. Stdlib only.

Layout: pipeline lives in 0x/_sync/ (this script, data/, categories.json); the reading
views are written one level up, straight into 0x/:
  x-new.md              ❤️ Likes: Part 1 keywords, Part 2 content
  x-note.md             🔖 Notes master index only: topic → NN-<slug>.md, title → NN-<slug>.md#x-<id>
  NN-<slug>.md          one file per topic, NN = importance order in categories.json

Content source per post
  data/readable/<id>.md  bulleted readable version (LLM-written, see RUNBOOK §5)
  raw text               kept verbatim inside a collapsed <details> block

Dedup
  - one data file per post id → a post never appears twice in the same view, across runs
  - a post that is both liked and noted: x-new.md keeps its keywords but links to the
    note instead of repeating the full content

Ordering = the order you liked/saved it, newest first
  (pulled_at desc, then rank = position in X's list asc)

Anchors: detail headings are `### x-<id>`, valid anchors on both GitHub and Obsidian.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent   # 0x/_sync
DATA = ROOT / "data"
OUT = ROOT.parent                                # 0x
TOPIC_FILE = re.compile(r"^\d{2}-[\w-]+\.md$")


def load(kind: str) -> list[dict]:
    items = [json.loads(p.read_text(encoding="utf-8")) for p in sorted((DATA / kind).glob("*.json"))]
    items.sort(key=lambda t: (t.get("pulled_at", ""), -t.get("rank", 0)), reverse=True)
    return items


def load_categories() -> dict[str, dict]:
    p = ROOT / "categories.json"
    raw = json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}
    out = {}
    for name, v in raw.items():
        v = v if isinstance(v, dict) else {"desc": v}
        v.setdefault("slug", "".join(c if c.isascii() and c.isalnum() else "-" for c in name.lower()).strip("-") or "misc")
        out[name] = v
    return out


def day(iso: str | None) -> str:
    return (iso or "")[:10]


def quote_block(text: str, indent: str = "") -> list[str]:
    if not text:
        return [indent + "> _(无正文)_"]
    return [indent + ("> " + line if line.strip() else ">") for line in text.splitlines()]


def raw_text(t: dict) -> str:
    parts = []
    if t.get("text"):
        parts.append(t["text"])
    for i, th in enumerate(t.get("thread") or [], 2):
        if th.get("text"):
            parts.append(f"[{i}] {th['text']}")
    art = t.get("x_article") or {}
    if art.get("title"):
        parts.append(f"《{art['title']}》")
    if art.get("body"):
        parts.append(art["body"])
    return "\n\n".join(parts)


def readable(t: dict) -> str | None:
    p = DATA / "readable" / f"{t['id']}.md"
    return p.read_text(encoding="utf-8").strip() if p.exists() else None


def body(t: dict) -> list[str]:
    """Readable bullets + collapsed original. Falls back to the quote if no readable yet."""
    r = readable(t)
    raw = raw_text(t)
    if not r:
        return quote_block(raw)
    out = [r, ""]
    if raw and len(raw) > 280:  # short posts: the bullets already carry everything
        out += ["<details><summary>原文</summary>", "", *quote_block(raw), "", "</details>"]
    return out


def extras(t: dict) -> list[str]:
    out = []
    par = t.get("parent")
    if par and par.get("text"):
        out.append(f"- 上文（作者原帖 @{par.get('handle', '')}）：")
        out += quote_block(par["text"], "  ")
    q = t.get("quote")
    if q and q.get("text") and not readable(t):
        out.append(f"- 引用 {q.get('name', '')}:")
        out += quote_block(q["text"], "  ")
    c = t.get("card")
    if c and c.get("href"):
        label = (c.get("text") or "").splitlines()[0][:80] if c.get("text") else c["href"]
        out.append(f"- 链接卡片：[{label}]({c['href']})")
    if t.get("media"):
        out.append("- 图片：" + " ".join(f"[img{i}]({m})" for i, m in enumerate(t["media"], 1)))
    if t.get("has_video"):
        out.append("- 含视频（未转写）")
    return out


def author(t: dict) -> str:
    return f"{t.get('name') or t['handle']} (@{t['handle']})"


def group_notes(notes: list[dict], cats: dict[str, dict]):
    groups: dict[str, list[dict]] = {}
    for t in notes:
        groups.setdefault(t.get("category") or "其他", []).append(t)
    order = list(cats)
    names = sorted(groups, key=lambda c: (order.index(c) if c in order else len(order), c))
    for c in names:
        cats.setdefault(c, {"slug": "".join(ch if ch.isascii() and ch.isalnum() else "-" for ch in c.lower()).strip("-") or "misc", "desc": ""})
    return names, groups


# ---------------------------------------------------------------- NN-<slug>.md
def render_topic(name: str, items: list[dict], meta: dict) -> str:
    L = [
        f"# {name}",
        "",
        f"- [← 返回总目录](x-note.md)",
        f"- {meta.get('desc', '')}" if meta.get("desc") else "",
        f"- 共 {len(items)} 篇，按收藏顺序倒序（最新在上）",
        "",
        "## Part 1 · Index",
        "",
    ]
    for t in items:
        L.append(f"- [{t.get('title') or t['id']}](#x-{t['id']}) · @{t['handle']} · {day(t['created_at'])} · {t.get('kind', '')}")
    L += ["", "## Part 2 · Details", ""]
    for t in items:
        src = "🔖 收藏" if t.get("source") == "bookmark" else f"❤️ 点赞的评论 → 原帖（via [{t.get('via_id')}](https://x.com/i/status/{t.get('via_id')})）"
        L += [
            f"### x-{t['id']}",
            "",
            f"**{t.get('title') or ''}**",
            "",
            f"- 作者：{author(t)} · 发帖 {day(t['created_at'])} · [原帖]({t['url']})",
            f"- 来源：{src} · 拉取 {day(t.get('pulled_at'))} · 类型：{t.get('kind', '')}",
            f"- **总结**：{t.get('summary', '')}",
            "",
            "**正文**",
            "",
            *body(t),
            "",
            *extras(t),
            "",
            "[↑ 回到本页目录](#part-1--index)",
            "",
        ]
    return "\n".join(l for l in L if l is not None).rstrip() + "\n"


# ---------------------------------------------------------------- x-note.md
def render_note_index(names, groups, cats) -> str:
    total = sum(len(v) for v in groups.values())
    L = [
        "# X Notes · 精读总目录",
        "",
        f"- 共 {total} 篇，{len(names)} 个主题；每个主题一个文件，主题内按收藏顺序倒序",
        "- 点主题名 → 打开主题文件；点标题 → 直接跳到那篇的详情",
        "- 自动生成，勿手改",
        "",
    ]
    for c in names:
        fname, desc = cats[c]["file"], cats[c].get("desc", "")
        L.append(f"- **[{fname[:2]} · {c}]({fname})**（{len(groups[c])}）" + (f" — {desc}" if desc else ""))
        for t in groups[c]:
            L.append(f"  - [{t.get('title') or t['id']}]({fname}#x-{t['id']}) · @{t['handle']} · {day(t['created_at'])}")
    return "\n".join(L).rstrip() + "\n"


# ---------------------------------------------------------------- x-new.md
def render_new(items: list[dict], note_loc: dict[str, tuple[str, str]]) -> str:
    L = [
        "# X Likes · 关键词速览",
        "",
        f"- 共 {len(items)} 条，按点赞顺序倒序（最新在上）",
        "- Part 1：关键词 + 简述；Part 2：正文（同时在 Notes 里的帖子只给链接，不重复全文）",
        "- 自动生成，勿手改",
        "",
        "## Part 1 · Keywords",
        "",
    ]
    for t in items:
        kw = ", ".join(f"`{k}`" for k in t.get("keywords", []))
        mark = " 🔖" if t["id"] in note_loc else ""
        L.append(f"- [{day(t['created_at'])} · @{t['handle']}](#x-{t['id']}){mark}：{kw}")
        if t.get("gist"):
            L.append(f"  - {t['gist']}")
    L += ["", "## Part 2 · 正文", ""]
    for t in items:
        L += [f"### x-{t['id']}", "", f"**{author(t)}** · 发帖 {day(t['created_at'])} · [原帖]({t['url']})", ""]
        if t["id"] in note_loc:
            fname, title = note_loc[t["id"]]
            L += [f"- 🔖 也在 Notes 里，全文见：[{title}]({fname}#x-{t['id']})", ""]
        else:
            L += [*body(t), "", *extras(t), ""]
        L += ["[↑ 回到目录](#part-1--keywords)", ""]
    return "\n".join(L).rstrip() + "\n"


def main() -> int:
    cats = load_categories()
    liked, notes = load("liked"), load("note")
    names, groups = group_notes(notes, cats)
    order = list(cats)  # importance order = key order in categories.json
    for c in names:
        cats[c]["file"] = f"{order.index(c) + 1:02d}-{cats[c]['slug']}.md"
    wanted = set()
    note_loc = {}
    for c in names:
        fname = cats[c]["file"]
        wanted.add(fname)
        (OUT / fname).write_text(render_topic(c, groups[c], cats[c]), encoding="utf-8")
        for t in groups[c]:
            note_loc[t["id"]] = (fname, t.get("title") or t["id"])
    for stale in OUT.glob("*.md"):  # topic renamed/reordered → drop its old file
        if TOPIC_FILE.match(stale.name) and stale.name not in wanted:
            stale.unlink()
    (OUT / "x-note.md").write_text(render_note_index(names, groups, cats), encoding="utf-8")
    (OUT / "x-new.md").write_text(render_new(liked, note_loc), encoding="utf-8")
    missing = [t["id"] for t in liked + notes if not readable(t)]
    print(f"x-new.md: {len(liked)} · notes: {len(notes)} in {len(names)} topic files · readable missing: {len(set(missing))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
