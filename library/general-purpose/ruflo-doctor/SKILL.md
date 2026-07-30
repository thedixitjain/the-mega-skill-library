---
name: ruflo-doctor
description: "Run health checks on the Ruflo installation and fix common issues"
allowed-tools: "Bash(npx *)"
category: general-purpose
source_repo: ruvnet/ruflo
source_path: "plugins/ruflo-core/skills/ruflo-doctor/SKILL.md"
source_url: https://github.com/ruvnet/ruflo/blob/HEAD/plugins/ruflo-core/skills/ruflo-doctor/SKILL.md
---

Run `npx @claude-flow/cli@latest doctor --fix` to diagnose and auto-repair common issues.

Checks: Node.js 20+, npm 9+, git, config validity, daemon status, memory database, API keys, MCP servers, disk space, TypeScript.

Targeted fixes:
- Memory: `npx @claude-flow/cli@latest memory init --force`
- Daemon: `npx @claude-flow/cli@latest daemon start`
- Config: `npx @claude-flow/cli@latest config reset`

---

**Source:** [`ruvnet/ruflo`](https://github.com/ruvnet/ruflo) → `plugins/ruflo-core/skills/ruflo-doctor/SKILL.md`
