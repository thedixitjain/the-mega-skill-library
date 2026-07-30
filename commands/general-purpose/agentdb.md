---
name: agentdb
description: "AgentDB health, controller status, and session management"
category: general-purpose
source_repo: ruvnet/ruflo
source_path: "plugins/ruflo-agentdb/commands/agentdb.md"
source_url: https://github.com/ruvnet/ruflo/blob/HEAD/plugins/ruflo-agentdb/commands/agentdb.md
---


AgentDB management:

1. Call `mcp__plugin_ruflo-core_ruflo__agentdb_health` to check database health
2. Call `mcp__plugin_ruflo-core_ruflo__agentdb_controllers` to list whatever the runtime reports — controller `total` and `active` counts. The canonical list of names lives at `v3/@claude-flow/memory/src/controller-registry.ts:34-73` (`ControllerName` union); the runtime tool is the source of truth.
3. Present a summary with: total entries, active sessions, controller `active` / `total`, and storage size.
4. If `agentdb_health.available` is `false` (bridge unavailable), see the README's "Bridge unavailable" replacement table — `memory_store` / `memory_search` substitute for most `agentdb_*` operations.
5. If issues found, suggest `npx @claude-flow/cli@latest memory init --force` to reinitialize.

---

**Source:** [`ruvnet/ruflo`](https://github.com/ruvnet/ruflo) → `plugins/ruflo-agentdb/commands/agentdb.md`
