---
name: comment-checker
description: "Use when Codex needs to understand or respond to automatic comment-checker feedback emitted after an edit-like PostToolUse hook."
category: ai-agents-and-harness
source_repo: code-yeongyu/oh-my-openagent
source_path: "packages/omo-codex/plugin/components/comment-checker/skills/comment-checker/SKILL.md"
source_url: https://github.com/code-yeongyu/oh-my-openagent/blob/HEAD/packages/omo-codex/plugin/components/comment-checker/skills/comment-checker/SKILL.md
---
# Codex Comment Checker

The plugin registers a `PostToolUse` hook for successful `apply_patch`, `write`, `edit`, `multi_edit`, and `multiedit` calls.

When comment-checker reports a warning after a patch, Codex receives blocking feedback and should fix or explain the flagged comment before moving on.

## Scope

- No MCP tool is exposed.
- Non-edit tools are ignored by this plugin.
- Missing checker binaries emit no hook output so normal Codex work can continue.

---

**Source:** [`code-yeongyu/oh-my-openagent`](https://github.com/code-yeongyu/oh-my-openagent) → `packages/omo-codex/plugin/components/comment-checker/skills/comment-checker/SKILL.md`
