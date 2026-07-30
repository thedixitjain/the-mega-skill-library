---
name: retellai-incident-runbook
description: "\"Retell AI incident runbook \\u2014 AI voice agent and phone call automation.\\n\\ Use when working with Retell AI for voice agents, phone calls, or telephony.\\nTrigger\\ \\ with phrases like \\\"retell incident runbook\\\", \\\"retellai-incident-runbook\\\",\\ \\ \\\"voice agent\\\".\\n\""
allowed-tools: "Read, Write, Edit, Bash(npm:*), Bash(curl:*), Grep"
category: engineering-core
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "skills/.curated/retellai-incident-runbook/SKILL.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/skills/.curated/retellai-incident-runbook/SKILL.md
---

# Retell AI Incident Runbook

## Overview

Implementation patterns for Retell AI incident runbook — voice agent and telephony platform.

## Prerequisites

- Completed `retellai-install-auth` setup

## Instructions

### Step 1: SDK Pattern

```typescript
import Retell from 'retell-sdk';
const retell = new Retell({ apiKey: process.env.RETELL_API_KEY! });

const agents = await retell.agent.list();
console.log(`Agents: ${agents.length}`);
```

## Output

- Retell AI integration for incident runbook

## Error Handling

| Error | Cause | Solution |
|-------|-------|----------|
| 401 Unauthorized | Invalid API key | Check RETELL_API_KEY |
| 429 Rate Limited | Too many requests | Implement backoff |
| 400 Bad Request | Invalid parameters | Check API documentation |

## Resources

- [Retell AI Documentation](https://docs.retellai.com)
- [retell-sdk npm](https://www.npmjs.com/package/retell-sdk)

## Next Steps

See related Retell AI skills for more workflows.

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `skills/.curated/retellai-incident-runbook/SKILL.md`

**Also appears in:** `jeremylongshore/claude-code-plugins-plus-skills/plugins/saas-packs/retellai-pack/skills/retellai-incident-runbook/SKILL.md`
