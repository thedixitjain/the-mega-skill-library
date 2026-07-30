---
name: federation-audit
description: "Query federation audit logs with compliance filtering"
allowed-tools: "Bash(npx *) mcp__plugin_ruflo-core_ruflo__memory_search Read Grep"
category: security-and-compliance
source_repo: ruvnet/ruflo
source_path: "plugins/ruflo-federation/skills/federation-audit/SKILL.md"
source_url: https://github.com/ruvnet/ruflo/blob/HEAD/plugins/ruflo-federation/skills/federation-audit/SKILL.md
---

Query structured federation audit logs. Supports compliance mode filtering (HIPAA, SOC2, GDPR) and severity filtering.

Steps:
1. Parse compliance mode, date range, and severity from arguments
2. `npx -y -p @claude-flow/plugin-agent-federation@latest ruflo-federation audit --compliance MODE --since DATE --severity LEVEL`
3. Summarize findings: total events, PII detections, threat blocks, trust changes
4. Highlight any critical or error-severity events

| Compliance Mode | What's Logged |
|----------------|---------------|
| HIPAA | Full audit trail, no PII in logs, PHI detection, 6-year retention |
| SOC2 | Access control events, change management, availability monitoring |
| GDPR | Data processing records, consent tracking, right to erasure, data residency |

---

**Source:** [`ruvnet/ruflo`](https://github.com/ruvnet/ruflo) → `plugins/ruflo-federation/skills/federation-audit/SKILL.md`
