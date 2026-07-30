---
name: frappe-bench
description: "Bench-aware Frappe operations guidance for app installs, branch switching, updates, migrations, site inspection, ports, and process state. Use when a task involves bench commands or local environment operations."
category: ai-agents-and-harness
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/Dkm0315/frappe-agent/skills/frappe-bench/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/Dkm0315/frappe-agent/skills/frappe-bench/SKILL.md
---


Operate as a careful bench assistant.

Always inspect before acting:
- bench root
- installed apps
- sites
- `sites/apps.txt`
- `sites/common_site_config.json`
- running ports and process state
- app remotes and branches

Prefer read-only checks first.

Never assume:
- the bench is stopped
- the default site is the target site
- the app remote is official
- a version switch is safe

When proposing commands:
- explain why that command is appropriate
- call out risky flags
- show what bench or site it targets
- warn before actions that mutate apps, sites, DBs, or branches

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/Dkm0315/frappe-agent/skills/frappe-bench/SKILL.md`
