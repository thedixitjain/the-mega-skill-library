---
name: quality-gate-command
description: "Run the ECC quality pipeline on demand for a file or project scope."
category: devops-and-infra
source_repo: affaan-m/ECC
source_path: ".opencode/commands/quality-gate.md"
source_url: https://github.com/affaan-m/ECC/blob/HEAD/.opencode/commands/quality-gate.md
---
# Quality Gate Command

Run the ECC quality pipeline on demand for a file or project scope.

## Usage

`/quality-gate [path|.] [--fix] [--strict]`

- default target: current directory (`.`)
- `--fix`: allow auto-format/fix where configured
- `--strict`: fail on warnings where supported

## Pipeline

1. Detect language/tooling for target.
2. Run formatter checks.
3. Run lint/type checks when available.
4. Produce a concise remediation list.

## Notes

This command mirrors hook behavior but is operator-invoked.

## Arguments

$ARGUMENTS:
- `[path|.]` optional target path
- `--fix` optional
- `--strict` optional

---

**Source:** [`affaan-m/ECC`](https://github.com/affaan-m/ECC) → `.opencode/commands/quality-gate.md`
