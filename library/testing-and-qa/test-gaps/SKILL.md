---
name: test-gaps
description: "Detect missing test coverage and generate test suggestions. Use when the user asks about coverage gaps, untested code, or what tests to write next; also after adding a feature to find what still needs tests."
allowed-tools: "Bash(npx *) mcp__plugin_ruflo-core_ruflo__hooks_worker-dispatch Read Grep"
category: testing-and-qa
source_repo: ruvnet/ruflo
source_path: "plugins/ruflo-testgen/skills/test-gaps/SKILL.md"
source_url: https://github.com/ruvnet/ruflo/blob/HEAD/plugins/ruflo-testgen/skills/test-gaps/SKILL.md
---

Find test coverage gaps via CLI:
```bash
npx @claude-flow/cli@latest hooks coverage-gaps --format table --limit 20
npx @claude-flow/cli@latest hooks coverage-route --task "add auth tests"
npx @claude-flow/cli@latest hooks coverage-suggest --path src/
```

Or dispatch the testgaps worker via MCP:
`mcp__plugin_ruflo-core_ruflo__hooks_worker-dispatch({ trigger: "testgaps" })`

For continuous detection, use `/loop` with the `loop-worker` skill targeting the `testgaps` worker.

---

**Source:** [`ruvnet/ruflo`](https://github.com/ruvnet/ruflo) → `plugins/ruflo-testgen/skills/test-gaps/SKILL.md`
