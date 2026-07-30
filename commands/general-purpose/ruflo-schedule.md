---
name: ruflo-schedule
description: "Schedule persistent workers via CronCreate"
category: general-purpose
source_repo: ruvnet/ruflo
source_path: "plugins/ruflo-loop-workers/commands/ruflo-schedule.md"
source_url: https://github.com/ruvnet/ruflo/blob/HEAD/plugins/ruflo-loop-workers/commands/ruflo-schedule.md
---

$ARGUMENTS
Schedule a persistent background worker using CronCreate.

Usage: /schedule <worker> [cron-expression]

Workers: audit, map, optimize, consolidate, testgaps, predict, document, benchmark.

Default cron expressions:
- audit, testgaps: `*/15 * * * *`
- optimize, map: `*/30 * * * *`
- consolidate, document: `0 * * * *`

Example: /schedule audit */15 * * * *
Creates: `CronCreate("audit", "*/15 * * * *", "Run security audit worker")`

---

**Source:** [`ruvnet/ruflo`](https://github.com/ruvnet/ruflo) → `plugins/ruflo-loop-workers/commands/ruflo-schedule.md`
