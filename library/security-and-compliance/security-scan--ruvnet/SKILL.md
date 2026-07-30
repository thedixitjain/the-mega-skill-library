---
name: security-scan
description: "Run full security scans on the codebase using Ruflo security tools. Use when reviewing PRs for security regressions, auditing auth/input-handling code, before production deploys, or when the user asks for a security check at quick/standard/deep depth."
allowed-tools: "Bash(npx *) mcp__plugin_ruflo-core_ruflo__memory_store mcp__plugin_ruflo-core_ruflo__hooks_post-task Read Grep"
category: security-and-compliance
source_repo: ruvnet/ruflo
source_path: "plugins/ruflo-security-audit/skills/security-scan/SKILL.md"
source_url: https://github.com/ruvnet/ruflo/blob/HEAD/plugins/ruflo-security-audit/skills/security-scan/SKILL.md
---

Run a security scan at the specified depth.

Via CLI:
```bash
npx @claude-flow/cli@latest security scan --depth DEPTH --output json
npx @claude-flow/cli@latest security cve --list
npx @claude-flow/cli@latest security threats --model stride --export md
```

| Depth | Checks |
|-------|--------|
| quick | Dependencies, known CVEs |
| standard | + Input validation, path traversal, secrets |
| deep | + Threat modeling, injection vectors, auth flows |

Store findings via MCP: `mcp__plugin_ruflo-core_ruflo__memory_store({ key: "scan-findings", value: "SUMMARY", namespace: "security-findings" })`

Train patterns: `mcp__plugin_ruflo-core_ruflo__hooks_post-task({ taskId: "security-scan", success: true, storeResults: true })`

---

**Source:** [`ruvnet/ruflo`](https://github.com/ruvnet/ruflo) → `plugins/ruflo-security-audit/skills/security-scan/SKILL.md`
