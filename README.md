<div align="center">

# 🧠 The Mega Skill Library

### The largest open catalog of AI agent skills on GitHub

**35,802 ready-to-use skills, subagents, slash commands, prompts and rules** —
harvested, deduplicated and organized from **186 repositories** across the
Claude Code / Cursor / Codex / Copilot skill ecosystem, so you never have to
write one from scratch again.

[![Validate catalog](https://github.com/thedixitjain/the-mega-skill-library/actions/workflows/validate-catalog.yml/badge.svg)](https://github.com/thedixitjain/the-mega-skill-library/actions/workflows/validate-catalog.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![GitHub stars](https://img.shields.io/github/stars/thedixitjain/the-mega-skill-library?style=social)](https://github.com/thedixitjain/the-mega-skill-library/stargazers)
![Assets](https://img.shields.io/badge/assets-35%2C802-informational)
![Source repos](https://img.shields.io/badge/sourced%20from-186%20repos-informational)
![Categories](https://img.shields.io/badge/categories-22-informational)

[Browse the index](INDEX.md) · [Search the catalog](CATALOG.tsv) · [Quick start](#-quick-start) · [Credits](CREDITS.md) · [Contribute](CONTRIBUTING.md)

</div>

---

## Why this exists

AI coding agents (Claude Code, Cursor, Codex, Copilot…) got a superpower this
year: **Skills** — small, self-contained instruction packs that teach an agent
how to do one thing well (write a spec, review a PR, design an API, run a
security audit, format a resume). The problem: they're scattered across
hundreds of individual GitHub repos, half-documented, and impossible to
search in one place.

This repo fixes that. Every skill-bearing repo in the ecosystem, pulled
together, deduplicated, categorized, and made **greppable in one file**.
Whether you're a student who just discovered agent skills exist, or a staff
engineer wiring up a fleet of subagents in production — the same catalog
works for you.

## What's inside

| Kind | Count | Where | What it is |
|---|---:|---|---|
| 🧩 Agent Skills | **18,681** | [`library/`](library) | Full `SKILL.md` bundles (+ scripts, templates, references) |
| 🤖 Subagents | **2,888** | [`agents/`](agents) | Specialized agent role definitions |
| ⚡ Slash Commands | **2,773** | [`commands/`](commands) | `/command` shortcuts |
| 💬 Prompts | **10,074** | [`prompts/`](prompts) | System prompts, prompt corpora, leaked prompts |
| 📏 Rules | **1,386** | [`rules/`](rules) | `CLAUDE.md` / `AGENTS.md` / `.cursorrules` exemplars |
| 📖 Reference | **543** | [`reference/`](reference) | Awesome-lists, cheatsheets, handbooks (verbatim) |

## 🚀 Quick start

```bash
git clone https://github.com/thedixitjain/the-mega-skill-library.git
```

Pick the path that matches how much you already know:

<details open>
<summary><b>🎓 New to agent skills?</b> — one command, zero config</summary>

Copy the router skill. It searches the other 35,801 assets for you — nothing
else loads into context or slows your agent down.

```bash
cp -r the-mega-skill-library/master-skill ~/.claude/skills/master-skill-library
```

Now just talk to Claude Code normally. When a task matches something in the
library, it finds the right skill and uses it automatically. That's it —
you're done.

</details>

<details>
<summary><b>💼 Know exactly what you want?</b> — install specific skills</summary>

Claude Code reads every installed skill's frontmatter at startup, so only
install what you'll actually use — dozens, not thousands.

```bash
cp -r the-mega-skill-library/library/engineering-core/tdd-guide ~/.claude/skills/
```

Project-only instead of global? Copy into `<project>/.claude/skills/` instead
of `~/.claude/skills/`.

</details>

<details>
<summary><b>⌨️ Power user?</b> — grep it, script it, pipe it</summary>

```bash
grep -i "pdf" CATALOG.tsv
awk -F'\t' '$2=="security-and-compliance" && $1=="skill"' CATALOG.tsv
grep -i "code review" CATALOG.tsv | awk -F'\t' '$1=="agent"' | cut -f3,6
```

`CATALOG.tsv` is one row per asset: `kind · category · name · path · source_repo · description`.

</details>

<details>
<summary><b>🛠️ Using Cursor, Codex, Copilot, or something else?</b></summary>

Most files here are plain Markdown with YAML frontmatter — portable by design.
`library/` bundles follow the Agent Skills spec (works with any harness that
supports it); `rules/` files map directly to `.cursorrules` / `AGENTS.md` /
custom instructions; `prompts/` and `commands/` are copy-paste text you can
drop into any system-prompt or slash-command config.

</details>

## 🗂️ Browse by category

22 categories, auto-sorted by asset count. Click through for the full
browsable table of every skill/agent/command/prompt in that category.

| Category | Assets | Covers |
|---|---:|---|
| 📦 [General purpose](_index/general-purpose.md) | 5,575 | Uncategorized / cross-cutting |
| 🤖 [AI agents & harness](_index/ai-agents-and-harness.md) | 4,583 | Agent design, orchestration, subagents, context engineering |
| 💬 [Prompt engineering](_index/prompt-engineering.md) | 2,868 | Prompt techniques, system prompts, optimizers, persona design |
| ⚙️ [Engineering core](_index/engineering-core.md) | 2,805 | Refactoring, debugging, review, architecture, git, TDD |
| 🔬 [Research & academic](_index/research-and-academic.md) | 2,483 | Literature review, papers, journals, grants, regulatory science |
| ☁️ [DevOps & infra](_index/devops-and-infra.md) | 1,605 | Docker, K8s, Terraform, CI/CD, cloud, observability, SRE |
| 🔒 [Security & compliance](_index/security-and-compliance.md) | 1,604 | AppSec, pentest, OSINT, threat modeling, SOC2/ISO/GDPR |
| 📣 [Marketing & growth](_index/marketing-and-growth.md) | 1,584 | SEO/AEO, ads, CRO, social, campaigns, growth loops |
| 🗄️ [Backend & data](_index/backend-and-data.md) | 1,583 | APIs, databases, schemas, queues, caching, pipelines |
| 🔌 [MCP & integrations](_index/mcp-and-integrations.md) | 1,524 | MCP servers/clients, third-party integrations, browser automation |
| 🧪 [Testing & QA](_index/testing-and-qa.md) | 1,506 | Test generation, E2E, coverage, QA process, browser testing |
| 🎨 [Frontend & design](_index/frontend-and-design.md) | 1,359 | UI/UX, design systems, CSS, React, accessibility |
| ✍️ [Writing & content](_index/writing-and-content.md) | 1,345 | Copywriting, editing, humanizing, translation, narrative |
| 📝 [Docs & knowledge mgmt](_index/docs-and-knowledge-mgmt.md) | 1,158 | Documentation, ADRs, technical writing, note systems |
| 💼 [Business & finance](_index/business-and-finance.md) | 1,152 | Finance, pricing, legal, sales, HR, exec advisory |
| 🎬 [Media & creative](_index/media-and-creative.md) | 778 | Video, image, slides/PPTX, audio, game dev, generative art |
| 📊 [Data science & ML](_index/data-science-and-ml.md) | 722 | ML/DL, training, fine-tuning, evaluation, statistics |
| 📋 [Product & PM](_index/product-and-pm.md) | 473 | PRDs, roadmaps, user stories, discovery, analytics |
| 📱 [Mobile & platform](_index/mobile-and-platform.md) | 398 | iOS/Android/Flutter, desktop, extensions, BI platforms |
| ⚡ [Productivity & workflow](_index/productivity-and-workflow.md) | 353 | Planning, automation, meetings, scaffolds, coaching |
| 📚 [RAG, memory & knowledge](_index/rag-memory-knowledge.md) | 333 | RAG, vector search, embeddings, agent memory, knowledge graphs |
| 🧩 [Skill authoring meta](_index/skill-authoring-meta.md) | 11 | Creating, testing, auditing and improving skills themselves |

Full index with descriptions and navigation: **[INDEX.md](INDEX.md)**

## 📁 Repo layout

```
the-mega-skill-library/
├── INDEX.md                 master index — start here
├── CATALOG.tsv               one row per asset — grep/awk this
├── master-skill/SKILL.md     router skill — install this one, it finds the rest
├── library/<category>/<slug>/SKILL.md    18,681 Agent Skills (+ bundled resources)
├── agents/<category>/<slug>.md           2,888 subagent definitions
├── commands/<category>/<slug>.md         2,773 slash commands
├── prompts/<category>/<slug>.md          10,074 system prompts / corpora
├── rules/<category>/<slug>.md            1,386 CLAUDE.md / AGENTS.md / .cursorrules
├── reference/<owner~repo>/...            543 awesome-lists, cheatsheets, handbooks
├── _index/<category>.md      per-category browsable tables
└── _logs/                    harvest run logs
```

> The raw upstream git clones used to build this (`_sources/`, ~9 GB, 186 repos)
> aren't part of this repository — only the curated, deduplicated output above
> is published. See [Refreshing](#-refreshing--regenerating) below.

## 🔎 Provenance, credits & licensing

**This is a curated aggregation, not original work.** Every skill, agent,
command, prompt and rules file was written by its original author — full
attribution for all 237 source repositories lives in **[CREDITS.md](CREDITS.md)**,
linked directly to each one's GitHub page.

Every single harvested file also carries `source_repo`, `source_path` and
`source_url` in its own frontmatter, plus a human-readable Source footer
linking upstream — open any file to see exactly where it came from. Duplicates
across repos were collapsed by content hash, keeping the most authoritative
copy (official vendor repos first, then by star count); collapsed copies are
listed in each file's "Also appears in" footer, so nothing is silently lost.

This repo's own layer — the categorization, indexing, catalog, router skill,
and documentation — is [MIT licensed](LICENSE). The 35,802 harvested files
themselves come from 186 different repositories (plus 51 more kept as
reference material) under their **own original licenses** — check the
upstream repo (linked in every file's footer, and in [CREDITS.md](CREDITS.md))
before redistributing or using an individual file commercially.

## 🔄 Refreshing / regenerating

The curated buckets here (`library/`, `agents/`, `commands/`, `prompts/`,
`rules/`, `reference/`, `_index/`, `CATALOG.tsv`) were generated once from
local clones of all 186 source repos. To regenerate: re-clone each repo listed
in `CATALOG.tsv` / `_index/by-source-repo.md`, then re-run a categorize →
dedup-by-hash → catalog pipeline against them. See [CONTRIBUTING.md](CONTRIBUTING.md)
if you want to help formalize that pipeline into a script others can run.

## 🤝 Contributing

Found a skill-bearing repo that isn't here yet? Found a broken path or a
duplicate that should've been collapsed? PRs and issues are very welcome —
see **[CONTRIBUTING.md](CONTRIBUTING.md)** for the frontmatter convention and
how to add an entry to `CATALOG.tsv`.

## ❓ FAQ

<details>
<summary>What's the difference between a "skill", "agent", "command", "prompt" and "rule"?</summary>

- **Skill** — a full `SKILL.md` bundle (+ optional scripts/templates) an agent loads on demand for one task.
- **Agent / subagent** — a role definition (persona + tools + instructions) spawned to handle a sub-task.
- **Command** — a `/slash-command` shortcut that expands to a fixed prompt or workflow.
- **Prompt** — a standalone system prompt or prompt corpus, not packaged as a skill.
- **Rule** — a `CLAUDE.md` / `AGENTS.md` / `.cursorrules` style always-on instruction file.
</details>

<details>
<summary>Will installing the router skill slow down my agent or eat my context window?</summary>

No. The router (`master-skill/`) is the only thing that ever loads, and it's
one small file. It searches `CATALOG.tsv` on demand and reads just the one or
two matching files per task — the other 35,800 assets sit untouched on disk.
</details>

<details>
<summary>Can I use this commercially?</summary>

The curation layer is MIT. Individual harvested files retain their original
upstream license — check the source before commercial use of a specific file.
See [Provenance & licensing](#-provenance--licensing).
</details>

<details>
<summary>My favorite skill repo isn't in here — why?</summary>

Either it hasn't been discovered yet, or it didn't fit the harvest criteria
(skill-shaped content: `SKILL.md`, subagent defs, slash commands, system
prompts, or rules files). Open a PR — see [Contributing](#-contributing).
</details>

## ⭐ Support

If this saved you time, **star the repo** — it's the main way other people
find it. Issues, PRs, and "hey you should add X" suggestions are all welcome.

<div align="center">

[![Star History Chart](https://api.star-history.com/svg?repos=thedixitjain/the-mega-skill-library&type=Date)](https://star-history.com/#thedixitjain/the-mega-skill-library&Date)

Made by [**@thedixitjain**](https://github.com/thedixitjain) · [MIT Licensed](LICENSE)

</div>
