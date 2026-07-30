---
name: yt-ideate
description: "Generate and validate video ideas aligned with content pillars"
allowed-tools: "Read, Write, Edit, Bash, Grep, Glob, Task, WebSearch, AskUserQuestion"
model: "sonnet"
category: marketing-and-growth
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "plugins/productivity/youtube-strategy/commands/yt-ideate.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/plugins/productivity/youtube-strategy/commands/yt-ideate.md
---


Run the YouTube Ideation skill. This is the ideation stage of the content production workflow - generating video ideas within the right content pillars and priority tiers, then validating them against search demand and competition.

Read the skill definition at `skills/yt-ideation/SKILL.md` and follow its workflow exactly.

**You are the orchestrator.** Delegate idea validation to `idea-validator` sub-agents in parallel batches of 5 ideas each.

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `plugins/productivity/youtube-strategy/commands/yt-ideate.md`
