---
name: rule-compression-process
description: "Create compressed rule sets that are decision-equivalent to the full source, not sentence-equivalent."
category: general-purpose
source_repo: ciembor/agent-rules-books
source_path: "_rule-workbench/PROCESS.md"
source_url: https://github.com/ciembor/agent-rules-books/blob/HEAD/_rule-workbench/PROCESS.md
---
# Rule Compression Process

## Goal

Create compressed rule sets that are decision-equivalent to the full source, not sentence-equivalent.

The compressed versions should preserve the rules that materially change an AI agent's design, architecture, refactoring, review, risk decisions, and repeated local implementation choices under context pressure.

This process should generalize across books. If review of one book exposes a recurring compression mistake, improve `PROCESS.md` first instead of hand-tuning that one book in isolation.

## Source of Truth

- The canonical full rule set stays in the main book directory.
- Each workbench directory exposes it as `full.md` via symlink.
- Do not edit `full.md` in the workbench.
- `mini.md` and `nano.md` must always trace back to the canonical full source through `traceability.md`.

## Deliverables Per Book

- `full.md`: canonical full source by symlink
- `traceability.md`: what was kept, merged, or omitted, with references to source sections
- `mini.md`: on-demand compressed version
- `nano.md`: compact fallback version for very tight always-on context budgets

## Heading Format

All generated or updated rule files for a book must use the same first-level heading:

```markdown
# OBEY {book name} by {author name}
```

If the source has no clear author, omit the author suffix:

```markdown
# OBEY {source name}
```

Apply this heading to:

- the canonical full file in the book directory
- `_rule-workbench/<book>/mini.md`
- `_rule-workbench/<book>/nano.md`
- `_rule-workbench/<book>/traceability.md`
- released `<book>/<book>.mini.md` and `<book>/<book>.nano.md` when release is run

Do not add version labels such as `Mini`, `Nano`, or `Traceability` to the H1. Put version-specific context in body text or lower-level headings if needed.

## Rule Classification

For each source section, classify rules before compressing:

- `default`: use this label only when target agents reliably follow the rule without prompting and you have evidence for that claim. Do not mark a rule as default just because it sounds obvious to a human.
- `book-thesis`: expresses the book's central corrective bias, recurring warning, or distinctive point of view
- `decision-changing`: changes architecture, modeling, persistence, error handling, operational, or refactoring decisions
- `micro-decision`: changes repeated local implementation choices such as naming, function shape, query-vs-command boundaries, mutation visibility, parameter design, error handling shape, test discipline, or abstraction level
- `conflict-resolver`: resolves tradeoffs such as simple vs rich model, local fix vs strategic fix, retry vs idempotency
- `trigger`: activates only when touching a risky area
- `checklist-only`: useful as a final scan, but too weak as a main rule
- `framing`: useful context, but not an operational rule

## Compression Rules

### Build `mini.md`

- Keep every `book-thesis`, even when it acts through local code-shape or API-shape discipline rather than architecture.
- Keep every `decision-changing` and `conflict-resolver`.
- Keep every `micro-decision` or strong `trigger` that target agents commonly miss, that blocks a known shortcut, or that would plausibly regress if removed.
- Remove `default` rules only when they are verified defaults for the target agents, not assumed defaults.
- Merge duplicated rules across purpose, codegen, review, testing, and forbidden-pattern sections only when they have the same operational consequence.
- Prefer short operational rules over explanatory prose.
- Convert long review and testing lists into trigger rules and a final checklist.
- Preserve enough of the book's own bias and vocabulary that `mini.md` still feels like that book instead of a generic style guide.
- `mini.md` does not have a target line count. Different books may need materially different sizes.
- If `mini.md` adds little beyond `nano.md`, strengthen `mini.md` or collapse the distinction intentionally.
- If unsure whether a rule is a harmless omission or a book-central correction, keep it in `mini.md`.

### Build `nano.md`

- Keep only rules safe for fallback always-on attachment in a constrained context budget.
- Keep rules that correct known model biases and the smallest set of `book-thesis` rules needed to keep the base bias visible:
  - shallow wrappers mistaken for good abstraction
  - framework-first design
  - unsafe retries
  - rewrite-first legacy work
  - fake DDD or fake layering
  - hidden consistency contracts
- Drop generic readability, formatting, and hygiene only when their absence does not repeatedly cause model failures.
- Do not drop a rule from `nano.md` if it is the smallest always-on reminder of a known shortcut in a risky hotspot.
- Keep trigger rules that prevent shortcuts in risky areas.

## Traceability Rules

- Every retained rule in `mini.md` gets an `M*` id in `traceability.md`.
- Every retained rule in `nano.md` gets an `N*` id in `traceability.md`.
- Each id must reference the source section names and current line ranges in `full.md`.
- Record intentional omissions, especially when whole sections are collapsed into one compressed rule.
- For every omitted or merged source rule or subsection, record one of:
  - `covered by Mx`
  - `covered by Nx`
  - `intentionally lost`
- When omitting a rule as `default`, record why it is believed to be a verified default for the target agents or which recurring evaluations suggest that.
- Do not describe an omission only as `secondary`, `lower-yield`, or similar. Show where the operational effect survived, or state explicitly that it was intentionally lost.

## Section Coverage Review

Before a book is done, walk every source section in `full.md` and assign it to one of these outcomes:

- kept directly in `mini.md`
- merged into specific `M*` rules
- kept only in `nano.md`
- intentionally lost

This review is mandatory even when no text changes are made to `mini.md` or `nano.md`.

## Process vs Book Diagnosis

Before changing a compressed book after review, decide whether the finding is:

- a `process bug`: a recurring compression mistake or omission class that could affect multiple books
- a `book-specific miss`: a rule that is clearly required by this book's own source and thesis under the current process

Treat the finding as a `process bug` when:

- the missing rule belongs to a reusable class such as naming pressure, local reasoning, mutation visibility, boundary ownership, validation discipline, cancellation and cleanup semantics, or anti-shortcut trigger design
- the same argument would likely strengthen several books, not just the current one
- the change is driven more by a better compression heuristic than by a unique property of this source text

Treat the finding as a `book-specific miss` only when:

- the rule is grounded in this book's own source sections and distinctive bias
- the current `PROCESS.md` already implies that the rule should have survived compression
- fixing it does not require inventing a new cross-book heuristic

If the finding is a `process bug`:

- update `PROCESS.md` first
- then re-run the affected book under the revised process
- do not patch the book ad hoc to match reviewer taste

If the finding is a `book-specific miss`:

- cite the exact source sections and the current `PROCESS.md` rule that required retention
- update the book and its traceability without changing unrelated books

## Preferred Output Shape

Use the same structure for `mini.md` and `nano.md`:

1. the required `# OBEY ...` title
2. when to use
3. primary bias to correct
4. decision rules
5. trigger rules
6. final checklist

## Validation Checklist

Before considering a book done:

- all H1 headings follow `# OBEY {book name} by {author name}` or `# OBEY {source name}` when no author is known
- `mini.md`, `nano.md`, and `traceability.md` do not add version labels to the H1
- the canonical full source is untouched
- each retained rule changes a real agent decision, a repeated local implementation choice, or blocks a known failure mode
- each omitted section or rule has a traceable disposition: `covered by Mx`, `covered by Nx`, or `intentionally lost`
- duplicate guidance is merged
- long lists are collapsed into triggers or checklist items
- `nano.md` can stand alone as a compact always-on fallback attachment
- `mini.md` adds clear value beyond `nano.md`; it is not just a slightly longer restatement
- `mini.md` still preserves the book's unique point of view
- the book's central thesis is still recognizable without reading the title
- removed rules have explicit reasons: verified default, true redundancy, too situational, or preserved only in `full.md`
- any rule labeled `default` has explicit supporting evidence, not just intuition
- a full-to-mini gap review has been completed section by section
- post-review book edits are justified by source plus process, not by reviewer preference alone
- if a review finding would apply as a reusable compression principle across books, it has been written back into `PROCESS.md` before changing book outputs
- `traceability.md` explains why anything important was removed or merged

## Interpretation Heuristics

- Human-obvious is not the same as agent-default.
- Require evidence from evals, review findings, or known model mistakes when labeling a rule `default`. If evidence is missing, do not use the label.
- Do not strengthen a book merely because a rule seems desirable, modern, or personally compelling. The justification must come from the source text, the current process, or explicit failure evidence.
- Do not import guidance from a different book during verification just because it would improve the output. Compression is source-faithful, not best-practices aggregation.
- Prefer rules that affect boundaries, invariants, data ownership, failure semantics, refactoring safety, or repeated local implementation choices that compound over time.
- Prefer explicit tradeoff rules over generic quality slogans.
- Keep book-specific biases visible. Compression must not turn all books into the same generic style guide.
- Rules about naming, function shape, mutation/query separation, parameter design, error handling, test discipline, local reasoning, comment discipline, concurrency discipline, invalid-state elimination, misuse-resistant API design, cancellation and cleanup semantics, and writing or communication discipline are often violated by agents even when they sound obvious to humans. Do not drop them automatically.
- If you keep rediscovering the same omission class while reviewing different books, promote that lesson into `PROCESS.md` instead of hand-fixing books one by one.
- If a rule matters only while touching a specific hotspot, move it into trigger form.
- Use the removal test: if deleting a rule is likely to bring back a known bad habit, keep it.
- If a rule is obvious but agents still commonly violate it, keep it.
- If a book's distinctive point is enforced through repeated local discipline rather than one big architectural choice, treat that local discipline as core rather than secondary.
- Prefer re-running a book from a better process over manually sculpting the output after the fact.
- When unsure, keep a rule in `mini.md`; make `nano.md` stricter.

---

**Source:** [`ciembor/agent-rules-books`](https://github.com/ciembor/agent-rules-books) → `_rule-workbench/PROCESS.md`
