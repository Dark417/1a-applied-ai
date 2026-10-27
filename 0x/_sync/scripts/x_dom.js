// x_dom.js — paste into an x.com tab (logged in) via the browser's javascript tool.
// Defines window.__xdom. All navigation is SPA (pushState + popstate), so this
// script stays alive across list → status page → list.
//
// Why DOM, not GraphQL interception: X keeps references to fetch/XHR from boot,
// so hooks installed after page load see nothing. (Playwright can use page.on('response').)
//
// Pages (as of 2026-10): /i/history = Bookmarks tab, /i/history/likes = Likes tab.
(() => {
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

  // tweetText → plain text; keeps emoji (img alt) and full URLs (hidden spans)
  const textOf = (el) => {
    if (!el) return '';
    let out = '';
    const walk = (n) => {
      if (n.nodeType === 3) { out += n.nodeValue; return; }
      if (n.nodeType !== 1) return;
      if (n.tagName === 'IMG') { out += n.getAttribute('alt') || ''; return; }
      if (n.tagName === 'A') {
        const t = n.textContent.replace(/…$/, '');
        out += /^https?:\/\//.test(t) || /^[\w.-]+\.[a-z]{2,}\//i.test(t) ? t : n.textContent;
        return;
      }
      if (n.tagName === 'BR') { out += '\n'; return; }
      n.childNodes.forEach(walk);
    };
    walk(el);
    return out.trim();
  };

  const statusFromHref = (h) => {
    const m = (h || '').match(/^\/([^/]+)\/status\/(\d+)/);
    return m ? { handle: m[1], id: m[2] } : null;
  };

  const extract = (a) => {
    const quoteBox = a.querySelector('div[role="link"]');
    const notInQuote = (e) => !quoteBox || !quoteBox.contains(e);
    const timeEl = [...a.querySelectorAll('time')].find(notInQuote);
    const st = statusFromHref(timeEl && timeEl.closest('a') && timeEl.closest('a').getAttribute('href'));
    if (!st) return null;
    const nameBox = [...a.querySelectorAll('[data-testid="User-Name"]')].find(notInQuote);
    const textEl = [...a.querySelectorAll('[data-testid="tweetText"]')].find(notInQuote);
    const quoteText = quoteBox && quoteBox.querySelector('[data-testid="tweetText"]');
    const quoteName = quoteBox && quoteBox.querySelector('[data-testid="User-Name"]');
    const card = a.querySelector('[data-testid="card.wrapper"]');
    const articleLink = a.querySelector('a[href*="/article/"]');
    const at = a.querySelector('[data-testid="twitter-article-title"]');      // X long-form Article
    const ab = a.querySelector('[data-testid="twitterArticleRichTextView"]'); // (status page only)
    const t = {
      id: st.id,
      handle: st.handle,
      name: nameBox ? nameBox.innerText.split('\n')[0] : '',
      url: `https://x.com/${st.handle}/status/${st.id}`,
      created_at: timeEl.getAttribute('datetime'),
      text: textOf(textEl),
      truncated: !!a.querySelector('[data-testid="tweet-text-show-more-link"]'),
      is_reply: /(^|\n)Replying to\s/.test(a.innerText),
      is_ad: [...a.querySelectorAll('span')].some((s) => s.textContent === 'Ad' || s.textContent === 'Promoted'),
      has_video: !!a.querySelector('[data-testid="videoPlayer"]'),
      media: [...a.querySelectorAll('img[src*="pbs.twimg.com/media"]')].filter(notInQuote)
        .map((i) => i.src.replace(/name=\w+/, 'name=large')),
      card: card ? { text: card.innerText.trim(), href: (card.querySelector('a') || {}).href || '' } : null,
      article: articleLink ? { href: articleLink.href } : null,
      quote: quoteBox && quoteText ? {
        name: quoteName ? quoteName.innerText.replace(/\n/g, ' ') : '',
        text: textOf(quoteText),
      } : null,
    };
    if (at || ab) t.x_article = { title: at ? at.innerText.trim() : '', body: ab ? ab.innerText.trim() : '' };
    return t;
  };

  const visible = () => [...document.querySelectorAll('article[data-testid="tweet"]')]
    .map(extract).filter((t) => t && !t.is_ad);

  // SPA navigation without a reload
  const go = async (path, waitFor = 'article[data-testid="tweet"]') => {
    history.pushState({}, '', path);
    window.dispatchEvent(new PopStateEvent('popstate', { state: {} }));
    for (let i = 0; i < 30; i++) {
      await sleep(300);
      if (location.pathname === path && document.querySelector(waitFor)) { await sleep(800); return true; }
    }
    return false;
  };

  // Scroll the current list page; collect in list order. Stop at maxN, at a
  // watermark id (stopIds), or after 4 scrolls with nothing new.
  const collectList = async (maxN = 50, stopIds = []) => {
    const stop = new Set(stopIds);
    const seen = new Map();
    let idle = 0, hitWatermark = null;
    window.scrollTo(0, 0);
    await sleep(1500);
    while (seen.size < maxN && idle < 4) {
      const before = seen.size;
      for (const t of visible()) {
        if (stop.has(t.id)) { hitWatermark = t.id; break; }
        if (!seen.has(t.id)) seen.set(t.id, t);
        if (seen.size >= maxN) break;
      }
      if (hitWatermark) break;
      idle = seen.size === before ? idle + 1 : 0;
      window.scrollBy(0, Math.round(window.innerHeight * 0.8));
      await sleep(1200);
    }
    return { items: [...seen.values()], hitWatermark };
  };

  // Status page: focal post (full text / Article body), conversation root
  // (first article above the focal), and the author's self-thread = consecutive
  // posts by the same author right after the focal. Stops at the first post by
  // anyone else, so comments are never collected.
  const readStatus = async (handle, id) => {
    if (!(await go(`/${handle}/status/${id}`))) return { id, error: 'load-timeout' };
    const list = visible();
    const fi = list.findIndex((t) => t.id === id);
    const focal = list[fi] || null;
    const root = fi > 0 ? list[0] : null;
    const seen = new Set(list.map((t) => t.id));
    const ordered = list.slice(fi + 1);
    for (let k = 0; k < 4; k++) {
      window.scrollBy(0, Math.round(window.innerHeight * 0.8));
      await sleep(800);
      for (const t of visible()) if (!seen.has(t.id)) { seen.add(t.id); ordered.push(t); }
    }
    const thread = [];
    for (const t of ordered) {
      if (focal && t.handle.toLowerCase() === focal.handle.toLowerCase()) thread.push(t);
      else break;
    }
    return { id, focal, root, thread };
  };

  // Long-running batch; poll window.__job from later calls (tool calls time out at ~45s).
  const job = async (name, tasks) => {
    window.__job = { name, total: tasks.length, done: 0, out: {}, errors: [] };
    for (const [h, id] of tasks) {
      try { window.__job.out[id] = await readStatus(h, id); } catch (e) { window.__job.errors.push(`${id}:${e}`); }
      window.__job.done++;
      await sleep(600);
    }
    window.__job.finished = true;
  };

  // Hand data to disk: triggers a download; save_dialog.ps1 answers the Save As dialog.
  const download = (name, obj) => {
    const b = new Blob([JSON.stringify(obj)], { type: 'application/json' });
    const a = document.createElement('a');
    a.href = URL.createObjectURL(b); a.download = name;
    document.body.appendChild(a); a.click(); a.remove();
    return b.size;
  };

  window.__xdom = { extract, visible, go, collectList, readStatus, job, download, sleep };
  return 'x_dom ready';
})();
