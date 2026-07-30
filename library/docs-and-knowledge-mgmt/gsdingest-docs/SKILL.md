---
name: gsdingest-docs
description: "Scan a repo for mixed ADRs, PRDs, SPECs, and DOCs and bootstrap or merge the full .planning/ setup from them. Classifies each doc in parallel, synthesizes a consolidated context with a conflicts report, and routes to new-project or merge-milestone depending on whether .planning/ already exists."
allowed-tools: "Read Write Edit Bash Glob Grep AskUserQuestion Task"
category: docs-and-knowledge-mgmt
source_repo: davepoon/buildwithclaude
source_path: "plugins/gsd/skills/ingest-docs/SKILL.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/gsd/skills/ingest-docs/SKILL.md
---


<objective>
Build the full `.planning/` setup (or merge into an existing one) from multiple pre-existing planning documents — ADRs, PRDs, SPECs, DOCs — in one pass.

- **Net-new bootstrap** (`--mode new`, default when `.planning/` is absent): produces PROJECT.md + REQUIREMENTS.md + ROADMAP.md + STATE.md from synthesized doc content, delegating final generation to `gsd-roadmapper`.
- **Merge into existing** (`--mode merge`, default when `.planning/` is present): appends phases and requirements derived from the ingested docs; hard-blocks any contradiction with existing locked decisions.

Auto-synthesizes most conflicts using the precedence rule `ADR > SPEC > PRD > DOC` (overridable via manifest). Surfaces unresolved cases in `.planning/INGEST-CONFLICTS.md` with three buckets: auto-resolved, competing-variants, unresolved-blockers. The BLOCKER gate from the shared conflict engine prevents any destination file from being written when unresolved contradictions exist.

**Inputs:** directory-convention discovery (`docs/adr/`, `docs/prd/`, `docs/specs/`, `docs/rfc/`, root-level `{ADR,PRD,SPEC,RFC}-*.md`), or an explicit `--manifest <file>` YAML listing `{path, type, precedence?}` per doc.

**v1 constraints:** hard cap of 50 docs per invocation; `--resolve interactive` is reserved for a future release.
</objective>

<execution_context>
@${CLAUDE_PLUGIN_ROOT}/workflows/ingest-docs.md
@${CLAUDE_PLUGIN_ROOT}/references/ui-brand.md
@${CLAUDE_PLUGIN_ROOT}/references/gate-prompts.md
@${CLAUDE_PLUGIN_ROOT}/references/doc-conflict-engine.md
</execution_context>

<context>
$ARGUMENTS
</context>

<process>
Execute the ingest-docs workflow end-to-end. Preserve all approval gates (discovery, conflict report, routing) and the BLOCKER safety rule.
</process>

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/gsd/skills/ingest-docs/SKILL.md`
