---
name: together-debug-bundle
description: "'Together AI debug bundle for inference, fine-tuning, and model deployment. Use when working with Together AI''s OpenAI-compatible API. Trigger: \"together debug bundle\". '"
allowed-tools: "Read, Write, Edit, Bash(pip:*), Grep"
category: engineering-core
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "plugins/saas-packs/together-pack/skills/together-debug-bundle/SKILL.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/plugins/saas-packs/together-pack/skills/together-debug-bundle/SKILL.md
---

# Together AI Debug Bundle

## Overview

Guidance for debug bundle with Together AI inference and fine-tuning API.

## Instructions

### Key Points

- Together AI is OpenAI-compatible: `base_url = 'https://api.together.xyz/v1'`
- Use the `together` Python SDK or any OpenAI client library
- Supports 100+ open-source models (Llama, Mixtral, Qwen, FLUX)
- Fine-tuning available for supported models
- Batch inference at 50% cost reduction

## Error Handling

| Error | Cause | Solution |
|-------|-------|----------|
| `401 Unauthorized` | Invalid API key | Check at api.together.xyz |
| `Model not found` | Wrong model ID | Use `client.models.list()` |
| `429 Rate limit` | Too many requests | Implement backoff |
| `500 Server error` | Model overloaded | Retry with backoff |

## Resources

- [Together AI Docs](https://docs.together.ai/)
- [API Reference](https://docs.together.ai/reference/chat-completions-1)
- [Model List](https://docs.together.ai/docs/inference-models)

## Next Steps

See related Together AI skills for more patterns.

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `plugins/saas-packs/together-pack/skills/together-debug-bundle/SKILL.md`
