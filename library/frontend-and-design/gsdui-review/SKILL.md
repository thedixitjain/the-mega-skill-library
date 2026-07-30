---
name: gsdui-review
description: "Retroactive 6-pillar visual audit of implemented frontend code"
allowed-tools: "Read Write Bash Glob Grep Task AskUserQuestion"
category: frontend-and-design
source_repo: davepoon/buildwithclaude
source_path: "plugins/gsd/skills/ui-review/SKILL.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/gsd/skills/ui-review/SKILL.md
---

<objective>
Conduct a retroactive 6-pillar visual audit. Produces UI-REVIEW.md with
graded assessment (1-4 per pillar). Works on any project.
Output: {phase_num}-UI-REVIEW.md
</objective>

<execution_context>
@${CLAUDE_PLUGIN_ROOT}/workflows/ui-review.md
@${CLAUDE_PLUGIN_ROOT}/references/ui-brand.md
</execution_context>

<context>
Phase: $ARGUMENTS — optional, defaults to last completed phase.
</context>

<process>
Execute @${CLAUDE_PLUGIN_ROOT}/workflows/ui-review.md end-to-end.
Preserve all workflow gates.
</process>

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/gsd/skills/ui-review/SKILL.md`
