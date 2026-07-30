# Millrace Launch Video Reference

This reference distills the local planning docs that live next to this plugin:

- `/Users/timinator/Desktop/TODO/01-remotion-implementation-plan.md`
- `/Users/timinator/Desktop/TODO/02-claude-code-build-spec.md`
- `/Users/timinator/Desktop/TODO/03-video-structure-and-asset-schema.md`

## Core Goal

Build a repeatable, code-driven launch video pipeline for Millrace that communicates:

- hands-off autonomy
- configurable human-in-the-loop intervention
- escalation and recovery behavior
- quality and auditability

The video system should not depend on a perfect full-length screen recording. It should render from structured inputs first and accept real footage later.

## Narrative Guardrails

Emphasize:

- autonomy without opacity
- intervention without constant babysitting
- long-running work without dead air
- quality and auditability over raw speed

Avoid:

- speed-first framing
- cinematic gimmicks
- fake AI magic visuals
- minute-by-minute literal replay of a full run

## Required V1 Deliverables

- `MillraceLaunch16x9` composition
- `MillraceLaunch9x16` composition
- shared input schema
- sample run data
- sample event timeline
- overlays for:
  - current stage
  - elapsed timer
  - escalation ladder
  - autonomy or HITL status
  - audit or result badge
  - lower-third explanation copy
- terminal or log replay layer, or placeholder footage layer
- one render command per target
- README with usage

## Recommended Project Shape

```text
src/
  Root.tsx
  compositions/
    MillraceLaunch.tsx
    MillraceLaunchVertical.tsx
    LaunchThumbnail.tsx
  components/
    StageBadge.tsx
    Timer.tsx
    EscalationLadder.tsx
    AuditBadge.tsx
    LowerThird.tsx
    TerminalReplay.tsx
    EventCallout.tsx
  lib/
    schema.ts
    calculateMetadata.ts
    timing.ts
    formatting.ts
  data/
    sample-run.json
    sample-events.json
```

## Input Model

Build around one top-level props object that includes:

- `profile`
- `title`
- `subtitle`
- `buildTarget`
- `commit`
- `elapsedSeconds`
- `footageMode`
- `footageSrc`
- `mode.autonomy`
- `mode.humanInLoopAvailable`
- `finalStatus`
- `events`

Recommended event fields:

- `atSeconds`
- `kind`
- `label`
- `details`
- `stage`
- `escalationLevel`
- `status`

Recommended `kind` values:

- `launch`
- `health-pass`
- `stage-change`
- `build-start`
- `escalation`
- `human-intervention`
- `recovery`
- `audit-pass`
- `complete`

## Scene Structure

Default order:

1. Cold open
2. Launch and health gate
3. Autonomous work
4. Escalation ladder
5. Recovery
6. Completion audit
7. End card

Use:

- `<Series>` for the section-to-section story
- `<Sequence>` for overlays and local entrances inside scenes

## Footage Modes

Support all three without architectural forks:

- `footageMode: "none"` for terminal or log replay only
- `footageMode: "placeholder"` for mock or stock footage
- `footageMode: "real"` for actual capture

The same event data and overlays should still drive all modes.

## Render Profiles

At minimum:

- `youtube-16x9`
- `social-9x16`

Differences between profiles should be data-driven:

- aspect ratio
- safe-area padding
- type scale
- overlay placement

Do not fork the narrative or event logic just because the aspect ratio changes.

## Success Criteria

The system is successful when:

- it renders without real footage
- it is driven by structured inputs
- 16:9 and 9:16 both work
- the escalation ladder is easy to understand
- the timer reflects real elapsed time, not playback time
- changing run inputs predictably changes the output
