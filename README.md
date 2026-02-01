# 🎮 たまごっち風デモ

このみちゃん専用のたまごっち風ブラウザゲームです！

## ✨ 特徴

- 32x32ピクセルのかわいいドット絵キャラクター
- 3つの表情（ふつう・うれしい・ねむい）
- ぴょこぴょこ動く待機アニメーション
- パステルカラーのかわいい背景
- iPhone SE2（375x667px）対応

## 🎨 使用技術

- **画像生成**: Python + Pillow
- **フロントエンド**: HTML + CSS + JavaScript
- **デプロイ**: GitHub Pages

## 📂 ファイル構成

```
tamagotchi-demo/
├── index.html              # メインHTMLファイル
├── assets/                 # 画像アセット
│   ├── spritesheet.png     # 全フレームのスプライトシート
│   ├── character_normal.png
│   ├── character_happy.png
│   ├── character_sleepy.png
│   ├── character_bounce1.png
│   ├── character_bounce2.png
│   └── character_bounce3.png
├── scripts/                # 生成スクリプト
│   └── generate_character.py
└── README.md
```

## 🚀 使い方

### ローカルで見る
```bash
open ~/clawd/games/tamagotchi-demo/index.html
```

### キャラクターを再生成
```bash
cd ~/clawd/games/tamagotchi-demo
python3 scripts/generate_character.py
```

## 🎮 遊び方

1. **ふつう** ボタン: げんきな表情
2. **うれしい** ボタン: 喜んでハートが出る！
3. **ねむい** ボタン: ねむねむな表情

キャラクターはずっとぴょこぴょこ動いています♪

## 🌟 今後の拡張案

- [ ] ごはんボタン
- [ ] あそびボタン
- [ ] おふろボタン
- [ ] ミニゲーム
- [ ] 成長システム
- [ ] 複数のキャラクター

---

Made with ❤️ for このみちゃん
