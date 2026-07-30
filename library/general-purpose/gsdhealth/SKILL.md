---
name: gsdhealth
description: "Diagnose planning directory health and optionally repair issues"
allowed-tools: "Read Bash Write AskUserQuestion"
category: general-purpose
source_repo: davepoon/buildwithclaude
source_path: "plugins/gsd/skills/health/SKILL.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/gsd/skills/health/SKILL.md
---

<objective>
Validate `.planning/` directory integrity and report actionable issues. Checks for missing files, invalid configurations, inconsistent state, and orphaned plans.
</objective>

<execution_context>
@${CLAUDE_PLUGIN_ROOT}/workflows/health.md
</execution_context>

<process>
Execute the health workflow from @${CLAUDE_PLUGIN_ROOT}/workflows/health.md end-to-end.
Parse --repair flag from arguments and pass to workflow.
</process>

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/gsd/skills/health/SKILL.md`
