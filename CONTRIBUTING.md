# Contributing to The Mega Skill Library

Thanks for wanting to help grow this. Two kinds of contributions are useful
here: **adding a new skill-bearing repo** you've found, and **fixing what's
already in the catalog** (broken links, wrong category, missed duplicate).

## Adding a new repo's skills

1. Pick the right bucket for what you're adding:
   - Full `SKILL.md` bundle → `library/<category>/<slug>/`
   - Subagent definition → `agents/<category>/<slug>.md`
   - Slash command → `commands/<category>/<slug>.md`
   - System prompt / corpus → `prompts/<category>/<slug>.md`
   - `CLAUDE.md` / `AGENTS.md` / `.cursorrules` → `rules/<category>/<slug>.md`
   - Awesome-list / cheatsheet / handbook (not skill-shaped) → `reference/<owner~repo>/...` (kept verbatim)

2. Pick a category from the 22 in [INDEX.md](INDEX.md) — closest fit wins.
   If genuinely nothing fits, use `general-purpose`.

3. Every file needs provenance frontmatter plus a footer, e.g.:

   ```markdown
   ---
   name: your-skill-slug
   description: One or two sentences, same as the original SKILL.md.
   source_repo: owner/repo
   source_path: path/inside/that/repo/SKILL.md
   source_url: https://github.com/owner/repo/blob/HEAD/path/inside/that/repo/SKILL.md
   ---

   <!-- original content, unmodified -->

   ---
   Source: [owner/repo](https://github.com/owner/repo) → `path/inside/that/repo/SKILL.md`
   ```

4. Add one row to `CATALOG.tsv` (tab-separated):

   ```
   kind<TAB>category<TAB>name<TAB>path<TAB>source_repo<TAB>description
   ```

5. If it's a genuine duplicate of something already in the catalog (same
   content, different repo), don't add a second copy — instead append a line
   to the existing file's "Also appears in" footer.

## Fixing something that's already here

- **Broken link / missing file**: open an issue or just fix it in a PR.
- **Wrong category**: move the file, update its row in `CATALOG.tsv`, and fix
  the two now-stale rows in the relevant `_index/<category>.md` files.
- **Should be deduped**: keep whichever copy is from the more authoritative
  source (official vendor repo first, then higher star count), fold the other
  into its "Also appears in" footer, remove the redundant catalog row.

## Ground rules

- Don't rewrite the harvested content itself — keep it verbatim from upstream
  (typo/format fixes to your *own* additions are fine, not to others' skills).
- Respect upstream licenses. If a repo's license clearly disallows
  redistribution, don't add it here — link to it from `_index/by-source-repo.md`
  instead.
- One logical change per PR (one new repo, or one batch of fixes) — makes
  review fast.

Questions or unsure where something fits? Open an issue and ask before doing
a big batch of work.
