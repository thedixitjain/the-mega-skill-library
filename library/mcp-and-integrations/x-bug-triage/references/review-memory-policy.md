# Review Memory Policy — X Bug Triage Plugin

## Override Types (8)

All human corrections are stored in the `overrides` table and loaded at the start of each triage run.

| Type | Effect | Persists |
|------|--------|----------|
| `cluster_merge` | Combine two clusters into one | Indefinitely |
| `cluster_split` | Divide a cluster into sub-clusters | Indefinitely |
| `noise_suppression` | Suppress matching pattern in future runs | Indefinitely |
| `routing_override` | Change owner recommendation for a cluster | Indefinitely |
| `issue_family_link` | Link cluster to an issue family | Indefinitely |
| `severity_override` | Override computed severity | Indefinitely |
| `label_correction` | Fix classification/family assignment | Indefinitely |
| `snooze` | Temporarily suppress with expiry | Until expires_at |

## Application Order

1. Label corrections (changes family/title)
2. Severity overrides (changes severity)
3. Routing overrides (checked during routing phase)
4. Noise suppression (checked during display/filing phase)
5. Snooze (checked during display phase)

## Key Rules

- Overrides are **durable memory** — they persist across runs, not just one-off
- Most recent override wins when multiple apply to the same cluster
- Snooze overrides have an `expires_at` field — expired snoozes are ignored
- `noise_suppression` with reason containing "false positive" is how false positives are tracked
- Override application is always logged to audit_log as `override_applied`

## Governance

- Human corrections take precedence over computed values
- A single correction can affect future runs automatically
- All override actions are audited for traceability
