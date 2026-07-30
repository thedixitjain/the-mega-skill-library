---
name: slopmopsm-refit
description: "Run slop-mop's one-time repository onboarding remediation rail"
allowed-tools: "Bash(sm:*)"
category: engineering-core
source_repo: davepoon/buildwithclaude
source_path: "plugins/slopmop/commands/sm-refit.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/slopmop/commands/sm-refit.md
---


# /slopmop:sm-refit

Run slop-mop's one-time onboarding remediation rail for this repository.

1. For an existing repo that has not been remediated, start with `sm refit --start`.
2. Fix the current gate or blocker it reports.
3. Run `sm refit --iterate` to resume the stored plan.
4. Repeat until the plan is complete, then run `sm refit --finish`.

This is step 0 for inherited or already-messy repositories. Let refit own the
structured remediation plan and commits; use the swab/scour/buff loop after the
repo has entered maintenance.

**Prerequisite:** `sm` must be installed. If `command not found`, suggest:
```bash
pipx install slopmop[all]
```

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/slopmop/commands/sm-refit.md`
