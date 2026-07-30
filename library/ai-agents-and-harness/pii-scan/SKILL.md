---
name: pii-scan
description: "Scan content for PII and secrets before writing files, sending messages, or including sensitive data in responses. Use before and after any operation that handles potentially sensitive content."
category: ai-agents-and-harness
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/getaxonflow/axonflow-codex-plugin/skills/pii-scan/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/getaxonflow/axonflow-codex-plugin/skills/pii-scan/SKILL.md
---


Before writing files or after tool calls that produce data, call the `check_output` MCP tool to scan for PII and secrets:

- `connector_type`: `codex.Write` (for file writes), `codex.Bash` (for command output), or the appropriate tool type
- `message`: the text content to scan — for file writes, scan the content being written

**Before file writes:** If the content being written contains PII (SSN, credit card, email, phone, etc.), `check_output` will return a `redacted_message`. Write the redacted version instead of the original, or warn the user that the content contains sensitive data.

**After tool output:** If tool output contains PII, use the `redacted_message` version in your response instead of the original.

If the response shows `allowed: false`, do not write the file or include the output in your response.

Note: For Bash/exec_command tool calls, PII scanning is handled automatically by the PostToolUse hook. This skill covers Write, Edit, and other non-Bash operations where hooks cannot intercept.

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/getaxonflow/axonflow-codex-plugin/skills/pii-scan/SKILL.md`
