---
name: gh-daily-report
description: "Analyze the top issues and PRs from these ComfyUI ecosystem repositories and create a morning briefing:"
category: media-and-creative
source_repo: Comfy-Org/comfy-claude-prompt-library
source_path: ".claude/commands/github/GH-daily-report.md"
source_url: https://github.com/Comfy-Org/comfy-claude-prompt-library/blob/HEAD/.claude/commands/github/GH-daily-report.md
---
Analyze the top issues and PRs from these ComfyUI ecosystem repositories and create a morning briefing:

- comfyanonymous/ComfyUI
- Comfy-Org/ComfyUI_frontend  
- Comfy-Org/desktop
- Comfy-Org/rfcs
- Comfy-Org/comfy-cli

For each repository:
1. Use gh to fetch recent open issues: gh issue list --repo <owner/repo> --limit 20 --state open
2. Identify the top 5-7 most important issues based on:
   - Labels (bug, enhancement, priority, breaking)
   - Number of comments/reactions
   - Recent activity (updated within last week)
   - Milestone/project assignment

Create a concise morning briefing with:

## ComfyUI Ecosystem Daily Digest

### Critical Issues
- Any bugs blocking core functionality
- Security vulnerabilities
- Breaking changes needing attention

### Repository Summaries
For each repo:
- **[Repo Name]** - Brief one-line description
  - Top issues with: #number, title, impact summary, assignee
  - Key PRs in review
  - Community requests trending

### Cross-Repository Themes
- Common issues affecting multiple repos
- Ecosystem-wide initiatives
- Community sentiment/feedback patterns

Format for quick scanning during morning coffee.

---

**Source:** [`Comfy-Org/comfy-claude-prompt-library`](https://github.com/Comfy-Org/comfy-claude-prompt-library) → `.claude/commands/github/GH-daily-report.md`
