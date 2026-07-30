---
name: veeva-observability
description: "'Veeva Vault observability for enterprise operations. Use when implementing advanced Veeva Vault patterns. Trigger: \"veeva observability\". '"
allowed-tools: "Read, Write, Edit, Grep"
category: devops-and-infra
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "plugins/saas-packs/veeva-pack/skills/veeva-observability/SKILL.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/plugins/saas-packs/veeva-pack/skills/veeva-observability/SKILL.md
---

# Veeva Vault Observability

## Overview

Enterprise-grade observability patterns for Veeva Vault deployments.

## Instructions

### Key Considerations

- Veeva Vault is purpose-built for regulated life sciences
- All API changes should be validated against compliance requirements
- Use VQL for efficient data retrieval
- VAPIL provides Java-native API coverage

## Error Handling

| Error | Cause | Solution |
|-------|-------|----------|
| Access denied | Security profile | Update profile permissions |
| Data validation | Required fields | Check object metadata |

## Resources

- [Vault API Reference](https://developer.veevavault.com/api/)
- [Vault Documentation](https://developer.veevavault.com/docs/)

## Next Steps

See related Veeva Vault skills.

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `plugins/saas-packs/veeva-pack/skills/veeva-observability/SKILL.md`
