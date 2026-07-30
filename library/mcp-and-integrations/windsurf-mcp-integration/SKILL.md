---
name: windsurf-mcp-integration
description: "'Manage integrate MCP servers with Windsurf for extended capabilities. Activate when users mention \"mcp integration\", \"model context protocol\", \"external tools\", \"mcp server\", or \"cascade tools\". Handles MCP server configuration and integration. Use when working with windsurf mcp integration functionality. Trigger with phrases like \"windsurf mcp integration\", \"windsurf integration\", \"windsurf\". '"
allowed-tools: "Read,Write,Edit,Bash(cmd:*)"
category: mcp-and-integrations
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "skills/.curated/windsurf-mcp-integration/SKILL.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/skills/.curated/windsurf-mcp-integration/SKILL.md
---

# Windsurf Mcp Integration

## Overview

This skill enables integration of MCP (Model Context Protocol) servers with Windsurf, extending Cascade's capabilities with external tools and services. MCP allows Cascade to interact with databases, filesystems, APIs, and custom tools through a standardized protocol.

## Prerequisites

- Windsurf IDE with MCP support enabled
- Node.js 18+ or Python 3.10+ for MCP servers
- MCP server packages installed (npm or pip)
- Network access for remote MCP servers
- Understanding of MCP protocol basics
- Admin permissions for server configuration

## Instructions

1. **Enable MCP Servers**
2. **Configure Tools**
3. **Set Up Authentication**
4. **Test Integration**
5. **Deploy to Team**

See `${CLAUDE_SKILL_DIR}/references/implementation.md` for detailed implementation guide.

## Output

- Configured MCP servers accessible via Cascade
- Tool registry with all available operations
- Permission matrix for access control
- Audit logs for tool invocations

## Error Handling

See `${CLAUDE_SKILL_DIR}/references/errors.md` for comprehensive error handling.

## Examples

See `${CLAUDE_SKILL_DIR}/references/examples.md` for detailed examples.

## Resources

- [MCP Protocol Specification](https://modelcontextprotocol.io/docs)
- [Windsurf MCP Guide](https://docs.windsurf.ai/features/mcp)
- MCP Server Development

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `skills/.curated/windsurf-mcp-integration/SKILL.md`

**Also appears in:** `jeremylongshore/claude-code-plugins-plus-skills/plugins/saas-packs/skill-databases/windsurf/skills/windsurf-mcp-integration/SKILL.md`
