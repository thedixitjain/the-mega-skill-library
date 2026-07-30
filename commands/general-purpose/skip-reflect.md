---
name: skip-reflect
description: "Discard queued learnings without processing"
allowed-tools: "Bash"
category: general-purpose
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "skills/.curated/claude-reflect/commands/skip-reflect.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/skills/.curated/claude-reflect/commands/skip-reflect.md
---


## Context

- Queue count: !`jq 'length' ~/.claude/learnings-queue.json 2>/dev/null || echo 0`

## Your Task

1. If queue is empty:
   - Output: "Queue is already empty. Nothing to skip."
   - Exit

2. If queue has items:
   - Show: "You are about to discard [count] learning(s). These will be lost:"
   - List each queued item briefly (type + first 50 chars of message)
   - Ask: "Are you sure? [y/n]"

3. If user confirms (y/yes):
   - Clear the queue:

   ```bash
   echo "[]" > ~/.claude/learnings-queue.json
   ```

   - Output: "Discarded [count] learnings. Queue cleared."

4. If user declines (n/no):
   - Output: "Aborted. Run /reflect to process learnings instead."

## Note

This is an escape hatch for when auto-detection captures false positives
or learnings aren't worth saving. Use sparingly.

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `skills/.curated/claude-reflect/commands/skip-reflect.md`

**Also appears in:** `jeremylongshore/claude-code-plugins-plus-skills/plugins/community/claude-reflect/commands/skip-reflect.md`
