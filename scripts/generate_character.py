#!/usr/bin/env python3
"""
たまごっち風ドット絵キャラクター生成スクリプト
パステルカラーでかわいい32x32pxのキャラクターを作成
"""

from PIL import Image, ImageDraw
import os

# パステルカラーパレット
COLORS = {
    'bg': (255, 255, 255, 0),  # 透明
    'body': (255, 192, 203),    # パステルピンク
    'body_shadow': (255, 160, 180),  # 少し濃いピンク
    'white': (255, 255, 255),   # 白
    'eye': (88, 88, 88),        # ダークグレー（目）
    'cheek': (255, 140, 160),   # チーク
    'mouth': (88, 88, 88),      # 口
    'happy': (255, 200, 100),   # ハッピー色（黄色っぽい）
    'sleep': (200, 200, 230),   # 睡眠色（薄紫）
}

def create_base_character(img, x_offset=0):
    """基本形のキャラクター（通常表情）"""
    draw = ImageDraw.Draw(img)
    
    # 体（楕円形）- 中心に配置
    cx, cy = 16 + x_offset, 18
    
    # 影（体の下部）
    draw.ellipse([cx-8, cy-6, cx+8, cy+8], fill=COLORS['body_shadow'])
    
    # メインボディ
    draw.ellipse([cx-9, cy-7, cx+9, cy+7], fill=COLORS['body'])
    
    # 目（点）
    draw.ellipse([cx-5, cy-2, cx-3, cy], fill=COLORS['eye'])
    draw.ellipse([cx+3, cy-2, cx+5, cy], fill=COLORS['eye'])
    
    # ハイライト（目の中）
    draw.point((cx-4, cy-1), fill=COLORS['white'])
    draw.point((cx+4, cy-1), fill=COLORS['white'])
    
    # 口（小さなカーブ）
    draw.point((cx, cy+2), fill=COLORS['mouth'])
    draw.point((cx-1, cy+3), fill=COLORS['mouth'])
    draw.point((cx+1, cy+3), fill=COLORS['mouth'])
    
    # チーク
    draw.point((cx-7, cy+1), fill=COLORS['cheek'])
    draw.point((cx+7, cy+1), fill=COLORS['cheek'])
    
    # 耳（小さな突起）
    draw.ellipse([cx-10, cy-5, cx-9, cy-3], fill=COLORS['body'])
    draw.ellipse([cx+9, cy-5, cx+10, cy-3], fill=COLORS['body'])

def create_happy_character(img, x_offset=0):
    """嬉しい表情"""
    draw = ImageDraw.Draw(img)
    
    cx, cy = 16 + x_offset, 18
    
    # 影（体の下部）
    draw.ellipse([cx-8, cy-6, cx+8, cy+8], fill=COLORS['body_shadow'])
    
    # メインボディ
    draw.ellipse([cx-9, cy-7, cx+9, cy+7], fill=COLORS['body'])
    
    # 目（閉じた感じ - 線）
    draw.line([cx-5, cy-1, cx-3, cy-1], fill=COLORS['eye'], width=1)
    draw.line([cx+3, cy-1, cx+5, cy-1], fill=COLORS['eye'], width=1)
    draw.point((cx-5, cy-2), fill=COLORS['eye'])
    draw.point((cx-3, cy-2), fill=COLORS['eye'])
    draw.point((cx+3, cy-2), fill=COLORS['eye'])
    draw.point((cx+5, cy-2), fill=COLORS['eye'])
    
    # 口（大きな笑顔）
    draw.arc([cx-4, cy+1, cx+4, cy+5], 0, 180, fill=COLORS['mouth'])
    draw.point((cx-3, cy+3), fill=COLORS['mouth'])
    draw.point((cx-2, cy+4), fill=COLORS['mouth'])
    draw.point((cx, cy+4), fill=COLORS['mouth'])
    draw.point((cx+2, cy+4), fill=COLORS['mouth'])
    draw.point((cx+3, cy+3), fill=COLORS['mouth'])
    
    # チーク（強調）
    draw.ellipse([cx-8, cy, cx-6, cy+2], fill=COLORS['cheek'])
    draw.ellipse([cx+6, cy, cx+8, cy+2], fill=COLORS['cheek'])
    
    # 耳
    draw.ellipse([cx-10, cy-5, cx-9, cy-3], fill=COLORS['body'])
    draw.ellipse([cx+9, cy-5, cx+10, cy-3], fill=COLORS['body'])
    
    # ハッピーオーラ（キラキラ）
    draw.point((cx-11, cy-8), fill=COLORS['happy'])
    draw.point((cx+11, cy-8), fill=COLORS['happy'])

def create_sleepy_character(img, x_offset=0):
    """眠い表情"""
    draw = ImageDraw.Draw(img)
    
    cx, cy = 16 + x_offset, 18
    
    # 影
    draw.ellipse([cx-8, cy-6, cx+8, cy+8], fill=COLORS['body_shadow'])
    
    # メインボディ
    draw.ellipse([cx-9, cy-7, cx+9, cy+7], fill=COLORS['body'])
    
    # 目（閉じてる - 線）
    draw.line([cx-5, cy, cx-3, cy], fill=COLORS['eye'], width=1)
    draw.line([cx+3, cy, cx+5, cy], fill=COLORS['eye'], width=1)
    
    # 口（小さなo）
    draw.ellipse([cx-1, cy+2, cx+1, cy+4], fill=COLORS['mouth'])
    
    # チーク（薄め）
    draw.point((cx-7, cy+1), fill=COLORS['cheek'])
    draw.point((cx+7, cy+1), fill=COLORS['cheek'])
    
    # 耳
    draw.ellipse([cx-10, cy-5, cx-9, cy-3], fill=COLORS['body'])
    draw.ellipse([cx+9, cy-5, cx+10, cy-3], fill=COLORS['body'])
    
    # Zzzマーク
    draw.point((cx+10, cy-10), fill=COLORS['sleep'])
    draw.point((cx+11, cy-10), fill=COLORS['sleep'])
    draw.point((cx+10, cy-11), fill=COLORS['sleep'])
    draw.point((cx+12, cy-9), fill=COLORS['sleep'])

def create_bounce_frame1(img, x_offset=0):
    """待機アニメ - フレーム1（通常位置）"""
    create_base_character(img, x_offset)

def create_bounce_frame2(img, x_offset=0):
    """待機アニメ - フレーム2（少し上）"""
    draw = ImageDraw.Draw(img)
    
    cx, cy = 16 + x_offset, 16  # 2px上
    
    # 影（体の下部）
    draw.ellipse([cx-8, cy-6, cx+8, cy+8], fill=COLORS['body_shadow'])
    
    # メインボディ
    draw.ellipse([cx-9, cy-7, cx+9, cy+7], fill=COLORS['body'])
    
    # 目
    draw.ellipse([cx-5, cy-2, cx-3, cy], fill=COLORS['eye'])
    draw.ellipse([cx+3, cy-2, cx+5, cy], fill=COLORS['eye'])
    draw.point((cx-4, cy-1), fill=COLORS['white'])
    draw.point((cx+4, cy-1), fill=COLORS['white'])
    
    # 口
    draw.point((cx, cy+2), fill=COLORS['mouth'])
    draw.point((cx-1, cy+3), fill=COLORS['mouth'])
    draw.point((cx+1, cy+3), fill=COLORS['mouth'])
    
    # チーク
    draw.point((cx-7, cy+1), fill=COLORS['cheek'])
    draw.point((cx+7, cy+1), fill=COLORS['cheek'])
    
    # 耳
    draw.ellipse([cx-10, cy-5, cx-9, cy-3], fill=COLORS['body'])
    draw.ellipse([cx+9, cy-5, cx+10, cy-3], fill=COLORS['body'])

def create_bounce_frame3(img, x_offset=0):
    """待機アニメ - フレーム3（少し潰れた感じ）"""
    draw = ImageDraw.Draw(img)
    
    cx, cy = 16 + x_offset, 19  # 1px下
    
    # 影（体の下部）
    draw.ellipse([cx-8, cy-5, cx+8, cy+8], fill=COLORS['body_shadow'])
    
    # メインボディ（少し横広）
    draw.ellipse([cx-10, cy-6, cx+10, cy+6], fill=COLORS['body'])
    
    # 目
    draw.ellipse([cx-5, cy-2, cx-3, cy], fill=COLORS['eye'])
    draw.ellipse([cx+3, cy-2, cx+5, cy], fill=COLORS['eye'])
    draw.point((cx-4, cy-1), fill=COLORS['white'])
    draw.point((cx+4, cy-1), fill=COLORS['white'])
    
    # 口
    draw.point((cx, cy+2), fill=COLORS['mouth'])
    draw.point((cx-1, cy+2), fill=COLORS['mouth'])
    draw.point((cx+1, cy+2), fill=COLORS['mouth'])
    
    # チーク
    draw.point((cx-8, cy+1), fill=COLORS['cheek'])
    draw.point((cx+8, cy+1), fill=COLORS['cheek'])
    
    # 耳
    draw.ellipse([cx-11, cy-4, cx-10, cy-2], fill=COLORS['body'])
    draw.ellipse([cx+10, cy-4, cx+11, cy-2], fill=COLORS['body'])

def main():
    """スプライトシートを生成"""
    # 各フレーム: 32x32
    # レイアウト: 横6枚（基本、嬉しい、眠い、バウンス1、バウンス2、バウンス3）
    sprite_width = 32 * 6
    sprite_height = 32
    
    sprite_sheet = Image.new('RGBA', (sprite_width, sprite_height), COLORS['bg'])
    
    # 各フレームを生成
    frames = [
        create_base_character,
        create_happy_character,
        create_sleepy_character,
        create_bounce_frame1,
        create_bounce_frame2,
        create_bounce_frame3,
    ]
    
    for i, frame_func in enumerate(frames):
        frame_func(sprite_sheet, x_offset=i*32)
    
    # 保存
    output_path = os.path.expanduser('~/clawd/games/tamagotchi-demo/assets/character_sprite.png')
    sprite_sheet.save(output_path)
    print(f'✨ スプライトシート生成完了: {output_path}')
    
    # プレビュー用に個別画像も保存（8倍拡大）
    scale = 8
    preview_dir = os.path.expanduser('~/clawd/games/tamagotchi-demo/assets/preview')
    os.makedirs(preview_dir, exist_ok=True)
    
    frame_names = ['normal', 'happy', 'sleepy', 'bounce1', 'bounce2', 'bounce3']
    for i, (frame_func, name) in enumerate(zip(frames, frame_names)):
        preview = Image.new('RGBA', (32, 32), COLORS['bg'])
        frame_func(preview, 0)
        preview_large = preview.resize((32*scale, 32*scale), Image.NEAREST)
        preview_large.save(f'{preview_dir}/{name}.png')
    
    print(f'📸 プレビュー画像も保存しました: {preview_dir}/')

if __name__ == '__main__':
    main()
