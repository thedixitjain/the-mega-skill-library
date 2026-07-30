---
name: merge
description: "Merge a completed Codex implementer's worktree back into its base_ref"
category: ai-agents-and-harness
source_repo: davepoon/buildwithclaude
source_path: "plugins/magic-cc-codex-worker/commands/merge.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/magic-cc-codex-worker/commands/merge.md
---


Parse `$ARGUMENTS`: first token is `agent_id`. Optional flags:
- `--strategy squash|ff|rebase` (default: squash)
- `--keep-worktree` (don't auto-remove after)
- `--message "commit msg"` (for squash strategy)

Call `magic-codex` MCP tool `merge`. On success, show the merged SHA and base ref. On conflict or other failure, surface the error and suggest manual resolution inside the worktree.

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/magic-cc-codex-worker/commands/merge.md`
