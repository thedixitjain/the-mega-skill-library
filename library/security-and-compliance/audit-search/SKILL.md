---
name: audit-search
description: "Search AxonFlow audit trail for recent tool executions, policy decisions, and compliance evidence"
category: security-and-compliance
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/getaxonflow/axonflow-codex-plugin/skills/audit-search/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/getaxonflow/axonflow-codex-plugin/skills/audit-search/SKILL.md
---


Call the `search_audit_events` MCP tool. Optionally provide:

- `from`: start time (ISO 8601, defaults to last 15 minutes)
- `to`: end time (ISO 8601, defaults to now)
- `limit`: max events to return (default 20, max 100)
- `request_type`: filter by type (e.g., `tool_call_audit`, `llm_call`)

Present results as a summary table with timestamp, tool name, decision, and key details.

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/getaxonflow/axonflow-codex-plugin/skills/audit-search/SKILL.md`
