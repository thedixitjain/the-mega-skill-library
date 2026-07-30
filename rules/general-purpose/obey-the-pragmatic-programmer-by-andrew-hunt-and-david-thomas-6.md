---
name: obey-the-pragmatic-programmer-by-andrew-hunt-and-david-thomas
description: "Canonical full source: full.md"
category: general-purpose
source_repo: ciembor/agent-rules-books
source_path: "_rule-workbench/the-pragmatic-programmer/traceability.md"
source_url: https://github.com/ciembor/agent-rules-books/blob/HEAD/_rule-workbench/the-pragmatic-programmer/traceability.md
---
# OBEY The Pragmatic Programmer by Andrew Hunt and David Thomas

Canonical full source: [full.md](full.md)

## Compression decisions

- Re-run under `_rule-workbench/PROCESS.md` on 2026-05-02 for book 12 in alphabetical order: `the-pragmatic-programmer`.
- Recompressed against the current 359-line canonical source. The prior traceability referenced stale section names and line ranges, so this pass updates `mini.md`, `nano.md`, and all mappings instead of preserving the old compressed output.
- No rule is labeled `default`; even generic-seeming ownership, naming, testing, feedback, automation, and communication rules are common agent failure points under local implementation pressure.
- This was a book-specific miss, not a process bug. `PROCESS.md` already requires current source ranges, full-to-mini section review, and retention of rules affecting boundaries, invariants, failure semantics, local reasoning, communication, test discipline, cancellation and cleanup semantics, and repeated local implementation choices.
- `mini.md` keeps the book's distinctive pragmatic bias across ownership, DRY, orthogonality, reversibility, tracer feedback, prototype discipline, requirements discovery, automation, explicit contracts, failure handling, resource ownership, plain text, state, tooling, debugging, increments, communication, team responsibility, and broken-window containment.
- `nano.md` keeps only always-on reminders that prevent the highest-risk shortcuts: local-only ownership, copied knowledge, hidden coupling, irreversible guesses, fossilized prototypes, manual rituals, unclear failures and cleanup, invisible shared state, coincidence debugging, skipped tests, implementation-shaped requirements, and quality decay.
- Individual named habits, detailed tool examples, exact checklist wording, and review anti-pattern lists are merged into operational rules unless their standalone wording changes a common agent decision.

## Mini mapping

Decision rules:

- `M1` Be pragmatic, not dogmatic; choose practices and stopping points by real outcomes. Source: `Purpose` (3-17), `Primary Directive` (21-32), `Core Pragmatic Principles` (53-61), `Project and Team Rules` (248-255), `Forbidden Patterns` (283-287).
- `M2` Own the result and surface tradeoffs, risks, uncertainty, and avoidable design costs. Source: `Purpose` (3-17), `Core Pragmatic Principles` (38-42), `Project and Team Rules` (248-255), `Review Rules` (268-280).
- `M3` Think beyond the local edit and leave touched areas better where the cost is low. Source: `Core Pragmatic Principles` (43-47), `Broken Windows Rule` (259-264), `Review Checklist` (334-346), `Final Instruction` (350-359).
- `M4` Keep one authoritative representation for each piece of system knowledge. Source: `Purpose` (8-15), `Primary Directive` (25-32), `DRY Rules` (64-79), `Code Generation Rules` (306-322), `Review Checklist` (334-346), `Final Instruction` (350-359).
- `M5` Preserve orthogonality with independent components, narrow interfaces, and separated concerns. Source: `Purpose` (8-15), `Primary Directive` (25-32), `Orthogonality Rules` (82-93), `Resource and Coupling Rules` (235-244), `Review Rules` (268-280), `Final Instruction` (350-359).
- `M6` Keep volatile decisions reversible until evidence justifies commitment. Source: `Core Pragmatic Principles` (48-52), `Reversibility, Domain Languages, and Requirements` (110-120), `Text and Data Rules` (189-195), `Final Instruction` (350-359).
- `M7` Use domain vocabulary and small domain languages only when they clarify rules for their readers. Source: `Reversibility, Domain Languages, and Requirements` (110-120), `Naming and Communication Rules` (179-185).
- `M8` Prefer thin end-to-end tracer bullets to validate architecture, integration, and assumptions early. Source: `Purpose` (8-15), `Tracer Bullets and Iterative Delivery` (96-107), `Code Generation Rules` (306-322).
- `M9` Use prototypes for learning while preventing experimental shortcuts from becoming production defaults. Source: `Tracer Bullets and Iterative Delivery` (103-107), `Prototyping Rules` (123-129), `Forbidden Patterns` (301-303), `Review Checklist` (334-346).
- `M10` Dig for real requirements and separate durable needs from implementation details, solution proposals, stale specs, and unresolved hesitation. Source: `Reversibility, Domain Languages, and Requirements` (110-120), `Estimation and Increment Rules` (207-213).
- `M11` Automate repetitive, error-prone, easy-to-forget, or ritualized work and keep shared checks reproducible. Source: `Purpose` (8-15), `DRY Rules` (72-77), `Automation Rules` (132-143), `Tooling Rules` (216-231), `Forbidden Patterns` (285-299), `Code Generation Rules` (306-322), `Testing Rules` (325-331), `Review Checklist` (334-346), `Final Instruction` (350-359).
- `M12` Shorten feedback loops with relevant tests, automated checks, visible failures, and cheap early signals. Source: `Purpose` (8-15), `Primary Directive` (25-32), `Feedback Loop Rules` (146-153), `Code Generation Rules` (306-322), `Testing Rules` (325-331), `Review Checklist` (334-346), `Final Instruction` (350-359).
- `M13` Make contracts, assumptions, invariants, responsibilities, and obligations explicit and close to the protected abstraction. Source: `Design by Contract and Assertions` (156-167), `Code Generation Rules` (306-322), `Review Checklist` (334-346).
- `M14` Separate failure types, preserve diagnostic context, and contain failure boundaries. Source: `Design by Contract and Assertions` (156-167), `Error Handling and Recovery` (170-176), `Review Rules` (268-280).
- `M15` Treat resource ownership and cleanup as explicit contracts on success and failure paths. Source: `Resource and Coupling Rules` (235-244), `Review Checklist` (334-346).
- `M16` Prefer inspectable text, open formats, scripts, explicit serialization, and version-aware configuration where longevity and automation matter. Source: `Text and Data Rules` (189-195), `Tooling Rules` (223-231).
- `M17` Treat shared mutable state, ambient context, globals, temporal coupling, and async complexity as visible costs. Source: `Orthogonality Rules` (82-93), `State and Concurrency Rules` (198-204), `Resource and Coupling Rules` (235-244).
- `M18` Use tools as leverage, but understand generated code, formal methods, specifications, and tool output before relying on them. Source: `Tooling Rules` (216-231), `Forbidden Patterns` (285-303).
- `M19` Debug from reproduced facts by observing, isolating, explaining, fixing, and verifying. Source: `Tooling Rules` (230-231).
- `M20` Break work into small deliverable increments with honest uncertainty, visible risk, and estimates corrected by feedback. Source: `Tracer Bullets and Iterative Delivery` (96-107), `Estimation and Increment Rules` (207-213).
- `M21` Communicate engineering intent through code, names, docs, comments, commit messages, scripts, tests, and artifacts. Source: `Core Pragmatic Principles` (53-61), `Naming and Communication Rules` (179-185), `Project and Team Rules` (248-255), `Review Rules` (268-280).
- `M22` Build teams and work around shared responsibility, explicit expectations, automation, fast feedback, visible quality, and defensible artifacts. Source: `Project and Team Rules` (248-255).
- `M23` Apply the broken windows rule by fixing or visibly containing quality decay. Source: `Core Pragmatic Principles` (53-61), `Broken Windows Rule` (259-264), `Review Checklist` (334-346).

Trigger rules:

- `M24` Copied facts trigger source-of-truth ownership and derivation, generation, validation, or traceability. Source: `DRY Rules` (64-79), `Forbidden Patterns` (289-292), `Review Rules` (268-280), `Review Checklist` (334-346).
- `M25` Unrelated places changing together trigger boundary repair and hidden-coupling removal. Source: `Orthogonality Rules` (82-93), `Forbidden Patterns` (293-295), `Review Rules` (268-280).
- `M26` Hard-coded volatile details trigger validated, controlled, versioned configuration, metadata, or an explicit abstraction. Source: `Reversibility, Domain Languages, and Requirements` (110-120), `Text and Data Rules` (189-195).
- `M27` High uncertainty or irreversible decisions trigger tracer feedback, prototypes, smaller reversible steps, or delayed commitment. Source: `Core Pragmatic Principles` (48-52), `Tracer Bullets and Iterative Delivery` (96-107), `Reversibility, Domain Languages, and Requirements` (110-120), `Estimation and Increment Rules` (207-213).
- `M28` Prototype code, generated scaffolds, diagrams, specs, formal models, or tool output becoming production truth triggers deliberate inspection, understanding, hardening, replacement, or rejection. Source: `Tracer Bullets and Iterative Delivery` (103-107), `Prototyping Rules` (123-129), `Tooling Rules` (229-231), `Forbidden Patterns` (301-303).
- `M29` Prose specifications growing without reduced uncertainty trigger a working slice, example, or prototype. Source: `Reversibility, Domain Languages, and Requirements` (116-119), `Tracer Bullets and Iterative Delivery` (96-107).
- `M30` Hidden assumptions in comments, caller folklore, or setup rituals trigger code, contracts, tests, scripts, or checked configuration. Source: `Design by Contract and Assertions` (156-167), `Automation Rules` (132-143), `Review Rules` (268-280).
- `M31` Errors or resources crossing boundaries trigger recovery, diagnostic-context, and cleanup ownership decisions. Source: `Error Handling and Recovery` (170-176), `Resource and Coupling Rules` (235-244).
- `M32` Shared state, async behavior, locks, ordering, or temporal coupling trigger explicit ownership, synchronization, cleanup, and ordering requirements. Source: `State and Concurrency Rules` (198-204), `Resource and Coupling Rules` (235-244).
- `M33` Repeated manual steps, human checks, environment rituals, or release procedures trigger automation and versioning. Source: `DRY Rules` (72-77), `Automation Rules` (132-143), `Forbidden Patterns` (285-299).
- `M34` Slow, flaky, environment-dependent, or setup-heavy tests trigger feedback-path improvement instead of skipped checks. Source: `Feedback Loop Rules` (146-153), `Testing Rules` (325-331).
- `M35` Human-found bugs trigger automatic regression tests around the protected contract. Source: `Testing Rules` (325-331), `Feedback Loop Rules` (146-153).
- `M36` Unexplained working behavior triggers proof with data before dependency. Source: `Tooling Rules` (230-231), `Design by Contract and Assertions` (156-167).
- `M37` Local decay in touched code triggers a cheap fix or explicit containment and cleanup path. Source: `Core Pragmatic Principles` (43-47), `Broken Windows Rule` (259-264), `Review Checklist` (334-346).

Final checklist:

- The checklist restates `M3`-`M6`, `M8`-`M9`, `M11`-`M17`, `M21`, and `M23` as a final scan rather than introducing new rules. Source: `Review Checklist` (334-346), `Final Instruction` (350-359).

## Nano mapping

Decision rules:

- `N1` Be pragmatic, not dogmatic; choose what improves real outcomes. Source: `Primary Directive` (21-32), `Core Pragmatic Principles` (53-61), `Forbidden Patterns` (283-287).
- `N2` Keep one authoritative source for each piece of system knowledge. Source: `Purpose` (8-15), `DRY Rules` (64-79), `Final Instruction` (350-359).
- `N3` Preserve orthogonality across concerns, business rules, views, and volatile details. Source: `Purpose` (8-15), `Orthogonality Rules` (82-93), `Resource and Coupling Rules` (235-244), `Final Instruction` (350-359).
- `N4` Keep important choices reversible until evidence justifies commitment. Source: `Core Pragmatic Principles` (48-52), `Reversibility, Domain Languages, and Requirements` (110-120).
- `N5` Learn through working slices, prototypes, examples, tests, and fast feedback without fossilizing shortcuts. Source: `Tracer Bullets and Iterative Delivery` (96-107), `Prototyping Rules` (123-129), `Feedback Loop Rules` (146-153), `Forbidden Patterns` (301-303).
- `N6` Automate repeatable work under version control and favor inspectable text or scripts where longevity and recovery matter. Source: `Automation Rules` (132-143), `Text and Data Rules` (189-195), `Tooling Rules` (216-231), `Forbidden Patterns` (285-299).
- `N7` Make assumptions, contracts, failure boundaries, diagnostics, resource ownership, cleanup, and ordering explicit. Source: `Design by Contract and Assertions` (156-167), `Error Handling and Recovery` (170-176), `Resource and Coupling Rules` (235-244).
- `N8` Treat shared mutable state, globals, ambient context, and async complexity as visible costs. Source: `Orthogonality Rules` (82-93), `State and Concurrency Rules` (198-204), `Resource and Coupling Rules` (235-244).
- `N9` Debug from reproduced facts and measured behavior. Source: `Tooling Rules` (230-231).
- `N10` Run relevant automatic tests before calling work done. Source: `Feedback Loop Rules` (146-153), `Testing Rules` (325-331).
- `N11` Dig for real requirements behind stated solutions and current implementation details. Source: `Reversibility, Domain Languages, and Requirements` (110-120).
- `N12` Leave touched work in a condition you can stand behind. Source: `Core Pragmatic Principles` (38-61), `Project and Team Rules` (248-255), `Broken Windows Rule` (259-264), `Final Instruction` (350-359).

Trigger rules:

- `N13` Copied knowledge triggers one owner and derivation or traceability. Source: `DRY Rules` (64-79), `Forbidden Patterns` (289-292).
- `N14` Wide fan-out changes trigger orthogonality repair. Source: `Orthogonality Rules` (82-93), `Forbidden Patterns` (293-295).
- `N15` Uncertain or hard-to-reverse decisions trigger feedback or smaller steps. Source: `Tracer Bullets and Iterative Delivery` (96-107), `Reversibility, Domain Languages, and Requirements` (110-120).
- `N16` Repeated manual steps trigger automation and versioning. Source: `Automation Rules` (132-143), `Forbidden Patterns` (285-299).
- `N17` Unexplained, generated, scaffolded, or tool-derived behavior triggers inspection and proof. Source: `Prototyping Rules` (123-129), `Tooling Rules` (229-231), `Forbidden Patterns` (301-303).
- `N18` Cross-boundary errors, resources, state, locks, or ordering trigger explicit recovery and cleanup ownership. Source: `Error Handling and Recovery` (170-176), `State and Concurrency Rules` (198-204), `Resource and Coupling Rules` (235-244).
- `N19` Implementation-shaped requirements trigger restating the durable need. Source: `Reversibility, Domain Languages, and Requirements` (110-120).

Final checklist:

- The checklist restates `N2`-`N8`, `N10`, and `N12` as a final scan rather than introducing new rules. Source: `Review Checklist` (334-346), `Final Instruction` (350-359).

## Section coverage review

- `Purpose` (3-17): covered by `M1`, `M2`, `M4`, `M8`, `M11`, `M12`, `N2`, and `N3`.
- `Primary Directive` (21-32): covered by `M1`, `M4`-`M6`, `M12`, `N1`, `N2`, and `N3`; exact priority wording is merged into the primary bias and final checklist.
- `Core Pragmatic Principles` (36-61): covered by `M1`-`M3`, `M6`, `M21`, `M23`, `M27`, `M37`, `N1`, `N4`, and `N12`; personal knowledge-portfolio detail is intentionally lost from compressed files.
- `DRY Rules` (64-79): covered by `M4`, `M11`, `M24`, `M33`, `N2`, `N13`, and `N16`.
- `Orthogonality Rules` (82-93): covered by `M5`, `M17`, `M25`, `N3`, `N8`, and `N14`.
- `Tracer Bullets and Iterative Delivery` (96-107): covered by `M8`, `M9`, `M20`, `M27`, `M29`, `N5`, and `N15`.
- `Reversibility, Domain Languages, and Requirements` (110-120): covered by `M6`, `M7`, `M10`, `M26`, `M27`, `M29`, `N4`, `N11`, `N15`, and `N19`.
- `Prototyping Rules` (123-129): covered by `M9`, `M28`, `N5`, and `N17`.
- `Automation Rules` (132-143): covered by `M11`, `M30`, `M33`, `N6`, and `N16`.
- `Feedback Loop Rules` (146-153): covered by `M12`, `M34`, `M35`, `N5`, and `N10`.
- `Design by Contract and Assertions` (156-167): covered by `M13`, `M14`, `M30`, `M36`, and `N7`.
- `Error Handling and Recovery` (170-176): covered by `M14`, `M31`, `N7`, and `N18`.
- `Naming and Communication Rules` (179-185): covered by `M7` and `M21`; generic clarity wording is merged into communication discipline.
- `Text and Data Rules` (189-195): covered by `M6`, `M16`, `M26`, and `N6`.
- `State and Concurrency Rules` (198-204): covered by `M17`, `M32`, `N8`, and `N18`.
- `Estimation and Increment Rules` (207-213): covered by `M10`, `M20`, and `M27`; exact estimation mechanics are merged into honest uncertainty and feedback correction.
- `Tooling Rules` (216-231): covered by `M11`, `M16`, `M18`, `M19`, `M28`, `M36`, `N6`, `N9`, and `N17`; individual editor and shell-tool examples are merged into tool-leverage rules.
- `Resource and Coupling Rules` (235-244): covered by `M5`, `M15`, `M17`, `M31`, `M32`, `N3`, `N7`, `N8`, and `N18`; metaprogramming, blackboard coordination, and algorithmic-growth detail are merged into explicit-cost and understand-before-relying rules.
- `Project and Team Rules` (248-255): covered by `M1`, `M2`, `M21`, `M22`, `N1`, and `N12`.
- `Broken Windows Rule` (259-264): covered by `M3`, `M23`, `M37`, and `N12`.
- `Review Rules` (268-280): covered by `M2`, `M4`, `M5`, `M11`, `M14`, `M21`, `M24`, `M25`, and `M30`; review list wording is collapsed into operational rules and triggers.
- `Forbidden Patterns` (283-303): covered by `M1`, `M4`, `M5`, `M9`, `M11`, `M18`, `M24`, `M25`, `M28`, `M33`, `N1`, `N2`, `N3`, `N5`, `N6`, `N13`, `N14`, `N16`, and `N17`.
- `Code Generation Rules` (306-322): covered by `M4`, `M5`, `M8`, `M11`-`M13`; code-generation checklist is merged into the main decision rules.
- `Testing Rules` (325-331): covered by `M11`, `M12`, `M34`, `M35`, `N10`, and `N16`.
- `Review Checklist` (334-346): covered by `M3`-`M5`, `M9`, `M11`-`M14`, `M23`, `M24`, `M37`, `N2`, `N3`, `N5`, `N6`, `N7`, and `N12`; checklist wording is collapsed into compressed final checks.
- `Final Instruction` (350-359): covered by `M3`-`M6`, `M11`, `M12`, `N2`, `N3`, and `N12`.

---

**Source:** [`ciembor/agent-rules-books`](https://github.com/ciembor/agent-rules-books) → `_rule-workbench/the-pragmatic-programmer/traceability.md`
