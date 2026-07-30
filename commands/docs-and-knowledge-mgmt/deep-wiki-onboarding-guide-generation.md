---
name: deep-wiki-onboarding-guide-generation
description: "Generate four audience-tailored onboarding guides in an onboarding/ folder — Contributor, Staff Engineer, Executive, and Product Manager"
category: docs-and-knowledge-mgmt
source_repo: microsoft/skills
source_path: ".github/plugins/deep-wiki/commands/onboard.md"
source_url: https://github.com/microsoft/skills/blob/HEAD/.github/plugins/deep-wiki/commands/onboard.md
---


# Deep Wiki: Onboarding Guide Generation

You are creating onboarding documentation for this codebase. Generate **four** audience-tailored guides in an `onboarding/` folder.

## Source Repository Resolution (MUST DO FIRST)

Before generating any guides, resolve the source repository context:

1. **Check for git remote**: Run `git remote get-url origin`
2. **Ask the user**: _"Is this a local-only repository, or do you have a source repository URL?"_
   - Remote URL → store as `REPO_URL`, use linked citations: `[file:line](REPO_URL/blob/BRANCH/file#Lline)`
   - Local → use `(file_path:line_number)`
3. **Determine default branch**: Run `git rev-parse --abbrev-ref HEAD`
4. **Do NOT proceed** until resolved

## Step 1: Language & Technology Detection

Before writing anything, detect:

1. **Primary language** from file extensions and build files:
   - `*.cs`/`*.csproj` → C#, `*.py`/`pyproject.toml` → Python, `*.go`/`go.mod` → Go
   - `*.ts`/`package.json` → TypeScript, `*.rs`/`Cargo.toml` → Rust, `*.java`/`pom.xml` → Java

2. **Comparison language** for cross-language explanations:
   - C# → Python, Java → Python, Go → Python, TypeScript → Python
   - Python → JavaScript, Rust → C++ or Go, Swift → TypeScript

3. **Key technologies** by scanning for:
   - Orleans/Akka → Actor model, Cosmos/Mongo → Document DB, PostgreSQL/MySQL → RDBMS
   - Redis → Caching, Kafka/RabbitMQ/ServiceBus → Messaging, gRPC/GraphQL → API protocol
   - Docker/K8s → Containers

## Output Structure

```
onboarding/
├── index.md                    # Onboarding hub with guide selector table
├── contributor-guide.md        # For new contributors (assumes Python or JS)
├── staff-engineer-guide.md     # For staff/principal engineers
├── executive-guide.md          # For VP/director-level engineering leaders
└── product-manager-guide.md    # For product managers
```

### `onboarding/index.md` — Onboarding Hub

Generate a landing page with project summary and a guide selector table linking to all 4 guides with audience descriptions and estimated reading times.

## Step 2: Generate Contributor Guide

**File**: `onboarding/contributor-guide.md`
**Audience**: Engineers joining the project. Assumes proficiency in Python or JavaScript.
**Length**: 1000–2500 lines. Progressive — each section builds on the last.

### Required Structure

**Part I: Foundations** (skip if repo uses Python or JS)
1. **{Primary Language} for Python/JS Engineers** — Syntax side-by-side tables, async model, collections, DI, type system. Concrete code comparisons, NOT abstract descriptions.
2. **{Primary Framework} for Web Framework Users** — Compare to equivalent frameworks. Request pipeline, controllers, routing, config, DI container.
3. **{Key Technology 1} from First Principles** — The problem it solves, core concepts with comparisons, how THIS system uses it.
4. **{Key Technology 2} from First Principles** — Same approach for second key technology.

**Part II: This Codebase**
5. **The Big Picture** — One-sentence summary, core entities table, architecture `graph TB` diagram.
6. **Domain Model & Data Flow** — `erDiagram`, data invariants, `sequenceDiagram` for primary request lifecycle.
7. **Key Patterns** — "If you want to add X, follow this pattern" templates with real code.

**Part III: Getting Productive**
8. **Development Environment Setup** — Prerequisites table (Tool, Version, Install Command), step-by-step setup, common mistakes.
9. **Your First Task** — End-to-end walkthrough of adding a simple feature.
10. **Development Workflow** — Branch strategy, commit conventions, PR process. Use `flowchart` diagram.
11. **Running Tests** — All tests, single file, single test, coverage commands.
12. **Debugging Guide** — Common issues table: Symptom, Cause, Fix.
13. **Common Pitfalls** — Mistakes every new contributor makes and how to avoid them.

**Appendices**
- **Glossary** (40+ terms)
- **Key File Reference** (Path, Purpose, Why It Matters, Source)
- **Quick Reference Card** — Cheat sheet of most-used commands

### Key Rules
- **Progressive depth**: Part I → Part II → Part III. Never reference something before explaining it.
- **Concrete over abstract**: Code examples from the actual codebase.
- **Minimum 5 Mermaid diagrams** — each followed by `<!-- Sources: ... -->` comment block
- Every claim has a linked citation
- Every command must be copy-pasteable with expected output

## Step 3: Generate Staff Engineer Guide

**File**: `onboarding/staff-engineer-guide.md`
**Audience**: Staff/principal engineers. Deep systems experience, may not know this repo's language.
**Length**: 800–1200 lines. Dense, opinionated, architectural.

### Required Sections

1. **Executive Summary** — What the system is in one dense paragraph. What it owns vs delegates.
2. **The Core Architectural Insight** — The SINGLE most important concept. Include pseudocode in a DIFFERENT language from the repo.
3. **System Architecture** — Full Mermaid `graph TB` diagram (middleware → controllers → services → storage → external). Call out the "heart" of the system.
4. **Domain Model** — Mermaid `erDiagram` of core entities. Data invariants table: Entity, Invariant, Enforced By, Source.
5. **Component Types & Execution Paths** — Table: Component, Type, Execution Path, Key File, Source.
6. **Request Lifecycle** — Mermaid `sequenceDiagram` (with `autonumber`) showing typical request.
7. **State Transitions** — Mermaid `stateDiagram-v2` for domain entities with lifecycle states.
8. **Decision Log** — Table: Decision, Alternatives Considered, Rationale, Source.
9. **Dependency Rationale** — Table: Dependency, Purpose, What It Replaced, Source.
10. **Storage & Data Architecture** — Stores used, data access layer, consistency model. Comparison table.
11. **Failure Modes & Error Handling** — `flowchart` for error propagation.
12. **API Surface & Protocols** — Table: Method, Path, Handler, Auth, Source.
13. **Configuration & Feature Flags** — Table: Key, Default, Description, Source.
14. **Performance Characteristics** — Bottlenecks, scaling limits, hot paths.
15. **Security Model** — Auth, authorization, trust boundaries.
16. **Testing Strategy** — What's tested, what isn't.
17. **Known Technical Debt** — Table: Issue, Risk Level, Affected Files, Source.
18. **Where to Go Deep** — Recommended source file reading order.

### Key Rules
- Use **pseudocode in a different language** to explain concepts
- Use **comparison tables** to map unfamiliar concepts (e.g., `Task<T>` = `Awaitable[T]`)
- Dense prose with tables, NOT shallow bullet lists
- Every claim has a linked citation + `<!-- Sources: ... -->` comment blocks after each diagram
- **Minimum 5 Mermaid diagrams** (architecture, ER, class, sequence, state/flowchart)
- Focus on WHY decisions were made, not just WHAT exists

## Step 4: Generate Executive Guide

**File**: `onboarding/executive-guide.md`
**Audience**: VP/director of engineering. Needs capability overview, risk assessment, and investment context — NOT code-level details.
**Length**: 400–800 lines. Strategic, concise, decision-oriented.

### Required Sections

1. **System Overview** — What it does, who uses it, business value (2-3 sentences)
2. **Capability Map** — Table: Capability, Status (Built/Partial/Planned), Maturity, Dependencies
3. **Architecture at a Glance** — High-level Mermaid `graph LR` diagram. Services and deployment units ONLY — no internal code. Focus on team boundaries.
4. **Team Topology** — Table: Component, Owner, Criticality, Bus Factor
5. **Technology Investment Thesis** — Table: Technology, Purpose, Alternatives Considered, Risk Level
6. **Risk Assessment** — Table: Risk, Likelihood, Impact, Mitigation, Owner. Cover reliability, security, scalability, compliance.
7. **Cost & Scaling Model** — How costs scale with usage. Bottlenecks. When next scaling investment is needed.
8. **Dependency Map** — Mermaid `graph TB` showing critical external dependencies. Table: Dependency, Type (Service/Library/Platform), Risk if Unavailable.
9. **Key Metrics & Observability** — Table: Metric, Current Value, Target, Source
10. **Roadmap Alignment** — Engineering workstreams mapped to business priorities
11. **Technical Debt Summary** — Table: Issue, Business Impact, Effort to Fix, Priority (top 5 items)
12. **Recommendations** — 3-5 actionable recommendations for next quarter, prioritized by impact

### Key Rules
- **NO code snippets** — this guide is for engineering leaders, not coders
- **Diagrams at service/team level**, not class/function level
- **Business language** — translate technical concepts into impact (reliability, velocity, cost, risk)
- Tables for every structured finding
- **Minimum 3 Mermaid diagrams** (architecture overview, dependency map, capability map)
- Every claim backed by evidence — cite wiki sections or source files

## Step 5: Generate Product Manager Guide

**File**: `onboarding/product-manager-guide.md`
**Audience**: Product managers and non-engineering stakeholders. Needs to understand capabilities and boundaries — NOT implementation.
**Length**: 400–800 lines. User-centric, feature-focused, constraint-aware.

### Required Sections

1. **What This System Does** — 2-3 sentence elevator pitch in plain language (zero jargon)
2. **User Journey Map** — Mermaid `graph LR` or `journey` diagram showing primary user flows
3. **Feature Capability Map** — Table: Feature, Status (Live/Beta/Planned/Not Possible), User Behavior, Limitations
4. **Data Model (Product View)** — Simplified Mermaid `erDiagram` in business terms (e.g., "A Project has many Documents")
5. **Configuration & Feature Flags** — Table: Flag, What It Controls, Default, Who Can Change It
6. **API Capabilities** — Table: Capability, Method, Authentication, Rate Limits (written for integration partners)
7. **Performance & SLAs** — Table: Operation, Expected Latency, Throughput Limit, Current SLA
8. **Known Limitations & Constraints** — Table: Limitation, User Impact, Workaround, Planned Fix
9. **Data & Privacy** — Table: Data Type, Storage Location, Retention, Compliance
10. **Glossary** — Domain terms in plain language
11. **FAQ** — 10+ common PM questions, answered concisely

### Key Rules
- **ZERO engineering jargon** — no "middleware", "dependency injection", "ORM"
- **User-centric framing** — everything described in terms of user experience
- **Minimum 3 Mermaid diagrams** (user journey, data model, feature map)
- Tables for every structured finding
- If a technical concept must be mentioned, explain it in one plain sentence
- Every claim grounded in evidence

## Mermaid Diagram Rules (ALL guides)

ALL diagrams must use dark-mode colors:
- Node fills: `#2d333b`, borders: `#6d5dfc`, text: `#e6edf3`
- Subgraph backgrounds: `#161b22`, borders: `#30363d`
- Lines: `#8b949e`
- If using inline `style` directives, use dark fills with `,color:#e6edf3`
- Do NOT use `<br/>` in Mermaid labels (use `<br>` or line breaks)

## Validation

After generating each guide, verify:
- All file paths mentioned actually exist in the repo
- All class/method names are accurate (not hallucinated)
- Mermaid diagrams render (no syntax errors)
- No bare HTML-like tags outside code fences — wrap in backticks
- Each guide is appropriate for its audience — no code in Executive/PM guides, no jargon in PM guide

$ARGUMENTS

---

**Source:** [`microsoft/skills`](https://github.com/microsoft/skills) → `.github/plugins/deep-wiki/commands/onboard.md`
