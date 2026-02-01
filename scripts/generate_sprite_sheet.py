#!/usr/bin/env python3
"""
たまごっちキャラクター フレームアニメーション スプライトシート生成
32x32px のキャラクターを各モーションごとに描画
"""

from PIL import Image, ImageDraw
import os

# キャラクターの基本カラー（パステル）
BODY_COLOR = (255, 220, 240)  # ピンク
EYE_COLOR = (80, 80, 100)
MOUTH_COLOR = (255, 160, 180)
CHEEK_COLOR = (255, 180, 200)
SPARKLE_COLOR = (255, 255, 150)
ZZZ_COLOR = (180, 200, 255)

# スプライトシート設定
FRAME_SIZE = 32
COLS = 4  # 最大フレーム数
ROWS = 5  # モーション数
SHEET_WIDTH = FRAME_SIZE * COLS
SHEET_HEIGHT = FRAME_SIZE * ROWS


def draw_body(draw, x_offset, y_offset, height_scale=1.0, width_scale=1.0):
    """キャラクターの体を描画"""
    center_x = FRAME_SIZE // 2 + x_offset
    center_y = FRAME_SIZE // 2 + y_offset
    
    # 楕円の体（高さと幅を調整可能）
    body_width = int(20 * width_scale)
    body_height = int(24 * height_scale)
    
    draw.ellipse(
        [center_x - body_width//2, center_y - body_height//2,
         center_x + body_width//2, center_y + body_height//2],
        fill=BODY_COLOR,
        outline=(230, 180, 210),
        width=2
    )
    
    return center_x, center_y


def draw_eyes(draw, center_x, center_y, closed=False):
    """目を描画"""
    eye_y = center_y - 4
    
    if closed:
        # 閉じた目（横線）
        draw.line([center_x - 8, eye_y, center_x - 4, eye_y], fill=EYE_COLOR, width=2)
        draw.line([center_x + 4, eye_y, center_x + 8, eye_y], fill=EYE_COLOR, width=2)
    else:
        # 開いた目（点）
        draw.ellipse([center_x - 8, eye_y - 2, center_x - 4, eye_y + 2], fill=EYE_COLOR)
        draw.ellipse([center_x + 4, eye_y - 2, center_x + 8, eye_y + 2], fill=EYE_COLOR)


def draw_mouth(draw, center_x, center_y, type="smile", open=False):
    """口を描画"""
    mouth_y = center_y + 4
    
    if type == "smile":
        # 笑顔（曲線）
        draw.arc([center_x - 6, mouth_y - 2, center_x + 6, mouth_y + 6],
                 start=0, end=180, fill=MOUTH_COLOR, width=2)
    elif type == "open":
        # 開いた口（円）
        draw.ellipse([center_x - 4, mouth_y - 2, center_x + 4, mouth_y + 4],
                     fill=MOUTH_COLOR, outline=EYE_COLOR, width=1)
    elif type == "closed":
        # 閉じた口（線）
        draw.line([center_x - 4, mouth_y, center_x + 4, mouth_y],
                  fill=MOUTH_COLOR, width=2)


def draw_cheeks(draw, center_x, center_y, puffed=False):
    """ほっぺを描画"""
    cheek_y = center_y + 2
    size = 4 if puffed else 3
    
    # 左ほっぺ
    draw.ellipse([center_x - 14, cheek_y - size, center_x - 10, cheek_y + size],
                 fill=CHEEK_COLOR)
    # 右ほっぺ
    draw.ellipse([center_x + 10, cheek_y - size, center_x + 14, cheek_y + size],
                 fill=CHEEK_COLOR)


def draw_legs(draw, center_x, center_y, left_forward=False, right_forward=False):
    """足を描画"""
    leg_y = center_y + 12
    
    # 左足
    if left_forward:
        draw.ellipse([center_x - 8, leg_y + 2, center_x - 2, leg_y + 8],
                     fill=BODY_COLOR, outline=(230, 180, 210), width=1)
    else:
        draw.ellipse([center_x - 8, leg_y, center_x - 2, leg_y + 6],
                     fill=BODY_COLOR, outline=(230, 180, 210), width=1)
    
    # 右足
    if right_forward:
        draw.ellipse([center_x + 2, leg_y + 2, center_x + 8, leg_y + 8],
                     fill=BODY_COLOR, outline=(230, 180, 210), width=1)
    else:
        draw.ellipse([center_x + 2, leg_y, center_x + 8, leg_y + 6],
                     fill=BODY_COLOR, outline=(230, 180, 210), width=1)


def draw_arms(draw, center_x, center_y, raised=False):
    """手を描画"""
    arm_y = center_y + 2
    
    if raised:
        # 手を上げる
        draw.ellipse([center_x - 14, center_y - 8, center_x - 10, center_y - 2],
                     fill=BODY_COLOR, outline=(230, 180, 210), width=1)
        draw.ellipse([center_x + 10, center_y - 8, center_x + 14, center_y - 2],
                     fill=BODY_COLOR, outline=(230, 180, 210), width=1)
    else:
        # 手を下げる
        draw.ellipse([center_x - 14, arm_y, center_x - 10, arm_y + 6],
                     fill=BODY_COLOR, outline=(230, 180, 210), width=1)
        draw.ellipse([center_x + 10, arm_y, center_x + 14, arm_y + 6],
                     fill=BODY_COLOR, outline=(230, 180, 210), width=1)


def draw_sparkles(draw, center_x, center_y):
    """キラキラを描画"""
    # 左上
    draw.line([center_x - 10, center_y - 12, center_x - 12, center_y - 14],
              fill=SPARKLE_COLOR, width=2)
    draw.line([center_x - 12, center_y - 12, center_x - 10, center_y - 14],
              fill=SPARKLE_COLOR, width=2)
    
    # 右上
    draw.line([center_x + 10, center_y - 12, center_x + 12, center_y - 14],
              fill=SPARKLE_COLOR, width=2)
    draw.line([center_x + 12, center_y - 12, center_x + 10, center_y - 14],
              fill=SPARKLE_COLOR, width=2)


def draw_zzz(draw, center_x, center_y, size="small"):
    """Zzzを描画"""
    offset_x = 10
    offset_y = -12 if size == "small" else -14
    z_size = 4 if size == "small" else 6
    
    # Z
    x = center_x + offset_x
    y = center_y + offset_y
    draw.line([x, y, x + z_size, y], fill=ZZZ_COLOR, width=2)
    draw.line([x + z_size, y, x, y + z_size], fill=ZZZ_COLOR, width=2)
    draw.line([x, y + z_size, x + z_size, y + z_size], fill=ZZZ_COLOR, width=2)


# ===== モーション別フレーム生成 =====

def create_idle_frames():
    """待機モーション（4フレーム）"""
    frames = []
    
    # フレーム1: 通常立ち
    img = Image.new('RGBA', (FRAME_SIZE, FRAME_SIZE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    cx, cy = draw_body(draw, 0, 0)
    draw_eyes(draw, cx, cy)
    draw_mouth(draw, cx, cy, "smile")
    draw_cheeks(draw, cx, cy)
    draw_legs(draw, cx, cy)
    draw_arms(draw, cx, cy)
    frames.append(img)
    
    # フレーム2: 少し縮む
    img = Image.new('RGBA', (FRAME_SIZE, FRAME_SIZE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    cx, cy = draw_body(draw, 0, 1, height_scale=0.9)
    draw_eyes(draw, cx, cy)
    draw_mouth(draw, cx, cy, "smile")
    draw_cheeks(draw, cx, cy)
    draw_legs(draw, cx, cy)
    draw_arms(draw, cx, cy)
    frames.append(img)
    
    # フレーム3: 通常立ち
    frames.append(frames[0].copy())
    
    # フレーム4: 少し伸びる
    img = Image.new('RGBA', (FRAME_SIZE, FRAME_SIZE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    cx, cy = draw_body(draw, 0, -1, height_scale=1.1)
    draw_eyes(draw, cx, cy)
    draw_mouth(draw, cx, cy, "smile")
    draw_cheeks(draw, cx, cy)
    draw_legs(draw, cx, cy)
    draw_arms(draw, cx, cy)
    frames.append(img)
    
    return frames


def create_walk_frames():
    """歩きモーション（4フレーム）"""
    frames = []
    
    # フレーム1: 右足前
    img = Image.new('RGBA', (FRAME_SIZE, FRAME_SIZE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    cx, cy = draw_body(draw, 0, 0)
    draw_eyes(draw, cx, cy)
    draw_mouth(draw, cx, cy, "smile")
    draw_cheeks(draw, cx, cy)
    draw_legs(draw, cx, cy, left_forward=False, right_forward=True)
    draw_arms(draw, cx, cy)
    frames.append(img)
    
    # フレーム2: 両足揃い
    img = Image.new('RGBA', (FRAME_SIZE, FRAME_SIZE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    cx, cy = draw_body(draw, 0, 0)
    draw_eyes(draw, cx, cy)
    draw_mouth(draw, cx, cy, "smile")
    draw_cheeks(draw, cx, cy)
    draw_legs(draw, cx, cy, left_forward=False, right_forward=False)
    draw_arms(draw, cx, cy)
    frames.append(img)
    
    # フレーム3: 左足前
    img = Image.new('RGBA', (FRAME_SIZE, FRAME_SIZE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    cx, cy = draw_body(draw, 0, 0)
    draw_eyes(draw, cx, cy)
    draw_mouth(draw, cx, cy, "smile")
    draw_cheeks(draw, cx, cy)
    draw_legs(draw, cx, cy, left_forward=True, right_forward=False)
    draw_arms(draw, cx, cy)
    frames.append(img)
    
    # フレーム4: 両足揃い
    frames.append(frames[1].copy())
    
    return frames


def create_eat_frames():
    """食べるモーション（4フレーム）"""
    frames = []
    
    # フレーム1: 口閉じ
    img = Image.new('RGBA', (FRAME_SIZE, FRAME_SIZE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    cx, cy = draw_body(draw, 0, 0)
    draw_eyes(draw, cx, cy)
    draw_mouth(draw, cx, cy, "closed")
    draw_cheeks(draw, cx, cy)
    draw_legs(draw, cx, cy)
    draw_arms(draw, cx, cy)
    frames.append(img)
    
    # フレーム2: 口開く
    img = Image.new('RGBA', (FRAME_SIZE, FRAME_SIZE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    cx, cy = draw_body(draw, 0, 0)
    draw_eyes(draw, cx, cy)
    draw_mouth(draw, cx, cy, "open")
    draw_cheeks(draw, cx, cy)
    draw_legs(draw, cx, cy)
    draw_arms(draw, cx, cy)
    frames.append(img)
    
    # フレーム3: もぐもぐ（口閉じ＋ほっぺ膨らむ）
    img = Image.new('RGBA', (FRAME_SIZE, FRAME_SIZE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    cx, cy = draw_body(draw, 0, 0)
    draw_eyes(draw, cx, cy)
    draw_mouth(draw, cx, cy, "closed")
    draw_cheeks(draw, cx, cy, puffed=True)
    draw_legs(draw, cx, cy)
    draw_arms(draw, cx, cy)
    frames.append(img)
    
    # フレーム4: ごっくん（満足顔）
    img = Image.new('RGBA', (FRAME_SIZE, FRAME_SIZE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    cx, cy = draw_body(draw, 0, 0)
    draw_eyes(draw, cx, cy)
    draw_mouth(draw, cx, cy, "smile")
    draw_cheeks(draw, cx, cy)
    draw_legs(draw, cx, cy)
    draw_arms(draw, cx, cy)
    frames.append(img)
    
    return frames


def create_sleep_frames():
    """寝るモーション（3フレーム + パディング）"""
    frames = []
    
    # フレーム1: 目閉じ
    img = Image.new('RGBA', (FRAME_SIZE, FRAME_SIZE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    cx, cy = draw_body(draw, 0, 2)
    draw_eyes(draw, cx, cy, closed=True)
    draw_mouth(draw, cx, cy, "closed")
    draw_cheeks(draw, cx, cy)
    frames.append(img)
    
    # フレーム2: Zzz小さく
    img = Image.new('RGBA', (FRAME_SIZE, FRAME_SIZE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    cx, cy = draw_body(draw, 0, 2)
    draw_eyes(draw, cx, cy, closed=True)
    draw_mouth(draw, cx, cy, "closed")
    draw_cheeks(draw, cx, cy)
    draw_zzz(draw, cx, cy, "small")
    frames.append(img)
    
    # フレーム3: Zzz大きく
    img = Image.new('RGBA', (FRAME_SIZE, FRAME_SIZE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    cx, cy = draw_body(draw, 0, 2)
    draw_eyes(draw, cx, cy, closed=True)
    draw_mouth(draw, cx, cy, "closed")
    draw_cheeks(draw, cx, cy)
    draw_zzz(draw, cx, cy, "large")
    frames.append(img)
    
    # パディング（4フレームに揃える）
    frames.append(frames[2].copy())
    
    return frames


def create_happy_frames():
    """喜ぶモーション（4フレーム）"""
    frames = []
    
    # フレーム1: 笑顔
    img = Image.new('RGBA', (FRAME_SIZE, FRAME_SIZE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    cx, cy = draw_body(draw, 0, 0)
    draw_eyes(draw, cx, cy)
    draw_mouth(draw, cx, cy, "smile")
    draw_cheeks(draw, cx, cy)
    draw_legs(draw, cx, cy)
    draw_arms(draw, cx, cy)
    frames.append(img)
    
    # フレーム2: ジャンプ（上に移動＋手上げ）
    img = Image.new('RGBA', (FRAME_SIZE, FRAME_SIZE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    cx, cy = draw_body(draw, 0, -4)
    draw_eyes(draw, cx, cy)
    draw_mouth(draw, cx, cy, "smile")
    draw_cheeks(draw, cx, cy)
    draw_arms(draw, cx, cy, raised=True)
    frames.append(img)
    
    # フレーム3: 頂点（キラキラ追加）
    img = Image.new('RGBA', (FRAME_SIZE, FRAME_SIZE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    cx, cy = draw_body(draw, 0, -6)
    draw_eyes(draw, cx, cy)
    draw_mouth(draw, cx, cy, "smile")
    draw_cheeks(draw, cx, cy)
    draw_arms(draw, cx, cy, raised=True)
    draw_sparkles(draw, cx, cy)
    frames.append(img)
    
    # フレーム4: 着地（笑顔）
    img = Image.new('RGBA', (FRAME_SIZE, FRAME_SIZE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    cx, cy = draw_body(draw, 0, 0)
    draw_eyes(draw, cx, cy)
    draw_mouth(draw, cx, cy, "smile")
    draw_cheeks(draw, cx, cy)
    draw_legs(draw, cx, cy)
    draw_arms(draw, cx, cy)
    frames.append(img)
    
    return frames


def generate_sprite_sheet():
    """スプライトシート生成"""
    # スプライトシート作成
    sprite_sheet = Image.new('RGBA', (SHEET_WIDTH, SHEET_HEIGHT), (0, 0, 0, 0))
    
    # 各モーションのフレームを生成
    motions = [
        ("idle", create_idle_frames()),
        ("walk", create_walk_frames()),
        ("eat", create_eat_frames()),
        ("sleep", create_sleep_frames()),
        ("happy", create_happy_frames()),
    ]
    
    # スプライトシートに配置
    for row, (name, frames) in enumerate(motions):
        for col, frame in enumerate(frames):
            x = col * FRAME_SIZE
            y = row * FRAME_SIZE
            sprite_sheet.paste(frame, (x, y))
        print(f"✅ {name}: {len(frames)} フレーム生成")
    
    return sprite_sheet


def main():
    """メイン処理"""
    print("🎨 たまごっちキャラクター フレームアニメーション生成開始")
    print(f"フレームサイズ: {FRAME_SIZE}x{FRAME_SIZE}px")
    print(f"スプライトシート: {SHEET_WIDTH}x{SHEET_HEIGHT}px")
    print("")
    
    # スプライトシート生成
    sprite_sheet = generate_sprite_sheet()
    
    # 保存
    output_dir = os.path.join(os.path.dirname(__file__), "..", "assets")
    os.makedirs(output_dir, exist_ok=True)
    
    output_path = os.path.join(output_dir, "character_spritesheet.png")
    sprite_sheet.save(output_path)
    
    print("")
    print(f"✅ スプライトシート保存完了: {output_path}")
    print(f"サイズ: {sprite_sheet.size}")
    
    # 個別フレームも保存（デバッグ用）
    frames_dir = os.path.join(output_dir, "frames")
    os.makedirs(frames_dir, exist_ok=True)
    
    motions = [
        ("idle", create_idle_frames()),
        ("walk", create_walk_frames()),
        ("eat", create_eat_frames()),
        ("sleep", create_sleep_frames()),
        ("happy", create_happy_frames()),
    ]
    
    for name, frames in motions:
        for i, frame in enumerate(frames):
            frame_path = os.path.join(frames_dir, f"{name}_{i}.png")
            frame.save(frame_path)
    
    print(f"✅ 個別フレーム保存完了: {frames_dir}/")


if __name__ == "__main__":
    main()
