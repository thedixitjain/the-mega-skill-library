---
name: build
description: "Build a new application from a plain-English description using Shipwright's autonomous 9-phase pipeline"
category: devops-and-infra
source_repo: davepoon/buildwithclaude
source_path: "plugins/shipwright/commands/build.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/shipwright/commands/build.md
---


Build a complete application from the provided description. Shipwright will:

1. Analyze requirements and generate a spec
2. Select the optimal stack (Next.js, FastAPI, Express, or Static)
3. Scaffold the project structure
4. Implement all features
5. Generate comprehensive tests
6. Run linting and security checks
7. Generate documentation
8. Verify the build
9. Prepare for deployment

Usage: `/shipwright:build <description of your app>`

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/shipwright/commands/build.md`
