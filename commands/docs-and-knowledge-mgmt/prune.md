---
name: prune
description: "プロモートされなかった30日以上経過の保留中インスティンクトを削除"
category: docs-and-knowledge-mgmt
source_repo: affaan-m/ECC
source_path: "docs/ja-JP/commands/prune.md"
source_url: https://github.com/affaan-m/ECC/blob/HEAD/docs/ja-JP/commands/prune.md
---
# 保留中インスティンクトの整理

自動生成されたがレビューまたはプロモートされなかった期限切れの保留中インスティンクトを削除します。

## 実装

プラグインルートパスを使用してインスティンクトCLIを実行:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/continuous-learning-v2/scripts/instinct-cli.py" prune
```

または`CLAUDE_PLUGIN_ROOT`が設定されていない場合（手動インストール）:

```bash
python3 ~/.claude/skills/continuous-learning-v2/scripts/instinct-cli.py prune
```

## 使い方

```
/prune                    # 30日以上のインスティンクトを削除
/prune --max-age 60      # カスタム経過閾値（日数）
/prune --dry-run         # 削除せずにプレビュー
```

---

**Source:** [`affaan-m/ECC`](https://github.com/affaan-m/ECC) → `docs/ja-JP/commands/prune.md`
