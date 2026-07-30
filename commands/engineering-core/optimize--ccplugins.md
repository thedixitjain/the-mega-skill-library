---
name: optimize
description: "Analyze and optimize code performance"
allowed-tools: "Bash(du:*), Bash(wc:*)"
category: engineering-core
source_repo: ccplugins/awesome-claude-code-plugins
source_path: "plugins/optimize/commands/optimize.md"
source_url: https://github.com/ccplugins/awesome-claude-code-plugins/blob/HEAD/plugins/optimize/commands/optimize.md
---


## Context

- File size: !`du -h $ARGUMENTS 2>/dev/null || echo "File not specified"`
- Line count: !`wc -l $ARGUMENTS 2>/dev/null || echo "File not specified"`

## Your task

Analyze and optimize: @$ARGUMENTS

Focus areas:
1. **Algorithm efficiency**: Improve time/space complexity
2. **Memory usage**: Reduce memory footprint
3. **I/O operations**: Optimize file/network operations
4. **Caching opportunities**: Identify cacheable operations
5. **Lazy loading**: Implement lazy loading where beneficial
6. **Bundle optimization**: Reduce bundle size (if applicable)

Provide before/after comparisons and performance impact estimates.

---

**Source:** [`ccplugins/awesome-claude-code-plugins`](https://github.com/ccplugins/awesome-claude-code-plugins) → `plugins/optimize/commands/optimize.md`
