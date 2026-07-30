---
name: monitor-stream
description: "Stream live swarm events using the Monitor tool for real-time observability"
allowed-tools: "Bash(npx *) mcp__plugin_ruflo-core_ruflo__swarm_status mcp__plugin_ruflo-core_ruflo__swarm_health Monitor"
category: ai-agents-and-harness
source_repo: ruvnet/ruflo
source_path: "plugins/ruflo-swarm/skills/monitor-stream/SKILL.md"
source_url: https://github.com/ruvnet/ruflo/blob/HEAD/plugins/ruflo-swarm/skills/monitor-stream/SKILL.md
---

Use the Monitor tool to stream swarm events in real time instead of polling:

Run via Monitor: `npx @claude-flow/cli@latest swarm watch --stream`

This streams NDJSON events for agent spawns, task completions, memory writes, and health checks. Each stdout line triggers a notification.

For one-shot status, use MCP: `mcp__plugin_ruflo-core_ruflo__swarm_status` or `mcp__plugin_ruflo-core_ruflo__swarm_health`.

Prefer Monitor over polling `swarm status` in a loop. See ADR-091 for rationale.

---

**Source:** [`ruvnet/ruflo`](https://github.com/ruvnet/ruflo) → `plugins/ruflo-swarm/skills/monitor-stream/SKILL.md`
