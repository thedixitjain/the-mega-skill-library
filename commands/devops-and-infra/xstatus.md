---
name: xstatus
description: "Show X account status, credit balance, and active monitors"
allowed-tools: "Bash(curl:*), WebFetch"
category: devops-and-infra
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "plugins/devops/tweetclaw/commands/xstatus.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/plugins/devops/tweetclaw/commands/xstatus.md
---


Check the current X account status, credit balance, active monitors, and webhook configurations.

1. Fetch account info: `GET /x/account`
2. Fetch credit balance: `GET /credits`
3. Fetch active monitors: `GET /monitors`
4. Display a summary table with account details, remaining credits, and monitor count

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `plugins/devops/tweetclaw/commands/xstatus.md`
