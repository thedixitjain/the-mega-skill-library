---
name: blueprint-writing
description: "| How to write Blueprint-quality blueprints that AI agents can consume effectively. Covers implementation-agnostic blueprint design, testable acceptance criteria, hierarchical structure, cross-referencing, blueprint templates, greenfield and rewrite patterns, blueprint compaction, and gap analysis. Trigger phrases: \"write blueprints\", \"create blueprints\", \"blueprint this out\", \"define requirements for agents\", \"how to write blueprints for AI\""
category: writing-and-content
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/JuliusBrussee/blueprint/skills/blueprint-writing/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/JuliusBrussee/blueprint/skills/blueprint-writing/SKILL.md
---


# Blueprint Writing

## Core Principle: Blueprints Describe WHAT, Not HOW

Blueprints are **implementation-agnostic**. They define what the system must do and how to verify it, but never prescribe a specific framework, language, or architecture.

This is the fundamental distinction in Blueprint:
- **Blueprints** = WHAT must be true (framework-agnostic, durable, portable)
- **Plans** = HOW to build it (framework-specific, derived from blueprints)
- **Code** = the implementation (generated from plans, validated against blueprints)

### Why Implementation-Agnostic?

When blueprints avoid prescribing HOW, they become:
- **Portable** — the same blueprints can drive implementations in different frameworks
- **Durable** — blueprints survive technology migrations
- **Testable** — acceptance criteria are about behavior, not implementation details
- **Reusable** — the same blueprints work for greenfield, rewrites, and cross-framework evaluation

**Bad blueprint requirement:** "Use React useState hook to manage form state"
**Good blueprint requirement:** "Form state persists across user interactions within a session. Acceptance: entering values, navigating away, and returning preserves all entered values."

---

## Every Requirement Needs Testable Acceptance Criteria

This is the single most important rule in Blueprint writing. If an agent cannot automatically validate a requirement, that requirement will not be met.

### The Validation-First Rule

Every requirement must answer: **"How would an automated test verify this?"**

| Weak Criterion | Strong Criterion |
|----------------|-----------------|
| "UI should look good" | "All interactive elements have minimum 44x44px touch targets" |
| "System should be fast" | "API responses return within 200ms at p95 under 100 concurrent users" |
| "Handle errors gracefully" | "Network failures display a retry prompt with exponential backoff (1s, 2s, 4s)" |
| "Support authentication" | "Valid credentials return a session token; invalid credentials return 401 with error message" |

### Acceptance Criteria Format

Each criterion should be:
- **Observable** — can be checked by reading output, UI state, or logs
- **Deterministic** — same input always produces same pass/fail result
- **Automatable** — an agent can write a test that checks this
- **Independent** — does not depend on subjective judgment

```markdown
**Acceptance Criteria:**
- [ ] {Action} results in {observable outcome}
- [ ] Given {precondition}, when {action}, then {result}
- [ ] {Metric} meets {threshold} under {conditions}
```

---

## Hierarchical Structure with Index

Blueprints must be organized as a hierarchy — one index file linking to domain-specific sub-blueprints. This enables progressive disclosure: agents read the index first, then only the sub-blueprints relevant to their task.

### The Blueprint Index Pattern

Create a `blueprint-overview.md` as the entry point:

```markdown
# Blueprint Overview

## Domains

| Domain | Blueprint File | Summary |
|--------|-----------|---------|
| Authentication | blueprint-auth.md | User registration, login, session management, OAuth |
| Data Models | blueprint-data-models.md | Core entities, relationships, validation rules |
| API | blueprint-api.md | REST endpoints, request/response formats, error handling |
| UI Components | blueprint-ui-components.md | Shared components, accessibility, responsive behavior |
| Notifications | blueprint-notifications.md | Email, push, in-app notification delivery |

## Cross-Cutting Concerns
- Security requirements: see blueprint-auth.md R3, blueprint-api.md R7
- Performance budgets: see blueprint-api.md R12, blueprint-ui-components.md R5
- Accessibility: see blueprint-ui-components.md R8-R10
```

### Why Hierarchical?

1. **Context window efficiency** — agents load only the domains they need
2. **Parallel work** — different agents can own different spec domains
3. **Review efficiency** — humans can review domain-by-domain
4. **Cross-referencing** — domains link to each other explicitly

---

## Cross-Referencing Between Blueprints

Related blueprints must link to each other. Cross-references prevent requirements from being lost at domain boundaries.

### Cross-Reference Patterns

```markdown
## Cross-References
- **Depends on:** blueprint-auth.md R1 (session tokens required for API access)
- **Depended on by:** blueprint-notifications.md R4 (uses user preferences from this blueprint)
- **Related:** blueprint-ui-components.md R6 (error display components used by this domain)
```

### When to Cross-Reference

- When one domain's requirement depends on another domain's output
- When shared entities are defined in one blueprint but used in many
- When validation criteria span multiple domains
- When out-of-scope items are in-scope for another blueprint

---

## Full Blueprint Format Template

Use this template for every domain blueprint:

```markdown
# Blueprint: {Domain Name}

## Scope
{One paragraph describing what this spec covers and its boundaries.}

## Requirements

### R1: {Requirement Name}
**Description:** {What must be true — stated in terms of behavior, not implementation.}
**Acceptance Criteria:**
- [ ] {Testable criterion 1}
- [ ] {Testable criterion 2}
- [ ] {Testable criterion 3}
**Dependencies:** {Other specs/requirements this depends on, or "None"}

### R2: {Requirement Name}
**Description:** {What must be true}
**Acceptance Criteria:**
- [ ] {Testable criterion 1}
- [ ] {Testable criterion 2}
**Dependencies:** {Dependencies}

### R3: ...

## Out of Scope
{Explicit list of things this blueprint does NOT cover. This is critical — it prevents
agents from over-building and clarifies domain boundaries.}
- {Thing explicitly excluded and why}
- {Another exclusion}

## Cross-References
- See also: blueprint-{related-domain}.md — {why it is related}
- Depends on: blueprint-{dependency}.md R{N} — {what is needed}
- Depended on by: blueprint-{dependent}.md R{N} — {what depends on this}
```

### Template Rules

1. **Number requirements sequentially** (R1, R2, R3...) — agents reference them by ID
2. **Every requirement gets acceptance criteria** — no exceptions
3. **Out of Scope is mandatory** — explicit exclusions prevent scope creep
4. **Cross-References section is mandatory** — even if it says "None"
5. **Scope section is one paragraph** — concise boundary description

---

## Greenfield Pattern: Reference Material → Blueprints

When building from scratch, you start with reference materials and derive blueprints from them.

### Flow

```
context/refs/              context/blueprints/
├── prd.md          →      ├── blueprint-overview.md
├── design-doc.md   →      ├── blueprint-auth.md
├── api-draft.md    →      ├── blueprint-api.md
└── research/       →      ├── blueprint-data-models.md
    └── ...         →      └── blueprint-ui.md
```

### Process

1. **Place all reference materials** in `context/refs/`
2. **Run blueprint generation** — agent reads all refs, decomposes into domains
3. **Agent produces:**
   - `blueprint-overview.md` — index with domain summaries
   - One `blueprint-{domain}.md` per identified domain
   - Cross-references between related domains
4. **Human reviews** blueprints for completeness and correctness
5. **Iterate** — refine blueprints based on review feedback

### Greenfield Prompt Pattern

The first prompt in a greenfield pipeline (typically `001-generate-blueprints-from-refs.md`) should:
- Read all files in `context/refs/`
- Decompose reference material into domains
- Generate blueprints following the template above
- Create `blueprint-overview.md` as the index
- Cross-reference related blueprints

---

## Rewrite Pattern: Old Code → Reference Docs → Blueprints

When rewriting an existing system, the existing code becomes your reference material. But you never go directly from old code to new code — you always extract blueprints first.

### Flow

```
Existing codebase          context/refs/              context/blueprints/
├── src/            →      ├── ref-apis.md      →     ├── blueprint-overview.md
├── tests/          →      ├── ref-data-models.md →   ├── blueprint-auth.md
└── docs/           →      ├── ref-ui-components.md →  ├── blueprint-api.md
                           └── ref-architecture.md →   └── blueprint-data.md
```

### Process

1. **Agent explores the existing codebase** and generates reference documents
2. **Reference docs capture** the current system's behavior, APIs, data models, and UI patterns
3. **Agent generates blueprints** from reference docs — implementation-agnostic requirements
4. **Validate blueprints against existing code** — verify acceptance criteria match current behavior
5. **Proceed with normal DABI** — blueprints drive the new implementation

### Rewrite Prompt Pattern

Rewrites typically use more prompts because of the reverse-engineering step:
- `001`: Generate reference materials from old code
- `002`: Generate blueprints from references + feature scope
- `003`: Validate blueprints against existing codebase
- `004+`: Plans and implementation

The key difference from greenfield: step 003 validates that your blueprints actually describe what the old system does, before you start building the new one.

---

## Blueprint Compaction

When implementation tracking or blueprint files grow beyond approximately 500 lines, they become unwieldy for agents to process efficiently. Spec compaction compresses large files while preserving active context.

### When to Compact

- Implementation tracking file exceeds 500 lines
- Blueprint file has many resolved/completed requirements mixed with active ones
- Agent is spending too much context window on historical information

### How to Compact

1. **Identify resolved content:** completed tasks, resolved issues, archived dead ends
2. **Archive removed content** to a separate file (e.g., `impl/archive/impl-domain-v1.md`)
3. **Preserve in the compacted file:**
   - All active/in-progress tasks
   - All open issues
   - Recent dead ends (last 2-3 sessions)
   - Current test health status
   - Active cross-references
4. **Target:** under 500 lines in the active file

### Compaction Rule

Never delete information — move it to an archive. Agents can still find archived context if needed, but it will not consume context window during normal operations.

---

## Gap Analysis

Gap analysis compares what was built against what was intended, identifying where blueprints, plans, or validation fell short.

### How to Perform Gap Analysis

1. **Read blueprints** (intended behavior) and **implementation tracking** (what was built)
2. **For each blueprint requirement,** check if acceptance criteria are satisfied
3. **Classify each requirement:**

| Status | Meaning |
|--------|---------|
| **Complete** | All acceptance criteria pass |
| **Partial** | Some criteria pass, others do not |
| **Missing** | Requirement not implemented at all |
| **Over-built** | Implementation exceeds blueprint (may indicate blueprint gap) |

4. **Report gaps** with: which blueprint, which criterion, what is missing
5. **Feed gaps into revision** — update blueprints if needed, then re-implement

### Gap Analysis as Feedback

Gap analysis is not a one-time activity. Run it:
- After each implementation iteration
- Before starting a new session (to prioritize work)
- When convergence stalls (to identify what is blocking progress)

---

## Integration with Other Skills

### Collaborative Design in the Draft Phase

The Draft phase (`/bp:draft`) now embeds brainstorming principles directly. When running in interactive mode (no arguments), the drafter follows a collaborative design process before generating any files:

1. **Explore project context** — check existing files, docs, commits before asking questions
2. **Ask clarifying questions one at a time** — understand purpose, constraints, success criteria
3. **Propose 2-3 domain decomposition approaches** — with tradeoffs and a recommendation
4. **Present the design incrementally** — section by section, get approval per domain
5. **Generate blueprints only after design approval** — formalize with acceptance criteria
6. **Blueprint review loop** — automated reviewer checks quality, up to 3 iterations
7. **User review gate** — explicit approval before transitioning to Architect phase

This process applies to EVERY project regardless of perceived simplicity. The design can be short for simple projects, but it must happen.

**Visual companion:** For projects involving visual elements (UI, architecture diagrams), the Draft phase can use a browser-based visual companion to show mockups and diagrams during the design conversation. See `references/visual-companion.md`.

**YAGNI enforcement:** During the design conversation and blueprint generation, actively strip requirements the user did not ask for. Smaller blueprints are better blueprints.

### With `bp:design-system`

When DESIGN.md exists at the project root, blueprints for UI domains should reference design tokens in acceptance criteria. This creates a traceable chain: DESIGN.md -> blueprint acceptance criterion -> plan task -> implementation.

| Acceptance Criterion Type | Design Reference |
|--------------------------|-----------------|
| "Button has primary CTA appearance" | DESIGN.md Section 4, primary button variant |
| "Text follows heading hierarchy" | DESIGN.md Section 3, type scale |
| "Card has subtle elevation" | DESIGN.md Section 6, elevation level 1 |
| "Layout uses 12-column grid" | DESIGN.md Section 5, grid system |
| "Colors adapt for dark mode" | DESIGN.md Section 2, dark mode mapping |

**Do NOT duplicate DESIGN.md content into blueprints.** Reference by section/token name only. If a color changes in DESIGN.md, blueprints should not need updating.

When a blueprint needs a visual pattern not yet defined in DESIGN.md, note it in the acceptance criterion:
```markdown
- [ ] Component uses card-like container [DESIGN.md: pattern not yet defined — flag for design update]
```

### With `bp:validation-first`

Every acceptance criterion in a blueprint must map to at least one validation gate. When writing blueprints, think about which gate will verify each requirement:

| Acceptance Criterion Type | Likely Gate |
|--------------------------|-------------|
| "Code compiles without errors" | Gate 1: Build |
| "Function returns correct output for input X" | Gate 2: Unit Tests |
| "User can complete workflow end-to-end" | Gate 3: E2E/Integration |
| "Response time under N ms" | Gate 4: Performance |
| "Application starts and displays main screen" | Gate 5: Launch Verification |
| "UI matches design intent" | Gate 6: Human Review |

### With `bp:context-architecture`

Blueprints live in the `context/blueprints/` directory. See `bp:context-architecture` for the full context directory structure, CLAUDE.md conventions, and multi-repo strategies.

### With `bp:impl-tracking`

As blueprints are implemented, progress is tracked in `context/impl/` documents. Dead ends discovered during implementation should be recorded to prevent future agents from retrying failed approaches.

---

## Common Mistakes

### 1. Writing Implementation-Specific Blueprints

**Wrong:** "Use PostgreSQL with a users table containing columns: id (UUID), email (VARCHAR), ..."
**Right:** "User accounts have a unique identifier and email. Email must be unique across all accounts. Acceptance: creating two accounts with the same email fails with a duplicate error."

### 2. Vague Acceptance Criteria

**Wrong:** "System handles errors properly"
**Right:** "When a network request fails, the UI displays an error message within 2 seconds and offers a retry action. Acceptance: simulating network failure shows error banner with retry button."

### 3. Missing Out of Scope

Every blueprint needs explicit exclusions. Without them, agents will over-build or make assumptions.

### 4. No Cross-References

Domains do not exist in isolation. If blueprint-auth defines session tokens that blueprint-api uses, both blueprints must cross-reference each other.

### 5. Monolithic Blueprints

A single 1000-line blueprint file defeats progressive disclosure. Decompose into domains with a clear index.

---

## Summary

Writing blueprints for AI agents follows these rules:

1. **WHAT, not HOW** — describe behavior, not implementation
2. **Every requirement gets testable acceptance criteria** — if agents cannot validate it, it will not be met
3. **Hierarchical with an index** — progressive disclosure for context efficiency
4. **Cross-referenced** — related domains link to each other
5. **Explicitly scoped** — out-of-scope section prevents over-building
6. **Compact when large** — archive resolved content, keep active files under 500 lines
7. **Living documents** — blueprints evolve through revision as gaps are discovered

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/JuliusBrussee/blueprint/skills/blueprint-writing/SKILL.md`
