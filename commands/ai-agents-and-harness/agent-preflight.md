---
name: agent-preflight
description: "Preflight a repo before AI agents change files"
category: ai-agents-and-harness
source_repo: davepoon/buildwithclaude
source_path: "plugins/all-commands/commands/agent-preflight.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/all-commands/commands/agent-preflight.md
---


# Agent Preflight

Run this before letting Claude Code, Codex, Cursor, or another coding agent modify a real repository. The goal is to make the agent produce a short, reviewable safety receipt before any file-changing work starts.

## Instructions

1. **Identify the proposed agent task**
   - Restate the requested change in one sentence.
   - List the files, directories, commands, secrets, services, and package managers the agent is likely to touch.
   - Flag any task that asks for credentials, payment details, KYC, production deploys, destructive commands, private prompt extraction, or unclear external network access.

2. **Map the repository blast radius**
   - Inspect the project layout, dependency manifests, test commands, CI config, lockfiles, and deployment files.
   - Identify protected paths such as `.env*`, secrets, auth code, billing code, migration files, infra config, release scripts, and generated artifacts.
   - Separate safe read-only exploration from write operations.

3. **Score the change before editing**
   - Mark the task `Green` when it is local, reversible, tested, and limited to low-risk files.
   - Mark it `Yellow` when it touches dependencies, config, generated code, authentication-adjacent logic, or unclear test coverage.
   - Mark it `Red` when it may expose secrets, change payment/auth/deployment behavior, delete data, or run untrusted code.

4. **Create guardrails for the agent run**
   - State the allowed files and commands.
   - State the blocked files and commands.
   - Require a branch or patch workflow for Yellow/Red work.
   - Require tests, lint, or a dry-run command before reporting success.
   - Require the agent to stop and ask before crossing any listed boundary.

5. **Produce a preflight receipt**
   - Output a concise Markdown receipt with: task summary, risk level, allowed scope, blocked scope, test plan, rollback plan, and exact stop conditions.
   - Do not perform the actual implementation in the same response unless the user explicitly approves the receipt.

## Receipt template

```markdown
# Agent preflight receipt

Task: <one-sentence task>
Risk: Green | Yellow | Red

Allowed scope:
- <files/directories/commands the agent may use>

Blocked scope:
- <files/directories/commands/secrets/payment/deploy actions the agent must not touch>

Required verification:
- <tests/lint/build/manual checks>

Rollback plan:
- <branch, patch, revert, backup, or restore step>

Stop conditions:
- <conditions requiring human approval before continuing>
```

## Optional reference

For a copy-paste scanner pattern and example AI-agent repo-risk receipts, see the free repo: <https://github.com/el-zachariah/ai-agent-safety-starter-pack>.

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/all-commands/commands/agent-preflight.md`

**Also appears in:** `davepoon/buildwithclaude/plugins/commands-code-analysis-testing/commands/agent-preflight.md`
