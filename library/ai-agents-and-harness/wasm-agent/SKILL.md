---
name: wasm-agent
description: "Create and manage sandboxed WASM agents for isolated code execution"
allowed-tools: "mcp__plugin_ruflo-core_ruflo__wasm_agent_create mcp__plugin_ruflo-core_ruflo__wasm_agent_list mcp__plugin_ruflo-core_ruflo__wasm_agent_prompt mcp__plugin_ruflo-core_ruflo__wasm_agent_tool mcp__plugin_ruflo-core_ruflo__wasm_agent_files mcp__plugin_ruflo-core_ruflo__wasm_agent_export mcp__plugin_ruflo-core_ruflo__wasm_agent_terminate Bash"
category: ai-agents-and-harness
source_repo: ruvnet/ruflo
source_path: "plugins/ruflo-agent/skills/wasm-agent/SKILL.md"
source_url: https://github.com/ruvnet/ruflo/blob/HEAD/plugins/ruflo-agent/skills/wasm-agent/SKILL.md
---


# WASM Agent

Create sandboxed agents that run in WebAssembly for safe, isolated execution.

## When to use

When you need to run untrusted code, experiment with agent configurations, or create portable agents that run anywhere WASM is supported.

## Steps

1. **Create agent** — call `mcp__plugin_ruflo-core_ruflo__wasm_agent_create` with agent configuration
2. **Send prompt** — call `mcp__plugin_ruflo-core_ruflo__wasm_agent_prompt` to interact with the agent
3. **Use tools** — call `mcp__plugin_ruflo-core_ruflo__wasm_agent_tool` to give the agent access to specific tools
4. **Manage files** — call `mcp__plugin_ruflo-core_ruflo__wasm_agent_files` to read/write files in the sandbox
5. **Export** — call `mcp__plugin_ruflo-core_ruflo__wasm_agent_export` to package the agent for sharing
6. **List agents** — call `mcp__plugin_ruflo-core_ruflo__wasm_agent_list` to see all running WASM agents
7. **Terminate** — call `mcp__plugin_ruflo-core_ruflo__wasm_agent_terminate` to stop an agent

## Benefits

- Full sandbox isolation — agents cannot access the host filesystem
- Portable — export and run on any WASM runtime
- Reproducible — same behavior across platforms
- Safe — no risk of system damage from agent actions

---

**Source:** [`ruvnet/ruflo`](https://github.com/ruvnet/ruflo) → `plugins/ruflo-agent/skills/wasm-agent/SKILL.md`
