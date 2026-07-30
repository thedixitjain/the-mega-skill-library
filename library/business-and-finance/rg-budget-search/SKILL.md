---
name: rg-budget-search
description: "In large or many-file projects, prefer cxs over raw rg/grep to reduce context waste."
category: business-and-finance
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/Rycen7822/codex-rg-guard/skills/rg-budget-search/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/Rycen7822/codex-rg-guard/skills/rg-budget-search/SKILL.md
---


In large or many-file projects, use MCP `cxs(op,args)` or CLI `cxs` before raw `rg`/`grep`.

Default flow: `find(files_only:true)` to identify candidate files, `find(paths=[...])` to locate bounded line hits, then use Codex-native reads for the exact file or span.

Use `--path` or `paths` for concrete files/directories. Use `--scope` or `scopes` only for presets: `docs`, `src`, `tests`, `config`, `analysis`, `runs`, `vendor`, `all`.

For small projects, known files, or narrow checks, normal file reads/direct shell tools are fine. If output is `truncated`, refine query/scope/path or continue files-only pagination with `next_page.offset`.

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/Rycen7822/codex-rg-guard/skills/rg-budget-search/SKILL.md`
