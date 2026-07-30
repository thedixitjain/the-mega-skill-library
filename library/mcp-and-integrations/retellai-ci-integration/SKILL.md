---
name: retellai-ci-integration
description: "\"Retell AI ci integration \\u2014 AI voice agent and phone call automation.\\n\\ Use when working with Retell AI for voice agents, phone calls, or telephony.\\nTrigger\\ \\ with phrases like \\\"retell ci integration\\\", \\\"retellai-ci-integration\\\", \\\"voice\\ \\ agent\\\".\\n\""
allowed-tools: "Read, Write, Edit, Bash(npm:*), Bash(curl:*), Grep"
category: mcp-and-integrations
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "skills/.curated/retellai-ci-integration/SKILL.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/skills/.curated/retellai-ci-integration/SKILL.md
---

# Retell AI Ci Integration

## Overview

Implementation patterns for Retell AI ci integration — voice agent and telephony platform.

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

- Retell AI integration for ci integration

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

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `skills/.curated/retellai-ci-integration/SKILL.md`

**Also appears in:** `jeremylongshore/claude-code-plugins-plus-skills/plugins/saas-packs/retellai-pack/skills/retellai-ci-integration/SKILL.md`
