---
name: constructive-criticism-from-reddit
description: "Below is a consolidated list of recurring criticisms and suggestions from the Reddit discussion, ordered from the most valid to the least valid."
category: docs-and-knowledge-mgmt
source_repo: ciembor/agent-rules-books
source_path: "docs/CRITICISM.md"
source_url: https://github.com/ciembor/agent-rules-books/blob/HEAD/docs/CRITICISM.md
---
# Constructive criticism from Reddit

Below is a consolidated list of recurring criticisms and suggestions from the Reddit discussion, ordered from the most valid to the least valid.

Status notes below reflect the repository state on April 26, 2026.

### 1. There is no clear measurement of improvement

**Validity: 9/10**

This is the strongest criticism. Without benchmarks, before/after comparisons, defect counts, review effort, or task-completion data, it is hard to know whether the rules actually improve code quality or just feel useful.

**Current status: weakly addressed, about 2/10 solved.**

We partially improved measurability by adding the release matrix in [README.md](../README.md), deterministic `full` / `mini` / `nano` outputs, and per-book [traceability](../_rule-workbench/) plus section-by-section coverage in [_rule-workbench/PROCESS.md](../_rule-workbench/PROCESS.md). This makes compression auditable, but it does not measure real coding outcomes yet. The core criticism still stands because the repo still lacks evals, before/after task comparisons, defect-rate data, and review-time data.

### 2. This can burn tokens and pollute the context

**Validity: 9/10**

Many of the generated rule files contain a large number of individual instructions. Loading too many of them at once can increase token usage, crowd out task-specific context, and make the agent less focused.

**Current status: largely addressed, about 8/10 solved.**

This was addressed through the three-level release model in [README.md](../README.md): `mini` for the recommended working layer, `nano` for very tight always-on budgets, and `full` for reference only. [USAGE.md](USAGE.md) now explicitly recommends the smallest mechanism that still changes agent decisions, warns against global loading, and shows scoped and retrieval-based alternatives. The remaining gap is behavioral rather than structural: the repo cannot stop a user from still attaching too much at once.

### 3. Skills, RAG, or progressive loading may be better than putting everything into `AGENTS.md`

**Validity: 9/10**

The rules are likely more useful when loaded selectively. Refactoring rules should be used during refactoring, legacy-code rules when working with legacy systems, data-intensive design rules when working on data-heavy systems, and so on.

**Current status: largely addressed, about 9/10 solved.**

This criticism directly shaped [USAGE.md](USAGE.md). The repo now recommends progressive loading, scoped rules, skills, nested files, MCP, retrieval, and editor-specific on-demand mechanisms instead of assuming one giant `AGENTS.md`. The current design treats large rule sets as material to be selected, scoped, or retrieved, not dumped globally.

### 4. A short set of project-specific rules may work better

**Validity: 9/10**

A compact `AGENTS.md` with 10–15 strong, testable, project-specific instructions may be more effective in daily use than a large generic rule set distilled from books.

**Current status: partially addressed, about 6/10 solved.**

This is partly addressed by [README.md](../README.md) and [USAGE.md](USAGE.md), which now recommend one primary `mini` layer when the context budget allows it, `nano` only as a compact fallback, and scoped or on-demand additions instead of stacking many generic books. That said, the repo still mainly ships book-derived rule packs, not automatically generated project-specific rules based on one team's codebase, incidents, and conventions. So the criticism is mitigated operationally, but not fully solved at the content level.

### 5. The model may ignore many of the rules anyway

**Validity: 8/10**

LLMs do not reliably obey hundreds of instructions at the same time. More rules can increase coverage, but they can also create ambiguity, competition between instructions, and instruction fatigue.

**Current status: partially addressed, about 6/10 solved.**

This is one of the main reasons [_rule-workbench/PROCESS.md](../_rule-workbench/PROCESS.md) now compresses toward decision-equivalent `mini` and `nano` files instead of keeping everything. The process explicitly prioritizes decision-changing rules, micro-decisions, triggers, and known shortcut blockers, and it requires evidence before calling a rule a safe default. That reduces instruction overload, but we still do not have empirical obedience data showing how often models follow the final compressed sets.

### 6. Rules should also come from real project failures

**Validity: 8/10**

Book-derived rules are a useful starting point, but the most valuable agent rules are often based on actual incidents: the agent made a mistake, it caused a specific problem, and a new rule was added to prevent it from happening again.

**Current status: weakly addressed, about 3/10 solved.**

We moved slightly in this direction by making [_rule-workbench/PROCESS.md](../_rule-workbench/PROCESS.md) demand evidence for `default` labels and by using review findings to strengthen missing rules. But the repository is still primarily book-derived, not incident-derived. There is still no first-class mechanism here for collecting production failures, failed agent runs, or postmortems and turning them into project rules.

### 7. Rules from different books may conflict

**Validity: 8/10**

Different books operate at different abstraction levels and sometimes encourage different tradeoffs. For example, rules inspired by Clean Code, Clean Architecture, DDD, DDIA, PoEAA, and A Philosophy of Software Design may push the agent toward different architectural decisions.

**Current status: partially addressed, about 7/10 solved.**

This is now addressed much more explicitly in [README.md](../README.md), [USAGE.md](USAGE.md), and [_rule-workbench/PROCESS.md](../_rule-workbench/PROCESS.md). The repo recommends one primary always-on rule set, on-demand secondary rule sets, and source-faithful compression instead of cross-book best-practice aggregation. That greatly reduces accidental mixing. The unresolved part is that the repo still does not provide a formal conflict matrix between books; it relies on loading discipline instead.

### 8. The approach may cause overengineering

**Validity: 8/10**

If the agent applies heavyweight architecture rules to a small feature or simple CRUD task, it may introduce unnecessary layers, abstractions, factories, ports, adapters, aggregates, or domain events.

**Current status: largely addressed, about 7/10 solved.**

This was mitigated in several places. [README.md](../README.md) and [USAGE.md](USAGE.md) now stress task-scoped loading and the smallest effective mechanism. The compressed books also preserve anti-ceremony and "use this only when warranted" pressure, especially in DDD-related rule sets. The remaining risk is user misuse: the repo can tell you not to load heavyweight rules for trivial tasks, but it cannot enforce good task selection.

### 9. The project could include more AI-agent-specific material

**Validity: 7/10**

Software engineering books teach good design, but AI coding agents also need operational guidance: tool use, planning loops, verification, test execution, avoiding guesses, scoped edits, and recovery from failed runs.

**Current status: partially addressed, about 6/10 solved.**

This is addressed more by delivery and process than by book content. [USAGE.md](USAGE.md) now contains editor-specific guidance for Codex, Claude Code, Cursor, skills, scoped rules, MCP, and retrieval. [_rule-workbench/PROCESS.md](../_rule-workbench/PROCESS.md) is also explicitly agent-centered: it optimizes for changed decisions under context pressure, repeated local choices, and known model shortcuts. Still, the repository is not yet a full AI-agent operations handbook; most substantive rules remain software-engineering-first.

### 10. Too many abstract rules may lead to pseudo-compliance

**Validity: 7/10**

The agent may produce code that appears architecturally “proper” while still missing the actual task constraints. The risk is not that the rules are wrong, but that they may encourage surface-level compliance instead of practical correctness.

**Current status: partially addressed, about 5/10 solved.**

This has been reduced by the current compression process. [_rule-workbench/PROCESS.md](../_rule-workbench/PROCESS.md) now prefers operational rules, triggers, micro-decisions, and conflict-resolvers over broad slogans, and every book has traceability showing what survived compression and why. That makes pseudo-compliance harder. But the repo still lacks direct outcome evals that would prove the agent is solving the user's actual task rather than merely sounding principled.

### 11. There may be legal or licensing concerns

**Validity: 6/10**

This is potentially important, but difficult to evaluate without legal analysis. A safer framing is that the project contains practical, original agent instructions inspired by software engineering principles, not substitutes for the books themselves. But... it's a destilled content taken from ChatGPT. So OpenAI had stolen books, I distilled ChatGPT, will OpenAI sue me for this?

**Current status: weakly addressed, about 3/10 solved.**

We improved the framing in [README.md](../README.md): the repository now says these files are practical engineering instructions inspired by the books, not official materials, not substitutes for the books, and not reproductions of book text. That is a safer product framing. But this is still not legal advice, and the repo still has no legal review. The underlying concern remains only partially addressed.

**Resolution policy: won't fix.**

This repository will keep the safer framing and avoid presenting the files as book replacements, but it will not attempt to provide formal legal clearance or legal analysis inside the project itself.

### 12. The LLM may already know these books

**Validity: 5/10**

This is partly true, but incomplete. Models may know the principles, yet still fail to apply them consistently. Explicit context can help, but a full book-sized rule set is not automatically better than a short, targeted reminder.

**Current status: moderately addressed, about 6/10 solved.**

The repository now essentially agrees with the criticism. [README.md](../README.md) and [USAGE.md](USAGE.md) no longer imply that full-book-sized context is the default. Instead they push `mini` as the recommended targeted reminder, keep `nano` as the compact fallback, and treat `full` as reference material. So the value proposition shifted from "the model needs the whole book" to "the model benefits from a short, decision-changing reminder." What is still missing is experimental proof that these reminders outperform model priors alone.

### 13. Some principles may be outdated in the AI coding era

**Validity: 5/10**

AI changes the economics of writing, rewriting, and refactoring code. However, many core principles remain relevant: readability, modularity, testability, resilience, boundaries, and maintainability.

**Current status: partially addressed, about 5/10 solved.**

This is addressed indirectly, not by rewriting the books, but by filtering them through an agent-oriented compression process. [_rule-workbench/PROCESS.md](../_rule-workbench/PROCESS.md) now keeps only rules that still change agent decisions, block shortcuts, or protect risky hotspots, and it drops more framing and passive prose. That helps modernize delivery. But the source material is still rooted in classic books, so this criticism remains partly valid until more AI-native rules are added alongside them.

---

**Source:** [`ciembor/agent-rules-books`](https://github.com/ciembor/agent-rules-books) → `docs/CRITICISM.md`
