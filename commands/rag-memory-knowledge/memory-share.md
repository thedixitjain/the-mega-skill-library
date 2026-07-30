---
name: memory-share
description: "Sync MEMORY.md to git so teammates can restore context"
category: rag-memory-knowledge
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "plugins/productivity/claude-memory-kit/commands/memory-share.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/plugins/productivity/claude-memory-kit/commands/memory-share.md
---


Sync MEMORY.md to git for team collaboration.

1. Run the share script:

   ```bash
   bash plugins/productivity/claude-memory-kit/skills/memory-kit/scripts/memory-share.sh
   ```

2. If the script succeeds, confirm the branch and timestamp
3. If it fails, report the error and suggest resolution

Teammates can then run `/memory-load` to pick up where you left off.

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `plugins/productivity/claude-memory-kit/commands/memory-share.md`
