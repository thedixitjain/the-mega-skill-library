---
name: obey-refactoringguru
description: "Canonical full source: full.md"
category: engineering-core
source_repo: ciembor/agent-rules-books
source_path: "_rule-workbench/refactoring-guru/traceability.md"
source_url: https://github.com/ciembor/agent-rules-books/blob/HEAD/_rule-workbench/refactoring-guru/traceability.md
---
# OBEY Refactoring.Guru

Canonical full source: [full.md](full.md)

## Compression decisions

- Initial compression under the current `PROCESS.md` on 2026-05-03 for `refactoring-guru`.
- The canonical source is `refactoring-guru/refactoring-guru.md`; `_rule-workbench/refactoring-guru/full.md` resolves to that source and was not edited as rule content during compression.
- This pass did not reveal a process bug. The current process already requires retaining book-thesis, decision-changing, conflict-resolver, trigger, refactoring-safety, boundary, local reasoning, validation, and anti-shortcut rules.
- `mini.md` preserves the source's distinctive bias: diagnose a smell, choose a catalog treatment, apply small behavior-preserving steps, verify, and stop.
- `nano.md` keeps the smallest always-on guardrails against common agent failures: cleanup without a smell, hidden behavior change, pattern overuse, speculative abstraction, unsafe deletion, and unbounded refactoring.
- The full technique catalog is compressed into treatment-selection, priority-map, technique-safety, and trigger rules. Individual technique names are not all repeated in `mini.md` or `nano.md`; their operational effects survive through grouped rules.

## Mini mapping

Decision rules:

- `M1` Separate refactoring from feature work and bug fixes. Source: `Primary Directive` (46-57), `Keep Refactoring Separate` (61-70), `Refactoring Workflow for Agents` (723-750).
- `M2` Diagnose smell, cost, scope, expected end state, verification, and stop condition before choosing a technique. Source: `Primary Directive` (46-57), `Smell Detection Process` (141-158), `Diagnose, Treat, Verify, Stop` (160-184), `Refactoring Workflow for Agents` (723-750).
- `M3` Prefer the smallest direct treatment and escalate only when blocked. Source: `Primary Directive` (46-57), `Diagnose, Treat, Verify, Stop` (160-184), `Smell-to-Treatment Priority Map` (497-523), `Safety and Tradeoff Rules` (708-719).
- `M4` Work in small named transformations and avoid broad redesign. Source: `Work in Small Steps` (72-79), `Technique Selection Rules` (411-493), `Technique Execution Safety` (631-704).
- `M5` Verify continuously after risky structural changes. Source: `Verify Continuously` (81-88), `Technique Playbook` (527-607), `Technique Execution Safety` (631-704), `Refactoring Workflow for Agents` (723-750).
- `M6` Stop when the diagnosed smell is materially reduced; do not chase unrelated smells. Source: `Diagnose, Treat, Verify, Stop` (160-184), `Decision Anti-Patterns` (611-627), `Refactoring Workflow for Agents` (723-750).
- `M7` Use the Rule of Three without abstracting coincidental similarity. Source: `Rule of Three` (99-106), `Duplicate Code` (325-333), `Decision Anti-Patterns` (611-627).
- `M8` Treat technical debt as compounding cost and pay down debt blocking current change, correctness, or understanding. Source: `Technical Debt Rules` (130-137), `When to Refactor` (99-126).
- `M9` Scan smells by category before selecting treatment. Source: `Smell Detection Process` (141-158), smell sections `Bloaters` through `Couplers` (199-407).
- `M10` For bloaters, prefer extraction, modeling, and responsibility splits before heavier object or hierarchy moves. Source: `Bloaters` (199-247), `Smell-to-Treatment Priority Map` (497-523), `Technique Playbook` (527-607).
- `M11` For switch/type-code smells, isolate decisions first and use polymorphism or state/strategy only for stable repeated variation. Source: `Switch Statements` (253-262), `Organizing Data` technique selection (436-452), `Conditional and Method Call Playbook` (572-595), `Decision Anti-Patterns` (611-627).
- `M12` For change preventers, move behavior and data toward the owner of the changing concept. Source: `Change Preventers` (290-312), `Moving Features Between Objects` (425-434), `Smell-to-Treatment Priority Map` (497-523).
- `M13` For dispensables, delete or inline unused structure only after compatibility and external reachability checks. Source: `Dispensables` (316-366), `Smell-to-Treatment Priority Map` (497-523), `Decision Anti-Patterns` (611-627).
- `M14` For couplers, reduce navigation and private knowledge while preserving useful boundary layers. Source: `Couplers` (370-407), `Moving Features Playbook` (543-552), `Safety and Tradeoff Rules` (708-719).
- `M15` Prefer names, extraction, variables, or assertions over comments that explain unclear code; keep rationale and constraints. Source: `Comments` (318-323), `Smell Exception Rules` (186-195), `Technique Selection Rules` (411-493).
- `M16` Keep behavior with the data it changes unless separation intentionally supports interchangeable behavior. Source: `Feature Envy` (372-378), `Moving Safety` (651-657), `Safety and Tradeoff Rules` (708-719).
- `M17` Treat encapsulation as behavior and invariant protection, not just getters and setters. Source: `Data Class` (342-348), `Encapsulation Safety` (659-665), `Decision Anti-Patterns` (611-627).
- `M18` Avoid speculative abstractions and mechanical wrappers, parameter objects, interfaces, superclasses, or variants. Source: `Speculative Generality` (359-366), `Decision Anti-Patterns` (611-627), `Safety and Tradeoff Rules` (708-719).
- `M19` Preserve public compatibility or transition paths for externally reachable structure. Source: `Technique Execution Safety` (631-704), `Safety and Tradeoff Rules` (708-719), `Refactoring Workflow for Agents` (723-750).
- `M20` Before extraction or movement, check inputs, outputs, mutation, callers, visibility, construction, and invariants. Source: `Technique Execution Safety` (631-657), `Technique Playbook` (527-607).
- `M21` Before condition consolidation or algorithm substitution, check side effects, ordering, truth tables, edge cases, and performance-sensitive behavior. Source: `Composing Methods Playbook` (531-541), `Conditional and Method Call Playbook` (572-595), `Conditional Safety` (667-674).
- `M22` Before data reorganization, decide identity, value/reference semantics, mutability, equality, lifecycle, association direction, and synchronization. Source: `Organizing Data` (436-452), `Organizing Data Playbook` (554-570), `Data Reorganization Safety` (686-694).
- `M23` Before generalization changes, prove shared behavior is real and preserve substitutability. Source: `Dealing With Generalization` (482-493), `Generalization Playbook` (597-607), `Generalization Safety` (696-704).
- `M24` Choose exceptions deliberately when mechanical smell treatment worsens clarity. Source: `Smell Exception Rules` (186-195), `Decision Anti-Patterns` (611-627), relevant smell `When to ignore` logic compressed throughout smell sections (199-407).

Trigger rules:

- `M25` Long method trigger: extract named methods and handle locals before using a method object. Source: `Long Method` (201-209), `Composing Methods Playbook` (531-541), `Extraction Safety` (633-641).
- `M26` Large class trigger: extract responsibility; subclass/interface only for stable variants or real client subsets. Source: `Large Class` (211-219), `Moving Features Playbook` (543-552), `Generalization Playbook` (597-607).
- `M27` Primitive/type-code trigger: model concepts only when names, validation, behavior, or safer variation handling survive. Source: `Primitive Obsession` (221-229), `Organizing Data Playbook` (554-570).
- `M28` Parameter list trigger: replace derived parameters, preserve whole objects, or introduce parameter objects only for real concepts. Source: `Long Parameter List` (231-237), `Data Clumps` (239-247), `Conditional and Method Call Playbook` (572-595).
- `M29` Shotgun/change-preventer trigger: centralize knowledge with movement or extraction. Source: `Change Preventers` (290-312), `Smell-to-Treatment Priority Map` (497-523).
- `M30` Message-chain/middle-man trigger: hide delegates, move behavior, or remove pass-through layers. Source: `Message Chains` (387-392), `Middle Man` (394-399), `Moving Features Playbook` (543-552).
- `M31` Query/modifier trigger: split mutation from returned information unless atomic read-modify is the contract. Source: `Simplifying Method Calls` (465-480), `Conditional and Method Call Playbook` (572-595), `Method Call Safety` (676-684).
- `M32` Conditional trigger: decompose or consolidate branches only after checking side effects and ordering. Source: `Simplifying Conditional Expressions` (454-463), `Conditional and Method Call Playbook` (572-595), `Conditional Safety` (667-674).
- `M33` Null/error/assertion/value/reference/association trigger: verify semantics before changing structure. Source: `Organizing Data Playbook` (554-570), `Conditional and Method Call Playbook` (572-595), `Data Reorganization Safety` (686-694).
- `M34` Inheritance trigger: push members down or replace inheritance with delegation when inheritance creates refused bequest or intimacy. Source: `Refused Bequest` (272-277), `Inappropriate Intimacy` (380-385), `Generalization Safety` (696-704).
- `M35` Dead/speculative/library trigger: check external reachability and use the narrowest library extension. Source: `Dead Code` (350-357), `Speculative Generality` (359-366), `Incomplete Library Class` (401-407).
- `M36` Cleanup-spread trigger: stop at the diagnosed smell and report the next smell separately. Source: `Diagnose, Treat, Verify, Stop` (160-184), `Decision Anti-Patterns` (611-627).

Final checklist:

- The checklist restates `M1`, `M2`, `M3`, `M5`, `M6`, `M18`, `M19`, and `M24` as a final scan rather than introducing new rules.

## Nano mapping

Decision rules:

- `N1` Separate refactoring from behavior change. Source: `Primary Directive` (46-57), `Keep Refactoring Separate` (61-70).
- `N2` Diagnose one smell, choose smallest treatment, verify, and stop. Source: `Primary Directive` (46-57), `Diagnose, Treat, Verify, Stop` (160-184), `Refactoring Workflow for Agents` (723-750).
- `N3` Prefer small named transformations over broad redesign. Source: `Work in Small Steps` (72-79), `Technique Selection Rules` (411-493).
- `N4` Run relevant checks after risky structure, state, API, or algorithm changes. Source: `Verify Continuously` (81-88), `Technique Execution Safety` (631-704).
- `N5` Do not chase new smells after the current smell is reduced. Source: `Diagnose, Treat, Verify, Stop` (160-184), `Decision Anti-Patterns` (611-627).
- `N6` Prefer local simplification before hierarchy, polymorphism, wrappers, or method objects. Source: `Smell-to-Treatment Priority Map` (497-523), `Safety and Tradeoff Rules` (708-719).
- `N7` Avoid speculative abstraction from coincidental similarity, random parameter bags, or simple conditionals. Source: `Smell Exception Rules` (186-195), `Decision Anti-Patterns` (611-627).
- `N8` Keep behavior with data unless separation is intentional. Source: `Feature Envy` (372-378), `Safety and Tradeoff Rules` (708-719).
- `N9` Preserve public compatibility around externally reachable structure. Source: `Dead Code` (350-357), `Safety and Tradeoff Rules` (708-719).
- `N10` Delete or inline dispensable code only after external reachability checks. Source: `Dispensables` (316-366), `Decision Anti-Patterns` (611-627).

Trigger rules:

- `N11` When a method needs comments or state reconstruction, extract only after checking inputs, outputs, and mutation. Source: `Long Method` (201-209), `Extraction Safety` (633-641).
- `N12` When a class changes for unrelated reasons, extract responsibility; use subtype/interface only for stable variants or client subsets. Source: `Large Class` (211-219), `Divergent Change` (292-297), `Generalization Safety` (696-704).
- `N13` When type conditionals repeat, isolate the decision before polymorphism; leave simple conditionals alone. Source: `Switch Statements` (253-262), `Conditional Safety` (667-674).
- `N14` When duplication appears the third time, refactor unless similarity is coincidental. Source: `Rule of Three` (99-106), `Duplicate Code` (325-333).
- `N15` When parameter or primitive clumps carry one concept, model it without creating oversized dependencies. Source: `Primitive Obsession` (221-229), `Long Parameter List` (231-237), `Data Clumps` (239-247).
- `N16` When clients navigate chains or internals, hide delegates or move behavior; remove pass-through middle men. Source: `Couplers` (370-407).
- `N17` When changing null/error/assertion/value/reference/association semantics, verify semantics before structure. Source: `Organizing Data Playbook` (554-570), `Conditional and Method Call Playbook` (572-595).

Final checklist:

- The checklist restates `N1`, `N2`, `N4`, `N5`, `N7`, and `N9` as a compact final scan.

## Section coverage review

- `Source and Scope` (3-20): intentionally lost as operational guidance; source provenance remains in this traceability file.
- `Purpose` (24-42): covered by `M1`, `M2`, `M8`, `N1`, and `N2`; clean-code feature list is merged into smell and final checklist rules.
- `Primary Directive` (46-57): covered by `M1`, `M2`, `M3`, `N1`, and `N2`.
- `Refactoring Process` (61-95): covered by `M1`, `M4`, `M5`, `M6`, `N1`, `N3`, `N4`, and `N5`.
- `When to Refactor` (99-126): covered by `M7`, `M8`, `M12`, `M36`, `N14`, and `N5`; review collaboration details are intentionally lost as standalone wording but preserved through checklist and stop-condition discipline.
- `Technical Debt Rules` (130-137): covered by `M8`; the detailed list of debt causes is merged into current-change cost and correctness/team-understanding priority.
- `Smell Detection Process` (141-195): covered by `M2`, `M3`, `M6`, `M9`, `M24`, `N2`, `N5`, and `N7`.
- `Bloaters` (199-247): covered by `M10`, `M25`, `M26`, `M27`, `M28`, `N11`, `N12`, and `N15`.
- `Object-Orientation Abusers` (251-286): covered by `M11`, `M27`, `M33`, `M34`, `N13`, and `N17`; alternative-class details are merged into treatment-priority and generalization rules.
- `Change Preventers` (290-312): covered by `M12`, `M29`, `N12`, and `N16`.
- `Dispensables` (316-366): covered by `M13`, `M15`, `M18`, `M35`, `N7`, `N9`, `N10`, and `N14`.
- `Couplers` (370-407): covered by `M14`, `M16`, `M30`, `M35`, `N8`, and `N16`.
- `Technique Selection Rules` (411-493): covered by `M3`, `M4`, `M10` through `M23`, `M25` through `M35`, `N3`, `N6`, and all nano triggers; individual technique names are intentionally merged into grouped operational rules.
- `Smell-to-Treatment Priority Map` (497-523): covered by `M3`, `M10` through `M14`, `M25` through `M35`, `N6`, and `N11` through `N17`.
- `Technique Playbook` (527-607): covered by `M20`, `M21`, `M22`, `M23`, `M25` through `M35`, `N11`, `N12`, `N13`, `N15`, `N16`, and `N17`; per-technique tutorial detail is intentionally lost while use/avoid/safe/verify consequences survive.
- `Decision Anti-Patterns` (611-627): covered by `M6`, `M18`, `M24`, `M36`, `N5`, and `N7`.
- `Technique Execution Safety` (631-704): covered by `M20`, `M21`, `M22`, `M23`, `M31`, `M32`, `M33`, `M34`, `N11`, `N13`, `N15`, and `N17`.
- `Safety and Tradeoff Rules` (708-719): covered by `M3`, `M14`, `M16`, `M18`, `M19`, `M22`, `M23`, `M24`, `N6`, `N7`, `N8`, and `N9`.
- `Refactoring Workflow for Agents` (723-750): covered by `M1`, `M2`, `M5`, `M6`, `M19`, `M36`, `N1`, `N2`, `N4`, and `N5`.
- `Review Checklist` (754-765): covered by the final checklists in `mini.md` and `nano.md`; checklist wording is merged rather than retained line-for-line.

## Intentional omissions

- The source URLs, crawl notes, and binding-policy prose are intentionally lost from compressed rule sets except through this traceability file.
- Individual technique tutorials and exact step sequences are merged into grouped safety and trigger rules; this is intentional because `mini.md` and `nano.md` are decision aids, not a full technique manual.
- Long smell catalogs are collapsed into category-level and hotspot trigger rules; omitted item names are covered by `M9` through `M35` rather than repeated.
- Review collaboration wording is intentionally lost as standalone prose because the operational effect survives in separation, verification, and checklist rules.
- No rule is omitted as `default`; where guidance sounds obvious to humans but agents commonly violate it, it is retained in compressed form.

---

**Source:** [`ciembor/agent-rules-books`](https://github.com/ciembor/agent-rules-books) → `_rule-workbench/refactoring-guru/traceability.md`
