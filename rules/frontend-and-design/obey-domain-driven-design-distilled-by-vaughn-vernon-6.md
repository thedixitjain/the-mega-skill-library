---
name: obey-domain-driven-design-distilled-by-vaughn-vernon
description: "Canonical full source: full.md"
category: frontend-and-design
source_repo: ciembor/agent-rules-books
source_path: "_rule-workbench/domain-driven-design-distilled/traceability.md"
source_url: https://github.com/ciembor/agent-rules-books/blob/HEAD/_rule-workbench/domain-driven-design-distilled/traceability.md
---
# OBEY Domain-Driven Design Distilled by Vaughn Vernon

Canonical full source: [full.md](full.md)

## Compression decisions

- Re-run against the current canonical source on 2026-05-02.
- No source rule is labeled `default`; agent failures around fake DDD, framework-first design, unclear context ownership, primitive obsession, service-centric models, overgrown Aggregates, and integration leakage are common enough that even human-obvious rules were retained when operational.
- `mini.md` preserves the book's central bias: use a small effective DDD subset, start with strategic design and language, invest in the Core Domain, keep Bounded Contexts explicit, translate between contexts, use tactical patterns only where they protect meaning or invariants, and keep delivery practical.
- `nano.md` keeps only always-on rules that block the highest-risk shortcuts under tight context: DDD ceremony, missing context ownership, vague language, unbounded models, foreign-model leakage, anemic services, multi-root transactions, and hidden modeling debt.
- Detailed named context relationship mechanics, integration style mechanics, project planning advice, review lists, and testing lists are merged into decision and trigger rules where they change agent behavior.

## Mini mapping

Decision rules:

- `M1` Identify capability, subdomain class, Bounded Context, Ubiquitous Language, and earned tactical patterns before designing code. Source: `Purpose` (3-16), `Primary Directive` (20-35), `Adoption Fit and Modeling Investment` (38-45), `Code Generation Rules` (245-261), `Final Instruction` (308-317).
- `M2` Put the most modeling effort into the Core Domain and keep Supporting and Generic Subdomains simpler unless complexity proves otherwise. Source: `Purpose` (8-14), `Adoption Fit and Modeling Investment` (38-45), `Start with Subdomains` (50-60), `Practicality Rules` (219-230).
- `M3` Avoid full tactical DDD for simple CRUD, generic subsystems, or mainly technical problems; strengthen the model only when real complexity rises. Source: `Primary Directive` (20-35), `Adoption Fit and Modeling Investment` (38-45), `Practicality Rules` (219-230), `Review Rules` (264-278).
- `M4` Give every meaningful model one explicit Bounded Context that owns language, rules, semantics, code structure, tests, and integration contracts. Source: `Purpose` (8-14), `Primary Directive` (25-30), `Define Bounded Contexts Early` (61-66), `Use Context Mapping` (67-77), `Review Checklist` (291-304).
- `M5` Treat same words across contexts as different until translated; avoid shared domain classes and foreign language leakage. Source: `Define Bounded Contexts Early` (61-66), `Use Context Mapping` (67-77), `Ubiquitous Language Rules` (112-124).
- `M6` Choose context relationships deliberately and honor their ownership and translation implications. Source: `Use Context Mapping` (67-77), `Context Relationship Rules` (80-99), `Code Generation Rules` (245-261), `Review Rules` (264-278).
- `M7` Select integration style from business coupling, latency, failure semantics, resource shape, messaging lag, duplicate handling, and ordering limits. Source: `Context Relationship Rules` (80-99), `Integration Style Rules` (101-109).
- `M8` Keep integration contracts separate from internal models and test translations across boundaries. Source: `Use Context Mapping` (67-77), `Integration Style Rules` (101-109), `Architecture and Infrastructure Rules` (191-202), `Testing Rules` (281-288).
- `M9` Use local domain terms consistently in code, tests, Commands, Domain Events, APIs, and conversations, and rename code when understanding improves. Source: `Purpose` (8-14), `Ubiquitous Language Rules` (112-124), `Collaboration Rules` (205-216), `Testing Rules` (281-288).
- `M10` Use Entities for explicit identity and lifecycle, and protect meaningful state transitions instead of exposing unrestricted setters. Source: `Entities` (129-136), `Review Rules` (264-278), `Testing Rules` (281-288).
- `M11` Use immutable, self-validating Value Objects when primitives hide domain meaning. Source: `Value Objects` (137-144), `Collaboration Rules` (205-216), `Review Rules` (264-278), `Testing Rules` (281-288).
- `M12` Use Aggregates only as invariant and transactional consistency boundaries; keep them small, root-protected, identity-referenced, and usually one Aggregate per transaction. Source: `Aggregates` (145-153), `Aggregate Minimalism Rules` (162-174), `Review Checklist` (291-304).
- `M13` Use Domain Events for meaningful past-tense business facts that clarify collaboration or integration, not noisy field changes. Source: `Domain Events` (154-160), `Integration Style Rules` (101-109), `Review Checklist` (291-304).
- `M14` Keep Application Services in orchestration: load Aggregates, invoke domain behavior, save, and trigger integration work without owning business decisions. Source: `Application Service Rules` (177-188), `Code Generation Rules` (245-261), `Review Rules` (264-278), `Review Checklist` (291-304).
- `M15` Keep frameworks, persistence, REST representations, transport formats, and infrastructure types out of the domain model. Source: `Architecture and Infrastructure Rules` (191-202), `Integration Style Rules` (101-109), `Code Generation Rules` (245-261).
- `M16` Write code that teaches the model by making assumptions explicit and exposing richer concepts instead of flags, status codes, booleans, enums, helpers, or utilities carrying domain meaning. Source: `Ubiquitous Language Rules` (112-124), `Collaboration Rules` (205-216), `Review Rules` (264-278).
- `M17` Use Event Storming, scenarios, acceptance tests, modeling spikes, and domain-expert walkthroughs when workflow, terminology, policies, or criteria are unclear; timebox modeling and track modeling debt. Source: `Adoption Fit and Modeling Investment` (38-45), `Accelerated Modeling and Project Rules` (233-242), `Testing Rules` (281-288).
- `M18` Estimate and plan DDD work from modeling uncertainty, integration risk, implementation cost, team skill, and expert access. Source: `Accelerated Modeling and Project Rules` (233-242).

Trigger rules:

- `M19` Fuzzy, generic, overloaded, or imported language triggers Ubiquitous Language refinement before more code. Source: `Primary Directive` (25-30), `Ubiquitous Language Rules` (112-124), `Collaboration Rules` (205-216).
- `M20` Core drift, code-language mismatch, or supporting complexity hiding the core triggers subdomain and boundary review. Source: `Adoption Fit and Modeling Investment` (38-45), `Start with Subdomains` (50-60), `Practicality Rules` (219-230).
- `M21` One model spreading across separate business concerns triggers splitting or translation instead of shared domain classes. Source: `Use Context Mapping` (67-77), `Context Relationship Rules` (80-99), `Review Rules` (264-278).
- `M22` Upstream model, schema, UI, framework, API payload, transport object, or database pressure triggers boundary translation. Source: `Use Context Mapping` (67-77), `Integration Style Rules` (101-109), `Architecture and Infrastructure Rules` (191-202).
- `M23` Shared Kernel requires small stable overlap, joint ownership, and tests. Source: `Context Relationship Rules` (80-99).
- `M24` A claimed Anticorruption Layer requires real translation. Source: `Context Relationship Rules` (80-99).
- `M25` Multi-root transactions, large graph loading, or graph mutation triggers Aggregate boundary and consistency timing review. Source: `Aggregates` (145-153), `Aggregate Minimalism Rules` (162-174).
- `M26` Controllers, helpers, services, or transport-shaped application services containing business decisions trigger moving behavior into the model or naming the missing concept. Source: `Application Service Rules` (177-188), `Collaboration Rules` (205-216), `Review Rules` (264-278).
- `M27` Vague, command-like, trivial, or field-change Domain Events trigger redesign as specific business facts or removal. Source: `Domain Events` (154-160), `Review Rules` (264-278).
- `M28` Primitives, flags, status codes, enums, or booleans carrying domain rules trigger richer concepts or Value Objects. Source: `Value Objects` (137-144), `Collaboration Rules` (205-216), `Review Rules` (264-278).
- `M29` Delivery pressure that would skip design triggers a short modeling spike, scenario, acceptance test, or explicit modeling debt. Source: `Adoption Fit and Modeling Investment` (38-45), `Accelerated Modeling and Project Rules` (233-242), `Practicality Rules` (219-230).

Final checklist:

- The checklist restates `M1`-`M17` and `M19`-`M29` as a final scan rather than introducing new rules.

## Nano mapping

Decision rules:

- `N1` Start from capability, subdomain type, Bounded Context, and local Ubiquitous Language before tactical patterns. Source: `Primary Directive` (20-35), `Code Generation Rules` (245-261).
- `N2` Invest most design effort in the Core Domain and keep Supporting, Generic, CRUD, and mainly technical areas simpler. Source: `Adoption Fit and Modeling Investment` (38-45), `Start with Subdomains` (50-60), `Practicality Rules` (219-230).
- `N3` Put every meaningful model inside one explicit Bounded Context that owns language, rules, semantics, code, tests, and integration contracts. Source: `Define Bounded Contexts Early` (61-66), `Use Context Mapping` (67-77).
- `N4` Translate between contexts when meanings differ; do not share domain classes or divergent terms. Source: `Define Bounded Contexts Early` (61-66), `Use Context Mapping` (67-77), `Ubiquitous Language Rules` (112-124).
- `N5` Choose context relationships and integration mechanisms deliberately, including Conformist or Anticorruption Layer when foreign meaning is involved. Source: `Context Relationship Rules` (80-99), `Integration Style Rules` (101-109).
- `N6` Keep integration contracts separate from internal models and do not expose Aggregate internals through REST or transport payloads. Source: `Integration Style Rules` (101-109), `Architecture and Infrastructure Rules` (191-202).
- `N7` Use Entities for identity, Value Objects for validated meaning, Aggregates for small invariant boundaries, and Domain Events for meaningful past-tense facts. Source: `Tactical Pattern Rules` (127-160), `Aggregate Minimalism Rules` (162-174).
- `N8` Modify one Aggregate per transaction by default; reference other Aggregates by identity and use eventual consistency when the business allows it. Source: `Aggregates` (145-153), `Aggregate Minimalism Rules` (162-174), `Integration Style Rules` (101-109).
- `N9` Keep business decisions in the domain model and Application Services in coordination. Source: `Application Service Rules` (177-188), `Review Rules` (264-278).
- `N10` Keep frameworks, persistence, transport, and external schemas out of the domain model. Source: `Architecture and Infrastructure Rules` (191-202).
- `N11` Use scenarios, acceptance tests, Event Storming, spikes, and domain-expert walkthroughs to learn quickly without hiding modeling debt. Source: `Adoption Fit and Modeling Investment` (38-45), `Accelerated Modeling and Project Rules` (233-242), `Testing Rules` (281-288).

Trigger rules:

- `N12` Fuzzy or overloaded language triggers term sharpening before code. Source: `Ubiquitous Language Rules` (112-124), `Collaboration Rules` (205-216).
- `N13` One model absorbing unrelated concerns triggers subdomain or context boundary review. Source: `Use Context Mapping` (67-77), `Review Rules` (264-278).
- `N14` Foreign models, schemas, APIs, or frameworks driving domain shape trigger boundary translation. Source: `Integration Style Rules` (101-109), `Architecture and Infrastructure Rules` (191-202).
- `N15` Multi-root transactions or large graph mutation trigger Aggregate boundary and consistency timing review. Source: `Aggregate Minimalism Rules` (162-174).
- `N16` Services, controllers, setters, flags, or primitives carrying business decisions trigger exposing the missing domain concept. Source: `Entities` (129-136), `Value Objects` (137-144), `Application Service Rules` (177-188), `Collaboration Rules` (205-216).
- `N17` Vague, command-like, or noisy events trigger redesign as specific business facts. Source: `Domain Events` (154-160).

Final checklist:

- The checklist restates `N1`, `N3`, `N4`, `N7`, `N11`, and `N15` as a final scan rather than introducing new rules.

## Section coverage review

- `Purpose` (3-16): covered by `M1`, `M2`, `M9`; binding-policy wording is intentionally lost because compressed files are operational attachments, not legal policy.
- `Primary Directive` (20-35): covered by `M1`, `M3`, `M19`, `N1`; both extremes are covered by `M3` and `N2`.
- `Adoption Fit and Modeling Investment` (38-45): covered by `M1`, `M2`, `M3`, `M17`, `M18`, `M20`, `M29`, `N2`, `N11`.
- `Strategic Rules / Start with Subdomains` (48-60): covered by `M2`, `M20`, `N2`.
- `Strategic Rules / Define Bounded Contexts Early` (61-66): covered by `M4`, `M5`, `N3`, `N4`.
- `Strategic Rules / Use Context Mapping` (67-77): covered by `M4`, `M5`, `M6`, `M8`, `M21`, `M22`, `N3`, `N4`, `N13`.
- `Context Relationship Rules` (80-99): covered by `M6`, `M7`, `M21`, `M23`, `M24`, `N5`; individual pattern definitions are merged into deliberate relationship selection except Shared Kernel and Anticorruption Layer safeguards retained as triggers.
- `Integration Style Rules` (101-109): covered by `M7`, `M8`, `M13`, `M22`, `N5`, `N6`, `N8`, `N14`; domain-event payload choice is merged into integration-coupling guidance.
- `Ubiquitous Language Rules` (112-124): covered by `M5`, `M9`, `M16`, `M19`, `N4`, `N12`.
- `Tactical Pattern Rules / Entities` (129-136): covered by `M10`, `N7`, `N16`.
- `Tactical Pattern Rules / Value Objects` (137-144): covered by `M11`, `M28`, `N7`, `N16`.
- `Tactical Pattern Rules / Aggregates` (145-153): covered by `M12`, `M25`, `N7`, `N8`.
- `Tactical Pattern Rules / Domain Events` (154-160): covered by `M13`, `M27`, `N7`, `N17`.
- `Aggregate Minimalism Rules` (162-174): covered by `M12`, `M25`, `N7`, `N8`, `N15`.
- `Application Service Rules` (177-188): covered by `M14`, `M26`, `N9`, `N16`.
- `Architecture and Infrastructure Rules` (191-202): covered by `M8`, `M15`, `M22`, `N6`, `N10`, `N14`.
- `Collaboration Rules` (205-216): covered by `M9`, `M16`, `M19`, `M26`, `M28`, `N12`, `N16`.
- `Practicality Rules` (219-230): covered by `M2`, `M3`, `M20`, `M29`, `N2`; over-modeling and dismissing DDD are merged into selective-investment rules.
- `Accelerated Modeling and Project Rules` (233-242): covered by `M17`, `M18`, `M29`, `N11`; detailed estimation and team-constraint mechanics are retained in `M18` and collapsed in `nano.md`.
- `Code Generation Rules` (245-261): covered by `M1`, `M6`, `M8`, `M9`, `M14`, `M15`, `N1`; default avoidance list is covered by `M3`, `M4`, `M9`, `M14`, and `M15`.
- `Review Rules` (264-278): covered by `M3`, `M6`, `M10`, `M11`, `M14`, `M16`, `M21`, `M26`, `M27`, `M28`, `N9`, `N13`; long review list is collapsed into triggers and checklist.
- `Testing Rules` (281-288): covered by `M8`, `M9`, `M10`, `M11`, `M17`, `N11`; service-orchestration testing is covered by `M14`.
- `Review Checklist` (291-304): covered by `M1`, `M3`, `M4`, `M9`, `M11`, `M12`, `M14`, `M15`, and the mini/nano final checklists.
- `Final Instruction` (308-317): covered by `M1`, `M3`, `M4`, `M9`, `M15`, `N1`, and `N2`.

---

**Source:** [`ciembor/agent-rules-books`](https://github.com/ciembor/agent-rules-books) → `_rule-workbench/domain-driven-design-distilled/traceability.md`
