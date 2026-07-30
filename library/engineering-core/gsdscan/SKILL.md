---
name: gsdscan
description: "Rapid codebase assessment — lightweight alternative to /gsd:map-codebase"
allowed-tools: "Read Write Bash Grep Glob Agent AskUserQuestion"
category: engineering-core
source_repo: davepoon/buildwithclaude
source_path: "plugins/gsd/skills/scan/SKILL.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/gsd/skills/scan/SKILL.md
---

<objective>
Run a focused codebase scan for a single area, producing targeted documents in `.planning/codebase/`.
Accepts an optional `--focus` flag: `tech`, `arch`, `quality`, `concerns`, or `tech+arch` (default).

Lightweight alternative to `/gsd:map-codebase` — spawns one mapper agent instead of four parallel ones.
</objective>

<execution_context>
@${CLAUDE_PLUGIN_ROOT}/workflows/scan.md
</execution_context>

<process>
Execute the scan workflow from @${CLAUDE_PLUGIN_ROOT}/workflows/scan.md end-to-end.
</process>

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/gsd/skills/scan/SKILL.md`
