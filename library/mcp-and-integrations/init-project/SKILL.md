---
name: init-project
description: "Initialize a new Ruflo project with MCP tools, hooks, and agent configuration. Use when setting up Ruflo in a fresh repo, or when the user says \"init ruflo\", \"set up ruflo\", or asks how to bootstrap the MCP server, hooks, and agent configs from scratch."
allowed-tools: "Bash(npx *) Read Write Edit"
category: mcp-and-integrations
source_repo: ruvnet/ruflo
source_path: "plugins/ruflo-core/skills/init-project/SKILL.md"
source_url: https://github.com/ruvnet/ruflo/blob/HEAD/plugins/ruflo-core/skills/init-project/SKILL.md
---

Run `npx @claude-flow/cli@latest init --wizard` to set up the project interactively, or `npx @claude-flow/cli@latest init --preset standard` for defaults.

This creates CLAUDE.md, .claude/settings.json, and .claude-flow/ config with MCP server registration for the `ruflo` MCP tools.

---

**Source:** [`ruvnet/ruflo`](https://github.com/ruvnet/ruflo) → `plugins/ruflo-core/skills/init-project/SKILL.md`
