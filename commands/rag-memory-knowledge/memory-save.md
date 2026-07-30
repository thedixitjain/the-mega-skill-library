---
name: memory-save
description: "Save current session context to MEMORY.md before compaction or session end"
category: rag-memory-knowledge
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "plugins/productivity/claude-memory-kit/commands/memory-save.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/plugins/productivity/claude-memory-kit/commands/memory-save.md
---


Save the current session context to MEMORY.md.

1. Read `tasks/current-task.md` if it exists
2. Collect from the current session:
   - Active goals and tasks
   - Decisions made (with rationale)
   - Patterns discovered
   - Open questions
   - Concrete next steps
3. Write to MEMORY.md using the template from the memory-kit skill's `references/output-format.md`
4. Confirm: "Memory saved to MEMORY.md. N items captured."

If MEMORY.md already exists, overwrite it with the fresh snapshot.

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `plugins/productivity/claude-memory-kit/commands/memory-save.md`
