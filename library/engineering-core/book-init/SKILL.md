---
name: book-init
description: "Phase 0: Onboarding. Initialize new book project — define genre, audience, language, scope, generate PRD.md and STYLE.md."
category: engineering-core
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/epicsagas/Velith/skills/book-init/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/epicsagas/Velith/skills/book-init/SKILL.md
---


# Phase 0: Onboarding

Max 3 questions per round, max 3 rounds.

**R1** — Genre (fiction/non-fiction/technical) · Audience (1-2 personas) · Language
**R2** — Scale (5-15 chapters, word count) · Timeline · Existing materials
**R3** — Voice (conversational/academic/narrative) · Tone · Special requirements

Source scan if materials confirmed: `find` vault + alcove `search_project_docs`/`search_vault` in parallel.

Outputs:
- `PRD.md` — genre, language, reader, scale, timeline, source map, success criteria
- `STYLE.md` — voice/tone, language rules, formatting, prohibited patterns
- `drafts/` `edits/` `publish/` `sources/` directories

Gate: PRD.md + STYLE.md exist, source map has 3+ items.

**Poetry note**: For poetry/poetry-essay genres, STYLE.md line targets per poem should be 20-80 lines (not the default 10-30). Word/character targets in PRD.md should reflect total poem count × average length rather than a flat word count.


## Post-Completion

Update the project dashboard status:

```bash
node {PLUGIN_ROOT}/velith.mjs scan [project-dir] --plugin-root={PLUGIN_ROOT}
```

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/epicsagas/Velith/skills/book-init/SKILL.md`
