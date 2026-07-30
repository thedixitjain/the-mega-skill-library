---
name: maestro-update
description: "Update Maestro to the latest marketplace version for Codex"
category: ai-agents-and-harness
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/mbanderas/maestro/codex-skills/maestro-update/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/mbanderas/maestro/codex-skills/maestro-update/SKILL.md
---


Update **Maestro** to the latest Codex marketplace code. This refreshes the
configured Git marketplace and reinstalls the Maestro plugin from it.

When the user invokes this skill, run:

```bash
codex plugin marketplace upgrade maestro
codex plugin add maestro@maestro
```

The update is idempotent. It will:

- Pull the latest Maestro source from the repository.
- Refresh the installed Maestro plugin cache.
- Refresh bundled Codex skills and hooks exposed by the plugin.
- Leave project-local configuration (state files, secrets) untouched.

## Notes

- Requires the Codex CLI on `PATH`.
- After reinstalling, restart the Codex session or open a new thread so updated
  skills and hooks take effect.
- If the marketplace is not configured yet, run
  `codex plugin marketplace add mbanderas/maestro` first.
- Portable/manual installs can still be refreshed with
  `npx github:mbanderas/maestro install --target codex` from the project root.

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/mbanderas/maestro/codex-skills/maestro-update/SKILL.md`
