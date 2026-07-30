---
name: task-planner
description: "Turn a list of goals, tasks, deadlines, and working constraints into a practical schedule with next actions and follow-ups."
category: ai-agents-and-harness
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/6Delta9/task-scheduler-codex-plugin/skills/task-planner/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/6Delta9/task-scheduler-codex-plugin/skills/task-planner/SKILL.md
---


# Task Planner

Use this skill when the user wants help organizing work into a schedule.

## Workflow

1. Gather the planning window, available hours, deadlines, and any fixed meetings or blocked days.
2. Group the work into concrete tasks with estimated effort and priority.
3. Produce a schedule that is realistic, not just complete.
4. Flag overflow, risky deadlines, and missing information.

## Output Format

Return the plan in markdown with these sections:

- `Summary`
- `Schedule`
- `Follow-Ups`
- `Risks`

For each scheduled item, include:

- task name
- planned date
- estimated effort
- short reason for placement

## Scheduling Rules

- Put urgent and high-priority work first.
- Avoid filling a day past the stated hour limit.
- Break large work into smaller steps when that makes the plan easier to follow.
- Keep at least one buffer slot when the schedule is tight.
- Call out tasks that do not fit inside the requested window.

## Script Assist

When the user provides structured JSON tasks, you can use:

```powershell
python .\scripts\build_schedule.py --input <tasks.json>
```

The script builds a first-pass markdown schedule that you can refine in your response.

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/6Delta9/task-scheduler-codex-plugin/skills/task-planner/SKILL.md`
