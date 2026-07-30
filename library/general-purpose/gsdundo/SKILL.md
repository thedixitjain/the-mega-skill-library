---
name: gsdundo
description: "Safe git revert. Roll back phase or plan commits using the phase manifest with dependency checks."
allowed-tools: "Read Bash Glob Grep AskUserQuestion"
category: general-purpose
source_repo: davepoon/buildwithclaude
source_path: "plugins/gsd/skills/undo/SKILL.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/gsd/skills/undo/SKILL.md
---


<objective>
Safe git revert — roll back GSD phase or plan commits using the phase manifest, with dependency checks and a confirmation gate before execution.

Three modes:
- **--last N**: Show recent GSD commits for interactive selection
- **--phase NN**: Revert all commits for a phase (manifest + git log fallback)
- **--plan NN-MM**: Revert all commits for a specific plan
</objective>

<execution_context>
@${CLAUDE_PLUGIN_ROOT}/workflows/undo.md
@${CLAUDE_PLUGIN_ROOT}/references/ui-brand.md
@${CLAUDE_PLUGIN_ROOT}/references/gate-prompts.md
</execution_context>

<context>
$ARGUMENTS
</context>

<process>
Execute the undo workflow from @${CLAUDE_PLUGIN_ROOT}/workflows/undo.md end-to-end.
</process>

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/gsd/skills/undo/SKILL.md`
