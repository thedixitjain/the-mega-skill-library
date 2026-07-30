---
name: ultracode
description: "Ultracode-style dynamic workflows for Codex. Use when the user says \"ultracode\", \"workflow:\", \"/deep-research\", or asks for broad multi-file work with planning, parallel agents, verification, or crash-resume."
category: ai-agents-and-harness
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/Suraj1235/open-dynamic-workflows/skills/ultracode/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/Suraj1235/open-dynamic-workflows/skills/ultracode/SKILL.md
---


# Ultracode Through Open Dynamic Workflows

This is the Codex-facing ultracode alias for Open Dynamic Workflows. It uses the same local ODW daemon, MCP tools, and native fallback as the `odw` skill, but gives users the expected ultracode entrypoint.

## Step 0: Check the daemon

Run:

```bash
node scripts/daemon-bridge.js --check
```

- Exit 0: use the daemon path.
- Exit 1: say exactly what is missing (`odw-daemon start` or `odw-daemon doctor codex`) and use Codex-native planning only if useful.

## Daemon Path

1. Plan with `node scripts/daemon-bridge.js plan "<task>"`.
2. If the task is expensive or mutation-risky, show the topology, agent count, estimated cost/time, and ask before execution.
3. Execute with `node scripts/daemon-bridge.js exec plan.json`.
4. Monitor with `node scripts/daemon-bridge.js status <workflowId>` and finish with `node scripts/daemon-bridge.js result <workflowId>`.
5. If MCP tools are available, prefer `odw_health`, `odw_plan`, `odw_run`, `odw_status`, `odw_result`, and `odw_list` over shell bridge calls.

## Native Fallback

If ODW is unavailable, be explicit that full ultracode power requires the daemon, then decompose into discovery -> parallel work -> adversarial verification -> synthesis using Codex-native capabilities.

Never include secrets in prompts, plans, logs, or workflow artifacts.

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/Suraj1235/open-dynamic-workflows/skills/ultracode/SKILL.md`
