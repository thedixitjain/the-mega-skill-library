---
name: hookify-configure
description: "hookifyルールをインタラクティブに有効化または無効化します"
category: docs-and-knowledge-mgmt
source_repo: affaan-m/ECC
source_path: "docs/ja-JP/commands/hookify-configure.md"
source_url: https://github.com/affaan-m/ECC/blob/HEAD/docs/ja-JP/commands/hookify-configure.md
---
既存のhookifyルールをインタラクティブに有効化または無効化します。

## ステップ

1. すべての`.claude/hookify.*.local.md`ファイルを検索
2. 各ルールの現在の状態を読み取り
3. 現在の有効/無効ステータス付きでリストを提示
4. どのルールを切り替えるか質問
5. 選択されたルールファイルの`enabled:`フィールドを更新
6. 変更を確認

---

**Source:** [`affaan-m/ECC`](https://github.com/affaan-m/ECC) → `docs/ja-JP/commands/hookify-configure.md`
