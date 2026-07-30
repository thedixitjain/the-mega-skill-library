---
name: changelog-validate
description: "Validate changelog config, tokens, and template paths"
category: engineering-core
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "plugins/devops/mattyp-changelog/commands/changelog-validate.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/plugins/devops/mattyp-changelog/commands/changelog-validate.md
---


# /changelog-validate

Validate `.changelog-config.json` before generating a changelog.

## Checks

- Config exists and is valid JSON
- Required environment variables exist (e.g., `GITHUB_TOKEN`, optional `SLACK_TOKEN`)
- Template path exists
- Output path is writable

If validation fails, show actionable fixes (missing token env vars, missing template, invalid paths).

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `plugins/devops/mattyp-changelog/commands/changelog-validate.md`
