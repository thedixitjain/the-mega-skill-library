---
name: git-commits
description: "Git Commit Rules"
category: engineering-core
source_repo: parcadei/Continuous-Claude-v3
source_path: ".claude/skills/git-commits/SKILL.md"
source_url: https://github.com/parcadei/Continuous-Claude-v3/blob/HEAD/.claude/skills/git-commits/SKILL.md
---


# Git Commit Rules

When the user asks to commit, push, or save changes to git:

## MUST Use /commit Skill

**DO NOT** run `git commit` directly. Instead:

```
Skill("commit")
```

The `/commit` skill:
1. Removes Claude attribution from commits
2. Generates reasoning.md capturing what was tried
3. Clears build attempts for next feature

## Why This Matters

- Regular `git commit` adds "Generated with Claude Code" and Co-Author lines
- The `/commit` skill removes these so commits appear user-authored
- Reasoning capture preserves build history for future sessions

## Trigger Words

When you see these in user prompts, use the commit skill:
- "commit", "push", "save changes"
- "push to github", "push changes"
- "commit and push"

## After Commit

The skill will prompt you to run:
```bash
bash "$CLAUDE_PROJECT_DIR/.claude/scripts/generate-reasoning.sh" <hash> "<message>"
```

Then push if requested:
```bash
git push origin <branch>
```

---

**Source:** [`parcadei/Continuous-Claude-v3`](https://github.com/parcadei/Continuous-Claude-v3) → `.claude/skills/git-commits/SKILL.md`
