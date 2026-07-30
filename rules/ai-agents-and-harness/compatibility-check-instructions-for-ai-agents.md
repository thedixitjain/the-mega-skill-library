---
name: compatibility-check-instructions-for-ai-agents
description: "You are creating a source-grounded compatibility map for all book-derived rule sets in this repository."
category: ai-agents-and-harness
source_repo: ciembor/agent-rules-books
source_path: "_rule-workbench/CHECK_COMPATIBILITY.md"
source_url: https://github.com/ciembor/agent-rules-books/blob/HEAD/_rule-workbench/CHECK_COMPATIBILITY.md
---
# Compatibility Check Instructions For AI Agents

You are creating a source-grounded compatibility map for all book-derived rule sets in this repository.

This is not a vibes-based comparison. You must compare the canonical `mini` versions methodically, cite both local rule sets, and produce files that another reviewer can audit.

## Required Output

Create and maintain:

- `docs/COMPATIBILITY.md`: legend, matrix, scoring definitions, verdict counts, and book name key.
- `docs/compatibility/<book-a>/<book-b>.md`: one detailed comparison file for each unordered pair.

The matrix cell must contain one linked verdict:

- `✅` when the books are complementary and can be loaded together as equal active guidance without one book acting as the primary arbiter.
- `❌` when the books conflict enough that loading both as equal active guidance can push the agent toward worse or contradictory decisions.
- `🔁` when the books mostly duplicate each other, compete for the same decision layer, or one should usually be used as a substitute for the other.

Each linked comparison file must explain:

- whether the comparison is `draft` or `reviewed`
- what conflicts and how strongly, as `Conflict: N%`
- what does the same job and how strongly, as `Overlap: N%`
- what complements the other book and how strongly, as `Complementarity: N%`
- why the chosen verdict is the right loading decision for an agent

## Non-Negotiable Rules

- Use canonical `mini` files as primary local evidence. Do not decide from titles, reputation, memory, or community stereotypes alone.
- Read enough of both `mini` files to identify their actual active agent pressure before scoring.
- Cite both source files with section names and line ranges in every comparison file.
- Do not invent percentages. Scores are qualitative estimates, but they must be tied to cited evidence.
- You may use common software-engineering knowledge and internet research as supporting context, especially where the books are commonly compared, but the local `mini` rule sets remain the compatibility target.
- For known high-risk pairs listed in this file, external research is required before `Status: reviewed`.
- Do not create both `A/B.md` and `B/A.md`. Use one canonical file per unordered pair.
- Do not mark a pair complete if either local `mini` file has not been reviewed directly.
- Do not hide uncertainty. If evidence is insufficient, write the comparison as incomplete and state what must be read next.
- Do not use broad whole-file citations as proof. A citation such as `lines 3-49` is not acceptable unless the claim genuinely depends on the whole file.
- Do not reuse boilerplate analysis across files. If a sentence could be pasted into many unrelated comparisons, rewrite it or remove it.
- Do not claim the compatibility matrix is final until every pair file is `Status: reviewed`.

## Source Of Truth

Use these sources, in this order:

1. Public canonical mini file: `<book>/<book>.mini.md`
2. Equivalent workbench mini file: `_rule-workbench/<book>/mini.md`
3. Helper local context only, after reading `mini`: `<book>/<book>.md`, `_rule-workbench/<book>/full.md`, `nano.md`, `traceability.md`, `README.md`, `docs/USAGE.md`
4. External context only, after reading local `mini`: public/common knowledge, reviews, articles, or internet comparisons of the books

`mini` is the evidence base because the matrix answers whether two active agent rule sets should be loaded together. `full` may be used to resolve ambiguity, but it should not turn the comparison into a full-book research project.

When citing evidence, prefer line ranges from the mini file. Use commands such as:

```bash
nl -ba <book>/<book>.mini.md | sed -n '1,220p'
rg -n "keyword|phrase|pattern" <book>/<book>.mini.md
```

Refresh line citations if the source files change.

## Use Of External Context

External context is allowed, but it must stay subordinate to the local `mini` rule sets.

You may use:

- widely known comparisons between the books
- public reviews or summaries
- internet search results and articles
- general software-engineering knowledge about the books' positions

Use external context to:

- identify likely tensions worth checking in `mini`
- clarify terminology or historical relationship between books
- support a judgment when local `mini` evidence is ambiguous
- avoid missing a well-known compatibility issue

Do not use external context to override local `mini` evidence. If the public discussion says two books conflict but the local `mini` files have already scoped away that conflict, score the local files, not the public stereotype.

When external context materially affects a verdict, add it to `Source Basis` under a separate `External context` bullet and include a short citation or link when available.

### Research Basis Label

Every detailed comparison file must include:

```markdown
Research basis: {mini-only | mini-plus-external}
```

Use `mini-only` only when the pair is not in the known high-risk list and no common public comparison is needed to avoid a shallow judgment.

Use `mini-plus-external` when internet research, public summaries, reviews, author statements, or widely known community comparisons influenced the analysis. Include links or named sources in `Source Basis`.

`Status: reviewed` is not allowed for a known high-risk pair unless `Research basis: mini-plus-external` is present.

## Known High-Risk Pairs

These pairs are not allowed to default to `✅` just because their scopes can be separated. They require explicit tension analysis and external context before `Status: reviewed`.

### Same-Family Or Substitute-Likely Pairs

Default to `🔁` unless the file proves that the two rule sets provide distinct active pressure worth loading together.

- `domain-driven-design` vs `domain-driven-design-distilled`
- `domain-driven-design` vs `implementing-domain-driven-design`
- `domain-driven-design-distilled` vs `implementing-domain-driven-design`
- `refactoring` vs `refactoring-guru`
- `clean-code` vs `code-complete`
- `clean-code` vs `the-pragmatic-programmer`
- `code-complete` vs `the-pragmatic-programmer`

For these pairs, the comparison must answer:

- Are these two books solving the same agent problem?
- Does one book summarize, operationalize, modernize, or deepen the other?
- Would loading both add useful decision pressure, or mostly duplicate context?
- If both are loaded, which rule set should arbitrate when they disagree?

If one rule set must arbitrate, prefer `🔁` or `❌`, not `✅`.

### Known Tension Pairs

Do not score these as `✅` without explicitly examining the named tension.

- `a-philosophy-of-software-design` vs `clean-code`: method length, comment philosophy, deep modules versus small-function pressure.
- `a-philosophy-of-software-design` vs `refactoring`: design-upfront/deep-module pressure versus small-step behavior-preserving transformation.
- `clean-architecture` vs `domain-driven-design`: architectural boundaries and dependency direction versus model-first domain boundaries.
- `clean-architecture` vs `implementing-domain-driven-design`: ports/use cases/adapters versus tactical DDD implementation stack.
- `clean-architecture` vs `patterns-of-enterprise-application-architecture`: architectural policy boundaries versus enterprise application pattern choices.
- `domain-driven-design` vs `patterns-of-enterprise-application-architecture`: domain model and aggregate pressure versus enterprise transaction/data access patterns.
- `domain-driven-design-distilled` vs `patterns-of-enterprise-application-architecture`: selective DDD gates versus broader enterprise pattern alternatives.
- `implementing-domain-driven-design` vs `patterns-of-enterprise-application-architecture`: DDD tactical implementation versus broader enterprise pattern alternatives.
- `release-it` vs `designing-data-intensive-applications`: service resilience and operational failure handling versus data-system correctness, ordering, replay, and consistency.

For these pairs, the comparison must answer:

- Do both rule sets trigger on the same task type?
- If yes, do they recommend compatible first moves?
- Does one book require gates before introducing mechanisms that the other book treats as normal?
- Could an agent obey both and add unnecessary layers, patterns, retries, queues, abstractions, or rewrites?
- Is the practical loading decision to use both, choose one, or keep one as background context only?

### `✅` Burden Of Proof

For any high-risk pair, `✅ Complementary` requires all of these:

- the pair has `Research basis: mini-plus-external`
- the comparison names the known public or conceptual tension
- the local `mini` files contain gates that prevent the tension from becoming an active contradiction
- loading both gives distinct, non-duplicative active pressure for a realistic task
- neither book needs to be the primary arbiter for the pair's shared trigger

If any of these are missing, use `🔁` when the books compete for the same decision layer, or `❌` when they push contradictory active defaults.

## Required Book Slugs

Use these slugs exactly:

- `a-philosophy-of-software-design`
- `clean-architecture`
- `clean-code`
- `code-complete`
- `designing-data-intensive-applications`
- `domain-driven-design`
- `domain-driven-design-distilled`
- `implementing-domain-driven-design`
- `patterns-of-enterprise-application-architecture`
- `refactoring`
- `refactoring-guru`
- `release-it`
- `the-pragmatic-programmer`
- `working-effectively-with-legacy-code`

There are 14 books and 91 unordered pairs.

## Canonical Pair Paths

Create exactly one file per unordered pair.

Use alphabetical slug order:

```text
docs/compatibility/<earlier-slug>/<later-slug>.md
```

Example:

```text
docs/compatibility/clean-architecture/domain-driven-design.md
```

Do not also create:

```text
docs/compatibility/domain-driven-design/clean-architecture.md
```

Both matrix directions, if both are shown, must link to the same canonical file. A triangular matrix is allowed only if it remains easy to scan and every non-diagonal relationship is linked.

## Temporary Work Queue

Before writing any comparison files, create a temporary work queue file:

```text
_rule-workbench/compatibility-pair-workqueue.md
```

This file is an execution aid for the agent, not a release artifact.

The work queue must contain all 91 canonical pair paths as checkboxes:

```markdown
# Compatibility Pair Work Queue

- [ ] docs/compatibility/a-philosophy-of-software-design/clean-architecture.md
- [ ] docs/compatibility/a-philosophy-of-software-design/clean-code.md
- [ ] ...
```

Agent rules for the work queue:

- Generate the complete 91-item checkbox list before starting pair analysis.
- Work from the first unchecked item unless the user explicitly directs a different pair.
- Analyze only one pair at a time. Do not work on multiple comparisons in parallel.
- Do not start the next pair until the current pair file is written, cited, scored, linked from `docs/COMPATIBILITY.md`, and checked against this instruction file.
- Mark a checkbox as done only after the detailed comparison file and matrix cell both pass the quality bar.
- Mark a checkbox as `[~]` when a pair file exists but is only `Status: draft`.
- If interrupted, resume from the first unchecked item.
- Keep the work queue updated after every completed pair.
- Delete the temporary work queue before final release, unless the user asks to keep it for audit.

## Verdict Definitions

Use exactly one verdict per pair.

### `✅ Complementary`

Use when the books can be loaded together because they apply useful pressure at different levels or reinforce compatible decisions without requiring one book to overrule the other.

Typical shapes:

- one book gives sequencing, the other gives design criteria
- one book gives architecture boundaries, the other gives implementation hygiene
- one book handles production failure, the other handles code structure
- one book gives strategic modeling, the other gives tactical refactoring or testing checks

Do not use `✅` merely because a careful human could reconcile the books by scoping them manually. If the agent must choose one book as primary for the same trigger, the verdict is usually `🔁` or `❌`.

### `❌ Conflicting`

Use when loading both as equal active guidance can push the agent toward opposite choices.

Typical conflict shapes:

- opposite default action
- incompatible preferred boundaries
- different tolerance for layers, indirection, tactical patterns, ceremony, or rewrite scope
- one book encourages a mechanism that the other warns against unless narrowly triggered
- one book's "always" or strong default would violate the other's stop condition or "only when"
- both books trigger on the same task but recommend incompatible first moves
- one book's default abstraction pressure increases the exact complexity the other book is trying to remove

Use `❌` even if both books are individually good when equal active loading would make agent behavior unstable.

### `🔁 Overlap`

Use when the books mostly do the same job, one is a narrower substitute, one is a practical implementation version of the other, or loading both would mostly spend context on duplicate guidance.

Typical overlap shapes:

- same failure modes
- same refactoring sequence
- same code-quality pressure
- same DDD or architecture vocabulary at different depth
- one book is an abbreviated/practical version of the other
- one book is better treated as the default and the other as background reading
- both books cover the same agent failure mode with different wording or different granularity

Use `🔁` for same-family books unless the comparison proves meaningful non-overlapping active pressure.

Do not use mixed verdicts such as `✅/❌`. If a pair has both synergy and tension, choose the verdict that best answers: "Should an agent load these together as active rules for one task?"

## Claim Evidence Rules

Each comparison must contain claim-level evidence. Do not cite both whole `mini` files and call the comparison complete.

Required minimum evidence:

- at least two specific line ranges from Book A
- at least two specific line ranges from Book B
- at least one evidence bullet supporting the overlap claim
- at least one evidence bullet supporting the complementarity claim
- at least one evidence bullet supporting the conflict/tension claim, even when the verdict is not `❌`

Each evidence bullet must explain why the cited rule matters for this pair. A citation without interpretation is not enough.

Bad:

```markdown
- `clean-architecture/clean-architecture.mini.md` lines 3-49: local mini used for this comparison.
```

Good:

```markdown
- `clean-architecture/clean-architecture.mini.md` lines 17-18: Clean Architecture requires volatile details behind ports and outer-layer wiring, which complements DDD's rule to keep persistence and framework concerns outside the model.
```

## Boilerplate Rejection Rules

A pair file fails review if:

- `Loading Decision` does not name both books' actual interaction.
- `Complementary Forces`, `Overlap`, or `Conflicts` could apply unchanged to more than two other pairs.
- `Use Together When` only says "when both scopes apply" without naming the specific combined task.
- `Prefer One When` only says "when only its scope applies" without naming concrete task types.
- scores are not justified by specific forces in the text.
- `Review Notes` says no external context was needed without explaining whether any common comparison was considered or why it was unnecessary.

## Scoring Rubric

Every comparison file must include:

- `Conflict: N%`
- `Overlap: N%`
- `Complementarity: N%`

The percentages are qualitative, not measured statistics. They must summarize the cited evidence and the practical risk of loading both rule sets.

Use this scale:

- `0-20%`: weak
- `21-40%`: noticeable
- `41-60%`: substantial
- `61-80%`: strong
- `81-100%`: dominant

Verdict guidance:

- Prefer `✅` when complementarity is the strongest force, conflict is low, overlap is not dominant, and neither book must arbitrate the other under shared triggers.
- Prefer `❌` when conflict is high enough that an agent could make worse decisions by obeying both at once.
- Prefer `🔁` when overlap is dominant, one book is a summary/implementation/deeper version of the other, or complementarity is not high enough to justify loading both.
- Prefer `🔁` over `✅` when the only reason the pair seems compatible is "use A for one scope and B for another."

These are decision aids, not mechanical formulas. Explain the judgment.

## Per-Book Evidence Extraction

Before comparing pairs, extract each book's active pressure from its `mini` file.

For each book, identify:

- primary corrective bias
- strongest defaults
- non-negotiable rules
- trigger conditions
- stop conditions
- forbidden or discouraged moves
- preferred boundaries, abstractions, tests, and change style
- scope limits or cases where the book should not drive the task

Do not skip this step. Pairwise comparison without per-book pressure extraction will produce shallow results.

## Pairwise Workflow

For each unordered pair:

1. Open `_rule-workbench/compatibility-pair-workqueue.md`.
2. Select exactly one unchecked pair.
3. Open both canonical `mini` files for that pair.
4. Identify each book's active pressure using the extraction checklist above.
5. List overlap:
   - same design pressure
   - same failure mode
   - same boundary advice
   - same testing or verification advice
   - broader/narrower versions of the same rule
6. List complementarity:
   - different levels of decision-making
   - different phases of work
   - different risks covered by compatible guidance
   - one book provides gates for the other book's techniques
7. List conflicts:
   - opposite defaults
   - incompatible boundaries
   - conflicting abstraction pressure
   - conflicting refactoring, rewrite, testing, data, reliability, or architecture advice
   - one book's strong rule would violate the other's trigger or stop condition
8. Score Conflict, Overlap, and Complementarity.
9. Choose exactly one verdict.
10. Write the canonical comparison file.
11. Update `docs/COMPATIBILITY.md` with a linked cell.
12. Re-check that the matrix verdict matches the detailed file verdict.
13. Mark exactly that pair as done in `_rule-workbench/compatibility-pair-workqueue.md`.
14. Move to the next unchecked pair.

Do not batch unfinished analysis across multiple files. Batching is allowed only as a review checkpoint after several individually completed pairs.

## Detailed Comparison File Template

Use this template for every file under `docs/compatibility/`.

```markdown
# {Book A} vs {Book B}

Status: {draft | reviewed}
Research basis: {mini-only | mini-plus-external}

Verdict: {✅ Complementary | ❌ Conflicting | 🔁 Overlap}

Conflict: {0-100}%
Overlap: {0-100}%
Complementarity: {0-100}%

## Loading Decision

One short paragraph explaining whether an agent should load these together, choose one, or keep them separate.

## Book A Pressure

- ...

## Book B Pressure

- ...

## Complementary Forces

- Claim: ...
- Evidence:
  - `{book-a}/{book-a}.mini.md` lines X-Y: ...
  - `{book-b}/{book-b}.mini.md` lines X-Y: ...

## Overlap

- Claim: ...
- Evidence:
  - `{book-a}/{book-a}.mini.md` lines X-Y: ...
  - `{book-b}/{book-b}.mini.md` lines X-Y: ...

## Conflicts

- Claim: ...
- Evidence:
  - `{book-a}/{book-a}.mini.md` lines X-Y: ...
  - `{book-b}/{book-b}.mini.md` lines X-Y: ...
```

If no major conflict is found, write:

```markdown
## Conflicts

- No major conflict found in the mini rule sets. Residual risk is context competition, over-application, or duplicated guidance rather than direct contradiction.
```

Continue the template:

```markdown
## Use Together When

- ...

## Prefer One When

- ...

## Source Basis

- `{book-a}/{book-a}.mini.md` lines X-Y: source point and why it matters.
- `{book-a}/{book-a}.mini.md` lines X-Y: source point and why it matters.
- `{book-b}/{book-b}.mini.md` lines X-Y: source point and why it matters.
- `{book-b}/{book-b}.mini.md` lines X-Y: source point and why it matters.
- External context, if used: citation or link, plus why it matters.

## Review Notes

- Any uncertainty, edge case, or follow-up source check.
```

Additional requirements:

- `Book A Pressure` and `Book B Pressure` must be based on `mini` evidence, not common knowledge alone.
- `Complementary Forces`, `Overlap`, and `Conflicts` must not repeat the same point under different labels unless the nuance is explained.
- `Prefer One When` is mandatory for `🔁` files.
- `Use Together When` must be narrow or warning-oriented for `❌` files.
- Known high-risk pairs must include `Research basis: mini-plus-external` and at least one external-context bullet.
- `Review Notes` may say `None` only after the source basis is complete.
- `Status: reviewed` is allowed only when the file passes the Claim Evidence Rules and Boilerplate Rejection Rules.

## `docs/COMPATIBILITY.md` Format

Use this structure:

```markdown
# Book Rule Compatibility Matrix

This matrix compares the canonical `mini` rule sets and answers whether two books should be loaded together as active agent guidance.

## Legend

- ✅ Complementary: can be combined as equal active guidance without one book arbitrating the other.
- ❌ Conflicting: do not load together as equal active rule sets.
- 🔁 Overlap: choose one; they apply similar pressure or one is a narrower substitute.
- `N/A`: same rule set.

## Matrix

| Book | APoSD | CleanA | CleanC | CodeC | ... |
| --- | --- | --- | --- |
| APoSD | `N/A` | [✅](compatibility/a-philosophy-of-software-design/clean-architecture.md) | [🔁](compatibility/a-philosophy-of-software-design/clean-code.md) | [✅](compatibility/a-philosophy-of-software-design/code-complete.md) | ... |

## Scores

- Conflict: how much active guidance can push opposite decisions.
- Overlap: how much guidance pushes the same decisions or covers the same failure modes.
- Complementarity: how much guidance works at different levels and strengthens the pair.

Scores are qualitative estimates grounded in cited `mini` evidence, with optional external context, not measured statistics.

For known high-risk pairs, external context is required before a reviewed verdict.

## Verdict Counts

- ✅ Complementary: N
- ❌ Conflicting: N
- 🔁 Overlap: N

## Book Names

| Short | Book |
| --- | --- |
| APoSD | `a-philosophy-of-software-design` |
| CleanA | `clean-architecture` |
| CleanC | `clean-code` |
| CodeC | `code-complete` |
| ... | ... |
```

Matrix requirements:

- Include all 14 books as rows and columns.
- Diagonal cells are `N/A`.
- Every non-diagonal cell links to a detailed comparison file.
- Link targets must use canonical alphabetical pair paths.
- Cell emoji must match the detailed file verdict.
- The matrix may be treated as final only when every linked pair file is `Status: reviewed`.

## Quality Bar

A pair comparison is not acceptable unless it:

- has `Status: reviewed`
- has `Research basis: mini-only` or `Research basis: mini-plus-external`
- cites both `mini` files
- cites specific line ranges rather than whole files
- has claim-level evidence for conflict, overlap, and complementarity
- gives all three percentage scores
- separates conflict, overlap, and complementarity
- explains the verdict as loading guidance for agents
- describes when to use both or prefer one
- identifies direct contradictions when they exist
- explicitly says when no major conflict was found
- uses `mini-plus-external` for known high-risk pairs
- avoids generic best-practice opinions not grounded in the `mini` files or explicitly labeled external context
- passes the Boilerplate Rejection Rules
- does not duplicate the reverse pair

The complete compatibility set is not acceptable unless:

- `docs/COMPATIBILITY.md` has a complete 14x14 matrix
- there are exactly 91 canonical comparison files
- the temporary work queue has 91 checked items before it is deleted
- every non-diagonal matrix cell links to an existing file
- every detailed file links back implicitly through the canonical path
- every detailed file has `mini` source evidence from both books
- every known high-risk detailed file has external context
- every detailed file is `Status: reviewed`
- no reverse duplicate files exist
- matrix verdicts match detailed file verdicts

## Stop Conditions

Stop and report incomplete work instead of guessing when:

- `_rule-workbench/compatibility-pair-workqueue.md` does not exist during active compatibility work
- a canonical `mini` file cannot be found
- the two books were not read deeply enough to cite both
- a percentage would be based only on memory or reputation instead of local `mini` evidence and labeled supporting context
- a conflict depends on an interpretation that is not supported by the source
- a known high-risk pair has not been externally researched
- the matrix links cannot be verified
- more than one pair is being analyzed at once
- repeated boilerplate appears in pair-specific analysis
- final matrix status is claimed elsewhere while any pair file is not `Status: reviewed`
- the number of comparison files is not 91 when the complete set is claimed complete

## Suggested Verification Commands

Use commands like these while working:

```bash
rg --files | rg '(^|/)([^/]+)\.md$'
find docs/compatibility -type f | sort
find docs/compatibility -type f | wc -l
rg -n "Verdict:|Conflict:|Overlap:|Complementarity:|Source Basis" docs/compatibility
rg -n "\[.*\]\(compatibility/" docs/COMPATIBILITY.md
```

Use `git status --short` before and after batches so unrelated changes are not mixed into the compatibility work.

---

**Source:** [`ciembor/agent-rules-books`](https://github.com/ciembor/agent-rules-books) → `_rule-workbench/CHECK_COMPATIBILITY.md`
