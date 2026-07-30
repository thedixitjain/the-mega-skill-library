---
name: windsurf-performance-profiling
description: "'Profile and optimize code with AI-assisted analysis. Activate when users mention \"performance profiling\", \"optimize performance\", \"bottleneck analysis\", \"profiling\", or \"performance tuning\". Handles performance analysis and optimization. Use when working with windsurf performance profiling functionality. Trigger with phrases like \"windsurf performance profiling\", \"windsurf profiling\", \"windsurf\". '"
allowed-tools: "Read,Write,Edit,Bash(cmd:*),Grep"
category: engineering-core
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "skills/.curated/windsurf-performance-profiling/SKILL.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/skills/.curated/windsurf-performance-profiling/SKILL.md
---

# Windsurf Performance Profiling

## Overview

This skill enables AI-assisted performance profiling within Windsurf. Cascade analyzes profiling data to identify bottlenecks, suggest optimizations, and predict impact of changes.

## Prerequisites

- Windsurf IDE with Cascade enabled
- Profiling tools installed (Chrome DevTools, node --prof, py-spy, etc.)
- Application with performance concerns
- Baseline metrics established
- Understanding of performance targets

## Instructions

1. **Establish Baseline**
2. **Collect Profile Data**
3. **Analyze with Cascade**
4. **Implement Optimizations**
5. **Document and Monitor**

See `${CLAUDE_SKILL_DIR}/references/implementation.md` for detailed implementation guide.

## Output

- Profiling data and analysis
- Bottleneck identification reports
- Optimization recommendations
- Before/after comparison metrics

## Error Handling

See `${CLAUDE_SKILL_DIR}/references/errors.md` for comprehensive error handling.

## Examples

See `${CLAUDE_SKILL_DIR}/references/examples.md` for detailed examples.

## Resources

- [Windsurf Performance Guide](https://docs.windsurf.ai/features/performance)
- [Profiling Best Practices](https://docs.windsurf.ai/guides/profiling)
- [Optimization Patterns](https://docs.windsurf.ai/guides/optimization)

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `skills/.curated/windsurf-performance-profiling/SKILL.md`

**Also appears in:** `jeremylongshore/claude-code-plugins-plus-skills/plugins/saas-packs/skill-databases/windsurf/skills/windsurf-performance-profiling/SKILL.md`
