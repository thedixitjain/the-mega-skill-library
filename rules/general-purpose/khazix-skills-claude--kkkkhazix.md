---
name: khazix-skills-claude
description: "团队任务管理工具，个人使用。"
category: general-purpose
source_repo: KKKKhazix/khazix-skills
source_path: "neat-freak/evals/fixtures/eval-1-routine-dev-sync/workspace/taskflow/CLAUDE.md"
source_url: https://github.com/KKKKhazix/khazix-skills/blob/HEAD/neat-freak/evals/fixtures/eval-1-routine-dev-sync/workspace/taskflow/CLAUDE.md
---
# taskflow

团队任务管理工具，个人使用。

## 技术栈

- 语言 / 框架：TypeScript + Express（REST API）+ React
- 数据库：SQLite（better-sqlite3）

## 启动

```bash
npm install
npm run dev   # Express 起在 :4000
```

## API 路由清单

- `GET /api/tasks` — 任务列表
- `POST /api/tasks` — 创建任务
- `PATCH /api/tasks/:id` — 更新任务
- `DELETE /api/tasks/:id` — 删除任务

## 部署

部署到 Vercel（`vercel --prod`）。

---

**Source:** [`KKKKhazix/khazix-skills`](https://github.com/KKKKhazix/khazix-skills) → `neat-freak/evals/fixtures/eval-1-routine-dev-sync/workspace/taskflow/CLAUDE.md`
