---
name: obey-a-philosophy-of-software-design-by-john-ousterhout
description: "Canonical full source: full.md"
category: frontend-and-design
source_repo: ciembor/agent-rules-books
source_path: "_rule-workbench/a-philosophy-of-software-design/traceability.md"
source_url: https://github.com/ciembor/agent-rules-books/blob/HEAD/_rule-workbench/a-philosophy-of-software-design/traceability.md
---
# OBEY A Philosophy of Software Design by John Ousterhout

Canonical full source: [full.md](full.md)

## Compression decisions

- Re-run under the current `PROCESS.md` on 2026-05-02 for alphabetical book position 1 in `_rule-workbench`.
- `full.md` was restored as a symlink to the canonical source after verifying that the regular file content matched the canonical source. The canonical full source was not edited.
- No `process bug` was found. The current process already says to retain local reasoning, naming, function shape, comments, test discipline, error handling, performance evidence, and anti-shortcut triggers that agents commonly miss.
- The prior `traceability.md` referenced stale section names and line ranges, so it was rebuilt against the actual current `full.md`.
- `mini.md` keeps the book's full operational bias: fight complexity through deep modules, information hiding, caller-centered interfaces, strategic design, exception elimination, naming, comments, testing, and performance evidence.
- `nano.md` keeps the smallest always-on correction: working code and small wrappers are not simple when they leak knowledge, spread special cases, or push complexity to callers.
- No retained rule is treated as `default`; no rule was omitted on the basis that target agents reliably follow it without prompting.

## Source classification

- `Purpose` (3-19): `book-thesis`.
- `Primary Directive` (21-34): `book-thesis`, `conflict-resolver`.
- `Core Complexity Rules` (36-54): `trigger`, `decision-changing`.
- `Module Depth Rules` (57-77): `book-thesis`, `decision-changing`.
- `Information Hiding Rules` (81-92): `decision-changing`.
- `Interface Design Rules` (96-114): `decision-changing`, `micro-decision`.
- `Strategic Programming over Tactical Programming` (118-131): `book-thesis`, `conflict-resolver`.
- `General-Purpose vs Special-Purpose Modules` (135-140): `conflict-resolver`.
- `Error Handling and Exception Elimination` (144-155): `decision-changing`, `conflict-resolver`.
- `Pull Complexity Downward` (159-166): `book-thesis`, `decision-changing`.
- `Comment Rules` (170-185): `micro-decision`, `trigger`.
- `Function and Variable Rules` (189-200): `micro-decision`.
- `Temporal Decomposition Rules` (204-214): `decision-changing`, `trigger`.
- `Special-General Decomposition` (218-227): `conflict-resolver`.
- `Combine or Separate Code` (231-242): `conflict-resolver`, `decision-changing`.
- `Design Alternatives and Comments-First Design` (246-257): `trigger`, `conflict-resolver`.
- `Naming, Consistency, and Obviousness` (261-267): `micro-decision`.
- `Performance, Trends, and Tests` (271-278): `conflict-resolver`, `trigger`.
- `Review Rules` (281-294): `checklist-only`, `trigger`.
- `Forbidden Patterns` (297-314): `trigger`.
- `Code Generation Rules` (317-332): `decision-changing`, `trigger`.
- `Testing Rules` (336-342): `trigger`, `micro-decision`.
- `Review Checklist` (345-357): `checklist-only`.
- `Final Instruction` (361-370): `book-thesis`.

## Mini mapping

Decision rules:

- `M1` Use reduced complexity as the primary success metric and optimize for local understandability rather than size, line count, or cleverness. Source: `Purpose` (3-19), `Primary Directive` (21-34), `Core Complexity Rules` (36-54), `Review Checklist` (345-357), `Final Instruction` (361-370).
- `M2` Treat design as continuous work; do not accept a working patch that worsens future changeability, and compare plausible alternatives for non-trivial design choices. Source: `Strategic Programming over Tactical Programming` (118-131), `Design Alternatives and Comments-First Design` (246-257), `Review Checklist` (345-357).
- `M3` Prefer deep modules and reject shallow wrappers, pass-through services, thin library wrappers, helper modules, and tiny split-outs that add names without reducing reader burden. Source: `Module Depth Rules` (57-77), `Combine or Separate Code` (231-242), `Forbidden Patterns / Shallow Decomposition` (297-302), `Code Generation Rules` (317-332).
- `M4` Design interfaces around caller knowledge rather than implementation mechanics; avoid fragile staging, setup sequences, flags, and arguments that expose internal choices. Source: `Interface Design Rules` (96-114), `Code Generation Rules` (317-332), `Review Checklist` (345-357).
- `M5` Hide volatile decisions, representations, storage shape, protocols, file formats, performance hacks, bookkeeping, normalization, and messy edge handling inside the owning module. Source: `Information Hiding Rules` (81-92), `Forbidden Patterns / Interface Leakage` (303-306), `Code Generation Rules` (317-332).
- `M6` Pull complexity downward when the lower module owns the detail, even if implementation grows slightly, so callers get a simpler public contract and less repeated reasoning. Source: `Pull Complexity Downward` (159-166), `Forbidden Patterns / Complexity Spread` (311-314), `Code Generation Rules` (317-332).
- `M7` Choose generality at the right level and isolate special behavior instead of overfitting, speculating, or polluting the core path with edge cases. Source: `General-Purpose vs Special-Purpose Modules` (135-140), `Special-General Decomposition` (218-227), `Error Handling and Exception Elimination` (144-155).
- `M8` Combine or split by total complexity, not size, runtime order, habit, or aesthetics; keep related state, behavior, invariants, and design decisions together unless the new boundary is deeper. Source: `Function and Variable Rules` (189-200), `Temporal Decomposition Rules` (204-214), `Combine or Separate Code` (231-242).
- `M9` Reduce exception surface by changing interfaces or invariants where possible instead of making every caller repeat defensive ceremony. Source: `Error Handling and Exception Elimination` (144-155), `Special-General Decomposition` (218-227), `Forbidden Patterns / Tactical Complexity Debt` (307-310).
- `M10` Use comments to reduce complexity through contracts, invariants, hidden design decisions, rationale, and tricky facts; do not narrate code or compensate for bad names, poor decomposition, or confusing flow. Source: `Comment Rules` (170-185), `Design Alternatives and Comments-First Design` (250-257), `Review Rules` (281-294).
- `M11` Treat names, consistency, and obviousness as design information; reveal abstractions rather than mechanisms and treat surprising code as complexity. Source: `Interface Design Rules` (98-102), `Naming, Consistency, and Obviousness` (261-267), `Function and Variable Rules` (191-200).
- `M12` Use tests to protect public behavior, interface contracts, hidden complexity through stable APIs, and isolated special cases; do not let test convenience force shallow or leaky interfaces. Source: `Performance, Trends, and Tests` (277-278), `Testing Rules` (336-342).
- `M13` Add performance optimizations, trends, paradigms, patterns, or frameworks only when they reduce complexity in this codebase or evidence shows the tradeoff matters; hide optimization details behind stable interfaces. Source: `Information Hiding Rules` (86), `Performance, Trends, and Tests` (271-278).

Trigger rules:

- `M14` When a feature feels awkward, one change spreads across files, or reviewers must reconstruct hidden dependencies, look for missing information hiding, shallow modules, temporal coupling, or complexity pushed to callers. Source: `Core Complexity Rules` (36-54), `Information Hiding Rules` (81-92), `Review Rules` (281-294), `Forbidden Patterns / Complexity Spread` (311-314).
- `M15` When adding a module, layer, service, helper, wrapper, facade, pattern, option, callback, or argument, prove that it hides more complexity than it adds. Source: `Module Depth Rules` (57-77), `Interface Design Rules` (100-114), `Forbidden Patterns` (297-314), `Code Generation Rules` (317-332).
- `M16` When touching an API, check whether ordinary callers must know sequencing, representation, storage, transport, caching, protocol, file format, internal workflow, or too many setup steps. Source: `Information Hiding Rules` (83-92), `Interface Design Rules` (98-114), `Forbidden Patterns / Interface Leakage` (303-306).
- `M17` When adding a special case, flag, exception path, conditional, or exposed container, first ask whether the owning module can eliminate the invalid state, isolate unusual behavior, or provide a stronger operation. Source: `Interface Design Rules` (110-114), `Error Handling and Exception Elimination` (144-155), `Special-General Decomposition` (218-227), `Forbidden Patterns` (307-314).
- `M18` When splitting, extracting, or introducing variables, check whether the new boundary or name captures meaning or only adds jumps, pass-through state, and visible intermediate steps. Source: `Function and Variable Rules` (189-200), `Combine or Separate Code` (231-242).
- `M19` When code is organized as `prepare/process/finalize`, staged objects, or execution-order phases, verify that temporal structure is the real concept; otherwise reorganize around stable responsibilities. Source: `Temporal Decomposition Rules` (204-214), `Combine or Separate Code` (239-242).
- `M20` When naming is vague, mechanism-focused, inconsistent, or surprising, reconsider the abstraction boundary instead of accepting a near miss. Source: `Interface Design Rules` (102), `Naming, Consistency, and Obviousness` (261-267).
- `M21` When comments get long, duplicate code, justify a confusing interface, or explain usage by exposing internals, redesign the abstraction or move the missing contract to the interface. Source: `Comment Rules` (170-185), `Design Alternatives and Comments-First Design` (250-257), `Review Rules` (292).
- `M22` When optimizing performance, measure first and hide the optimization; do not sacrifice module depth or information hiding without evidence that the tradeoff matters. Source: `Information Hiding Rules` (86), `Performance, Trends, and Tests` (271-275).
- `M23` When testing or reviewing, focus on public behavior, interface contracts, hidden complexity through stable APIs, and special cases isolated behind the abstraction. Source: `Review Rules` (281-294), `Testing Rules` (336-342).

Final checklist:

- The mini checklist restates `M1`, `M3`, `M4`, `M5`, `M6`, `M9`, `M10`, `M11`, and `M13` as a final scan rather than introducing new standalone rules.

## Nano mapping

Decision rules:

- `N1` Optimize for lower cognitive load and local understandability, not shorter files, familiar patterns, fewer lines, or clever compactness. Source: `Purpose` (3-19), `Primary Directive` (21-34), `Core Complexity Rules` (36-54), `Final Instruction` (361-370).
- `N2` Prefer deep modules and reject wrappers, layers, helpers, facades, and split-outs that do not hide real complexity. Source: `Module Depth Rules` (57-77), `Combine or Separate Code` (231-242), `Forbidden Patterns / Shallow Decomposition` (297-302).
- `N3` Hide volatile decisions, representations, storage, protocol facts, workflow bookkeeping, and messy edge handling in one owning module. Source: `Information Hiding Rules` (81-92), `Forbidden Patterns / Interface Leakage` (303-306), `Code Generation Rules` (317-332).
- `N4` Make interfaces caller-centered and semantic; avoid staged APIs, flags, setup sequences, and mechanism leakage when the module can provide the right operation. Source: `Interface Design Rules` (96-114), `Pull Complexity Downward` (159-166), `Error Handling and Exception Elimination` (144-155).
- `N5` Improve ownership and abstraction when a change feels awkward or spreads widely instead of adding tactical special cases. Source: `Core Complexity Rules` (47-53), `Strategic Programming over Tactical Programming` (118-131), `Forbidden Patterns / Tactical Complexity Debt` (307-310).
- `N6` Combine or split by total complexity, keeping shared knowledge together and splitting only at independently understandable boundaries. Source: `Function and Variable Rules` (189-200), `Temporal Decomposition Rules` (204-214), `Combine or Separate Code` (231-242).
- `N7` Treat names and comments as design signals: precise abstraction names, explicit contracts, and no comments that compensate for bad decomposition. Source: `Comment Rules` (170-185), `Design Alternatives and Comments-First Design` (250-257), `Naming, Consistency, and Obviousness` (261-267).
- `N8` Add complexity for performance, trends, patterns, frameworks, tests, or exception handling only when evidence or caller needs justify it. Source: `Error Handling and Exception Elimination` (144-155), `Performance, Trends, and Tests` (271-278), `Testing Rules` (336-342).

Trigger rules:

- `N9` When adding a helper, layer, option, callback, pattern, or abstraction, prove it removes complexity for callers. Source: `Module Depth Rules` (57-77), `Interface Design Rules` (110-114), `Forbidden Patterns` (297-314).
- `N10` When an API requires sequencing, representation, storage, transport, caching, protocol, or file-format knowledge, redesign the boundary. Source: `Information Hiding Rules` (83-92), `Interface Design Rules` (96-114), `Forbidden Patterns / Interface Leakage` (303-306).
- `N11` When naming is hard, comments get long, or reviewers are surprised, treat it as design evidence. Source: `Comment Rules` (170-185), `Design Alternatives and Comments-First Design` (250-257), `Naming, Consistency, and Obviousness` (261-267), `Review Rules` (281-294).
- `N12` When one change spreads widely, look for duplicated knowledge, hidden dependencies, temporal coupling, or the wrong owner. Source: `Core Complexity Rules` (38-53), `Information Hiding Rules` (89-92), `Temporal Decomposition Rules` (204-214), `Forbidden Patterns / Complexity Spread` (311-314).
- `N13` When optimizing or adding exception paths, keep the common path simple and require evidence or a stronger invariant. Source: `Error Handling and Exception Elimination` (144-155), `Special-General Decomposition` (218-227), `Performance, Trends, and Tests` (271-275).

Final checklist:

- The nano checklist restates `N1`, `N2`, `N3`, `N4`, `N7`, and `N8` as a final scan rather than introducing new standalone rules.

## Section coverage review

- `Purpose` (3-19): covered by `M1` and `N1`; binding-language boilerplate is intentionally lost because `mini.md` and `nano.md` are operational attachments rather than policy-definition files.
- `Primary Directive` (21-34): covered by `M1`, `N1`, and the final checklists.
- `Core Complexity Rules` (36-54): symptoms are covered by `M1`, `M14`, `N1`, and `N12`; default-response questions are merged into `M14`-`M17`.
- `Module Depth Rules` (57-77): covered by `M3`, `M15`, `N2`, and `N9`.
- `Information Hiding Rules` (81-92): covered by `M5`, `M16`, `N3`, and `N10`.
- `Interface Design Rules` (96-114): covered by `M4`, `M15`, `M16`, `N4`, `N9`, and `N10`.
- `Strategic Programming over Tactical Programming` (118-131): covered by `M2`, `M14`, `N5`; deadline and copy/paste examples are merged into tactical-complexity rules.
- `General-Purpose vs Special-Purpose Modules` (135-140): covered by `M7`; kept out of `nano.md` as a standalone rule but represented by `N2`, `N5`, and `N9`.
- `Error Handling and Exception Elimination` (144-155): covered by `M7`, `M9`, `M17`, `N4`, `N8`, and `N13`.
- `Pull Complexity Downward` (159-166): covered by `M6`, `M14`, `N4`, and `N5`.
- `Comment Rules` (170-185): covered by `M10`, `M21`, `N7`, and `N11`.
- `Function and Variable Rules` (189-200): covered by `M8`, `M11`, `M18`, and `N6`.
- `Temporal Decomposition Rules` (204-214): covered by `M8`, `M14`, `M19`, `N6`, and `N12`.
- `Special-General Decomposition` (218-227): covered by `M7`, `M9`, `M17`, and `N13`.
- `Combine or Separate Code` (231-242): covered by `M3`, `M8`, `M18`, `M19`, `N2`, and `N6`.
- `Design Alternatives and Comments-First Design` (246-257): covered by `M2`, `M10`, `M21`, `N7`, and `N11`; detailed comments-first timing is merged into design and comment triggers.
- `Naming, Consistency, and Obviousness` (261-267): covered by `M11`, `M20`, `N7`, and `N11`.
- `Performance, Trends, and Tests` (271-278): covered by `M12`, `M13`, `M22`, `M23`, `N8`, and `N13`.
- `Review Rules` (281-294): covered by `M14`-`M17`, `M21`, `M23`, `N9`-`N12`; list form is merged into triggers and checklist.
- `Forbidden Patterns` (297-314): covered by `M3`, `M4`, `M6`, `M9`, `M15`, `M16`, `M17`, `N2`, `N5`, `N9`, `N10`, and `N12`.
- `Code Generation Rules` (317-332): covered by `M1`, `M3`-`M6`, `M7`, `M15`, `N1`-`N5`, and `N9`-`N10`; standalone generation sequence is intentionally merged.
- `Testing Rules` (336-342): covered by `M12`, `M23`, and `N8`; detailed bullet shape is merged into public-contract testing.
- `Review Checklist` (345-357): covered by the mini and nano final checklists and by `M1`, `M3`-`M6`, `M9`, `M11`, `N1`-`N5`, and `N7`.
- `Final Instruction` (361-370): covered by `M1`, `M3`, `M5`, `M6`, `M9`, `N1`, `N2`, and `N3`.

## Omission and merge notes

- No current source section is wholly intentionally lost.
- Repeated examples and anti-pattern bullets are merged into the mapped `M*` and `N*` rules above when they have the same operational consequence.
- `MUST`/`SHOULD`/`MUST NOT` policy-language mechanics from `Purpose` (17) are intentionally lost in compressed attachments; the underlying binding decisions survive as direct imperatives.
- Subsection labels such as `Prefer Deep Modules`, `Avoid Shallow Modules`, `Strategic Programming`, `Tactical Programming`, and the `Forbidden Patterns` categories are merged into rule and trigger wording instead of retained as separate headings.
- Review-list bullets are intentionally collapsed into triggers and final checklist items; their operational effects survive through `M14`-`M17`, `M21`, `M23`, and `N9`-`N12`.
- Testing detail is collapsed into `M12` and `M23`; `nano.md` keeps only the broader always-on evidence and interface-contract guard through `N8`.

---

**Source:** [`ciembor/agent-rules-books`](https://github.com/ciembor/agent-rules-books) → `_rule-workbench/a-philosophy-of-software-design/traceability.md`
