---
name: hookify-configure
description: "交互式启用或禁用 hookify 规则"
category: docs-and-knowledge-mgmt
source_repo: affaan-m/ECC
source_path: "docs/zh-CN/commands/hookify-configure.md"
source_url: https://github.com/affaan-m/ECC/blob/HEAD/docs/zh-CN/commands/hookify-configure.md
---
交互式启用或禁用现有的 hookify 规则。

## 步骤

1. 查找所有 `.claude/hookify.*.local.md` 文件
2. 读取每条规则的当前状态
3. 展示列表，包含每条规则的当前启用/禁用状态
4. 询问需要切换哪些规则
5. 更新所选规则文件中的 `enabled:` 字段
6. 确认更改

---

**Source:** [`affaan-m/ECC`](https://github.com/affaan-m/ECC) → `docs/zh-CN/commands/hookify-configure.md`
