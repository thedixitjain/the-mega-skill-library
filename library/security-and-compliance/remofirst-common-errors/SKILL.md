---
name: remofirst-common-errors
description: "\"RemoFirst common errors \\u2014 global HR, EOR, and payroll platform\\ \\ integration.\\nUse when working with RemoFirst for global employment, payroll,\\ \\ or compliance.\\nTrigger with phrases like \\\"remofirst common errors\\\", \\\"remofirst-common-errors\\\"\\ , \\\"global HR API\\\".\\n\""
allowed-tools: "Read, Write, Edit, Bash(npm:*), Bash(curl:*), Grep"
category: security-and-compliance
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "skills/.curated/remofirst-common-errors/SKILL.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/skills/.curated/remofirst-common-errors/SKILL.md
---

# RemoFirst Common Errors

## Overview

Implementation patterns for RemoFirst common errors — global HR and EOR platform integration.

## Prerequisites

- Completed `remofirst-install-auth` setup

## Instructions

### Step 1: API Pattern

```python
client = RemoFirstClient()
employees = client.get("/employees", params={"page_size": 10})
print(f"Employees: {len(employees['data'])}")
```

## Output

- RemoFirst integration for common errors

## Error Handling

| Error | Cause | Solution |
|-------|-------|----------|
| 401 Unauthorized | Invalid API key | Contact RemoFirst support |
| 429 Rate Limited | Too many requests | Implement backoff |
| 422 Validation Error | Missing required field | Check API documentation |

## Resources

- [RemoFirst](https://www.remofirst.com)

## Next Steps

See related RemoFirst skills for more workflows.

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `skills/.curated/remofirst-common-errors/SKILL.md`

**Also appears in:** `jeremylongshore/claude-code-plugins-plus-skills/plugins/saas-packs/remofirst-pack/skills/remofirst-common-errors/SKILL.md`
