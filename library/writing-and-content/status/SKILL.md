---
name: status
description: "Summarize the active Maestro session without mutating state"
category: writing-and-content
source_repo: josstei/maestro-orchestrate
source_path: "claude/skills/status/SKILL.md"
source_url: https://github.com/josstei/maestro-orchestrate/blob/HEAD/claude/skills/status/SKILL.md
---



# Maestro Status

Call `get_skill_content` with resources: ["architecture"].


## Workflow

1. Read the active session using MCP state tools if available; otherwise fall back to scripts or direct file read
2. Report session ID, creation timestamp, workflow mode, and overall status
3. Show phase breakdown: completed phases with timestamps, current active phase, pending phases, and failed phases with error summaries
4. Report file manifest (files created, modified, deleted), token usage by agent, and unresolved errors

## Constraints

- This is read-only; do not mutate state, archive sessions, or continue execution
- If no active session exists, say so plainly

---

**Source:** [`josstei/maestro-orchestrate`](https://github.com/josstei/maestro-orchestrate) → `claude/skills/status/SKILL.md`
