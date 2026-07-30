---
name: persona-upgrade-migration
description: "'Upgrade Persona API versions and handle breaking changes. Use when working with Persona identity verification. Trigger with phrases like \"persona upgrade-migration\", \"persona upgrade-migration\". '"
allowed-tools: "Read, Write, Edit, Bash(npm:*), Bash(git:*)"
category: prompt-engineering
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "skills/.curated/persona-upgrade-migration/SKILL.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/skills/.curated/persona-upgrade-migration/SKILL.md
---

# persona upgrade migration | sed 's/\b\(.\)/\u\1/g'

## Overview

API versioning via Persona-Version header, deprecated field migration, test against sandbox.

## Prerequisites

- Completed `persona-install-auth` setup
- Valid Persona API key (sandbox or production)

## Instructions

### Step 1: Implementation

```python
import os, requests

HEADERS = {
    "Authorization": f"Bearer {os.environ['PERSONA_API_KEY']}",
    "Persona-Version": "2023-01-05",
}
BASE = "https://withpersona.com/api/v1"

# Upgrade Persona API versions and handle breaking changes
resp = requests.get(f"{BASE}/inquiries?page[size]=10", headers=HEADERS)
resp.raise_for_status()
inquiries = resp.json()["data"]
for inq in inquiries:
    print(f"  {inq['id']}: {inq['attributes']['status']}")
```

## Output

- API versioning via Persona-Version header, deprecated field migration, test against sandbox.

## Error Handling

| Error | Cause | Solution |
|-------|-------|----------|
| 401 Unauthorized | Invalid API key | Check PERSONA_API_KEY |
| 429 Rate Limited | Too many requests | Implement backoff |
| 404 Not Found | Wrong resource ID | Verify ID format |

## Resources

- [Persona API Reference](https://docs.withpersona.com/reference/introduction)
- [Persona Documentation](https://docs.withpersona.com)

## Next Steps

See related Persona skills for more workflows.

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `skills/.curated/persona-upgrade-migration/SKILL.md`

**Also appears in:** `jeremylongshore/claude-code-plugins-plus-skills/plugins/saas-packs/persona-pack/skills/persona-upgrade-migration/SKILL.md`
