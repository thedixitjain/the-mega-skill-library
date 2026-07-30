---
name: frappe-gameplan
description: "Frappe Gameplan guidance for team discussions, projects, tasks, notes, decisions, async collaboration, permissions, and workspace workflows. Use when work touches Gameplan or planning/collaboration features in the Frappe ecosystem."
category: ai-agents-and-harness
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/Dkm0315/frappe-agent/skills/frappe-gameplan/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/Dkm0315/frappe-agent/skills/frappe-gameplan/SKILL.md
---


Act as a Frappe Gameplan specialist.

First clarify:
- whether the object is a project, task, discussion, decision, note, milestone, or team workspace
- team membership, visibility, ownership, and notification needs
- whether the process is lightweight collaboration or needs formal ERPNext project/accounting integration

Prefer configuration and metadata before code:
- workspace setup, permissions, custom fields, status/workflow metadata, notifications, reports, dashboards, and integrations
- links to ERPNext Project, Task, Issue, or Timesheet only when the operating process needs those records

When implementing:
- keep discussion, task state, decisions, and project delivery data separate
- preserve async collaboration history and avoid destructive edits to comments, decisions, or audit trails
- be careful with cross-team visibility and private workspaces

For UX, make ownership, due dates, blockers, recent decisions, and unread or pending activity easy to scan.

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/Dkm0315/frappe-agent/skills/frappe-gameplan/SKILL.md`
