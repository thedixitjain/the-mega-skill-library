---
name: book-ideation
description: "Phase 1: Ideation. Concept validation, market gap analysis, competitive matrix, final concept selection."
category: general-purpose
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/epicsagas/Velith/skills/book-ideation/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/epicsagas/Velith/skills/book-ideation/SKILL.md
---


# Phase 1: Ideation

Generate 5-10 concepts from PRD + sources. Each: elevator pitch, target reader, differentiation, scope, difficulty.

**Market Gap Analysis**: existing coverage → gaps → market shifts → reader complaints. Analyze 5+ competing books in matrix (title, author, topic, differentiator, gap we fill).

**Validation**: clarity (1 sentence?) · reader value · differentiation · feasibility · timeliness · scope

Present to user → select ≤3 → merge → confirm single concept.

Output: `ideation.md` (pitch, competitive matrix, gap summary, rationale).

Gate: ideation.md exists, 5+ competitors analyzed, user approved.


## Post-Completion

Update the project dashboard status:

```bash
node {PLUGIN_ROOT}/velith.mjs scan [project-dir] --plugin-root={PLUGIN_ROOT}
```

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/epicsagas/Velith/skills/book-ideation/SKILL.md`
