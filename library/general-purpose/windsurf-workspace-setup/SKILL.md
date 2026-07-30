---
name: windsurf-workspace-setup
description: "'Initialize Windsurf workspace with project-specific AI rules. Activate when users mention \"create windsurfrules\", \"setup workspace\", \"configure project ai\", \"initialize windsurf workspace\", or \"migrate to windsurf\". Handles workspace configuration and team standardization. Use when working with windsurf workspace setup functionality. Trigger with phrases like \"windsurf workspace setup\", \"windsurf setup\", \"windsurf\". '"
allowed-tools: "Read,Write,Edit,Bash(cmd:*)"
category: general-purpose
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "skills/.curated/windsurf-workspace-setup/SKILL.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/skills/.curated/windsurf-workspace-setup/SKILL.md
---

# Windsurf Workspace Setup

## Overview

This skill enables rapid workspace setup for Windsurf projects. It covers creating .windsurfrules for AI behavior, configuring editor settings, establishing team conventions, and setting up multi-root workspaces.

## Prerequisites

- Windsurf IDE installed
- Project repository cloned
- Understanding of project architecture
- Team conventions documented
- Admin access for team-wide settings (optional)

## Instructions

1. **Create .windsurfrules**
2. **Configure Editor Settings**
3. **Set Up Extensions**
4. **Configure Cross-Editor Consistency**
5. **Establish Team Standards**

See `${CLAUDE_SKILL_DIR}/references/implementation.md` for detailed implementation guide.

## Output

- Configured .windsurfrules file
- Editor settings.json
- Extension recommendations
- Cross-editor configuration files
- Workspace configuration for monorepos

## Error Handling

See `${CLAUDE_SKILL_DIR}/references/errors.md` for comprehensive error handling.

## Examples

See `${CLAUDE_SKILL_DIR}/references/examples.md` for detailed examples.

## Resources

- [Windsurf Workspace Guide](https://docs.windsurf.ai/features/workspace)
- [.windsurfrules Reference](https://docs.windsurf.ai/reference/windsurfrules)
- [Multi-Root Workspaces](https://docs.windsurf.ai/features/multi-root)

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `skills/.curated/windsurf-workspace-setup/SKILL.md`

**Also appears in:** `jeremylongshore/claude-code-plugins-plus-skills/plugins/saas-packs/skill-databases/windsurf/skills/windsurf-workspace-setup/SKILL.md`
