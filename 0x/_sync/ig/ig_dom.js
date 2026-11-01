// ig_dom.js — paste into the Claude built-in browser on the xlei___ self-chat
// (https://www.instagram.com/direct/t/<thread_id>/) via javascript_tool.
// Defines window.__igdom. collect(scrolls) scrolls the message pane up and returns
//   urls:  every URL typed as TEXT in a message
//   posts: every shared post / reel (ad) card: {account, caption, key}. The ad's landing URL is
//          not in the DM — the run finds it (open the post, or web-search account + caption).
// Only pure-text messages (no URL, no shared post) are ignored. Unavailable stories are skipped.
(() => {
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
  const URL_RX = /\bhttps?:\/\/[^\s<>"'）)\]]+|\b(?:www\.)[^\s<>"'）)\]]+/gi;
  const unwrap = (h) => {
    try {
      const u = new URL(h);
      if (/(^|\.)l\.instagram\.com$/.test(u.hostname) && u.searchParams.get('u')) return u.searchParams.get('u');
    } catch (e) {}
    return h;
  };
  // anything on instagram / facebook (profiles, explore, shared posts) is not a report link
  const isIgInternal = (h) => /^https?:\/\/([\w-]+\.)*(instagram|facebook|fb)\.com(\/|$)/i.test(h);
  const pane = () => {
    // the scrollable message list: the tallest scrollable element inside main
    const els = [...document.querySelectorAll('div[role="main"] div, main div')]
      .filter((e) => e.scrollHeight > e.clientHeight + 50 && /(auto|scroll)/.test(getComputedStyle(e).overflowY));
    return els.sort((a, b) => b.clientHeight - a.clientHeight)[0] || document.scrollingElement;
  };
  const harvest = (found) => {
    const root = document.querySelector('div[role="main"]') || document.body;
    // 1) real anchors in message bubbles (IG wraps typed links in l.instagram.com)
    for (const a of root.querySelectorAll('a[href]')) {
      const h = unwrap(a.href);
      if (!/^https?:/.test(h) || isIgInternal(h) || /instagram\.com\/?$/.test(h)) continue;
      if (a.closest('nav, header')) continue;
      const row = a.closest('div[role="row"], div[role="gridcell"]') || a.parentElement;
      found.set(h, (row ? row.innerText : a.innerText).trim().slice(0, 300));
    }
    // 2) plain text URLs that IG did not linkify
    for (const el of root.querySelectorAll('div[dir="auto"], span[dir="auto"]')) {
      for (const m of (el.innerText || '').matchAll(URL_RX)) {
        let h = m[0].replace(/[.,;:!?]+$/, '');
        if (!/^https?:/.test(h)) h = 'https://' + h;
        if (!isIgInternal(h) && !found.has(h)) found.set(h, el.innerText.trim().slice(0, 300));
      }
    }
  };
  const hash = (t) => { let h = 5381; for (const c of t) h = ((h * 33) ^ c.charCodeAt(0)) >>> 0; return h.toString(36); };
  // shared post cards: a role=button whose text starts with the account name, then the caption
  const harvestPosts = (posts) => {
    const root = document.querySelector('div[role="main"]') || document.body;
    for (const b of root.querySelectorAll('[role="button"]')) {
      const prof = [...b.parentElement?.parentElement?.parentElement?.querySelectorAll('a[href^="https://www.instagram.com/"], a[href^="/"]') || []]
        .map((a) => a.href).find((h) => /^https:\/\/www\.instagram\.com\/[^/]+\/?$/.test(h) && !/\/(direct|explore|reels)\/?$/.test(h));
      if (!prof) continue;
      const account = decodeURIComponent(prof.replace(/\/$/, '').split('/').pop());
      const txt = (b.innerText || '').trim();
      if (!txt.startsWith(account)) continue;
      const caption = txt.slice(account.length).trim().slice(0, 500);
      if (!caption || /story unavailable/i.test(txt)) continue;
      const key = 'post:' + account.toLowerCase() + ':' + hash(caption.slice(0, 200));
      posts.set(key, { key, account, caption });
    }
  };
  const collect = async (scrolls = 8) => {
    const found = new Map();
    const posts = new Map();
    const p = pane();
    harvest(found); harvestPosts(posts);
    for (let i = 0; i < scrolls; i++) {
      p.scrollTop = Math.max(0, p.scrollTop - p.clientHeight * 0.9);
      await sleep(1300);
      harvest(found); harvestPosts(posts);
      if (p.scrollTop === 0) break;
    }
    return { thread: location.pathname, urls: [...found].map(([url, text]) => ({ url, text })), posts: [...posts.values()] };
  };
  window.__igdom = { collect, unwrap };
  return 'ig_dom ready';
})();
