---
name: forget
description: "Remove something from project memory"
category: rag-memory-knowledge
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "plugins/community/claude-never-forgets/commands/forget.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/plugins/community/claude-never-forgets/commands/forget.md
---

Read `.claude/memories/project_memory.json`, find and remove entries matching "$ARGUMENTS" from `manual_memories` or `realtime_memories`.

Confirm: `✓ Forgot: "<matched>"`

If not found: `No memory found matching "$ARGUMENTS". Use /memories to see all.`

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `plugins/community/claude-never-forgets/commands/forget.md`
