import base64

with open('assets/ashwin-portrait.jpg', 'rb') as f:
    img_b64 = base64.b64encode(f.read()).decode('utf-8')

about_lines = [
    ("Name",          "Ashwin Kumar L"),
    ("Education",     "B.E. Computer Science &amp; Engineering, Sri Ramakrishna Engineering College"),
    ("Specialization","Artificial Intelligence, Machine Learning &amp; Intelligent Software Engineering"),
    ("Problem Solving","150+ LeetCode algorithms solved &#x2022; HackerRank Gold Badge in Python"),
    ("Current Focus", "Computer Vision, Large Language Models &amp; Deep Learning Pipelines"),
    ("Interests",     "Autonomous Systems, Competitive Programming, Game Strategy &amp; Automation"),
]

# SVG dimensions
W = 960
H = 360

# Photo frame
PHOTO_X  = 26
PHOTO_Y  = 26
PHOTO_W  = 270
PHOTO_H  = H - 52   # 308px

# Right panel starts right after photo + gap
PANEL_X  = PHOTO_X + PHOTO_W + 22   # 318
PANEL_W  = W - PANEL_X - 26          # 616

# Build slide-in keyframes for each line
slide_styles = ""
for i in range(len(about_lines)):
    delay = 0.3 + i * 0.18
    slide_styles += f"""
      .row-{i} {{
        animation: slideIn 0.55s cubic-bezier(0.22,1,0.36,1) {delay:.2f}s both;
      }}"""

# Build rows SVG
ROW_START_Y = 82    # where rows begin inside panel
ROW_H       = 35    # px per row
rows_svg = ""
for i, (label, value) in enumerate(about_lines):
    y = ROW_START_Y + i * ROW_H
    # alternating subtle row tint
    row_fill = "#1e0e34" if i % 2 == 0 else "#180c2c"
    rows_svg += f"""
    <!-- Row {i}: {label} -->
    <g class="row-{i}" transform="translate({PANEL_X}, {y})">
      <rect width="{PANEL_W}" height="{ROW_H - 4}" rx="7"
            fill="{row_fill}" stroke="#2e1050" stroke-width="0.8" />
      <!-- Label -->
      <text x="14" y="14" font-family="Segoe UI, system-ui, sans-serif"
            font-weight="700" font-size="10"
            fill="#c84bff" letter-spacing="0.8">{label.upper()}:</text>
      <!-- Value -->
      <text x="14" y="26" font-family="Segoe UI, system-ui, sans-serif"
            font-weight="500" font-size="15" fill="#f0eaff">{value}</text>
    </g>"""

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
     viewBox="0 0 {W} {H}" width="100%" height="100%" role="img"
     aria-label="Ashwin Kumar L profile card">

  <defs>
    <!-- Background -->
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1" gradientUnits="objectBoundingBox">
      <stop offset="0%"   stop-color="#0a0514"/>
      <stop offset="50%"  stop-color="#130924"/>
      <stop offset="100%" stop-color="#070310"/>
    </linearGradient>

    <!-- Animated neon border gradient -->
    <linearGradient id="neon" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%"   stop-color="#c84bff">
        <animate attributeName="stop-color" values="#c84bff;#00f5ff;#ff3b5c;#c84bff" dur="7s" repeatCount="indefinite"/>
      </stop>
      <stop offset="50%"  stop-color="#00f5ff">
        <animate attributeName="stop-color" values="#00f5ff;#ff3b5c;#c84bff;#00f5ff" dur="7s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" stop-color="#ff3b5c">
        <animate attributeName="stop-color" values="#ff3b5c;#c84bff;#00f5ff;#ff3b5c" dur="7s" repeatCount="indefinite"/>
      </stop>
    </linearGradient>

    <!-- Photo clip -->
    <clipPath id="photoClip">
      <rect x="{PHOTO_X}" y="{PHOTO_Y}" width="{PHOTO_W}" height="{PHOTO_H}" rx="16"/>
    </clipPath>

    <!-- Clip for each slide row so text doesn't bleed outside panel -->
    <clipPath id="panelClip">
      <rect x="{PANEL_X}" y="0" width="{PANEL_W}" height="{H}"/>
    </clipPath>

    <style>
      @keyframes slideIn {{
        from {{ transform: translateX(-40px); opacity: 0; }}
        to   {{ transform: translateX(0);     opacity: 1; }}
      }}
      @keyframes laserScan {{
        0%   {{ stroke-dashoffset: 0; }}
        100% {{ stroke-dashoffset: -1200; }}
      }}
      @keyframes pulse {{
        0%, 100% {{ opacity: 0.35; }}
        50%       {{ opacity: 1;    }}
      }}
      .laser {{
        stroke-dasharray: 100 500;
        animation: laserScan 6s linear infinite;
      }}
      .green-dot {{ animation: pulse 2.5s ease-in-out infinite; }}
      {slide_styles}
    </style>
  </defs>

  <!-- Outer card background -->
  <rect x="2" y="2" width="{W-4}" height="{H-4}" rx="18" fill="url(#bg)" stroke="#200d40" stroke-width="1.5"/>

  <!-- Animated neon border -->
  <rect x="2" y="2" width="{W-4}" height="{H-4}" rx="18" fill="none"
        stroke="url(#neon)" stroke-width="2" class="laser"
        filter="url(#neonGlowFilter)"/>

  <!-- Corner crosshair accents -->
  <path d="M15 8 L8 8 L8 15"  fill="none" stroke="#00f5ff" stroke-width="2"/>
  <path d="M{W-15} 8 L{W-8} 8 L{W-8} 15" fill="none" stroke="#ff3b5c" stroke-width="2"/>
  <path d="M15 {H-8} L8 {H-8} L8 {H-15}" fill="none" stroke="#c84bff" stroke-width="2"/>
  <path d="M{W-15} {H-8} L{W-8} {H-8} L{W-8} {H-15}" fill="none" stroke="#00f5ff" stroke-width="2"/>

  <!-- ===== LEFT: PHOTO ===== -->
  <!-- Shadow/background frame -->
  <rect x="{PHOTO_X-2}" y="{PHOTO_Y-2}" width="{PHOTO_W+4}" height="{PHOTO_H+4}"
        rx="17" fill="#150830" stroke="#5c1fa0" stroke-width="1.5"/>

  <!-- Real photo embedded -->
  <image href="data:image/jpeg;base64,{img_b64}"
         x="{PHOTO_X}" y="{PHOTO_Y}" width="{PHOTO_W}" height="{PHOTO_H}"
         preserveAspectRatio="xMidYMid slice"
         clip-path="url(#photoClip)"/>

  <!-- Photo overlay glow border -->
  <rect x="{PHOTO_X}" y="{PHOTO_Y}" width="{PHOTO_W}" height="{PHOTO_H}"
        rx="16" fill="none" stroke="url(#neon)" stroke-width="1.8" opacity="0.75"/>

  <!-- Live status dot on photo -->
  <circle cx="{PHOTO_X+16}" cy="{PHOTO_Y+16}" r="7" fill="#00ea64" class="green-dot"/>
  <circle cx="{PHOTO_X+16}" cy="{PHOTO_Y+16}" r="3.5" fill="#ffffff"/>

  <!-- ===== RIGHT: ABOUT ME (with slide animation) ===== -->
  <g clip-path="url(#panelClip)">

    <!-- Section heading -->
    <text x="{PANEL_X}" y="52"
          font-family="Segoe UI, system-ui, sans-serif"
          font-weight="800" font-size="22"
          fill="#ffffff" letter-spacing="0.5">About Me</text>

    <!-- Underline accent -->
    <line x1="{PANEL_X}" y1="60" x2="{PANEL_X+100}" y2="60"
          stroke="url(#neon)" stroke-width="2" opacity="0.8"/>

    {rows_svg}
  </g>

</svg>"""

with open('assets/profile-banner.svg', 'w', encoding='utf-8') as f:
    f.write(svg)

print('Done! Written assets/profile-banner.svg')
print('SVG size:', len(svg.encode()) // 1024, 'KB')
