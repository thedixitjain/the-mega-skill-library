---
name: cancel-skill-improver
description: "Stops, cancels, or aborts the active skill improvement loop while preserving all changes made to skill files. Use to manually stop, cancel, abort, or kill the iteration process early."
allowed-tools: "Bash(${CLAUDE_PLUGIN_ROOT}/scripts/cancel-skill-improver.sh:*)"
category: general-purpose
source_repo: trailofbits/skills
source_path: "plugins/skill-improver/commands/cancel-skill-improver.md"
source_url: https://github.com/trailofbits/skills/blob/HEAD/plugins/skill-improver/commands/cancel-skill-improver.md
---


# Cancel Skill Improver

Cancel the active skill improvement loop:

```!
"${CLAUDE_PLUGIN_ROOT}/scripts/cancel-skill-improver.sh" "$ARGUMENTS"
```

All changes made to the skill files during the improvement loop are preserved.

If multiple improvement sessions are active (from parallel Claude Code instances), provide the session ID shown in the list.

---

**Source:** [`trailofbits/skills`](https://github.com/trailofbits/skills) → `plugins/skill-improver/commands/cancel-skill-improver.md`
