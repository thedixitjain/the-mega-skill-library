---
name: pressreleasesonline
description: "Draft and publish AI-powered press releases — submit a URL + notes, get a live release page instantly. Free, no API key required."
category: backend-and-data
source_repo: davepoon/buildwithclaude
source_path: "plugins/all-skills/skills/pressreleasesonline/SKILL.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/all-skills/skills/pressreleasesonline/SKILL.md
---


# pressreleases.online

Draft and publish press releases using AI. Submit a URL and some notes, get a polished release page with RSS feed and sitemap — no account, no API key, completely free.

## When to Use This Skill

- User wants to announce a product launch, feature, or milestone
- User wants to generate a press release draft from a website URL
- User wants to publish a press release without signing up for a service

## What This Skill Does

1. Accepts a URL and optional notes/instructions
2. Uses AI to draft a professional press release
3. Publishes it as a live page with its own URL, RSS feed, and sitemap

## Usage

```bash
# Submit a URL for AI-drafted press release
curl -X POST https://pressreleases.online/api/v1/releases \
  -H "Content-Type: application/json" \
  -d '{"website": "https://example.com", "email": "you@example.com", "notes": "Announcing our v2 launch"}'

# Confirm with email code (last 4 chars of md5(email))
curl -X POST https://pressreleases.online/api/v1/releases/confirm \
  -H "Content-Type: application/json" \
  -d '{"token": "<token from above>", "code": "<4-char code from email>"}'
```

## Resources

- Website: https://pressreleases.online
- API docs: https://pressreleases.online/skills.md

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/all-skills/skills/pressreleasesonline/SKILL.md`
