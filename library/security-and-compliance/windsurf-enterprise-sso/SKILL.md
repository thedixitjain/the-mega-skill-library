---
name: windsurf-enterprise-sso
description: "'Configure enterprise SSO integration for Windsurf. Activate when users mention \"sso configuration\", \"single sign-on\", \"enterprise authentication\", \"saml setup\", or \"identity provider\". Handles enterprise identity integration. Use when working with windsurf enterprise sso functionality. Trigger with phrases like \"windsurf enterprise sso\", \"windsurf sso\", \"windsurf\". '"
allowed-tools: "Read,Write,Edit,Bash(cmd:*)"
category: security-and-compliance
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "skills/.curated/windsurf-enterprise-sso/SKILL.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/skills/.curated/windsurf-enterprise-sso/SKILL.md
---

# Windsurf Enterprise Sso

## Overview

This skill enables enterprise Single Sign-On (SSO) integration for Windsurf deployments. It supports SAML 2.0, OIDC/OAuth 2.0, and integration with major identity providers including Okta, Azure AD, and Google Workspace.

## Prerequisites

- Windsurf Enterprise subscription
- Organization administrator access
- Identity provider admin access
- Understanding of SAML/OIDC protocols
- Compliance requirements documented
- Certificate management capabilities

## Instructions

1. **Prepare Identity Provider**
2. **Configure Windsurf SSO**
3. **Set Up Certificates**
4. **Configure Policies**
5. **Test and Enable**

See `${CLAUDE_SKILL_DIR}/references/implementation.md` for detailed implementation guide.

## Output

- Configured SSO integration
- User attribute mappings
- Group sync configuration
- Audit logging setup

## Error Handling

See `${CLAUDE_SKILL_DIR}/references/errors.md` for comprehensive error handling.

## Examples

See `${CLAUDE_SKILL_DIR}/references/examples.md` for detailed examples.

## Resources

- [Windsurf SSO Guide](https://docs.windsurf.ai/admin/sso)
- [SAML 2.0 Configuration](https://docs.windsurf.ai/admin/saml)
- [OIDC Configuration](https://docs.windsurf.ai/admin/oidc)

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `skills/.curated/windsurf-enterprise-sso/SKILL.md`

**Also appears in:** `jeremylongshore/claude-code-plugins-plus-skills/plugins/saas-packs/skill-databases/windsurf/skills/windsurf-enterprise-sso/SKILL.md`
