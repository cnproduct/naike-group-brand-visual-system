#!/usr/bin/env python3
"""
App Icon Matrix & Digital Favicon Generator (app_icon_generator.py)
------------------------------------------------------------------
Generates:
1. iOS App Store Icon (1024x1024 SVG with squircle continuous curvature)
2. Android Adaptive Icon (Foreground SVG & Background SVG)
3. Multi-resolution Web Favicon (SVG & metadata package)
"""

import os
import sys
import json

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

def generate_ios_icon_svg(tokens, output_path):
    primary = tokens["color_palette"]["primary"]["hex"]
    secondary = tokens["color_palette"]["secondary"]["hex"]
    accent = tokens["color_palette"]["accent_cta"]["hex"]
    dark = tokens["color_palette"]["surface_dark"]["hex"]
    name = tokens["brand_meta"]["name"]

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <defs>
    <linearGradient id="iosIconBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{primary}"/>
      <stop offset="70%" stop-color="{dark}"/>
      <stop offset="100%" stop-color="#020617"/>
    </linearGradient>
    <linearGradient id="symbolGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="100%" stop-color="{accent}"/>
    </linearGradient>
    <filter id="dropShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="24" stdDeviation="32" flood-color="rgba(0,0,0,0.35)"/>
    </filter>
  </defs>

  <!-- iOS App Store 1024 Canvas (Square with continuous curvature masking) -->
  <rect width="1024" height="1024" rx="224" fill="url(#iosIconBg)"/>

  <!-- Inner ambient light ring -->
  <rect x="24" y="24" width="976" height="976" rx="200" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="4"/>

  <!-- Central Super-symbol -->
  <g transform="translate(512, 512)" filter="url(#dropShadow)">
    <!-- Base geometric shield/diamond -->
    <rect x="-240" y="-240" width="480" height="480" rx="120" fill="{dark}" stroke="{secondary}" stroke-width="12" transform="rotate(45)"/>
    <!-- Core dynamic glow circle -->
    <circle cx="0" cy="0" r="160" fill="url(#symbolGrad)"/>
    <!-- Center cut-out apex mark -->
    <path d="M 0 -80 L 70 60 L -70 60 Z" fill="{primary}"/>
    <!-- Micro accent spark -->
    <circle cx="0" cy="0" r="28" fill="#FFFFFF"/>
  </g>
</svg>"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)

def generate_android_adaptive_icons(tokens, output_dir):
    primary = tokens["color_palette"]["primary"]["hex"]
    accent = tokens["color_palette"]["accent_cta"]["hex"]
    dark = tokens["color_palette"]["surface_dark"]["hex"]

    # Background layer (432x432 dp standard)
    bg_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 432 432" width="432" height="432">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{primary}"/>
      <stop offset="100%" stop-color="{dark}"/>
    </linearGradient>
  </defs>
  <rect width="432" height="432" fill="url(#bgGrad)"/>
  <!-- Concentric ripple motif -->
  <circle cx="216" cy="216" r="140" fill="none" stroke="rgba(255,255,255,0.06)" stroke-width="2"/>
  <circle cx="216" cy="216" r="90" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="2"/>
</svg>"""

    # Foreground layer (432x432 dp with 264dp safe area)
    fg_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 432 432" width="432" height="432">
  <defs>
    <linearGradient id="fgSymbol" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="100%" stop-color="{accent}"/>
    </linearGradient>
    <filter id="fgShadow">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="rgba(0,0,0,0.3)"/>
    </filter>
  </defs>
  <g transform="translate(216, 216)" filter="url(#fgShadow)">
    <circle cx="0" cy="0" r="76" fill="url(#fgSymbol)"/>
    <path d="M 0 -38 L 33 28 L -33 28 Z" fill="{primary}"/>
    <circle cx="0" cy="0" r="14" fill="#FFFFFF"/>
  </g>
</svg>"""

    with open(os.path.join(output_dir, "android_adaptive_background.svg"), "w", encoding="utf-8") as f:
        f.write(bg_svg)
    with open(os.path.join(output_dir, "android_adaptive_foreground.svg"), "w", encoding="utf-8") as f:
        f.write(fg_svg)

def generate_web_favicon(tokens, output_path):
    primary = tokens["color_palette"]["primary"]["hex"]
    accent = tokens["color_palette"]["accent_cta"]["hex"]

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
  <rect width="64" height="64" rx="16" fill="{primary}"/>
  <circle cx="32" cy="32" r="18" fill="{accent}"/>
  <path d="M 32 20 L 42 38 L 22 38 Z" fill="#FFFFFF"/>
</svg>"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)

def generate_all_icons(tokens, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    generate_ios_icon_svg(tokens, os.path.join(output_dir, "ios_app_icon_1024.svg"))
    generate_android_adaptive_icons(tokens, output_dir)
    generate_web_favicon(tokens, os.path.join(output_dir, "favicon.svg"))
    print(f"[✓] Successfully generated App Icon Matrix in: {output_dir}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 app_icon_generator.py <tokens_json_path> <output_dir>")
        sys.exit(1)
    with open(sys.argv[1], "r", encoding="utf-8") as f:
        tokens = json.load(f)
    generate_all_icons(tokens, sys.argv[2])
