---
name: hookify-list
description: "列出所有已配置的 hookify 规则"
category: docs-and-knowledge-mgmt
source_repo: affaan-m/ECC
source_path: "docs/zh-CN/commands/hookify-list.md"
source_url: https://github.com/affaan-m/ECC/blob/HEAD/docs/zh-CN/commands/hookify-list.md
---
查找并以格式化表格显示所有 hookify 规则。

## 步骤

1. 查找所有 `.claude/hookify.*.local.md` 文件
2. 读取每个文件的前置元数据：
   * `name`
   * `enabled`
   * `event`
   * `action`
   * `pattern`
3. 以表格形式显示：

| 规则 | 启用状态 | 事件 | 模式 | 文件 |
|------|---------|-------|---------|------|

4. 显示规则数量，并提醒用户 `/hookify-configure` 后续可更改状态。

---

**Source:** [`affaan-m/ECC`](https://github.com/affaan-m/ECC) → `docs/zh-CN/commands/hookify-list.md`
