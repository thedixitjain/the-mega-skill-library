---
name: deployment-patterns
description: "Kubernetes、Docker、Vercel、クラウドプロバイダーにおけるデプロイメントパターンと戦略。ブルーグリーン、カナリア、ローリングデプロイメント、ゼロダウンタイムアップグレード。"
category: devops-and-infra
source_repo: affaan-m/ECC
source_path: "docs/ja-JP/skills/deployment-patterns/SKILL.md"
source_url: https://github.com/affaan-m/ECC/blob/HEAD/docs/ja-JP/skills/deployment-patterns/SKILL.md
---
# デプロイメント パターン

本番環境でのデプロイメント戦略とパターン。

## 使用時期

- Kubernetesへのデプロイメント戦略
- ゼロダウンタイムアップグレード
- カナリアまたはブルーグリーンロールアウト
- 自動スケール構成
- デプロイメントヘルスチェック設定

## デプロイメント戦略

### 1. ローリングデプロイメント

古いポッドを段階的に新しいものと置き換え。デフォルトで安全。

```yaml
spec:
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
```

### 2. ブルーグリーン

2つの完全な環境。即座にスイッチ可能。

### 3. カナリアデプロイメント

トラフィックのわずかなパーセンテージを新バージョンに。段階的に増加。

## ベストプラクティス

- [ ] ヘルスチェックエンドポイント実装
- [ ] ログシステム構成
- [ ] メトリクス収集セットアップ
- [ ] ロールバック計画作成
- [ ] 本番環境との間隔でテスト

詳細については、ドキュメントを参照してください。

---

**Source:** [`affaan-m/ECC`](https://github.com/affaan-m/ECC) → `docs/ja-JP/skills/deployment-patterns/SKILL.md`
