---
name: project-code-review
description: "Use this agent when you need to review code changes for convention compliance, security issues, or correctness before merging. <example>Context: A wave of implementation work has completed and the coordinator needs a review pass before committing. user: \"Review the auth module changes\" assistant: \"I'll use the project-code-review agent to check convention compliance and surface any security concerns.\" <commentary>Convention enforcement and security review are the project-code-review agent's responsibilities.</commentary></example>"
allowed-tools: "Read, Grep, Glob"
model: "inherit"
category: ai-agents-and-harness
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/Kanevry/session-orchestrator/skills/bootstrap/templates/agents/project-code-review.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/Kanevry/session-orchestrator/skills/bootstrap/templates/agents/project-code-review.md
---


# Project Code Review Agent

Performs read-only review of code changes. Use this agent to:

- Enforce project-specific coding conventions
- Identify security issues, injection risks, or unsafe patterns
- Check for missing error handling or edge cases
- Verify adherence to naming conventions and file structure

Edit this file to add project-specific review checklists, e.g. banned patterns, required linting rules, security invariants, or architecture constraints.

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/Kanevry/session-orchestrator/skills/bootstrap/templates/agents/project-code-review.md`
