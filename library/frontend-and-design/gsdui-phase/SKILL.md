---
name: gsdui-phase
description: "Generate UI design contract (UI-SPEC.md) for frontend phases"
allowed-tools: "Read Write Bash Glob Grep Task WebFetch AskUserQuestion mcp__context7__*"
category: frontend-and-design
source_repo: davepoon/buildwithclaude
source_path: "plugins/gsd/skills/ui-phase/SKILL.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/gsd/skills/ui-phase/SKILL.md
---

<objective>
Create a UI design contract (UI-SPEC.md) for a frontend phase.
Orchestrates gsd-ui-researcher and gsd-ui-checker.
Flow: Validate → Research UI → Verify UI-SPEC → Done
</objective>

<execution_context>
@${CLAUDE_PLUGIN_ROOT}/workflows/ui-phase.md
@${CLAUDE_PLUGIN_ROOT}/references/ui-brand.md
</execution_context>

<context>
Phase number: $ARGUMENTS — optional, auto-detects next unplanned phase if omitted.
</context>

<process>
Execute @${CLAUDE_PLUGIN_ROOT}/workflows/ui-phase.md end-to-end.
Preserve all workflow gates.
</process>

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/gsd/skills/ui-phase/SKILL.md`
