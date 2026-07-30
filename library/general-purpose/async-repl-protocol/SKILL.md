---
name: async-repl-protocol
description: "Async REPL Protocol"
category: general-purpose
source_repo: parcadei/Continuous-Claude-v3
source_path: ".claude/skills/async-repl-protocol/SKILL.md"
source_url: https://github.com/parcadei/Continuous-Claude-v3/blob/HEAD/.claude/skills/async-repl-protocol/SKILL.md
---


# Async REPL Protocol

When working with Agentica's async REPL harness for testing.

## Rules

### 1. Use `await` for Future-returning tools

```python
content = await view_file(path)  # NOT view_file(path)
answer = await ask_memory("...")
```

### 2. Single code block per response

Compute AND return in ONE block. Multiple blocks means only first executes.

```python
# GOOD: Single block
content = await view_file(path)
return any(c.isdigit() for c in content)

# BAD: Split blocks (second block never runs)
content = await view_file(path)

---

**Source:** [`parcadei/Continuous-Claude-v3`](https://github.com/parcadei/Continuous-Claude-v3) → `.claude/skills/async-repl-protocol/SKILL.md`

**Also appears in:** `parcadei/Continuous-Claude-v3/.claude/skills/archive/async-repl-protocol/SKILL.md`
