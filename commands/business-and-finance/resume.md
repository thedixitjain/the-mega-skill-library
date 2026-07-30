---
name: resume
description: "Continue a completed/failed/cancelled Codex agent with a new prompt"
category: business-and-finance
source_repo: davepoon/buildwithclaude
source_path: "plugins/magic-cc-codex-worker/commands/resume.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/magic-cc-codex-worker/commands/resume.md
---


Parse `$ARGUMENTS` as `<agent_id> <prompt...>`.

Call `magic-codex` MCP tool `resume` with `agent_id` and `prompt`. If the tool rejects (still running, no thread_id, etc.), explain the reason clearly.

After success, remind the user to poll `/magic-codex:status $agent_id`.

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/magic-cc-codex-worker/commands/resume.md`
