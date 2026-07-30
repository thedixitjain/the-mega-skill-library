---
name: memstack
description: "127 production skills across 10 categories (Security, Deployment, Dev, Business, Content, SEO, Marketing, Product, Automation, Core). Skills auto-load based on your task. Includes localhost dashboard with Agent Runner, Burn Report, and session diary."
category: marketing-and-growth
source_repo: davepoon/buildwithclaude
source_path: "plugins/memstack/skills/memstack/SKILL.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/memstack/skills/memstack/SKILL.md
---


# MemStack

The structured skill framework for Claude Code.

## Install
/plugin marketplace add cwinvestments/memstack
/plugin install memstack@cwinvestments-memstack

## Pro Skills (42 additional)
pip install memstack-skill-loader
claude mcp add --scope user memstack-skills -- python -m memstack_skill_loader
activate_license(key="your-key", email="your-email")

## Features
- 127 skills across 10 categories, auto-loading based on task
- Localhost dashboard with Agent Runner (3-agent Manager/Builder/Reviewer)
- Burn Report tracking token usage and costs per skill
- Session diary with AI-authored markdown narratives
- Context window monitoring per agent
- Safe git staging to prevent accidental secret commits

More info: https://memstack.pro

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/memstack/skills/memstack/SKILL.md`
