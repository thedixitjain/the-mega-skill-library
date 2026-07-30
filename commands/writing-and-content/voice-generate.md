---
name: voice-generate
description: "Generate text in your extracted writing voice"
category: writing-and-content
source_repo: athola/claude-night-market
source_path: "plugins/scribe/commands/voice-generate.md"
source_url: https://github.com/athola/claude-night-market/blob/HEAD/plugins/scribe/commands/voice-generate.md
---


# /voice-generate Command

Generate text in a trained writing voice.

## Usage

```bash
# Generate with default register, review enabled
/voice-generate myvoice

# Use specific register, skip review
/voice-generate myvoice --register casual --review false

# Generate without learning snapshots
/voice-generate myvoice --learn false
```

## What This Does

1. Loads voice profile and selected register
2. Asks for source material (notes, topic, outline)
3. Frames source material as "raw notes to think through"
4. Generates text using Opus with full voice features
5. Auto-fixes hard failures (banned phrases, em dashes)
6. Dispatches prose and craft review agents (if --review)
7. Presents advisory tables for user decisions
8. Saves snapshots (if --learn)

## Source Material

Provide your source material when prompted. Best results
when framed as rough notes or ideas you're thinking through.
The skill automatically reframes input as raw notes unless
you explicitly request otherwise.

## Skill Invocation

```
Skill(scribe:voice-generate)
```

---

**Source:** [`athola/claude-night-market`](https://github.com/athola/claude-night-market) → `plugins/scribe/commands/voice-generate.md`
