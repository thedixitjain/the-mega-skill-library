---
name: remotion-video-builder
description: "Use when building, reviewing, or refactoring a Remotion project, especially parameterized launch or demo videos with shared props schemas, calculateMetadata, Sequence and Series timing, multiple aspect ratios, terminal or footage layers, and render scripts. Prefer official Remotion docs or MCP for API details because package behavior may change."
category: media-and-creative
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/tim-osterhus/codex-remotion-plugin/skills/remotion-video-builder/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/tim-osterhus/codex-remotion-plugin/skills/remotion-video-builder/SKILL.md
---


# Remotion Video Builder

Your Remotion knowledge may be stale. When exact API behavior matters, prefer the official `remotion-documentation` MCP server or the docs at [remotion.dev](https://www.remotion.dev/).

## Start Here

- If the project does not exist yet, scaffold it with `npx create-video@latest` and prefer the blank template.
- Keep every `remotion` and `@remotion/*` package on the exact same version and avoid caret ranges.
- Standard entry shape:
  - `src/index.ts` calls `registerRoot()`
  - `src/Root.tsx` registers all videos with `<Composition>` or `<Still>`

## Build Order

1. Model the input contract first:
   - top-level props schema
   - timeline or event data
   - render profile
2. Define shared props with `zod` and pass the schema to each `<Composition>`.
3. Use `calculateMetadata` to derive `durationInFrames`, `width`, `height`, transformed props, and `defaultOutName`.
4. Build the scene structure with `<Series>` for narrative order and `<Sequence>` for overlays, entrances, footage windows, and callouts.
5. In Remotion v4.x projects, explicitly set `premountFor` on `<Sequence>` elements that need assets loaded before they appear.
6. Add sample data and render scripts before polishing animation.

## Defaults And Rules

- Default to `fps={30}` and `1920x1080` for landscape unless the brief says otherwise.
- Use `AbsoluteFill` for layering.
- Use `staticFile()` for anything coming from `public/`.
- Use `useCurrentFrame()` and `useVideoConfig()` for frame-based logic.
- Prefer subtle motion:
  - `spring()` with high damping
  - `interpolate()` with clamping
- Do not use `Math.random()`. Use `random(seed)` from `remotion`.
- Keep text animation simple and legible.
- Keep landscape and vertical outputs on the same business logic unless the brief truly requires divergence.

## Parameterized Video Checklist

- One shared top-level `z.object()` schema
- `defaultProps` matching the component prop shape
- `calculateMetadata` returning dynamic duration or dimensions when inputs require it
- Sample JSON or TypeScript data for local preview
- Render scripts for every target output

## Footage Strategy

Support at least these modes when footage is optional:

- `none`
- `placeholder`
- `real`

The timeline and overlays should still render when no real footage exists.

## Millrace Launch Video

If the request is about Millrace or the launch video pipeline, read [references/millrace-launch-video.md](references/millrace-launch-video.md) before implementing.

## References

- [references/remotion-core.md](references/remotion-core.md)
- [references/millrace-launch-video.md](references/millrace-launch-video.md)

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/tim-osterhus/codex-remotion-plugin/skills/remotion-video-builder/SKILL.md`
