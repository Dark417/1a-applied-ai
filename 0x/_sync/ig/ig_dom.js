// ig_dom.js — paste into the Claude built-in browser on the xlei___ self-chat
// (https://www.instagram.com/direct/t/<thread_id>/) via javascript_tool.
// Defines window.__igdom. collect(scrolls) scrolls the message pane up and returns every
// URL typed as TEXT in a message. Shared posts / reels / stories are NOT URLs → ignored.
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
  const isIgInternal = (h) => /^https?:\/\/(www\.)?instagram\.com\/(p|reel|reels|stories|direct|accounts)\b/i.test(h);
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
  const collect = async (scrolls = 8) => {
    const found = new Map();
    const p = pane();
    harvest(found);
    for (let i = 0; i < scrolls; i++) {
      p.scrollTop = Math.max(0, p.scrollTop - p.clientHeight * 0.9);
      await sleep(1300);
      harvest(found);
      if (p.scrollTop === 0) break;
    }
    return { thread: location.pathname, urls: [...found].map(([url, text]) => ({ url, text })) };
  };
  window.__igdom = { collect, unwrap };
  return 'ig_dom ready';
})();
