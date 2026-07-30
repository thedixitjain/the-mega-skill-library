---
name: obey-release-it-by-michael-t-nygard
description: "Canonical full source: full.md"
category: general-purpose
source_repo: ciembor/agent-rules-books
source_path: "_rule-workbench/release-it/traceability.md"
source_url: https://github.com/ciembor/agent-rules-books/blob/HEAD/_rule-workbench/release-it/traceability.md
---
# OBEY Release It! by Michael T. Nygard

Canonical full source: [full.md](full.md)

## Compression decisions

- Re-run against the current 382-line canonical source on 2026-05-02.
- This is a `book-specific miss` correction: the previous workbench traceability referenced stale section names and ranges from a broader source, while current `full.md` contains the narrower Release It! policy shown here.
- No rule is labeled `default`; timeout, retry, overload, validation, observability, startup, deployment, and operational-control rules are common agent failure points under implementation pressure.
- `mini.md` keeps the book's production-survivability thesis, dependency protection, overload control, resource discipline, boundary validation, observability, startup/deployment safety, interconnect/API/cache/job failure behavior, security, and controlled resilience practice.
- `nano.md` keeps only always-on reminders that prevent the highest-risk shortcuts: happy-path design, unbounded waits or resources, unsafe retries, failure cascades, unvalidated bad data, opaque production state, unsafe release automation, and uncontrolled traffic or experiments.
- Detailed enumerations of resource types, metric names, anti-pattern examples, review bullets, and test cases are merged into operational rules, triggers, and final checklist items unless their exact wording changes an agent decision.

## Mini mapping

Decision rules:

- `M1` Assume dependencies, queues, caches, timeouts, callers, and degraded states can fail slowly, partially, or for hours. Source: `Purpose` (3-18), `Stability Mindset Rules` (36-45).
- `M2` Prefer visible failure, blast-radius limits, load shedding, core-service preservation, and diagnosability over coupled happy-path design. Source: `Primary Directive` (21-32), `Final Instruction` (373-382).
- `M3` Treat deployment, operations, security, observability, rollback, state visibility, and configuration validation as part of production readiness. Source: `Purpose` (8-17), `Production Readiness and Release Risk Rules` (49-55).
- `M4` Put explicit, intentional time limits on outbound calls and waits; forbid infinite waits where finite response matters. Source: `Dependency Protection Rules / Timeouts Are Mandatory` (59-66), `Code Generation Rules` (323-340), `Review Checklist` (355-360).
- `M5` Retry only when safe, bounded, backed off or jittered, and not used for validation or permanent failures. Source: `Dependency Protection Rules / Retries Must Be Disciplined` (67-72), `Forbidden Patterns / Retry Storms` (302-305), `Scheduled and Background Work Rules` (270-276), `Review Checklist` (355-360).
- `M6` Isolate dependency and workload failures with breakers, fast failure, bulkheads, separate pools, and slow-work isolation. Source: `Dependency Protection Rules / Circuit Breakers and Fast Failure` (73-77), `Dependency Protection Rules / Bulkheads and Isolation` (78-88), `Forbidden Patterns / Blast-Radius Amplification` (317-320), `Review Checklist` (355-367).
- `M7` Design overload behavior with back pressure, finite queues, demand limits, critical capacity reservation, and load shedding. Source: `Load and Capacity Rules` (91-126), `Forbidden Patterns / Collapse by Queue` (307-310), `Review Checklist` (355-367).
- `M8` Choose stability patterns by failure mode: steady state, fail fast, let-it-crash only with supervision and isolation, handshaking, monitored decoupling middleware, and governors. Source: `Load and Capacity Rules / Additional Stability Patterns` (114-120).
- `M9` Make runtime state, external responses, automation progress, migrations, operational assumptions, and boundary data visible and validated, with rollback or roll-forward for partial changes. Source: `Runtime State and Restart Safety Rules` (129-148), `Deployment and Startup Rules` (224-230).
- `M10` Budget and release scarce resources, avoid holding locks or expensive connections across slow remote calls, and stream or paginate large payloads. Source: `Resource Management Rules` (151-169).
- `M11` Validate external input and responses before trusting them, and prevent malformed data from poisoning caches, queues, or downstream systems. Source: `Runtime State and Restart Safety Rules` (131-135), `Data Boundary Rules` (172-179).
- `M12` Build observability into boundaries and failure points with structured logs, correlation, metrics, health, dependency, version, configuration, runtime, saturation, queue, retry, and breaker signals. Source: `Operational Visibility Rules` (182-211), `Review Rules` (280-293), `Review Checklist` (355-367).
- `M13` Make startup, health checks, migrations, one-time jobs, administrative controls, process code, and delivery tooling safe, authorized, auditable, observable, stoppable, and recoverable. Source: `Incidents, Capacity, and Runtime Control` (214-220), `Deployment and Startup Rules` (224-230), `Code Generation Rules` (323-340), `Testing Rules` (344-351).
- `M14` Make interconnects, routing, API contracts, caches, scheduled work, and background work production-aware by avoiding concentrated demand, hidden SPOFs, uncontrolled fan-out, fragile chattiness, cache dogpiles, stale data surprises, and synchronized retries. Source: `Interconnect, Routing, Security, and Chaos Rules` (234-242), `API and Contract Rules` (246-252), `Cache Rules` (256-266), `Scheduled and Background Work Rules` (270-276).
- `M15` Include security and hostile traffic in production readiness, and run production tests, game days, chaos, or disaster simulations only with limited blast radius, observability, stop conditions, recovery, and design feedback. Source: `Interconnect, Routing, Security, and Chaos Rules` (234-242), `Incidents, Capacity, and Runtime Control` (217-220), `Testing Rules` (344-351).

Trigger rules:

- `M16` Outbound calls, dependency operations, resource checkouts, queue consumes, or thread waits trigger timeout, retry eligibility, retry bounds, fallback or degraded mode, validation, and caller-survival decisions. Source: `Dependency Protection Rules` (59-88), `Runtime State and Restart Safety Rules` (131-135), `Code Generation Rules` (323-340).
- `M17` Queues, buffers, pools, caches, log streams, background jobs, scheduled jobs, or collection APIs trigger capacity, full behavior, cleanup, miss/stampede/staleness behavior, pacing, pagination or streaming, and saturation monitoring. Source: `Load and Capacity Rules` (91-126), `Resource Management Rules` (151-169), `Cache Rules` (256-266), `Scheduled and Background Work Rules` (270-276).
- `M18` Deployment, configuration, startup, migrations, one-time jobs, scripts, or operational automation trigger idempotency or restartability, durable state, auditability, verification, and rollback or roll-forward. Source: `Production Readiness and Release Risk Rules` (49-55), `Runtime State and Restart Safety Rules` (129-148), `Deployment and Startup Rules` (224-230).
- `M19` Health checks, load balancing, service discovery, routing, or inter-service handshakes trigger readiness-aware traffic routing and health signals that reflect real ability to serve. Source: `Load and Capacity Rules / Additional Stability Patterns` (114-120), `Deployment and Startup Rules` (224-230), `Interconnect, Routing, Security, and Chaos Rules` (234-242).
- `M20` API and integration contracts trigger explicit failure modes, retryable/non-retryable outcomes, resilient interaction granularity, versioning, compatibility, and documented timeout or retry expectations. Source: `API and Contract Rules` (246-252).
- `M21` Incidents, performance failures, or capacity issues trigger failure-chain analysis, missing-defense review, detection-gap review, demand and saturation inspection, queue-age and dependency review, traffic-concentration review, and design changes. Source: `Incidents, Capacity, and Runtime Control` (214-220).
- `M22` Administrative controls, control planes, delivery tooling, hostile-traffic handling, or chaos/disaster work trigger authorization, auditability, safe defaults, stop mechanisms, bounded blast radius, and recovery paths. Source: `Incidents, Capacity, and Runtime Control` (214-220), `Interconnect, Routing, Security, and Chaos Rules` (234-242).

Final checklist:

- The checklist restates `M4`-`M7`, `M9`-`M15`, and `M16`-`M22` as a final scan rather than introducing new rules. Source: `Review Rules` (280-293), `Review Checklist` (355-369), `Final Instruction` (373-382).

## Nano mapping

Decision rules:

- `N1` Assume production dependencies, queues, caches, callers, bad data, and degraded states fail slowly, partially, and for longer than expected. Source: `Purpose` (3-18), `Stability Mindset Rules` (36-45).
- `N2` Prefer visible failure, blast-radius limits, load shedding, core-service preservation, and diagnosis over happy-path elegance. Source: `Primary Directive` (21-32), `Final Instruction` (373-382).
- `N3` Bound external calls, waits, retries, queues, pools, caches, logs, result sets, payloads, and scarce resources. Source: `Dependency Protection Rules` (59-88), `Load and Capacity Rules` (91-126), `Resource Management Rules` (151-169), `Cache Rules` (256-266).
- `N4` Retry only when safe, bounded, and backed off or jittered; avoid permanent-failure retries and stacked retry storms. Source: `Dependency Protection Rules / Retries Must Be Disciplined` (67-72), `Forbidden Patterns / Retry Storms` (302-305), `Scheduled and Background Work Rules` (270-276).
- `N5` Isolate failure with breakers, bulkheads, fast failure, separate pools, degraded modes, and deterministic cleanup. Source: `Dependency Protection Rules` (73-88), `Load and Capacity Rules / Additional Stability Patterns` (114-120), `Resource Management Rules` (160-163), `Forbidden Patterns` (296-320).
- `N6` Treat deployment, startup, automation, health, observability, configuration, rollback, security, and runtime state as production design. Source: `Production Readiness and Release Risk Rules` (49-55), `Runtime State and Restart Safety Rules` (129-148), `Operational Visibility Rules` (182-211), `Deployment and Startup Rules` (224-230), `Interconnect, Routing, Security, and Chaos Rules` (234-242).
- `N7` Validate external input and responses before trusting them and prevent bad data from poisoning caches, queues, state, or downstream systems. Source: `Runtime State and Restart Safety Rules` (131-135), `Data Boundary Rules` (172-179), `Cache Rules` (256-266).
- `N8` Make APIs, interconnects, caches, jobs, and operational controls explicit about failure, capacity, recovery, authorization, and stop behavior. Source: `Incidents, Capacity, and Runtime Control` (214-220), `Interconnect, Routing, Security, and Chaos Rules` (234-242), `API and Contract Rules` (246-252), `Cache Rules` (256-266), `Scheduled and Background Work Rules` (270-276).

Trigger rules:

- `N9` Remote calls, waits, queues, pools, caches, jobs, retries, or large result paths trigger bounds, failure behavior, validation, and saturation signals. Source: `Dependency Protection Rules` (59-88), `Load and Capacity Rules` (91-126), `Resource Management Rules` (151-169), `Operational Visibility Rules` (182-211).
- `N10` Startup, deployment, migration, configuration, scripts, or control tooling trigger recovery, auditability, observability, and restartability decisions. Source: `Production Readiness and Release Risk Rules` (49-55), `Runtime State and Restart Safety Rules` (129-148), `Incidents, Capacity, and Runtime Control` (214-220), `Deployment and Startup Rules` (224-230).
- `N11` Concentrated traffic through routing, scheduling, retries, fan-out, or hostile use triggers back pressure, shedding, pacing, or isolation before expensive work. Source: `Load and Capacity Rules` (91-126), `Interconnect, Routing, Security, and Chaos Rules` (234-242), `Scheduled and Background Work Rules` (270-276).
- `N12` Production tests, game days, chaos, or disaster drills trigger hypothesis, blast-radius limit, observability, stop condition, and recovery path. Source: `Interconnect, Routing, Security, and Chaos Rules` (240-242), `Testing Rules` (344-351).

Final checklist:

- The checklist restates `N3`-`N8` and `N9`-`N12` as a final scan rather than introducing new rules. Source: `Review Checklist` (355-369).

## Section coverage review

- `Purpose` (3-18): covered by `M1`, `M3`, `N1`, and `N6`; binding-policy wording is intentionally lost because it is metadata for the full source.
- `Primary Directive` (21-32): covered by `M2` and `N2`.
- `Stability Mindset Rules` (36-45): covered by `M1` and `N1`.
- `Production Readiness and Release Risk Rules` (49-55): covered by `M3`, `M18`, `N6`, and `N10`.
- `Dependency Protection Rules` (59-88): covered by `M4`-`M6`, `M16`, `N3`-`N5`, and `N9`.
- `Load and Capacity Rules` (91-126): covered by `M7`, `M8`, `M17`, `M19`, `N3`, `N5`, `N9`, and `N11`.
- `Runtime State and Restart Safety Rules` (129-148): covered by `M9`, `M11`, `M18`, `N6`, `N7`, and `N10`.
- `Resource Management Rules` (151-169): covered by `M10`, `M17`, `N3`, `N5`, and `N9`; the individual resource-type list is merged into scarce-resource budgeting.
- `Data Boundary Rules` (172-179): covered by `M11` and `N7`.
- `Operational Visibility Rules` (182-211): covered by `M12`, `N6`, and `N9`; individual metric names are merged into the observability rule and checklist.
- `Incidents, Capacity, and Runtime Control` (214-220): covered by `M13`, `M15`, `M21`, `M22`, `N8`, and `N10`.
- `Deployment and Startup Rules` (224-230): covered by `M9`, `M13`, `M18`, `M19`, `N6`, and `N10`.
- `Interconnect, Routing, Security, and Chaos Rules` (234-242): covered by `M14`, `M15`, `M19`, `M22`, `N6`, `N8`, `N11`, and `N12`.
- `API and Contract Rules` (246-252): covered by `M14`, `M20`, and `N8`.
- `Cache Rules` (256-266): covered by `M14`, `M17`, `N3`, `N7`, `N8`, and `N9`.
- `Scheduled and Background Work Rules` (270-276): covered by `M5`, `M14`, `M17`, `N4`, `N8`, and `N11`.
- `Review Rules` (280-293): covered by `M4`-`M7`, `M12`, `M14`, and the mini final checklist; collapsed from a review list into triggers and checklist.
- `Forbidden Patterns` (296-320): covered by `M1`, `M4`-`M7`, `M12`, `N2`-`N5`; examples are merged into operational anti-shortcut rules.
- `Code Generation Rules` (323-340): covered by `M4`, `M5`, `M9`, `M13`, `M16`, `N3`, `N4`, `N6`, and `N10`; standalone generation prose is intentionally lost.
- `Testing Rules` (344-351): covered by `M13`, `M15`, `M21`, `N6`, `N10`, and `N12`; detailed test cases are collapsed into triggers and checklist.
- `Review Checklist` (355-369): covered by `M4`-`M7`, `M12`, `M14`, `M16`-`M17`, and `N3`-`N8`; checklist wording is collapsed into final checks.
- `Final Instruction` (373-382): covered by `M2`, `M6`, `M7`, `M12`, and `N2`.

---

**Source:** [`ciembor/agent-rules-books`](https://github.com/ciembor/agent-rules-books) → `_rule-workbench/release-it/traceability.md`
