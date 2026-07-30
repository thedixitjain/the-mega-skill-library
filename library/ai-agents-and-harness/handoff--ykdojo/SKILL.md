---
name: handoff
description: "Write or update a handoff document so the next agent with fresh context can continue this work."
category: ai-agents-and-harness
source_repo: ykdojo/claude-code-tips
source_path: "skills/handoff/SKILL.md"
source_url: https://github.com/ykdojo/claude-code-tips/blob/HEAD/skills/handoff/SKILL.md
---


Write or update a handoff document so the next agent with fresh context can continue this work.

Steps:
1. Check if HANDOFF.md already exists in the project
2. If it exists, read it first to understand prior context before updating
3. Create or update the document with:
   - **Goal**: What we're trying to accomplish
   - **Current Progress**: What's been done so far
   - **What Worked**: Approaches that succeeded
   - **What Didn't Work**: Approaches that failed (so they're not repeated)
   - **Next Steps**: Clear action items for continuing

Save as HANDOFF.md in the project root and tell the user the file path so they can start a fresh conversation with just that path.

---

**Source:** [`ykdojo/claude-code-tips`](https://github.com/ykdojo/claude-code-tips) → `skills/handoff/SKILL.md`
