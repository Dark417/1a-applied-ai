# Readable-version style spec (strong bullet style)

You are turning one X (Twitter) post, thread, or long-form X Article into a **readable, bulleted version** for a personal study notebook. The reader wants to study the full content quickly. This is NOT a summary — every substantive point must survive — but it is restructured, not copied.

## Output
- Write exactly one file per post: `0x/_sync/data/readable/<ID>.md`
- Markdown fragment only. No `#` headings of any level (the fragment is embedded under an existing heading). No front matter. No intro/outro from you.
- UTF-8. Nested bullets use **2 spaces** per level. Max 3 levels deep.

## Language
- Keep the post's original language. Chinese stays Chinese, English stays English. Do not translate. Keep English technical terms as-is inside Chinese text.

## Structure rules
- Section headings in the source → a bold top-level bullet: `- **Phase 1: Master the Loop First**`, with that section's content as sub-bullets.
- Every paragraph → one or more bullets. One idea per bullet. Break long sentences into short ones.
- Parallel items (lists, steps, options, pros/cons) → each on its own bullet; numbered steps keep their numbers (`- **Step 3 ·** ...` or `1.` style is fine).
- Layered ideas (claim → reason → example) → parent bullet + indented sub-bullets.
- Use **bold** for key terms and the one-line takeaway of a section. Use `code` for commands, file names, identifiers.
- Short posts (a few sentences): just 2–6 clean bullets. Don't pad.
- Threads: treat `[thread N]` parts as continuation of the same text; no need to label them unless the split matters.
- A quoted post (QUOTED POST) → a final bullet `- **引用 / Quoted:** ...` with its points as sub-bullets.

## Keep (never drop)
- All facts, numbers, names, steps, definitions, comparisons, warnings, examples.
- All URLs, written in full (e.g. `https://github.com/org/repo`). If the source shows a shortened `github.com/foo…`, keep what is visible.
- Code: reconstruct into fenced code blocks with a language tag (` ```python `). X's article export flattens code into plain lines (often preceded by a lone `python`/`markdown`/`bash` line) — put those lines back into a fenced block, preserving content and indentation as best you can. Place the fence as a sub-item under the bullet it belongs to (indent the fence 2 spaces) or at top level between bullets.
- Tables / metric lists → a markdown table if clearly tabular, else bullets.
- Prompts/templates shown verbatim in the source → keep verbatim in a fenced block (```text).

## Drop
- Engagement bait and self-promotion: "Save this", "Bookmark", "Follow me / my Substack", "hope this was useful", "reposts appreciated", "DM me", newsletter plugs, repeated hype ("This beats any $500 course").
- Pure filler and rhetorical repetition. Image placeholders.

## Example
Source:
> Most people use AI at one speed: ask, read, fix, ask again. It works. It's also the slowest way to do it. There is a faster setup. It has three parts: an agent that plans and acts, a loop that runs until the work clears the bar, and a graph of parallel workers. Claude runs all three.

Output:
```
- **Most people use AI at one speed**: ask → read → fix → ask again
  - It works, but it is the slowest way
- **The faster setup has three parts**
  - **Agent** — plans and acts without step-by-step guidance
  - **Loop** — runs until the work clears the bar
  - **Graph** — parallel workers for what one prompt can't handle
- Claude can run all three
```
