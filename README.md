# 🥚 たまごっち風キャラクター デモ

Pillow（PIL）で生成したパステルカラーのかわいいキャラクターを使った、たまごっち風のデモプロジェクトです。

## 📦 収録デモ

### 1. 基本デモ（index.html）
- CSSアニメーションによる動き
- ボタンでキャラクターの状態を変更
- シンプルなインタラクション

### 2. フレームアニメーション（animation.html） ⭐ NEW!
- **スプライトシートを使った本格的なフレームアニメーション**
- Pillowで描画した各フレームを切り替えて動きを表現
- 5種類のモーション（待機/歩く/食べる/寝る/喜ぶ）
- 各モーション複数フレーム（3〜4フレーム）

## 🎨 キャラクター仕様

- **サイズ:** 32x32px（ピクセルアート風）
- **スタイル:** パステルカラーの丸っこいフォルム
- **生成方法:** Python + Pillow（PIL）

## 🎬 アニメーションモーション

### 待機（Idle）- 4フレーム
呼吸するような柔らかい動き
1. 通常立ち
2. 少し縮む
3. 通常立ち
4. 少し伸びる

### 歩く（Walk）- 4フレーム
トコトコと可愛く歩く
1. 右足前
2. 両足揃い
3. 左足前
4. 両足揃い

### 食べる（Eat）- 4フレーム
もぐもぐと美味しそうに食べる
1. 口閉じ
2. 口開く
3. もぐもぐ（ほっぺ膨らむ）
4. ごっくん（満足顔）

### 寝る（Sleep）- 3フレーム
すやすやと気持ちよく眠る
1. 目閉じ
2. Zzz小さく
3. Zzz大きく

### 喜ぶ（Happy）- 4フレーム
嬉しくてジャンプ！
1. 笑顔
2. ジャンプ（手上げ）
3. 頂点（キラキラ）
4. 着地

## 🚀 デモサイト

GitHub Pagesでホスティング中：
- **基本デモ:** https://ximanuki.github.io/tamagotchi-demo/
- **フレームアニメーション:** https://ximanuki.github.io/tamagotchi-demo/animation.html

## 🛠️ ローカル実行

### 必要なもの
- Python 3.x
- Pillow（PIL）

### セットアップ
```bash
# Pillowインストール
pip install Pillow

# スプライトシート生成
python3 scripts/generate_sprite_sheet.py

# ローカルサーバー起動
python3 -m http.server 8000

# ブラウザでアクセス
# http://localhost:8000/animation.html
```

## 📁 プロジェクト構成

```
tamagotchi-demo/
├── index.html                      # 基本デモ
├── animation.html                  # フレームアニメーションデモ ⭐
├── README.md
├── assets/
│   ├── character_spritesheet.png   # スプライトシート（128x160px）⭐
│   └── frames/                     # 個別フレーム画像（デバッグ用）⭐
└── scripts/
    └── generate_sprite_sheet.py    # スプライトシート生成スクリプト ⭐
```

## 🎯 技術ポイント

### スプライトシートアニメーション
- **方式:** Canvas APIでスプライトシートから該当フレームを切り出し
- **フレームレート:** 200ms/フレーム（5 FPS）
- **シート構成:** 横4列×縦5行（各モーション1行、最大4フレーム）
- **サイズ:** 128x160px（32x32pxフレーム × 4列5行）

### Pillowによる描画
- 楕円、線、円などの基本図形の組み合わせ
- パラメータで体の高さ・幅を調整可能
- 目・口・ほっぺ・足・手などのパーツを関数化
- Zzz、キラキラなどのエフェクト表現

### CSSアニメーション（基本デモ）
- CSS `@keyframes`による滑らかなアニメーション
- ホバーエフェクト
- グラデーション背景

## 📝 ライセンス

MIT License

## 🔗 リポジトリ

https://github.com/ximanuki/tamagotchi-demo

---

**Made with ❤️ using Python Pillow & HTML5 Canvas**
