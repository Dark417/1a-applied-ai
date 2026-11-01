#!/usr/bin/env python3
"""ig_pw.py — local Playwright for the IG report pipeline (no AI, no tokens).

Runs on the Windows PC (the IG session lives in a local Chrome profile):
  uv run --with playwright python ig_pw.py login            # one-time: log in to IG by hand (10 min)
  uv run --with playwright python ig_pw.py check            # LOGGED_IN / NOT_LOGGED_IN
  uv run --with playwright python ig_pw.py threads          # list DM threads (title + id)
  uv run --with playwright python ig_pw.py links            # new links from the configured thread

`links` reads the DM thread set in config.json ("thread_id"), collects every shared post /
reel / external link, opens each NEW shared post to find its ad CTA (the "Learn more" link,
l.instagram.com/?u=<landing>) and prints one JSON object to stdout:
  {"run": ..., "items": [{"key", "src", "landing", "text", "ts"}], "out": "<path>"}
It also writes the same JSON to D:\\2Alfred\\x-sync\\ig\\raw\\<RUN>\\links.json.
Dedup: keys already in state.json ("seen") are skipped; state.json is written only by the
cloud run (ig_build.py), so running `links` twice is harmless.
Profile (cookies) lives OUTSIDE the repo: D:\\1AL\\ig-profile (never commit it).
Exit codes: 0 ok · 3 not logged in · 5 no thread configured
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlparse

from playwright.sync_api import sync_playwright

PROFILE = Path(r"D:\1AL\ig-profile")
OUT = Path(r"D:\2Alfred\x-sync\ig\raw")
HERE = Path(__file__).resolve().parent
CONFIG = HERE / "config.json"
STATE = HERE / "state.json"
BASE = "https://www.instagram.com"


def ctx(p, headless=False):
    return p.chromium.launch_persistent_context(
        str(PROFILE), channel="chrome", headless=headless,
        viewport={"width": 1280, "height": 1000},
        args=["--disable-blink-features=AutomationControlled"],
    )


def has_session(c) -> bool:
    return any(k["name"] == "sessionid" and k["value"] for k in c.cookies(BASE))


def load(path: Path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def unwrap(href: str) -> str:
    """l.instagram.com/?u=<url> → <url>; strips IG tracking params."""
    u = urlparse(href)
    if u.netloc.endswith("l.instagram.com"):
        q = parse_qs(u.query).get("u")
        if q:
            href = unquote(q[0])
    return href


def key_of(href: str) -> str:
    m = re.search(r"instagram\.com/(?:[^/]+/)?(p|reel)/([\w-]+)", href) or re.match(r"^/(?:[^/]+/)?(p|reel)/([\w-]+)", href)
    if m:
        return f"ig:{m.group(2)}"
    u = urlparse(href)
    return f"url:{u.netloc.lower().removeprefix('www.')}{u.path.rstrip('/')}"


def cmd_login(_a) -> int:
    PROFILE.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        c = ctx(p)
        page = c.pages[0] if c.pages else c.new_page()
        page.goto(BASE + "/accounts/login/")
        print("Log in to Instagram in the opened Chrome window (up to 10 minutes)...", flush=True)
        deadline = time.time() + 600
        while time.time() < deadline:
            time.sleep(3)
            if has_session(c) and "/accounts/login" not in page.url and "/challenge" not in page.url:
                print("LOGGED_IN", flush=True)
                time.sleep(5)          # let IG finish writing cookies / "save login info"
                c.close()
                return 0
        c.close()
        print("LOGIN_TIMEOUT", flush=True)
        return 2


def cmd_check(_a) -> int:
    with sync_playwright() as p:
        c = ctx(p)
        page = c.pages[0] if c.pages else c.new_page()
        page.goto(BASE + "/direct/inbox/", wait_until="domcontentloaded")
        page.wait_for_timeout(4000)
        ok = has_session(c) and "/accounts/login" not in page.url
        c.close()
    print("LOGGED_IN" if ok else "NOT_LOGGED_IN")
    return 0 if ok else 3


def open_inbox(c):
    page = c.pages[0] if c.pages else c.new_page()
    page.goto(BASE + "/direct/inbox/", wait_until="domcontentloaded")
    page.wait_for_timeout(5000)
    if not has_session(c) or "/accounts/login" in page.url:
        print("NOT_LOGGED_IN: run `ig_pw.py login` first")
        sys.exit(3)
    for label in ("Not Now", "Not now"):          # "Turn on notifications?" dialog
        try:
            page.get_by_role("button", name=label).click(timeout=1500)
        except Exception:
            pass
    return page


def cmd_threads(_a) -> int:
    with sync_playwright() as p:
        c = ctx(p)
        page = open_inbox(c)
        rows = page.evaluate("""() => {
          const out = [];
          for (const a of document.querySelectorAll('a[href*="/direct/t/"]')) {
            const m = a.getAttribute('href').match(/\\/direct\\/t\\/(\\d+)/);
            if (m) out.push({id: m[1], title: a.innerText.split('\\n').slice(0, 2).join(' · ')});
          }
          // newer IG inbox rows are divs with role=button; read their text, ids come from clicking
          if (!out.length) {
            for (const d of document.querySelectorAll('div[role="listitem"], div[role="button"]')) {
              const t = d.innerText.trim(); if (t && t.length < 120) out.push({id: null, title: t.split('\\n').slice(0, 2).join(' · ')});
            }
          }
          return out;
        }""")
        if rows and all(r["id"] is None for r in rows):
            # resolve ids by clicking each of the first 15 rows
            res = []
            for r in rows[:15]:
                try:
                    page.get_by_text(r["title"].split(" · ")[0], exact=True).first.click(timeout=3000)
                    page.wait_for_timeout(1500)
                    m = re.search(r"/direct/t/(\d+)", page.url)
                    res.append({"id": m.group(1) if m else None, "title": r["title"]})
                except Exception:
                    pass
            rows = res
        c.close()
    print(json.dumps(rows, ensure_ascii=False, indent=1))
    return 0


JS_LINKS = r"""() => {
  const main = document.querySelector('div[role="main"]') || document.body;
  const out = [];
  for (const a of main.querySelectorAll('a[href]')) {
    const h = a.getAttribute('href');
    if (/\/(p|reel)\/[\w-]+/.test(h) || /^https?:\/\//.test(h) && !/instagram\.com\/(direct|accounts|explore|stories)?\/?$/.test(h)) {
      const row = a.closest('div[role="row"], div[role="gridcell"]') || a.parentElement;
      out.push({href: a.href, text: (row ? row.innerText : a.innerText).slice(0, 300)});
    }
  }
  return out;
}"""

JS_CTA = r"""() => {
  const as = [...document.querySelectorAll('a[href]')];
  const cta = as.filter(a => /l\.instagram\.com\/\?u=/.test(a.href) || (/^https?:\/\//.test(a.href) && !/instagram\.com|facebook\.com|meta\.com/.test(a.href)));
  const cap = document.querySelector('h1, article h1, div[role="dialog"] h1');
  return {cta: cta.map(a => ({href: a.href, label: a.innerText.trim().slice(0, 40)})),
          caption: (cap ? cap.innerText : '').slice(0, 600),
          author: (document.querySelector('header a[href^="/"]') || {}).innerText || ''};
}"""


def cmd_links(a) -> int:
    cfg = load(CONFIG, {})
    tid = a.thread or cfg.get("thread_id")
    if not tid:
        print("NO_THREAD: set thread_id in config.json (see `threads`)")
        return 5
    seen = set(load(STATE, {}).get("seen", []))
    run = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M")
    items: dict[str, dict] = {}
    with sync_playwright() as p:
        c = ctx(p)
        page = open_inbox(c)
        page.goto(f"{BASE}/direct/t/{tid}/", wait_until="domcontentloaded")
        page.wait_for_timeout(5000)
        for _ in range(a.scrolls):                 # newest at the bottom; scroll up for older
            for r in page.evaluate(JS_LINKS):
                k = key_of(r["href"])
                if k not in seen and k not in items:
                    items[k] = {"key": k, "src": r["href"], "landing": "", "text": r["text"], "ts": run}
            page.mouse.move(700, 400)
            page.mouse.wheel(0, -2500)
            page.wait_for_timeout(1200)
        for it in items.values():
            if it["key"].startswith("ig:"):
                try:
                    page.goto(it["src"], wait_until="domcontentloaded")
                    page.wait_for_timeout(3500)
                    info = page.evaluate(JS_CTA)
                    it["caption"], it["author"] = info["caption"], info["author"]
                    it["cta"] = info["cta"][:5]
                    if info["cta"]:
                        it["landing"] = unwrap(info["cta"][0]["href"])
                except Exception as e:
                    it["error"] = str(e)[:200]
            else:
                it["landing"] = unwrap(it["src"])
        c.close()
    obj = {"run": run, "thread": tid, "items": list(items.values())}
    d = OUT / run
    d.mkdir(parents=True, exist_ok=True)
    (d / "links.json").write_text(json.dumps(obj, ensure_ascii=False, indent=1), encoding="utf-8")
    obj["out"] = str(d / "links.json")
    print(json.dumps(obj, ensure_ascii=False))
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("login"); sub.add_parser("check"); sub.add_parser("threads")
    lk = sub.add_parser("links")
    lk.add_argument("--thread", default="")
    lk.add_argument("--scrolls", type=int, default=6)
    a = ap.parse_args()
    return {"login": cmd_login, "check": cmd_check, "threads": cmd_threads, "links": cmd_links}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
