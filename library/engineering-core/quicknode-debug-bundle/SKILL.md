---
name: quicknode-debug-bundle
description: "\"QuickNode debug bundle \\u2014 blockchain RPC and Web3 infrastructure\\ \\ integration.\\nUse when working with QuickNode for blockchain development.\\nTrigger\\ \\ with phrases like \\\"quicknode debug bundle\\\", \\\"quicknode-debug-bundle\\\", \\\"blockchain\\ \\ RPC\\\".\\n\""
allowed-tools: "Read, Write, Edit, Bash(npm:*), Bash(curl:*), Grep"
category: engineering-core
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "skills/.curated/quicknode-debug-bundle/SKILL.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/skills/.curated/quicknode-debug-bundle/SKILL.md
---

# QuickNode Debug Bundle

## Overview

Implementation patterns for QuickNode debug bundle using blockchain RPC endpoints and the QuickNode SDK.

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

- QuickNode integration for debug bundle

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

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `skills/.curated/quicknode-debug-bundle/SKILL.md`

**Also appears in:** `jeremylongshore/claude-code-plugins-plus-skills/plugins/saas-packs/quicknode-pack/skills/quicknode-debug-bundle/SKILL.md`
