---
name: versioning-documents
description: "Use when the user wants to retrieve a stored document and its extraction result, list a document's versions, or diff two versions. Covers GET /v1/documents/{id}, GET /v1/documents/{id}/versions, and the sync-with-async-fallback diff at GET /v1/documents/{id}/diff plus its poll endpoint."
category: devops-and-infra
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/kreuzberg-dev/plugins/plugins/kreuzberg-cloud/skills/versioning-documents/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/kreuzberg-dev/plugins/plugins/kreuzberg-cloud/skills/versioning-documents/SKILL.md
---


# Versioning documents

Every extraction is stored against a stable `document_id` that persists
across re-processing. Use these endpoints when an application extracts the
same logical document more than once and needs the latest result, the full
version history, or a diff between two versions.

All four endpoints are `GET` and require a Bearer token.

## Endpoints

| Method | Path | Purpose |
|---|---|---|
| GET | `/v1/documents/{document_id}` | Latest version of a document with its extraction result. |
| GET | `/v1/documents/{document_id}/versions` | List all versions (paginated), newest first. |
| GET | `/v1/documents/{document_id}/diff?from={v}&to={v}` | Diff two versions — sync (`200`), async fallback (`202`) when over budget. |
| GET | `/v1/documents/{document_id}/diff/{diff_job_id}` | Poll an async diff job. |

`document_id` is the UUID returned alongside each extraction job. The
`from` and `to` query params accept either a version sequence integer or a
job UUID.

## Get the latest version

```bash
curl -s https://api.kreuzberg.dev/v1/documents/$DOC_ID \
  -H "Authorization: Bearer $KREUZBERG_API_KEY"
```

Returns the latest version's extraction result (same `result` shape as
`GET /v1/jobs/{id}` — `content`, `tables`, `images`, `metadata`).

## List versions

```bash
curl -s https://api.kreuzberg.dev/v1/documents/$DOC_ID/versions \
  -H "Authorization: Bearer $KREUZBERG_API_KEY"
```

Returns an array of `DocumentVersionEntry` (paginated). Each entry carries
its version sequence number and the job ID that produced it — use either as
a `from`/`to` value when diffing.

## Diff two versions

```bash
curl -s "https://api.kreuzberg.dev/v1/documents/$DOC_ID/diff?from=1&to=3" \
  -H "Authorization: Bearer $KREUZBERG_API_KEY"
```

The diff is computed **synchronously** and returned inline as `200` when it
fits the request budget:

```json
{
  "document_id": "…",
  "from_job_id": "…", "from_version": 1,
  "to_job_id": "…",   "to_version": 3,
  "diff": { "…": "kreuzberg ExtractionDiff shape" },
  "computed_at": "2026-06-20T10:00:00Z"
}
```

The `diff` field is the full `kreuzberg::diff::ExtractionDiff`. The OpenAPI
schema declares it opaque because the Rust type recurses; decode it against
kreuzberg's published diff schema if you need a typed surface — do not
hard-code a shape from this skill.

### Async fallback

When the diff exceeds the inline compute budget, the endpoint returns `202`
with a job handle instead:

```json
{ "diff_job_id": "…", "status": "pending" }
```

Poll it the same way you poll extraction jobs — exponential backoff capped
at ~30s — until terminal:

```bash
curl -s https://api.kreuzberg.dev/v1/documents/$DOC_ID/diff/$DIFF_JOB_ID \
  -H "Authorization: Bearer $KREUZBERG_API_KEY"
```

Treat both `200` (inline) and `202` (queued) as success at submit time;
branch on the status code to decide whether to poll.

## Errors

| Status | Meaning | Action |
|---|---|---|
| `400` | Invalid `from`/`to` | Pass a version sequence integer or a job UUID. |
| `401` | Bad API key | Check the `Authorization` header. |
| `404` | Version not found | Document or version doesn't exist in this project. |
| `422` | Async diff failed | The queued diff errored server-side; resubmit or report. |

## Other skills

- `tracking-cloud-jobs` — polling cadence and terminal-status detection (reuse it for async diff jobs).
- `offloading-extraction` — produces the `document_id` these endpoints read.

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/kreuzberg-dev/plugins/plugins/kreuzberg-cloud/skills/versioning-documents/SKILL.md`
