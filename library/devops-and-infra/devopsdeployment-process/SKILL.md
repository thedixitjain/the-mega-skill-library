---
name: devopsdeployment-process
description: "部署流程和CI/CD配置，确保安全可靠的部署"
category: devops-and-infra
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/echoVic/boss-skill/skill/skills/devops/deployment-process/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/echoVic/boss-skill/skill/skills/devops/deployment-process/SKILL.md
---


# 部署流程与CI/CD

## 部署策略

| 策略 | 说明 | 适用场景 |
|------|------|----------|
| 蓝绿部署 | 两套环境切换 | 需要快速回滚 |
| 滚动部署 | 逐步替换实例 | 零停机部署 |
| 金丝雀部署 | 小流量验证 | 风险较高的更新 |

## CI/CD流程

```
代码提交 → 自动构建 → 自动测试 → 部署到测试环境 → 部署到生产环境
```

### GitHub Actions示例

```yaml
name: CI/CD
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Install
        run: npm install
      - name: Test
        run: npm test
      - name: Build
        run: npm run build
      - name: Deploy
        run: npm run deploy
```

## 环境配置

| 环境 | 用途 | 数据 |
|------|------|------|
| local | 本地开发 | 测试数据 |
| dev | 开发测试 | 测试数据 |
| staging | 预发布 | 生产数据副本 |
| prod | 生产环境 | 真实数据 |

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/echoVic/boss-skill/skill/skills/devops/deployment-process/SKILL.md`
