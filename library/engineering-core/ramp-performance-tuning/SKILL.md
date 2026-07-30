---
name: ramp-performance-tuning
description: "\"Ramp performance tuning \\u2014 corporate card and expense management\\ \\ API integration.\\nUse when working with Ramp for card management, expenses, or\\ \\ accounting sync.\\nTrigger with phrases like \\\"ramp performance tuning\\\", \\\"ramp-performance-tuning\\\"\\ , \\\"corporate card API\\\".\\n\""
allowed-tools: "Read, Write, Edit, Bash(npm:*), Bash(curl:*), Grep"
category: engineering-core
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "skills/.curated/ramp-performance-tuning/SKILL.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/skills/.curated/ramp-performance-tuning/SKILL.md
---

# Ramp Performance Tuning

## Overview

Implementation patterns for Ramp performance tuning using the Developer API with OAuth2 authentication.

## Prerequisites

- Completed `ramp-install-auth` setup

## Instructions

### Step 1: API Call Pattern

```python
import os, requests

# Obtain token
token_resp = requests.post(f"{os.environ['RAMP_BASE_URL'].replace('/v1','')}/v1/token", data={
    "grant_type": "client_credentials",
    "client_id": os.environ["RAMP_CLIENT_ID"],
    "client_secret": os.environ["RAMP_CLIENT_SECRET"],
})
access_token = token_resp.json()["access_token"]
headers = {"Authorization": f"Bearer {access_token}"}

cards = requests.get(f"{os.environ['RAMP_BASE_URL']}/cards", headers=headers)
print(f"Cards: {len(cards.json()['data'])}")
```

## Output

- Ramp API integration for performance tuning

## Error Handling

| Error | Cause | Solution |
|-------|-------|----------|
| 401 Unauthorized | Expired token | Re-authenticate |
| 429 Rate Limited | Too many requests | Implement backoff |
| 403 Forbidden | Insufficient permissions | Check API app permissions |

## Resources

- [Ramp API Documentation](https://docs.ramp.com/)
- [Authorization](https://docs.ramp.com/developer-api/v1/authorization)

## Next Steps

See related Ramp skills for more workflows.

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `skills/.curated/ramp-performance-tuning/SKILL.md`

**Also appears in:** `jeremylongshore/claude-code-plugins-plus-skills/plugins/saas-packs/ramp-pack/skills/ramp-performance-tuning/SKILL.md`
