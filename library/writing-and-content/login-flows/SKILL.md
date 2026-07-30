---
name: login-flows
description: "Common login automation patterns for web apps using Playwright"
category: writing-and-content
source_repo: andrewyng/context-hub
source_path: "content/playwright-community/skills/login-flows/SKILL.md"
source_url: https://github.com/andrewyng/context-hub/blob/HEAD/content/playwright-community/skills/login-flows/SKILL.md
---


# Login Flow Patterns for Playwright

Reusable patterns for automating login flows in end-to-end tests.

## Basic Username/Password Login

```typescript
import { Page } from '@playwright/test';

async function login(page: Page, username: string, password: string) {
  await page.goto('/login');
  await page.fill('[name="username"]', username);
  await page.fill('[name="password"]', password);
  await page.click('button[type="submit"]');
  await page.waitForURL('/dashboard');
}
```

## OAuth / SSO Login

For OAuth flows that redirect to an external provider:

```typescript
async function loginWithOAuth(page: Page) {
  await page.goto('/login');
  await page.click('text=Sign in with Google');

  // Handle the OAuth popup or redirect
  await page.fill('input[type="email"]', process.env.TEST_EMAIL!);
  await page.click('text=Next');
  await page.fill('input[type="password"]', process.env.TEST_PASSWORD!);
  await page.click('text=Next');

  // Wait for redirect back to app
  await page.waitForURL('**/dashboard');
}
```

## Persisting Auth State (storageState)

Avoid logging in before every test by saving and reusing browser state:

```typescript
// global-setup.ts — runs once before all tests
import { chromium } from '@playwright/test';

async function globalSetup() {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  await page.goto('/login');
  await page.fill('[name="username"]', 'testuser');
  await page.fill('[name="password"]', 'testpass');
  await page.click('button[type="submit"]');
  await page.waitForURL('/dashboard');

  // Save signed-in state
  await page.context().storageState({ path: './auth.json' });
  await browser.close();
}

export default globalSetup;
```

Then in `playwright.config.ts`:

```typescript
export default defineConfig({
  globalSetup: './global-setup.ts',
  use: {
    storageState: './auth.json',
  },
});
```

## MFA / 2FA Handling

For test environments with TOTP-based 2FA:

```typescript
import { authenticator } from 'otplib';

async function loginWithMFA(page: Page, secret: string) {
  await login(page, 'user', 'pass');

  // Generate TOTP code
  const code = authenticator.generate(secret);
  await page.fill('[name="totp"]', code);
  await page.click('button[type="submit"]');
  await page.waitForURL('/dashboard');
}
```

## Tips

- Always use `storageState` to avoid repeated logins — it's the single biggest speedup for E2E suites
- Use environment variables for credentials, never hardcode them
- For CI, consider a dedicated test user with stable credentials
- Use `page.waitForURL()` instead of arbitrary `waitForTimeout()` after login

---

**Source:** [`andrewyng/context-hub`](https://github.com/andrewyng/context-hub) → `content/playwright-community/skills/login-flows/SKILL.md`
