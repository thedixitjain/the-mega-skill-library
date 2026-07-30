---
name: gsdinsert-phase
description: "Insert urgent work as decimal phase (e.g., 72.1) between existing phases"
allowed-tools: "Read Write Bash"
category: general-purpose
source_repo: davepoon/buildwithclaude
source_path: "plugins/gsd/skills/insert-phase/SKILL.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/gsd/skills/insert-phase/SKILL.md
---


<objective>
Insert a decimal phase for urgent work discovered mid-milestone that must be completed between existing integer phases.

Uses decimal numbering (72.1, 72.2, etc.) to preserve the logical sequence of planned phases while accommodating urgent insertions.

Purpose: Handle urgent work discovered during execution without renumbering entire roadmap.
</objective>

<execution_context>
@${CLAUDE_PLUGIN_ROOT}/workflows/insert-phase.md
</execution_context>

<context>
Arguments: $ARGUMENTS (format: <after-phase-number> <description>)

Roadmap and state are resolved in-workflow via `init phase-op` and targeted tool calls.
</context>

<process>
Execute the insert-phase workflow from @${CLAUDE_PLUGIN_ROOT}/workflows/insert-phase.md end-to-end.
Preserve all validation gates (argument parsing, phase verification, decimal calculation, roadmap updates).
</process>

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/gsd/skills/insert-phase/SKILL.md`
