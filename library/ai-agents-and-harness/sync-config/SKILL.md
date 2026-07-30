---
name: sync-config
description: "Use when the user wants to view or change claudebase settings like global sync, agent skills sync, auto-push, or machine ID."
allowed-tools: "Bash(bash \"${CLAUDE_PLUGIN_ROOT}/scripts/*\"), Read"
category: ai-agents-and-harness
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "plugins/productivity/claudebase/skills/sync-config/SKILL.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/plugins/productivity/claudebase/skills/sync-config/SKILL.md
---


# Config Sync Settings

View and modify claudebase configuration.

## Instructions

Run the config manager script with the appropriate action:

```bash
bash "${CLAUDE_PLUGIN_ROOT}/scripts/config-manager.sh" ACTION [KEY] [VALUE]
```

### Actions

- **show** (default) — Display all current settings
- **set `<key>` `<value>`** — Change a setting
- **get `<key>`** — Read a single setting
- **reset `<key>`** — Remove a setting (revert to default)

### Configurable keys

| Key | Values | Description |
|-----|--------|-------------|
| `include_global` | `true`/`false` | Sync `~/.claude/settings.json` on push/pull |
| `sync_agent_skills` | `true`/`false` | Sync `skills-lock.json` (lock file only; prints install commands on pull) |
| `auto_push` | `true`/`false` | Auto-push config when a Claude Code session ends |
| `machine_id` | any string | Identifier for this machine (used in multi-machine warnings) |

### Examples

- `/sync-config` — show all settings
- `/sync-config set include_global true` — enable global settings sync
- `/sync-config set auto_push false` — disable auto-push

## User Arguments

$ARGUMENTS

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `plugins/productivity/claudebase/skills/sync-config/SKILL.md`
