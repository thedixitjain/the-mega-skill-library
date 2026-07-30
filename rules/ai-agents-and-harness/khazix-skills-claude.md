---
name: khazix-skills-claude
description: "团队 skill 分发中心：同步、安装、管理团队共享的 agent skills。"
category: ai-agents-and-harness
source_repo: KKKKhazix/khazix-skills
source_path: "neat-freak/evals/fixtures/eval-4-cross-project/workspace/skills-hub/CLAUDE.md"
source_url: https://github.com/KKKKhazix/khazix-skills/blob/HEAD/neat-freak/evals/fixtures/eval-4-cross-project/workspace/skills-hub/CLAUDE.md
---
# skills-hub

团队 skill 分发中心：同步、安装、管理团队共享的 agent skills。

## 技术栈

- Bash（setup.sh 安装器）+ React 管理前端

## 启动

```bash
./setup.sh          # 安装 / 更新本机 skills
cd web && pnpm dev  # 管理前端 :5173
```

## 认证

通过 auth-center 的 Authorization Code Flow 登录（浏览器跳转回调）。

---

**Source:** [`KKKKhazix/khazix-skills`](https://github.com/KKKKhazix/khazix-skills) → `neat-freak/evals/fixtures/eval-4-cross-project/workspace/skills-hub/CLAUDE.md`
