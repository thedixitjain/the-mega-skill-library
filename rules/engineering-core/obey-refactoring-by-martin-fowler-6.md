---
name: obey-refactoring-by-martin-fowler
description: "Canonical full source: full.md"
category: engineering-core
source_repo: ciembor/agent-rules-books
source_path: "_rule-workbench/refactoring/traceability.md"
source_url: https://github.com/ciembor/agent-rules-books/blob/HEAD/_rule-workbench/refactoring/traceability.md
---
# OBEY Refactoring by Martin Fowler

Canonical full source: [full.md](full.md)

## Compression decisions

- Re-run under the current `PROCESS.md` on 2026-05-02 for alphabetical book position 10 in `_rule-workbench`: `refactoring`.
- `full.md` is kept as the canonical source exposure and should resolve to `../../refactoring/refactoring.md`; the canonical full source was not edited.
- No `PROCESS.md` update was needed. The current process already requires retaining book-thesis, decision-changing, conflict-resolving, and commonly missed micro-decision rules.
- The prior `traceability.md` referenced stale section names and line ranges, so it was rebuilt against the current `full.md`.
- `mini.md` was rebuilt to match the current source: it keeps behavior preservation, small-step safety, preparatory refactoring, smell-driven moves, ownership, mutation discipline, conditionals, error handling, reviewability, and stopping rules.
- `nano.md` keeps only the smallest always-on reminders that block common unsafe refactoring shortcuts.
- No retained rule is treated as `default`; no rule was omitted on the basis that target agents reliably follow it without prompting.

## Mini mapping

Decision rules:

- `M1` Preserve observable behavior and isolate behavior changes from structural changes. Source: `Purpose` (3-16), `Primary Directive` (20-31), `What Counts as Refactoring` (35-49), `Non-Negotiable Rules` (53-58), `Forbidden Patterns` (329-342), `Review Checklist` (410-414).
- `M2` Work in small reversible, buildable, testable, reviewable steps. Source: `Primary Directive` (25-31), `Non-Negotiable Rules` (60-67), `Commit and Patch Discipline` (88-92), `Code Generation Rules` (360-369), `Final Instruction` (429-433).
- `M3` Establish a safety net or characterization before risky refactoring and preserve failing tests. Source: `Tests and Verification` (79-87), `Testing Rules` (388-395), `Forbidden Patterns` (353-357), `Review Checklist` (417).
- `M4` Use preparatory and follow-up refactoring around feature work. Source: `Primary Directive` (25-29), `Non-Negotiable Rules` (69-75), `Preparatory Refactoring` (94-100), `Code Generation Rules` (360-369).
- `M5` Refactor the current blocking smell instead of detached polish. Source: `Code Smell Policy` (104-155), `Review Rules` (310-325), `Review Checklist` (415-418).
- `M6` Prefer the simplest named refactoring move that helps. Source: `Preferred Refactoring Moves` (158-187), `Refactoring Catalog Index` (191-255), `Code Generation Rules` (371-379).
- `M7` Make names and functions reveal intent with coherent tasks, consistent abstraction levels, tight scope, and separated phases. Source: `Naming Refactorings` (160-165), `Extraction Refactorings` (166-170), `Long Functions` (113-117), `Function-Level Rules` (258-267), `Review Checklist` (421-422).
- `M8` Put behavior and state with the owning concept and split modules by reasons to change. Source: `Divergent Change` (128-130), `Shotgun Surgery` (132-134), `Feature Envy` (136-138), `Movement Refactorings` (172-175), `Moving Features` (204-212), `Generalization and Big Refactorings` (243-255), `Class and Module Rules` (270-278), `Review Checklist` (423).
- `M9` Keep data, mutation, and call contracts explicit. Source: `Long Parameter Lists` (118-122), `Data Clumps and Primitive Obsession` (140-143), `Data Refactorings` (183-187), `Composing Methods` (193-202), `Organizing Data` (213-225), `Simplifying Calls and Conditionals` (234-241), `Data and Mutation Rules` (291-298).
- `M10` Simplify conditionals without introducing needless indirection. Source: `Switch Statements and Conditionals` (144-147), `Simplification Refactorings` (177-181), `Simplifying Calls and Conditionals` (227-233), `Rules for Working with Conditionals` (281-288), `Review Checklist` (422).
- `M11` Use abstraction, inheritance, delegation, and generalization only when current evidence justifies them. Source: `Use the Simplest Helpful Refactoring` (73-75), `Middle Man and Speculative Generality` (152-155), `Generalization and Big Refactorings` (243-255), `Class and Module Rules` (274-277), `Forbidden Patterns` (343-351).
- `M12` Preserve error semantics and refactor error handling to reveal the main path. Source: `Simplifying Calls and Conditionals` (241), `Error Handling Rules` (301-307).
- `M13` Keep patch intent reviewable and avoid giant mixed changes. Source: `Commit and Patch Discipline` (88-92), `Forbidden Patterns` (338-342), `Code Generation Rules` (380-385), `Review Checklist` (420).
- `M14` Stop when the requested change is easy, the blocking smell is removed, and further cleanup would be speculative. Source: `Use the Simplest Helpful Refactoring` (73-75), `Stopping Rules` (399-406), `Review Checklist` (425), `Final Instruction` (429-433).

Trigger rules:

- `M15` When adding behavior, decide whether a small preparatory refactor should come first. Source: `Primary Directive` (25-29), `Preparatory Refactoring` (94-100), `Code Generation Rules` (360-369).
- `M16` When fixing a bug in unclear code, characterize the failure and refactor only enough to make the fix visible before changing behavior. Source: `Tests and Verification` (81-87), `Testing Rules` (388-395), `Code Generation Rules` (360-369).
- `M17` When tests are absent or weak, make the smallest structural move and improve testability before broader cleanup. Source: `Tests and Verification` (81-87), `Testing Rules` (388-395), `Untested Structural Surgery` (353-357).
- `M18` When the same edit appears for a third time, remove duplication through clearer ownership. Source: `Duplicated Code` (108-111), `Shotgun Surgery` (132-134), `Code Generation Rules` (371-379).
- `M19` When a function mixes responsibilities, levels, phases, or hidden side effects, rename, extract, split phases, or isolate side effects. Source: `Long Functions` (113-117), `Extraction Refactorings` (166-170), `Function-Level Rules` (258-267).
- `M20` When one change spreads across many files, centralize knowledge or introduce a clearer boundary. Source: `Shotgun Surgery` (132-134), `Divergent Change` (128-130), `Class and Module Rules` (270-278), `Review Rules` (319-325).
- `M21` When repeated conditionals or type codes grow, decompose intent before introducing heavier variation mechanisms. Source: `Switch Statements and Conditionals` (144-147), `Simplifying Calls and Conditionals` (227-233), `Rules for Working with Conditionals` (281-288).
- `M22` When UI and domain behavior mix, move rules toward domain objects and verify any required presentation synchronization. Source: `Divergent Change` (128-130), `Data Refactorings` (183-187), `Generalization and Big Refactorings` (252-254), `Class and Module Rules` (272-273).
- `M23` When a patch mixes intents or code motion makes review hard, split the change unless context makes that impractical. Source: `Commit and Patch Discipline` (88-92), `Mixed-Intent Patches` (338-342), `Code Generation Rules` (380-385).
- `M24` When tempted to rewrite, choose the next small behavior-preserving transformation. Source: `Primary Directive` (20-31), `Big-Bang Rewrite` (333-337), `Final Instruction` (429-433).

Final checklist:

- The mini checklist restates `M1`, `M2`, `M3`, `M5`, `M7`, `M8`, `M10`, `M11`, `M13`, and `M14` as a final scan rather than introducing new standalone rules.

## Nano mapping

Decision rules:

- `N1` Preserve observable behavior and isolate feature changes, migrations, redesign, and cleanup. Source: `Purpose` (3-16), `Primary Directive` (20-31), `What Counts as Refactoring` (35-49), `Non-Negotiable Rules` (53-58), `Forbidden Patterns` (329-342).
- `N2` Work in small buildable, testable, reviewable steps. Source: `Primary Directive` (25-31), `Non-Negotiable Rules` (60-67), `Commit and Patch Discipline` (88-92), `Code Generation Rules` (360-369), `Final Instruction` (429-433).
- `N3` Get a safety net or record the verification gap before risky structural edits. Source: `Tests and Verification` (81-87), `Testing Rules` (388-395), `Untested Structural Surgery` (353-357).
- `N4` Refactor the smell that blocks the current change. Source: `Code Smell Policy` (104-155), `Review Rules` (310-325), `Stopping Rules` (399-406).
- `N5` Prefer simple named moves that preserve behavior and improve clarity. Source: `Preferred Refactoring Moves` (158-187), `Refactoring Catalog Index` (191-255), `Code Generation Rules` (371-379).
- `N6` Put behavior, state, and validation with the owning concept; reject vague utilities and just-in-case abstractions. Source: `Divergent Change` (128-130), `Shotgun Surgery` (132-134), `Feature Envy` (136-138), `Middle Man and Speculative Generality` (152-155), `Class and Module Rules` (270-278), `Forbidden Patterns` (343-351).
- `N7` Keep mutation and call contracts clear. Source: `Long Parameter Lists` (118-122), `Composing Methods` (200), `Organizing Data` (213-225), `Simplifying Calls and Conditionals` (234-241), `Data and Mutation Rules` (291-298).
- `N8` Stop when the change is easy, the code is clearer, and further cleanup would be speculative. Source: `Use the Simplest Helpful Refactoring` (73-75), `Stopping Rules` (399-406), `Final Instruction` (429-433).

Trigger rules:

- `N9` When behavior is unclear or tests are weak, characterize current behavior before broader refactoring. Source: `Tests and Verification` (81-87), `Testing Rules` (388-395), `Untested Structural Surgery` (353-357).
- `N10` When adding a feature is awkward, make the smallest preparatory refactor that makes it straightforward. Source: `Preparatory Refactoring` (94-100), `Code Generation Rules` (360-369).
- `N11` When the same edit appears for a third time, centralize ownership instead of copying again. Source: `Duplicated Code` (108-111), `Shotgun Surgery` (132-134), `Code Generation Rules` (371-379).
- `N12` When conditionals or type codes grow, decompose intent before reaching for polymorphism, state, strategy, or lookup tables. Source: `Switch Statements and Conditionals` (144-147), `Simplifying Calls and Conditionals` (227-233), `Rules for Working with Conditionals` (281-288).
- `N13` When a patch mixes cleanup with behavior or broad code motion, split it where practical. Source: `Commit and Patch Discipline` (88-92), `Mixed-Intent Patches` (338-342), `Code Generation Rules` (380-385).
- `N14` When tempted to rewrite, choose the next small behavior-preserving transformation. Source: `Primary Directive` (20-31), `Big-Bang Rewrite` (333-337), `Final Instruction` (429-433).

Final checklist:

- The nano checklist restates `N1`, `N2`, `N3`, `N5`, `N6`, `N8`, and `N13` as a final scan rather than introducing new standalone rules.

## Section coverage review

- `Purpose` (3-16): covered by `M1`, `N1`; binding-policy wording is merged into modal strength of compressed rules.
- `Primary Directive` (20-31): covered by `M1`, `M2`, `M4`, `M15`, `M24`, `N1`, `N2`, `N14`.
- `What Counts as Refactoring` (35-49): covered by `M1`, `N1`; examples of non-refactoring are merged into anti-rewrite and mixed-intent rules.
- `Non-Negotiable Rules` (53-75): covered by `M1`, `M2`, `M4`, `M11`, `M14`, `N1`, `N2`, `N8`.
- `Tests and Verification` (81-87): covered by `M3`, `M16`, `M17`, `N3`, `N9`.
- `Commit and Patch Discipline` (88-92): covered by `M2`, `M13`, `M23`, `N2`, `N13`.
- `Preparatory Refactoring` (94-100): covered by `M4`, `M15`, `N10`.
- `Code Smell Policy` (104-155): covered by `M5`, `M18`, `M20`, `M21`, `N4`, `N6`, `N11`, `N12`; detailed per-smell recipes are intentionally merged into smell and trigger rules.
- `Preferred Refactoring Moves` (158-187): covered by `M6`, `M7`, `M8`, `M9`, `M10`, `N5`; exact move catalog detail is intentionally merged.
- `Refactoring Catalog Index` (191-255): covered by `M6`, `M8`, `M9`, `M10`, `M11`, `M12`, `M21`, `M22`, `N5`, `N7`, `N12`; individual catalog entries are intentionally lost from compressed files because the operational selection rules survive and exact recipes remain in `full.md`.
- `Function-Level Rules` (258-267): covered by `M7`, `M19`, `N5`; dead-code detail is merged into cleanup clarity rather than retained as a standalone rule.
- `Class and Module Rules` (270-278): covered by `M8`, `M11`, `M20`, `M22`, `N6`; `utils/helpers/common` warning is merged into vague-utility avoidance.
- `Rules for Working with Conditionals` (281-288): covered by `M10`, `M21`, `N12`.
- `Data and Mutation Rules` (291-298): covered by `M9`, `N7`; immutable intermediate values are merged into mutation clarity rather than retained as a standalone rule.
- `Error Handling Rules` (301-307): covered by `M12`; `nano.md` intentionally loses detailed error-handling discipline because it is less central than behavior preservation, safety, ownership, and anti-rewrite reminders under tight context.
- `Review Rules` (310-325): covered by `M5`, `M20`, `N4`; the full review smell list is intentionally merged into smell-trigger rules.
- `Forbidden Patterns` (329-357): covered by `M1`, `M11`, `M13`, `M17`, `M23`, `M24`, `N1`, `N3`, `N6`, `N13`, `N14`.
- `Code Generation Rules` (360-385): covered by `M2`, `M4`, `M6`, `M13`, `M15`, `M18`, `M23`, `N2`, `N5`, `N10`, `N11`, `N13`; preferred first moves are merged into `M6`/`N5`.
- `Testing Rules` (388-395): covered by `M3`, `M16`, `M17`, `N3`, `N9`; expressive test-data detail is intentionally lost from compressed files.
- `Stopping Rules` (399-406): covered by `M14`, `N4`, `N8`.
- `Review Checklist` (410-425): covered by the mini and nano final checklists plus `M1`, `M3`, `M5`, `M7`, `M8`, `M10`, `M11`, `M13`, `M14`, `N5`, `N6`, `N8`, `N13`.
- `Final Instruction` (429-433): covered by `M2`, `M14`, `M24`, `N2`, `N8`, `N14`.

## Omission and merge notes

- No current source section is wholly intentionally lost.
- Detailed smell-by-smell remedies are covered by `M5`, `M18`, `M20`, `M21`, `N4`, `N6`, `N11`, and `N12`; exact examples are intentionally lost from compressed files.
- Detailed catalog entries are covered by `M6`, `M8`, `M9`, `M10`, `M11`, `M12`, `M21`, `M22`, `N5`, `N7`, and `N12`; exact recipes remain only in `full.md`.
- Review and testing lists are collapsed into trigger rules and final checklists; fixture/data-detail guidance is intentionally lost.
- `nano.md` intentionally loses detailed error-handling, UI/domain synchronization, and full class/module review taxonomy to stay usable as a compact fallback; the broader behavior-preservation, ownership, mutation, and anti-mixed-patch effects survive.

---

**Source:** [`ciembor/agent-rules-books`](https://github.com/ciembor/agent-rules-books) → `_rule-workbench/refactoring/traceability.md`
