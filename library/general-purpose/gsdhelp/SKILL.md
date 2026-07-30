---
name: gsdhelp
description: "Show available GSD commands and usage guide"
allowed-tools: "Read"
category: general-purpose
source_repo: davepoon/buildwithclaude
source_path: "plugins/gsd/skills/help/SKILL.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/gsd/skills/help/SKILL.md
---

<objective>
Display the complete GSD command reference.

Output ONLY the reference content below. Do NOT add:
- Project-specific analysis
- Git status or file context
- Next-step suggestions
- Any commentary beyond the reference
</objective>

<execution_context>
@${CLAUDE_PLUGIN_ROOT}/workflows/help.md
</execution_context>

<process>
Output the complete GSD command reference from @${CLAUDE_PLUGIN_ROOT}/workflows/help.md.
Display the reference content directly — no additions or modifications.
</process>

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/gsd/skills/help/SKILL.md`
