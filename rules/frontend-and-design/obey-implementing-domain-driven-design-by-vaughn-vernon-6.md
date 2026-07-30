---
name: obey-implementing-domain-driven-design-by-vaughn-vernon
description: "Canonical full source: full.md"
category: frontend-and-design
source_repo: ciembor/agent-rules-books
source_path: "_rule-workbench/implementing-domain-driven-design/traceability.md"
source_url: https://github.com/ciembor/agent-rules-books/blob/HEAD/_rule-workbench/implementing-domain-driven-design/traceability.md
---
# OBEY Implementing Domain-Driven Design by Vaughn Vernon

Canonical full source: [full.md](full.md)

## Compression decisions

- Re-run under the current `PROCESS.md` on 2026-05-02 for the 8th alphabetic book, `implementing-domain-driven-design`.
- This was a book-specific re-run, not a `PROCESS.md` bug. The process already requires source-faithful compression, current line ranges, section-by-section coverage, and explicit dispositions for merged or omitted material.
- No retained rule is labeled `default`; the source uses even generic-looking guidance to block common DDD failures: global models, fake Ubiquitous Language, ORM-shaped Aggregates, shared domain packages, generic Repositories, anemic Application Services, and unbounded cross-context coupling.
- `mini.md` keeps every rule that changes architecture, modeling, integration, persistence, testing, review, or repeated local implementation decisions.
- `nano.md` keeps only always-on guardrails for the highest-risk shortcuts under tight context: missing Bounded Context, language drift, shared model types, Aggregate sprawl, anemic services, Repository leakage, and client or foreign model pressure.
- Detailed code-generation, review, testing, and checklist lists are merged into operational rules, trigger rules, and final checklist items rather than repeated verbatim.

## Mini mapping

Decision rules:

- `M1` Name the Bounded Context before interpreting model artifacts and reject a global company model. Source: `Purpose` (3-17), `Primary Directive` (21-33), `Bounded Context Is Mandatory` (39-44), `Code Generation Rules` (261-270), `Final Instruction` (328-337).
- `M2` Use one local Ubiquitous Language consistently across implementation artifacts and rename when understanding improves. Source: `Purpose` (8-15), `Primary Directive` (25-33), `Ubiquitous Language Rules` (64-75), `Code Generation Rules` (261-264), `Review Checklist` (312-324), `Final Instruction` (330-337).
- `M3` Protect the Core Domain, spend rich modeling only where complexity warrants it, keep supporting or CRUD areas simpler, and avoid DDD ceremony. Source: `Core Domain Protection` (51-55), `Practical Simplicity Rule` (245-255).
- `M4` Make context interactions explicit through visible relationships, translation responsibility, and upstream/downstream influence. Source: `Context Mapping Is a Design Artifact` (45-50), `Context Integration Rules` (212-230).
- `M5` Translate foreign, legacy, partner, external, and infrastructure models into local language and keep them out of local domain objects. Source: `Primary Directive` (25-33), `Context Mapping Is a Design Artifact` (45-50), `Context Integration Rules` (214-230), `Client Representation and Scope Discipline` (236-241).
- `M6` Treat Aggregates as small immediate consistency boundaries with one root, root-mediated invariant changes, hidden mutable internals, and intention-revealing behavior. Source: `Aggregate Rules of Thumb` (78-90), anti-patterns (102-106), `Code Generation Rules` (264-267), `Review Rules` (284-294).
- `M7` Reference other Aggregates by identity, avoid graph loading, and default to one Aggregate per transaction with eventual coordination outside the boundary. Source: `Primary Directive` (25-33), `Reference Other Aggregates by Identity` (92-96), `One Aggregate per Transaction by Default` (97-100), aggregate anti-patterns (102-106), `Domain Event Rules` (161-165), `Final Instruction` (330-337).
- `M8` Use Entities for identity, lifecycle, meaningful state transitions, and behavior rather than passive ORM containers. Source: `Entities` (112-117).
- `M9` Use immutable Value Objects for meaningful descriptive concepts, validate on construction, compare by value, and avoid primitive obsession for domain values. Source: `Value Objects` (118-123), required behavior (124-126).
- `M10` Use Domain or Transformation Services only for domain-significant operations or transformations that fit no model object, and keep technical mapping outside the domain. Source: `Domain and Transformation Service Rules` (130-139).
- `M11` Provide Repositories for Aggregate Roots with domain-oriented access contracts, not table CRUD, ORM rows, or business-rule implementations. Source: `Repository Rules` (143-155).
- `M12` Publish Domain Events only for meaningful completed business facts, use past-tense names, keep payloads model-local, and avoid property-change or command-like events. Source: `Domain Event Rules` (159-166), event anti-patterns (174-178), `Review Rules` (284-294), `Review Checklist` (312-324).
- `M13` Use Event Sourcing only when event streams are the right persistence model, with Aggregate identity, versioning, deterministic replay, and evolution support. Source: `Event Sourcing` (167-172).
- `M14` Keep Application Services as use-case coordinators that load Aggregates, invoke domain behavior, persist, publish events, and own transaction or integration coordination without holding core decision logic. Source: `Application Service Rules` (182-193).
- `M15` Organize modules by Bounded Context first and by domain or use-case ownership inside the context; avoid giant shared or common domain packages. Source: `Module and Package Rules` (197-208), strategic anti-patterns (56-60).
- `M16` Use DTOs, projections, use-case queries, rendition adapters, mediators, command/query separation, and explicit scope identifiers when client needs differ from Aggregate shape. Source: `Client Representation and Scope Discipline` (234-241).
- `M17` Follow the source code-generation order from context to language, tactical type, Aggregate boundary, identity references, invariants, repositories, Application Services, and translation layers. Source: `Code Generation Rules` (259-278).
- `M18` Test domain behavior and boundaries directly, including Aggregate invariants, transitions, Value Objects, events, repositories, translation layers, and Application Service orchestration. Source: `Testing Rules` (298-306).

Trigger rules:

- `M19` Ambiguous, reused, or technical-placeholder terms trigger qualification, splitting, or renaming before more code is written. Source: `Ubiquitous Language Rules` (66-75), `Review Rules` (284-294).
- `M20` Direct imports of another context's domain package, shared cross-context enums, or database coupling trigger explicit translation instead. Source: strategic anti-patterns (56-60), `Context Integration Rules` (222-230), `Review Checklist` (312-324).
- `M21` Legacy, vendor, partner, API, transport, persistence, UI, or foreign-context shapes in local code trigger an Anticorruption Layer or mapping boundary. Source: `Context Mapping Is a Design Artifact` (45-50), `Domain and Transformation Service Rules` (134-139), `Context Integration Rules` (214-230), `Client Representation and Scope Discipline` (234-241).
- `M22` Aggregate boundary changes or multi-Aggregate transactions trigger immediate-invariant proof; otherwise coordinate by identity, Domain Events, policies, processes, or Application Services. Source: `Aggregate Rules of Thumb` (80-100), `Domain Event Rules` (161-165), `Application Service Rules` (184-188).
- `M23` External mutation of Aggregate internals or read-decide-write behavior outside the root triggers movement behind intention-revealing root behavior. Source: `Aggregate Root Discipline` (86-90), aggregate anti-patterns (102-106), `Review Rules` (284-294).
- `M24` Generic CRUD, table-shaped, ORM-row-returning, or rule-owning Repository APIs trigger reshaping around Aggregate access. Source: `Repository Rules` (143-155), `Code Generation Rules` (272-278), `Review Rules` (284-294).
- `M25` Command-like events, property-change events, or events carrying framework request objects or persistence artifacts trigger renaming, narrowing, or removal. Source: `Domain Event Rules` (159-166), event anti-patterns (174-178), `Review Rules` (284-294), `Review Checklist` (312-324).
- `M26` Application Services or controllers accumulating branching business rules trigger moving decisions back into the domain model. Source: `Application Service Rules` (182-193).
- `M27` Client rendering, query speed, or representation pressure triggers DTOs, projections, use-case queries, or adapters instead of exposing or reshaping Aggregates. Source: `Client Representation and Scope Discipline` (234-241), `Practical Simplicity Rule` (245-255).
- `M28` Simple CRUD subdomains trigger simpler patterns, while real invariants and lifecycle complexity trigger honest modeling. Source: `Practical Simplicity Rule` (245-255).

Final checklist:

- The checklist restates `M1`-`M16`, `M20`, `M22`, `M24`-`M27` as a final scan rather than introducing new rules. Source: `Review Checklist` (310-324), `Final Instruction` (328-337).

## Nano mapping

Decision rules:

- `N1` Name the Bounded Context and local Ubiquitous Language before interpreting model artifacts. Source: `Purpose` (8-15), `Primary Directive` (25-33), `Bounded Context Is Mandatory` (39-44), `Ubiquitous Language Rules` (64-75).
- `N2` Translate across contexts and foreign systems instead of sharing local Aggregates, Entities, enums, or domain objects as contracts. Source: `Context Mapping Is a Design Artifact` (45-50), strategic anti-patterns (56-60), `Context Integration Rules` (212-230).
- `N3` Treat Aggregates as small immediate consistency boundaries with one root, hidden mutable internals, identity references, and eventual consistency outside one boundary by default. Source: `Aggregate Rules of Thumb` (78-100), aggregate anti-patterns (102-106), `Final Instruction` (330-337).
- `N4` Use Entities for identity and lifecycle, Value Objects for immutable validated descriptive values, and Domain Services only when no model object owns the operation. Source: `Entity and Value Object Rules` (110-126), `Domain and Transformation Service Rules` (130-139).
- `N5` Keep Repositories focused on Aggregate Roots and Application Services focused on coordination rather than domain decisions. Source: `Repository Rules` (143-155), `Application Service Rules` (182-193).
- `N6` Publish Domain Events as meaningful completed past-tense facts and use Event Sourcing only when event history is the right persistence model. Source: `Domain Event Rules` (159-166), `Event Sourcing` (167-172), event anti-patterns (174-178).
- `N7` Use client representations, projections, queries, adapters, and explicit scope identifiers instead of exposing or reshaping domain internals. Source: `Client Representation and Scope Discipline` (234-241).

Trigger rules:

- `N8` Ambiguous, generic, or reused terms trigger splitting or qualification by Bounded Context. Source: `Ubiquitous Language Rules` (66-75), `Review Rules` (284-294).
- `N9` Multi-root transactions or graph traversal across Aggregate roots trigger immediate-invariant proof and identity/event/policy/process/application coordination. Source: `Aggregate Rules of Thumb` (92-100), aggregate anti-patterns (102-106), `Final Instruction` (330-337).
- `N10` Foreign models, database shape, framework objects, transport payloads, UI needs, or another context's model leaking into domain code trigger boundary translation. Source: `Domain and Transformation Service Rules` (134-139), `Context Integration Rules` (212-230), `Client Representation and Scope Discipline` (234-241).
- `N11` DDD vocabulary around CRUD services, generic repositories, mutable graphs, or anemic models triggers invariant and behavior proof or simplification. Source: `Primary Directive` (23-33), `Repository Rules` (151-155), `Practical Simplicity Rule` (245-255), `Final Instruction` (330-337).
- `N12` DDD review triggers checks for context, language, Aggregate boundary, translation, Repository shape, events-as-facts, and Application Service thinness. Source: `Review Rules` (282-294), `Review Checklist` (310-324).

Final checklist:

- The checklist restates `N1`-`N7`, `N9`, `N10`, and `N12` as a final scan rather than introducing new rules.

## Section coverage review

- `Purpose` (3-17): covered by `M1`, `M2`, `N1`; binding policy wording is merged into the compressed rule tone.
- `Primary Directive` (21-33): covered by `M1`, `M2`, `M5`, `M7`, `M17`, `N1`, and `N11`; ordering details are preserved through `M17`.
- `Strategic Design Rules` (37-60): covered by `M1`, `M3`, `M4`, `M5`, `M15`, `M20`, `M21`, `N1`, `N2`; anti-patterns are merged into context and translation triggers.
- `Ubiquitous Language Rules` (64-75): covered by `M2`, `M19`, `N1`, and `N8`; no language rule is intentionally lost.
- `Aggregate Rules of Thumb` (78-106): covered by `M6`, `M7`, `M22`, `M23`, `N3`, and `N9`; object-graph and transaction anti-patterns are merged into triggers.
- `Entity and Value Object Rules` (110-126): covered by `M8`, `M9`, and `N4`; no entity or value-object rule is intentionally lost.
- `Domain and Transformation Service Rules` (130-139): covered by `M10`, `M21`, `M26`, `N4`, and `N10`; technical mapping details are merged into boundary triggers.
- `Repository Rules` (143-155): covered by `M11`, `M24`, `N5`, and `N11`; repository anti-patterns are merged into the Repository trigger.
- `Domain Event Rules` (159-178): covered by `M12`, `M13`, `M22`, `M25`, `N6`; event anti-patterns are merged into event trigger rules.
- `Application Service Rules` (182-193): covered by `M14`, `M22`, `M26`, `N5`, and `N12`; controller duplication is merged into `M26`.
- `Module and Package Rules` (197-208): covered by `M1`, `M2`, `M15`; example package names are intentionally lost as examples, while their operational effect survives in `M15`.
- `Context Integration Rules` (212-230): covered by `M4`, `M5`, `M20`, `M21`, `N2`, and `N10`; identity and contract details are merged into translation and contract-separation rules.
- `Client Representation and Scope Discipline` (234-241): covered by `M5`, `M16`, `M21`, `M27`, `N7`, and `N10`; individual representation options are merged into `M16` and `N7`.
- `Practical Simplicity Rule` (245-255): covered by `M3`, `M27`, `M28`, and `N11`; over-modeling and under-modeling anti-patterns are preserved as a trigger.
- `Code Generation Rules` (259-278): covered by `M17`, `M24`, `N1`, `N2`, `N3`, and `N5`; avoid-by-default bullets are merged into the matching decision and trigger rules.
- `Review Rules` (282-294): covered by `M19`, `M20`, `M22`-`M25`, `N8`, `N9`, and `N12`; the list is collapsed into targeted review triggers.
- `Testing Rules` (298-306): covered by `M18`; testing detail is intentionally absent from `nano.md` because `nano.md` is reserved for always-on design guardrails.
- `Review Checklist` (310-324): covered by `M1`, `M2`, `M4`, `M6`, `M7`, `M11`, `M12`, `M14`, `M20`, `M22`, `M24`, `M25`, `N1`-`N3`, `N5`, `N6`, and `N12`; checklist bullets are merged into final scans.
- `Final Instruction` (328-337): covered by `M1`, `M2`, `M5`, `M7`, `M22`, `M28`, `N1`, `N2`, `N3`, `N9`, and `N11`; no final-instruction rule is intentionally lost.

---

**Source:** [`ciembor/agent-rules-books`](https://github.com/ciembor/agent-rules-books) → `_rule-workbench/implementing-domain-driven-design/traceability.md`
