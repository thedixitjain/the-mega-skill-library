---
name: repair
description: "Safe maintenance for an existing docflow setup: regenerate INDEX.md, install missing helpers, check links, report placeholders. Use after adding/renaming docs or when doctor recommends repair."
category: docs-and-knowledge-mgmt
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/MedAdemBHA/docflow/skills/repair/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/MedAdemBHA/docflow/skills/repair/SKILL.md
---


# repair

Goal: safe generated-file maintenance only.

## Run

```bash
bash scripts/docflow-repair.sh --target <REPO ROOT>
```

## It May Change

- `<DOCS_ROOT>/INDEX.md`
- missing helper scripts under `scripts/`

## It Must Not Change

- README content
- product specs
- ADRs
- changelog months
- roadmap/plans
- existing project docs

Report broken links, placeholders, and validation warnings instead of fixing content unless the user asks.

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/MedAdemBHA/docflow/skills/repair/SKILL.md`
