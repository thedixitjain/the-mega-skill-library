---
name: veeva-data-handling
description: "'Veeva Vault data handling for enterprise operations. Use when implementing advanced Veeva Vault patterns. Trigger: \"veeva data handling\". '"
allowed-tools: "Read, Write, Edit, Grep"
category: backend-and-data
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "plugins/saas-packs/veeva-pack/skills/veeva-data-handling/SKILL.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/plugins/saas-packs/veeva-pack/skills/veeva-data-handling/SKILL.md
---

# Veeva Vault Data Handling

## Overview

Enterprise-grade data handling patterns for Veeva Vault deployments.

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

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `plugins/saas-packs/veeva-pack/skills/veeva-data-handling/SKILL.md`
