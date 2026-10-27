#!/usr/bin/env python3
"""x_pw.py — Playwright driver for X Likes / Bookmarks (MVP1, local first).

Why Playwright instead of the Claude browser pane:
  - Playwright's Chromium flags disable background/occlusion throttling, so infinite
    scroll keeps loading even when the window is covered or the PC is idle.
  - It sees network responses, so we can read X's own JSON instead of guessing the DOM
    (X's new 2026 UI dropped data-testid/<time>; the DOM is no longer a stable contract).

Usage (Windows, from any dir; uv pulls playwright into a cached env):
  uv run --with playwright python x_pw.py login              # one-time: log in by hand
  uv run --with playwright python x_pw.py count [--headless] # scroll both lists to the end, count

Profile (cookies) lives OUTSIDE the repo: D:\\1AL\\x-tw-profile  (never commit it).
Output: <out>/<run>/counts.json, ids_<list>.json, net_log.jsonl, api_*.json (sample bodies)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

from playwright.sync_api import sync_playwright

PROFILE = Path(r"D:\1AL\x-tw-profile")
OUT = Path(r"D:\2Alfred\x-twitter\raw")
LISTS = {"likes": "https://x.com/i/history/likes", "bookmarks": "https://x.com/i/history"}
OWN_STATUS = re.compile(r"^/[^/]+/status/(\d+)$")

# One JS helper, works on both the old (data-testid) and new (2026) X markup:
# each <article>'s first link of the form /<user>/status/<id> is the post itself
# (quoted posts come later inside the same article).
JS_VISIBLE = """
() => [...document.querySelectorAll('article')].map(a => {
  const links = [...a.querySelectorAll('a[href]')];
  const own = links.find(l => /^\\/[^/]+\\/status\\/\\d+$/.test(l.getAttribute('href')));
  if (!own) return null;
  const href = own.getAttribute('href');
  const dateLink = links.find(l => l.getAttribute('href') === href && l.innerText.trim());
  return { href, date: dateLink ? dateLink.innerText.trim() : '' };
}).filter(Boolean)
"""


def ctx(p, headless: bool):
    return p.chromium.launch_persistent_context(
        str(PROFILE),
        channel="chrome",                 # the installed Chrome; no browser download
        headless=headless,
        viewport={"width": 1280, "height": 1000},
        service_workers="block",          # force data requests through the page so we can see them
        args=["--disable-blink-features=AutomationControlled"],
    )


def logged_in(page) -> bool:
    return page.evaluate("""() => !!document.querySelector('a[href="/compose/post"], a[aria-label*="Profile" i], [data-testid="SideNav_AccountSwitcher_Button"]')
                                 || /\\/home$/.test(location.pathname)""")


def cmd_login(_args) -> int:
    PROFILE.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        c = ctx(p, headless=False)
        page = c.pages[0] if c.pages else c.new_page()
        page.goto("https://x.com/i/flow/login")
        print("Log in to X in the opened Chrome window (up to 10 minutes)...", flush=True)
        deadline = time.time() + 600
        while time.time() < deadline:
            time.sleep(3)
            try:
                if "/home" in page.url or logged_in(page):
                    print("LOGGED_IN", flush=True)
                    time.sleep(3)
                    c.close()
                    return 0
            except Exception:
                pass
        c.close()
        print("LOGIN_TIMEOUT", flush=True)
        return 2


def scroll_all(page, name: str, url: str, max_idle: int = 15) -> list[dict]:
    page.goto(url, wait_until="domcontentloaded")
    page.wait_for_timeout(4000)
    if "login" in page.url or "/i/flow" in page.url:
        raise SystemExit("NOT_LOGGED_IN: run `x_pw.py login` first")
    seen: dict[str, dict] = {}
    idle, rounds = 0, 0
    while idle < max_idle:
        rounds += 1
        before = len(seen)
        for v in page.evaluate(JS_VISIBLE):
            m = OWN_STATUS.match(v["href"])
            if m and m.group(1) not in seen:
                seen[m.group(1)] = {"id": m.group(1), "href": v["href"], "date": v["date"], "pos": len(seen)}
        idle = idle + 1 if len(seen) == before else 0
        page.mouse.move(640, 500)
        page.mouse.wheel(0, 2200)
        page.wait_for_timeout(1200 if idle == 0 else 2500)
        if rounds % 20 == 0:
            print(f"  {name}: {len(seen)} so far", flush=True)
    return list(seen.values())


def cmd_count(args) -> int:
    run = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M") + "-count"
    out = OUT / run
    out.mkdir(parents=True, exist_ok=True)
    net_log = (out / "net_log.jsonl").open("w", encoding="utf-8")
    saved_samples: set[str] = set()

    def on_response(r):
        u = r.url
        if "x.com/i/api" not in u and "api.x.com" not in u and "/graphql/" not in u:
            return
        op = u.split("?")[0].rsplit("/", 1)[-1]
        net_log.write(json.dumps({"op": op, "status": r.status, "url": u[:200]}) + "\n")
        # keep one sample body per operation that looks like our lists → learn the API shape
        if re.search(r"(?i)like|bookmark|history|timeline", op) and op not in saved_samples:
            try:
                (out / f"api_{op}.json").write_text(r.text(), encoding="utf-8")
                saved_samples.add(op)
            except Exception:
                pass

    result = {}
    with sync_playwright() as p:
        c = ctx(p, headless=args.headless)
        c.on("response", on_response)
        page = c.pages[0] if c.pages else c.new_page()
        for name, url in LISTS.items():
            t0 = time.time()
            items = scroll_all(page, name, url)
            (out / f"ids_{name}.json").write_text(json.dumps(items, ensure_ascii=False, indent=1), encoding="utf-8")
            result[name] = {"count": len(items), "newest": items[0] if items else None,
                            "oldest": items[-1] if items else None, "seconds": round(time.time() - t0)}
            print(f"{name}: {len(items)}", flush=True)
        c.close()
    net_log.close()
    result["api_samples"] = sorted(saved_samples)
    (out / "counts.json").write_text(json.dumps(result, ensure_ascii=False, indent=1), encoding="utf-8")
    print("RESULT " + json.dumps(result, ensure_ascii=False), flush=True)
    print("OUT " + str(out), flush=True)
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("login")
    c = sub.add_parser("count")
    c.add_argument("--headless", action="store_true")
    a = ap.parse_args()
    return {"login": cmd_login, "count": cmd_count}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
