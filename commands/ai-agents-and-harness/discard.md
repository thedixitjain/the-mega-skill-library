---
name: discard
description: "Discard a terminal Codex agent's worktree and delete its branch"
category: ai-agents-and-harness
source_repo: davepoon/buildwithclaude
source_path: "plugins/magic-cc-codex-worker/commands/discard.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/magic-cc-codex-worker/commands/discard.md
---


Parse `$ARGUMENTS` as `<agent_id>`. Call `magic-codex` MCP tool `discard`.

If the agent is still running, explain the user must `/magic-codex:cancel` first. This action is irreversible; warn before proceeding on any agent whose work has not been reviewed.

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/magic-cc-codex-worker/commands/discard.md`
