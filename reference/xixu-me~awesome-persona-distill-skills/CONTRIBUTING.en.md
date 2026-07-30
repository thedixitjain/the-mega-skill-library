<!-- Harvested from https://github.com/xixu-me/awesome-persona-distill-skills/blob/HEAD/CONTRIBUTING.en.md -->
> **Source:** [`xixu-me/awesome-persona-distill-skills`](https://github.com/xixu-me/awesome-persona-distill-skills) → `CONTRIBUTING.en.md`

# Contributing Guide

Thank you for contributing to this repository.

This repository collects Agent Skills centered on "persona distillation", with emphasis on:

- Distilling expressive style, judgment patterns, or interaction habits from people, relationships, conversations, works, or digital traces.
- Turning a personal perspective, relationship experience, or methodology into a reusable skill.
- Keeping a clear thematic boundary so each entry fits an awesome-style list instead of a generic AI tools directory.

## Welcome Contributions

- Add links to skill repositories that fit the theme.
- Fix dead links, repository names, descriptions, or category placement.
- Improve wording in the READMEs so categories and descriptions are more accurate.

For new inclusion requests, the issue form is the only public intake path. After a maintainer reviews the request and adds the `approved` label, the workflow will generate a pull request automatically.

## Contributions We Discourage

- Generic AI tools, prompt collections, or resource directories that are only loosely related to persona distillation.
- Projects without a public repository, with inaccessible content, or with too little public material to evaluate.
- Obvious duplicates, thin repackaging, or entries that heavily overlap with existing items without adding value.
- Projects primarily intended for privacy invasion, harassment, impersonation of real people, or consent avoidance.
- Pure advertising copy or submissions that require readers to click through before they can understand the basics.

## Before You Submit

Please try to make sure each entry meets these standards:

- The repository is publicly accessible.
- The project is relevant to this list and fits the chosen category.
- The Chinese and English names each use the project's commonly used name in that language.
- The description stays within one sentence and explains what is being distilled, from what source, or for what purpose, without promotional wording.
- If the project fits a different category better, submit it directly in the more appropriate section.

## Entry Writing Reference

If you are requesting a new inclusion, use the format and tone below when filling in the bilingual names and descriptions in the issue form. After a maintainer adds the `approved` label, the workflow will use that content to generate the README entry automatically.

If you are directly revising an existing entry, keep using the current README list format:

```md
- [Project Name](https://github.com/owner/repo) - One sentence describing what the project distills, where it comes from, or what it is for.
```

Suggested writing style:

- Say what it is before saying what it does.
- Be specific instead of using vague praise like "high quality", "powerful", or "useful".
- Match the tone and level of detail of nearby entries.

## Submission Process

1. If you want to request a new inclusion, start with the issue form and fill in the repository link, category, bilingual names, bilingual descriptions, and rationale.
2. After review, a maintainer may add the `approved` label to the issue, and the workflow will generate a pull request automatically.
3. If you are fixing existing entries, documentation, or broken links, you can still fork the repository, create a branch, and open a pull request directly.
4. For direct PR changes, update the affected content in both [`README.md`](./README.md) and [`README.en.md`](./README.en.md). If your change affects inclusion standards or collaboration rules, update the relevant contribution guide as well.
5. Run formatting locally, then check that entry style, links, and wording remain consistent with the current content.

## Local Check

Before submitting, run:

```bash
bun install
bun run format
```

Then double-check:

- Markdown list formatting matches the existing entries.
- Links are publicly accessible.
- Names and descriptions are accurate and non-promotional.

## PR Notes

To help review move faster, please explain:

- What you added or changed.
- Which category it belongs to and why.
- If it is a new project, how it relates to the persona distillation theme.
- If there are similar entries already listed, how this one differs from them.

## Communication

- New inclusion requests should go through the issue form instead of a direct PR.
- Small fixes, updates to existing entries, and broken-link fixes can go straight to a PR.
- If you plan to restructure categories, rewrite many descriptions, or noticeably expand the inclusion scope, it is better to open an issue first to explain the idea.
- Keep discussion focused on thematic boundaries, readability, and reader value.
