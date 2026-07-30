---
name: cancel
description: "Cancel a running Codex agent (optionally --force to also remove its worktree)"
category: ai-agents-and-harness
source_repo: davepoon/buildwithclaude
source_path: "plugins/magic-cc-codex-worker/commands/cancel.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/magic-cc-codex-worker/commands/cancel.md
---


Parse `$ARGUMENTS`. First token is the agent_id. If `--force` appears anywhere, pass `force: true` (also removes the worktree + branch).

Call `magic-codex` MCP tool `cancel` and report whether the worktree was preserved (the default) so the user can still inspect partial work.

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/magic-cc-codex-worker/commands/cancel.md`
