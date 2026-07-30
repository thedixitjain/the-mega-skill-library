---
name: gsdsketch-wrap-up
description: "Package sketch design findings into a persistent project skill for future build conversations"
allowed-tools: "Read Write Edit Bash Grep Glob AskUserQuestion"
category: general-purpose
source_repo: davepoon/buildwithclaude
source_path: "plugins/gsd/skills/sketch-wrap-up/SKILL.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/gsd/skills/sketch-wrap-up/SKILL.md
---

<objective>
Curate sketch design findings and package them into a persistent project skill that Claude
auto-loads when building the real UI. Also writes a summary to `.planning/sketches/` for
project history. Output skill goes to `./.claude/skills/sketch-findings-[project]/` (project-local).
</objective>

<execution_context>
@${CLAUDE_PLUGIN_ROOT}/workflows/sketch-wrap-up.md
@${CLAUDE_PLUGIN_ROOT}/references/ui-brand.md
</execution_context>

<runtime_note>
**Copilot (VS Code):** Use `vscode_askquestions` wherever this workflow calls `AskUserQuestion`.
</runtime_note>

<process>
Execute the sketch-wrap-up workflow from @${CLAUDE_PLUGIN_ROOT}/workflows/sketch-wrap-up.md end-to-end.
Preserve all curation gates (per-sketch review, grouping approval, CLAUDE.md routing line).
</process>

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/gsd/skills/sketch-wrap-up/SKILL.md`
