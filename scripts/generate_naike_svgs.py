#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Production-grade Vector SVG Generator for NAIKE GROUP Brand Identity
Generates:
1. logo_naike_mark.svg (Master Badge)
2. logo_naike_horizontal.svg (Horizontal Master Lockup)
3. logo_naike_vertical.svg (Vertical Master Lockup)
4. business_card_front.svg (90x54mm Luxury Dark Card)
5. business_card_back.svg (90x54mm Corporate Light Info Card)
6. employee_badge.svg (54x85mm CR80 Smart ID & Lanyard)
7. meeting_room_frosted_film.svg (200mm Privacy Frosted Film)
8. rollup_banner.svg (800x2000mm Trade Show Rollup)
9. ios_app_icon_1024.svg (iOS App Store 1024 Icon)
10. android_adaptive_background.svg & foreground.svg
11. favicon.svg (Web Favicon)
"""

import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

# Reusable SVG fragment for the Naike Badge interior (size normalized to 400x400)
def get_naike_badge_def():
    return """
  <defs>
    <!-- Background Red Gradient -->
    <linearGradient id="naikeRedGrad" x1="0%" y1="0%" x2="40%" y2="100%">
      <stop offset="0%" stop-color="#E0221B"/>
      <stop offset="60%" stop-color="#B70005"/>
      <stop offset="100%" stop-color="#8E0003"/>
    </linearGradient>

    <!-- Background Blue Gradient -->
    <linearGradient id="naikeBlueGrad" x1="20%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0066CC"/>
      <stop offset="50%" stop-color="#004B98"/>
      <stop offset="100%" stop-color="#002868"/>
    </linearGradient>

    <!-- Golden Sparkle Glow -->
    <filter id="starGlow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="2" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <!-- Subtle Drop Shadow for 3D depth -->
    <filter id="badgeShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="rgba(0,0,0,0.25)"/>
    </filter>
  </defs>
"""

# The core badge graphic normalized in a 400x400 viewBox
def get_naike_badge_symbol(size=400):
    return f"""
    <!-- Squircle Container with Clip Path -->
    <g id="naikeBadgeGraphic">
      <clipPath id="squircleClip">
        <rect x="0" y="0" width="400" height="400" rx="90" ry="90" />
      </clipPath>

      <g clip-path="url(#squircleClip)">
        <!-- Top Crimson Background -->
        <rect x="0" y="0" width="400" height="400" fill="url(#naikeRedGrad)"/>

        <!-- Bottom Dynamic Ocean Blue Wave/Field -->
        <path d="M -20 220 C 120 240, 180 180, 420 150 L 420 420 L -20 420 Z" fill="url(#naikeBlueGrad)"/>

        <!-- Stylized White Dynamic 'n' Arch -->
        <!-- Left Stem: Tilted Pillar with forward slant -->
        <path d="M 125 105 L 165 105 L 115 305 L 75 305 Z" fill="#FFFFFF"/>

        <!-- Forward Sweeping Arch Bridge & Right Leg -->
        <path d="M 152 185 C 190 120, 290 120, 310 180 C 315 195, 305 240, 295 305 L 255 305 C 265 245, 272 198, 258 178 C 242 155, 178 160, 142 225 Z" fill="#FFFFFF"/>

        <!-- Four-Point Precision Sparkle Star -->
        <!-- Center of star at (315, 125) -->
        <g transform="translate(315, 125)" filter="url(#starGlow)">
          <path d="M 0 -28 Q 0 0, 28 0 Q 0 0, 0 28 Q 0 0, -28 0 Q 0 0, 0 -28 Z" fill="#FFFFFF"/>
          <circle cx="0" cy="0" r="3.5" fill="#FFB800"/>
        </g>
      </g>

      <!-- Inner Ambient Specular Highlight Line -->
      <rect x="3" y="3" width="394" height="394" rx="88" ry="88" fill="none" stroke="rgba(255,255,255,0.22)" stroke-width="3"/>
    </g>
"""

def generate_logo_mark(output_path):
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
{get_naike_badge_def()}
  <g transform="translate(56, 56)" filter="url(#badgeShadow)">
    {get_naike_badge_symbol(400)}
  </g>
</svg>"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)

def generate_logo_horizontal(output_path):
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="1200" height="400">
{get_naike_badge_def()}
  <!-- Left Badge -->
  <g transform="translate(60, 60) scale(0.7)" filter="url(#badgeShadow)">
    {get_naike_badge_symbol(400)}
  </g>

  <!-- Right Typography -->
  <g transform="translate(380, 195)">
    <text x="0" y="0" font-family="'Montserrat', 'Helvetica Neue', Arial, sans-serif" font-size="82" font-weight="900" fill="#0F172A" letter-spacing="-1">Naike Group</text>
    <text x="4" y="52" font-family="'Inter', 'PingFang SC', sans-serif" font-size="20" font-weight="700" fill="#B70005" letter-spacing="4">耐科集团 · FACTORY-BACKED PRODUCT DEVELOPMENT</text>
    <line x1="4" y1="74" x2="680" y2="74" stroke="#E2E8F0" stroke-width="2"/>
    <text x="4" y="105" font-family="'Inter', sans-serif" font-size="16" font-weight="500" fill="#64748B" letter-spacing="1.5">GLOBAL CUSTOM GIFTS · REUSABLE TABLEWARE · OEM/ODM</text>
  </g>
</svg>"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)

def generate_logo_vertical(output_path):
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 900" width="800" height="900">
{get_naike_badge_def()}
  <!-- Centered Top Badge -->
  <g transform="translate(200, 100)" filter="url(#badgeShadow)">
    {get_naike_badge_symbol(400)}
  </g>

  <!-- Bottom Centered Wordmark -->
  <g transform="translate(400, 620)" text-anchor="middle">
    <text x="0" y="0" font-family="'Montserrat', 'Helvetica Neue', Arial, sans-serif" font-size="92" font-weight="900" fill="#0F172A" letter-spacing="-1">Naike Group</text>
    <text x="0" y="60" font-family="'PingFang SC', 'Source Han Sans CN', sans-serif" font-size="28" font-weight="700" fill="#B70005" letter-spacing="6">耐 科 集 团</text>
    <text x="0" y="105" font-family="'Inter', sans-serif" font-size="18" font-weight="600" fill="#64748B" letter-spacing="3">SINCE 2008 · WWW.NAIKEGROUP.COM</text>
  </g>
</svg>"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)

def generate_business_card_front(output_path):
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1062 638" width="1062" height="638">
{get_naike_badge_def()}
  <defs>
    <linearGradient id="cardDarkBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#141B2D"/>
      <stop offset="100%" stop-color="#080C14"/>
    </linearGradient>
    <linearGradient id="goldRedLine" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#B70005"/>
      <stop offset="50%" stop-color="#FFB800"/>
      <stop offset="100%" stop-color="#004B98"/>
    </linearGradient>
    <pattern id="cardDotGrid" width="30" height="30" patternUnits="userSpaceOnUse">
      <circle cx="15" cy="15" r="1" fill="rgba(255,255,255,0.04)"/>
    </pattern>
  </defs>

  <!-- Deep Slate Background with Dot Matrix Texture -->
  <rect width="1062" height="638" rx="28" fill="url(#cardDarkBg)"/>
  <rect width="1062" height="638" rx="28" fill="url(#cardDotGrid)"/>

  <!-- Geometric Architectural Accent Glow -->
  <path d="M 720 0 L 1062 0 L 1062 638 L 840 638 Z" fill="#004B98" opacity="0.08"/>
  <path d="M 880 0 L 1062 0 L 1062 380 Z" fill="#B70005" opacity="0.07"/>

  <!-- Bottom Precision Color Bar -->
  <rect x="0" y="626" width="1062" height="12" fill="url(#goldRedLine)"/>

  <!-- Left Main Badge -->
  <g transform="translate(100, 180) scale(0.68)" filter="url(#badgeShadow)">
    {get_naike_badge_symbol(400)}
  </g>

  <!-- Brand Typography -->
  <g transform="translate(420, 290)">
    <text x="0" y="0" font-family="'Montserrat', sans-serif" font-size="54" font-weight="900" fill="#FFFFFF" letter-spacing="-0.5">Naike Group</text>
    <text x="2" y="38" font-family="'PingFang SC', sans-serif" font-size="18" font-weight="700" fill="#FFB800" letter-spacing="4">耐科集团 · 实体智造与全球供应链</text>
    <text x="2" y="70" font-family="'Inter', sans-serif" font-size="14" font-weight="500" fill="#94A3B8" letter-spacing="2">FACTORY-BACKED PRODUCT DEVELOPMENT SINCE 2008</text>
  </g>

  <!-- Microchip Security Anti-counterfeiting Accent -->
  <g transform="translate(930, 80)">
    <rect width="52" height="42" rx="8" fill="rgba(255,255,255,0.04)" stroke="rgba(255,184,0,0.4)" stroke-width="1.5"/>
    <circle cx="26" cy="21" r="8" fill="none" stroke="#FFB800" stroke-width="1.5"/>
    <line x1="8" y1="21" x2="18" y2="21" stroke="#FFB800" stroke-width="1.5"/>
    <line x1="34" y1="21" x2="44" y2="21" stroke="#FFB800" stroke-width="1.5"/>
  </g>
</svg>"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)

def generate_business_card_back(output_path):
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1062 638" width="1062" height="638">
  <defs>
    <linearGradient id="backBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="100%" stop-color="#F8FAFC"/>
    </linearGradient>
  </defs>

  <rect width="1062" height="638" rx="28" fill="url(#backBg)" stroke="#E2E8F0" stroke-width="2"/>

  <!-- Left Accent Vertical Spine -->
  <rect x="0" y="0" width="18" height="638" rx="8" fill="#B70005"/>
  <rect x="18" y="160" width="6" height="260" rx="3" fill="#004B98"/>

  <!-- Executive Info Block -->
  <g transform="translate(90, 130)">
    <text x="0" y="32" font-family="'PingFang SC', sans-serif" font-size="36" font-weight="800" fill="#0F172A">张 敏 <tspan font-family="'Inter', sans-serif" font-size="24" font-weight="600" fill="#64748B">/ Michael Zhang</tspan></text>
    <text x="0" y="70" font-family="'Inter', sans-serif" font-size="16" font-weight="700" fill="#B70005" letter-spacing="1">Director of Global Supply Chain &amp; OEM/ODM Programs</text>
    <text x="0" y="94" font-family="'PingFang SC', sans-serif" font-size="13" font-weight="500" fill="#64748B">全球供应链总监 · 礼品与餐具智造项目部</text>

    <line x1="0" y1="120" x2="520" y2="120" stroke="#E2E8F0" stroke-width="1.5"/>

    <!-- Contact details -->
    <g transform="translate(0, 155)" font-family="'Inter', sans-serif" font-size="15" fill="#334155">
      <text x="0" y="0">📞 +86 (571) 8800-2008 / +86 138-0000-8888</text>
      <text x="0" y="34">✉️ michael.zhang@naikegroup.com</text>
      <text x="0" y="68">🌐 www.naikegroup.com · www.naikegifts.com · www.naiketableware.com</text>
      <text x="0" y="102">📍 NAIKE Industrial Innovation Center, Building 6, High-Tech Park</text>
    </g>
  </g>

  <!-- Right QR & Certifications Block -->
  <g transform="translate(770, 140)">
    <!-- QR Code Box -->
    <rect width="180" height="180" rx="16" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <!-- Simulated QR elements -->
    <rect x="20" y="20" width="44" height="44" fill="#0F172A"/>
    <rect x="28" y="28" width="28" height="28" fill="#FFFFFF"/>
    <rect x="34" y="34" width="16" height="16" fill="#B70005"/>

    <rect x="116" y="20" width="44" height="44" fill="#0F172A"/>
    <rect x="124" y="28" width="28" height="28" fill="#FFFFFF"/>
    <rect x="130" y="34" width="16" height="16" fill="#004B98"/>

    <rect x="20" y="116" width="44" height="44" fill="#0F172A"/>
    <rect x="28" y="124" width="28" height="28" fill="#FFFFFF"/>
    <rect x="34" y="130" width="16" height="16" fill="#0F172A"/>

    <!-- Data matrix dots -->
    <g fill="#334155">
      <rect x="80" y="30" width="14" height="14"/>
      <rect x="74" y="60" width="16" height="16"/>
      <rect x="100" y="80" width="18" height="14"/>
      <rect x="40" y="80" width="14" height="18"/>
      <rect x="80" y="120" width="20" height="12"/>
      <rect x="120" y="100" width="16" height="16"/>
      <rect x="140" y="130" width="14" height="24"/>
      <rect x="110" y="145" width="20" height="15"/>
    </g>
    <!-- Center logo pill -->
    <rect x="72" y="72" width="36" height="36" rx="8" fill="#B70005"/>
    <text x="90" y="96" font-family="'Montserrat', sans-serif" font-size="20" font-weight="900" fill="#FFFFFF" text-anchor="middle">n</text>

    <text x="90" y="215" font-family="'Inter', sans-serif" font-size="12" font-weight="600" fill="#64748B" text-anchor="middle">SCAN FOR E-CATALOG</text>

    <!-- Global Compliance Pills -->
    <g transform="translate(0, 245)">
      <rect x="0" y="0" width="84" height="28" rx="6" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="1"/>
      <text x="42" y="18" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#004B98" text-anchor="middle">ISO 9001</text>

      <rect x="96" y="0" width="84" height="28" rx="6" fill="#FEF2F2" stroke="#FECACA" stroke-width="1"/>
      <text x="138" y="18" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#B70005" text-anchor="middle">SGS AUDIT</text>
    </g>
  </g>
</svg>"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)

def generate_employee_badge(output_path):
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 638 1004" width="638" height="1004">
{get_naike_badge_def()}
  <!-- Lanyard Slot Punch Hole -->
  <rect width="638" height="1004" rx="36" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
  <rect x="259" y="32" width="120" height="22" rx="11" fill="#E2E8F0"/>

  <!-- Top Header Crimson Gradient Banner -->
  <rect x="0" y="80" width="638" height="220" fill="url(#naikeRedGrad)"/>
  <path d="M 0 250 C 200 270, 360 210, 638 190 L 638 300 L 0 300 Z" fill="url(#naikeBlueGrad)" opacity="0.9"/>

  <!-- Center Badge Floating over Header -->
  <g transform="translate(259, 140) scale(0.3)" filter="url(#badgeShadow)">
    {get_naike_badge_symbol(400)}
  </g>
  <text x="319" y="285" font-family="'Montserrat', sans-serif" font-size="28" font-weight="900" fill="#FFFFFF" text-anchor="middle" letter-spacing="1">NAIKE GROUP</text>

  <!-- Photo Box Frame -->
  <g transform="translate(209, 340)">
    <rect width="220" height="260" rx="20" fill="#F1F5F9" stroke="#E2E8F0" stroke-width="3"/>
    <!-- Avatar Silhouette -->
    <circle cx="110" cy="100" r="50" fill="#CBD5E1"/>
    <path d="M 40 240 C 40 180, 180 180, 180 240 Z" fill="#CBD5E1"/>
    <rect x="180" y="10" width="30" height="30" rx="6" fill="#FFB800"/>
    <text x="195" y="30" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0F172A" text-anchor="middle">VIP</text>
  </g>

  <!-- Name & Department -->
  <g transform="translate(319, 660)" text-anchor="middle">
    <text x="0" y="0" font-family="'PingFang SC', sans-serif" font-size="34" font-weight="800" fill="#0F172A">张 敏</text>
    <text x="0" y="36" font-family="'Inter', sans-serif" font-size="20" font-weight="600" fill="#475569">Michael Zhang</text>
    <text x="0" y="74" font-family="'Inter', sans-serif" font-size="16" font-weight="700" fill="#B70005" letter-spacing="1.5">GLOBAL OPERATIONS &amp; EXPORT</text>
    <text x="0" y="102" font-family="'PingFang SC', sans-serif" font-size="14" font-weight="500" fill="#64748B">全球运营与出口管理部 · 工号 NK-200808</text>
  </g>

  <!-- Barcode & Access Security -->
  <g transform="translate(119, 820)">
    <line x1="0" y1="0" x2="400" y2="0" stroke="#E2E8F0" stroke-width="1.5"/>
    <!-- Simulated Code 128 Barcode -->
    <g transform="translate(40, 20)" fill="#0F172A">
      <rect x="0" y="0" width="4" height="60"/>
      <rect x="8" y="0" width="2" height="60"/>
      <rect x="14" y="0" width="6" height="60"/>
      <rect x="24" y="0" width="2" height="60"/>
      <rect x="30" y="0" width="4" height="60"/>
      <rect x="40" y="0" width="8" height="60"/>
      <rect x="52" y="0" width="2" height="60"/>
      <rect x="60" y="0" width="4" height="60"/>
      <rect x="68" y="0" width="6" height="60"/>
      <rect x="80" y="0" width="2" height="60"/>
      <rect x="86" y="0" width="8" height="60"/>
      <rect x="100" y="0" width="4" height="60"/>
      <rect x="110" y="0" width="2" height="60"/>
      <rect x="118" y="0" width="6" height="60"/>
      <rect x="130" y="0" width="4" height="60"/>
      <rect x="140" y="0" width="2" height="60"/>
      <rect x="148" y="0" width="8" height="60"/>
      <rect x="162" y="0" width="4" height="60"/>
      <rect x="172" y="0" width="2" height="60"/>
      <rect x="180" y="0" width="6" height="60"/>
      <rect x="192" y="0" width="4" height="60"/>
      <rect x="202" y="0" width="8" height="60"/>
      <rect x="216" y="0" width="2" height="60"/>
      <rect x="224" y="0" width="4" height="60"/>
      <rect x="234" y="0" width="6" height="60"/>
      <rect x="246" y="0" width="4" height="60"/>
      <rect x="256" y="0" width="2" height="60"/>
      <rect x="264" y="0" width="8" height="60"/>
      <rect x="278" y="0" width="4" height="60"/>
      <rect x="288" y="0" width="2" height="60"/>
      <rect x="296" y="0" width="6" height="60"/>
      <rect x="308" y="0" width="4" height="60"/>
      <rect x="318" y="0" width="2" height="60"/>
    </g>
    <text x="200" y="96" font-family="'JetBrains Mono', monospace" font-size="12" fill="#64748B" text-anchor="middle">NK-8839-2008-GLOBAL-RFID</text>
  </g>

  <!-- Bottom Accent Stripe -->
  <rect x="0" y="990" width="638" height="14" fill="#004B98"/>
</svg>"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)

def generate_meeting_room_frosted_film(output_path):
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 200" width="1600" height="200">
{get_naike_badge_def()}
  <!-- Frosted Glass Background (65% Translucent Simulated) -->
  <defs>
    <linearGradient id="frostedTrans" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="rgba(255, 255, 255, 0.72)"/>
      <stop offset="50%" stop-color="rgba(240, 245, 250, 0.62)"/>
      <stop offset="100%" stop-color="rgba(255, 255, 255, 0.72)"/>
    </linearGradient>
  </defs>

  <rect width="1600" height="200" fill="url(#frostedTrans)"/>

  <!-- Top 2mm Crimson Guide Line -->
  <rect x="0" y="0" width="1600" height="3" fill="#B70005"/>
  <!-- Bottom 2mm Cobalt Blue Guide Line -->
  <rect x="0" y="197" width="1600" height="3" fill="#004B98"/>

  <!-- Repeating Motif 1 (Left 200) -->
  <g transform="translate(180, 50) scale(0.25)">
    {get_naike_badge_symbol(400)}
  </g>
  <text x="310" y="112" font-family="'Montserrat', sans-serif" font-size="28" font-weight="800" fill="#1E293B" opacity="0.85">Naike Group</text>
  <text x="310" y="136" font-family="'Inter', sans-serif" font-size="12" font-weight="600" fill="#B70005" letter-spacing="2">INTELLIGENT BOARDROOM</text>

  <!-- Divider Dashed Line -->
  <line x1="560" y1="40" x2="560" y2="160" stroke="#CBD5E1" stroke-width="1.5" stroke-dasharray="6 6"/>

  <!-- Repeating Motif 2 (Center 700) -->
  <g transform="translate(680, 50) scale(0.25)">
    {get_naike_badge_symbol(400)}
  </g>
  <text x="810" y="112" font-family="'Montserrat', sans-serif" font-size="28" font-weight="800" fill="#1E293B" opacity="0.85">Naike Group</text>
  <text x="810" y="136" font-family="'Inter', sans-serif" font-size="12" font-weight="600" fill="#004B98" letter-spacing="2">CONFIDENTIAL MEETING ZONE</text>

  <!-- Divider Dashed Line -->
  <line x1="1100" y1="40" x2="1100" y2="160" stroke="#CBD5E1" stroke-width="1.5" stroke-dasharray="6 6"/>

  <!-- Repeating Motif 3 (Right 1200) -->
  <g transform="translate(1220, 50) scale(0.25)">
    {get_naike_badge_symbol(400)}
  </g>
  <text x="1350" y="112" font-family="'Montserrat', sans-serif" font-size="28" font-weight="800" fill="#1E293B" opacity="0.85">Naike Group</text>
  <text x="1350" y="136" font-family="'Inter', sans-serif" font-size="12" font-weight="600" fill="#FFB800" letter-spacing="2">GLOBAL EXPORT SUITE</text>
</svg>"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)

def generate_rollup_banner(output_path):
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 2000" width="800" height="2000">
{get_naike_badge_def()}
  <defs>
    <linearGradient id="bannerBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0F172A"/>
      <stop offset="40%" stop-color="#141E33"/>
      <stop offset="100%" stop-color="#090E17"/>
    </linearGradient>
  </defs>

  <!-- Main Canvas -->
  <rect width="800" height="2000" fill="url(#bannerBg)"/>

  <!-- Top Hero Glow & Angled Geometry -->
  <path d="M 0 0 L 800 0 L 800 550 L 0 420 Z" fill="#B70005" opacity="0.12"/>
  <path d="M 0 0 L 600 0 L 0 500 Z" fill="#004B98" opacity="0.18"/>

  <!-- Header Logo & Subtitle -->
  <g transform="translate(100, 120)">
    <g transform="scale(0.55)" filter="url(#badgeShadow)">
      {get_naike_badge_symbol(400)}
    </g>
    <text x="260" y="125" font-family="'Montserrat', sans-serif" font-size="52" font-weight="900" fill="#FFFFFF" letter-spacing="-1">Naike Group</text>
    <text x="264" y="165" font-family="'PingFang SC', sans-serif" font-size="20" font-weight="700" fill="#FFB800" letter-spacing="4">耐科集团 · 始于2008</text>
  </g>

  <!-- Big Catchy Headline -->
  <g transform="translate(100, 420)">
    <text x="0" y="0" font-family="'Montserrat', sans-serif" font-size="44" font-weight="800" fill="#FFFFFF" line-height="1.2">Factory-Backed</text>
    <text x="0" y="56" font-family="'Montserrat', sans-serif" font-size="44" font-weight="800" fill="#FFB800">Product Development.</text>
    <text x="0" y="120" font-family="'PingFang SC', sans-serif" font-size="26" font-weight="600" fill="#E2E8F0">专注全球定制礼品与环保餐具智造</text>
    <text x="0" y="156" font-family="'Inter', sans-serif" font-size="16" fill="#94A3B8">From drawings &amp; molds to rapid sampling and global export.</text>
  </g>

  <!-- Pillar 1: NAIKE GIFTS Card -->
  <g transform="translate(80, 680)">
    <rect width="640" height="280" rx="20" fill="rgba(255,255,255,0.04)" stroke="rgba(255,255,255,0.12)" stroke-width="1.5"/>
    <rect x="0" y="0" width="8" height="280" rx="4" fill="#B70005"/>
    <text x="40" y="55" font-family="'Montserrat', sans-serif" font-size="28" font-weight="800" fill="#FFFFFF">NAIKE GIFTS</text>
    <text x="40" y="90" font-family="'PingFang SC', sans-serif" font-size="18" font-weight="700" fill="#B70005">企业定制礼品与品牌周边</text>
    <text x="40" y="140" font-family="'Inter', sans-serif" font-size="15" fill="#CBD5E1">
      • Drinkware, Tumblers &amp; Vacuum Bottles<br/>
      • Executive Promotional Merchandise<br/>
      • Custom Packaging, Tooling &amp; Rapid Prototypes
    </text>
    <text x="40" y="245" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="600" fill="#FFB800">→ www.naikegifts.com</text>
  </g>

  <!-- Pillar 2: NAIKE TABLEWARE Card -->
  <g transform="translate(80, 1000)">
    <rect width="640" height="280" rx="20" fill="rgba(255,255,255,0.04)" stroke="rgba(255,255,255,0.12)" stroke-width="1.5"/>
    <rect x="0" y="0" width="8" height="280" rx="4" fill="#004B98"/>
    <text x="40" y="55" font-family="'Montserrat', sans-serif" font-size="28" font-weight="800" fill="#FFFFFF">NAIKE TABLEWARE</text>
    <text x="40" y="90" font-family="'PingFang SC', sans-serif" font-size="18" font-weight="700" fill="#004B98">可重复使用环保餐具与模压制品</text>
    <text x="40" y="140" font-family="'Inter', sans-serif" font-size="15" fill="#CBD5E1">
      • Reusable Food Containers &amp; Bento Sets<br/>
      • Eco-friendly Molded Fiber &amp; Polymers<br/>
      • Food-Contact FDA / LFGB Certified Production
    </text>
    <text x="40" y="245" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="600" fill="#38BDF8">→ www.naiketableware.com</text>
  </g>

  <!-- Global Certifications Grid -->
  <g transform="translate(80, 1340)">
    <rect width="640" height="200" rx="20" fill="rgba(15,23,42,0.8)" stroke="#334155" stroke-width="1.5"/>
    <text x="320" y="45" font-family="'Montserrat', sans-serif" font-size="20" font-weight="800" fill="#FFFFFF" text-anchor="middle" letter-spacing="2">GLOBAL EXPORT AUDITS &amp; COMPLIANCE</text>
    <g transform="translate(40, 75)">
      <!-- Badge 1 -->
      <rect x="0" y="0" width="120" height="80" rx="12" fill="#1E293B"/>
      <text x="60" y="48" font-family="'Inter', sans-serif" font-size="16" font-weight="800" fill="#004B98" text-anchor="middle">ISO 9001</text>
      <!-- Badge 2 -->
      <rect x="145" y="0" width="120" height="80" rx="12" fill="#1E293B"/>
      <text x="205" y="48" font-family="'Inter', sans-serif" font-size="16" font-weight="800" fill="#B70005" text-anchor="middle">SGS LAB</text>
      <!-- Badge 3 -->
      <rect x="290" y="0" width="120" height="80" rx="12" fill="#1E293B"/>
      <text x="350" y="48" font-family="'Inter', sans-serif" font-size="16" font-weight="800" fill="#FFB800" text-anchor="middle">FDA/LFGB</text>
      <!-- Badge 4 -->
      <rect x="435" y="0" width="120" height="80" rx="12" fill="#1E293B"/>
      <text x="495" y="48" font-family="'Inter', sans-serif" font-size="16" font-weight="800" fill="#10B981" text-anchor="middle">BSCI AUDIT</text>
    </g>
  </g>

  <!-- Bottom Contact & QR Zone (Eye-level for trade show visitors) -->
  <g transform="translate(80, 1600)">
    <rect width="640" height="280" rx="24" fill="#FFFFFF"/>
    <!-- QR Code placeholder -->
    <g transform="translate(40, 40)">
      <rect width="180" height="180" rx="12" fill="#0F172A"/>
      <rect x="20" y="20" width="50" height="50" fill="#FFFFFF"/>
      <rect x="30" y="30" width="30" height="30" fill="#B70005"/>
      <rect x="110" y="20" width="50" height="50" fill="#FFFFFF"/>
      <rect x="120" y="30" width="30" height="30" fill="#004B98"/>
      <rect x="20" y="110" width="50" height="50" fill="#FFFFFF"/>
      <rect x="30" y="120" width="30" height="30" fill="#FFB800"/>
      <!-- Inner text -->
      <circle cx="90" cy="90" r="24" fill="#FFFFFF"/>
      <text x="90" y="98" font-family="'Montserrat', sans-serif" font-size="22" font-weight="900" fill="#0F172A" text-anchor="middle">n</text>
      <text x="90" y="215" font-family="'Inter', sans-serif" font-size="12" font-weight="700" fill="#475569" text-anchor="middle">SCAN FOR INQUIRY</text>
    </g>

    <g transform="translate(260, 70)" font-family="'Inter', sans-serif">
      <text x="0" y="0" font-size="26" font-weight="900" fill="#0F172A">Meet Our Team at the Booth</text>
      <text x="0" y="34" font-size="16" font-weight="600" fill="#B70005">Hong Kong &amp; Global Trade Shows</text>
      <text x="0" y="74" font-size="15" fill="#475569">Email: info@naikegroup.com</text>
      <text x="0" y="104" font-size="15" fill="#475569">Web: www.naikegroup.com</text>
      <text x="0" y="134" font-size="15" font-weight="700" fill="#004B98">Factory-Backed Product Development Since 2008</text>
    </g>
  </g>
</svg>"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)

def generate_ios_icon_1024(output_path):
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
{get_naike_badge_def()}
  <!-- Continuous Curvature 1024 Canvas -->
  <rect width="1024" height="1024" rx="224" ry="224" fill="#090D16"/>

  <!-- Centered Naike Badge scaled to 768x768 -->
  <g transform="translate(128, 128) scale(1.92)" filter="url(#badgeShadow)">
    {get_naike_badge_symbol(400)}
  </g>
</svg>"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)

def generate_android_adaptive_icons(output_dir):
    bg_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 432 432" width="432" height="432">
{get_naike_badge_def()}
  <rect width="432" height="432" fill="url(#naikeRedGrad)"/>
  <path d="M 0 240 C 140 270, 220 180, 432 150 L 432 432 L 0 432 Z" fill="url(#naikeBlueGrad)"/>
  <!-- Concentric Ambient Ripple -->
  <circle cx="216" cy="216" r="140" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="2"/>
  <circle cx="216" cy="216" r="80" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="2"/>
</svg>"""

    fg_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 432 432" width="432" height="432">
  <defs>
    <filter id="fgDropShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="rgba(0,0,0,0.35)"/>
    </filter>
  </defs>
  <!-- Centered White 'n' Arch & Star scaled to fit safe zone 264dp -->
  <g transform="translate(76, 76) scale(0.7)" filter="url(#fgDropShadow)">
    <path d="M 125 105 L 165 105 L 115 305 L 75 305 Z" fill="#FFFFFF"/>
    <path d="M 152 185 C 190 120, 290 120, 310 180 C 315 195, 305 240, 295 305 L 255 305 C 265 245, 272 198, 258 178 C 242 155, 178 160, 142 225 Z" fill="#FFFFFF"/>
    <g transform="translate(315, 125)">
      <path d="M 0 -28 Q 0 0, 28 0 Q 0 0, 0 28 Q 0 0, -28 0 Q 0 0, 0 -28 Z" fill="#FFFFFF"/>
      <circle cx="0" cy="0" r="3.5" fill="#FFB800"/>
    </g>
  </g>
</svg>"""

    with open(os.path.join(output_dir, "android_adaptive_background.svg"), "w", encoding="utf-8") as f:
        f.write(bg_svg)
    with open(os.path.join(output_dir, "android_adaptive_foreground.svg"), "w", encoding="utf-8") as f:
        f.write(fg_svg)

def generate_web_favicon(output_path):
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
{get_naike_badge_def()}
  <g transform="scale(0.16)">
    {get_naike_badge_symbol(400)}
  </g>
</svg>"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)

def main():
    svg_dir = r"d:\耐科group品牌视觉系统\naike_brand_output\svg"
    os.makedirs(svg_dir, exist_ok=True)

    generate_logo_mark(os.path.join(svg_dir, "logo_naike_mark.svg"))
    generate_logo_horizontal(os.path.join(svg_dir, "logo_naike_horizontal.svg"))
    generate_logo_vertical(os.path.join(svg_dir, "logo_naike_vertical.svg"))
    generate_business_card_front(os.path.join(svg_dir, "business_card_front.svg"))
    generate_business_card_back(os.path.join(svg_dir, "business_card_back.svg"))
    generate_employee_badge(os.path.join(svg_dir, "employee_badge.svg"))
    generate_meeting_room_frosted_film(os.path.join(svg_dir, "meeting_room_frosted_film.svg"))
    generate_rollup_banner(os.path.join(svg_dir, "rollup_banner.svg"))
    generate_ios_icon_1024(os.path.join(svg_dir, "ios_app_icon_1024.svg"))
    generate_android_adaptive_icons(svg_dir)
    generate_web_favicon(os.path.join(svg_dir, "favicon.svg"))

    print("[✓] All 11 production-grade SVGs generated successfully in:", svg_dir)

if __name__ == "__main__":
    main()
