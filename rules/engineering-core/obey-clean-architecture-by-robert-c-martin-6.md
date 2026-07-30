---
name: obey-clean-architecture-by-robert-c-martin
description: "Canonical full source: full.md"
category: engineering-core
source_repo: ciembor/agent-rules-books
source_path: "_rule-workbench/clean-architecture/traceability.md"
source_url: https://github.com/ciembor/agent-rules-books/blob/HEAD/_rule-workbench/clean-architecture/traceability.md
---
# OBEY Clean Architecture by Robert C. Martin

Canonical full source: [full.md](full.md)

## Compression decisions

- Re-run under `_rule-workbench/PROCESS.md` on 2026-05-02 for book position 2 in alphabetical workbench order: `clean-architecture`.
- Diagnosis: book-specific rerun, not a process bug. The current process already requires retaining decision-changing rules, conflict resolvers, micro-decisions, trigger rules, testing discipline, boundary ownership, and anti-shortcut guidance.
- `mini.md` keeps the current source's operational Clean Architecture bias: inward dependencies, independent business rules, replaceable details, use-case-first structure, policy-owned ports, humble adapters, enforceable boundaries, incremental refactoring, and detail-free policy tests.
- `nano.md` keeps only always-on reminders that block common model shortcuts: framework-first structure, database-shaped policy, direct volatile dependencies, layer bypass, generic service/utility dumping grounds, fake boundaries, and brittle policy tests.
- No rule is marked `default`; no source rule was removed on the claim that agents reliably follow it without prompting.
- Repeated examples of details, adapters, and forbidden patterns are merged when their operational consequence is the same: keep policy inward and detail translation outward.

## Mini mapping

Decision rules:

- `M1` Preserve independent business rules, inward dependencies, testability, and replaceable details even when the immediate feature would be shorter without them. Source: `Purpose` (3-17), `Architecture Economics and Priority` (257-264), `Final Instruction` (506-515).
- `M2` Source dependencies must point inward toward higher-level policy; core policy must not import volatile details. Source: `Non-Negotiable Rules` (21-24, 66-70), `Required Layer Responsibilities` (85-96, 106-115, 125-152), `Architecture Heuristics` (214-221), `Paradigm and Component Rules` (270-280), `Forbidden Patterns` (377-380), `Preferred Default Shapes` (487-490), `Final Instruction` (506-515).
- `M3` Put enterprise rules and invariants in entities or equivalent domain objects; put application-specific orchestration in focused use cases. Source: `Non-Negotiable Rules` (26-29, 56-64), `Required Layer Responsibilities` (76-115), `Architecture Heuristics` (223-230), `Output Expectations` (421-427), `Review Checklist` (448-453).
- `M4` Pass plain request and response models across use-case boundaries; do not pass framework, web, ORM, database, or response objects into or out of core policy. Source: `Non-Negotiable Rules` (26-44), `Application Layer` (98-115), `Code Generation Rules` (160-180), `Forbidden Patterns` (352-360), `Preferred Default Shapes` (480-485).
- `M5` Treat frameworks, databases, web delivery, messaging, filesystems, clocks, service clients, networks, devices, and vendors as outer-layer details behind ports, gateways, presenters, mappers, or adapters. Source: `Non-Negotiable Rules` (31-49), `Required Layer Responsibilities` (117-152), `Code Generation Rules` (182-208), `Architecture Heuristics` (232-241), `Services, Distribution, and Embedded Boundaries` (296-302), `Refactoring Rules` (396-405), `Output Expectations` (421-427).
- `M6` Inner layers own the interfaces they need; outer layers implement them; concrete wiring belongs in the composition root or outer-layer main component. Source: `Non-Negotiable Rules` (46-70), `Infrastructure Layer` (134-152), `Code Generation Rules` (182-203), `Preferred Default Shapes` (487-490).
- `M7` Keep adapters humble: translate external formats to use-case calls and back instead of owning business decisions. Source: `Non-Negotiable Rules` (41-44), `Interface Adapters Layer` (117-132), `Infrastructure Layer` (134-152), `Services, Distribution, and Embedded Boundaries` (296-302), `Forbidden Patterns` (362-375), `Output Expectations` (434-440).
- `M8` Organize by use case, feature, or business capability before generic technical buckets. Source: `Non-Negotiable Rules` (51-59), `Architecture Heuristics` (243-253), `Naming Rules` (306-313), `Output Expectations` (421-427), `Review Checklist` (457-459), `Preferred Default Shapes` (468-478).
- `M9` Choose boundaries by volatility, policy importance, substitution value, testability, and cost; use the lightest enforceable boundary, including partial boundaries, when full separation is too expensive. Source: `Code Generation Rules` (205-208), `Architecture Economics and Priority` (257-264), `Boundary Cost, Deployment, and Operations` (284-292), `When Tradeoffs Are Necessary` (494-502).
- `M10` Do not merge unrelated use cases or eliminate duplication when sharing would couple actors, change reasons, team ownership, deployment needs, or release pressure. Source: `Architecture Economics and Priority` (264), `Paradigm and Component Rules` (273-280), `Boundary Cost, Deployment, and Operations` (289-291), `Naming Rules` (306-313), `Forbidden Patterns` (367-385).
- `M11` Use structured code, dependency inversion, role-sized interfaces, substitutable implementations, controlled mutation, acyclic components, and stability-directed dependencies to protect policy from volatile details. Source: `Paradigm and Component Rules` (268-280), `Code Generation Rules` (200-203), `Forbidden Patterns` (377-385).
- `M12` Enforce boundaries with package structure, dependency rules, build constraints, tests, visibility, or narrow APIs. Source: `Code Generation Rules` (200-208), `Boundary Cost, Deployment, and Operations` (286-292), `Services, Distribution, and Embedded Boundaries` (298-302), `Forbidden Patterns` (372-385).
- `M13` Test entities, use cases, and boundary contracts first, without real volatile details; test adapters separately at the seams. Source: `Non-Negotiable Rules` (36-39), `Testing Rules` (317-344), `Services, Distribution, and Embedded Boundaries` (301-302), `Refactoring Rules` (410-411), `Review Checklist` (456).
- `M14` Preserve behavior while improving dependency direction; prefer incremental boundary extraction over rewrites and call out architectural debt when it cannot be fixed safely now. Source: `Refactoring Rules` (389-415), `Output Expectations` (429-440), `When Tradeoffs Are Necessary` (494-502).

Trigger rules:

- `M15` When urgent delivery would skip architecture, state the future change, test, replacement, or operational cost before accepting the shortcut. Source: `Architecture Economics and Priority` (257-264), `When Tradeoffs Are Necessary` (494-502), `Final Instruction` (506-515).
- `M16` When framework annotations, request/response objects, serializers, ORM rows, schemas, vendor SDKs, config, environment reads, device registers, or transport formats enter core policy, move translation outward. Source: `Non-Negotiable Rules` (26-49), `Required Layer Responsibilities` (85-152), `Code Generation Rules` (177-180), `Forbidden Patterns` (352-360), `Services, Distribution, and Embedded Boundaries` (301-302).
- `M17` When controllers, jobs, handlers, views, presenters, gateways, repositories, SQL, service listeners, scripts, or hardware adapters contain business branching or validation, move the rule inward. Source: `Non-Negotiable Rules` (56-64), `Interface Adapters Layer` (117-132), `Infrastructure Layer` (149-152), `Services, Distribution, and Embedded Boundaries` (298-302), `Forbidden Patterns` (357-370), `Refactoring Rules` (393-405).
- `M18` When a use case instantiates infrastructure, calls a volatile dependency directly, or depends on a concrete implementation, introduce a policy-owned port and wire the concrete detail at the edge. Source: `Code Generation Rules` (182-203), `Forbidden Patterns` (377-380), `Preferred Default Shapes` (487-490).
- `M19` When a `*Service`, utility folder, shared module, base package, or generic `core` package becomes an escape hatch, split by use case, role, or ownership and restore dependency direction. Source: `Non-Negotiable Rules` (51-59), `Code Generation Rules` (200-203), `Naming Rules` (306-313), `Forbidden Patterns` (367-385), `Refactoring Rules` (406-408).
- `M20` When an adapter bypasses a use case, a presenter reads persistence directly, or infrastructure is both imported by and importing inward code, restore the intended boundary. Source: `Interface Adapters Layer` (117-132), `Architecture Heuristics` (214-221), `Forbidden Patterns` (372-380), `Review Checklist` (448-460).
- `M21` When service boundaries, process boundaries, remote calls, deployment boundaries, or embedded hardware appear, still verify source dependencies, data ownership, I/O cost, and policy independence. Source: `Boundary Cost, Deployment, and Operations` (284-292), `Services, Distribution, and Embedded Boundaries` (296-302), `Final Instruction` (508-513).
- `M22` When tests need volatile details to verify business rules, move tests to use cases/entities with fakes or add a stable boundary contract. Source: `Testing Rules` (317-344), `Services, Distribution, and Embedded Boundaries` (301-302), `Refactoring Rules` (410-411), `Review Checklist` (456).
- `M23` When a compromise is unavoidable, keep it at the outermost layer possible, document the violation, avoid normalizing it, and preserve a path to separation. Source: `When Tradeoffs Are Necessary` (494-502), `Output Expectations` (429-432), `Final Instruction` (506-515).

Final checklist:

- The checklist restates `M1`, `M2`, `M3`, `M5`, `M6`, `M7`, `M8`, `M12`, and `M13` as a final scan rather than introducing independent rules.

## Nano mapping

Decision rules:

- `N1` Source dependencies point inward; domain and use cases must not import volatile details. Source: `Purpose` (3-17), `Non-Negotiable Rules` (21-24, 66-70), `Required Layer Responsibilities` (85-96, 106-115), `Forbidden Patterns` (377-380), `Final Instruction` (508-515).
- `N2` Entities guard enterprise invariants; focused use cases orchestrate application actions with plain input and output models. Source: `Non-Negotiable Rules` (26-29, 56-64), `Required Layer Responsibilities` (76-115), `Code Generation Rules` (160-180), `Preferred Default Shapes` (480-485).
- `N3` Volatile mechanisms sit behind policy-owned ports and outer-layer adapters. Source: `Non-Negotiable Rules` (31-49), `Code Generation Rules` (182-208), `Architecture Heuristics` (232-241), `Services, Distribution, and Embedded Boundaries` (296-302), `Preferred Default Shapes` (487-490).
- `N4` Controllers, presenters, gateways, service listeners, mappers, and hardware adapters translate; they do not own business rules. Source: `Interface Adapters Layer` (117-132), `Services, Distribution, and Embedded Boundaries` (298-302), `Forbidden Patterns` (362-375), `Refactoring Rules` (393-405).
- `N5` Organize by use case, feature, or business capability; avoid generic technical buckets, god services, shared utility escape hatches, and sideways coupling. Source: `Non-Negotiable Rules` (51-59), `Architecture Heuristics` (243-253), `Naming Rules` (306-313), `Forbidden Patterns` (367-385).
- `N6` Choose the lightest enforceable boundary that preserves likely change independence; a service, package, diagram, or folder name is not enough. Source: `Architecture Economics and Priority` (257-264), `Boundary Cost, Deployment, and Operations` (284-292), `Services, Distribution, and Embedded Boundaries` (298-302), `When Tradeoffs Are Necessary` (494-502).
- `N7` Test policy through entities, use cases, and boundary contracts without real volatile details. Source: `Testing Rules` (317-344), `Services, Distribution, and Embedded Boundaries` (301-302), `Review Checklist` (456).

Trigger rules:

- `N8` When framework, ORM, request, response, schema, transport, config, vendor, or hardware types enter core policy, move translation outward. Source: `Non-Negotiable Rules` (26-49), `Required Layer Responsibilities` (85-152), `Forbidden Patterns` (352-360), `Services, Distribution, and Embedded Boundaries` (301-302).
- `N9` When edge or service classes grow business rules, move policy inward and split by use case. Source: `Non-Negotiable Rules` (56-64), `Interface Adapters Layer` (117-132), `Forbidden Patterns` (362-370), `Refactoring Rules` (393-408).
- `N10` When core code constructs or calls volatile details directly, define an inward-owned port and wire the concrete implementation at the edge. Source: `Code Generation Rules` (182-203), `Forbidden Patterns` (377-380), `Preferred Default Shapes` (487-490).
- `N11` When a shortcut bypasses a use case, crosses layers, creates a cycle, or hides coupling in `common` or `utils`, restore dependency direction and ownership. Source: `Code Generation Rules` (200-208), `Architecture Heuristics` (214-221), `Paradigm and Component Rules` (278-280), `Forbidden Patterns` (372-385).
- `N12` When constraints force a compromise, keep it outermost, name the violation, and preserve a future path to separation. Source: `When Tradeoffs Are Necessary` (494-502), `Output Expectations` (429-432), `Final Instruction` (506-515).

Final checklist:

- The checklist restates `N1`, `N2`, `N3`, `N4`, `N5`, `N6`, and `N7` as a final scan rather than introducing independent rules.

## Section coverage review

- `Purpose` (3-17): covered by `M1`, `M2`, `N1`; binding keyword explanation is intentionally lost from compressed outputs because `full.md` remains the canonical policy source.
- `Non-Negotiable Rules` (19-72): covered by `M2`-`M8`, `M13`, `M16`, `M17`, `M19`, `N1`-`N5`, `N8`, and `N9`.
- `Required Layer Responsibilities` (74-154): covered by `M2`-`M7`, `M16`, `M17`, `N1`, `N2`, `N4`, and `N8`; exhaustive layer contents are merged into role rules.
- `Code Generation Rules` (156-210): covered by `M4`-`M6`, `M8`, `M12`, `M18`, `M19`, `N2`, `N3`, `N10`, and `N11`; detail lists for gateway-like dependencies are merged into volatile-detail rules.
- `Architecture Heuristics` (212-255): covered by `M2`, `M3`, `M5`, `M8`, `M20`, `N3`, `N5`, and `N11`; question lists are converted into operational checks and triggers.
- `Architecture Economics and Priority` (257-264): covered by `M1`, `M9`, `M10`, `M15`, and `N6`.
- `Paradigm and Component Rules` (268-280): covered by `M2`, `M10`, `M11`, `N11`; named principle labels are compressed into their operational consequences.
- `Boundary Cost, Deployment, and Operations` (284-292): covered by `M9`, `M10`, `M12`, `M21`, and `N6`.
- `Services, Distribution, and Embedded Boundaries` (296-302): covered by `M5`, `M7`, `M13`, `M21`, `M22`, `N3`, `N4`, `N6`, `N7`, and `N8`.
- `Naming Rules` (306-313): covered by `M8`, `M10`, `M19`, and `N5`; individual naming examples are merged into role/use-case naming pressure.
- `Testing Rules` (317-344): covered by `M13`, `M22`, and `N7`; adapter test examples are retained through seam-specific testing guidance.
- `Forbidden Patterns` (348-386): covered by `M2`, `M4`, `M7`, `M10`-`M12`, `M16`-`M20`, `N1`, `N4`, `N5`, and `N8`-`N11`; pattern lists are compressed into triggers.
- `Refactoring Rules` (389-417): covered by `M5`, `M7`, `M14`, `M17`, `M19`, `M22`, `N4`, and `N9`; ordered steps are merged into refactoring and trigger guidance.
- `Output Expectations` (419-442): covered by `M3`, `M5`, `M8`, `M14`, `M17`, `M23`, `N12`; implementation/review lists are compressed into decision rules and final checks.
- `Review Checklist` (444-462): covered by final checklists in `mini.md` and `nano.md`, with operational content also covered by `M2`, `M3`, `M5`-`M8`, `M12`, `M13`, and `M20`.
- `Preferred Default Shapes` (466-492): covered by `M4`, `M6`, `M8`, `M18`, `N2`, `N3`, and `N10`; directory-shape examples are intentionally compressed to avoid format-over-content guidance.
- `When Tradeoffs Are Necessary` (494-502): covered by `M9`, `M14`, `M15`, `M23`, `N6`, and `N12`.
- `Final Instruction` (506-515): covered by `M1`, `M2`, `M21`, `M23`, `N1`, `N6`, and `N12`.

## Omission notes

- No source section is wholly omitted.
- Exhaustive example lists are merged when they only enumerate details already covered by volatile-detail, adapter, boundary, or testing rules.
- Binding language (`MUST`, `SHOULD`, `MUST NOT`) is intentionally not repeated in compressed outputs because the compressed files are operational attachments, while `full.md` remains the binding source of truth.

---

**Source:** [`ciembor/agent-rules-books`](https://github.com/ciembor/agent-rules-books) → `_rule-workbench/clean-architecture/traceability.md`
