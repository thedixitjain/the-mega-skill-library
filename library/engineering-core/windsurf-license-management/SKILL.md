---
name: windsurf-license-management
description: "'Manage Windsurf licenses and seat allocation. Activate when users mention \"license management\", \"seat allocation\", \"billing optimization\", \"user licenses\", or \"subscription management\". Handles license administration. Use when working with windsurf license management functionality. Trigger with phrases like \"windsurf license management\", \"windsurf management\", \"windsurf\". '"
allowed-tools: "Read,Write,Edit"
category: engineering-core
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "skills/.curated/windsurf-license-management/SKILL.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/skills/.curated/windsurf-license-management/SKILL.md
---

# Windsurf License Management

## Overview

This skill enables enterprise license management for Windsurf deployments. It covers seat allocation, usage tracking, cost optimization, and compliance reporting.

## Prerequisites

- Windsurf Enterprise subscription with admin access
- Organization administrator role
- Access to billing portal
- User directory integration (optional: SCIM, Azure AD, Okta)
- Understanding of organization structure and teams

## Instructions

1. **Inventory Current Licenses**
2. **Set Allocation Policies**
3. **Configure Usage Tracking**
4. **Optimize Subscription**
5. **Monitor and Report**

See `${CLAUDE_SKILL_DIR}/references/implementation.md` for detailed implementation guide.

## Output

- License inventory with current allocations
- Utilization reports with recommendations
- Cost analysis with optimization opportunities
- Compliance reports for audits

## Error Handling

See `${CLAUDE_SKILL_DIR}/references/errors.md` for comprehensive error handling.

## Examples

See `${CLAUDE_SKILL_DIR}/references/examples.md` for detailed examples.

## Resources

- [Windsurf License Administration](https://docs.windsurf.ai/admin/licensing)
- [SCIM Integration Guide](https://docs.windsurf.ai/admin/scim)
- [Cost Optimization Best Practices](https://docs.windsurf.ai/admin/cost-optimization)

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `skills/.curated/windsurf-license-management/SKILL.md`

**Also appears in:** `jeremylongshore/claude-code-plugins-plus-skills/plugins/saas-packs/skill-databases/windsurf/skills/windsurf-license-management/SKILL.md`
