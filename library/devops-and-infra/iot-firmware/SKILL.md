---
name: iot-firmware
description: "Orchestrate firmware rollouts with canary deployment and anomaly-gated advancement"
allowed-tools: "Bash(npx *) mcp__plugin_ruflo-core_ruflo__memory_store mcp__plugin_ruflo-core_ruflo__memory_search Read"
category: devops-and-infra
source_repo: ruvnet/ruflo
source_path: "plugins/ruflo-iot-cognitum/skills/iot-firmware/SKILL.md"
source_url: https://github.com/ruvnet/ruflo/blob/HEAD/plugins/ruflo-iot-cognitum/skills/iot-firmware/SKILL.md
---

Manage firmware rollouts across device fleets.

**deploy**: `npx -y -p @claude-flow/plugin-iot-cognitum@latest cognitum-iot firmware deploy FLEET_ID --version VERSION`
**advance**: `npx -y -p @claude-flow/plugin-iot-cognitum@latest cognitum-iot firmware advance ROLLOUT_ID`
**rollback**: `npx -y -p @claude-flow/plugin-iot-cognitum@latest cognitum-iot firmware rollback ROLLOUT_ID`
**status**: `npx -y -p @claude-flow/plugin-iot-cognitum@latest cognitum-iot firmware status ROLLOUT_ID`
**list**: `npx -y -p @claude-flow/plugin-iot-cognitum@latest cognitum-iot firmware list`

Rollout stages: pending → canary → rolling → complete (or rolled-back)

---

**Source:** [`ruvnet/ruflo`](https://github.com/ruvnet/ruflo) → `plugins/ruflo-iot-cognitum/skills/iot-firmware/SKILL.md`
