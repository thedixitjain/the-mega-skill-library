---
name: status
description: "Summarize the active Maestro session without mutating state"
category: writing-and-content
source_repo: josstei/maestro-orchestrate
source_path: "plugins/maestro/skills/status/SKILL.md"
source_url: https://github.com/josstei/maestro-orchestrate/blob/HEAD/plugins/maestro/skills/status/SKILL.md
---


Read `../../references/runtime-guide.md`.
Call `get_skill_content` with resources: ["architecture", "session-management"].

## Workflow

1. Read the active session using MCP state tools if available; otherwise fall back to scripts or direct file read
2. Report session ID, creation timestamp, workflow mode, and overall status
3. Show phase breakdown: completed phases with timestamps, current active phase, pending phases, and failed phases with error summaries
4. Report file manifest (files created, modified, deleted), token usage by agent, and unresolved errors

---

**Source:** [`josstei/maestro-orchestrate`](https://github.com/josstei/maestro-orchestrate) → `plugins/maestro/skills/status/SKILL.md`
