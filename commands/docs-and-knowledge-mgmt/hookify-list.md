---
name: hookify-list
description: "設定済みのすべてのhookifyルールを一覧表示します"
category: docs-and-knowledge-mgmt
source_repo: affaan-m/ECC
source_path: "docs/ja-JP/commands/hookify-list.md"
source_url: https://github.com/affaan-m/ECC/blob/HEAD/docs/ja-JP/commands/hookify-list.md
---
すべてのhookifyルールを検索し、フォーマットされたテーブルで表示します。

## ステップ

1. すべての`.claude/hookify.*.local.md`ファイルを検索
2. 各ファイルのフロントマターを読み取り:
   - `name`
   - `enabled`
   - `event`
   - `action`
   - `pattern`
3. テーブルとして表示:

| ルール | 有効 | イベント | パターン | ファイル |
|--------|------|---------|---------|---------|

4. ルール数を表示し、`/hookify-configure`で後から状態を変更できることを通知。

---

**Source:** [`affaan-m/ECC`](https://github.com/affaan-m/ECC) → `docs/ja-JP/commands/hookify-list.md`
