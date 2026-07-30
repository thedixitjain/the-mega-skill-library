---
name: database-configuration
description: "Set up environment configuration files from templates with validation."
category: backend-and-data
source_repo: rohitg00/awesome-claude-code-toolkit
source_path: "plugins/env-manager/commands/env-setup.md"
source_url: https://github.com/rohitg00/awesome-claude-code-toolkit/blob/HEAD/plugins/env-manager/commands/env-setup.md
---
Set up environment configuration files from templates with validation.

## Steps

1. Scan for environment template files: `.env.example`, `.env.template`, `.env.sample`.
2. If no template exists, analyze the codebase for environment variable usage:
   - Search for `process.env.`, `os.environ`, `env::var`, `os.Getenv` patterns.
   - Extract all referenced variable names.
3. Generate `.env.example` with all required variables:
   - Group by category (database, API keys, feature flags, etc.).
   - Add descriptions as comments.
   - Include sensible defaults for non-sensitive values.
   - Mark required vs optional variables.
4. If `.env` does not exist, create it from the template:
   - Copy `.env.example` to `.env`.
   - Prompt for values of required variables without defaults.
5. Verify `.env` is in `.gitignore`.
6. Generate a TypeScript/Python config module that validates env vars at startup.

## Format

```env
# Database Configuration
DATABASE_URL=postgresql://localhost:5432/myapp  # Required
DATABASE_POOL_SIZE=10                            # Optional, default: 10

# API Keys
API_KEY=                                         # Required, no default
```

## Rules

- Never commit `.env` files; always verify `.gitignore` includes them.
- Always provide an `.env.example` with placeholder values, never real credentials.
- Mark each variable as required or optional with clear comments.
- Generate runtime validation that fails fast on missing required variables.
- Use consistent naming: UPPER_SNAKE_CASE with logical prefixes.

---

**Source:** [`rohitg00/awesome-claude-code-toolkit`](https://github.com/rohitg00/awesome-claude-code-toolkit) → `plugins/env-manager/commands/env-setup.md`
