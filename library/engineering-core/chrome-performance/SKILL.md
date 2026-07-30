---
name: chrome-performance
description: "Use Chrome DevTools MCP for frontend performance work such as slow page loads, LCP, CLS, INP, Lighthouse regressions, scripting hotspots, or layout thrash. Trigger when the user asks for page speed analysis, Core Web Vitals debugging, trace-based investigation, or before-and-after performance verification."
category: engineering-core
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/win4r/chrome-devtools-codex-plugin/skills/chrome-performance/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/win4r/chrome-devtools-codex-plugin/skills/chrome-performance/SKILL.md
---


Use this skill when performance findings need evidence from Chrome instead of code inspection alone.

## Default Flow

1. Start from the exact URL and device profile that reproduces the problem.
2. Record a baseline with `lighthouse_audit` or `performance_start_trace` and `performance_stop_trace`.
3. Drill into the highest-signal issue first, then inspect network, DOM, or scripts only as needed.
4. After code changes, rerun the same scenario and compare the results.

## Tool Selection

- `lighthouse_audit` for quick page-level diagnostics and report output.
- `performance_start_trace` and `performance_stop_trace` for deeper timing analysis.
- `performance_analyze_insight` to drill into a specific DevTools insight.
- `emulate` to keep device, network, CPU, and viewport conditions consistent.

## Working Rules

- Keep the scenario deterministic: one URL, one interaction path, one device profile.
- Save traces and reports to files when they are large.
- Treat LCP, CLS, and INP as user-path problems; connect each finding to the specific element, request, or script that caused it.
- Avoid mixing unrelated experiments in one trace.

## Expected Output

Return the problem, the evidence, the likely cause, and the concrete code area to change before proposing fixes.

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/win4r/chrome-devtools-codex-plugin/skills/chrome-performance/SKILL.md`
