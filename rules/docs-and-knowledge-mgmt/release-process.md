---
name: release-process
description: "Release the compressed rule sets from rule-workbench/ into the main repository without losing traceability or making the README drift from the actual files."
category: docs-and-knowledge-mgmt
source_repo: ciembor/agent-rules-books
source_path: "_rule-workbench/RELEASE.md"
source_url: https://github.com/ciembor/agent-rules-books/blob/HEAD/_rule-workbench/RELEASE.md
---
# Release Process

## Goal

Release the compressed rule sets from `_rule-workbench/` into the main repository without losing traceability or making the README drift from the actual files.

## Target layout

For each book:

- keep the current canonical full file as-is:
  - `<book>/<book>.md`
- copy the compressed release files from the workbench into the book directory:
  - `_rule-workbench/<book>/mini.md` -> `<book>/<book>.mini.md`
  - `_rule-workbench/<book>/nano.md` -> `<book>/<book>.nano.md`

`traceability.md` and `full.md` stay in `_rule-workbench/` and are not part of the released public surface by default.

## Release steps

### 1. Validate the workbench

Before copying anything:

- every book must have `full.md`, `traceability.md`, `mini.md`, and `nano.md`
- `full.md` must still resolve to the canonical source file
- `mini.md` and `nano.md` must follow the structure from `PROCESS.md`
- `nano.md` must stay small enough for compact always-on fallback use
- `traceability.md` must map retained rules back to the full source

### 2. Add or update repository `README.md`

The repository README must contain a table with:

- one row per book
- grouped columns for `full`, `mini`, and `nano`
- for each version:
  - line count
  - rule count
  - file size
  - file link

Recommended columns:

| Book | Full file | Full lines | Full rules | Full size | Mini file | Mini lines | Mini rules | Mini size | Nano file | Nano lines | Nano rules | Nano size |
| --- | --- | ---: | ---: | ---: | --- | ---: | ---: | ---: | --- | ---: | ---: | ---: |

Recommended link targets:

- full: `<book>/<book>.md`
- mini: `<book>/<book>.mini.md`
- nano: `<book>/<book>.nano.md`

### 3. Copy files into the repository

For each book:

- keep `<book>/<book>.md` unchanged as the full version
- copy `_rule-workbench/<book>/mini.md` to `<book>/<book>.mini.md`
- copy `_rule-workbench/<book>/nano.md` to `<book>/<book>.nano.md`

After copying:

- verify that every README link resolves
- verify that metrics in README match the actual released files
- verify that no workbench-only file leaked into the release surface by accident

## Metric rules

Use deterministic metrics so README stays reproducible.

### Line count

- count physical lines in the released file
- use `wc -l`

### File size

- use raw bytes
- use `wc -c`

### Rule count

Use one deterministic rule-counting convention across all versions:

- count Markdown list items that represent actionable instructions
- include:
  - unordered list items starting with `- `
  - ordered list items like `1.`
- exclude:
  - headings
  - blank lines
  - prose paragraphs
  - code fences and code examples
  - table rows

For `mini.md` and `nano.md`, this corresponds to bullets under:

- `Decision rules`
- `Trigger rules`
- `Final checklist`

For `full` files, apply the same list-item counting rule consistently even if the prose density differs by book.

## Suggested release verification commands

Examples:

```bash
find _rule-workbench -maxdepth 2 -type f | sort
```

```bash
wc -l <book>/<book>.md <book>/<book>.mini.md <book>/<book>.nano.md
```

```bash
wc -c <book>/<book>.md <book>/<book>.mini.md <book>/<book>.nano.md
```

If you automate README generation later, keep the metric definitions above unchanged so historical releases remain comparable.

## Non-goals

- Do not edit the canonical full files during release.
- Do not treat `traceability.md` as public release content unless there is a separate decision to expose it.
- Do not change the metric definitions between releases without also updating this document and regenerating README consistently.

---

**Source:** [`ciembor/agent-rules-books`](https://github.com/ciembor/agent-rules-books) → `_rule-workbench/RELEASE.md`
