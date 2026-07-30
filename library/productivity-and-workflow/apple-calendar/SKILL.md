---
name: apple-calendar
description: "Read and create Calendar.app events through a local macOS helper. Use when the user wants to inspect Apple Calendar calendars, summarize a day, check upcoming events, or create a new Calendar.app event from Codex."
category: productivity-and-workflow
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/matk0shub/apple-productivity-mcp/skills/apple-calendar/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/matk0shub/apple-productivity-mcp/skills/apple-calendar/SKILL.md
---


# Apple Calendar

## Overview

Use this skill to work with the local macOS Calendar app through the bundled helper at `../../scripts/apple_calendar.py`. The helper now uses an EventKit/Swift backend for data operations. Prefer the quick commands `today`, `tomorrow`, `agenda`, `free`, and `add` over lower-level calls unless you need raw JSON or direct lifecycle operations like `update-event`, `delete-event`, reminder changes, or `.ics` export/import.

## Workflow

1. Confirm the task is meant for Apple Calendar on macOS, not Google Calendar or Outlook.
2. Never run Calendar helper commands in parallel. The helper now serializes access to Calendar.app, and parallel calls only add latency.
3. For daily summaries, start with `today` or `tomorrow`. These default to the configured personal calendars in `../../config.json` instead of scanning every subscribed calendar.
4. Use `agenda` or `list-events` only when you need a specific date window or raw JSON payload.
5. Normalize relative dates into exact local timestamps before reasoning about conflicts or creating an event.
6. Prefer `add --if-free` for new events so overlapping slots are blocked unless the user explicitly wants a conflict.
7. For changing an existing event, use `find-events` first when you do not already have the event `uid`.

## Commands

List calendars and configured aliases:

```bash
/usr/bin/python3 ../../scripts/apple_calendar.py list-calendars
```

Today's agenda across the configured personal calendars:

```bash
/usr/bin/python3 ../../scripts/apple_calendar.py today
```

Tomorrow's agenda:

```bash
/usr/bin/python3 ../../scripts/apple_calendar.py tomorrow
```

List one day's events from a named calendar or alias:

```bash
/usr/bin/python3 ../../scripts/apple_calendar.py list-events \
  --calendar "prace" \
  --date today
```

Human-readable agenda for a specific day:

```bash
/usr/bin/python3 ../../scripts/apple_calendar.py agenda \
  --date 2026-03-27
```

Find free windows:

```bash
/usr/bin/python3 ../../scripts/apple_calendar.py free \
  --date today \
  --slot-minutes 30
```

Quick-add a new event with conflict protection:

```bash
/usr/bin/python3 ../../scripts/apple_calendar.py add \
  --calendar "doma" \
  --title "Design Review" \
  --date tomorrow \
  --start-time 15:00 \
  --duration-minutes 30 \
  --location "Zoom" \
  --notes "Bring the launch checklist." \
  --if-free
```

Find an event by title and day:

```bash
/usr/bin/python3 ../../scripts/apple_calendar.py find-events \
  --calendar doma \
  --title "Stolní Tenis" \
  --date today
```

Update an event:

```bash
/usr/bin/python3 ../../scripts/apple_calendar.py update-event \
  --calendar doma \
  --title "Stolní Tenis" \
  --date today \
  --set-location "Velká nad Veličkou 276"
```

Replace reminders:

```bash
/usr/bin/python3 ../../scripts/apple_calendar.py set-reminder \
  --calendar doma \
  --title "Stolní Tenis" \
  --date today \
  --minutes-before 30
```

Clear reminders:

```bash
/usr/bin/python3 ../../scripts/apple_calendar.py clear-reminders \
  --calendar doma \
  --title "Stolní Tenis" \
  --date today
```

Export to `.ics`:

```bash
/usr/bin/python3 ../../scripts/apple_calendar.py export-ics \
  --calendar doma \
  --date tomorrow \
  --days 1 \
  --output /tmp/my-events.ics
```

Import from `.ics`:

```bash
/usr/bin/python3 ../../scripts/apple_calendar.py import-ics \
  --calendar doma \
  --input /tmp/my-events.ics \
  --if-free
```

Delete an event:

```bash
/usr/bin/python3 ../../scripts/apple_calendar.py delete-event \
  --calendar doma \
  --title "Stolní Tenis" \
  --date today
```

## Safety

- Treat `add` and `create-event` as write operations.
- Do not invent calendar names. Use the exact name or alias returned by `list-calendars`.
- The helper serializes Calendar.app access with a lock and timeout; avoid parallel tool calls into the helper.
- Use `--if-free` by default for new events. Use `--allow-conflict` only when the user explicitly wants an overlapping event.
- Duplicate detection defaults to `title+start+end`. Set `--dedupe-by none` only when a true duplicate is intended.
- macOS may prompt for Calendar automation access the first time the helper runs.

## Output Conventions

- Use exact dates and local times in the response.
- Summaries should explain why a window is free or blocked instead of dumping raw JSON.
- When creating an event, echo the final title, calendar, start, end, and any location or notes that were applied.
- When `today`, `tomorrow`, `agenda`, or `free` is sufficient, prefer those outputs over raw JSON.

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/matk0shub/apple-productivity-mcp/skills/apple-calendar/SKILL.md`
