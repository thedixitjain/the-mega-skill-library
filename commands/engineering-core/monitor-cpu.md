---
name: monitor-cpu
description: "Monitor and optimize CPU usage"
category: engineering-core
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "plugins/performance/cpu-usage-monitor/commands/monitor-cpu.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/plugins/performance/cpu-usage-monitor/commands/monitor-cpu.md
---

# CPU Usage Monitor

Analyze code for CPU-intensive operations and optimize processor utilization.

## Analysis Areas

1. **Computational Complexity**: Identify O(n²) or worse algorithms
2. **Synchronous Operations**: Blocking operations on main thread
3. **Loop Optimization**: Inefficient iteration patterns
4. **Regular Expressions**: CPU-heavy regex patterns
5. **Recursive Functions**: Deep or inefficient recursion
6. **String Operations**: Excessive string concatenation
7. **JSON Processing**: Large JSON parsing operations

## Process

1. Scan codebase for CPU-intensive patterns
2. Analyze algorithmic complexity
3. Identify blocking operations
4. Check for optimization opportunities
5. Generate report with recommendations

## Output

Provide:

- CPU hotspot identification with file locations
- Complexity analysis for key algorithms
- Before/after code examples for optimizations
- Estimated performance improvements
- Best practices for CPU efficiency

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `plugins/performance/cpu-usage-monitor/commands/monitor-cpu.md`
