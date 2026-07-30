---
name: quick-generate
description: "Quick image generation — skip conversation, go straight to image"
category: mcp-and-integrations
source_repo: davepoon/buildwithclaude
source_path: "plugins/mcp-servers-creative/commands/gen.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/mcp-servers-creative/commands/gen.md
---


# Quick Generate

Generate an image immediately from the user's description.

1. Look at the user's prompt: `$ARGUMENTS`
2. If the prompt is very short (under 10 words), call enhance_prompt first
3. If already detailed (10+ words), use it directly
4. Delegate to the image-generator agent
5. Show a brief one-line creative comment about the generation

Do NOT ask for confirmation, suggest alternatives, or give lengthy explanations.

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/mcp-servers-creative/commands/gen.md`
