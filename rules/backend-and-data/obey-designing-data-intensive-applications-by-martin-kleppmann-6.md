---
name: obey-designing-data-intensive-applications-by-martin-kleppmann
description: "Canonical full source: full.md"
category: backend-and-data
source_repo: ciembor/agent-rules-books
source_path: "_rule-workbench/designing-data-intensive-applications/traceability.md"
source_url: https://github.com/ciembor/agent-rules-books/blob/HEAD/_rule-workbench/designing-data-intensive-applications/traceability.md
---
# OBEY Designing Data-Intensive Applications by Martin Kleppmann

Canonical full source: [full.md](full.md)

## Compression decisions

- Re-run under `_rule-workbench/PROCESS.md` on 2026-05-02 for book position 5 in alphabetical workbench order: `designing-data-intensive-applications`.
- Diagnosis: book-specific miss, not a process bug. `PROCESS.md` already requires current line ranges, section-by-section coverage, source-faithful compression, and retention of decision-changing data ownership, consistency, idempotency, replay, evolution, and distributed-systems rules.
- The previous `traceability.md` referenced older source section names and line ranges that are not present in the current `full.md`.
- `mini.md` was rebuilt against the current `full.md` and removes unsupported older-source detail while preserving the book's operational bias: explicit trade-offs, ownership of truth, idempotent and replay-safe processing, durable boundaries, schema evolution, and realistic distributed assumptions.
- `nano.md` keeps only the smallest always-on reminders for hidden data contracts, derived data, versioned contracts, retry/replay safety, distributed uncertainty, and invariant-matched coordination.
- No rule was omitted as `default`; every omission is either merged into a retained rule, collapsed into a trigger/checklist item, or intentionally lost as tool-specific detail too narrow for compressed attachments.

## Mini mapping

Decision rules:

- `M1` Make core data-system trade-offs explicit. Source: `Purpose` (3-16), `Primary Directive` (20-32), `Final Instruction` (384-393).
- `M2` Treat crashes, partial writes, duplicate work, timeouts, stale reads, and unknown downstream success as normal inputs; distinguish accepted, persisted, applied, and durable success. Source: `Reliability Rules` (36-47), `Primary Directive` (25-32), `Final Instruction` (386-393).
- `M3` Describe load and performance with concrete workload, bottleneck, contention, and tail-latency facts before changing architecture. Source: `Scalability and Maintainability Rules` (50-58).
- `M4` Choose data models, query models, and ownership boundaries from relationships, access patterns, consistency, update locality, evolution pressure, and primary-vs-derived data status. Source: `Data Model and Storage Rules` (61-80), `Query Model and Data Shape Rules` (83-91), `API and Service Boundary Rules` (290-296).
- `M5` Match storage engines, indexes, and analytical layouts to write/read/range/recovery needs, OLTP-vs-analytics fit, write amplification, and memory-vs-durability assumptions. Source: `Storage Engine and Indexing Rules` (94-103).
- `M6` Treat derived data as derived unless explicitly authoritative, with propagation, lag, observability, repair, and rebuild paths. Source: `Data Model and Storage Rules` (65-80), `Derived Data Rules` (251-261), `Review Rules` (309-310), `Code Generation Rules` (342-345).
- `M7` Define write semantics: durability, visibility, staleness, conflict detection, and conflict resolution. Source: `Consistency Rules` (106-125), `Review Checklist` (369-375), `Final Instruction` (386-393).
- `M8` Make commands, jobs, events, batch jobs, and stream processors safe under retry and replay; do not rely on unproved exactly-once delivery. Source: `Reliability Rules` (38-47), `Idempotency and Replay Rules` (128-139), `Batch and Stream Processing Rules` (280-287), `Code Generation Rules` (338-352), `Testing Rules` (357-359).
- `M9` Preserve only required ordering and scope it to the key, stream, partition, record, or entity history that defines correctness. Source: `Primary Directive` (28, 32), `Ordering Rules` (142-157), `Review Rules` (301-307), `Review Checklist` (372).
- `M10` Separate commands, events, durable logs, streams, and materialized views; design consumers and events for lag, duplicates, restart, replay, stable identifiers, metadata, and versioning. Source: `Event, Log, and Stream Rules` (160-178), `Schema Evolution Rules` (181-193), `Review Rules` (302-310).
- `M11` Design schemas, encodings, APIs, messages, events, and database changes as evolving contracts across mixed versions and migrations. Source: `Schema Evolution Rules` (181-193), `Encoding and Data Flow Rules` (196-204), `API and Service Boundary Rules` (294-296), `Code Generation Rules` (344).
- `M12` Choose replication topology from write topology, latency, failure tolerance, lag, failover, reconfiguration, conflict handling, read guarantees, quorum, and convergence needs. Source: `Replication Rules` (221-229).
- `M13` Partition by workload-relevant locality and consistency keys, with hot-key, skew, routing, secondary-index, rebalancing, and cross-partition costs explicit. Source: `Partitioning and Locality Rules` (207-218), `Review Rules` (311).
- `M14` Match transactions and isolation to invariants, atomicity scope, commit behavior, recovery, reconciliation, anomalies, and side-effect repair. Source: `Transaction Rules` (232-248), `Testing Rules` (360), `Review Checklist` (375).
- `M15` Treat distributed faults, clocks, timeouts, leases, locks, majorities, leadership, and coordination dependencies as assumptions needing a fault model. Source: `Distributed Fault, Clock, and Consensus Rules` (265-275).
- `M16` Use linearizability, total order broadcast, atomic commit, or consensus only where the coordination problem truly requires agreement. Source: `Distributed Fault, Clock, and Consensus Rules` (272-274).
- `M17` Make batch and stream processing recomputable and recoverable, with explicit time semantics, windows, late data, joins, checkpoints, external side effects, and source-to-sink guarantees. Source: `Batch and Stream Processing Rules` (278-287), `Testing Rules` (362).
- `M18` Align service boundaries with data ownership and update semantics; avoid casual splits of tightly consistent concepts and chatty cross-service joins. Source: `API and Service Boundary Rules` (290-296), `Review Checklist` (377).

Trigger rules:

- `M19` When changing a write path, state source of truth, consistency boundary, durability, visibility, downstream effects, rollback or repair, and unknown-success behavior. Source: `Primary Directive` (25-30), `Reliability Rules` (38-47), `Consistency Rules` (114-125), `Transaction Rules` (232-248), `Review Rules` (309).
- `M20` When adding or changing derived representations, define ownership, propagation, staleness, write cost, lag visibility, rebuild, and repair. Source: `Data Model and Storage Rules` (65-80), `Storage Engine and Indexing Rules` (99-101), `Derived Data Rules` (251-261), `Review Checklist` (373).
- `M21` When changing a schema, API, message, event, enum, status, or payload meaning, plan compatibility and migration across old readers, old writers, old data, old messages, new writers, and rollout. Source: `Schema Evolution Rules` (181-193), `Encoding and Data Flow Rules` (198-203), `Testing Rules` (361).
- `M22` When adding retries, jobs, consumers, queues, CDC, event sourcing, stream processors, or replayable batch work, prove duplicate, replay, ordering, retention, side-effect, and recovery safety. Source: `Idempotency and Replay Rules` (128-139), `Event, Log, and Stream Rules` (160-178), `Batch and Stream Processing Rules` (278-287), `Testing Rules` (357-359).
- `M23` When routing reads to replicas or using asynchronous replication, identify read-your-writes, monotonic-read, consistent-prefix, staleness, catch-up, failover, and conflict expectations. Source: `Replication Rules` (221-229), `Consistency Rules` (108-125).
- `M24` When partitioning data or work, test the ordinary query path for locality, skew, hot keys, routing metadata, rebalancing, secondary indexes, and cross-partition coordination. Source: `Partitioning and Locality Rules` (207-218), `Review Rules` (311).
- `M25` When choosing transaction isolation or weakening consistency, map each anomaly to the invariant it can break and add a compensating design where needed. Source: `Transaction Rules` (232-248), `Consistency Rules` (106-125), `Testing Rules` (360).
- `M26` When using timestamps, leases, locks, leadership, majority decisions, coordination services, or consensus-like mechanisms, define the clock assumption, quorum/session semantics, stale-authority behavior, and fencing. Source: `Distributed Fault, Clock, and Consensus Rules` (265-275).
- `M27` When reviewing or testing data-intensive code, scan for hidden ownership, missing idempotency, exactly-once assumptions, unscoped ordering, schema drift, unrebuildable projections, unclear multi-writes, and unobservable lag or failure. Source: `Review Rules` (299-312), `Forbidden Patterns` (315-332), `Testing Rules` (355-363), `Review Checklist` (366-380).

Final checklist:

- The checklist restates `M1`, `M6`-`M18`, and `M19`-`M27` as a final scan. Source: `Review Checklist` (366-380), `Final Instruction` (384-393).

## Nano mapping

Decision rules:

- `N1` State source of truth, consistency, durability, visibility, retry semantics, and evolution path for every important data change. Source: `Purpose` (8-14), `Primary Directive` (20-32), `Consistency Rules` (106-125), `Final Instruction` (384-393).
- `N2` Choose data tools from workload, access pattern, consistency, reliability, maintainability, and operational cost. Source: `Scalability and Maintainability Rules` (50-58), `Data Model and Storage Rules` (61-80), `Query Model and Data Shape Rules` (83-91), `Storage Engine and Indexing Rules` (94-103), `API and Service Boundary Rules` (290-296).
- `N3` Treat derived representations as secondary data with staleness, lag visibility, repair, and rebuild paths. Source: `Data Model and Storage Rules` (65-80), `Derived Data Rules` (251-261), `Review Checklist` (373).
- `N4` Make retried, replayed, queued, batch, stream, and event-driven work idempotent or transactional; reject casual exactly-once claims. Source: `Reliability Rules` (38-47), `Idempotency and Replay Rules` (128-139), `Batch and Stream Processing Rules` (280-287), `Forbidden Patterns` (317-320).
- `N5` Treat schemas, encodings, APIs, messages, logs, and events as versioned contracts for old code, old data, rolling upgrades, and in-flight messages. Source: `Event, Log, and Stream Rules` (168-178), `Schema Evolution Rules` (181-193), `Encoding and Data Flow Rules` (196-204).
- `N6` Assume distributed uncertainty: crashes, partial writes, timeouts, duplicate messages, reordered events, stale replicas, lag, clock error, pauses, stale leaders, and unknown success. Source: `Primary Directive` (28, 32), `Reliability Rules` (38-47), `Replication Rules` (223-229), `Distributed Fault, Clock, and Consensus Rules` (265-275).
- `N7` Match replication, partitioning, isolation, transactions, and coordination to the invariant instead of trusting follower freshness, quorum formulas, weak isolation, wall-clock order, or ad hoc leadership. Source: `Replication Rules` (221-229), `Partitioning and Locality Rules` (207-218), `Transaction Rules` (232-248), `Distributed Fault, Clock, and Consensus Rules` (265-275).

Trigger rules:

- `N8` Prove duplicate, replay, ordering, side-effect, and recovery safety when adding retries, jobs, consumers, queues, CDC, event sourcing, or stream processing. Source: `Idempotency and Replay Rules` (128-139), `Event, Log, and Stream Rules` (160-178), `Batch and Stream Processing Rules` (278-287), `Testing Rules` (357-359).
- `N9` Plan backward and forward compatibility plus migration, bootstrap, or rebuild paths when changing schemas, APIs, messages, events, enum values, or status meanings. Source: `Schema Evolution Rules` (181-193), `Encoding and Data Flow Rules` (196-204), `Testing Rules` (361).
- `N10` Define staleness, routing, hot-key, ordering, rebalancing, and cross-partition behavior when reading from replicas or partitioning data. Source: `Ordering Rules` (142-157), `Replication Rules` (221-229), `Partitioning and Locality Rules` (207-218).
- `N11` Define fault model, quorum/session semantics, stale-authority behavior, and fencing when using locks, leases, timestamps, leadership, majorities, or coordination services. Source: `Distributed Fault, Clock, and Consensus Rules` (265-275).

Final checklist:

- The checklist restates `N1`, `N3`-`N7`, and `N9`-`N11` as a final scan. Source: `Review Checklist` (366-380), `Final Instruction` (384-393).

## Section coverage review

- `Purpose` (3-16): covered by `M1`, `N1`; line 16 intentionally lost as modal policy wording rather than a separate operational rule.
- `Primary Directive` (20-32): covered by `M1`, `M2`, `M7`, `M8`, `M9`, `N1`, `N4`, `N6`.
- `Reliability Rules` (36-47): covered by `M2`, `M8`, `M19`, `N4`, `N6`.
- `Scalability and Maintainability Rules` (50-58): covered by `M3`, `N2`; operability and accidental complexity are merged into `M3`.
- `Data Model and Storage Rules` (61-80): covered by `M4`, `M6`, `M19`, `M20`, `N1`, `N2`, `N3`.
- `Query Model and Data Shape Rules` (83-91): covered by `M4`, `N2`; named query languages are merged into the rule about choosing expression forms by relationship, intent, maintainability, and optimization tradeoffs.
- `Storage Engine and Indexing Rules` (94-103): covered by `M5`, `M20`, `N2`; LSM, B-tree, column, compression, sort-order, materialized-view, cube, and memory-residency details are merged into workload-fit and derived-data-cost rules.
- `Consistency Rules` (106-125): covered by `M7`, `M19`, `M23`, `M25`, `N1`.
- `Idempotency and Replay Rules` (128-139): covered by `M8`, `M22`, `N4`, `N8`.
- `Ordering Rules` (142-157): covered by `M9`, `M22`, `M27`, `N10`.
- `Event, Log, and Stream Rules` (160-178): covered by `M10`, `M22`, `N5`, `N8`; event-design bullets are merged into stable identifiers, correlation metadata, replay, and versioned-payload wording.
- `Schema Evolution Rules` (181-193): covered by `M10`, `M11`, `M21`, `N5`, `N9`.
- `Encoding and Data Flow Rules` (196-204): covered by `M11`, `M21`, `N5`, `N9`; specific JSON, XML, Thrift, Protocol Buffers, and Avro examples are merged into compatibility and encoding-contract choices.
- `Partitioning and Locality Rules` (207-218): covered by `M13`, `M24`, `N7`, `N10`.
- `Replication Rules` (221-229): covered by `M12`, `M23`, `N6`, `N7`, `N10`.
- `Transaction Rules` (232-248): covered by `M14`, `M19`, `M25`, `N7`; named isolation levels and anomaly examples are preserved through invariant/anomaly mapping.
- `Derived Data Rules` (251-261): covered by `M6`, `M20`, `N3`.
- `Distributed Fault, Clock, and Consensus Rules` (265-275): covered by `M15`, `M16`, `M26`, `N6`, `N7`, `N11`.
- `Batch and Stream Processing Rules` (278-287): covered by `M17`, `M22`, `N4`, `N8`.
- `API and Service Boundary Rules` (290-296): covered by `M4`, `M11`, `M18`, `N2`.
- `Review Rules` (299-312): covered by `M6`, `M9`, `M19`, `M20`, `M21`, `M24`, `M27`; no standalone review item is intentionally lost.
- `Forbidden Patterns` (315-332): covered by `M8`, `M19`, `M21`, `M27`, `N4`, `N9`.
- `Code Generation Rules` (336-352): covered by `M1`, `M6`, `M8`, `M9`, `M11`, `M27`, `N1`, `N3`-`N6`; avoid-by-default bullets are merged into retry, ordering, multi-write, and stream-boundary rules.
- `Testing Rules` (355-363): covered by `M8`, `M14`, `M17`, `M21`, `M22`, `M27`, `N8`, `N9`.
- `Review Checklist` (366-380): covered by the final checklists in `mini.md` and `nano.md`, especially `M1`, `M6`-`M18`, `M19`-`M27`, `N1`, `N3`-`N7`, and `N9`-`N11`.
- `Final Instruction` (384-393): covered by `M1`, `M2`, `M7`, `M8`, `M11`, `M15`, `N1`, `N4`, `N6`.

---

**Source:** [`ciembor/agent-rules-books`](https://github.com/ciembor/agent-rules-books) → `_rule-workbench/designing-data-intensive-applications/traceability.md`
