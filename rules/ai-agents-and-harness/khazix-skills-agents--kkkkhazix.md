---
name: khazix-skills-agents
description: "PDF 工具集。"
category: ai-agents-and-harness
source_repo: KKKKhazix/khazix-skills
source_path: "neat-freak/evals/fixtures/eval-5-governance/workspace/pdf-tools/AGENTS.md"
source_url: https://github.com/KKKKhazix/khazix-skills/blob/HEAD/neat-freak/evals/fixtures/eval-5-governance/workspace/pdf-tools/AGENTS.md
---
# pdf-tools

PDF 工具集。

## 启动

```bash
pip install -r requirements.txt
uvicorn app:api --port 3001
```

## 约定

- 输出文件统一落 `output/` 目录
- 大文件（>50MB）走流式处理，别整个读进内存

---

**Source:** [`KKKKhazix/khazix-skills`](https://github.com/KKKKhazix/khazix-skills) → `neat-freak/evals/fixtures/eval-5-governance/workspace/pdf-tools/AGENTS.md`
