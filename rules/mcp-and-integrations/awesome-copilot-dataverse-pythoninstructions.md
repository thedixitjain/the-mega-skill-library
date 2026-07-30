---
name: awesome-copilot-dataverse-pythoninstructions
description: "- Install the Dataverse Python SDK and prerequisites. - Configure environment variables for Dataverse tenant, client ID, secret, and resource URL. - Use the SDK to authenticate via OAuth and perform CRUD operations."
category: mcp-and-integrations
source_repo: github/awesome-copilot
source_path: "instructions/dataverse-python.instructions.md"
source_url: https://github.com/github/awesome-copilot/blob/HEAD/instructions/dataverse-python.instructions.md
---
# Dataverse SDK for Python — Getting Started

- Install the Dataverse Python SDK and prerequisites.
- Configure environment variables for Dataverse tenant, client ID, secret, and resource URL.
- Use the SDK to authenticate via OAuth and perform CRUD operations.

## Setup
- Python 3.10+
- Recommended: virtual environment

## Install
```bash
pip install dataverse-sdk
```

## Auth Basics
- Use OAuth with Azure AD app registration.
- Store secrets in `.env` and load via `python-dotenv`.

## Common Tasks
- Query tables
- Create/update rows
- Batch operations
- Handle pagination and throttling

## Tips
- Reuse clients; avoid frequent re-auth.
- Add retries for transient failures.
- Log requests for troubleshooting.

---

**Source:** [`github/awesome-copilot`](https://github.com/github/awesome-copilot) → `instructions/dataverse-python.instructions.md`
