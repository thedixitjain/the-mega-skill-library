---
name: sync-pull
description: "Use when the user wants to restore, download, or pull their Claude Code config from GitHub onto this machine."
allowed-tools: "Bash(bash \"${CLAUDE_PLUGIN_ROOT}/scripts/*\"), Bash(gh *), Bash(git *), Read"
category: ai-agents-and-harness
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "plugins/productivity/claudebase/skills/sync-pull/SKILL.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/plugins/productivity/claudebase/skills/sync-pull/SKILL.md
---


# Config Sync Pull

Pull configuration from your GitHub backup repo and apply it to the local machine.

## What happens

1. **Backup** — Current local config is backed up to plugin data directory (timestamped, keeps last 10)
2. **Apply shared** — Files from `shared/` directory are applied first (base layer)
3. **Apply profile** — Profile-specific files overlay on top (overrides shared where both exist)
4. **Apply global** — User-level settings from `global/` are applied to `~/.claude/`
5. **Verify** — JSON config files are validated for correct syntax

## Instructions

Parse user arguments and run the pull script:

```bash
bash "${CLAUDE_PLUGIN_ROOT}/scripts/sync-pull.sh" [OPTIONS]
```

**Options:**
- `--profile NAME` — Pull a specific profile (default: active profile)
- `--dry-run` — Show what would be applied without writing any files
- `--no-backup` — Skip backup step (use with caution)
- `--yes` / `-y` — Skip confirmation prompt (auto-approve)
- `--include-global` — Also pull `~/.claude/settings.json` (global settings are opt-in)

### Profile switching

If the user specifies a different profile than their current one, this effectively switches their setup. Let them know which profile they're switching from/to.

### After pull

Tell the user:
- How many files were applied
- Any validation warnings
- That a backup was created (and where)
- They may need to restart Claude Code for some settings to take effect

## User Arguments

$ARGUMENTS

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `plugins/productivity/claudebase/skills/sync-pull/SKILL.md`
