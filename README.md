# 🧠 The Mega Skill Library

**35,802 agent skills, subagents, slash commands, system prompts and rules files**,
harvested and organized from **186 GitHub repositories** — curated from the
wider agent-skills ecosystem (Claude Code, Codex, Cursor, and friends).

- **Browse:** [INDEX.md](INDEX.md)
- **Search (scripts/grep):** [CATALOG.tsv](CATALOG.tsv)
- **Let Claude route for you:** [master-skill/SKILL.md](master-skill/SKILL.md)
- **License:** [MIT](LICENSE) for the curation layer — see [Provenance](#provenance) below for the harvested files themselves

```bash
git clone https://github.com/thedixitjain/the-mega-skill-library.git
```

## Layout

```
skills/
├── INDEX.md                 master index — start here
├── CATALOG.tsv              one row per asset (grep this)
├── master-skill/SKILL.md    router skill — install this one, it finds the rest
├── library/<category>/<slug>/SKILL.md    18,681 Agent Skills (+ bundled resources)
├── agents/<category>/<slug>.md           2,888 subagent definitions
├── commands/<category>/<slug>.md         2,773 slash commands
├── prompts/<category>/<slug>.md          10,074 system prompts / corpora
├── rules/<category>/<slug>.md            1,386 CLAUDE.md / AGENTS.md / .cursorrules
├── reference/<owner~repo>/...            543 awesome-lists, cheatsheets, handbooks
├── _index/<category>.md     per-category browsable tables
└── _logs/                   harvest run logs
```

> The raw upstream git clones used to build this (`_sources/`, ~9 GB, 186 repos)
> are not part of this repository — only the curated, deduplicated output above is
> published. See [Refreshing](#refreshing) if you want to regenerate everything
> from scratch on your own machine.

## How to use it

### Option A — install the router (recommended)

Copy one folder; Claude searches the rest on demand. Nothing else eats context.

```bash
cp -r "master-skill" ~/.claude/skills/master-skill-library
```

Then just work normally — when a task matches something in the library, Claude
greps `CATALOG.tsv`, loads the single relevant `SKILL.md`, and applies it.

> Edit the `Library root` path inside `master-skill/SKILL.md` if you move this folder.

### Option B — install specific skills

Claude Code loads every skill's frontmatter at startup, so install only what you
actually want (dozens, not thousands):

```bash
cp -r "library/engineering-core/tdd-guide" ~/.claude/skills/
```

Project-scoped instead of global: copy into `<project>/.claude/skills/`.

### Option C — grep it directly

```bash
grep -i "pdf" CATALOG.tsv
awk -F'\t' '$2=="security-and-compliance" && $1=="skill"' CATALOG.tsv
```

## Provenance

Every file carries `source_repo`, `source_path` and `source_url` frontmatter plus a
Source footer linking upstream. Duplicates were collapsed by content hash, keeping
the most authoritative copy (official vendor repos first, then by star count); the
collapsed copies are listed in each file's "Also appears in" footer.

**Licensing:** these files come from 186 different repositories under their
own licenses. Check the upstream repo before redistributing or using commercially.

## Refreshing

The curated buckets in this repo (`library/`, `agents/`, `commands/`, `prompts/`,
`rules/`, `reference/`, `_index/`, `CATALOG.tsv`) were generated once from local
clones of all 186 source repos. To regenerate from scratch: re-clone each repo
listed in `CATALOG.tsv` / `_index/by-source-repo.md` under a local `_sources/`
folder, then re-run the categorization/dedup pipeline against it. Pull requests
that add newly-discovered skill repos are welcome — see Contributing below.

## Contributing

Found a skill-bearing repo that isn't here yet? Open a PR adding the files under
the right `library/<category>/`, `agents/<category>/`, etc., following the
existing frontmatter convention (`source_repo`, `source_path`, `source_url` +
a Source footer), and add a row to `CATALOG.tsv`.
