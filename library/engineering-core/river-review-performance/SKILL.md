---
name: river-review-performance
description: "| パフォーマンス観点のレビューエージェント。 N+1クエリ、メモリ効率、キャッシュ戦略、可観測性の観点でコード変更を評価する。"
category: engineering-core
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/s977043/river-review/skills/agent-skills/river-review-performance/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/s977043/river-review/skills/agent-skills/river-review-performance/SKILL.md
---


# Performance Review（パフォーマンスレビュー）

パフォーマンスに影響する変更を検出し、適切な個別スキルで検証する。

## When to Use / いつ使うか

- データベースクエリの追加・変更時
- ループ処理やバッチ処理の変更時
- キャッシュ戦略の変更時
- 大量データの処理ロジック変更時

## Routing / ルーティング

| キーワード             | スキルID                      | 説明                                                                                               |
| ---------------------- | ----------------------------- | -------------------------------------------------------------------------------------------------- |
| キャッシュ, TTL        | `cache-strategy-consistency`  | 参照のみ。実行は `river-review-architecture`（[理由](#cache-strategy-consistency-の帰属について)） |
| 障害, 監視, メトリクス | `failure-modes-observability` | 障害モードと可観測性                                                                               |
| ログ, トレース         | `logging-observability`       | ロギング・可観測性                                                                                 |
| SLO, レイテンシ        | `operability-slo`             | 運用性・SLO                                                                                        |

### `cache-strategy-consistency` の帰属について

`cache-strategy-consistency` はキャッシュ戦略という語感から performance の懸念に見えるが、実体は設計ドキュメント（docs/spec/RFC 等）のキャッシュ戦略記述をレビューする upstream スキル（`applyTo` が `docs/**/*.md` 等の docs 系のみ、Pre-execution Gate も「差分に設計ドキュメントの変更がある」ことを要求）である。本エントリ（phase midstream、`applyTo` が code/sql）とはドメインが異なるため、ドメイン一貫性を優先し実行は `river-review-architecture`（phase upstream、docs 系 applyTo を保有）に据え置く。本表には**到達性のための参照行**として掲載するのみで、performance 側に重複するアクティブなキーワードルートは追加しない。

### デフォルト動作

- キーワード指定なし → 以下のヒューリスティクスで判定:
  - ループ内I/O → N+1クエリ検出
  - 大量データ処理 → メモリ効率チェック
  - 外部API呼び出し → タイムアウト・リトライ検証

## Execution Flow / 実行フロー

```text
1. 変更内容の分析
   ├─ ループ内I/O → N+1クエリ検出を優先
   ├─ 大量データ処理 → メモリ効率チェックを優先
   ├─ 外部API呼び出し → タイムアウト・リトライ検証を優先
   └─ キーワード指定あり → 該当スキルを直接選択

2. スキルの実行
   ├─ cache-strategy-consistency: キャッシュ戦略の一貫性
   ├─ failure-modes-observability: 障害モードと可観測性
   ├─ logging-observability: ロギング・可観測性
   └─ operability-slo: 運用性・SLO

3. 統合
   ├─ 重複する指摘の除去
   └─ Checklistに基づくパフォーマンスチェックの補完
```

## Checklist / チェックリスト

パフォーマンスレビューでは以下を確認する:

### クエリ効率

- N+1クエリが発生していないか
- 必要なeager loadingが設定されているか
- 不要なカラムを取得していないか（SELECT \*）

### メモリ効率

- ループ内での不要なオブジェクト生成がないか
- 大量データのストリーム処理が適切か
- メモリリークのパターンがないか

### I/O効率

- 外部API呼び出しのタイムアウト設定
- リトライ戦略の妥当性
- 並列化可能なI/Oの逐次実行

### キャッシュ

- キャッシュキーの設計が適切か
- TTLが妥当か
- キャッシュの無効化戦略

## Output Format / 出力形式

```text
<file>:<line>: <message>
```

- **Finding**: 何が問題か（1文）
- **Impact**: 推定される影響（レイテンシ増加、メモリ消費等）
- **Fix**: 次の一手（最小の修正案）

## 他スキルとの関係

| スキル                      | 関係 | 棲み分け                                                                |
| --------------------------- | ---- | ----------------------------------------------------------------------- |
| `river-review-architecture` | 補完 | performance は「実行時効率」、architecture は「構造的スケーラビリティ」 |
| `river-review-code`         | 補完 | performance は「速度・効率」、code は「可読性・保守性」                 |

## References

- [ROUTING.md](./references/ROUTING.md): 詳細なルーティングルール

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/s977043/river-review/skills/agent-skills/river-review-performance/SKILL.md`
