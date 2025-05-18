# 家庭の断捨離ガイド

![CI](https://github.com/USERNAME/home-declutter/actions/workflows/ci.yml/badge.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python](https://img.shields.io/badge/python-3.x-blue.svg)

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
        └── ci.yml
```

## 3. 家具・衣類・書籍などカテゴリー別チェックリスト
- **家具**: ベッド、テーブル、椅子、収納棚 など
- **衣類**: コート、シャツ、パンツ、靴 など
- **書籍**: 雑誌、文庫本、教科書 など
- **その他**: キッチン用品、家電、趣味の道具 など

各カテゴリーごとに「残す」「処分する」「寄付する」などの判断基準を設け、リスト化しておくと便利です。サンプルとして `data/checklist.csv` に3行のデータを用意しています。

## 4. 使い方（例：Python スクリプトで在庫管理）
`src/convert.py` を使うと、CSV ファイルを JSON 形式に変換できます。

```bash
python src/convert.py data/checklist.csv checklist.json
```

変換後の JSON はアプリケーションや別のツールで再利用できます。

## 5. ライセンス
このプロジェクトは MIT License の下で公開されます。詳細は `LICENSE` ファイルをご覧ください。

## 6. コントリビュートガイド
1. Issue を作成して変更点を提案してください。
2. Fork してブランチを作成し、修正をコミットします。
3. Pull Request を送ってください。

皆さまのコントリビューションを歓迎します。
