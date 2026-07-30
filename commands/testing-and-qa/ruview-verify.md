---
name: ruview-verify
description: "Verify a RuView build — Rust tests, deterministic Python proof, firmware hashes, ADR-028 witness bundle + self-verification, and the pre-merge checklist."
category: testing-and-qa
source_repo: ruvnet/RuView
source_path: "plugins/ruview/commands/ruview-verify.md"
source_url: https://github.com/ruvnet/RuView/blob/HEAD/plugins/ruview/commands/ruview-verify.md
---


# /ruview-verify

Run RuView's trust pipeline.

1. Invoke the **`ruview-verify`** skill.
2. Based on `$ARGUMENTS` (default `all`):
   - **tests** — `cd v2 && cargo test --workspace --no-default-features` (1,400+ pass, 0 fail).
   - **proof** — `python archive/v1/data/proof/verify.py` (must print `VERDICT: PASS`; if hash drift from a legit numpy/scipy bump, `--generate-hash` then re-run). Optionally `cd archive/v1 && python -m pytest tests/ -x -q`.
   - **bundle** — `bash scripts/generate-witness-bundle.sh`, then `cd dist/witness-bundle-ADR028-*/ && bash VERIFY.sh` (must be 7/7 PASS).
   - **all** — do all of the above in order.
3. If this follows a code change, walk the **pre-merge checklist** from `CLAUDE.md` (README/CLAUDE.md/CHANGELOG/user-guide updates, ADR count, witness bundle regen, Docker rebuild only if needed, crate publishing in dependency order, `.gitignore`, security review for hardware/network modules).
4. For security-related changes also run `npx @claude-flow/cli@latest security scan`.

---

**Source:** [`ruvnet/RuView`](https://github.com/ruvnet/RuView) → `plugins/ruview/commands/ruview-verify.md`
