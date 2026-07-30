---
name: gsdimport
description: "Ingest external plans with conflict detection against project decisions before writing anything."
allowed-tools: "Read Write Edit Bash Glob Grep AskUserQuestion Task"
category: writing-and-content
source_repo: davepoon/buildwithclaude
source_path: "plugins/gsd/skills/import/SKILL.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/gsd/skills/import/SKILL.md
---


<objective>
Import external plan files into the GSD planning system with conflict detection against PROJECT.md decisions.

- **--from**: Import an external plan file, detect conflicts, write as GSD PLAN.md, validate via gsd-plan-checker.

Future: `--prd` mode for PRD extraction is planned for a follow-up PR.
</objective>

<execution_context>
@${CLAUDE_PLUGIN_ROOT}/workflows/import.md
@${CLAUDE_PLUGIN_ROOT}/references/ui-brand.md
@${CLAUDE_PLUGIN_ROOT}/references/gate-prompts.md
@${CLAUDE_PLUGIN_ROOT}/references/doc-conflict-engine.md
</execution_context>

<context>
$ARGUMENTS
</context>

<process>
Execute the import workflow end-to-end.
</process>

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/gsd/skills/import/SKILL.md`
