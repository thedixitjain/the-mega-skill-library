---
name: book-status
description: "Book project status and progress dashboard. Writes status.json for the web UI."
allowed-tools: "Bash(node), Read, Write"
model: "haiku"
category: frontend-and-design
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/epicsagas/Velith/skills/book-status/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/epicsagas/Velith/skills/book-status/SKILL.md
---


# Book Status

Run: `node {PLUGIN_ROOT}/velith.mjs scan [dir] [--ui] --plugin-root={PLUGIN_ROOT}`

Outputs: `{dir}/.velith/status.json`, `~/.velith/projects.json`, terminal ASCII dashboard.

`--ui` opens browser dashboard at `http://localhost:9631/{index}/overview`.

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/epicsagas/Velith/skills/book-status/SKILL.md`
