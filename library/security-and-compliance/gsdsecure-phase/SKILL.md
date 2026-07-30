---
name: gsdsecure-phase
description: "Retroactively verify threat mitigations for a completed phase"
allowed-tools: "Read Write Edit Bash Glob Grep Task AskUserQuestion"
category: security-and-compliance
source_repo: davepoon/buildwithclaude
source_path: "plugins/gsd/skills/secure-phase/SKILL.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/gsd/skills/secure-phase/SKILL.md
---

<objective>
Verify threat mitigations for a completed phase. Three states:
- (A) SECURITY.md exists — audit and verify mitigations
- (B) No SECURITY.md, PLAN.md with threat model exists — run from artifacts
- (C) Phase not executed — exit with guidance

Output: updated SECURITY.md.
</objective>

<execution_context>
@${CLAUDE_PLUGIN_ROOT}/workflows/secure-phase.md
</execution_context>

<context>
Phase: $ARGUMENTS — optional, defaults to last completed phase.
</context>

<process>
Execute @${CLAUDE_PLUGIN_ROOT}/workflows/secure-phase.md.
Preserve all workflow gates.
</process>

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/gsd/skills/secure-phase/SKILL.md`
