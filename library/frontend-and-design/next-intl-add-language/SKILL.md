---
name: next-intl-add-language
description: "Add new language to a Next.js + next-intl application"
category: frontend-and-design
source_repo: github/awesome-copilot
source_path: "skills/next-intl-add-language/SKILL.md"
source_url: https://github.com/github/awesome-copilot/blob/HEAD/skills/next-intl-add-language/SKILL.md
---
This is a guide to add a new language to a Next.js project using next-intl for internationalization,

- For i18n, the application uses next-intl.
- All translations are in the directory `./messages`.
- The UI component is `src/components/language-toggle.tsx`.
- Routing and middleware configuration are handled in:
  - `src/i18n/routing.ts`
  - `src/middleware.ts`

When adding a new language:

- Translate all the content of `en.json` to the new language. The goal is to have all the JSON entries in the new language for a complete translation.
- Add the path in `routing.ts` and `middleware.ts`.
- Add the language to `language-toggle.tsx`.

---

**Source:** [`github/awesome-copilot`](https://github.com/github/awesome-copilot) → `skills/next-intl-add-language/SKILL.md`
