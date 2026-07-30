---
name: upwork-application-session
description: "Use when the user wants to search Upwork, qualify roles, draft proposals, submit applications, or continue an active Upwork application session. This skill uses a Chrome CDP workflow, payload JSON files, sequential browser actions, connect-budget tracking, and final success confirmation through Upwork proposal URLs."
category: business-and-finance
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/klajdikkolaj/upwork-autopilot/skills/upwork-application-session/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/klajdikkolaj/upwork-autopilot/skills/upwork-application-session/SKILL.md
---


# Upwork Application Session

Use this skill for real Upwork application work. Prefer the Chrome CDP path. Only use Atlas if JavaScript execution is confirmed to work there.

## Read first

- First try `../../config/applicant-profile.local.md`
- If that file does not exist in the cache copy, fall back to `$HOME/plugins/upwork-autopilot/config/applicant-profile.local.md`
- If that file does not exist, run `node ../../scripts/setup-applicant-profile.mjs`
- Then read `../../config/search-profile.local.json` if it exists
- If that file does not exist in the cache copy, fall back to `$HOME/plugins/upwork-autopilot/config/search-profile.local.json`
- If the local search profile does not exist, use `../../config/search-profile.template.json`
- `../../references/search-strategy.md`

## Non-negotiables

- Start every cover letter with `Hi,`
- Tone: friendly, professional, specific, low-fluff.
- Never invent project examples, metrics, portfolio URLs, or domain history.
- Never include email, phone, Telegram, WhatsApp, Calendly, or any off-platform contact detail in a proposal.
- Never attach the CV in this workflow.
- Do not parallelize browser actions against the live Upwork session.
- Stop when available Connects drop below `15`.
- Skip jobs that are already applied, blocked by hard geography, citizenship, or security constraints, or clearly below the user's floor.

## Setup

1. Run `../../scripts/bootstrap.sh` once from the plugin root.
2. Ensure the applicant profile exists. If it does not, run `node ../../scripts/setup-applicant-profile.mjs`.
2. Run `../../scripts/launch-controlled-chrome.sh` by default to reuse the user's normal logged-in Chrome profile.
3. If the user explicitly wants a clean browser state, run `../../scripts/launch-isolated-chrome.sh` instead.
4. Ask the user to log into Upwork only if the chosen browser mode is not already signed in.
5. Run `node ../../scripts/upwork-session-probe.mjs` to confirm login state.
6. Export a log path before submissions, for example:

```bash
export UPWORK_AUTOPILOT_LOG=$HOME/.codex/upwork-autopilot/logs/$(date +%F).jsonl
```

## Search and qualification

- List search results:

```bash
node ../../scripts/upwork-search-plan.mjs
```

- A raw keyword is converted into the default filtered Upwork search URL.
- A full Upwork search URL is accepted as-is.
- If `upwork-search-plan.mjs` returns multiple URLs, iterate them sequentially.
- To open a result and inspect the full job page:

```bash
node ../../scripts/upwork-search-inspect.mjs '<search-url-or-keyword>' detail 0
```

- To probe the apply flow for a specific job:

```bash
node ../../scripts/upwork-apply-probe.mjs '<job-url>'
```

Apply only if all of these hold:

- the client is payment verified
- the role is technically relevant
- the rate is compatible with the user's floor
- there is no hard location block
- the role is not already applied
- any requested proof, portfolio examples, or niche experience can be answered honestly from the profile or current context

## Proposal writing

Create a payload JSON file with `apply_patch`. The scripts fill fields in DOM order.

```json
{
  "textareas": [
    "Hi,\n\n..."
  ],
  "inputs": []
}
```

Rules:

- Before drafting, extract the actual deliverable, stack, client pain point, any written questions, and any request for examples or proof.
- First paragraph: open casually and directly, and name the actual problem or fit in plain language within the first 2 sentences.
- Default structure: 3 to 5 short paragraphs in natural prose, not a bullet-heavy sales pitch.
- Weave relevant experience into the paragraphs instead of defaulting to bullets.
- Use bullets only when the client explicitly asks for list-style answers or when multiple written questions are easier to answer that way.
- Proof section: use relevant project evidence from the profile only when it actually matches the post.
- When the applicant profile includes named project examples, prefer dropping 1 to 3 of the strongest ones naturally into the prose instead of listing every example.
- If the applicant profile includes `Differentiators to mention when relevant`, use at most 1 or 2 that genuinely strengthen this specific job. Do not force them into unrelated proposals.
- Closing: use the profile's `Preferred closing CTA` when present, or a close natural variant of it.
- If the client asks for project examples, case studies, metrics, URLs, or niche background, answer with the closest truthful match from the profile.
- If the profile does not contain the proof the client is asking for, stop and ask the user for the missing details before submitting. Do not guess.
- Keep the proposal usually around `220` to `320` words unless the page asks multiple written questions.
- Answer written questions directly in field order. Do not dodge them with generic sales copy.
- Use conversational phrasing and contractions when natural. Avoid templated buzzwords, generic praise, AI-sounding filler, and overly heavy systems language unless the post clearly calls for it.
- If the applicant profile states tone or structure preferences, follow those over the generic defaults in this file.
- The first line must begin with `Hi,`

## Submission

Run:

```bash
node ../../scripts/upwork-submit-proposal.mjs '<proposal-url>' /abs/path/to/payload.json
```

Success is confirmed only when the final URL contains `?success`.

The submit script:

- fills visible `textarea` fields in order
- fills visible text, url, email, and number inputs in order
- clicks `Submit a proposal`
- extracts the success URL and proposal ID
- appends a JSONL log entry if `UPWORK_AUTOPILOT_LOG` is set

## Failure handling

- If the page opens a video interview flow, skip unless the user explicitly wants that path.
- If the apply button is disabled, read the probe output before deciding whether to skip.
- If the form asks for required information that is missing from the profile, stop and ask the user before submitting.
- If `net::ERR_ABORTED` appears, another command touched the same Upwork tab. Resume with single-threaded browser actions only.
- If login, CAPTCHA, or 2FA appears, hand control to the user and resume after confirmation.

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/klajdikkolaj/upwork-autopilot/skills/upwork-application-session/SKILL.md`
