---
name: gsdvalidate-phase
description: "Retroactively audit and fill Nyquist validation gaps for a completed phase"
allowed-tools: "Read Write Edit Bash Glob Grep Task AskUserQuestion"
category: security-and-compliance
source_repo: davepoon/buildwithclaude
source_path: "plugins/gsd/skills/validate-phase/SKILL.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/gsd/skills/validate-phase/SKILL.md
---

<objective>
Audit Nyquist validation coverage for a completed phase. Three states:
- (A) VALIDATION.md exists — audit and fill gaps
- (B) No VALIDATION.md, SUMMARY.md exists — reconstruct from artifacts
- (C) Phase not executed — exit with guidance

Output: updated VALIDATION.md + generated test files.
</objective>

<execution_context>
@${CLAUDE_PLUGIN_ROOT}/workflows/validate-phase.md
</execution_context>

<context>
Phase: $ARGUMENTS — optional, defaults to last completed phase.
</context>

<process>
Execute @${CLAUDE_PLUGIN_ROOT}/workflows/validate-phase.md.
Preserve all workflow gates.
</process>

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/gsd/skills/validate-phase/SKILL.md`
