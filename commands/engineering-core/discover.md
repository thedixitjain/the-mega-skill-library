---
name: discover
description: "Run brownfield codebase discovery. Spawns scout agents that explore the codebase and produce structured mulch records for architecture patterns, dependency graph, test coverage, API surface, config conventions, and implicit knowledge."
category: engineering-core
source_repo: jayminwest/overstory
source_path: ".claude/commands/discover.md"
source_url: https://github.com/jayminwest/overstory/blob/HEAD/.claude/commands/discover.md
---
## intro

Run brownfield codebase discovery. Spawns scout agents that explore the codebase and produce structured mulch records for architecture patterns, dependency graph, test coverage, API surface, config conventions, and implicit knowledge.

**Argument:** $ARGUMENTS — optional flags (e.g., --skip testing,config to skip categories, --task-id <id> to set task ID).

## steps

1. Run: ov discover $ARGUMENTS
2. Monitor progress with: ov status
3. When scouts complete, review results with: ml prime

---

**Source:** [`jayminwest/overstory`](https://github.com/jayminwest/overstory) → `.claude/commands/discover.md`
