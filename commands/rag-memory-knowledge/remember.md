---
name: remember
description: "Manually add something to project memory"
category: rag-memory-knowledge
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "plugins/community/claude-never-forgets/commands/remember.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/plugins/community/claude-never-forgets/commands/remember.md
---

Add to `.claude/memories/project_memory.json` in `manual_memories` array:

```json
{"type": "manual", "content": "$ARGUMENTS", "added_at": "<timestamp>", "source": "user_command"}
```

Confirm: `✓ Remembered: "$ARGUMENTS"`

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `plugins/community/claude-never-forgets/commands/remember.md`
