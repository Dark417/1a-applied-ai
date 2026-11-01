#!/usr/bin/env python3
"""ig_fill.py — cloud Playwright: open a report landing page, fill ONLY the required fields
with the persona from config.json, submit, and catch the PDF.

  python3 ig_fill.py <url> <outdir>
Prints one JSON line:
  {"status": "pdf" | "email" | "submitted" | "no_form" | "blocked" | "error",
   "pdf": "<path>", "pdf_url": "...", "title": "...", "final_url": "...",
   "filled": [...], "skipped_required": [...], "shot": "<png>"}
status meaning: pdf = got the file; email = page says it was emailed (check Gmail later);
submitted = sent but no clear signal; blocked = a required field we will not fake (phone, …);
no_form = page has no lead form (maybe the PDF is directly linked — see pdf_url).
Rules: required fields only (+ email); required consent checkboxes only, never optional
marketing ones; cookie banners → reject / necessary-only. Phone only if config.persona.phone is set.
Multi-step forms (Next → more fields) are followed on the same page; account sign-up forms never.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

CFG = json.loads((Path(__file__).with_name("config.json")).read_text(encoding="utf-8"))
P = CFG["persona"]
COUNTRY = CFG.get("country", "United States")

FIELD_RULES = [  # (regex on name/id/label/placeholder/autocomplete, value)
    (r"e-?mail", P["email"]),
    (r"first.?name|given|fname|vorname", P["first_name"]),
    (r"last.?name|surname|family|lname", P["last_name"]),
    (r"^(full.?)?name$|your name|full name", f'{P["first_name"]} {P["last_name"]}'),
    (r"company|organi[sz]ation|employer|business name|account", P["company"]),
    (r"job.?title|title|role|position|designation", P["title"]),
    (r"website|domain|url", "https://xiaoxiaolei.com"),
]
NEVER = r"phone|mobile|tel|cell|zip|postal|address|street|city"

JS_FIELDS = r"""(root) => {
  const vis = e => { const r = e.getBoundingClientRect(); const s = getComputedStyle(e);
    return r.width > 0 && r.height > 0 && s.visibility !== 'hidden' && s.display !== 'none'; };
  const labelOf = e => {
    let t = '';
    if (e.id) { const l = document.querySelector(`label[for="${CSS.escape(e.id)}"]`); if (l) t = l.innerText; }
    if (!t) { const l = e.closest('label'); if (l) t = l.innerText; }
    if (!t) { const w = e.closest('div, li, fieldset'); if (w) { const l = w.querySelector('label, legend'); if (l) t = l.innerText; } }
    return (t || '').trim().slice(0, 120);
  };
  const out = [];
  document.querySelectorAll('input, select, textarea').forEach((e, i) => {
    const type = (e.getAttribute('type') || e.tagName).toLowerCase();
    if (['hidden', 'submit', 'button', 'image', 'reset', 'search', 'password', 'file'].includes(type)) return;
    if (!vis(e) && type !== 'checkbox') return;
    e.setAttribute('data-igf', String(i));
    const label = labelOf(e);
    out.push({ i, tag: e.tagName.toLowerCase(), type, name: e.name || '', id: e.id || '',
      ph: e.placeholder || '', ac: e.autocomplete || '', label,
      req: e.required || e.getAttribute('aria-required') === 'true' || /\*\s*$|\*\s*:?$|required/i.test(label),
      opts: e.tagName === 'SELECT' ? [...e.options].filter(o => o.value !== '' && !o.disabled).map(o => o.text.trim()).slice(0, 80) : null,
      val: e.value || '' });
  });
  return out;
}"""

DONE_EMAIL = re.compile(r"check your (e-?mail|inbox)|sent (it )?to your (e-?mail|inbox)|on its way|we('|’)ve (sent|emailed)|email(ed)? you", re.I)
DONE_OK = re.compile(r"thank(s| you)|success|download (now|the|your)|access (the|your)|here('|’)s your", re.I)


def pick(f):
    hay = " ".join([f["name"], f["id"], f["ph"], f["ac"], f["label"]]).lower()
    if f["type"] == "email" or re.search(r"e-?mail", hay):   # before NEVER: "Email Address"
        return P["email"]
    if P.get("phone") and (f["type"] == "tel" or re.search(r"phone|mobile|tel\b|cell", hay)):
        return P["phone"]                   # only if the user put a phone in config.json
    if re.search(NEVER, hay):
        return None
    for rx, v in FIELD_RULES:
        if re.search(rx, hay):
            return v
    return None


def choose_option(f):
    hay = (f["label"] + " " + f["name"]).lower()
    opts = [o for o in (f["opts"] or []) if o and not re.match(r"^(select|choose|please|--|-)", o, re.I)]
    if not opts:
        return None
    if "country" in hay:
        return next((o for o in opts if o.lower() in ("united states", "usa", "us", "united states of america")), None)
    if re.search(r"size|employees", hay):
        return opts[0]
    if re.search(r"industry", hay):
        return next((o for o in opts if re.search(r"tech|software|it\b|computer", o, re.I)), opts[-1])
    if re.search(r"role|title|function|department|level", hay):
        return next((o for o in opts if re.search(r"architect|engineer|it|technical|developer", o, re.I)), opts[-1])
    return next((o for o in opts if re.search(r"other", o, re.I)), opts[0])


def dismiss_cookies(page):
    for name in ["Reject all", "Reject All", "Decline", "Necessary only", "Only necessary", "Reject", "Deny"]:
        try:
            page.get_by_role("button", name=name, exact=True).first.click(timeout=800)
            return
        except Exception:
            pass


SUBMIT_RX = re.compile(r"^next$|^continue$|download|submit|get (it|the|my|your|access|report|guide|ebook|cheat)|access|send|read|continue|unlock", re.I)


def submit(frame, page):
    """Click the form's submit button. Handles banners covering it, non-type=submit buttons,
    and falls back to requestSubmit() on the form that holds the email field."""
    dismiss_cookies(page)
    cands = [frame.locator("button[type=submit], input[type=submit]").first,
             frame.locator("form button:not([type=button])").first,
             frame.get_by_role("button", name=SUBMIT_RX).first]
    for loc in cands:
        try:
            if loc.count() == 0:
                continue
            loc.scroll_into_view_if_needed(timeout=3000)
            try:
                loc.click(timeout=5000)
            except Exception:
                loc.click(timeout=5000, force=True)
            return
        except Exception:
            continue
    frame.evaluate("""() => { const e = document.querySelector('input[type=email], input[name*=mail i]');
      const f = e && e.closest('form'); if (f) { f.requestSubmit ? f.requestSubmit() : f.submit(); } }""")


def fill_step(frame, res):
    """Fill the currently visible required fields (+ email). Returns required fields we won't fill."""
    skipped = []
    for f in frame.evaluate(JS_FIELDS, None):
        sel = f'[data-igf="{f["i"]}"]'
        hay = f["name"] + " " + f["label"] + " " + f["ph"]
        is_email = f["type"] == "email" or re.search("e-?mail", hay, re.I)
        if not (f["req"] or is_email) and CFG.get("only_required", True):
            continue
        try:
            if f["type"] in ("checkbox", "radio"):
                if f["req"]:
                    frame.check(sel, force=True); res["filled"].append(f"[x] {f['label'][:60]}")
                continue
            if f["tag"] == "select":
                o = choose_option(f)
                if o:
                    frame.select_option(sel, label=o); res["filled"].append(f"{(f['label'] or f['name'])[:40]}={o}")
                else:
                    skipped.append(f["label"] or f["name"])
                continue
            if f["val"]:
                continue
            v = pick(f)
            if v is None:
                skipped.append(f["label"] or f["name"] or f["ph"])
                continue
            frame.fill(sel, v); res["filled"].append(f"{(f['name'] or f['label'])[:40]}={v}")
        except Exception as e:
            res.setdefault("warn", []).append(f"{f['name'] or f['label']}: {str(e)[:80]}")
    return skipped


def main():
    url, out = sys.argv[1], Path(sys.argv[2])
    out.mkdir(parents=True, exist_ok=True)
    res = {"status": "error", "pdf": "", "pdf_url": "", "filled": [], "skipped_required": []}
    with sync_playwright() as p:
        b = p.chromium.launch()
        c = b.new_context(accept_downloads=True, viewport={"width": 1280, "height": 1100},
                          user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36")
        page = c.new_page()
        pdf_hits: list[str] = []
        c.on("response", lambda r: pdf_hits.append(r.url) if "application/pdf" in (r.headers.get("content-type") or "") else None)

        def save_download(d):
            path = out / (d.suggested_filename or "report.pdf")
            d.save_as(path)
            res["pdf"] = str(path)
        page.on("download", save_download)
        try:
            r0 = c.request.get(url, timeout=60000)      # the link itself may be the PDF
            if r0.ok and r0.body()[:4] == b"%PDF":
                path = out / (Path(url.split("?")[0]).name or "report.pdf")
                path.write_bytes(r0.body())
                res.update(status="pdf", pdf=str(path), pdf_url=url, final_url=r0.url, via="direct")
                print(json.dumps(res, ensure_ascii=False)); b.close(); return
            page.goto(url, wait_until="domcontentloaded", timeout=45000)
            page.wait_for_timeout(5000)
            dismiss_cookies(page)
            res["title"] = page.title()
            # the form may live in an iframe (HubSpot / Marketo / Pardot)
            frame = None
            for fr in page.frames:
                try:
                    fields = fr.evaluate(JS_FIELDS, None)
                except Exception:
                    continue
                if any(f["type"] == "email" or re.search("mail", f["name"] + f["label"], re.I) for f in fields):
                    frame = fr
                    break
            if not frame:
                links = page.eval_on_selector_all("a[href]", "as => as.map(a => a.href).filter(h => /\\.pdf(\\?|$)/i.test(h))")
                res.update(status="no_form", pdf_url=(links or pdf_hits or [""])[0])
            else:
                # multi-step forms (Wiz: email → Next → more fields): fill visible required fields,
                # submit, and repeat while a new unfilled step shows up (max 4 steps)
                start_url = page.url.split("?")[0].rstrip("/")
                for step in range(4):
                    skipped = fill_step(frame, res)
                    if skipped:
                        res["skipped_required"] = skipped
                        break
                    submit(frame, page)
                    page.wait_for_timeout(6000 if step < 3 else 9000)
                    if res["pdf"] or pdf_hits:
                        break
                    nxt = None
                    if page.url.split("?")[0].rstrip("/") != start_url:
                        break                    # left the landing page (thank-you page): never fill a 2nd form there
                    for fr in page.frames:
                        try:
                            fs = fr.evaluate(JS_FIELDS, None)
                        except Exception:
                            continue
                        if any(f["type"] == "password" or re.search(r"signup|sign-up|register|password", f["name"] + f["id"], re.I) for f in fs):
                            continue             # account sign-up / login forms are never filled
                        if any(f["req"] and not f["val"] and f["type"] not in ("checkbox", "radio") for f in fs):
                            nxt = fr
                            break
                    if not nxt:
                        break
                    frame = nxt
                if res["skipped_required"]:
                    res["status"] = "blocked"
                else:
                    page.wait_for_timeout(3000)
                    for pg in c.pages:      # popups / new tabs with the PDF
                        if pg is not page and pg.url.lower().split("?")[0].endswith(".pdf"):
                            pdf_hits.append(pg.url)
                    txt = " ".join(fr.evaluate("() => document.body ? document.body.innerText : ''") for fr in page.frames if not fr.is_detached())[:20000]
                    links = []
                    for fr in page.frames:
                        try:
                            links += fr.eval_on_selector_all("a[href]", "as => as.map(a => a.href).filter(h => /\\.pdf(\\?|$)/i.test(h))")
                        except Exception:
                            pass
                    res["pdf_url"] = (pdf_hits or links or [""])[0]
                    if res["pdf"] or res["pdf_url"]:
                        res["status"] = "pdf"
                    elif DONE_EMAIL.search(txt):
                        res["status"] = "email"
                    else:
                        res["status"] = "submitted"
            if res["pdf_url"] and not res["pdf"]:
                r = c.request.get(res["pdf_url"], timeout=60000)
                if r.ok and r.body()[:4] == b"%PDF":
                    path = out / (Path(res["pdf_url"].split("?")[0]).name or "report.pdf")
                    path.write_bytes(r.body()); res["pdf"] = str(path); res["status"] = "pdf"
            res["final_url"] = page.url
        except Exception as e:
            res["error"] = str(e)[:300]
        finally:
            shot = out / "after.png"
            try:
                page.screenshot(path=str(shot), full_page=False); res["shot"] = str(shot)
            except Exception:
                pass
            b.close()
    print(json.dumps(res, ensure_ascii=False))


if __name__ == "__main__":
    main()
