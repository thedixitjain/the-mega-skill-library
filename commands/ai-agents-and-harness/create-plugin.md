---
name: create-plugin
description: "Scaffold a new Claude Code plugin interactively"
category: ai-agents-and-harness
source_repo: ruvnet/ruflo
source_path: "plugins/ruflo-plugin-creator/commands/create-plugin.md"
source_url: https://github.com/ruvnet/ruflo/blob/HEAD/plugins/ruflo-plugin-creator/commands/create-plugin.md
---


Create a new Claude Code plugin:

1. Ask the user for: plugin name, description, desired skills, commands, and agents
2. Use the `create-plugin` skill to scaffold the complete directory structure
3. Run the `validate-plugin` skill to verify correctness
4. Show the user what was created and how to test it with `claude --plugin-dir ./plugins/<name>`

---

**Source:** [`ruvnet/ruflo`](https://github.com/ruvnet/ruflo) → `plugins/ruflo-plugin-creator/commands/create-plugin.md`
