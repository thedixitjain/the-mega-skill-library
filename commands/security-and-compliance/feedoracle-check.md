---
name: feedoracle-check
description: "Check MiCA compliance status and peg stability for a stablecoin"
category: security-and-compliance
source_repo: davepoon/buildwithclaude
source_path: "plugins/feedoracle-compliance/commands/feedoracle-check.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/feedoracle-compliance/commands/feedoracle-check.md
---


Check the MiCA compliance status for the stablecoin symbol provided by the user.

Steps:
1. Call the mica_status MCP tool with the token symbol
2. Call the peg_deviation MCP tool with the same symbol
3. Call the compliance_preflight MCP tool with the same symbol

Present the results in a clear summary:
- MiCA authorization status (verified/pending/not_authorized)
- Current peg deviation percentage and status
- Preflight decision (PASS/WARN/BLOCK) with reason codes
- Cite the request_id and ES256K signature for each response

Example output format:

## USDC - MiCA Compliance Check

**MiCA Status:** Verified (Art. 48 EMT)
**Peg:** 0.01% deviation - STABLE
**Preflight:** PASS - no risk flags

Evidence IDs: fo-abc123, fo-def456, fo-ghi789
Signatures: ES256K (verify via JWKS)

If the user provides multiple symbols, check each one separately.

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/feedoracle-compliance/commands/feedoracle-check.md`
