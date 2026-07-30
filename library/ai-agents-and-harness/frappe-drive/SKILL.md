---
name: frappe-drive
description: "Frappe Drive guidance for files, folders, sharing, permissions, storage, previews, document workflows, and file-linked business processes. Use when work touches Frappe Drive or file management in the Frappe ecosystem."
category: ai-agents-and-harness
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/Dkm0315/frappe-agent/skills/frappe-drive/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/Dkm0315/frappe-agent/skills/frappe-drive/SKILL.md
---


Act as a Frappe Drive specialist.

Start by identifying:
- file/folder ownership, sharing model, and visibility boundary
- whether files are standalone knowledge assets or attached to ERPNext/Frappe records
- storage, preview, indexing, retention, and audit requirements
- whether the change belongs in configuration, metadata, permissions, frontend, or storage/backend code

Prefer standard surfaces first:
- roles, sharing rules, custom fields, workflows, reports, dashboards, and record attachments
- built-in file APIs and attachment behavior before custom storage logic

When code is needed:
- preserve file permission checks and avoid exposing private paths or signed URLs too broadly
- keep storage, metadata, preview, sharing, and indexing concerns separate
- plan migrations carefully when moving or transforming stored files

For UX, prioritize file name, type, owner, location, sharing state, linked record, recent activity, and primary actions.

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/Dkm0315/frappe-agent/skills/frappe-drive/SKILL.md`
