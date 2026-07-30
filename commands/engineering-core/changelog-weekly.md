---
name: changelog-weekly
description: "Generate a changelog draft for the last 7 days"
category: engineering-core
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "plugins/devops/mattyp-changelog/commands/changelog-weekly.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/plugins/devops/mattyp-changelog/commands/changelog-weekly.md
---


# /changelog-weekly

Generate a changelog for the last 7 days using `.changelog-config.json`, then prepare a branch/PR.

## Steps

1. Ensure `.changelog-config.json` exists at repo root (copy `${CLAUDE_PLUGIN_ROOT}/config/changelog-config.example.json` if missing).
2. Validate setup by running `/changelog-validate` first.
3. Use the `changelog-orchestrator` skill to:
   - Compute date range (today minus 7 days → today)
   - Fetch changes (GitHub/Slack/Git)
   - Draft + format changelog using the configured template
   - Run quality gate (threshold from config)
   - Create branch + commit, then open PR if possible

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `plugins/devops/mattyp-changelog/commands/changelog-weekly.md`
