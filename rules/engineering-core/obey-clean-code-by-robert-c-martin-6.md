---
name: obey-clean-code-by-robert-c-martin
description: "Canonical full source: full.md"
category: engineering-core
source_repo: ciembor/agent-rules-books
source_path: "_rule-workbench/clean-code/traceability.md"
source_url: https://github.com/ciembor/agent-rules-books/blob/HEAD/_rule-workbench/clean-code/traceability.md
---
# OBEY Clean Code by Robert C. Martin

Canonical full source: [full.md](full.md)

## Compression decisions

- Re-run under the current `PROCESS.md` on 2026-05-02 for alphabetical book position 3: `clean-code`.
- The canonical source is `clean-code/clean-code.md`; `_rule-workbench/clean-code/full.md` resolves to that source and was not edited as rule content.
- This pass found book-specific misses, not a process bug. The current process already requires retaining book-thesis, decision-changing, micro-decision, boundary, local reasoning, mutation visibility, test discipline, and anti-shortcut trigger rules.
- `mini.md` keeps Clean Code's delivery bias, local readability discipline, naming pressure, small-function shape, command/query separation, explicit error and cleanup handling, boundary isolation, clean tests, emergent design, and proportional cleanup.
- `nano.md` stays compact but keeps the smallest always-on reminders that working code is not automatically clean, touched code should become cleaner within scope, and confusing names, mutation, flags, comments, and boundaries should not be normalized.
- Detailed formatting mechanics, comment categories, class-size lists, exception taxonomy, TDD mechanics, concurrency instrumentation, smell catalog items, output-reporting prose, and review lists are compressed into decision or trigger rules unless their standalone wording changes a repeated agent decision.

## Mini mapping

Decision rules:

- `M1` Treat cleanliness as part of delivery; preserve behavior, leave touched code cleaner within scope, and reject schedule or rewrite excuses for new mess. Source: `Priority and behavior` (5-12), `Core clean code principles` (14-22), `Refactoring rules` (188-197), `Emergent design and successive refinement` (199-205), `Hard rules` (290-297).
- `M2` Write for local reasoning so readers do not reconstruct hidden state, wide jumps, or naming trivia. Source: `Core clean code principles` (14-22), `Formatting and structure` (81-91), `Class and module design` (104-113), `Implementation preferences` (255-264), `Review checklist` (266-279).
- `M3` Use precise names and one term per concept; rename when vocabulary hides intent, overloads meaning, or forces comments to compensate. Source: `Naming rules` (24-42), `Function rules` (44-62), `Comment rules` (64-79), `Refactoring rules` (188-197), `Smells to detect and eliminate` (207-240), `Change Process` (242-253), `Hard rules` (290-297).
- `M4` Keep functions small, focused, top-down, and at one abstraction level. Source: `Function rules` (44-62), `Formatting and structure` (81-91), `Smells to detect and eliminate` (207-240), `Review checklist` (266-279).
- `M5` Keep parameters few and meaningful; avoid boolean flags, output parameters, and grab-bag argument lists by modeling the concept. Source: `Function rules` (44-62), `Smells to detect and eliminate` (207-240).
- `M6` Separate commands from queries and eliminate hidden side effects. Source: `Function rules` (44-62), `Smells to detect and eliminate` (207-240), `Hard rules` (290-297).
- `M7` Keep the happy path readable; isolate error handling, invalid-state handling, and cleanup; prefer explicit optionality or typed results over null-like sentinel flow when supported. Source: `Function rules` (44-62), `Error handling` (115-124), `Concurrency and async work` (172-186), `Review checklist` (266-279).
- `M8` Expose behavior rather than raw representation and avoid train-wreck access, utility dumping grounds, and mixed responsibilities. Source: `Objects, modules, and data structures` (93-102), `Class and module design` (104-113), `Smells to detect and eliminate` (207-240).
- `M9` Keep construction, framework, persistence, transaction, security, and vendor details outside business behavior. Source: `Objects, modules, and data structures` (93-102), `Boundaries and external dependencies` (126-132), `System construction rules` (134-143), `Implementation preferences` (255-264).
- `M10` Make public APIs small, explicit, and hard to misuse; encode boundary logic, required order, and likely changes where readers can see them. Source: `Objects, modules, and data structures` (93-102), `Class and module design` (104-113), `Error handling` (115-124), `Boundaries and external dependencies` (126-132), `Implementation preferences` (255-264).
- `M11` Use comments only for rationale, constraints, warnings, or external contracts; never as a bandage for bad names or structure. Source: `Naming rules` (24-42), `Comment rules` (64-79), `Change Process` (242-253), `Review checklist` (266-279), `Hard rules` (290-297).
- `M12` Treat tests as production code and back changes with proportionate validation before calling them done. Source: `Tests` (145-157), `TDD and clean test rules` (159-170), `Change Process` (242-253), `Review checklist` (266-279), `Output Expectations` (281-288).
- `M13` Let design emerge through tests, duplication removal, expressiveness, and minimal structure; avoid needless abstractions and infrastructure. Source: `Priority and behavior` (5-12), `System construction rules` (134-143), `Refactoring rules` (188-197), `Emergent design and successive refinement` (199-205), `Implementation preferences` (255-264).
- `M14` When touching code, remove the smell that most increases change cost without silently broadening the task beyond the smallest cleanup that keeps the change safe. Source: `Priority and behavior` (5-12), `Refactoring rules` (188-197), `Emergent design and successive refinement` (199-205), `Smells to detect and eliminate` (207-240), `Change Process` (242-253), `Hard rules` (290-297).

Trigger rules:

- `M15` When a function mixes setup, validation, computation, and side effects, split the phases. Source: `Function rules` (44-62), `Smells to detect and eliminate` (207-240).
- `M16` When a comment explains control flow, simplify names or structure before keeping the comment. Source: `Comment rules` (64-79), `Change Process` (242-253), `Hard rules` (290-297).
- `M17` When a function both mutates and answers, or hides a mode switch behind a flag, separate the responsibilities. Source: `Function rules` (44-62), `Smells to detect and eliminate` (207-240), `Hard rules` (290-297).
- `M18` When duplication, repeated switches, or primitive clusters appear, name the concept with an argument object, polymorphism, special case, or another small abstraction. Source: `Function rules` (44-62), `Refactoring rules` (188-197), `Emergent design and successive refinement` (199-205), `Smells to detect and eliminate` (207-240).
- `M19` When a boundary leaks framework, vendor, or persistence quirks inward, add or strengthen a local adapter. Source: `Objects, modules, and data structures` (93-102), `Boundaries and external dependencies` (126-132), `System construction rules` (134-143), `Implementation preferences` (255-264).
- `M20` When async or concurrency enters, isolate threading policy, minimize shared mutable state, define shutdown, and test timing-sensitive behavior. Source: `Error handling` (115-124), `Concurrency and async work` (172-186), `Smells to detect and eliminate` (207-240).
- `M21` When fixing a bug or changing behavior, add or update the test that protects the intended contract. Source: `Tests` (145-157), `TDD and clean test rules` (159-170), `Change Process` (242-253), `Review checklist` (266-279).
- `M22` When cleanup starts spreading into unrelated areas, cut back to the smallest refactor that keeps the requested change safe and readable. Source: `Priority and behavior` (5-12), `Refactoring rules` (188-197), `Emergent design and successive refinement` (199-205), `Change Process` (242-253), `Hard rules` (290-297).

Final checklist:

- The checklist restates `M2`, `M3`, `M6`, `M7`, `M9`, `M12`, and `M14` as a final scan rather than introducing new rules.

## Nano mapping

Decision rules:

- `N1` Preserve behavior, write for the next reader, and leave touched code cleaner within scope. Source: `Priority and behavior` (5-12), `Core clean code principles` (14-22), `Refactoring rules` (188-197), `Emergent design and successive refinement` (199-205), `Hard rules` (290-297).
- `N2` Write for local reasoning and use precise names with one term per concept. Source: `Core clean code principles` (14-22), `Naming rules` (24-42), `Formatting and structure` (81-91), `Review checklist` (266-279).
- `N3` Split boolean flags, mixed abstraction levels, and hidden side effects out of functions. Source: `Function rules` (44-62), `Smells to detect and eliminate` (207-240).
- `N4` Separate commands from queries and keep parameters small and meaningful. Source: `Function rules` (44-62), `Hard rules` (290-297).
- `N5` Keep the happy path readable and make invalid states, errors, and cleanup explicit instead of implicit. Source: `Function rules` (44-62), `Error handling` (115-124), `Concurrency and async work` (172-186).
- `N6` Use comments only for rationale or contracts, not to explain confusing code. Source: `Comment rules` (64-79), `Hard rules` (290-297).
- `N7` When touching code, remove the smell most likely to make the next change risky or unclear. Source: `Priority and behavior` (5-12), `Refactoring rules` (188-197), `Emergent design and successive refinement` (199-205), `Smells to detect and eliminate` (207-240).

Trigger rules:

- `N8` When a function both mutates and answers, split it. Source: `Function rules` (44-62), `Hard rules` (290-297).
- `N9` When a comment explains the flow, simplify the code first. Source: `Comment rules` (64-79), `Change Process` (242-253).
- `N10` When async, concurrency, or framework quirks spread the change, reduce shared mutable state and add the right boundary instead of more branching. Source: `Objects, modules, and data structures` (93-102), `Boundaries and external dependencies` (126-132), `System construction rules` (134-143), `Concurrency and async work` (172-186).

Final checklist:

- The checklist restates `N2`, `N3`, `N4`, and `N7` as a final scan rather than introducing new rules.

## Section coverage review

- `Priority and behavior` (5-12): covered by `M1`, `M13`, `M14`, `M22`, `N1`, and `N7`; modal priority wording is intentionally lost as standalone prose because compressed rules are already operational instructions.
- `Core clean code principles` (14-22): covered by `M1`, `M2`, `N1`, and `N2`.
- `Naming rules` (24-42): covered by `M3`, `M11`, and `N2`; detailed examples such as pronounceability, searchability, and cute names are intentionally lost as standalone wording but preserved through precise naming and one-term vocabulary pressure.
- `Function rules` (44-62): covered by `M4`, `M5`, `M6`, `M7`, `M15`, `M17`, `M18`, `N3`, `N4`, `N5`, and `N8`.
- `Comment rules` (64-79): covered by `M11`, `M16`, `N6`, and `N9`; individual good-comment categories are merged into rationale, constraints, warnings, and external contracts.
- `Formatting and structure` (81-91): covered by `M2`, `M4`, and `N2`; detailed whitespace, line-length, and decorative-alignment mechanics are intentionally lost in favor of project formatter and scanning rules.
- `Objects, modules, and data structures` (93-102): covered by `M8`, `M9`, `M10`, `M19`, and `N10`.
- `Class and module design` (104-113): covered by `M2`, `M8`, and `M10`; constructor/setup details are merged into `M9`.
- `Error handling` (115-124): covered by `M7`, `M10`, `M20`, and `N5`; fine-grained exception-shape details are merged into typed caller decisions and explicit invalid-state handling.
- `Boundaries and external dependencies` (126-132): covered by `M9`, `M10`, `M19`, and `N10`; learning tests survive as proportionate boundary validation through `M12` and `M21`.
- `System construction rules` (134-143): covered by `M9`, `M13`, `M19`, and `N10`; standards, AOP, and DSL details are intentionally lost except where they preserve visible business flow or demonstrable value.
- `Tests` (145-157): covered by `M12` and `M21`.
- `TDD and clean test rules` (159-170): covered by `M12` and `M21`; exact TDD cycle, one-assert preference, helper DSL, and coverage-tool nuance are intentionally lost as standalone wording while behavior validation and clean-test pressure survive.
- `Concurrency and async work` (172-186): covered by `M7`, `M20`, `N5`, and `N10`; lock-strategy and platform-variation details are intentionally lost as standalone wording but preserved through shutdown, ownership, execution-model, and timing-sensitive testing pressure.
- `Refactoring rules` (188-197): covered by `M1`, `M13`, `M14`, `M18`, `M22`, `N1`, and `N7`.
- `Emergent design and successive refinement` (199-205): covered by `M1`, `M13`, `M14`, `M18`, `M22`, `N1`, and `N7`.
- `Smells to detect and eliminate` (207-240): covered by `M3`, `M4`, `M5`, `M6`, `M8`, `M14`, `M15`, `M17`, `M18`, `M20`, `N3`, and `N7`; the long smell catalog is intentionally collapsed into trigger rules and final checks.
- `Change Process` (242-253): covered by `M3`, `M11`, `M12`, `M14`, `M16`, `M21`, `M22`, and `N9`.
- `Implementation preferences` (255-264): covered by `M2`, `M9`, `M10`, and `M13`; anti-premature-optimization and dependency-selection details are intentionally lost as standalone wording because they are generic unless a local project convention or complexity tradeoff triggers them.
- `Review checklist` (266-279): covered by `M2`, `M3`, `M4`, `M7`, `M12`, `M13`, `M14`, and the compressed final checklist; collapsed from checklist prose into operational rules.
- `Output Expectations` (281-288): mostly intentionally lost as standalone prose because it governs final reporting rather than compressed coding behavior; validation reporting survives through `M12`.
- `Hard rules` (290-297): covered by `M1`, `M3`, `M6`, `M11`, `M14`, `M17`, `M22`, `N1`, `N4`, `N6`, and `N8`.

---

**Source:** [`ciembor/agent-rules-books`](https://github.com/ciembor/agent-rules-books) → `_rule-workbench/clean-code/traceability.md`
