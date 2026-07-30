---
name: pwf
description: "Short alias for /plan. Starts Manus-style file-based planning: task_plan.md, findings.md, progress.md. Available since v3.0.0."
category: general-purpose
source_repo: OthmanAdi/planning-with-files
source_path: "commands/pwf.md"
source_url: https://github.com/OthmanAdi/planning-with-files/blob/HEAD/commands/pwf.md
---


Invoke the planning-with-files:planning-with-files skill and follow it exactly as presented to you. Treat any arguments as the task to plan.

Create the three planning files in the current project directory if they don't exist:
- task_plan.md — for phases, progress, and decisions
- findings.md — for research and discoveries
- progress.md — for session logging

If the user asked for autonomous or gated mode in their words (for example "autonomous", "gated", "don't stop until done"), initialize with `init-session.sh --autonomous` or `init-session.sh --gated` accordingly; otherwise initialize the default way.

Then guide the user through the planning workflow.

---

**Source:** [`OthmanAdi/planning-with-files`](https://github.com/OthmanAdi/planning-with-files) → `commands/pwf.md`
