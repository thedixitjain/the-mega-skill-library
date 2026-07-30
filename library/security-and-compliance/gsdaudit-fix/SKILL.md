---
name: gsdaudit-fix
description: "Autonomous audit-to-fix pipeline — find issues, classify, fix, test, commit"
allowed-tools: "Read Write Edit Bash Grep Glob Agent AskUserQuestion"
category: security-and-compliance
source_repo: davepoon/buildwithclaude
source_path: "plugins/gsd/skills/audit-fix/SKILL.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/gsd/skills/audit-fix/SKILL.md
---

<objective>
Run an audit, classify findings as auto-fixable vs manual-only, then autonomously fix
auto-fixable issues with test verification and atomic commits.

Flags:
- `--max N` — maximum findings to fix (default: 5)
- `--severity high|medium|all` — minimum severity to process (default: medium)
- `--dry-run` — classify findings without fixing (shows classification table)
- `--source <audit>` — which audit to run (default: audit-uat)
</objective>

<execution_context>
@${CLAUDE_PLUGIN_ROOT}/workflows/audit-fix.md
</execution_context>

<process>
Execute the audit-fix workflow from @${CLAUDE_PLUGIN_ROOT}/workflows/audit-fix.md end-to-end.
</process>

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/gsd/skills/audit-fix/SKILL.md`
