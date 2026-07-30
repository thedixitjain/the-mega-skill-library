---
name: quicknode-local-dev-loop
description: "\"QuickNode local dev loop \\u2014 blockchain RPC and Web3 infrastructure\\ \\ integration.\\nUse when working with QuickNode for blockchain development.\\nTrigger\\ \\ with phrases like \\\"quicknode local dev loop\\\", \\\"quicknode-local-dev-loop\\\",\\ \\ \\\"blockchain RPC\\\".\\n\""
allowed-tools: "Read, Write, Edit, Bash(npm:*), Bash(curl:*), Grep"
category: devops-and-infra
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "skills/.curated/quicknode-local-dev-loop/SKILL.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/skills/.curated/quicknode-local-dev-loop/SKILL.md
---

# QuickNode Local Dev Loop

## Overview

Implementation patterns for QuickNode local dev loop using blockchain RPC endpoints and the QuickNode SDK.

## Prerequisites

- Completed `quicknode-install-auth` setup

## Instructions

### Step 1: Connect to QuickNode

```typescript
import { ethers } from 'ethers';
const provider = new ethers.JsonRpcProvider(process.env.QUICKNODE_ENDPOINT);
const block = await provider.getBlockNumber();
console.log(`Connected at block ${block}`);
```

## Output

- QuickNode integration for local dev loop

## Error Handling

| Error | Cause | Solution |
|-------|-------|----------|
| 401 Unauthorized | Invalid endpoint token | Verify URL from Dashboard |
| Rate limited | Too many requests | Implement backoff or upgrade plan |
| Method not found | Add-on required | Enable in QuickNode Dashboard |

## Resources

- [QuickNode Docs](https://www.quicknode.com/docs/welcome)
- [Ethereum API](https://www.quicknode.com/docs/ethereum)

## Next Steps

See related QuickNode skills for more workflows.

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `skills/.curated/quicknode-local-dev-loop/SKILL.md`

**Also appears in:** `jeremylongshore/claude-code-plugins-plus-skills/plugins/saas-packs/quicknode-pack/skills/quicknode-local-dev-loop/SKILL.md`
