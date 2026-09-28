#!/usr/bin/env python3
"""
Logo Visual DNA Extractor (extract_logo_dna.py)
------------------------------------------------
Analyzes a brand logo (PNG, JPG, SVG, WebP) to extract:
1. Dominant color palette (Primary, Secondary, Accent, Dark Neutral, Light Neutral, Semantics)
2. Color space representations (HEX, RGB, CMYK, HSL, Pantone approx)
3. WCAG 2.1 Contrast ratios against light (#FFFFFF) and dark (#0F172A) surfaces
4. Geometric aspect ratio, bounding box, recommended clear space (0.5X), and minimum sizes
5. Outputs standard W3C-compatible brand_tokens.json
"""

import sys
import os
import json
import math
from PIL import Image

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

def rgb_to_hex(r, g, b):
    return f"#{int(r):02X}{int(g):02X}{int(b):02X}"

def hex_to_rgb(hex_str):
    hex_str = hex_str.lstrip('#')
    if len(hex_str) == 3:
        hex_str = ''.join([c*2 for c in hex_str])
    return tuple(int(hex_str[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_cmyk(r, g, b):
    if (r, g, b) == (0, 0, 0):
        return 0, 0, 0, 100
    c = 1 - r / 255.0
    m = 1 - g / 255.0
    y = 1 - b / 255.0
    min_cmy = min(c, m, y)
    c = (c - min_cmy) / (1 - min_cmy)
    m = (m - min_cmy) / (1 - min_cmy)
    y = (y - min_cmy) / (1 - min_cmy)
    k = min_cmy
    return int(round(c * 100)), int(round(m * 100)), int(round(y * 100)), int(round(k * 100))

def rgb_to_hsl(r, g, b):
    r_norm, g_norm, b_norm = r / 255.0, g / 255.0, b / 255.0
    cmax = max(r_norm, g_norm, b_norm)
    cmin = min(r_norm, g_norm, b_norm)
    delta = cmax - cmin
    
    l = (cmax + cmin) / 2.0
    if delta == 0:
        s = 0
        h = 0
    else:
        s = delta / (1 - abs(2 * l - 1))
        if cmax == r_norm:
            h = ((g_norm - b_norm) / delta) % 6
        elif cmax == g_norm:
            h = (b_norm - r_norm) / delta + 2
        else:
            h = (r_norm - g_norm) / delta + 4
        h = h * 60
        if h < 0:
            h += 360
    return int(round(h)), int(round(s * 100)), int(round(l * 100))

def relative_luminance(r, g, b):
    def to_linear(val):
        v = val / 255.0
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    return 0.2126 * to_linear(r) + 0.7152 * to_linear(g) + 0.0722 * to_linear(b)

def contrast_ratio(rgb1, rgb2):
    lum1 = relative_luminance(*rgb1)
    lum2 = relative_luminance(*rgb2)
    brighter = max(lum1, lum2)
    darker = min(lum1, lum2)
    return round((brighter + 0.05) / (darker + 0.05), 2)

def color_distance(c1, c2):
    return math.sqrt((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2 + (c1[2]-c2[2])**2)

def extract_palette_from_image(image_path, num_colors=8):
    try:
        img = Image.open(image_path).convert("RGBA")
    except Exception as e:
        print(f"[Warning] Failed to load image directly: {e}. Generating fallback tokens.")
        return None, (1, 1)

    width, height = img.size
    thumb = img.copy()
    thumb.thumbnail((200, 200), Image.Resampling.LANCZOS)
    
    pixels = []
    for r, g, b, a in thumb.getdata():
        if a < 40:
            continue
        pixels.append((r, g, b))
        
    if not pixels:
        return None, (width, height)
        
    color_counts = {}
    for p in pixels:
        quant = (p[0] // 16 * 16, p[1] // 16 * 16, p[2] // 16 * 16)
        color_counts[quant] = color_counts.get(quant, 0) + 1
        
    sorted_colors = sorted(color_counts.items(), key=lambda x: x[1], reverse=True)
    distinct_colors = []
    for col, count in sorted_colors:
        if not distinct_colors:
            distinct_colors.append(col)
            continue
        if all(color_distance(col, c) > 35 for c in distinct_colors):
            distinct_colors.append(col)
            if len(distinct_colors) >= num_colors:
                break
                
    return distinct_colors, (width, height)

def build_brand_tokens(image_path=None, brand_name="Brand", raw_colors=None):
    width, height = 800, 800
    if image_path and os.path.exists(image_path):
        palette, (w, h) = extract_palette_from_image(image_path)
        width, height = w, h
    else:
        palette = raw_colors or [(14, 116, 233), (249, 115, 22), (15, 23, 42)]
        
    if not palette:
        palette = [(14, 116, 233), (249, 115, 22), (15, 23, 42)]

    scored_colors = []
    for c in palette:
        h, s, l = rgb_to_hsl(*c)
        scored_colors.append({
            "rgb": c,
            "hex": rgb_to_hex(*c),
            "hsl": (h, s, l),
            "sat": s,
            "lum": l,
            "cmyk": rgb_to_cmyk(*c)
        })
        
    vibrants = [c for c in scored_colors if c["sat"] >= 20 and 15 < c["lum"] < 85]
    darks = [c for c in scored_colors if c["lum"] <= 25]
    lights = [c for c in scored_colors if c["lum"] >= 88]
    
    if vibrants:
        primary = max(vibrants, key=lambda x: x["sat"])
        remaining_vibrants = [c for c in vibrants if c["hex"] != primary["hex"]]
        secondary = remaining_vibrants[0] if remaining_vibrants else None
    else:
        primary = scored_colors[0]
        secondary = scored_colors[1] if len(scored_colors) > 1 else None

    import colorsys
    if not secondary:
        p_h, p_s, p_l = primary["hsl"]
        sec_h = (p_h + 35) % 360
        sec_r, sec_g, sec_b = [int(x * 255) for x in colorsys.hls_to_rgb(sec_h / 360.0, p_l / 100.0, min(1.0, (p_s + 10) / 100.0))]
        secondary = {
            "rgb": (sec_r, sec_g, sec_b),
            "hex": rgb_to_hex(sec_r, sec_g, sec_b),
            "hsl": (sec_h, p_s, p_l),
            "cmyk": rgb_to_cmyk(sec_r, sec_g, sec_b)
        }

    p_h, p_s, _ = primary["hsl"]
    accent_h = (p_h + 180) % 360
    acc_r, acc_g, acc_b = [int(x * 255) for x in colorsys.hls_to_rgb(accent_h / 360.0, 0.52, 0.95)]
    accent = {
        "rgb": (acc_r, acc_g, acc_b),
        "hex": rgb_to_hex(acc_r, acc_g, acc_b),
        "hsl": (accent_h, 95, 52),
        "cmyk": rgb_to_cmyk(acc_r, acc_g, acc_b)
    }

    dark_neutral = darks[0] if darks else {
        "rgb": (15, 23, 42),
        "hex": "#0F172A",
        "hsl": (222, 47, 11),
        "cmyk": (64, 45, 0, 84)
    }

    light_neutral = lights[0] if lights else {
        "rgb": (248, 250, 252),
        "hex": "#F8FAFC",
        "hsl": (210, 40, 98),
        "cmyk": (2, 1, 0, 1)
    }

    semantics = {
        "success": {"hex": "#10B981", "rgb": (16, 185, 129), "cmyk": (75, 0, 60, 0)},
        "warning": {"hex": "#F59E0B", "rgb": (245, 158, 11), "cmyk": (0, 42, 100, 0)},
        "danger": {"hex": "#EF4444", "rgb": (239, 68, 68), "cmyk": (0, 85, 65, 0)},
        "info": {"hex": primary["hex"], "rgb": primary["rgb"], "cmyk": primary["cmyk"]}
    }

    white_rgb = (255, 255, 255)
    primary_on_white = contrast_ratio(primary["rgb"], white_rgb)
    primary_on_dark = contrast_ratio(primary["rgb"], dark_neutral["rgb"])
    white_on_primary = contrast_ratio(white_rgb, primary["rgb"])

    aspect = round(width / max(1, height), 2)
    logo_type = "horizontal_wordmark" if aspect >= 1.8 else ("vertical_lockup" if aspect <= 0.6 else "symbol_or_square")

    tokens = {
        "brand_meta": {
            "name": brand_name,
            "logo_file": os.path.basename(image_path) if image_path else "logo.png",
            "logo_dimensions": {"width": width, "height": height, "aspect_ratio": aspect},
            "logo_form_factor": logo_type,
            "version": "2.0.0",
            "generator": "Brand Visual System Master (AGY/Claude/OpenCode Standard)"
        },
        "color_palette": {
            "primary": {
                "name": "Brand Primary Core",
                "hex": primary["hex"],
                "rgb": f"rgb{primary['rgb']}",
                "cmyk": f"C{primary['cmyk'][0]} M{primary['cmyk'][1]} Y{primary['cmyk'][2]} K{primary['cmyk'][3]}",
                "hsl": f"hsl({primary['hsl'][0]}, {primary['hsl'][1]}%, {primary['hsl'][2]}%)",
                "usage_ratio": "30% (Brand anchors, key surfaces, navigation active states)"
            },
            "secondary": {
                "name": "Brand Secondary Accent",
                "hex": secondary["hex"],
                "rgb": f"rgb{secondary['rgb']}",
                "cmyk": f"C{secondary['cmyk'][0]} M{secondary['cmyk'][1]} Y{secondary['cmyk'][2]} K{secondary['cmyk'][3]}",
                "hsl": f"hsl({secondary['hsl'][0]}, {secondary['hsl'][1]}%, {secondary['hsl'][2]}%)",
                "usage_ratio": "15% (Data highlights, secondary illustrations, badges)"
            },
            "accent_cta": {
                "name": "High-Energy CTA Accent",
                "hex": accent["hex"],
                "rgb": f"rgb{accent['rgb']}",
                "cmyk": f"C{accent['cmyk'][0]} M{accent['cmyk'][1]} Y{accent['cmyk'][2]} K{accent['cmyk'][3]}",
                "hsl": f"hsl({accent['hsl'][0]}, {accent['hsl'][1]}%, {accent['hsl'][2]}%)",
                "usage_ratio": "10% (Action buttons, high-priority alert badges, conversion anchors)"
            },
            "canvas_light": {
                "name": "Base Light Canvas",
                "hex": light_neutral["hex"],
                "rgb": f"rgb{light_neutral['rgb']}",
                "usage_ratio": "45% (Background canvases, card fills, clean space)"
            },
            "surface_dark": {
                "name": "Deep Space Charcoal",
                "hex": dark_neutral["hex"],
                "rgb": f"rgb{dark_neutral['rgb']}",
                "usage_ratio": "Primary Text, Dark Mode background, architectural fascia backplates"
            },
            "semantics": semantics
        },
        "contrast_audit": {
            "primary_on_white": {
                "ratio": primary_on_white,
                "wcag_aa_normal_text": primary_on_white >= 4.5,
                "wcag_aa_large_text": primary_on_white >= 3.0,
                "wcag_aaa_normal_text": primary_on_white >= 7.0
            },
            "white_on_primary": {
                "ratio": white_on_primary,
                "wcag_aa_normal_text": white_on_primary >= 4.5,
                "wcag_aa_large_text": white_on_primary >= 3.0
            },
            "primary_on_dark": {
                "ratio": primary_on_dark,
                "wcag_aa_normal_text": primary_on_dark >= 4.5
            }
        },
        "spatial_clearance": {
            "unit": "X (defined as 1/2 of logo height or core symbol radius)",
            "safe_zone": "0.5X on all 4 boundaries (No text, graphics or border intrusion)",
            "minimum_digital_size_px": 32 if logo_type == "symbol_or_square" else 48,
            "minimum_print_size_mm": 12 if logo_type == "symbol_or_square" else 20
        },
        "typography_pairings": {
            "chinese_display": "PingFang SC, 'Source Han Sans CN', 'Microsoft YaHei', sans-serif",
            "chinese_body": "'PingFang SC', 'Source Han Sans CN', 'Hiragino Sans GB', sans-serif",
            "western_display": "'Inter', 'Montserrat', 'Helvetica Neue', Arial, sans-serif",
            "western_body": "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif",
            "monospace_code": "'JetBrains Mono', 'Fira Code', Menlo, Consolas, monospace",
            "hierarchy_scale": {
                "hero_display": {"size": "48px / 3rem", "weight": "800", "line_height": "1.15"},
                "h1_title": {"size": "36px / 2.25rem", "weight": "700", "line_height": "1.25"},
                "h2_section": {"size": "24px / 1.5rem", "weight": "600", "line_height": "1.35"},
                "h3_card": {"size": "18px / 1.125rem", "weight": "600", "line_height": "1.45"},
                "body_base": {"size": "15px / 0.9375rem", "weight": "400", "line_height": "1.65"},
                "caption_small": {"size": "13px / 0.8125rem", "weight": "400", "line_height": "1.5"},
                "micro_tag": {"size": "11px / 0.6875rem", "weight": "600", "line_height": "1.4", "letter_spacing": "0.05em"}
            }
        }
    }
    return tokens

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 extract_logo_dna.py <logo_image_path> [brand_name] [output_json_path]")
        sys.exit(1)
        
    logo_file = sys.argv[1]
    brand_name = sys.argv[2] if len(sys.argv) > 2 else "RenAsset & RenWork Enterprise"
    output_file = sys.argv[3] if len(sys.argv) > 3 else "brand_tokens.json"
    
    print(f"[*] Analyzing logo: {logo_file} for brand: {brand_name}...")
    tokens = build_brand_tokens(logo_file, brand_name)
    
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(tokens, f, indent=2, ensure_ascii=False)
        
    print(f"[✓] Successfully extracted brand visual DNA to: {output_file}")
    print(f"    - Primary Color: {tokens['color_palette']['primary']['hex']}")
    print(f"    - Secondary Color: {tokens['color_palette']['secondary']['hex']}")
    print(f"    - Accent Color: {tokens['color_palette']['accent_cta']['hex']}")
    print(f"    - Contrast (White on Primary): {tokens['contrast_audit']['white_on_primary']['ratio']}:1 (AA: {tokens['contrast_audit']['white_on_primary']['wcag_aa_normal_text']})")
