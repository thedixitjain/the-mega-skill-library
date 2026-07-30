---
name: techsmith-deploy-integration
description: "'TechSmith deploy integration for Snagit COM API and Camtasia automation. Use when working with TechSmith screen capture and video editing automation. Trigger: \"techsmith deploy integration\". '"
allowed-tools: "Read, Write, Edit, Bash(powershell:*), Grep"
category: mcp-and-integrations
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "plugins/saas-packs/techsmith-pack/skills/techsmith-deploy-integration/SKILL.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/plugins/saas-packs/techsmith-pack/skills/techsmith-deploy-integration/SKILL.md
---

# TechSmith Deploy Integration

## Overview

Guidance for deploy integration with TechSmith Snagit COM API and Camtasia automation.

## Instructions

### Key Considerations

- Snagit COM API is Windows-only (requires COM registration)
- Camtasia Producer CLI for batch rendering
- PowerShell is the primary scripting language
- Python interop via `pywin32` (`pip install pywin32`)

### Snagit COM Input Types

| Value | Constant | Description |
|-------|----------|-------------|
| 0 | siiDesktop | Full desktop |
| 2 | siiRegion | User-selected region |
| 4 | siiWindow | Active window |
| 5 | siiFile | From file |

### Snagit COM Output Types

| Value | Constant | Description |
|-------|----------|-------------|
| 1 | sioClipboard | Copy to clipboard |
| 2 | sioFile | Save to file |
| 4 | sioPrinter | Send to printer |

## Error Handling

| Error | Cause | Solution |
|-------|-------|----------|
| COM not registered | Snagit not installed | Install and register COM server |
| Permission denied | Not running as admin | Elevate PowerShell |
| File locked | Snagit Editor has file open | Close editor first |

## Resources

- [Snagit COM Samples](https://github.com/TechSmith/Snagit-COM-Samples)
- [TechSmith Support](https://support.techsmith.com/)

## Next Steps

See related TechSmith skills for more automation patterns.

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `plugins/saas-packs/techsmith-pack/skills/techsmith-deploy-integration/SKILL.md`
