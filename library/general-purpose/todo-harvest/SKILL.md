---
name: todo-harvest
description: "List TODO/FIXME/HACK comments with author + age in days"
allowed-tools: "Bash"
category: general-purpose
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/mturac/todo-harvest/skills/todo-harvest/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/mturac/todo-harvest/skills/todo-harvest/SKILL.md
---


Role: act as a debt-triage assistant. Surface the oldest, highest-cost TODOs first.

Run the helper:

```bash
python3 scripts/harvest.py --format md
```

Useful flags: `--markers TODO,FIXME,HACK`, `--min-age 90`, `--format json`.

The helper uses `git ls-files` (respecting .gitignore) and runs `git blame` per match for author + age. Read the table, then propose a short triage list: which TODOs are stale enough to delete, which need owners, which look like real bugs. Be specific — quote the file and line.

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/mturac/todo-harvest/skills/todo-harvest/SKILL.md`
