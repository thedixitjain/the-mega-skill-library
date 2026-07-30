---
name: dependency-check
description: "Scan project dependencies for known vulnerabilities and CVEs. Use when auditing third-party packages, before releases, after `npm install`/lockfile changes, or when investigating reported CVE advisories."
allowed-tools: "Bash(npx * npm *) mcp__plugin_ruflo-core_ruflo__memory_store Read"
category: security-and-compliance
source_repo: ruvnet/ruflo
source_path: "plugins/ruflo-security-audit/skills/dependency-check/SKILL.md"
source_url: https://github.com/ruvnet/ruflo/blob/HEAD/plugins/ruflo-security-audit/skills/dependency-check/SKILL.md
---

Check dependencies for CVEs and outdated packages:

```bash
npx @claude-flow/cli@latest security cve --list
npx @claude-flow/cli@latest security cve --severity critical
npx @claude-flow/cli@latest security scan --type deps --depth deep
npm audit --json
```

| Severity | Action |
|----------|--------|
| critical | Block deployment, fix immediately |
| high | Fix before next release |
| moderate | Schedule fix within sprint |
| low | Track in backlog |

Auto-fix via the scan command: `npx @claude-flow/cli@latest security scan --type deps --fix`

For continuous monitoring, dispatch via MCP:
`mcp__plugin_ruflo-core_ruflo__hooks_worker-dispatch({ trigger: "audit" })`

---

**Source:** [`ruvnet/ruflo`](https://github.com/ruvnet/ruflo) → `plugins/ruflo-security-audit/skills/dependency-check/SKILL.md`
