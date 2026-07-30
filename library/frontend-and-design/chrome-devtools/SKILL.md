---
name: chrome-devtools
description: "Use Chrome DevTools MCP to inspect live pages, reproduce browser issues, automate user flows, inspect console and network activity, and verify frontend fixes in a real Chrome session. Trigger when the user mentions browser bugs, client-side errors, broken forms, flaky UI behavior, or asks to interact with a site directly."
category: frontend-and-design
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/win4r/chrome-devtools-codex-plugin/skills/chrome-devtools/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/win4r/chrome-devtools-codex-plugin/skills/chrome-devtools/SKILL.md
---


Use this skill when source inspection alone is not enough and Codex should operate a live browser.

## Default Flow

1. Open or reuse a page with `new_page` or `navigate_page`.
2. Wait for the relevant UI if needed with `wait_for`.
3. Capture structure with `take_snapshot`.
4. Interact using `uid` values from the snapshot.
5. Inspect the relevant evidence surface:
   - `list_console_messages` or `get_console_message` for runtime errors
   - `list_network_requests` or `get_network_request` for API and asset failures
   - `take_screenshot` when visible state matters
   - `evaluate_script` for targeted DOM or app-state checks
6. Re-run the smallest verification path after each code change.

## Working Rules

- Prefer `take_snapshot` over screenshots for navigation and form work.
- Take a fresh snapshot after navigation or DOM-changing actions.
- Keep console and network queries filtered or paginated to reduce noise.
- Save large artifacts to disk with `filePath` when the tool supports it.
- If you need an already-running browser session, point the MCP server at it with `--browser-url=...` instead of launching a fresh instance.

## Common Patterns

- Reproduce a bug: navigate, wait, snapshot, interact, inspect console and network.
- Verify a fix: repeat the exact user path and compare visible state plus console and request results.
- Gather evidence: capture a screenshot, the failing request, and the matching console message.

## When Not to Use It

- If the question is purely about static source code and no live browser state matters.
- If the MCP server is running in a restricted mode that does not expose the tools you need.

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/win4r/chrome-devtools-codex-plugin/skills/chrome-devtools/SKILL.md`
