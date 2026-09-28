# 色彩科学对照算法与设计变量规范 (Color Spaces, Conversions & Design Tokens)

本参考文档详述数字颜色空间（sRGB、HEX、HSL）与物理印刷工业（CMYK、Pantone PMS）之间的互转算法、WCAG 2.1 无障碍对比度计算推导，以及现代 W3C Design Tokens 标准结构。

---

## 🧮 一、色彩空间数学转换模型

### 1. sRGB 转换为四色胶印 CMYK
工业印刷中，RGB 向 CMYK 转换须扣除补色并计算黑版总量（K版）：
$$C' = 1 - \frac{R}{255}, \quad M' = 1 - \frac{G}{255}, \quad Y' = 1 - \frac{B}{255}$$
$$K = \min(C', M', Y')$$
$$C = \frac{C' - K}{1 - K} \times 100\%, \quad M = \frac{M' - K}{1 - K} \times 100\%, \quad Y = \frac{Y' - K}{1 - K} \times 100\%$$
*注：总油墨覆盖率（Total Ink Coverage, TIC = C + M + Y + K）在铜版纸印刷中严禁超过 320%，在胶版纸印刷中严禁超过 280%，以防止油墨干燥不及造成背面粘脏。*

### 2. sRGB 转换为感知 HSL
$$R' = \frac{R}{255}, \quad G' = \frac{G}{255}, \quad B' = \frac{B}{255}$$
$$C_{\max} = \max(R', G', B'), \quad C_{\min} = \min(R', G', B'), \quad \Delta = C_{\max} - C_{\min}$$
- **明度 (Lightness)**: $L = \frac{C_{\max} + C_{\min}}{2}$
- **饱和度 (Saturation)**:
  - 若 $\Delta = 0$，则 $S = 0$
  - 若 $\Delta \ne 0$，则 $S = \frac{\Delta}{1 - |2L - 1|}$

---

## 👁️ 二、W3C WCAG 2.1 相对亮度与对比度公式

### 1. 相对亮度（Relative Luminance, $L$）
对 sRGB 的每个通道（$R, G, B \in [0, 255]$），先归一化为 $[0, 1]$：
$$V_{\text{norm}} = \frac{V}{255}$$
执行伽马逆校正转为线性色彩空间：
$$V_{\text{linear}} = \begin{cases} \frac{V_{\text{norm}}}{12.92} & \text{if } V_{\text{norm}} \le 0.03928 \\ \left(\frac{V_{\text{norm}} + 0.055}{1.055}\right)^{2.4} & \text{if } V_{\text{norm}} > 0.03928 \end{cases}$$
计算加权相对亮度：
$$L = 0.2126 \times R_{\text{linear}} + 0.7152 \times G_{\text{linear}} + 0.0722 \times B_{\text{linear}}$$

### 2. 对比度（Contrast Ratio, $CR$）
设前景与背景的相对亮度分别为 $L_1$ 与 $L_2$（且 $L_1 > L_2$）：
$$CR = \frac{L_1 + 0.05}{L_2 + 0.05}$$
结果取值范围在 $1:1$ 到 $21:1$ 之间。

---

## 💻 三、W3C Design Tokens Community Group (DTCG) 格式标准

系统导出的 `brand_tokens.json` 与 DTCG 国际标准高度兼容：

```json
{
  "color": {
    "brand": {
      "primary": {
        "$value": "#0E74E9",
        "$type": "color",
        "$description": "Core primary brand color used for primary interactive states and illuminated signage"
      },
      "secondary": {
        "$value": "#F97316",
        "$type": "color",
        "$description": "Complementary vibrant accent for charts and highlights"
      }
    }
  },
  "dimension": {
    "spacing": {
      "logo-clear-space": {
        "$value": "0.5X",
        "$type": "dimension"
      }
    }
  }
}
```
