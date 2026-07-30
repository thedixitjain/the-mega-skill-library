---
name: iot-fleet
description: "Create and manage Cognitum Seed device fleets with firmware policies"
allowed-tools: "Bash(npx *) mcp__plugin_ruflo-core_ruflo__memory_store mcp__plugin_ruflo-core_ruflo__memory_search Read"
category: general-purpose
source_repo: ruvnet/ruflo
source_path: "plugins/ruflo-iot-cognitum/skills/iot-fleet/SKILL.md"
source_url: https://github.com/ruvnet/ruflo/blob/HEAD/plugins/ruflo-iot-cognitum/skills/iot-fleet/SKILL.md
---

Manage device fleets. Parse subcommand from arguments.

**create**: `npx -y -p @claude-flow/plugin-iot-cognitum@latest cognitum-iot fleet create --name NAME`
**list**: `npx -y -p @claude-flow/plugin-iot-cognitum@latest cognitum-iot fleet list`
**add**: `npx -y -p @claude-flow/plugin-iot-cognitum@latest cognitum-iot fleet add FLEET_ID DEVICE_ID`
**remove**: `npx -y -p @claude-flow/plugin-iot-cognitum@latest cognitum-iot fleet remove FLEET_ID DEVICE_ID`
**delete**: `npx -y -p @claude-flow/plugin-iot-cognitum@latest cognitum-iot fleet delete FLEET_ID`

---

**Source:** [`ruvnet/ruflo`](https://github.com/ruvnet/ruflo) → `plugins/ruflo-iot-cognitum/skills/iot-fleet/SKILL.md`
