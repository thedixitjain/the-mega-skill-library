---
name: frappe-backend
description: "Frappe backend guidance for Python and backend-adjacent JavaScript surfaces such as client interaction patterns, hooks, APIs, patches, scheduler logic, reports, and server-side review. Use when implementing or reviewing Frappe backend behavior."
category: backend-and-data
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/Dkm0315/frappe-agent/skills/frappe-backend/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/Dkm0315/frappe-agent/skills/frappe-backend/SKILL.md
---


Treat Frappe backend work as a Python-first system with important JavaScript touchpoints.

Cover:
- controllers and document lifecycle methods
- hooks
- whitelisted methods
- scheduler jobs and background work
- patches and migrations
- server scripts when they are the right layer
- report backends
- client-to-server API contracts

Principles:
- prefer framework APIs over ad hoc patterns
- keep imports clean and explicit
- use permissions deliberately
- separate document logic, service logic, and integration logic
- avoid accidental public APIs

Before writing code, decide whether the request should instead be handled by:
- `Custom Field`
- `Property Setter`
- `Client Script`
- `Server Script`
- `Workflow`
- `Report`
- `Workspace`

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/Dkm0315/frappe-agent/skills/frappe-backend/SKILL.md`
