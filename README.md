# 家庭の断捨離ガイド
[![build](https://github.com/yourname/home-declutter/actions/workflows/python-app.yml/badge.svg)](https://github.com/yourname/home-declutter/actions/workflows/python-app.yml)
[![license](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)

## 1. プロジェクト概要
このプロジェクトは、家庭内の不要品を整理し、効率的に管理するためのアイデアやツールをまとめることを目的としています。断捨離を進める際のチェックリストや簡単なスクリプトを共有し、より快適な生活空間を実現するサポートを行います。

## 2. フォルダ構成
```
/
├── README.md
├── LICENSE
├── data/
│   └── checklist.csv
├── src/
│   └── convert.py
├── tests/
│   └── test_convert.py
└── .github/
    └── workflows/
        └── python-app.yml
```

## 3. 家具・衣類・書籍などカテゴリー別チェックリスト
- **家具**: ベッド、テーブル、椅子、収納棚 など
- **衣類**: コート、シャツ、パンツ、靴 など
- **書籍**: 雑誌、文庫本、教科書 など
- **その他**: キッチン用品、家電、趣味の道具 など

各カテゴリーごとに「残す」「処分する」「寄付する」などの判断基準を設け、リスト化しておくと便利です。

## 4. 使い方（例：Python スクリプトで在庫管理）
`src/convert.py` を使用して CSV を JSON に変換できます。

```bash
python src/convert.py data/checklist.csv output.json
```

`data/checklist.csv` には各アイテムのカテゴリや状態を記録しています。実行すると `output.json` に変換結果が保存されます。

## 5. ライセンス
このプロジェクトは MIT License の下で公開されます。詳細は `LICENSE` ファイルをご覧ください。

## 6. コントリビュートガイド
1. Issue を作成して変更点を提案してください。
2. Fork してブランチを作成し、修正をコミットします。
3. Pull Request を送ってください。

皆さまのコントリビューションを歓迎します。
