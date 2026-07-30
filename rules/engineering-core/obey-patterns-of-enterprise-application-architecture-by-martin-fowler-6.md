---
name: obey-patterns-of-enterprise-application-architecture-by-martin-f
description: "Canonical full source: full.md"
category: engineering-core
source_repo: ciembor/agent-rules-books
source_path: "_rule-workbench/patterns-of-enterprise-application-architecture/traceability.md"
source_url: https://github.com/ciembor/agent-rules-books/blob/HEAD/_rule-workbench/patterns-of-enterprise-application-architecture/traceability.md
---
# OBEY Patterns of Enterprise Application Architecture by Martin Fowler

Canonical full source: [full.md](full.md)

## Compression decisions

- Re-run under `_rule-workbench/PROCESS.md` on 2026-05-02 for the 9th alphabetic book: `patterns-of-enterprise-application-architecture`.
- Diagnosis: book-specific rerun. The previous workbench compression and traceability referenced obsolete section names and line ranges that do not match the current 404-line full source. No reusable compression-process bug was found, so `PROCESS.md` was not changed.
- `mini.md` keeps the source's decision-changing enterprise pattern choices: responsibility placement, layering, business logic pattern selection, application workflow, persistence, object-relational behavior, transactions, presentation, integration, session state, distribution, generation order, and testing.
- `nano.md` keeps only always-on reminders that block common model shortcuts: framework/ORM-driven design, fake layering, generic repositories, hidden Unit of Work/lazy-load behavior, implicit transaction/session/concurrency ownership, business logic in boundary shapes, and local-looking remote APIs.
- No rule was omitted as `default`; omitted details are either merged into retained force-based rules or intentionally lost as catalog-level detail too situational for compressed context.

## Mini mapping

Decision rules:

- `M1` Make responsibility ownership explicit before naming patterns; one class or layer must not own presentation, workflow, domain, data source, transactions, concurrency, and integration. Source: `Purpose` (3-16), `Primary Directive` (20-34).
- `M2` Use layering by responsibility, with lower layers independent of presentation and no fake pass-through layers. Source: `Architectural Baseline` (38-57).
- `M3` Choose Transaction Script, Table Module, or Domain Model by business complexity, tabular shape, identity, lifecycle, and behavior needs. Source: `Choosing the Business Logic Pattern` (60-94).
- `M4` Keep each business logic pattern within its force: short scripts, honest table modules, and rich behavior in domain models; escalate when duplication, lifecycle, or invariant complexity grows. Source: `Choosing the Business Logic Pattern` (62-94), `Code Generation Rules` (310-320).
- `M5` Use Service Layer for application operations, orchestration, and transaction boundaries without absorbing all domain logic or exposing UI mechanics. Source: `Application Workflow Rules` (97-107), `Code Generation Rules` (301-308).
- `M6` Use Remote Facade and DTOs only at remote or layer/process boundaries, with coarse operations, batching, translation, and no domain behavior in DTOs. Source: `Application Workflow Rules` (108-129), `Distribution Rules` (285-295), `Code Generation Rules` (306-308).
- `M7` Choose Repository, Data Mapper, Row Data Gateway, Table Data Gateway, or Active Record by coupling and domain-separation pressure; repositories must speak domain terms and not become generic gateways. Source: `Persistence Pattern Rules` (132-162), `Code Generation Rules` (305, 310-320).
- `M8` Keep Identity Map, Unit of Work, and Lazy Load explicit so identity scope, logical commits, loading behavior, N+1 risk, hidden persistence, and ad hoc saves do not surprise callers. Source: `Identity, Caching, and Unit-of-Work Rules` (166-185).
- `M9` Choose object-relational mappings by identity, lifecycle, query need, schema shape, and evolution cost. Source: `Object-Relational Mapping Pattern Index` (189-202).
- `M10` Make concurrency and transaction policy explicit in the workflow: conflict detection, merge semantics, justified pessimism, short transactions, remote-call avoidance, and visible transaction ownership. Source: `Concurrency and Transaction Rules` (206-228), `Review Checklist` (382, 389).
- `M11` Use offline locks only when they preserve user-level consistency without hiding ownership, contention, or stale-lock diagnosis. Source: `Concurrency and Transaction Rules` (225-228).
- `M12` Keep presentation responsible for input, rendering, routing, formatting, pagination, UI state, and transport, not business rules. Source: `Presentation Layer Rules` (232-248), `Review Rules` (326-329).
- `M13` Keep external-system access behind boundaries, translate partner formats, and prevent integration messages, vendor DTOs, and serialization code from becoming domain design. Source: `Offline and Integration Rules` (252-262).
- `M14` Choose client, server, or database session state deliberately with security, scaling, cleanup, durability, sharing, and database-load costs explicit. Source: `Session State and Base Pattern Index` (266-270).
- `M15` Use base patterns only for concrete pressure: Gateway, Mapper, Layer Supertype, Separated Interface, Registry, Value Object, Money, Special Case, Plugin, Service Stub, and Record Set. Source: `Session State and Base Pattern Index` (271-281).
- `M16` Avoid distribution by default; when remote boundaries exist, make contracts coarse, separate them from local object design, and budget latency, serialization, versioning, and partial failure. Source: `Distribution Rules` (285-295).
- `M17` Generate code by first choosing the business logic pattern, then placing workflow, domain decisions, persistence, transactions, DTO/facade boundaries, and presentation concerns in their owning layers. Source: `Code Generation Rules` (299-320).
- `M18` Test behavior at the responsibility that owns it: domain, data-access infrastructure, service workflow, concurrency, and DTO/remote boundary mapping. Source: `Testing Rules` (367-373).

Trigger rules:

- `M19` Domain behavior in controllers, views, handlers, SQL scripts, triggers, DTOs, framework glue, serialization code, or vendor adapters triggers a responsibility move or explicit exception. Source: `Architectural Baseline` (52-56), `Presentation Layer Rules` (232-248), `Offline and Integration Rules` (252-262), `Review Rules` (326-337).
- `M20` One class or layer owning rendering, validation, SQL, transactions, domain rules, and external calls triggers a responsibility split. Source: `Primary Directive` (25-34), `Forbidden Patterns` (354-363).
- `M21` Transaction Script duplication, invariants, or lifecycle complexity triggers a Domain Model and persistence-pattern review. Source: `Choosing the Business Logic Pattern` (62-94), `Review Rules` (330-331).
- `M22` Table-shaped models in behavior-rich domains, generic CRUD repositories, or pass-through services trigger an ORM/database-ownership review. Source: `Persistence Pattern Rules` (134-162), `Forbidden Patterns` (346-352), `Review Checklist` (383, 386).
- `M23` Scattered SQL, mapping, transactions, locks, saves, or external resource access triggers the smallest centralizing repository, mapper, gateway, Unit of Work, service boundary, or policy. Source: `Persistence Pattern Rules` (132-162), `Identity, Caching, and Unit-of-Work Rules` (166-185), `Concurrency and Transaction Rules` (219-228), `Session State and Base Pattern Index` (271-272), `Review Rules` (332-334).
- `M24` Lazy-load surprises, duplicate identities, hidden auto-persistence, N+1 behavior, or ad hoc saves trigger explicit identity scope, Unit of Work, and loading behavior. Source: `Identity, Caching, and Unit-of-Work Rules` (168-185), `Review Rules` (334-335), `Review Checklist` (389).
- `M25` Concurrency conflicts, stale locks, user-level edits, or long-running workflows trigger explicit optimistic, pessimistic, coarse-grained, or implicit locking semantics. Source: `Concurrency and Transaction Rules` (206-228), `Forbidden Patterns` (360-363), `Testing Rules` (372).
- `M26` Chatty, object-shaped, or internals-leaking remote APIs trigger a coarse use-case contract with DTO translation. Source: `Application Workflow Rules` (108-129), `Distribution Rules` (285-295), `Review Rules` (336-337).
- `M27` Unclear session owner, lifetime, storage, security, scaling, failover, durability, or cleanup triggers an explicit session-state pattern choice. Source: `Session State and Base Pattern Index` (266-270).
- `M28` Layering theater, generic repository everywhere, ORM-driven everything, controller-centric enterprise workflow, distributed-object fantasy, or unclear transaction ownership blocks review until pattern ownership is corrected. Source: `Forbidden Patterns` (341-363).

Final checklist:

- The `mini.md` checklist restates `M1`-`M18` and trigger outcomes `M19`-`M28`; it adds no separate retained rule.

## Nano mapping

Decision rules:

- `N1` Keep presentation/transport, application workflow, domain, data source, transaction, concurrency, and integration responsibilities logically separate. Source: `Purpose` (3-16), `Primary Directive` (20-34), `Architectural Baseline` (38-57).
- `N2` Choose Transaction Script, Table Module, or Domain Model by actual complexity, tabular shape, identity, and lifecycle. Source: `Choosing the Business Logic Pattern` (60-94).
- `N3` Use Service Layer for use-case coordination and transaction orchestration without making it the default domain-behavior bucket. Source: `Application Workflow Rules` (97-107).
- `N4` Match Repository, Data Mapper, Gateway, or Active Record to persistence coupling pressure and avoid generic repositories or ORM-driven design. Source: `Persistence Pattern Rules` (132-162), `Forbidden Patterns` (346-352).
- `N5` Make Unit of Work, Identity Map, Lazy Load, transaction boundaries, and lock semantics visible before trusting ORM behavior. Source: `Identity, Caching, and Unit-of-Work Rules` (166-185), `Concurrency and Transaction Rules` (206-228).
- `N6` Keep presentation, DTOs, integration messages, vendor payloads, and serialization code free of business behavior. Source: `Application Workflow Rules` (119-129), `Presentation Layer Rules` (232-248), `Offline and Integration Rules` (252-262).
- `N7` Treat remote boundaries as expensive and failure-prone with coarse Remote Facade operations, DTO translation, versioning, and partial-failure handling. Source: `Application Workflow Rules` (108-129), `Distribution Rules` (285-295).
- `N8` Use session-state and base patterns only for concrete pressure; reject fake layers, generic repositories, ORM-driven design, controller-centric workflows, and distributed-object illusions. Source: `Session State and Base Pattern Index` (266-281), `Forbidden Patterns` (341-363).

Trigger rules:

- `N9` One class or layer owning UI, workflow, domain rules, SQL, transactions, and external calls triggers responsibility splitting. Source: `Primary Directive` (25-34), `Forbidden Patterns` (354-363).
- `N10` A simple Transaction Script growing duplication, invariants, or lifecycle decisions triggers domain logic and persistence pattern review. Source: `Choosing the Business Logic Pattern` (62-94), `Review Rules` (330-331).
- `N11` Table-shaped CRUD repositories, table-mirroring behavior-rich models, or pass-through services trigger ORM/database-design capture review. Source: `Persistence Pattern Rules` (132-162), `Forbidden Patterns` (346-352).
- `N12` Lazy loads, duplicate identities, hidden writes, N+1 behavior, ad hoc saves, or unclear locks trigger explicit identity scope, Unit of Work, loading, and concurrency semantics. Source: `Identity, Caching, and Unit-of-Work Rules` (166-185), `Concurrency and Transaction Rules` (206-228).
- `N13` Chatty, object-shaped, or internals-leaking remote APIs trigger coarse use-case boundary design with DTO translation. Source: `Application Workflow Rules` (108-129), `Distribution Rules` (285-295).

Final checklist:

- The `nano.md` checklist restates `N1`-`N8` and trigger outcomes `N9`-`N13`; it adds no separate retained rule.

## Section coverage review

- `Purpose` (3-16): covered by `M1` and `N1`; binding-policy wording is intentionally lost because the compressed files are themselves rule artifacts.
- `Primary Directive` (20-34): covered by `M1`, `M20`, `N1`, and `N9`.
- `Architectural Baseline` (38-57): covered by `M2`, `M19`, `M28`, `N1`, and `N8`.
- `Choosing the Business Logic Pattern` (60-94): covered by `M3`, `M4`, `M21`, `N2`, and `N10`.
- `Application Workflow Rules` (97-129): covered by `M5`, `M6`, `M17`, `M26`, `N3`, `N6`, `N7`, and `N13`.
- `Persistence Pattern Rules` (132-162): covered by `M7`, `M22`, `M23`, `N4`, and `N11`.
- `Identity, Caching, and Unit-of-Work Rules` (166-185): covered by `M8`, `M23`, `M24`, `N5`, and `N12`.
- `Object-Relational Mapping Pattern Index` (189-202): covered by `M9`; detailed mapping choices are intentionally lost from `nano.md` except identity/lifecycle pressure in `N5`.
- `Concurrency and Transaction Rules` (206-228): covered by `M10`, `M11`, `M23`, `M25`, `N5`, and `N12`.
- `Presentation Layer Rules` (232-248): covered by `M12`, `M19`, `N6`; detailed presentation pattern mechanics are collapsed into responsibility ownership.
- `Offline and Integration Rules` (252-262): covered by `M13`, `M19`, `N6`.
- `Session State and Base Pattern Index` (266-281): covered by `M14`, `M15`, `M27`, `N8`; individual base pattern mechanics are intentionally lost from `nano.md` except as concrete-pressure reminders.
- `Distribution Rules` (285-295): covered by `M16`, `M26`, `N7`, and `N13`.
- `Code Generation Rules` (299-320): covered by `M4`, `M5`, `M6`, `M7`, `M17`, `N2`, `N3`, `N4`, and `N6`; the exact default-choice wording is merged into pattern-selection rules.
- `Review Rules` (324-337): covered by triggers `M19`, `M21`, `M23`, `M24`, `M26`, `N10`, `N12`, and `N13`.
- `Forbidden Patterns` (341-363): covered by `M20`, `M22`, `M25`, `M28`, `N8`, `N9`, and `N11`.
- `Testing Rules` (367-373): covered by `M18`; intentionally lost from `nano.md` to keep fallback context focused on design failures.
- `Review Checklist` (377-391): covered by `mini.md` and `nano.md` final checklists plus `M10`, `M28`, `N5`, and `N8`.
- `Final Instruction` (395-404): covered by `M1`, `M7`, `M10`, `M16`, `N1`, `N4`, `N5`, and `N7`.

---

**Source:** [`ciembor/agent-rules-books`](https://github.com/ciembor/agent-rules-books) → `_rule-workbench/patterns-of-enterprise-application-architecture/traceability.md`
