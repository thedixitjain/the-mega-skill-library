---
name: retellai-install-auth
description: "\"Retell AI install auth \\u2014 AI voice agent and phone call automation.\\n\\ Use when working with Retell AI for voice agents, phone calls, or telephony.\\nTrigger\\ \\ with phrases like \\\"retell install auth\\\", \\\"retellai-install-auth\\\", \\\"voice\\ \\ agent\\\".\\n\""
allowed-tools: "Read, Write, Edit, Bash(npm:*), Bash(curl:*), Grep"
category: ai-agents-and-harness
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "skills/.curated/retellai-install-auth/SKILL.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/skills/.curated/retellai-install-auth/SKILL.md
---

# Retell AI Install Auth

## Overview

Install the Retell AI SDK and configure API key authentication for building voice agents.

## Prerequisites

- Retell AI account at retellai.com
- API key from the Retell AI dashboard
- Node.js 18+ or Python 3.9+

## Instructions

### Step 1: Install SDK

```bash
set -euo pipefail
# Node.js
npm install retell-sdk

# Python
pip install retell-sdk
```

### Step 2: Configure Environment

```bash
# .env
RETELL_API_KEY=key_xxxxxxxxxxxxxxxxxxxxxxxx
```

### Step 3: Initialize Client (Node.js)

```typescript
import Retell from 'retell-sdk';

const retell = new Retell({ apiKey: process.env.RETELL_API_KEY! });

// Verify connection — list agents
const agents = await retell.agent.list();
console.log(`Connected! ${agents.length} agent(s) configured.`);
```

### Step 4: Initialize Client (Python)

```python
from retell import Retell
import os

retell = Retell(api_key=os.environ["RETELL_API_KEY"])
agents = retell.agent.list()
print(f"Connected! {len(agents)} agent(s) configured.")
```

## Output

- `retell-sdk` installed
- API key configured
- Connection verified with agent listing

## Error Handling

| Error | Cause | Solution |
|-------|-------|----------|
| `401 Unauthorized` | Invalid API key | Verify key in Retell Dashboard |
| `ModuleNotFoundError` | SDK not installed | `npm install retell-sdk` |
| Connection timeout | Network issue | Check firewall allows HTTPS |

## Resources

- [Retell AI SDKs](https://docs.retellai.com/get-started/sdk)
- [retell-sdk npm](https://www.npmjs.com/package/retell-sdk)

## Next Steps

Create your first agent: `retellai-hello-world`

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `skills/.curated/retellai-install-auth/SKILL.md`

**Also appears in:** `jeremylongshore/claude-code-plugins-plus-skills/plugins/saas-packs/retellai-pack/skills/retellai-install-auth/SKILL.md`
