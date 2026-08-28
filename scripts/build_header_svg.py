import base64
import os

os.makedirs('assets', exist_ok=True)

with open('assets/ashwin-portrait.jpg', 'rb') as f:
    img_b64 = base64.b64encode(f.read()).decode('utf-8')

svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 370" width="100%" height="100%">
  <defs>
    <!-- Gradients -->
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0a0514" />
      <stop offset="50%" stop-color="#150a24" />
      <stop offset="100%" stop-color="#080410" />
    </linearGradient>

    <linearGradient id="panelGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1a0c2e" stop-opacity="0.92" />
      <stop offset="100%" stop-color="#0e061a" stop-opacity="0.96" />
    </linearGradient>

    <linearGradient id="neonBorder" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#c84bff">
        <animate attributeName="stop-color" values="#c84bff;#00f5ff;#ff3b5c;#c84bff" dur="8s" repeatCount="indefinite" />
      </stop>
      <stop offset="50%" stop-color="#00f5ff">
        <animate attributeName="stop-color" values="#00f5ff;#ff3b5c;#c84bff;#00f5ff" dur="8s" repeatCount="indefinite" />
      </stop>
      <stop offset="100%" stop-color="#ff3b5c">
        <animate attributeName="stop-color" values="#ff3b5c;#c84bff;#00f5ff;#ff3b5c" dur="8s" repeatCount="indefinite" />
      </stop>
    </linearGradient>

    <linearGradient id="nameGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ffffff" />
      <stop offset="50%" stop-color="#f0d5ff" />
      <stop offset="100%" stop-color="#00f5ff" />
    </linearGradient>

    <!-- Filters -->
    <filter id="neonGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="5" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>

    <filter id="softGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.5" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>

    <!-- Clip Path for Photo -->
    <clipPath id="photoClip">
      <rect x="28" y="28" width="255" height="314" rx="16" />
    </clipPath>

    <style>
      .mono-title {{
        font-family: 'Consolas', 'Fira Code', 'Courier New', monospace;
        font-weight: 700;
        font-size: 13px;
        letter-spacing: 1px;
      }}
      .name-text {{
        font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
        font-weight: 800;
        font-size: 26px;
        letter-spacing: 0.5px;
      }}
      .section-label {{
        font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
        font-weight: 700;
        font-size: 11px;
        letter-spacing: 1px;
      }}
      .body-text {{
        font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
        font-weight: 600;
        font-size: 13.5px;
        fill: #f5f0ff;
      }}
      .sub-text {{
        font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
        font-weight: 500;
        font-size: 12.5px;
        fill: #bda6d8;
      }}
      .cmd-text {{
        font-family: 'Consolas', 'Fira Code', 'Courier New', monospace;
        font-size: 12px;
        fill: #00f5ff;
      }}
      .badge-text {{
        font-family: 'Consolas', 'Fira Code', 'Segoe UI', monospace;
        font-weight: 700;
        font-size: 10px;
        letter-spacing: 0.5px;
      }}
      .laser-border {{
        stroke-dasharray: 90 400;
        animation: laserScan 6s linear infinite;
      }}
      @keyframes laserScan {{
        0% {{ stroke-dashoffset: 0; }}
        100% {{ stroke-dashoffset: -1000; }}
      }}
      @keyframes blink {{
        0%, 100% {{ opacity: 1; }}
        50% {{ opacity: 0; }}
      }}
      .blinking-cursor {{
        animation: blink 1s step-start infinite;
      }}
      @keyframes pulseEffect {{
        0%, 100% {{ opacity: 0.4; }}
        50% {{ opacity: 1; }}
      }}
      .pulse {{
        animation: pulseEffect 2.5s ease-in-out infinite;
      }}
    </style>
  </defs>

  <!-- Outer Base Card -->
  <rect x="2" y="2" width="996" height="366" rx="20" fill="url(#bgGrad)" stroke="#261340" stroke-width="1.5" />

  <!-- Animated Neon Border -->
  <rect x="2" y="2" width="996" height="366" rx="20" fill="none" stroke="url(#neonBorder)" stroke-width="2" class="laser-border" filter="url(#neonGlow)" />

  <!-- Corner Tech Accents -->
  <path d="M 18 10 L 10 10 L 10 18" fill="none" stroke="#00f5ff" stroke-width="2.5" />
  <path d="M 982 10 L 990 10 L 990 18" fill="none" stroke="#ff3b5c" stroke-width="2.5" />
  <path d="M 18 360 L 10 360 L 10 352" fill="none" stroke="#c84bff" stroke-width="2.5" />
  <path d="M 982 360 L 990 360 L 990 352" fill="none" stroke="#00f5ff" stroke-width="2.5" />

  <!-- ================= LEFT: USER PHOTO FRAME ================= -->
  <g>
    <!-- Photo Shadow and Background -->
    <rect x="26" y="26" width="259" height="318" rx="17" fill="#120822" stroke="#7b2cbf" stroke-width="1.5" />
    
    <!-- Real High-Res Photo of Ashwin -->
    <image href="data:image/jpeg;base64,{img_b64}" x="28" y="28" width="255" height="314" preserveAspectRatio="xMidYMid slice" clip-path="url(#photoClip)" />

    <!-- Photo Overlay Glow Border -->
    <rect x="28" y="28" width="255" height="314" rx="16" fill="none" stroke="url(#neonBorder)" stroke-width="1.8" opacity="0.85" />

    <!-- Live Status Dot on Photo -->
    <circle cx="48" cy="48" r="7" fill="#00ea64" filter="url(#softGlow)" />
    <circle cx="48" cy="48" r="3.5" fill="#ffffff" />
  </g>

  <!-- ================= RIGHT: RESTYLED CRISP INFO HUD ================= -->
  <g transform="translate(305, 26)">
    <!-- Panel Background -->
    <rect width="665" height="318" rx="16" fill="url(#panelGrad)" stroke="#4a2074" stroke-width="1.2" />

    <!-- Window Top Header Bar -->
    <path d="M 0 16 C 0 7.16 7.16 0 16 0 L 649 0 C 657.84 0 665 7.16 665 16 L 665 38 L 0 38 Z" fill="#120822" />
    <line x1="0" y1="38" x2="665" y2="38" stroke="#381758" stroke-width="1" />
    
    <!-- Mac OS Window Dots -->
    <circle cx="20" cy="19" r="5.5" fill="#ff5f56" />
    <circle cx="36" cy="19" r="5.5" fill="#ffbd2e" />
    <circle cx="52" cy="19" r="5.5" fill="#27c93f" />
    
    <text x="72" y="23" fill="#00f5ff" class="mono-title">// SYSTEM_PROFILE_v3.2 [ONLINE]</text>

    <!-- Status Active Pill in Header Right -->
    <rect x="545" y="10" width="104" height="18" rx="9" fill="#0a2e16" stroke="#00ea64" stroke-width="0.8" />
    <circle cx="556" cy="19" r="3.5" fill="#00ea64" class="pulse" />
    <text x="564" y="22" fill="#00ea64" class="badge-text">STATUS: ACTIVE</text>

    <!-- CONTENT BODY -->
    <!-- Name -->
    <text x="24" y="72" fill="url(#nameGrad)" class="name-text">ASHWIN KUMAR L</text>

    <!-- Section 1: Department -->
    <g transform="translate(24, 94)">
      <rect width="24" height="24" rx="6" fill="#00f5ff" fill-opacity="0.15" stroke="#00f5ff" stroke-width="0.8" />
      <!-- Graduation Cap Vector Icon -->
      <path d="M 5 10 L 12 6 L 19 10 L 12 14 Z M 8 12.5 L 8 16 C 8 17.5 16 17.5 16 16 L 16 12.5" fill="none" stroke="#00f5ff" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" />
      <text x="34" y="11" fill="#00f5ff" class="section-label">DEPARTMENT</text>
      <text x="34" y="25" class="body-text">B.E. Computer Science &amp; Engineering</text>
    </g>

    <!-- Section 2: Institution -->
    <g transform="translate(24, 134)">
      <rect width="24" height="24" rx="6" fill="#c84bff" fill-opacity="0.15" stroke="#c84bff" stroke-width="0.8" />
      <!-- Building/University Vector Icon -->
      <path d="M 6 18 L 6 10 L 12 6 L 18 10 L 18 18 Z M 10 18 L 10 13 L 14 13 L 14 18" fill="none" stroke="#c84bff" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" />
      <text x="34" y="11" fill="#c84bff" class="section-label">INSTITUTION</text>
      <text x="34" y="25" class="sub-text">Sri Ramakrishna Engineering College, Coimbatore</text>
    </g>

    <!-- Section 3: Domain Focus -->
    <g transform="translate(24, 174)">
      <rect width="24" height="24" rx="6" fill="#ffd700" fill-opacity="0.15" stroke="#ffd700" stroke-width="0.8" />
      <!-- Lightning Vector Icon -->
      <path d="M 13 5 L 7 13 L 12 13 L 11 19 L 17 11 L 12 11 Z" fill="#ffd700" stroke="#ffd700" stroke-width="0.5" />
      <text x="34" y="11" fill="#ffd700" class="section-label">DOMAIN FOCUS</text>
      <text x="34" y="25" class="body-text">AI &amp; ML • Computer Vision • Intelligent Systems</text>
    </g>

    <!-- Section 4: Highlights -->
    <g transform="translate(24, 214)">
      <rect width="24" height="24" rx="6" fill="#ff3b5c" fill-opacity="0.15" stroke="#ff3b5c" stroke-width="0.8" />
      <!-- Trophy Vector Icon -->
      <path d="M 7 7 L 17 7 L 17 11 C 17 14 14.5 15.5 12 15.5 C 9.5 15.5 7 14 7 11 Z M 12 15.5 L 12 18 M 9 18 L 15 18" fill="none" stroke="#ff3b5c" stroke-width="1.3" stroke-linecap="round" />
      <text x="34" y="11" fill="#ff3b5c" class="section-label">HIGHLIGHTS</text>
      <text x="34" y="25" class="sub-text">150+ LeetCode • Python 5★ Gold • Kick Start (Ideathon 1st) • Code Rush 2nd</text>
    </g>

    <!-- Interactive Terminal Command Bar -->
    <g transform="translate(24, 248)">
      <rect width="617" height="26" rx="7" fill="#0a0412" stroke="#381854" stroke-width="1" />
      <text x="12" y="17" class="cmd-text">ashwin@ai-core:~$ build_profile --render</text>
      <rect x="305" y="7" width="7" height="13" fill="#00f5ff" class="blinking-cursor" />
    </g>

    <!-- Bottom Status Badges -->
    <g transform="translate(24, 284)">
      <!-- Badge 1: AI/ML DEV -->
      <rect x="0" y="0" width="92" height="22" rx="6" fill="#220d38" stroke="#c84bff" stroke-width="1" />
      <text x="46" y="14" text-anchor="middle" fill="#e4b5ff" class="badge-text">AI/ML DEV</text>

      <!-- Badge 2: PYTHON 5★ -->
      <rect x="100" y="0" width="100" height="22" rx="6" fill="#0a2816" stroke="#00ea64" stroke-width="1" />
      <text x="150" y="14" text-anchor="middle" fill="#7affb2" class="badge-text">PYTHON 5★</text>

      <!-- Badge 3: LEETCODE 150+ -->
      <rect x="208" y="0" width="120" height="22" rx="6" fill="#2b1805" stroke="#ffa116" stroke-width="1" />
      <text x="268" y="14" text-anchor="middle" fill="#ffd28a" class="badge-text">LEETCODE 150+</text>

      <!-- Badge 4: IDEATHON 1ST -->
      <rect x="336" y="0" width="112" height="22" rx="6" fill="#08202b" stroke="#00f5ff" stroke-width="1" />
      <text x="392" y="14" text-anchor="middle" fill="#85f6ff" class="badge-text">IDEATHON 1ST</text>

      <!-- Badge 5: CODE RUSH 2ND -->
      <rect x="456" y="0" width="120" height="22" rx="6" fill="#2b0814" stroke="#ff3b5c" stroke-width="1" />
      <text x="516" y="14" text-anchor="middle" fill="#ff94a8" class="badge-text">CODE RUSH 2ND</text>
    </g>
  </g>
</svg>'''

with open('assets/header.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)
with open('assets/profile-header.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)
print('Generated assets/header.svg and assets/profile-header.svg successfully!')
