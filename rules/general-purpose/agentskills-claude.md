---
name: agentskills-claude
description: "Format and lint with ruff:"
category: general-purpose
source_repo: agentskills/agentskills
source_path: "skills-ref/CLAUDE.md"
source_url: https://github.com/agentskills/agentskills/blob/HEAD/skills-ref/CLAUDE.md
---
# Development

## Code Quality

Format and lint with ruff:

```bash
uv run ruff format .
uv run ruff check --fix .
```

## Testing

Run tests with pytest:

```bash
uv run pytest
```

---

**Source:** [`agentskills/agentskills`](https://github.com/agentskills/agentskills) → `skills-ref/CLAUDE.md`
