---
name: no-task-output
description: "Never Use TaskOutput"
category: general-purpose
source_repo: parcadei/Continuous-Claude-v3
source_path: ".claude/skills/no-task-output/SKILL.md"
source_url: https://github.com/parcadei/Continuous-Claude-v3/blob/HEAD/.claude/skills/no-task-output/SKILL.md
---


# Never Use TaskOutput

TaskOutput floods the main context window with agent transcripts (70k+ tokens).

## Rule

NEVER use `TaskOutput` tool. Use `Task` tool with synchronous mode instead.

## Why

- TaskOutput reads full agent transcript into context
- This causes mid-conversation compaction
- Defeats the purpose of agent context isolation

## Pattern

```
# WRONG - floods context
Task(run_in_background=true)
TaskOutput(task_id="...")  // 70k tokens dumped

# RIGHT - isolated context, returns summary
Task(run_in_background=false)  // Agent runs, returns summary
```

## Source
- Session where TaskOutput caused context overflow

---

**Source:** [`parcadei/Continuous-Claude-v3`](https://github.com/parcadei/Continuous-Claude-v3) → `.claude/skills/no-task-output/SKILL.md`
