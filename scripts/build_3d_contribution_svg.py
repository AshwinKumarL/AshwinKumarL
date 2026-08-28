import os
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import json

# Load exact parsed metrics
with open('scripts/real_stats.json', 'r', encoding='utf-8') as f:
    stats = json.load(f)

total_count = stats['total']          # 60
this_week_count = stats['this_week']  # 6
best_day_count = stats['best_day_count'] # 9
longest_streak = stats['longest_streak'] # 2
current_streak = stats['current_streak'] # 2
daily_counts = stats['daily_counts']

# Populate 52 x 7 grid with real daily counts
grid = np.zeros((52, 7), dtype=int)
for idx, count in enumerate(daily_counts[:52*7]):
    x = idx // 7
    y = idx % 7
    if count == 0:
        lvl = 0
    elif count <= 2:
        lvl = 1
    elif count <= 4:
        lvl = 2
    elif count <= 6:
        lvl = 3
    else:
        lvl = 4
    grid[x, y] = lvl

# Canvas Dimensions: 980 x 430 (rendered at 2X for retina sharpness)
W, H = 980, 430
SCALE = 2
W2, H2 = W * SCALE, H * SCALE

origin_x = 240 * SCALE
origin_y = 175 * SCALE
tile_w = 9.2 * SCALE
tile_h = 4.8 * SCALE
h_unit = 8.5 * SCALE

BG_DARK     = (4, 19, 21)
CARD_BG     = (9, 34, 38)
BORDER_TEAL = (14, 80, 88)
EMERALD     = (0, 214, 143)
JADE        = (20, 184, 166)
COOL_TEAL   = (0, 240, 255)
MINT_WHITE  = (235, 255, 250)
MUTED_MINT  = (167, 243, 208)

colors = {
    0: {'top': (8, 35, 39),    'left': (5, 24, 27),    'right': (3, 16, 18)},
    1: {'top': (14, 85, 78),   'left': (10, 61, 56),   'right': (6, 40, 36)},
    2: {'top': (20, 184, 166), 'left': (15, 118, 110), 'right': (10, 79, 74)},
    3: {'top': (0, 214, 143),  'left': (5, 150, 105),  'right': (4, 120, 87)},
    4: {'top': (0, 240, 255),  'left': (0, 197, 212),  'right': (0, 150, 164)}
}

title_font = ImageFont.truetype('C:\\Windows\\Fonts\\segoeuib.ttf', 16 * SCALE)
sub_font   = ImageFont.truetype('C:\\Windows\\Fonts\\segoeui.ttf', 11 * SCALE)
stat_num   = ImageFont.truetype('C:\\Windows\\Fonts\\segoeuib.ttf', 20 * SCALE)
stat_lbl   = ImageFont.truetype('C:\\Windows\\Fonts\\segoeuib.ttf', 11 * SCALE)
stat_sub   = ImageFont.truetype('C:\\Windows\\Fonts\\segoeui.ttf', 10 * SCALE)

blocks = []
for x in range(52):
    for y in range(7):
        lvl = grid[x, y]
        blocks.append((x, y, lvl, x + y))
blocks.sort(key=lambda b: (b[3], b[1], b[0]))

TOTAL_FRAMES = 36
frames = []

for f_idx in range(TOTAL_FRAMES):
    im = Image.new('RGB', (W2, H2), BG_DARK)
    draw = ImageDraw.Draw(im)
    
    # Outer Container
    draw.rounded_rectangle([3*SCALE, 3*SCALE, W2-4*SCALE, H2-4*SCALE], radius=16*SCALE, fill=BG_DARK, outline=BORDER_TEAL, width=2*SCALE)
    
    # Tech Corner crosshairs
    for cx, cy in [(14*SCALE, 14*SCALE), (W2-14*SCALE, 14*SCALE), (14*SCALE, H2-14*SCALE), (W2-14*SCALE, H2-14*SCALE)]:
        draw.line([cx-4*SCALE, cy, cx+4*SCALE, cy], fill=COOL_TEAL, width=int(1.5*SCALE))
        draw.line([cx, cy-4*SCALE, cx, cy+4*SCALE], fill=COOL_TEAL, width=int(1.5*SCALE))
        
    # Top Header
    draw.text((25*SCALE, 20*SCALE), '3D ISOMETRIC CONTRIBUTION MATRIX', font=title_font, fill=MINT_WHITE)
    draw.text((25*SCALE, 42*SCALE), 'Visualizing AshwinKumarL live GitHub activity landscape in 3D voxels', font=sub_font, fill=MUTED_MINT)
    
    # Top Right Stats Card: REAL CONTRIBUTIONS
    cx = 680 * SCALE
    cy = 18 * SCALE
    cw = 275 * SCALE
    ch = 95 * SCALE
    draw.rounded_rectangle([cx, cy, cx+cw, cy+ch], radius=10*SCALE, fill=CARD_BG, outline=BORDER_TEAL, width=1*SCALE)
    draw.text((cx + 14*SCALE, cy + 8*SCALE), 'CONTRIBUTIONS', font=stat_lbl, fill=COOL_TEAL)
    draw.line([cx + 14*SCALE, cy + 26*SCALE, cx + cw - 14*SCALE, cy + 26*SCALE], fill=BORDER_TEAL, width=1*SCALE)
    
    # Col 1: Real Total (60)
    draw.text((cx + 20*SCALE, cy + 34*SCALE), str(total_count), font=stat_num, fill=EMERALD)
    draw.text((cx + 20*SCALE, cy + 60*SCALE), 'Total', font=stat_lbl, fill=MINT_WHITE)
    draw.text((cx + 20*SCALE, cy + 74*SCALE), 'Past Year', font=stat_sub, fill=MUTED_MINT)
    
    # Col 2: Real This Week (6)
    draw.text((cx + 110*SCALE, cy + 34*SCALE), str(this_week_count), font=stat_num, fill=COOL_TEAL)
    draw.text((cx + 110*SCALE, cy + 60*SCALE), 'This week', font=stat_lbl, fill=MINT_WHITE)
    draw.text((cx + 110*SCALE, cy + 74*SCALE), 'Recent commits', font=stat_sub, fill=MUTED_MINT)
    
    # Col 3: Real Best Day (9)
    draw.text((cx + 200*SCALE, cy + 34*SCALE), str(best_day_count), font=stat_num, fill=JADE)
    draw.text((cx + 200*SCALE, cy + 60*SCALE), 'Best day', font=stat_lbl, fill=MINT_WHITE)
    draw.text((cx + 200*SCALE, cy + 74*SCALE), 'Peak activity', font=stat_sub, fill=MUTED_MINT)
    
    # Bottom Left Stats Card: REAL STREAKS
    sx = 25 * SCALE
    sy = 305 * SCALE
    sw = 210 * SCALE
    sh = 95 * SCALE
    draw.rounded_rectangle([sx, sy, sx+sw, sy+sh], radius=10*SCALE, fill=CARD_BG, outline=BORDER_TEAL, width=1*SCALE)
    draw.text((sx + 14*SCALE, sy + 8*SCALE), 'STREAKS & FLOW', font=stat_lbl, fill=EMERALD)
    draw.line([sx + 14*SCALE, sy + 26*SCALE, sx + sw - 14*SCALE, sy + 26*SCALE], fill=BORDER_TEAL, width=1*SCALE)
    
    # Real Longest Streak
    draw.text((sx + 20*SCALE, sy + 34*SCALE), f"{longest_streak}d", font=stat_num, fill=EMERALD)
    draw.text((sx + 20*SCALE, sy + 60*SCALE), 'Longest', font=stat_lbl, fill=MINT_WHITE)
    draw.text((sx + 20*SCALE, sy + 74*SCALE), 'Consecutive days', font=stat_sub, fill=MUTED_MINT)
    
    # Real Current Streak
    draw.text((sx + 115*SCALE, sy + 34*SCALE), f"{current_streak}d", font=stat_num, fill=COOL_TEAL)
    draw.text((sx + 115*SCALE, sy + 60*SCALE), 'Current', font=stat_lbl, fill=MINT_WHITE)
    draw.text((sx + 115*SCALE, sy + 74*SCALE), 'Active streak', font=stat_sub, fill=MUTED_MINT)
    
    # Bottom Right Legend: Positioned cleanly with zero overlap
    lx = 770 * SCALE
    ly = 385 * SCALE
    draw.text((lx - 32*SCALE, ly), 'Less', font=stat_sub, fill=MUTED_MINT)
    for c_i, c_lvl in enumerate([0, 1, 2, 3, 4]):
        box_x = lx + c_i * 18 * SCALE
        draw.rounded_rectangle([box_x, ly - 2*SCALE, box_x + 12*SCALE, ly + 10*SCALE], radius=2*SCALE, fill=colors[c_lvl]['top'], outline=(3, 16, 18), width=1)
    draw.text((lx + 5 * 18 * SCALE + 6 * SCALE, ly), 'More', font=stat_sub, fill=MUTED_MINT)
    
    # --- RENDER 3D ISOMETRIC VOXELS FROM REAL COMMIT HISTORY ---
    for x, y, lvl, _ in blocks:
        wave_start = (x / 52.0) * 20.0
        dur = 8.0
        
        if f_idx < wave_start:
            growth = 0.0
        else:
            growth = min(1.0, (f_idx - wave_start) / dur)
            
        ease_g = 6*(growth**5) - 15*(growth**4) + 10*(growth**3)
        
        bx = origin_x + (x * tile_w) - (y * tile_w)
        by = origin_y + (x * tile_h * 0.7) + (y * tile_h * 0.7)
        
        target_h = (lvl * h_unit) if lvl > 0 else 1.5 * SCALE
        block_h = (1.5 * SCALE) + (target_h - 1.5 * SCALE) * ease_g
        
        c = colors[lvl] if ease_g > 0.1 else colors[0]
        
        top_pts = [
            (bx, by - block_h),
            (bx + tile_w, by + tile_h - block_h),
            (bx, by + tile_h * 2 - block_h),
            (bx - tile_w, by + tile_h - block_h)
        ]
        left_pts = [
            (bx - tile_w, by + tile_h - block_h),
            (bx, by + tile_h * 2 - block_h),
            (bx, by + tile_h * 2),
            (bx - tile_w, by + tile_h)
        ]
        right_pts = [
            (bx, by + tile_h * 2 - block_h),
            (bx + tile_w, by + tile_h - block_h),
            (bx + tile_w, by + tile_h),
            (bx, by + tile_h * 2)
        ]
        
        outline_c = (3, 16, 18)
        draw.polygon(right_pts, fill=c['right'], outline=outline_c)
        draw.polygon(left_pts, fill=c['left'], outline=outline_c)
        draw.polygon(top_pts, fill=c['top'], outline=outline_c)
        
    final_frame = im.resize((W, H), Image.Resampling.LANCZOS)
    p_frame = final_frame.convert('P', palette=Image.Palette.ADAPTIVE, colors=256)
    frames.append(p_frame)

durations = [45] * (len(frames) - 1) + [65535]

frames[0].save(
    'assets/github-contribution-3d.gif',
    save_all=True,
    append_images=frames[1:],
    duration=durations,
    loop=1,
    optimize=True
)

frames[-1].convert('RGB').save('assets/github-contribution-3d.png')

print(f'Successfully built 3D contribution matrix with REAL metrics: Total={total_count}, Week={this_week_count}, Best={best_day_count}, Streak={longest_streak}d!')
