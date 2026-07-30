---
name: persona-reference-architecture
description: "'KYC service architecture with Persona as verification provider. Use when working with Persona identity verification. Trigger with phrases like \"persona reference-architecture\", \"persona reference-architecture\". '"
allowed-tools: "Read, Grep"
category: prompt-engineering
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "skills/.curated/persona-reference-architecture/SKILL.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/skills/.curated/persona-reference-architecture/SKILL.md
---

# persona reference architecture | sed 's/\b\(.\)/\u\1/g'

## Overview

Service architecture, inquiry lifecycle, webhook-driven processing, compliance patterns.

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

# KYC service architecture with Persona as verification provider
resp = requests.get(f"{BASE}/inquiries?page[size]=10", headers=HEADERS)
resp.raise_for_status()
inquiries = resp.json()["data"]
for inq in inquiries:
    print(f"  {inq['id']}: {inq['attributes']['status']}")
```

## Output

- Service architecture, inquiry lifecycle, webhook-driven processing, compliance patterns.

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

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `skills/.curated/persona-reference-architecture/SKILL.md`

**Also appears in:** `jeremylongshore/claude-code-plugins-plus-skills/plugins/saas-packs/persona-pack/skills/persona-reference-architecture/SKILL.md`
