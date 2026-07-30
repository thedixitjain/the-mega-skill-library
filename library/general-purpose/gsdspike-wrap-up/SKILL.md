---
name: gsdspike-wrap-up
description: "Package spike findings into a persistent project skill for future build conversations"
allowed-tools: "Read Write Edit Bash Grep Glob AskUserQuestion"
category: general-purpose
source_repo: davepoon/buildwithclaude
source_path: "plugins/gsd/skills/spike-wrap-up/SKILL.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/gsd/skills/spike-wrap-up/SKILL.md
---

<objective>
Curate spike experiment findings and package them into a persistent project skill that Claude
auto-loads in future build conversations. Also writes a summary to `.planning/spikes/` for
project history. Output skill goes to `./.claude/skills/spike-findings-[project]/` (project-local).
</objective>

<execution_context>
@${CLAUDE_PLUGIN_ROOT}/workflows/spike-wrap-up.md
@${CLAUDE_PLUGIN_ROOT}/references/ui-brand.md
</execution_context>

<runtime_note>
**Copilot (VS Code):** Use `vscode_askquestions` wherever this workflow calls `AskUserQuestion`.
</runtime_note>

<process>
Execute the spike-wrap-up workflow from @${CLAUDE_PLUGIN_ROOT}/workflows/spike-wrap-up.md end-to-end.
Preserve all curation gates (per-spike review, grouping approval, CLAUDE.md routing line).
</process>

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/gsd/skills/spike-wrap-up/SKILL.md`
