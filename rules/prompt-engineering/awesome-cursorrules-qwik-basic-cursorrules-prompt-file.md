---
name: awesome-cursorrules-qwik-basic-cursorrules-prompt-file
description: "Cursor rules for Qwik development with TypeScript and Vite integration."
category: prompt-engineering
source_repo: PatrickJS/awesome-cursorrules
source_path: "rules/qwik-basic-cursorrules-prompt-file.mdc"
source_url: https://github.com/PatrickJS/awesome-cursorrules/blob/HEAD/rules/qwik-basic-cursorrules-prompt-file.mdc
---

// Qwik.js Basic Setup (with TypeScript and Vite) .cursorrules

// Prefer functional components

const preferFunctionalComponents = true;

// Qwik.js best practices

const qwikBestPractices = [
  "Use $ suffix for lazy-loaded functions",
  "Utilize useSignal() for reactive state",
  "Implement useStore() for complex state objects",
  "Use useResource$() for data fetching",
  "Implement useTask$() for side effects",
  "Utilize useVisibleTask$() for browser-only code",
  "Leverage TypeScript for type safety",
  "Use Vite's fast HMR for development",
];

// Folder structure

const folderStructure = `
src/
  components/
  routes/
  global.css
  root.tsx
  entry.ssr.tsx
public/
vite.config.ts
tsconfig.json
`;

// Additional instructions

const additionalInstructions = `
1. Use TypeScript for all .ts and .tsx files
2. Implement proper error boundaries
3. Utilize Qwik City for routing when applicable
4. Use Qwik's built-in optimization features
5. Implement lazy-loading for improved performance
6. Follow Qwik's naming conventions and best practices
7. Use server$ for server-side code execution
8. Leverage Vite plugins for optimized builds
`;

---

**Source:** [`PatrickJS/awesome-cursorrules`](https://github.com/PatrickJS/awesome-cursorrules) → `rules/qwik-basic-cursorrules-prompt-file.mdc`
