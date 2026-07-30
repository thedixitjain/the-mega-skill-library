---
name: gsdultraplan-phase
description: "[BETA] Offload plan phase to Claude Code's ultraplan cloud — drafts remotely while terminal stays free, review in browser with inline comments, import back via /gsd:import. Claude Code only."
allowed-tools: "Read Bash Glob Grep"
category: ai-agents-and-harness
source_repo: davepoon/buildwithclaude
source_path: "plugins/gsd/skills/ultraplan-phase/SKILL.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/gsd/skills/ultraplan-phase/SKILL.md
---


<objective>
Offload GSD's plan phase to Claude Code's ultraplan cloud infrastructure.

Ultraplan drafts the plan in a remote cloud session while your terminal stays free.
Review and comment on the plan in your browser, then import it back via /gsd:import --from.

⚠ BETA: ultraplan is in research preview. Use /gsd:plan-phase for stable local planning.
Requirements: Claude Code v2.1.91+, claude.ai account, GitHub repository.
</objective>

<execution_context>
@${CLAUDE_PLUGIN_ROOT}/workflows/ultraplan-phase.md
@${CLAUDE_PLUGIN_ROOT}/references/ui-brand.md
</execution_context>

<context>
$ARGUMENTS
</context>

<process>
Execute the ultraplan-phase workflow end-to-end.
</process>

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/gsd/skills/ultraplan-phase/SKILL.md`
