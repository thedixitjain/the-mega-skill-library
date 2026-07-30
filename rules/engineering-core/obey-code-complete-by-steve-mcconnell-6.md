---
name: obey-code-complete-by-steve-mcconnell
description: "Canonical full source: full.md"
category: engineering-core
source_repo: ciembor/agent-rules-books
source_path: "_rule-workbench/code-complete/traceability.md"
source_url: https://github.com/ciembor/agent-rules-books/blob/HEAD/_rule-workbench/code-complete/traceability.md
---
# OBEY Code Complete by Steve McConnell

Canonical full source: [full.md](full.md)

## Compression decisions

- Re-run for book 4 alphabetically (`code-complete`) on 2026-05-02 against the current 354-line `full.md`.
- This is a book-specific re-run, not a `PROCESS.md` change: the existing process already requires source-faithful retention of book-thesis, decision-changing, micro-decision, trigger, and conflict-resolving construction rules with section coverage.
- The earlier workbench compression referenced an older source shape, so the main correction is updated source mapping and removal of rules that were no longer grounded in this `full.md`.
- No rule was omitted as `default`; without evaluation evidence, apparently obvious construction discipline was either retained, merged, or explicitly marked as intentionally lost.
- `mini.md` keeps Code Complete's operational construction bias: low-defect construction, inspectability, controlled complexity, defensive programming, routine/data/class discipline, incremental verification, and evidence-based correction.
- `nano.md` keeps only always-on reminders that block common agent shortcuts: solution-first coding, clever compactness, vague routines, hidden data meaning, weak boundaries, unreadable flow, happy-path testing, guess-driven fixes, unsafe refactoring, and unmeasured tuning.

## Mini mapping

Decision rules:

- `M1` Before large construction work, verify requirements, architecture, major risks, coding conventions, language constraints, error policy, data representation, reuse, integration, and testing approach. Source: `Construction Prerequisites and Decisions` (45-52), `Purpose` (3-16), `Review Checklist` (327-341).
- `M2` When upstream uncertainty remains, build a small validated slice instead of speculative code, and make expensive-to-reverse decisions deliberately. Source: `Construction Prerequisites and Decisions` (45-52), `Primary Directive` (20-31).
- `M3` Optimize for human readers: clarity, locality, explicitness, visible control flow, consistent conventions, and practical correctness over cleverness, minimal keystrokes, or fashion. Source: `Primary Directive` (20-31), `Foundational Construction Rules` (35-42), `Forbidden Patterns / Cleverness over Clarity` (273-278), `Final Instruction` (345-354).
- `M4` For complex routines, sketch precise pseudocode or intent comments, then keep only comments that still explain intent, constraints, contracts, or rationale. Source: `Pseudocode Programming Process` (55-61), `Comment Rules` (207-213).
- `M5` Keep routines cohesive, precisely named, small at the interface, and hard to misuse; separate setup, validation, computation, and side effects. Source: `Routine Design Rules` (64-79), `Forbidden Patterns / Routine Bloat` (279-282), `Review Rules` (257-270).
- `M6` Make variable and data meaning explicit through names, small scope, deliberate initialization, constants, stronger types, and visible units or sentinel meanings. Source: `Variable and Data Rules` (82-95), `Data Type Rules` (98-107), `Code Generation Rules` (298-315).
- `M7` Choose data types that make invalid or ambiguous values harder to represent; use booleans, enumerations, records, maps, and tables only where they clarify meaning. Source: `Data Type Rules` (98-107), `Construction with Preconditions and Postconditions` (198-204).
- `M8` Keep control flow simple enough to verify: shallow nesting, named predicates, clear normal path, clear loops, and no side-effect-dependent expressions or clever one-liners. Source: `Control Flow Rules` (110-124), `Statement, Conditional, and Loop Rules` (127-136), `Forbidden Patterns / Cleverness over Clarity` (273-278), `Code Generation Rules` (298-315).
- `M9` Use table-driven or data-driven logic for stable explicit mappings only when the table is clearer, obvious, synchronized with the rules, and validated. Source: `Statement, Conditional, and Loop Rules` (127-136), `Table-Driven and Data-Driven Rules` (164-170), `Testing Rules` (318-324).
- `M10` Validate input at trust boundaries; use assertions, invariant checks, and simple contracts for programmer assumptions, and validation or domain errors for expected external or business failures. Source: `Defensive Programming Rules` (139-151), `Construction with Preconditions and Postconditions` (198-204), `Testing Rules` (318-324).
- `M11` Handle errors at the right abstraction, preserve diagnostic context, standardize similar failures, keep the normal path readable, and never silently continue from corrupted or impossible state. Source: `Defensive Programming Rules` (139-151), `Error Handling Rules` (154-161), `Final Instruction` (345-354).
- `M12` Keep classes and modules focused, cohesive, and bounded by clear contracts; hide representation and internal bookkeeping, and avoid mixed concerns. Source: `Class and Module Design Rules` (173-185), `Review Rules` (257-270), `Code Generation Rules` (298-315).
- `M13` Treat rising complexity as defect risk: split tangled routines or modules, remove duplication that multiplies maintenance effort, and reduce maintainer working-memory load. Source: `Complexity Management Rules` (188-195), `Review Checklist` (327-341).
- `M14` Build in small, verifiable increments; integrate often enough to expose conflicts, keep partial work from rotting, and review and improve code during construction. Source: `Incremental Construction Rules` (225-231), `Performance, Integration, Tools, and Craftsmanship` (245-254).
- `M15` Match reviews, inspections, pair work, tests, static checks, and regression tests to defect risk; debug by reproducing, isolating, explaining, fixing, and verifying root causes. Source: `Quality, Collaboration, Debugging, and Refactoring` (234-242), `Review Rules` (257-270), `Testing Rules` (318-324).
- `M16` Refactor when structure hides intent, duplicates knowledge, or raises defect probability, and separate refactoring from behavior change when that improves reviewability. Source: `Quality, Collaboration, Debugging, and Refactoring` (234-242).
- `M17` Tune performance only when requirements and evidence justify it; measure before and after, and keep clarity unless an explicit measured tradeoff warrants the cost. Source: `Performance, Integration, Tools, and Craftsmanship` (245-254).
- `M18` Use tools, scripts, debuggers, profilers, editors, and build automation to reduce error-prone manual work, not to replace understanding. Source: `Performance, Integration, Tools, and Craftsmanship` (245-254).
- `M19` Use layout, comments, documentation, and coding standards to lower reader effort; prefer self-documenting structure first and keep comments accurate and purposeful. Source: `Comment Rules` (207-213), `Coding Standards Rules` (216-222), `Performance, Integration, Tools, and Craftsmanship` (245-254), `Forbidden Patterns / Comment-as-Crutch` (288-290), `Forbidden Patterns / Consistency Neglect` (292-294).

Trigger rules:

- `M20` When coding starts from a proposed solution, restate the requirement, architecture fit, risks, conventions, and success constraints. Source: `Construction Prerequisites and Decisions` (45-52), `Review Checklist` (327-341).
- `M21` When a routine is hard to name, mixes phases, has flag arguments, long parameters, or hidden side effects, redesign the interface or split the routine. Source: `Routine Design Rules` (64-79), `Forbidden Patterns / Routine Bloat` (279-282), `Review Rules` (257-270).
- `M22` When readers must decode units, ranges, precision, encoding, ownership, status, magic values, or primitive flags, move that meaning into names, constants, types, or structures. Source: `Variable and Data Rules` (82-95), `Data Type Rules` (98-107).
- `M23` When input crosses a trust boundary, decide what is validated, rejected, recovered from, asserted, and kept diagnosable. Source: `Defensive Programming Rules` (139-151), `Error Handling Rules` (154-161), `Review Checklist` (327-341).
- `M24` When branches, loops, recursion, exits, or exception paths become hard to verify, simplify before adding logic. Source: `Control Flow Rules` (110-124), `Statement, Conditional, and Loop Rules` (127-136), `Code Generation Rules` (298-315).
- `M25` When repeated branching maps stable categories, ranges, conversions, validation, dispatch, or configuration-like rules, consider a validated table. Source: `Statement, Conditional, and Loop Rules` (127-136), `Table-Driven and Data-Driven Rules` (164-170).
- `M26` When a class or module exposes representation, grows into a god object, or mixes unrelated responsibilities, restore the abstraction boundary. Source: `Class and Module Design Rules` (173-185), `Review Rules` (257-270), `Forbidden Patterns` (273-295).
- `M27` When tests cover only the happy path, add normal, boundary, invalid-input, defensive-check, routine-contract, and data-driven edge cases. Source: `Testing Rules` (318-324), `Defensive Programming Rules` (139-151).
- `M28` When debugging begins from a guess, first make the failure repeatable, collect evidence, isolate the path, and explain the cause. Source: `Quality, Collaboration, Debugging, and Refactoring` (234-242).
- `M29` When refactoring poorly understood or risky code, add tests or analysis first and keep behavior changes separate. Source: `Quality, Collaboration, Debugging, and Refactoring` (234-242), `Testing Rules` (318-324).
- `M30` When performance work begins, set a target, measure current behavior, change one thing, remeasure, and document any clarity tradeoff. Source: `Performance, Integration, Tools, and Craftsmanship` (245-254).
- `M31` When comments restate obvious mechanics or go stale, rewrite the code or delete the comment; when code cannot express intent, constraints, or usage, add a close accurate comment. Source: `Comment Rules` (207-213), `Performance, Integration, Tools, and Craftsmanship` (245-254), `Forbidden Patterns / Comment-as-Crutch` (288-290).
- `M32` When local style starts to diverge, follow shared formatting, naming, file-structure, and idiom conventions instead of creating a module-specific dialect. Source: `Coding Standards Rules` (216-222), `Forbidden Patterns / Consistency Neglect` (292-294).

Final checklist:

- The checklist restates `M1`, `M3`, `M5`-`M19`, and `M23`-`M30` as a final scan rather than introducing new retained rules.

## Nano mapping

Decision rules:

- `N1` Clarify requirements, architecture fit, risks, conventions, and major construction decisions before coding from a solution idea. Source: `Construction Prerequisites and Decisions` (45-52), `Code Generation Rules` (298-315).
- `N2` Choose clarity, locality, explicitness, simple control flow, and consistent style over clever compactness or fashionable idioms. Source: `Primary Directive` (20-31), `Foundational Construction Rules` (35-42), `Forbidden Patterns / Cleverness over Clarity` (273-278), `Final Instruction` (345-354).
- `N3` Keep routines, classes, and modules cohesive, precisely named, small at the interface, encapsulated, and hard to misuse. Source: `Routine Design Rules` (64-79), `Class and Module Design Rules` (173-185), `Review Rules` (257-270).
- `N4` Make data meaning visible with names, constants, stronger types, closed states, deliberate initialization, units, and ownership. Source: `Variable and Data Rules` (82-95), `Data Type Rules` (98-107).
- `N5` Validate trust boundaries; use assertions, invariants, and contracts for programmer assumptions; keep error handling explicit and diagnosable. Source: `Defensive Programming Rules` (139-151), `Error Handling Rules` (154-161), `Construction with Preconditions and Postconditions` (198-204).
- `N6` Keep branches, loops, exits, exceptions, and table-driven logic simple enough to verify. Source: `Control Flow Rules` (110-124), `Statement, Conditional, and Loop Rules` (127-136), `Table-Driven and Data-Driven Rules` (164-170).
- `N7` Build, test, review, debug, refactor, integrate, and tune in small evidence-based loops: root cause before fixes, behavior protection before refactoring, measurement before optimization. Source: `Incremental Construction Rules` (225-231), `Quality, Collaboration, Debugging, and Refactoring` (234-242), `Performance, Integration, Tools, and Craftsmanship` (245-254), `Testing Rules` (318-324).
- `N8` Use comments, documentation, tools, and standards to reduce reader or manual effort, never to hide poor structure. Source: `Comment Rules` (207-213), `Coding Standards Rules` (216-222), `Performance, Integration, Tools, and Craftsmanship` (245-254), `Forbidden Patterns / Comment-as-Crutch` (288-290), `Forbidden Patterns / Consistency Neglect` (292-294).

Trigger rules:

- `N9` When a solution appears before the problem is clear, restate the requirement, constraints, and construction risks. Source: `Construction Prerequisites and Decisions` (45-52).
- `N10` When readers must decode names, flags, primitives, units, states, or layout, model the meaning explicitly. Source: `Variable and Data Rules` (82-95), `Data Type Rules` (98-107), `Review Rules` (257-270).
- `N11` When a routine mixes phases or has a hard-to-use interface, split concerns or change the data model. Source: `Routine Design Rules` (64-79), `Forbidden Patterns / Routine Bloat` (279-282).
- `N12` When input crosses a trust boundary, decide validation, rejection, recovery, assertion, and diagnostics. Source: `Defensive Programming Rules` (139-151), `Error Handling Rules` (154-161).
- `N13` When control flow, loops, exceptions, or branching tables are hard to inspect, simplify before adding logic. Source: `Control Flow Rules` (110-124), `Statement, Conditional, and Loop Rules` (127-136), `Table-Driven and Data-Driven Rules` (164-170).
- `N14` When tests only prove happy paths, add boundary, invalid-input, defensive-check, contract, and data-driven cases. Source: `Testing Rules` (318-324), `Construction with Preconditions and Postconditions` (198-204).
- `N15` When debugging, refactoring, or performance work starts from a guess, get evidence first. Source: `Quality, Collaboration, Debugging, and Refactoring` (234-242), `Performance, Integration, Tools, and Craftsmanship` (245-254).
- `N16` When comments repeat obvious mechanics, rewrite the code or delete the comment; keep comments for intent and constraints. Source: `Comment Rules` (207-213), `Forbidden Patterns / Comment-as-Crutch` (288-290).

Final checklist:

- The checklist restates `N1`-`N8` and `N12`-`N15` as a final scan rather than introducing new retained rules.

## Section coverage review

- `Purpose` (3-18): covered by `M1`, `M3`, `M5`, `M10`, `M12`, `M13`, `N2`, `N3`, and `N5`; the binding policy wording itself is intentionally lost from compressed attachments because it is repository-policy metadata, not an extra construction rule.
- `Primary Directive` (20-33): covered by `M2`, `M3`, `M11`, `M13`, `N2`, and `N5`.
- `Foundational Construction Rules` (35-43): covered by `M3`, `M8`, `M19`, `N2`, and `N6`.
- `Construction Prerequisites and Decisions` (45-53): covered by `M1`, `M2`, `M20`, `N1`, and `N9`; the software-metaphor detail is intentionally lost except where it helps concrete construction decisions through `M1`.
- `Pseudocode Programming Process` (55-62): covered by `M4`; intentionally lost from `nano.md` because it is a complex-routine technique rather than a smallest always-on rule.
- `Routine Design Rules` (64-80): covered by `M5`, `M21`, `N3`, and `N11`.
- `Variable and Data Rules` (82-96): covered by `M6`, `M22`, `N4`, and `N10`.
- `Data Type Rules` (98-108): covered by `M6`, `M7`, `M22`, `N4`, and `N10`.
- `Control Flow Rules` (110-125): covered by `M8`, `M24`, `N2`, `N6`, and `N13`.
- `Statement, Conditional, and Loop Rules` (127-137): covered by `M8`, `M9`, `M24`, `M25`, `N6`, and `N13`.
- `Defensive Programming Rules` (139-152): covered by `M10`, `M11`, `M23`, `M27`, `N5`, `N12`, and `N14`.
- `Error Handling Rules` (154-162): covered by `M10`, `M11`, `M23`, `N5`, and `N12`.
- `Table-Driven and Data-Driven Rules` (164-171): covered by `M9`, `M25`, `N6`, and `N13`.
- `Class and Module Design Rules` (173-186): covered by `M12`, `M26`, and `N3`.
- `Complexity Management Rules` (188-196): covered by `M3`, `M13`, `N2`, and `N6`.
- `Construction with Preconditions and Postconditions` (198-205): covered by `M10`, `M11`, `N5`, and `N14`.
- `Comment Rules` (207-214): covered by `M4`, `M19`, `M31`, `N8`, and `N16`.
- `Coding Standards Rules` (216-223): covered by `M3`, `M19`, `M32`, `N2`, and `N8`.
- `Incremental Construction Rules` (225-232): covered by `M14` and `N7`.
- `Quality, Collaboration, Debugging, and Refactoring` (234-243): covered by `M15`, `M16`, `M28`, `M29`, `N7`, and `N15`; inspection and pair-work details are merged into risk-matched quality practices.
- `Performance, Integration, Tools, and Craftsmanship` (245-255): covered by `M14`, `M17`, `M18`, `M19`, `M30`, `M31`, `N7`, `N8`, and `N15`; the broader craftsmanship phrase is intentionally compressed into current construction-quality discipline.
- `Review Rules` (257-271): covered by `M5`, `M12`, `M13`, `M15`, `M19`, `M21`, `M23`, `M24`, `M26`, and `N3`; the long list is collapsed into trigger rules and final checklist.
- `Forbidden Patterns` (273-296): covered by `M3`, `M5`, `M10`, `M19`, `M21`, `M26`, `M31`, `M32`, `N2`, `N8`, `N11`, and `N16`.
- `Code Generation Rules` (298-316): covered by `M3`, `M5`, `M6`, `M8`, `M10`, `M12`, `M19`, and `N1`; the standalone generation list is merged into the decision rules it repeats.
- `Testing Rules` (318-325): covered by `M9`, `M10`, `M15`, `M27`, `M29`, `N7`, and `N14`.
- `Review Checklist` (327-342): covered by the mini and nano final checklists plus `M1`, `M3`, `M5`, `M10`, `M12`, `M13`, `M19`, `M20`, `M23`, `N2`, `N3`, and `N5`.
- `Final Instruction` (345-354): covered by `M3`, `M8`, `M10`, `M11`, `M13`, `N2`, `N5`, and `N6`.

---

**Source:** [`ciembor/agent-rules-books`](https://github.com/ciembor/agent-rules-books) → `_rule-workbench/code-complete/traceability.md`
