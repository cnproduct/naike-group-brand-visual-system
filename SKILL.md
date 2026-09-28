---
name: brand-visual-system-master
description: 全方位品牌视觉系统 (Brand Visual Identity System) 自主生成主控技能。只需输入一个 Logo（图像/SVG/路径），一键自动化提取视觉 DNA，生成涵盖标志基础规范（网格制图/色彩/字体/安全区）、线上数字触点（Web Tokens、App Icon 矩阵、16:9 PPT 母版、官网展示、富文本邮件签名）与线下实体空间导视（公司门头、前台形象、文化墙、会议室磨砂腰线、培训室大屏、贵宾接待室、产品发布会主舞台巨幕KV、易拉宝与商务文具）的全方位 VI 系统，并输出交互式 HTML VI 手册、SVG 矢量源文件与 3D 真实场景 AI 渲染 Prompts。
---

# Brand Visual System Master · 全方位品牌视觉系统生成主控技能

本技能遵循国际标准 Skill Creator 架构规范，深度融合了 **`dsclca12/agent-teams`（Brand Guardian 品牌守护者人格与 VI 全案）**、**`DevinKuang/brand-strategy-guide`（企业级三层价值决策树与结构化工程交付）** 以及 **`cnproduct/renasset-brand-video-master`（多模态资产摄取、设计变量 Tokens 体系、质量门禁与自进化飞轮）** 的核心精髓。

其核心价值在于：**用户无需具备专业平面设计或广告工程背景，只需提供一个原始 Logo，技能即可全自动推演并生成全套企业级线上与线下品牌视觉应用系统**。

---

## 🏛️ 技能架构与全触点生成流水线

```mermaid
graph TD
    UserIn[输入: 仅需 1 个 Logo 图像/SVG] --> Extract[1. scripts/extract_logo_dna.py 视觉DNA提取引擎]
    Extract --> Tokens[(核心品牌设计变量 brand_tokens.json)]
    
    Tokens --> M1[基础识别系统 Basic VIS]
    Tokens --> M2[线上数字应用 Digital Suite]
    Tokens --> M3[线下空间导视 Environmental Suite]
    Tokens --> M4[3D AI 空间渲染 Prompt Director]
    
    M1 --> M1_1[几何网格制图法 / 0.5X 安全隔离区 / 最小使用尺寸]
    M1 --> M1_2[60-30-10 黄金色彩配比 / CMYK 印刷分色 / WCAG 对比度]
    M1 --> M1_3[中英文字体阶梯 / 辅助超级符号与平铺底纹]
    
    M2 --> M2_1[Web Tokens: tokens.css & Tailwind 变量]
    M2 --> M2_2[App Icon 矩阵: iOS 1024 连续曲率 / Android 自适应双层 / Favicon]
    M2 --> M2_3[商业演示: 16:9 PPT / Keynote 7大核心母版规范]
    M2 --> M2_4[数字社交: 微信 / LinkedIn / X / 邮件签名 / 虚拟会议背景]
    
    M3 --> M3_1[公司门头: 钛锌板幕墙 + 3D金属背发光字 (4000K自然白)]
    M3 --> M3_2[前台接待区: 意大利大理石 + 3D拉丝金属悬浮字 (1500mm黄金视线)]
    M3 --> M3_3[走廊文化墙: 愿景使命价值观 + 磁吸时间轴模块化展板]
    M3 --> M3_4[智能会议室: 200mm防撞磨砂隐私腰线 + 镂空超级符号]
    M3 --> M3_5[多功能培训厅: 实木讲台金属标牌 + 16:9 待机主视觉]
    M3 --> M3_6[贵宾接待室: 极简轻奢纳帕真皮压凹杯垫 + 骨瓷茶具烫金微标]
    M3 --> M3_7[全球产品发布会: 32:9 超宽巨幕舞台KV + 签到背板 + 80x200cm 易拉宝]
    M3 --> M3_8[商务办公用品: 90x54mm 双面特种纸名片 + CR80 员工工牌]
    
    M4 --> Prompts[10大空间 Midjourney v6 / FLUX.1 实景逼真渲染 Prompts]
    
    Tokens --> HTML[交互式 VI 规范手册: brand_guidelines.html]
    Tokens --> SVG[高精度矢量源文件库: svg/*.svg]
```

---

## 🚦 五道质量与品牌守护者门禁 (Quality Gates A–E)

执行本技能时，输出成果必须通过内置的五道 Brand Guardian 质量闸门（详见 `instructions/05_brand_guardian_audit.md`）：

1. **Gate A（几何与分辨率门禁）**: 确保输入 Logo 不受低清像素噪点污染，建立严格的 `0.5X` 保护区红线；
2. **Gate B（色彩科学与 WCAG 无障碍门禁）**: 核心操作在白底与黑底上的对比度必须 $\ge 4.5:1$（AA 级以上），印刷 CMYK 总墨量 $\le 300\%$；若主色对比度不足，强制触发防眩光胶囊底托保护；
3. **Gate C（多端数字像素网格对齐门禁）**: App Icon 必须在 16px Favicon 与 1024px App Store 状态下均高度可辨，CSS Tokens 符合 W3C DTCG 规范；
4. **Gate D（实体空间工程可行性门禁）**: 发光字最小笔画宽度 $\ge 15mm$（可容纳 LED 模组），会议室腰线距地 $1200mm$，易拉宝关键图文位于视线黄金区；
5. **Gate E（品牌一致性全域综合守护）**: 确保所有衍生应用具备严格的母标几何血统，综合合规评分 $\ge 90$ 分。

---

## 💻 快速开始与命令行使用

### 1. 极简单行运行 (Single Command)
传入任意一张 Logo 图像与品牌名称，一键输出全套 VI 系统：
```bash
python3 scripts/generate_vi_system.py path/to/logo.png "Your Brand Name" output_vi_dir
```

### 2. 输出产物清单
执行完成后，将在 `output_vi_dir/` 下生成出版级全套资产：
- `brand_tokens.json`: 完整机器可读的标准设计变量（色值、字阶、网格、安全区）；
- `tokens.css`: 现代 Web 与 Tailwind 适配的标准 CSS 变量；
- `brand_guidelines.html`: 沉浸式交互型响应式品牌手册（支持浅色/暗黑切换、一键复制色值）；
- `svg/`:
  - `business_card_front.svg` & `business_card_back.svg`: 标准 90×54mm 双面名片矢量源文件；
  - `employee_badge.svg`: 54×85mm CR80 工牌与挂绳矢量源文件；
  - `meeting_room_frosted_film.svg`: 玻璃隔断防撞磨砂腰线矢量源文件；
  - `rollup_banner.svg`: 800×2000mm 展会发布会易拉宝矢量源文件；
  - `ios_app_icon_1024.svg`: iOS App Store 标准 1024 矢量图标；
  - `android_adaptive_background.svg` & `foreground.svg`: Android 自适应双层图标；
  - `favicon.svg`: Web 多分辨率矢量微标；
- `prompts/`:
  - `photorealistic_vi_prompts.json`: 结构化 10 大场景 3D 渲染 Prompts；
  - `photorealistic_vi_prompts.md`: 排版精美的一键复制版 Midjourney / FLUX 提示词手册。

---

## 🏆 实战案例库 (Case Studies)
- **[开思 (KAISI) 全方位品牌视觉系统全案](examples/CASE_STUDY_KAISI.md)**:
  - 输入标志：开思官方横版字标 (`examples/kaisi_brand_output/logo_source.png`)；
  - 核心色彩：开思科技蓝 `#0070F0`、进取阶梯金 `#F0B000`、深邃碳灰 `#303030`；
  - 完整资产：包含 10 大场景 8K 出版级效果图 (`examples/kaisi_brand_output/images/`)、Web 设计变量 (`tokens.css`)、多端 App Icon 矩阵、双面名片工牌与交互式品牌手册 (`brand_guidelines.html`)。

---

## 📚 模块化指南与核心参考

- **[01. 标志几何解构与色彩 DNA 提取](instructions/01_logo_extraction.md)**: 几何网格、色彩聚类、CMYK 胶印转换与 WCAG 算法；
- **[02. 线上数字全场景应用系统](instructions/02_digital_applications.md)**: Web Tokens、App Icon 矩阵、16:9 PPT 母版与社交物料；
- **[03. 线下实体空间与环境导视全场景](instructions/03_environmental_signage.md)**: 门头发光字、大理石前台、走廊文化墙、会议室磨砂、发布会舞台巨幕与办公用品；
- **[04. 3D 真实场景 AI 空间渲染提示词工程](instructions/04_ai_rendering_director.md)**: 工业级光影、PBR 材质、相机镜头与 Midjourney/FLUX 语法；
- **[05. 品牌守护者审计体系与五道质量门禁](instructions/05_brand_guardian_audit.md)**: 品牌一致性评审与避坑指南；
- **[全尺寸速查规格矩阵](references/vi_dimension_matrix.md)**: 印刷开本、屏幕分辨率与建筑施工尺度速查；
- **[工程材质与印刷特种工艺词典](references/materials_and_craftsmanship.md)**: 不锈钢、亚克力、4000K LED 与烫金压凹工艺；
- **[色彩科学对照与设计变量标准](references/color_conversion_and_tokens.md)**: 数学推导模型与 W3C DTCG 格式规范。
