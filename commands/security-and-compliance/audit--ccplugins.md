---
name: audit
description: "Perform security audit on codebase"
allowed-tools: "Bash(find:*), Bash(grep:*)"
category: security-and-compliance
source_repo: ccplugins/awesome-claude-code-plugins
source_path: "plugins/audit/commands/audit.md"
source_url: https://github.com/ccplugins/awesome-claude-code-plugins/blob/HEAD/plugins/audit/commands/audit.md
---


## Context

- Package.json dependencies: @package.json
- Environment files: !`find . -name ".env*" -o -name "config.*" | head -10`
- Potential security files: !`find . -name "*secret*" -o -name "*key*" -o -name "*password*" | head -10`

## Your task

Perform a security audit focusing on:

1. **Dependency vulnerabilities**: Check for known CVEs
2. **Authentication/Authorization**: Review auth implementations
3. **Input validation**: Check for injection vulnerabilities
4. **Data exposure**: Look for sensitive data leaks
5. **Configuration security**: Review security configurations
6. **Secrets management**: Ensure proper secret handling

Target: $ARGUMENTS (if specified, otherwise audit entire codebase)

Provide prioritized findings with remediation steps.

---

**Source:** [`ccplugins/awesome-claude-code-plugins`](https://github.com/ccplugins/awesome-claude-code-plugins) → `plugins/audit/commands/audit.md`
