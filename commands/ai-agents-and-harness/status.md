---
name: status
description: "Show status of Codex agents — one agent by id, or all"
category: ai-agents-and-harness
source_repo: davepoon/buildwithclaude
source_path: "plugins/magic-cc-codex-worker/commands/status.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/magic-cc-codex-worker/commands/status.md
---


If `$ARGUMENTS` contains an agent_id (starts with `codex-`), call the `magic-codex` MCP `status` tool with `agent_id`. Otherwise call it with no args.

Render the response as a compact table: agent_id, role, status, started_at, last_output_preview. For all-agent queries, include the summary counts.

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/magic-cc-codex-worker/commands/status.md`
