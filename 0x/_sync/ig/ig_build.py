#!/usr/bin/env python3
"""ig_build.py — bookkeeping for the IG report pipeline (cloud side, no network).

  python3 ig_build.py new <links.json>                    # print URLs not yet in state (dedup by url_key)
  python3 ig_build.py key <url>                           # the dedup key for a URL (use as --key)
  python3 ig_build.py mark <key> <status> [--landing U] [--org O]   # remember a link (seen / pending email)
  python3 ig_build.py add <pdf> --key K --title T --category C --org O --kind K --summary S [--url U] [--slug s]
        # dedup by sha256 → copy to 0x/ig/NN.<slug>.pdf, write data/NN.json, clear pending
  python3 ig_build.py gmail-done <message_id> [--note ...]  # an email we have handled (any outcome)
  python3 ig_build.py pending                             # links still waiting for an email
  python3 ig_build.py render                              # 0x/ig-catalog.md
State: state.json (seen keys, link log, pending, gmail ids, pdf hashes, next number).
Categories: categories.json (ordered by importance); unknown category in `add` is an error —
add it to categories.json first (name + one-line description).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT0X = HERE.parent.parent
PDF_DIR = ROOT0X / "ig"
DATA = HERE / "data"
STATE = HERE / "state.json"
CATS = HERE / "categories.json"
CATALOG = ROOT0X / "ig-catalog.md"


def load(p, d):
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return d


def save(p, obj):
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def st():
    s = load(STATE, {})
    for k, v in {"seen": [], "links": {}, "pending": {}, "gmail_done": {}, "pdf_sha": {}, "next_no": 1}.items():
        s.setdefault(k, v)
    if isinstance(s["gmail_done"], list):
        s["gmail_done"] = {m: "" for m in s["gmail_done"]}
    return s


def now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")


def slugify(t):
    s = re.sub(r"[^A-Za-z0-9]+", "-", t).strip("-").lower()
    return (s[:60].rstrip("-")) or "report"


TRACKING = re.compile(r"^(utm_|fbclid|igshid|igsh|gclid|mc_|_hs|hsa_|li_fat_id)", re.I)


def url_key(u):
    """dedup key: host + path + non-tracking query (ad links differ only by utm_* / fbclid)."""
    from urllib.parse import parse_qsl, urlencode, urlparse
    p = urlparse(u.strip())
    q = urlencode(sorted((k, v) for k, v in parse_qsl(p.query) if not TRACKING.match(k)))
    return f"url:{p.netloc.lower().removeprefix('www.')}{p.path.rstrip('/')}" + (f"?{q}" if q else "")


def cmd_new(a):
    s = st()
    obj = json.loads(Path(a.links).read_text(encoding="utf-8"))
    items = obj.get("items") or [{"key": url_key(u["url"]), "landing": u["url"], "text": u.get("text", "")}
                                 for u in obj.get("urls", [])]
    seen, fresh = set(s["seen"]), {}
    for i in items:
        if i["key"] not in seen:
            fresh.setdefault(i["key"], i)
    fresh = list(fresh.values())
    print(json.dumps(fresh, ensure_ascii=False, indent=1))


def cmd_mark(a):
    s = st()
    if a.key not in s["seen"]:
        s["seen"].append(a.key)
    s["links"][a.key] = {"status": a.status, "landing": a.landing, "org": a.org, "at": now()}
    if a.status == "email":
        s["pending"][a.key] = {"landing": a.landing, "org": a.org, "since": now()}
    save(STATE, s)
    print(f"marked {a.key} {a.status}")


def cmd_add(a):
    s = st()
    cats = [c["name"] for c in load(CATS, [])]
    if a.category not in cats:
        sys.exit(f"UNKNOWN_CATEGORY {a.category!r}: add it to categories.json first")
    b = Path(a.pdf).read_bytes()
    if b[:4] != b"%PDF":
        sys.exit("NOT_A_PDF")
    h = hashlib.sha256(b).hexdigest()
    if h in s["pdf_sha"]:
        print(f"DUP of {s['pdf_sha'][h]}")
        if a.key and a.key not in s["seen"]:
            s["seen"].append(a.key)
        s["pending"].pop(a.key, None)
        save(STATE, s)
        return
    no = s["next_no"]
    fname = f"{no:02d}.{a.slug or slugify(a.title)}.pdf"
    PDF_DIR.mkdir(exist_ok=True)
    shutil.copyfile(a.pdf, PDF_DIR / fname)
    DATA.mkdir(exist_ok=True)
    rec = {"no": no, "file": fname, "title": a.title, "category": a.category, "org": a.org, "kind": a.kind,
           "summary": a.summary, "url": a.url, "key": a.key, "via": a.via, "added": now(),
           "bytes": len(b), "sha256": h}
    save(DATA / f"{no:02d}.json", rec)
    s["pdf_sha"][h] = fname
    s["next_no"] = no + 1
    if a.key:
        if a.key not in s["seen"]:
            s["seen"].append(a.key)
        s["links"].setdefault(a.key, {})["status"] = "pdf"
        s["pending"].pop(a.key, None)
    save(STATE, s)
    print(f"ADDED {fname}")


def cmd_gmail_done(a):
    s = st()
    s["gmail_done"][a.message_id] = a.note or now()
    save(STATE, s)
    print("ok")


def cmd_pending(_a):
    print(json.dumps(st()["pending"], ensure_ascii=False, indent=1))


def cmd_render(_a):
    cats = load(CATS, [])
    recs = sorted((json.loads(p.read_text(encoding="utf-8")) for p in DATA.glob("*.json")), key=lambda r: -r["no"])
    by = {c["name"]: [] for c in cats}
    for r in recs:
        by.setdefault(r["category"], []).append(r)
    s = st()
    L = ["# IG Reports · 目录", "",
         f"- 共 {len(recs)} 份 PDF，{sum(1 for v in by.values() if v)} 个分类；文件在 [`ig/`](ig/)，编号越大越新",
         f"- 等邮件中：{len(s['pending'])} 个链接",
         "- 点标题 → 跳到详情；点文件名 → 打开 PDF",
         "- 自动生成，勿手改", "", "## Part 1 · Index", ""]
    for i, c in enumerate(cats, 1):
        rs = by.get(c["name"], [])
        if not rs:
            continue
        L.append(f"- **{i:02d} · {c['name']}**（{len(rs)}） — {c.get('desc', '')}")
        for r in rs:
            L.append(f"  - [{r['title']}](#ig-{r['no']:02d}) · {r['org']} · `{r['file']}`")
    L += ["", "## Part 2 · Details", ""]
    for r in recs:
        L += [f"### ig-{r['no']:02d}", "", f"**{r['title']}**", "",
              f"- 文件：[{r['file']}](ig/{r['file']}) · {r['bytes'] // 1024} KB",
              f"- 发布方：{r['org']} · 分类：{r['category']} · 类型：{r['kind']}",
              f"- 来源：{'IG 私信链接' if r['key'].startswith('url:') else 'Gmail'} · 获取方式：{r['via']} · 收录 {r['added'][:10]}"
              + (f" · [落地页]({r['url']})" if r.get("url") else ""),
              f"- **总结**：{r['summary']}", ""]
    CATALOG.write_text("\n".join(L).rstrip() + "\n", encoding="utf-8")
    print(f"ig-catalog.md: {len(recs)} pdfs, pending {len(s['pending'])}")


def main():
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    x = sp.add_parser("new"); x.add_argument("links")
    x = sp.add_parser("mark"); x.add_argument("key"); x.add_argument("status")
    x.add_argument("--landing", default=""); x.add_argument("--org", default="")
    x = sp.add_parser("add"); x.add_argument("pdf")
    for f in ("key", "title", "category", "org", "kind", "summary"):
        x.add_argument(f"--{f}", required=f != "key", default="")
    x.add_argument("--url", default=""); x.add_argument("--slug", default=""); x.add_argument("--via", default="form")
    x = sp.add_parser("key"); x.add_argument("url")
    x = sp.add_parser("gmail-done"); x.add_argument("message_id"); x.add_argument("--note", default="")
    sp.add_parser("pending"); sp.add_parser("render")
    a = ap.parse_args()
    {"new": cmd_new, "key": lambda a: print(url_key(a.url)), "mark": cmd_mark, "add": cmd_add, "gmail-done": cmd_gmail_done,
     "pending": cmd_pending, "render": cmd_render}[a.cmd](a)


if __name__ == "__main__":
    main()
