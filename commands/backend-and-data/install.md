---
name: install
description: "Install dependencies and start the dev server"
category: backend-and-data
source_repo: coleam00/ai-transformation-workshop
source_path: ".claude/commands/install.md"
source_url: https://github.com/coleam00/ai-transformation-workshop/blob/HEAD/.claude/commands/install.md
---


# Install

## Run

Think through each step carefully to ensure nothing is missed.

### Install & Setup

1. Install dependencies: `bun install`
2. Push database schema: `bun run db:push`
3. Start dev server: `bun run dev`
4. Verify app is running at http://localhost:3000

This is a Next.js monolith — one package.json, one dev server, no separate backend.

## Report

Output what you've done in a concise bullet point list:
- Dependencies: installed or already up to date
- Database: schema pushed to `local.db`
- Dev server: http://localhost:3000
- Any issues encountered

---

**Source:** [`coleam00/ai-transformation-workshop`](https://github.com/coleam00/ai-transformation-workshop) → `.claude/commands/install.md`
