---
name: oh-my-openagent-agents
description: "Generated: 2026-06-01"
category: ai-agents-and-harness
source_repo: code-yeongyu/oh-my-openagent
source_path: "packages/omo-opencode/src/__tests__/AGENTS.md"
source_url: https://github.com/code-yeongyu/oh-my-openagent/blob/HEAD/packages/omo-opencode/src/__tests__/AGENTS.md
---
# src/__tests__/ — Plugin Perf Benchmarks

**Generated:** 2026-06-01

## OVERVIEW

Plugin-level tests that intentionally break the co-located `*.test.ts` convention: they boot the whole plugin via `createPluginModule()` and measure init cost.

| Path | Measures |
|------|----------|
| `perf/plugin-init.test.ts` | Cold `createPluginModule()` init time |
| `perf/plugin-init-team-mode-resume-defer.test.ts` | Init cost when team-mode resume is deferred |

## FIXTURES (DO NOT EXPAND)

`perf/fixtures/in-tree/` is a synthetic project tree (20 dummy `*.ts` files under `src/app`, `src/lib`, `packages/pkg-one/src`) that benchmarks AGENTS.md walk-up discovery.

Its three `AGENTS.md` files (`in-tree/`, `in-tree/src/`, `in-tree/packages/pkg-one/`) are deliberate 1-line stubs (`# fixture root`, etc.). They are TEST DATA, not documentation. `/init-deep` and any doc tooling MUST leave them as single-line stubs; expanding them corrupts the benchmark baseline.

---

**Source:** [`code-yeongyu/oh-my-openagent`](https://github.com/code-yeongyu/oh-my-openagent) → `packages/omo-opencode/src/__tests__/AGENTS.md`
