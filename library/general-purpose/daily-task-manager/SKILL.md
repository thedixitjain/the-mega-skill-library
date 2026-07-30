---
name: daily-task-manager
description: "| Task lifecycle management. Add, complete, defer, remove, and review tasks. Maintains a running task list as a brain page."
allowed-tools: "search get_page put_page add_timeline_entry"
category: general-purpose
source_repo: garrytan/gbrain
source_path: "skills/daily-task-manager/SKILL.md"
source_url: https://github.com/garrytan/gbrain/blob/HEAD/skills/daily-task-manager/SKILL.md
---


# Daily Task Manager

## Contract

This skill guarantees:
- Tasks stored as a brain page (`ops/tasks.md`) with structured format
- Task lifecycle: add → in-progress → complete | defer
- Priority levels: P0 (urgent), P1 (today), P2 (this week), P3 (backlog)
- Completed tasks archived with completion date
- Deferred tasks carry forward with reason

## Phases

1. **Load current tasks.** `gbrain get ops/tasks` — read the task list.
2. **Execute the requested action:**
   - **Add:** Append task with priority, description, due date. Add timeline entry.
   - **Complete:** Mark as done, move to completed section with date.
   - **Defer:** Move to next day/week with reason.
   - **Remove:** Delete from list (rare, prefer complete or defer).
   - **Review:** Display all active tasks by priority.
3. **Save.** `gbrain put ops/tasks` — write updated task list.

## Output Format

```markdown
# Tasks

## P0 — Urgent
- [ ] {task description} (due: {date})

## P1 — Today
- [ ] {task description}

## P2 — This Week
- [ ] {task description}

## P3 — Backlog
- [ ] {task description}

## Completed
- [x] {task} (completed: {date})
```

## Anti-Patterns

- Adding tasks without a priority level
- Completing tasks without recording the completion date
- Deferring tasks without a reason
- Letting the task list grow unbounded (review weekly)
- Storing tasks outside the brain (they should be searchable)

---

**Source:** [`garrytan/gbrain`](https://github.com/garrytan/gbrain) → `skills/daily-task-manager/SKILL.md`
