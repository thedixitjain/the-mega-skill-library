---
name: retellai-multi-env-setup
description: "\"Retell AI multi env setup \\u2014 AI voice agent and phone call automation.\\n\\ Use when working with Retell AI for voice agents, phone calls, or telephony.\\nTrigger\\ \\ with phrases like \\\"retell multi env setup\\\", \\\"retellai-multi-env-setup\\\", \\\"\\ voice agent\\\".\\n\""
allowed-tools: "Read, Write, Edit, Bash(npm:*), Bash(curl:*), Grep"
category: ai-agents-and-harness
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "skills/.curated/retellai-multi-env-setup/SKILL.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/skills/.curated/retellai-multi-env-setup/SKILL.md
---

# Retell AI Multi Env Setup

## Overview

Implementation patterns for Retell AI multi env setup — voice agent and telephony platform.

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

- Retell AI integration for multi env setup

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

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `skills/.curated/retellai-multi-env-setup/SKILL.md`

**Also appears in:** `jeremylongshore/claude-code-plugins-plus-skills/plugins/saas-packs/retellai-pack/skills/retellai-multi-env-setup/SKILL.md`
