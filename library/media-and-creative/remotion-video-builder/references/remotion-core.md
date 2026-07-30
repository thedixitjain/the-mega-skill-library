# Remotion Core Reference

Official sources used for this plugin:

- [Agent Skills](https://www.remotion.dev/docs/ai/skills)
- [Remotion MCP](https://www.remotion.dev/docs/ai/mcp)
- [System Prompt For LLMs](https://www.remotion.dev/docs/ai/system-prompt)
- [The fundamentals](https://www.remotion.dev/docs/the-fundamentals)
- [Composition docs](https://www.remotion.dev/docs/composition)
- [calculateMetadata()](https://www.remotion.dev/docs/calculate-metadata)
- [Sequence docs](https://www.remotion.dev/docs/sequence)
- [Series docs](https://www.remotion.dev/docs/series)
- [Premounting](https://www.remotion.dev/docs/player/premounting)
- [Agent Skills repo guidance](https://github.com/remotion-dev/skills)

## Setup

- Start new work with `npx create-video@latest`.
- The Remotion docs also mention that new projects can opt into Tailwind and Remotion skills during scaffolding.
- Remotion maintains official agent skills that can be installed with:

```bash
npx skills add remotion-dev/skills
```

## MCP

The official docs show a command-based MCP install using:

```json
{
  "mcpServers": {
    "remotion-documentation": {
      "command": "npx",
      "args": ["@remotion/mcp@latest"]
    }
  }
}
```

For Codex CLI, the equivalent manual setup is:

```bash
codex mcp add remotion-documentation -- npx @remotion/mcp@latest
```

## Project Shape

- `src/index.ts` should call `registerRoot()`.
- `src/Root.tsx` should register renderable outputs using `<Composition>` and optionally `<Still>`.
- A composition defines:
  - `id`
  - `component`
  - `durationInFrames`
  - `width`
  - `height`
  - `fps`

## Parameterized Compositions

- Install `zod` and define a top-level `z.object()` schema for props.
- Pass the schema to the `schema` prop on `<Composition>`.
- Keep `defaultProps` JSON-serializable and matched to the component prop shape.

## Dynamic Metadata

Use `calculateMetadata` when:

- duration depends on data
- dimensions depend on inputs
- props need preprocessing or fetching
- output naming should derive from inputs

Return only JSON-serializable data. Useful fields include:

- `durationInFrames`
- `width`
- `height`
- `fps`
- `props`
- `defaultOutName`

## Timing

- Use `<Series>` to stitch scenes one after another.
- Use `<Sequence>` to offset timed layers, overlays, and nested content.
- Local frame numbering resets inside a sequence.
- In current Remotion v4.x work, explicitly set `premountFor` where assets need time to load before they appear.

## Animation And Determinism

- Prefer `spring()` with restrained settings and high damping.
- Prefer `interpolate()` with clamped extrapolation.
- Avoid non-deterministic behavior. Do not use `Math.random()`; use `random(seed)`.

## Assets

- Use `staticFile()` for anything loaded from `public/`.
- Use `AbsoluteFill` for layered full-frame layouts.

## Rendering

Common CLI patterns:

```bash
npx remotion render MyComp
npx remotion still Thumbnail
```

## Versioning

Remotion's package README for `@remotion/mcp` notes that all `remotion` and `@remotion/*` packages should stay on the exact same version. Do not mix ranges loosely.
