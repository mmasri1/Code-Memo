---
title: "New Page Guide (Internal)"
exclude_from_pages_json: true
---

# Internal: How to write a new page in Code-Memo

This file is **for AI agents and contributors** to produce new pages that match this repo’s conventions.

- This file is **internal** and should **not** be linked from `README.md` or `index.md`.
- This file is excluded from `pages.json` (random-page button) via `exclude_from_pages_json: true` and by being inside `_internal/`.

---

## What this repo is (tone + goal)

Code-Memo is a **personal notes** repo meant for **fast recall**, not long-form teaching.

- **Write for scanning**: short sections, bullets, crisp sentences.
- **Prefer practical**: what to do, common pitfalls, quick examples.
- **Assume some context**: you can reference concepts without fully re-teaching them.

---

## Where to put new pages

Place the file under the most relevant section folder:

- `python/…`
- `django/…`
- `drf/…`
- `dsa/…`
- `leetcode/…`
- `systemdesign/…`
- `misc/…`
- `aws/…`

If the page is a section index (a list of links), it can live at the top level like `python.md` / `django.md`.

---

## File naming conventions

Use lowercase and hyphens:

- Good: `django/query-optimization.md`
- Good: `misc/sql-transactions.md`
- Avoid: spaces, camelCase, extra punctuation

Keep names descriptive and stable (don’t rename unless necessary).

---

## Link conventions (important)

Most pages link like this:

- Use **relative links** (no leading `/`).
- Link to the rendered path (omit the `.md` extension).

Examples:

- `[QuerySets](django/querysets)`
- `[Topic 1](python/topic-1)`

Do **not** link to generated `.html` paths; GitHub Pages/Jekyll will handle rendering.

---

## Recommended page structure (default)

Use this structure unless the topic strongly suggests a different one.

### 1) Title

Start with a single clear title:

- Prefer `## Title` for most note pages.
- Use `# Title` only when the file is a section landing page (some existing ones do this, e.g. `django.md`).

### 2) Short intro (2–5 lines)

- What the thing is
- When you would use it
- 1 gotcha or rule of thumb

### 3) Main content as scan-friendly sections

Use headings, bullets, and short paragraphs:

- `##` for main sections
- `###` for subsections

### 4) Examples

Include at least one example when it helps.

- Prefer minimal examples that prove the point.
- Use fenced code blocks with a language tag.

### 5) Pitfalls / trade-offs

Have a dedicated section when useful:

- `## Common trade-offs`
- `## trade-offs`
- `## Mistakes I keep making`

---

## Markdown style rules

- **Headings**:
  - Don’t skip levels (e.g. don’t jump from `##` to `####`).
  - Keep headings short and specific.
- **Lists**:
  - Prefer bullets for recall.
  - Use numbered lists for procedures/steps.
- **Code**:
  - Inline code: use backticks, e.g. `select_related`.
  - Blocks: always fenced with language, e.g. ```python, ```sql, ```bash.
- **No parentheses**:
  - Avoid using parentheses `(...)` in sentences/bullets (write the note without asides in parentheses).
- **Spacing**:
  - Add a blank line before and after lists and code blocks.
  - Use `<br>` sparingly (this repo uses it sometimes; it’s okay when it improves readability).
- **Tables**:
  - OK when they improve scanning (see `system-design.md` for precedent).
- **Emphasis**:
  - Use **bold** for key terms and rules of thumb.
  - Don’t overuse emojis; a couple is fine but keep it readable.

---

## Content quality bar (what good looks like here)

- **Actionable**: includes commands, snippets, or concrete rules.
- **Opinionated**: clearly states recommended default choices.
- **Compact**: avoids overly long narratives.
- **Accurate**: don’t invent APIs; prefer verified syntax.

---

## New page template (copy/paste)

Use the template below to create a new page quickly.

```markdown
## <Topic title>

<2–5 lines: what it is, when to use it, one key rule/gotcha.>

## When to use it

- <bullet>
- <bullet>

## Core idea

- **Rule of thumb**: <one-liner>
- <bullet>

## Example

```<lang>
<minimal example>
```

## Common trade-offs

- <pitfall + fix>
- <pitfall + fix>

## Quick checklist

- [ ] <check>
- [ ] <check>
```

---

## Instructions for AI agents (prompt block)

When asked write about topic X for this repo, follow this checklist:

1. Put the page in the **right folder** and name it with **kebab-case**.
2. Use the **template structure** above.
3. Use **relative links** like `django/foo` when referencing other notes.
4. Keep it **scan-first**: short sections, bullets, minimal examples.
5. Don’t add this guide to any index pages.

