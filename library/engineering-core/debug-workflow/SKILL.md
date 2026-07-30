---
name: debug-workflow
description: "Run the Maestro debugging workflow for investigation-heavy tasks"
category: engineering-core
source_repo: josstei/maestro-orchestrate
source_path: "claude/skills/debug-workflow/SKILL.md"
source_url: https://github.com/josstei/maestro-orchestrate/blob/HEAD/claude/skills/debug-workflow/SKILL.md
---



# Maestro Debug Workflow

Call `get_skill_content` with resources: ["architecture"].

## Protocol

Before delegating, call `get_skill_content` with resources: ["delegation"] and follow the returned methodology.

## Workflow

1. Establish the failing behavior, repro path, and expected behavior
2. Form concrete hypotheses (2-3 likely root causes)
3. Gather evidence from code, logs, tests, and runtime behavior before proposing fixes
4. Isolate the most likely root cause and trace the execution path from trigger to failure
5. Verify the conclusion explains all symptoms and present the recommended fix with specific code location

## Constraints

- Prefer evidence over speculation
- Make uncertainty explicit when the issue cannot be reproduced
- Return root cause, affected files, confidence level, and the smallest defensible next action

---

**Source:** [`josstei/maestro-orchestrate`](https://github.com/josstei/maestro-orchestrate) → `claude/skills/debug-workflow/SKILL.md`
