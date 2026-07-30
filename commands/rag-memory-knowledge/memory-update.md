---
name: memory-update
description: "Log a decision or pattern mid-session to MEMORY.md"
category: rag-memory-knowledge
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "plugins/productivity/claude-memory-kit/commands/memory-update.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/plugins/productivity/claude-memory-kit/commands/memory-update.md
---


Log a decision, pattern, or note to MEMORY.md without a full save.

1. If the user didn't specify what to log, ask: decision, pattern, or note?
2. Append to MEMORY.md under the relevant section (create section if missing)
3. Add an ISO 8601 timestamp to the entry
4. Confirm: "Logged to MEMORY.md: [brief description]"

If MEMORY.md doesn't exist, create it with proper section structure first, then append.

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `plugins/productivity/claude-memory-kit/commands/memory-update.md`
