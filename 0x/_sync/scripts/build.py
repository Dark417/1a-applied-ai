#!/usr/bin/env python3
"""Merge one run's raw browser dumps + AI enrichment into data/*.json, update state.json.

Inputs (in a run dir, e.g. raw/2026-10-27T17-30/):
  likes.json      list[post]       X Likes, list order (newest like first)
  bookmarks.json  list[post]       X Bookmarks, list order
  details.json    {id: {focal, root, thread}}   status-page reads
  enrich.json     {id: {...}}      written by the LLM step (see RUNBOOK.md)
                    liked: keywords[list], gist
                    note:  title, category, kind, summary

Routing rules (from the spec):
  Like on a top-level post      -> data/liked/<id>.json   (x-new.md)
  Like on a reply               -> root post -> data/note/<rootId>.json (x-note.md)
  Bookmark                      -> data/note/<id>.json    (x-note.md); if it is a reply,
                                   the root is attached as `parent` context
  Liked AND bookmarked          -> both (two independent tasks)

Usage:
  build.py plan   <run_dir>          -> prints the items that need enrichment (JSON)
  build.py apply  <run_dir> [note]   -> writes data/*.json + state.json, appends runs.json
  build.py empty  <RUN> [note]       -> appends a "nothing new" entry to runs.json

runs.json (one entry per run, rendered into 0x/x-log.md by render.py):
  {run, liked: [new ids], notes: [new ids], seen: {likes, bookmarks}, note}
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
STATE = ROOT / "state.json"
RUNS = ROOT / "runs.json"
KEEP = ("id", "handle", "name", "url", "created_at", "text", "quote", "media", "card", "has_video", "x_article")


def rd(p: Path, default):
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else default


def slim(t: dict | None) -> dict:
    return {k: t.get(k) for k in KEEP if t and t.get(k) not in (None, "", [])} if t else {}


def best(item: dict, det: dict | None) -> dict:
    """Prefer the status-page version (untruncated, has article body)."""
    focal = (det or {}).get("focal")
    base = slim(item)
    if focal:
        base.update(slim(focal))
    return base


def route(run: Path):
    likes, bms = rd(run / "likes.json", []), rd(run / "bookmarks.json", [])
    det = rd(run / "details.json", {})
    pulled_at = run.name
    liked, notes = {}, {}
    for rank, t in enumerate(likes):
        d = det.get(t["id"]) or {}
        if t.get("is_reply") and d.get("root"):
            r = d["root"]
            notes.setdefault(r["id"], {**slim(r), "source": "liked-reply-root", "via_id": t["id"],
                                       "pulled_at": pulled_at, "rank": rank})
        else:
            liked[t["id"]] = {**best(t, d), "pulled_at": pulled_at, "rank": rank}
    for rank, t in enumerate(bms):
        d = det.get(t["id"]) or {}
        n = {**best(t, d), "source": "bookmark", "pulled_at": pulled_at, "rank": rank,
             "thread": [slim(x) for x in d.get("thread") or []]}
        if t.get("is_reply") and d.get("root"):
            n["parent"] = slim(d["root"])
        notes[t["id"]] = n  # a bookmark wins over a liked-reply root with the same id
    return liked, notes


def plan(run: Path) -> None:
    liked, notes = route(run)
    out = {
        "liked": [{"id": i, "handle": t["handle"], "text": t.get("text", "")[:1500],
                   "article_title": (t.get("x_article") or {}).get("title", ""),
                   "quote": (t.get("quote") or {}).get("text", "")[:400]} for i, t in liked.items()
                  if not (DATA / "liked" / f"{i}.json").exists()],
        "note": [{"id": i, "handle": t["handle"], "text": t.get("text", "")[:3000],
                  "thread": " / ".join(x.get("text", "") for x in t.get("thread", []))[:3000],
                  "article_title": (t.get("x_article") or {}).get("title", ""),
                  "article_body": (t.get("x_article") or {}).get("body", "")[:6000],
                  "parent": (t.get("parent") or {}).get("text", "")[:600]} for i, t in notes.items()
                 if not (DATA / "note" / f"{i}.json").exists()],
    }
    print(json.dumps(out, ensure_ascii=False, indent=1))


def record(run: str, new: dict, seen: dict, note: str = "") -> None:
    runs = [r for r in rd(RUNS, []) if r["run"] != run]
    runs.append({"run": run, "liked": new.get("liked", []), "notes": new.get("note", []),
                 "seen": seen, "note": note})
    runs.sort(key=lambda r: r["run"])
    RUNS.write_text(json.dumps(runs, ensure_ascii=False, indent=1), encoding="utf-8")


def apply(run: Path, note: str = "") -> None:
    liked, notes = route(run)
    enrich = rd(run / "enrich.json", {})
    new = {"liked": [], "note": []}
    for kind, items in (("liked", liked), ("note", notes)):
        (DATA / kind).mkdir(parents=True, exist_ok=True)
        for i, t in items.items():
            p = DATA / kind / f"{i}.json"
            if p.exists():
                continue  # already processed in an earlier run; keep its original order
            t.update(enrich.get(i, {}))
            p.write_text(json.dumps(t, ensure_ascii=False, indent=1), encoding="utf-8")
            new[kind].append(i)
    record(run.name, new, {"likes": len(rd(run / "likes.json", [])),
                           "bookmarks": len(rd(run / "bookmarks.json", []))}, note)
    # watermark: remember the top 30 ids of each list (robust to un-like / un-bookmark)
    state = rd(STATE, {})
    for key, f in (("likes", "likes.json"), ("bookmarks", "bookmarks.json")):
        ids = [t["id"] for t in rd(run / f, [])]
        state[key] = (ids + [x for x in state.get(key, []) if x not in ids])[:30]
    state["last_run"] = run.name
    STATE.write_text(json.dumps(state, indent=1), encoding="utf-8")
    print(f"liked +{len(new['liked'])} · note +{len(new['note'])} · state + runs.json updated")


if __name__ == "__main__":
    cmd, arg, note = sys.argv[1], sys.argv[2], (sys.argv[3] if len(sys.argv) > 3 else "")
    if cmd == "plan":
        plan(Path(arg))
    elif cmd == "apply":
        apply(Path(arg), note)
    elif cmd == "empty":
        record(arg, {}, {"likes": 0, "bookmarks": 0}, note or "没有新收藏")
        print("runs.json: empty run recorded")
    else:
        sys.exit(f"unknown command {cmd}")
