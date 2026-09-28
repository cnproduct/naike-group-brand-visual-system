#!/usr/bin/env python3
"""
Brand Physical & Stationery SVG Generator (stationery_generator.py)
-------------------------------------------------------------------
Generates production-grade, print-ready vector SVGs for corporate stationery:
1. Double-sided Business Card (90mm x 54mm @ 300DPI equivalent)
2. Employee ID Badge & Lanyard (54mm x 85mm standard CR80 format)
3. Conference Room Glass Partition Frosted Film (1500mm x 200mm stripe)
4. Standard Roll-up Banner (800mm x 2000mm 1:2.5 presentation display)
"""

import os
import sys
import json

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

def generate_business_card_front(tokens, output_path):
    primary = tokens["color_palette"]["primary"]["hex"]
    secondary = tokens["color_palette"]["secondary"]["hex"]
    accent = tokens["color_palette"]["accent_cta"]["hex"]
    dark = tokens["color_palette"]["surface_dark"]["hex"]
    name = tokens["brand_meta"]["name"]

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1062 638" width="1062" height="638">
  <defs>
    <linearGradient id="cardBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{dark}" />
      <stop offset="100%" stop-color="#020617" />
    </linearGradient>
    <linearGradient id="accentLine" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{primary}" />
      <stop offset="50%" stop-color="{accent}" />
      <stop offset="100%" stop-color="{secondary}" />
    </linearGradient>
    <pattern id="gridPattern" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="rgba(255,255,255,0.03)" stroke-width="1"/>
    </pattern>
  </defs>

  <!-- Background -->
  <rect width="1062" height="638" rx="24" fill="url(#cardBg)"/>
  <rect width="1062" height="638" rx="24" fill="url(#gridPattern)"/>

  <!-- Decorative dynamic brand angle -->
  <path d="M 750 0 L 1062 0 L 1062 638 L 880 638 Z" fill="{primary}" opacity="0.08"/>
  <path d="M 880 0 L 1062 0 L 1062 450 Z" fill="{accent}" opacity="0.05"/>
  <line x1="0" y1="630" x2="1062" y2="630" stroke="url(#accentLine)" stroke-width="8"/>

  <!-- Logo Mark Graphic -->
  <g transform="translate(100, 240)">
    <rect width="72" height="72" rx="18" fill="{primary}"/>
    <circle cx="36" cy="36" r="18" fill="{accent}"/>
    <path d="M 28 36 L 44 36 M 36 28 L 36 44" stroke="#FFFFFF" stroke-width="4" stroke-linecap="round"/>
    <!-- Brand Typography -->
    <text x="96" y="46" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="42" font-weight="800" fill="#FFFFFF" letter-spacing="1">{name}</text>
    <text x="98" y="74" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="600" fill="{secondary}" letter-spacing="4">ENTERPRISE GLOBAL VI</text>
  </g>

  <!-- Anti-counterfeiting microchip pill -->
  <rect x="910" y="80" width="52" height="40" rx="8" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.15)" stroke-width="1.5"/>
  <circle cx="936" cy="100" r="8" fill="none" stroke="{accent}" stroke-width="1.5"/>
</svg>"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg_content)

def generate_business_card_back(tokens, output_path):
    primary = tokens["color_palette"]["primary"]["hex"]
    secondary = tokens["color_palette"]["secondary"]["hex"]
    accent = tokens["color_palette"]["accent_cta"]["hex"]
    light_bg = tokens["color_palette"]["canvas_light"]["hex"]
    dark = tokens["color_palette"]["surface_dark"]["hex"]
    name = tokens["brand_meta"]["name"]

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1062 638" width="1062" height="638">
  <defs>
    <linearGradient id="cardBackBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{light_bg}" />
      <stop offset="100%" stop-color="#FFFFFF" />
    </linearGradient>
  </defs>

  <rect width="1062" height="638" rx="24" fill="url(#cardBackBg)" stroke="rgba(0,0,0,0.06)" stroke-width="2"/>

  <!-- Left Accent Accent Line -->
  <rect x="0" y="0" width="16" height="638" rx="8" fill="{primary}"/>
  <rect x="16" y="180" width="6" height="240" rx="3" fill="{accent}"/>

  <!-- Person Info -->
  <g transform="translate(100, 150)">
    <text x="0" y="40" font-family="'PingFang SC', sans-serif" font-size="38" font-weight="700" fill="{dark}">陈晨 / Chen Chen</text>
    <text x="0" y="80" font-family="-apple-system, sans-serif" font-size="18" font-weight="600" fill="{primary}" letter-spacing="1">VP of Global Brand &amp; Product Strategy</text>
    <line x1="0" y1="110" x2="480" y2="110" stroke="rgba(0,0,0,0.08)" stroke-width="1.5"/>

    <!-- Contact details -->
    <g transform="translate(0, 150)" font-family="-apple-system, sans-serif" font-size="16" fill="#475569">
      <text x="0" y="0">📱 +86 186-0000-8888 / +1 (800) 888-0199</text>
      <text x="0" y="36">✉️ contact@{name.lower().replace(' ', '')}.com</text>
      <text x="0" y="72">🌐 www.{name.lower().replace(' ', '')}.com</text>
      <text x="0" y="108">📍 High-Tech Innovation Center, Tower A, 28F</text>
    </g>
  </g>

  <!-- QR Code Mockup Frame -->
  <g transform="translate(840, 360)">
    <rect width="130" height="130" rx="12" fill="#FFFFFF" stroke="rgba(0,0,0,0.08)" stroke-width="2"/>
    <rect x="15" y="15" width="40" height="40" fill="{dark}"/>
    <rect x="75" y="15" width="40" height="40" fill="{dark}"/>
    <rect x="15" y="75" width="40" height="40" fill="{dark}"/>
    <rect x="25" y="25" width="20" height="20" fill="#FFFFFF"/>
    <rect x="85" y="25" width="20" height="20" fill="#FFFFFF"/>
    <rect x="25" y="85" width="20" height="20" fill="#FFFFFF"/>
    <rect x="70" y="70" width="45" height="45" fill="{primary}" opacity="0.8"/>
    <text x="65" y="160" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="12" font-weight="600" fill="#94A3B8">SCAN CONTACT</text>
  </g>
</svg>"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg_content)

def generate_frosted_film(tokens, output_path):
    primary = tokens["color_palette"]["primary"]["hex"]
    secondary = tokens["color_palette"]["secondary"]["hex"]
    accent = tokens["color_palette"]["accent_cta"]["hex"]
    name = tokens["brand_meta"]["name"]

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 240" width="1600" height="240">
  <defs>
    <linearGradient id="frostGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="rgba(255,255,255,0.15)"/>
      <stop offset="30%" stop-color="rgba(255,255,255,0.75)"/>
      <stop offset="70%" stop-color="rgba(255,255,255,0.75)"/>
      <stop offset="100%" stop-color="rgba(255,255,255,0.15)"/>
    </linearGradient>
  </defs>

  <!-- Glass panel background -->
  <rect width="1600" height="240" fill="#E2E8F0" opacity="0.3"/>
  <!-- Sandblasted frosted waist film -->
  <rect y="20" width="1600" height="200" fill="url(#frostGrad)"/>
  
  <!-- Optical clear line cuts -->
  <line x1="0" y1="28" x2="1600" y2="28" stroke="{primary}" stroke-width="2.5" opacity="0.8"/>
  <line x1="0" y1="212" x2="1600" y2="212" stroke="{accent}" stroke-width="2" opacity="0.6"/>

  <!-- Repeating cutout logo motifs -->
  <g transform="translate(150, 80)">
    <rect width="40" height="40" rx="10" fill="{primary}"/>
    <circle cx="20" cy="20" r="10" fill="{accent}"/>
    <text x="54" y="28" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" fill="#334155" letter-spacing="2">{name}</text>
  </g>
  <g transform="translate(650, 80)">
    <rect width="40" height="40" rx="10" fill="{primary}"/>
    <circle cx="20" cy="20" r="10" fill="{accent}"/>
    <text x="54" y="28" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" fill="#334155" letter-spacing="2">{name}</text>
  </g>
  <g transform="translate(1150, 80)">
    <rect width="40" height="40" rx="10" fill="{primary}"/>
    <circle cx="20" cy="20" r="10" fill="{accent}"/>
    <text x="54" y="28" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" fill="#334155" letter-spacing="2">{name}</text>
  </g>
</svg>"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg_content)

def generate_rollup_banner(tokens, output_path):
    primary = tokens["color_palette"]["primary"]["hex"]
    secondary = tokens["color_palette"]["secondary"]["hex"]
    accent = tokens["color_palette"]["accent_cta"]["hex"]
    dark = tokens["color_palette"]["surface_dark"]["hex"]
    name = tokens["brand_meta"]["name"]

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 2000" width="800" height="2000">
  <defs>
    <linearGradient id="bannerBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="{dark}"/>
      <stop offset="60%" stop-color="#090D16"/>
      <stop offset="100%" stop-color="#020617"/>
    </linearGradient>
    <linearGradient id="glowLine" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{primary}"/>
      <stop offset="100%" stop-color="{accent}"/>
    </linearGradient>
  </defs>

  <!-- Background -->
  <rect width="800" height="2000" fill="url(#bannerBg)"/>

  <!-- Geometric Super-graphic shapes -->
  <circle cx="800" cy="400" r="500" fill="{primary}" opacity="0.12"/>
  <circle cx="0" cy="1200" r="400" fill="{secondary}" opacity="0.08"/>
  <path d="M 0 600 L 800 900 L 800 950 L 0 650 Z" fill="url(#glowLine)" opacity="0.25"/>

  <!-- Header Brand Lockup -->
  <g transform="translate(80, 120)">
    <rect width="64" height="64" rx="16" fill="{primary}"/>
    <circle cx="32" cy="32" r="16" fill="{accent}"/>
    <text x="84" y="44" font-family="-apple-system, sans-serif" font-size="36" font-weight="800" fill="#FFFFFF" letter-spacing="1">{name}</text>
  </g>

  <!-- Main Value Proposition / Launch Headline -->
  <g transform="translate(80, 420)">
    <rect width="200" height="36" rx="8" fill="{primary}" opacity="0.2"/>
    <text x="16" y="24" font-family="-apple-system, sans-serif" font-size="16" font-weight="700" fill="{primary}" letter-spacing="2">GLOBAL PRODUCT LAUNCH</text>
    
    <text x="0" y="110" font-family="'PingFang SC', sans-serif" font-size="56" font-weight="800" fill="#FFFFFF" line-height="1.2">
      <tspan x="0" dy="0">智汇全球 · 破界生长</tspan>
      <tspan x="0" dy="72" fill="{accent}">NEXT-GEN VI SYSTEM</tspan>
    </text>
    
    <text x="0" y="250" font-family="'PingFang SC', sans-serif" font-size="22" font-weight="400" fill="#94A3B8" width="640">
      全链路自进化数字资产与空间导视系统 · 驱动企业全球化增长
    </text>
  </g>

  <!-- Core Pillars / Cards -->
  <g transform="translate(80, 850)">
    <!-- Card 1 -->
    <rect width="640" height="150" rx="20" fill="rgba(255,255,255,0.04)" stroke="rgba(255,255,255,0.08)" stroke-width="1.5"/>
    <circle cx="60" cy="75" r="28" fill="{primary}" opacity="0.2"/>
    <text x="60" y="83" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="24" font-weight="700" fill="{primary}">01</text>
    <text x="110" y="65" font-family="'PingFang SC', sans-serif" font-size="24" font-weight="700" fill="#FFFFFF">全端数字自适应</text>
    <text x="110" y="100" font-family="-apple-system, sans-serif" font-size="16" fill="#94A3B8">Web Tokens · App Icon · 响应式官网 · PPT母版</text>

    <!-- Card 2 -->
    <g transform="translate(0, 180)">
      <rect width="640" height="150" rx="20" fill="rgba(255,255,255,0.04)" stroke="rgba(255,255,255,0.08)" stroke-width="1.5"/>
      <circle cx="60" cy="75" r="28" fill="{accent}" opacity="0.2"/>
      <text x="60" y="83" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="24" font-weight="700" fill="{accent}">02</text>
      <text x="110" y="65" font-family="'PingFang SC', sans-serif" font-size="24" font-weight="700" fill="#FFFFFF">线下实体空间导视</text>
      <text x="110" y="100" font-family="-apple-system, sans-serif" font-size="16" fill="#94A3B8">门头标牌 · 前台形象墙 · 会议室磨砂 · 走廊文化墙</text>
    </g>

    <!-- Card 3 -->
    <g transform="translate(0, 360)">
      <rect width="640" height="150" rx="20" fill="rgba(255,255,255,0.04)" stroke="rgba(255,255,255,0.08)" stroke-width="1.5"/>
      <circle cx="60" cy="75" r="28" fill="{secondary}" opacity="0.2"/>
      <text x="60" y="83" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="24" font-weight="700" fill="{secondary}">03</text>
      <text x="110" y="65" font-family="'PingFang SC', sans-serif" font-size="24" font-weight="700" fill="#FFFFFF">大型发布会主视觉</text>
      <text x="110" y="100" font-family="-apple-system, sans-serif" font-size="16" fill="#94A3B8">舞台巨幕KV · 签到背板 · 嘉宾挂绳 · 伴手礼盒</text>
    </g>
  </g>

  <!-- Bottom Action Footer & QR -->
  <g transform="translate(80, 1680)">
    <line x1="0" y1="0" x2="640" y2="0" stroke="rgba(255,255,255,0.1)" stroke-width="1"/>
    <text x="0" y="60" font-family="'PingFang SC', sans-serif" font-size="20" font-weight="600" fill="#FFFFFF">即刻体验全方位品牌视觉生态</text>
    <text x="0" y="95" font-family="-apple-system, sans-serif" font-size="16" fill="#64748B">扫码获取完整品牌 VI 指南与数字资产包</text>
    <!-- QR Code Box -->
    <rect x="490" y="20" width="150" height="150" rx="16" fill="#FFFFFF"/>
    <rect x="510" y="40" width="40" height="40" fill="{dark}"/>
    <rect x="580" y="40" width="40" height="40" fill="{dark}"/>
    <rect x="510" y="110" width="40" height="40" fill="{dark}"/>
    <rect x="520" y="50" width="20" height="20" fill="#FFFFFF"/>
    <rect x="590" y="50" width="20" height="20" fill="#FFFFFF"/>
    <rect x="520" y="120" width="20" height="20" fill="#FFFFFF"/>
    <rect x="575" y="105" width="45" height="45" fill="{primary}"/>
  </g>
</svg>"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg_content)

def generate_employee_badge(tokens, output_path):
    primary = tokens["color_palette"]["primary"]["hex"]
    accent = tokens["color_palette"]["accent_cta"]["hex"]
    dark = tokens["color_palette"]["surface_dark"]["hex"]
    name = tokens["brand_meta"]["name"]

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 638 1004" width="638" height="1004">
  <defs>
    <linearGradient id="badgeBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF" />
      <stop offset="100%" stop-color="#F1F5F9" />
    </linearGradient>
  </defs>

  <!-- Lanyard punch slot -->
  <rect x="259" y="30" width="120" height="20" rx="10" fill="#CBD5E1"/>

  <!-- Badge Card Container -->
  <rect x="20" y="70" width="598" height="910" rx="28" fill="url(#badgeBg)" stroke="rgba(0,0,0,0.08)" stroke-width="2"/>

  <!-- Top Brand Banner -->
  <path d="M 20 98 Q 20 70 48 70 L 590 70 Q 618 70 618 98 L 618 200 L 20 200 Z" fill="{primary}"/>
  <line x1="20" y1="200" x2="618" y2="200" stroke="{accent}" stroke-width="6"/>

  <!-- Logo lockup in banner -->
  <g transform="translate(60, 110)">
    <rect width="48" height="48" rx="12" fill="#FFFFFF"/>
    <circle cx="24" cy="24" r="12" fill="{primary}"/>
    <text x="64" y="34" font-family="-apple-system, sans-serif" font-size="28" font-weight="800" fill="#FFFFFF">{name}</text>
  </g>

  <!-- Photo Holder -->
  <g transform="translate(209, 280)">
    <circle cx="110" cy="110" r="110" fill="#E2E8F0" stroke="{primary}" stroke-width="6"/>
    <!-- Avatar silhouette -->
    <circle cx="110" cy="90" r="44" fill="#94A3B8"/>
    <path d="M 50 190 Q 110 130 170 190 Z" fill="#94A3B8"/>
  </g>

  <!-- Employee Name & Details -->
  <g transform="translate(319, 570)" text-anchor="middle">
    <text y="0" font-family="'PingFang SC', sans-serif" font-size="36" font-weight="700" fill="{dark}">张伟 / David Zhang</text>
    <text y="40" font-family="-apple-system, sans-serif" font-size="18" font-weight="600" fill="{primary}" letter-spacing="1">SENIOR CHIEF ARCHITECT</text>
    <rect x="-80" y="65" width="160" height="32" rx="16" fill="{accent}" opacity="0.2"/>
    <text y="87" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="{accent}">ID: REN-202609</text>
  </g>

  <!-- Barcode / NFC chip zone -->
  <g transform="translate(70, 770)">
    <rect width="498" height="140" rx="16" fill="#FFFFFF" stroke="rgba(0,0,0,0.06)" stroke-width="1.5"/>
    <text x="30" y="45" font-family="-apple-system, sans-serif" font-size="14" font-weight="600" fill="#64748B">DEPARTMENT: AI &amp; DIGITAL ASSET LAB</text>
    <text x="30" y="75" font-family="-apple-system, sans-serif" font-size="14" font-weight="600" fill="#64748B">SECURITY CLEARANCE: LEVEL 4 (ALL ACCESS)</text>
    <!-- Barcode stripes -->
    <g transform="translate(30, 95)" fill="{dark}">
      <rect x="0" width="4" height="30"/>
      <rect x="8" width="8" height="30"/>
      <rect x="20" width="3" height="30"/>
      <rect x="28" width="6" height="30"/>
      <rect x="40" width="12" height="30"/>
      <rect x="58" width="4" height="30"/>
      <rect x="68" width="9" height="30"/>
      <rect x="85" width="4" height="30"/>
      <rect x="95" width="7" height="30"/>
      <rect x="110" width="5" height="30"/>
      <rect x="125" width="14" height="30"/>
      <rect x="145" width="4" height="30"/>
      <rect x="155" width="8" height="30"/>
      <rect x="170" width="6" height="30"/>
      <rect x="185" width="10" height="30"/>
      <rect x="205" width="4" height="30"/>
      <rect x="220" width="8" height="30"/>
      <rect x="240" width="6" height="30"/>
    </g>
  </g>
</svg>"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg_content)

def generate_all_stationery(tokens, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    generate_business_card_front(tokens, os.path.join(output_dir, "business_card_front.svg"))
    generate_business_card_back(tokens, os.path.join(output_dir, "business_card_back.svg"))
    generate_frosted_film(tokens, os.path.join(output_dir, "meeting_room_frosted_film.svg"))
    generate_rollup_banner(tokens, os.path.join(output_dir, "rollup_banner.svg"))
    generate_employee_badge(tokens, os.path.join(output_dir, "employee_badge.svg"))
    print(f"[✓] Successfully generated 5 physical stationery vector SVGs in: {output_dir}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 stationery_generator.py <tokens_json_path> <output_dir>")
        sys.exit(1)
    with open(sys.argv[1], "r", encoding="utf-8") as f:
        tokens = json.load(f)
    generate_all_stationery(tokens, sys.argv[2])
