---
name: awesome-cursorrules-sveltekit-typescript-guide-cursorrules-promp
description: "Cursor rules for SvelteKit development with TypeScript integration."
category: prompt-engineering
source_repo: PatrickJS/awesome-cursorrules
source_path: "rules/sveltekit-typescript-guide-cursorrules-prompt-file.mdc"
source_url: https://github.com/PatrickJS/awesome-cursorrules/blob/HEAD/rules/sveltekit-typescript-guide-cursorrules-prompt-file.mdc
---

You are an expert in Svelte 5, SvelteKit, TypeScript, Supabase, Drizzle and modern web development.

Key Principles

Code Style and Structure
Naming Conventions
TypeScript Usage
Svelte Runes
UI and Styling
Shadcn Color Conventions
SvelteKit Project Structure
Component Development
State Management

Use classes for complex state management (state machines):
```typescript
// counter.svelte.ts
class Counter {
  count = $state(0);
  incrementor = $state(1);
  increment() {
    this.count += this.incrementor;
  }
  resetCount() {
    this.count = 0;
  }
  resetIncrementor() {
    this.incrementor = 1;
  }
}
export const counter = new Counter();

---

**Source:** [`PatrickJS/awesome-cursorrules`](https://github.com/PatrickJS/awesome-cursorrules) → `rules/sveltekit-typescript-guide-cursorrules-prompt-file.mdc`
