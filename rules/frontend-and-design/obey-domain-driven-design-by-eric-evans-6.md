---
name: obey-domain-driven-design-by-eric-evans
description: "Canonical full source: full.md"
category: frontend-and-design
source_repo: ciembor/agent-rules-books
source_path: "_rule-workbench/domain-driven-design/traceability.md"
source_url: https://github.com/ciembor/agent-rules-books/blob/HEAD/_rule-workbench/domain-driven-design/traceability.md
---
# OBEY Domain-Driven Design by Eric Evans

Canonical full source: [full.md](full.md)

## Compression decisions

- Re-run against the current canonical source on 2026-05-02 for book position 6 in `_rule-workbench` alphabetical order.
- The alphabetical book list resolves position 6 to `domain-driven-design`.
- `full.md` was treated as source of truth and was not edited.
- No rule is labeled `default`; generic-seeming DDD rules were retained when they block common agent failures such as fake DDD terminology, passive domain models, framework-first design, persistence-shaped models, primitive obsession, and missing invariant or boundary tests.
- The previous workbench traceability referenced an older source shape and stale line ranges, so `mini.md`, `nano.md`, and this mapping were regenerated from the current 979-line `full.md`.
- This was a book-specific rerun caused by stale artifacts, not a process bug. `PROCESS.md` already requires section-by-section coverage and current line references.
- Detailed pattern catalogs are merged into operational rules when the same agent decision survives; catalog names are intentionally lost where preserving the name would not change decisions under context pressure.

## Mini mapping

Decision rules:

- `M1` Use a model only when it organizes domain knowledge, clarifies communication, and can be expressed in implementation; iterate through code, expert conversation, scenarios, and refactoring toward deeper insight. Source: `Purpose` (3-17), `Primary Directive` (19-34), `What DDD Means in This Repository` (36-56), `Knowledge Crunching and Deep Models` (58-79), `Model-Driven Design` (81-101), `Breakthrough and Deeper Insight` (103-121), `Scenario Walkthroughs` (187-204).
- `M2` Maintain one Ubiquitous Language per Bounded Context across names, tests, documents, diagrams, planning, and feature discussion; keep explanatory models separate from the implementation model. Source: `Purpose` (3-17), `Model-Driven Design` (81-101), `Ubiquitous Language` (144-164), `Communication Artifacts` (167-184), `Testing Rules` (806-833), `Review Checklist` (943-968).
- `M3` Put business logic in the domain layer. Keep UI, application coordination, infrastructure, persistence, messaging, and framework constraints outside the model or behind adapters. Source: `Primary Directive` (19-34), `What DDD Means in This Repository` (36-56), `Layered Architecture and Smart UI` (207-220), `Application Layer` (593-615), `Infrastructure` (617-630), `Forbidden Patterns` (836-885), `Final Instruction` (970-979).
- `M4` Use tactical patterns for model meaning: Entities for stable identity, Value Objects for immutable descriptive value, Services for important operations with no natural object home, and Modules for conceptual cohesion. Source: `Entities` (386-411), `Value Objects` (414-440), `Associations and Modules` (443-467), `Domain Services` (496-517), `Code Generation Rules` (708-757), `Review Rules` (759-804), `Review Checklist` (943-968).
- `M5` Manage lifecycle through Aggregates, Factories, and Repositories: expose only Aggregate roots, enforce invariants inside the boundary, hide complex creation and persistence, and prevent partially formed objects from escaping. Source: `Purpose` (3-17), `Aggregates` (470-493), `Repositories` (542-569), `Factories` (572-592), `Code Generation Rules` (708-757), `Forbidden Patterns` (836-885), `Review Checklist` (943-968).
- `M6` Design domain objects for the model first and persistence second; preserve identity, Aggregate boundaries, Value Object semantics, and domain query criteria instead of exposing database structure. Source: `Primary Directive` (19-34), `Entities` (386-411), `Value Objects` (414-440), `Aggregates` (470-493), `Repositories` (542-569), `Infrastructure` (617-630), `Code Generation Rules` (708-757), `Final Instruction` (970-979).
- `M7` Refactor toward deeper domain insight, not only mechanical cleanliness. Make constraints, policies, processes, calculations, allocations, and generation rules explicit when they carry domain meaning. Source: `Knowledge Crunching and Deep Models` (58-79), `Breakthrough and Deeper Insight` (103-121), `Making Implicit Concepts Explicit` (124-140), `Explicit Concepts and Specifications` (520-539), `Supple Design` (653-678), `Refactoring Rules` (887-905), `Output Expectations` (908-941).
- `M8` Design for model users: name operations by domain purpose, separate side-effect-free functions from state-changing commands, make assertions explicit, and shape boundaries around conceptual contours. Source: `Ubiquitous Language` (144-164), `Entities` (386-411), `Explicit Concepts and Specifications` (520-539), `Supple Design` (653-678), `Forbidden Patterns` (836-885), `Review Checklist` (943-968).
- `M9` Define every Bounded Context explicitly. Do not assume a term has the same meaning elsewhere; use context maps, tests, and active communication to protect model integrity. Source: `Purpose` (3-17), `Bounded Contexts` (223-242), `Strategic Design` (245-266), `Model Integrity Patterns` (269-302), `Translation at Boundaries` (633-650), `Testing Rules` (806-833), `Review Checklist` (943-968).
- `M10` Choose context relationships deliberately: Shared Kernel, Customer/Supplier, Conformist, Anticorruption Layer, Separate Ways, Open Host Service, Published Language, or incremental legacy replacement. Source: `Strategic Design` (245-266), `Model Integrity Patterns` (269-302), `Translation at Boundaries` (633-650), `Code Generation Rules` (708-757), `Forbidden Patterns` (836-885), `Output Expectations` (908-941).
- `M11` Distill and protect the Core Domain by strategic value. Keep generic subdomains, infrastructure, reusable mechanisms, and supporting details from consuming core-domain attention. Source: `What DDD Means in This Repository` (36-56), `Strategic Design` (245-266), `Distillation` (305-331), `Strategic Decision Making` (363-383), `Code Generation Rules` (708-757), `Review Rules` (759-804), `Output Expectations` (908-941).
- `M12` Add large-scale structure only when individual objects no longer make a large model understandable; keep structures domain-specific, evolvable, and valid only inside compatible contexts. Source: `Large-Scale Structure` (334-360), `Strategic Decision Making` (363-383), `Review Rules` (759-804), `Review Checklist` (943-968).
- `M13` Use analysis patterns, design patterns, specifications, industry formalisms, and prior art only when they clarify the current model and preserve domain language. Source: `Making Implicit Concepts Explicit` (124-140), `Explicit Concepts and Specifications` (520-539), `Supple Design` (653-678), `Analysis and Model Patterns` (681-705).
- `M14` Test the model in the Ubiquitous Language: prioritize domain tests for invariants, allowed and forbidden transitions, valid construction, specifications, application orchestration, and boundary translation before generic infrastructure checks. Source: `Communication Artifacts` (167-184), `Scenario Walkthroughs` (187-204), `Testing Rules` (806-833), `Review Checklist` (943-968).
- `M15` Make major strategic moves with people who understand both the implementation and the domain; architecture and framework guidance must serve application teams and domain goals. Source: `Model-Driven Design` (81-101), `Strategic Decision Making` (363-383), `Review Rules` (759-804), `Output Expectations` (908-941).

Trigger rules:

- `M16` Awkward, ambiguous, inconsistent, or repeatedly translated terminology triggers Ubiquitous Language refinement and code renaming. Source: `Knowledge Crunching and Deep Models` (58-79), `Making Implicit Concepts Explicit` (124-140), `Ubiquitous Language` (144-164), `Review Rules` (759-804), `Refactoring Rules` (887-905).
- `M17` Controllers, services, scripts, SQL, jobs, or serializers carrying business decisions trigger moving rules into domain objects, domain services, specifications, or explicit domain concepts. Source: `Model-Driven Design` (81-101), `Layered Architecture and Smart UI` (207-220), `Domain Services` (496-517), `Explicit Concepts and Specifications` (520-539), `Application Layer` (593-615), `Review Rules` (759-804), `Forbidden Patterns` (836-885), `Refactoring Rules` (887-905).
- `M18` UI, persistence, messaging, APIs, or frameworks shaping domain concepts triggers layers, adapters, translation, or an Anticorruption Layer. Source: `Primary Directive` (19-34), `Layered Architecture and Smart UI` (207-220), `Repositories` (542-569), `Infrastructure` (617-630), `Translation at Boundaries` (633-650), `Forbidden Patterns` (836-885), `Final Instruction` (970-979).
- `M19` A change crossing unrelated modules, many objects, or multiple roots triggers Module cohesion, Aggregate ownership, consistency timing, and context-boundary review. Source: `Associations and Modules` (443-467), `Aggregates` (470-493), `Application Layer` (593-615), `Review Rules` (759-804), `Refactoring Rules` (887-905).
- `M20` Client knowledge of creation, lifecycle, persistence, identity generation, or internal mutation details triggers repairs to Factories, Repositories, roots, and encapsulation. Source: `Entities` (386-411), `Aggregates` (470-493), `Repositories` (542-569), `Factories` (572-592), `Forbidden Patterns` (836-885).
- `M21` Behavior that is hard to explain, test, or extend triggers search for a deeper model, missing implicit concept, or breakthrough refactoring instead of adding procedural branches. Source: `Knowledge Crunching and Deep Models` (58-79), `Breakthrough and Deeper Insight` (103-121), `Making Implicit Concepts Explicit` (124-140), `Scenario Walkthroughs` (187-204), `Explicit Concepts and Specifications` (520-539), `Refactoring Rules` (887-905).
- `M22` Cross-model integration triggers explicit relationship, translation strategy, published language or protocol, and boundary tests before boundary code. Source: `Bounded Contexts` (223-242), `Strategic Design` (245-266), `Model Integrity Patterns` (269-302), `Translation at Boundaries` (633-650), `Testing Rules` (806-833), `Forbidden Patterns` (836-885).
- `M23` When changing invariants, lifecycle transitions, specifications, orchestration, or context translation, add domain-language tests that prove valid behavior and block invalid states. Source: `Scenario Walkthroughs` (187-204), `Aggregates` (470-493), `Explicit Concepts and Specifications` (520-539), `Application Layer` (593-615), `Testing Rules` (806-833).
- `M24` Generic mechanisms, reusable frameworks, or supporting subdomains obscuring distinctive value trigger Core Domain distillation or mechanism separation. Source: `Strategic Design` (245-266), `Distillation` (305-331), `Large-Scale Structure` (334-360), `Strategic Decision Making` (363-383), `Forbidden Patterns` (836-885).

Final checklist:

- The checklist restates `M2`, `M3`, `M4`, `M5`, `M9`, `M10`, `M11`, `M14`, and `M15` as a final scan rather than introducing new rules.

## Nano mapping

Decision rules:

- `N1` Keep model, code, tests, documents, and team language aligned inside each Bounded Context. Source: `Purpose` (3-17), `Model-Driven Design` (81-101), `Ubiquitous Language` (144-164), `Communication Artifacts` (167-184), `Bounded Contexts` (223-242), `Testing Rules` (806-833).
- `N2` Make business behavior explicit in model code, not hidden in controllers, persistence, jobs, scripts, or framework glue. Source: `What DDD Means in This Repository` (36-56), `Layered Architecture and Smart UI` (207-220), `Application Layer` (593-615), `Forbidden Patterns` (836-885).
- `N3` Refine Ubiquitous Language when terms are fuzzy, and use only models that solve the problem and can be implemented. Source: `Primary Directive` (19-34), `Knowledge Crunching and Deep Models` (58-79), `Model-Driven Design` (81-101), `Making Implicit Concepts Explicit` (124-140), `Ubiquitous Language` (144-164).
- `N4` Use tactical patterns for domain meaning: Entities for identity, Value Objects for value, Services for homeless operations, and Modules for conceptual cohesion. Source: `Entities` (386-411), `Value Objects` (414-440), `Associations and Modules` (443-467), `Domain Services` (496-517).
- `N5` Treat Aggregates as consistency and lifecycle boundaries; expose roots only and protect invariants inside the boundary. Source: `Aggregates` (470-493), `Review Checklist` (943-968), `Final Instruction` (970-979).
- `N6` Hide complex creation and persistence behind Factories and Repositories; design for the model first and storage second. Source: `Repositories` (542-569), `Factories` (572-592), `Infrastructure` (617-630), `Forbidden Patterns` (836-885).
- `N7` Define context boundaries and relationships explicitly before sharing terms, data, or behavior across systems. Source: `Bounded Contexts` (223-242), `Strategic Design` (245-266), `Model Integrity Patterns` (269-302), `Translation at Boundaries` (633-650).
- `N8` Protect the Core Domain from generic subdomains, reusable mechanisms, infrastructure, framework pressure, and foreign models. Source: `What DDD Means in This Repository` (36-56), `Strategic Design` (245-266), `Distillation` (305-331), `Forbidden Patterns` (836-885), `Final Instruction` (970-979).
- `N9` Refactor toward deeper insight: make important constraints, policies, processes, and calculations explicit domain concepts. Source: `Knowledge Crunching and Deep Models` (58-79), `Breakthrough and Deeper Insight` (103-121), `Making Implicit Concepts Explicit` (124-140), `Explicit Concepts and Specifications` (520-539), `Refactoring Rules` (887-905).
- `N10` Test invariants, invalid construction, lifecycle transitions, and boundary translations in the Ubiquitous Language. Source: `Scenario Walkthroughs` (187-204), `Testing Rules` (806-833), `Review Checklist` (943-968).

Trigger rules:

- `N11` Fuzzy or inconsistent terms trigger language refinement and code renaming. Source: `Knowledge Crunching and Deep Models` (58-79), `Making Implicit Concepts Explicit` (124-140), `Ubiquitous Language` (144-164), `Review Rules` (759-804).
- `N12` Procedural business rules in orchestration, SQL, jobs, or serializers trigger moving behavior into the model. Source: `Model-Driven Design` (81-101), `Layered Architecture and Smart UI` (207-220), `Application Layer` (593-615), `Forbidden Patterns` (836-885).
- `N13` Sprawling transactions or cross-module changes trigger Aggregate and context-boundary review. Source: `Associations and Modules` (443-467), `Aggregates` (470-493), `Review Rules` (759-804), `Refactoring Rules` (887-905).
- `N14` Foreign model, schema, API, or legacy pressure triggers translation or an explicit Conformist choice. Source: `Bounded Contexts` (223-242), `Model Integrity Patterns` (269-302), `Translation at Boundaries` (633-650), `Forbidden Patterns` (836-885).
- `N15` Supporting mechanisms obscuring distinctive value trigger Core Domain distillation. Source: `Strategic Design` (245-266), `Distillation` (305-331), `Forbidden Patterns` (836-885).

Final checklist:

- The checklist restates `N1`, `N2`, `N5`, `N7`, `N8`, and `N10` as a final scan rather than introducing new rules.

## Section coverage review

- `Purpose` (3-17): covered by `M1`, `M2`, `M5`, `M9`, `N1`; policy-binding wording is intentionally lost from compressed files because the compressed files are attachments, not the canonical policy.
- `Primary Directive` (19-34): covered by `M1`, `M3`, `M6`, `M18`, `N3`, `Final Instruction` coverage through `N5` and `N8`; the detailed list of discouraged optimizations is merged into framework, persistence, CRUD, and generic-reuse trigger rules.
- `What DDD Means in This Repository` (36-56): covered by `M1`, `M3`, `M11`, `N2`, and `N8`; individual fake-DDD examples are merged into anti-fake-DDD and pattern-use rules.
- `Knowledge Crunching and Deep Models` (58-79): covered by `M1`, `M7`, `M16`, `M21`, `N3`, `N9`, and `N11`.
- `Model-Driven Design` (81-101): covered by `M1`, `M2`, `M3`, `M15`, `M17`, `N1`, `N3`, and `N12`; separate analysis-vs-coding wording is merged into model-code alignment and strategic governance.
- `Breakthrough and Deeper Insight` (103-121): covered by `M1`, `M7`, `M21`, `N9`; migration-cost detail is preserved as safe incremental refactoring, not as a standalone rule.
- `Making Implicit Concepts Explicit` (124-140): covered by `M7`, `M13`, `M16`, `M21`, `N3`, `N9`, and `N11`.
- `Ubiquitous Language` (144-164): covered by `M2`, `M8`, `M16`, `N1`, `N3`, and `N11`; shipping-specific example names are intentionally lost.
- `Communication Artifacts` (167-184): covered by `M2`, `M14`, `N1`; document length and diagram-inventory details are merged into language-alignment and living-documentation rules.
- `Scenario Walkthroughs` (187-204): covered by `M1`, `M14`, `M21`, `M23`, `N10`; premature performance tuning is merged into model-first decision rules.
- `Layered Architecture and Smart UI` (207-220): covered by `M3`, `M17`, `N2`, `N12`; Smart UI is intentionally retained only as the tradeoff that simple domains may not need rich modeling.
- `Bounded Contexts` (223-242): covered by `M9`, `M22`, `N1`, `N7`, and `N14`.
- `Strategic Design` (245-266): covered by `M9`, `M10`, `M11`, `M22`, `M24`, `N7`, `N8`, and `N15`.
- `Model Integrity Patterns` (269-302): covered by `M9`, `M10`, `M22`, `N7`, and `N14`; individual relationship mechanics are merged into deliberate context-relationship choice.
- `Distillation` (305-331): covered by `M11`, `M24`, `N8`, and `N15`; individual distillation pattern names are intentionally lost unless their operational effect survives through Core Domain protection.
- `Large-Scale Structure` (334-360): covered by `M12`, `M24`; `Evolving Order`, `System Metaphor`, `Responsibility Layers`, `Knowledge Level`, and `Pluggable Component Framework` are intentionally lost from `nano.md` and merged into the large-scale-structure rule in `mini.md`.
- `Strategic Decision Making` (363-383): covered by `M11`, `M12`, `M15`, `M24`; team ownership and revisability survive, while detailed process phrasing is intentionally lost.
- `Entities` (386-411): covered by `M4`, `M6`, `M8`, `M20`, `N4`; public-setter and passive-entity prohibitions are merged into behavior-rich tactical modeling.
- `Value Objects` (414-440): covered by `M4`, `M6`, `N4`; primitive and validation details are retained through value semantics and valid-construction rules.
- `Associations and Modules` (443-467): covered by `M4`, `M19`, `N4`, `N13`; detailed association navigation mechanics are merged into aggregate and module-boundary review.
- `Aggregates` (470-493): covered by `M5`, `M6`, `M19`, `M20`, `M23`, `N5`, and `N13`.
- `Domain Services` (496-517): covered by `M4`, `M17`, `N4`; god-service warnings are merged into behavior-placement trigger rules.
- `Explicit Concepts and Specifications` (520-539): covered by `M7`, `M8`, `M13`, `M17`, `M21`, `M23`, `N9`; query-builder implementation detail is intentionally lost from `nano.md` but retained in `mini.md` as model-vs-persistence separation.
- `Repositories` (542-569): covered by `M5`, `M6`, `M18`, `M20`, `N6`; detailed method-shape guidance is merged into intent-bearing repository contracts.
- `Factories` (572-592): covered by `M5`, `M20`, `N6`; trivial-constructor guidance is merged into "hide complex creation" rather than kept as a separate rule.
- `Application Layer` (593-615): covered by `M3`, `M17`, `M19`, `M23`, `N2`, and `N12`.
- `Infrastructure` (617-630): covered by `M3`, `M6`, `M18`, `N6`; specific ORM/lazy-loading examples are merged into persistence-ignorance and model-first rules.
- `Translation at Boundaries` (633-650): covered by `M9`, `M10`, `M18`, `M22`, `N7`, and `N14`.
- `Supple Design` (653-678): covered by `M7`, `M8`, `M13`, `N9`; closure, declarative design, subsumption, and DSL detail are intentionally lost from `nano.md`.
- `Analysis and Model Patterns` (681-705): covered by `M13`; detailed Strategy, Composite, exploration-team, and public-API naming guidance is intentionally lost from `nano.md`.
- `Code Generation Rules` (708-757): covered by `M4`, `M5`, `M6`, `M7`, `M9`, `M10`, and `M11`; ordered-codegen wording is intentionally lost while the operational sequence survives.
- `Review Rules` (759-804): covered by `M4`, `M11`, `M12`, `M15`, `M16`, `M17`, `M19`, `M22`, `N11`, `N13`; the long review list is collapsed into triggers and final checklist.
- `Testing Rules` (806-833): covered by `M2`, `M9`, `M14`, `M22`, `M23`, `N1`, and `N10`; infrastructure-test separation is intentionally lost from `nano.md`.
- `Forbidden Patterns` (836-885): covered by `M3`, `M5`, `M8`, `M10`, `M11`, `M17`, `M18`, `M20`, `M22`, `M24`, `N2`, `N6`, `N8`, `N12`, `N14`, and `N15`.
- `Refactoring Rules` (887-905): covered by `M7`, `M16`, `M17`, `M19`, `M21`, `N9`, `N11`, and `N13`; do-not-rewrite-everything-at-once is merged into safe-step breakthrough/refactoring rules.
- `Output Expectations` (908-941): covered by `M7`, `M10`, `M11`, `M15`; implementation/review/modify output lists are collapsed into decision rules and final checklist.
- `Review Checklist` (943-968): covered by `M2`, `M4`, `M5`, `M8`, `M9`, `M11`, `M12`, `M14`, `N5`, `N10`; collapsed into the final checklists.
- `Final Instruction` (970-979): covered by `M3`, `M6`, `N3`, `N5`, `N8`; generic-vs-clear-domain rule survives as primary bias and model-first decisions.

---

**Source:** [`ciembor/agent-rules-books`](https://github.com/ciembor/agent-rules-books) → `_rule-workbench/domain-driven-design/traceability.md`
