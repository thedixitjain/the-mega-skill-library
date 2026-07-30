---
name: sys-configure
description: "Configure Claude Octopus — redirects to /octo:setup interactive wizard"
category: general-purpose
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/nyldn/claude-octopus/skills/sys-configure/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/nyldn/claude-octopus/skills/sys-configure/SKILL.md
---


> **Host: Codex CLI** — This skill was designed for Claude Code and adapted for Codex.
> Cross-reference commands use installed skill names in Codex rather than `/octo:*` slash commands.
> Use the active Codex shell and subagent tools. Do not claim a provider, model, or host subagent is available until the current session exposes it.
> For host tool equivalents, see `skills/blocks/codex-host-adapter.md`.


# Configuration → Setup Redirect

This skill is an alias for `/octo:setup`. When triggered, invoke the setup command directly.

**Action:** Run `/octo:setup` — the interactive setup wizard handles all configuration:
- Provider installation and auth
- RTK token optimization
- Work mode selection
- First-run onboarding

Do NOT duplicate setup logic here. Just invoke the setup skill.

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/nyldn/claude-octopus/skills/sys-configure/SKILL.md`
