---
name: gsdplan-milestone-gaps
description: "Create phases to close all gaps identified by milestone audit"
allowed-tools: "Read Write Bash Glob Grep AskUserQuestion"
category: security-and-compliance
source_repo: davepoon/buildwithclaude
source_path: "plugins/gsd/skills/plan-milestone-gaps/SKILL.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/gsd/skills/plan-milestone-gaps/SKILL.md
---

<objective>
Create all phases necessary to close gaps identified by `/gsd:audit-milestone`.

Reads MILESTONE-AUDIT.md, groups gaps into logical phases, creates phase entries in ROADMAP.md, and offers to plan each phase.

One command creates all fix phases — no manual `/gsd:add-phase` per gap.
</objective>

<execution_context>
@${CLAUDE_PLUGIN_ROOT}/workflows/plan-milestone-gaps.md
</execution_context>

<context>
**Audit results:**
Glob: .planning/v*-MILESTONE-AUDIT.md (use most recent)

Original intent and current planning state are loaded on demand inside the workflow.
</context>

<process>
Execute the plan-milestone-gaps workflow from @${CLAUDE_PLUGIN_ROOT}/workflows/plan-milestone-gaps.md end-to-end.
Preserve all workflow gates (audit loading, prioritization, phase grouping, user confirmation, roadmap updates).
</process>

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/gsd/skills/plan-milestone-gaps/SKILL.md`
