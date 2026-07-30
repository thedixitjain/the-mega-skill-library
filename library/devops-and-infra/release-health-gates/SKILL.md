---
name: release-health-gates
description: "Standardizes release approvals with GitHub-aware checklists and deployment gates. Use before releasing to production to verify all gates pass."
allowed-tools: "[]"
category: devops-and-infra
source_repo: athola/claude-night-market
source_path: "plugins/minister/skills/release-health-gates/SKILL.md"
source_url: https://github.com/athola/claude-night-market/blob/HEAD/plugins/minister/skills/release-health-gates/SKILL.md
---

# Release Health Gates

## When NOT To Use

- Measuring delivery performance (use `minister:dora-metrics`)
- PR-level quality gates before merge (use `sanctum:pr-prep`)

## Purpose

Standardize release approvals by expressing gates as GitHub-aware checklists. Ensure code, docs, comms, and observability items are green before deployment.

## Gate Categories

1. **Scope & Risk** – Are all blocking issues closed or deferred with owners?
2. **Quality Signals** – Are required checks, tests, and soak times satisfied?
3. **Comms & Docs** – Are docs merged and release notes posted?
4. **Operations** – Are runbooks, oncall sign-off, and rollback plans ready?

## Workflow

1. Load skill to access gate modules.
2. Attach Release Gate section to deployment PR.
3. Use tracker data to auto-fill blockers and highlight overdue tasks.
4. Update comment as gates turn green; require approvals for any waivers.

## Outputs

- Release Gate markdown snippet (embed in PR/issue).
- QA Handshake summary referencing GitHub Checks.
- Rollout scorecard that persists in tracker data for retros.

## Exit Criteria

- All release gates evaluated and documented.
- Any blocking gates have waiver approvals recorded.
- Deployment PR contains embedded Release Gate snippet.
- Rollout scorecard saved for post-release retrospective.

---

**Source:** [`athola/claude-night-market`](https://github.com/athola/claude-night-market) → `plugins/minister/skills/release-health-gates/SKILL.md`
