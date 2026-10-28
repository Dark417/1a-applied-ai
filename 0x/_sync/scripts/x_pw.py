#!/usr/bin/env python3
"""x_pw.py — Playwright driver for X Likes / Bookmarks (MVP1, local first).

Why Playwright instead of the Claude browser pane:
  - Playwright's Chromium flags disable background/occlusion throttling, so infinite
    scroll keeps loading even when the window is covered or the PC is idle.
  - It sees network responses, so we can read X's own JSON instead of guessing the DOM
    (X's new 2026 UI dropped data-testid/<time>; the DOM is no longer a stable contract).

Usage (Windows, from any dir; uv pulls playwright into a cached env):
  uv run --with playwright python x_pw.py login              # one-time: log in by hand
  uv run --with playwright python x_pw.py check              # headless: is the saved session still logged in?
  uv run --with playwright python x_pw.py pull               # what Cowork does nightly, no AI: new likes/bookmarks
  uv run --with playwright python x_pw.py pull --all         # full history (ignore the watermark)
  uv run --with playwright python x_pw.py count [--headless] # scroll both lists to the end, count

Profile (cookies) lives OUTSIDE the repo: D:\\1AL\\x-tw-profile  (never commit it).

`pull` = RUNBOOK steps 2–4 without the Claude browser pane or the Save-As dialog:
  - injects the same x_dom.js the Cowork run pastes into the browser pane (one source of truth)
  - writes <out>/<RUN>-pw/{likes,bookmarks,details}.json in exactly the format build.py reads,
    plus api/*.json: the raw GraphQL responses X sent (Likes / Bookmarks / TweetDetail), for debugging
  - reads the watermark from ../state.json but never writes it: build.py apply does that after the
    AI step (summaries + readable versions), so running `pull` twice is harmless
Exit codes: 0 ok · 3 not logged in (run `login` again) · 4 X page layout changed (x_dom.js finds no posts)
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


BASE = "https://x.com"
CHANNEL = "chrome"                        # the installed Chrome; "" = Playwright's own Chromium (tests)
X_DOM = Path(__file__).with_name("x_dom.js")
STATE = Path(__file__).resolve().parent.parent / "state.json"


def ctx(p, headless: bool):
    return p.chromium.launch_persistent_context(
        str(PROFILE),
        channel=CHANNEL or None,
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


# ---------------------------------------------------------------- pull
class NotLoggedIn(SystemExit):
    def __init__(self):
        super().__init__(3)


def open_history(page) -> None:
    """Land on Bookmarks (renders reliably; Likes sometimes stays blank on a cold load), inject x_dom.js."""
    try:  # logged out, X may answer /i/history with an error status instead of a redirect
        page.goto(BASE + "/i/history", wait_until="domcontentloaded")
        page.wait_for_selector('article[data-testid="tweet"]', timeout=20000)
        ok = True
    except Exception:
        ok = False
    if not ok:
        try:
            page.goto(BASE + "/home", wait_until="domcontentloaded")
            page.wait_for_timeout(5000)
        except Exception:
            pass
        signed_in = page.evaluate("""() => !!document.querySelector('a[href="/compose/post"], [data-testid="SideNav_AccountSwitcher_Button"], [data-testid="AppTabBar_Profile_Link"]')""")
        if "/login" in page.url or "/i/flow" in page.url or not signed_in:
            print("NOT_LOGGED_IN: run `x_pw.py login` first", flush=True)
            raise NotLoggedIn()
        page.goto(BASE + "/i/history", wait_until="domcontentloaded")
        page.wait_for_timeout(5000)
    print(page.evaluate(X_DOM.read_text(encoding="utf-8")), flush=True)  # -> "x_dom ready"


def collect(page, path: str, max_n: int, stop_ids: list[str]) -> dict:
    """SPA-navigate to a list and scroll it; same call the Cowork run makes."""
    if not page.evaluate("p => __xdom.go(p)", path):
        # blank list: bounce through the other tab once (what fixed it by hand in the pane)
        other = "/i/history" if path != "/i/history" else "/i/history/likes"
        page.evaluate("p => __xdom.go(p)", other)
        if not page.evaluate("p => __xdom.go(p)", path):
            print(f"LAYOUT_CHANGED: no posts on {path}", flush=True)
            raise SystemExit(4)
    return page.evaluate("([n, s]) => __xdom.collectList(n, s)", [max_n, stop_ids])


def cmd_pull(args) -> int:
    run = args.run or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M") + "-pw"
    out = Path(args.out) / run
    (out / "api").mkdir(parents=True, exist_ok=True)
    state = json.loads(STATE.read_text(encoding="utf-8")) if STATE.exists() and not args.all else {}
    max_n = 5000 if args.all else args.max

    n_api = {"n": 0}

    def on_response(r):
        op = r.url.split("?")[0].rsplit("/", 1)[-1]
        if "/graphql/" in r.url and op in ("Likes", "Bookmarks", "TweetDetail"):
            try:
                n_api["n"] += 1
                (out / "api" / f"{n_api['n']:03d}_{op}.json").write_text(r.text(), encoding="utf-8")
            except Exception:
                pass

    t0 = time.time()
    with sync_playwright() as p:
        c = ctx(p, headless=not args.headed)
        c.on("response", on_response)
        page = c.pages[0] if c.pages else c.new_page()
        try:
            open_history(page)
            bm = collect(page, "/i/history", max_n, state.get("bookmarks", []))
            print(f"bookmarks: {len(bm['items'])} new (stopped at {bm['hitWatermark']})", flush=True)
            lk = collect(page, "/i/history/likes", max_n, state.get("likes", []))
            print(f"likes: {len(lk['items'])} new (stopped at {lk['hitWatermark']})", flush=True)
            # status pages: every new bookmark + likes that are replies / cut off / text-less (RUNBOOK §3)
            tasks, seen = [], set()
            for t in bm["items"] + [x for x in lk["items"] if x["is_reply"] or x["truncated"] or not x["text"]]:
                if t["id"] not in seen:
                    seen.add(t["id"])
                    tasks.append([t["handle"], t["id"]])
            print(f"details: {len(tasks)} status pages", flush=True)
            page.evaluate("t => __xdom.job('detail', t)", tasks)
            det = page.evaluate("() => window.__job")
        finally:
            c.close()

    w = lambda name, obj: (out / name).write_text(json.dumps(obj, ensure_ascii=False), encoding="utf-8")
    w("likes.json", lk["items"])
    w("bookmarks.json", bm["items"])
    w("details.json", det["out"])
    meta = {"run": run, "likes": len(lk["items"]), "bookmarks": len(bm["items"]), "details": len(det["out"]),
            "detail_errors": det["errors"], "watermark": {"likes": lk["hitWatermark"], "bookmarks": bm["hitWatermark"]},
            "all": args.all, "seconds": round(time.time() - t0)}
    w("meta.json", meta)
    print("RESULT " + json.dumps(meta, ensure_ascii=False), flush=True)
    print("OUT " + str(out), flush=True)
    return 0


def cmd_check(args) -> int:
    with sync_playwright() as p:
        c = ctx(p, headless=True)
        page = c.pages[0] if c.pages else c.new_page()
        try:
            open_history(page)
        finally:
            c.close()
    print("LOGGED_IN", flush=True)
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("login")
    c = sub.add_parser("count")
    c.add_argument("--headless", action="store_true")
    sub.add_parser("check")
    pl = sub.add_parser("pull")
    pl.add_argument("--all", action="store_true", help="full history, ignore the state.json watermark")
    pl.add_argument("--max", type=int, default=50, help="max new items per list (default 50)")
    pl.add_argument("--headed", action="store_true", help="show the Chrome window")
    pl.add_argument("--out", default=str(OUT))
    pl.add_argument("--run", default="", help="run folder name (default <UTC time>-pw)")
    for sp in sub.choices.values():  # test hooks: point at a mock site / bundled Chromium / temp profile
        sp.add_argument("--base", default=None, help=argparse.SUPPRESS)
        sp.add_argument("--channel", default=None, help=argparse.SUPPRESS)
        sp.add_argument("--profile", default=None, help=argparse.SUPPRESS)
        sp.add_argument("--state", default=None, help=argparse.SUPPRESS)
    a = ap.parse_args()
    global BASE, CHANNEL, PROFILE, STATE
    BASE = a.base or BASE
    CHANNEL = CHANNEL if a.channel is None else a.channel
    PROFILE = Path(a.profile) if a.profile else PROFILE
    STATE = Path(a.state) if a.state else STATE
    return {"login": cmd_login, "count": cmd_count, "check": cmd_check, "pull": cmd_pull}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
