---
name: autopilot-status
description: "Quick autopilot progress summary with task completion stats"
category: general-purpose
source_repo: ruvnet/ruflo
source_path: "plugins/ruflo-autopilot/commands/autopilot-status.md"
source_url: https://github.com/ruvnet/ruflo/blob/HEAD/plugins/ruflo-autopilot/commands/autopilot-status.md
---

$ARGUMENTS
Show autopilot progress. Calls `autopilot_status` and `autopilot_progress` via MCP.

Displays:
- Enabled/disabled state
- Iteration count vs max
- Elapsed time vs timeout
- Task completion by source (team-tasks, swarm-tasks, file-checklist)
- Overall completion percentage

For detailed task breakdown, use `autopilot_progress`. For event log, use `autopilot_log`.

---

**Source:** [`ruvnet/ruflo`](https://github.com/ruvnet/ruflo) → `plugins/ruflo-autopilot/commands/autopilot-status.md`
