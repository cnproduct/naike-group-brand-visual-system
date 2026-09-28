# 04. 3D 真实场景 AI 空间渲染提示词工程指南 (AI Rendering Director)

本指南指导设计师、策划师与开发团队，如何将自动提取的品牌视觉变量（Brand Tokens）与标准空间参数，转化为能够在 **Midjourney v6**、**FLUX.1 [dev/schnell]**、**Stable Diffusion XL** 及 **Gemini Imagen 3** 中生成具有《Architectural Digest》出版级质感的 3D 实景空间效果图。

---

## 📸 一、工业级实景摄影提示词语法结构 (Prompt Engineering Formula)

一个优秀的实景空间 Prompt 由六大核心积木拼接而成：

```
[镜头摄影类型与机型] + [空间主体与品牌命名] + [核心材质与建筑细节] + [品牌色彩光晕注入] + [灯光氛围与环境色温] + [渲染引擎与参数后缀]
```

### 1. 镜头与器材参数注入
- **商业建筑摄影**: `Shot on Hasselblad H6D-100c, 24mm tilt-shift architectural lens, perfectly straight vertical lines`
- **室内空间特写**: `Shot on Sony A7R V, 35mm f/2.8 lens, shallow depth of field, soft natural ambient bokeh`
- **桌面文具俯拍**: `Top-down flatlay commercial studio photography, 50mm prime macro lens, dual Profoto softbox lighting, crisp clean shadows`

### 2. 真实物理材质描述词库 (PBR Materials)
- **金属类**: `Brushed 304 stainless steel, matte champagne gold electroplating, anodized dark titanium`
- **石材与板材**: `Calacatta Italian white marble with soft grey veining, fluted acoustic oak wood panels, matte flamed dark granite`
- **玻璃与光学**: `Acoustic tempered smart glass with translucent 65% sandblasted frosted film, anti-reflective optical coating`

### 3. 灯光与氛围渲染词库 (Lighting & Atmosphere)
- **色温校准**: `4000K natural daylight LED halo-lit backlighting, 3000K warm linear wall-washers`
- **黄昏暮色**: `Golden hour dusk twilight exterior lighting, dramatic reflections on polished terrazzo floor`
- **会务舞台**: `High-contrast theatrical stage lighting, haze beam atmospherics, glossy black lacquer reflective floor`

---

## 🛠️ 二、主流 AI 图像模型语法适配表

| 图像生成模型 | 推荐提示词结构特点 | 必备后缀参数 | 典型优势 |
| :--- | :--- | :--- | :--- |
| **Midjourney v6.0 / v6.1** | 结构化逗号短语 + 强光影修饰词 | `--ar 16:9 --style raw --v 6.0` | 顶级的材质纹理光泽与高级审美调色 |
| **FLUX.1 [dev / schnell]** | 连贯自然语言段落，精准实体描述 | 默认 16:9 或 3:2，CFG 3.5 | 极高保真的文字排版还原与空间几何准确性 |
| **Stable Diffusion XL** | 标签式 Prompt + 强 Negative Prompt | 采样器 DPM++ 2M Karras, Steps 30+ | 适合私有化本地部署与 ControlNet 精确控形 |
| **Gemini Imagen 3** | 丰富的空间逻辑与品牌诉求说明 | 原生摄影风格 | 商业场景光影平衡度与多角色自然融合 |

---

## 🚫 三、强制通用反向提示词 (Negative Prompts)

为杜绝 AI 常见的塑料质感、畸变扭曲与杂乱无序，在 SDXL 或支持 Negative Prompt 的引擎中强制注入：

```text
Negative Prompt:
blurry, low resolution, distorted letters, deformed geometry, chaotic layout, overexposed neon glow, cheap plastic texture, misaligned walls, noisy background, oversaturated colors, watermark, signature, stock photo watermark, low-budget office, warped text, tilted perspective.
```
