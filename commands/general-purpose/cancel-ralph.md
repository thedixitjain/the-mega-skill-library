---
name: cancel-ralph
description: "Cancel active Ralph Wiggum loop"
allowed-tools: "[\"Bash(test -f .claude/ralph-loop.local.md:*)\", \"Bash(rm .claude/ralph-loop.local.md)\", \"Read(.claude/ralph-loop.local.md)\"]"
category: general-purpose
source_repo: anthropics/claude-code
source_path: "plugins/ralph-wiggum/commands/cancel-ralph.md"
source_url: https://github.com/anthropics/claude-code/blob/HEAD/plugins/ralph-wiggum/commands/cancel-ralph.md
---
# Cancel Ralph

To cancel the Ralph loop:

1. Check if `.claude/ralph-loop.local.md` exists using Bash: `test -f .claude/ralph-loop.local.md && echo "EXISTS" || echo "NOT_FOUND"`

2. **If NOT_FOUND**: Say "No active Ralph loop found."

3. **If EXISTS**:
   - Read `.claude/ralph-loop.local.md` to get the current iteration number from the `iteration:` field
   - Remove the file using Bash: `rm .claude/ralph-loop.local.md`
   - Report: "Cancelled Ralph loop (was at iteration N)" where N is the iteration value

---

**Source:** [`anthropics/claude-code`](https://github.com/anthropics/claude-code) → `plugins/ralph-wiggum/commands/cancel-ralph.md`

**Also appears in:** `anthropics/claude-plugins-official/plugins/ralph-loop/commands/cancel-ralph.md`
