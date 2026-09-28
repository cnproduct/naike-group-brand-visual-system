# Brand Visual System Master (品牌全方位视觉识别系统自主生成主控技能)

<div align="center">

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.9+-brightgreen.svg)
![W3C Design Tokens](https://img.shields.io/badge/W3C-Design%20Tokens-orange.svg)
![WCAG 2.1](https://img.shields.io/badge/WCAG-2.1%20AA%20Compliant-emerald.svg)
![Midjourney & FLUX](https://img.shields.io/badge/AI%203D%20Render-FLUX%20%7C%20MJ%20v6-purple.svg)

**只需输入 1 个 Logo，一键全自动衍生生成全套企业级线上数字应用与线下实体空间环境导视系统**  
*Single-Logo Driven Autonomous Brand Visual Identity (VI) Generation Engine*

[核心特性](#-核心特性) • [生成流水线](#-全触点生成流水线) • [快速开始](#-快速开始) • [交付资产清单](#-交付产物全集) • [空间与数字规范](#-空间与数字规范细则) • [License](#-开源协议)

</div>

---

## 🌟 核心特性 (Key Highlights)

- 🎯 **单 Logo 极简驱动**: 仅需提供一张品牌 Logo（PNG / JPG / SVG / WebP），自动萃取品牌色彩基因与几何构型；
- 🔬 **色彩科学与无障碍合规**: 自动输出 HEX、sRGB、CMYK 印刷分色与 HSL，严格执行 WCAG 2.1 AA/AAA 对比度审计与 60-30-10 黄金比例分配；
- 💻 **全链路线上数字触点**: 自动输出 `tokens.css`、Tailwind 变量、iOS 1024 连续曲率图标、Android 自适应双层图标、多端 Favicon、16:9 PPT 商业演讲母版、官网 Hero 展示及富文本 HTML 邮件签名；
- 🏢 **全场景线下实体空间导视**: 严格对标国家建筑与广告工程规范，输出公司门头（3D不锈钢背发光 4000K）、前台形象墙（大理石+1500mm黄金视线）、走廊企业文化墙、会议室磨砂腰线（200mm/65%透光）、培训室大屏待机主视觉、贵宾接待室轻奢微标、产品发布会主舞台巨幕 KV（32:9/21:9）、易拉宝展架及双面特种纸名片/工牌；
- 📸 **3D 真实场景 AI 空间渲染工程**: 内置面向 Midjourney v6、FLUX.1 [dev/schnell] 与 SDXL 的工业级摄影提示词库（含相机机型、镜头焦段、PBR 材质与光影色温）；
- 📖 **出版级交互式 HTML 品牌手册**: 零配置生成可在浏览器直接交互与演讲的 `brand_guidelines.html`，支持明暗主题无缝切换与色值/Prompt 一键复制。

---


---

## 🏆 真实实战全案演示一：NAIKE GROUP (耐科集团) 全方位品牌视觉系统

> 📖 **完整深度解析文档**：[examples/CASE_STUDY_NAIKE.md](examples/CASE_STUDY_NAIKE.md)  
> 🌐 **交互式品牌手册 (支持浏览器直接打开)**：[naike_brand_output/brand_guidelines.html](naike_brand_output/brand_guidelines.html)  
> 🌍 **官方门户**：[www.naikegroup.com](http://www.naikegroup.com) (定制礼品 NAIKE GIFTS / 环保餐具 NAIKE TABLEWARE)

输入仅需一个 **耐科集团 (NAIKE GROUP)** 官方标志，系统自动完成色彩提取（耐科激情红 `#B70005`、耐科远洋蓝 `#004B98`、星辉金 `#FFB800`），并推演出涵盖线上数字应用与线下实体空间的 **10 大全景 8K 出版级效果图**：

<div align="center">
  <img src="naike_brand_output/logo_source.png" width="400" alt="NAIKE GROUP 官方标志">
</div>

| 01. 公司总部大厦门头 (3D背发光 4000K) | 02. 前台接待区大理石形象墙 (1500mm黄金视平线) |
| :---: | :---: |
| <img src="naike_brand_output/images/01_doorhead_facade.jpg" width="100%"> | <img src="naike_brand_output/images/02_reception_lobby.jpg" width="100%"> |

| 03. 走廊企业使命愿景文化墙 (Since 2008) | 04. 智能高管会议室与防撞磨砂腰线 |
| :---: | :---: |
| <img src="naike_brand_output/images/03_corridor_wall.jpg" width="100%"> | <img src="naike_brand_output/images/04_conference_room.jpg" width="100%"> |

| 05. 多功能培训厅演讲台与LED大屏 | 06. 贵宾接待室轻奢空间与品牌抽象艺术 |
| :---: | :---: |
| <img src="naike_brand_output/images/05_training_hall.jpg" width="100%"> | <img src="naike_brand_output/images/06_vip_lounge.jpg" width="100%"> |

| 07. 全球产品发布会 32:9 巨幕主舞台 | 08. 商务办公文具平铺 (烫金名片/工牌/画册) |
| :---: | :---: |
| <img src="naike_brand_output/images/07_launch_stage.jpg" width="100%"> | <img src="naike_brand_output/images/08_stationery_flatlay.jpg" width="100%"> |

| 09. 移动端 App Icon 与采购追踪界面 UI | 10. 官网展示模版与多设备监控看板透视 |
| :---: | :---: |
| <img src="naike_brand_output/images/09_app_mobile_showcase.jpg" width="100%"> | <img src="naike_brand_output/images/10_web_showcase_mockup.jpg" width="100%"> |

---

## 🏆 真实实战全案演示二：开思 (KAISI) 全方位品牌视觉系统

> 📖 **完整深度解析文档**：[examples/CASE_STUDY_KAISI.md](examples/CASE_STUDY_KAISI.md)  
> 🌐 **交互式品牌手册 (支持浏览器打开)**：[examples/kaisi_brand_output/brand_guidelines.html](examples/kaisi_brand_output/brand_guidelines.html)

输入仅需一个 **开思 (KAISI)** 原始 Logo，系统自动完成色彩提取（开思科技蓝 `#0070F0`、进取阶梯金 `#F0B000`、深邃碳灰 `#303030`），并推演出涵盖线上数字应用与线下实体空间的 **10 大全景 8K 出版级效果图**：

<div align="center">
  <img src="examples/kaisi_brand_output/logo_source.png" width="480" alt="开思 KAISI 输入标志">
</div>

| 01. 公司总部大厦门头 (3D背发光 4000K) | 02. 前台接待区大理石形象墙 (1500mm黄金视平线) |
| :---: | :---: |
| <img src="examples/kaisi_brand_output/images/01_doorhead_facade.jpg" width="100%"> | <img src="examples/kaisi_brand_output/images/02_reception_lobby.jpg" width="100%"> |

| 03. 走廊企业使命愿景文化墙 | 04. 智能高管会议室与防撞磨砂腰线 |
| :---: | :---: |
| <img src="examples/kaisi_brand_output/images/03_corridor_wall.jpg" width="100%"> | <img src="examples/kaisi_brand_output/images/04_conference_room.jpg" width="100%"> |

| 05. 多功能培训厅演讲台与LED大屏 | 06. 贵宾接待室轻奢空间与品牌抽象艺术 |
| :---: | :---: |
| <img src="examples/kaisi_brand_output/images/05_training_hall.jpg" width="100%"> | <img src="examples/kaisi_brand_output/images/06_vip_lounge.jpg" width="100%"> |

| 07. 全球产品发布会 32:9 巨幕主舞台 | 08. 商务办公文具平铺 (烫金名片/工牌/信纸) |
| :---: | :---: |
| <img src="examples/kaisi_brand_output/images/07_launch_stage.jpg" width="100%"> | <img src="examples/kaisi_brand_output/images/08_stationery_flatlay.jpg" width="100%"> |

| 09. 移动端 App Icon 与汽配采购界面 UI | 10. 官网展示模版与多设备监控看板透视 |
| :---: | :---: |
| <img src="examples/kaisi_brand_output/images/09_app_mobile_showcase.jpg" width="100%"> | <img src="examples/kaisi_brand_output/images/10_web_showcase_mockup.jpg" width="100%"> |


## 🏛️ 全触点生成流水线 (Architecture Pipeline)

```mermaid
graph TD
    In[用户输入: 仅需 1 个 Logo 图像/SVG] --> Extract[scripts/extract_logo_dna.py 视觉DNA萃取引擎]
    Extract --> Tokens[(brand_tokens.json 标准设计变量)]
    
    Tokens --> Dig[线上数字系统 Digital Suite]
    Tokens --> Env[线下空间导视 Environmental Suite]
    Tokens --> Prompts[3D 空间 AI 渲染 Director]
    Tokens --> Manual[交互式 VI 品牌手册 brand_guidelines.html]
    
    Dig --> D1[Web CSS / Tailwind Tokens]
    Dig --> D2[iOS 1024 & Android 双层 App Icon]
    Dig --> D3[16:9 商业演示 PPT 母版 7套版式]
    Dig --> D4[官网响应式 Hero 与多端 Mockup]
    
    Env --> E1[公司门头与建筑外立面背发光字]
    Env --> E2[前台接待区大理石形象背景墙]
    Env --> E3[走廊企业使命愿景价值观文化墙]
    Env --> E4[会议室防撞磨砂隐私腰线与门牌]
    Env --> E5[多功能厅演讲台与LED待机视觉]
    Env --> E6[全球产品发布会舞台巨幕KV与易拉宝]
    Env --> E7[双面商务名片、CR80工牌与商务文具]
    
    Prompts --> P1[10 大实景空间 Midjourney / FLUX 提示词]
```

---

## 🚀 快速开始 (Quick Start)

### 1. 环境依赖 (Prerequisites)
- Python 3.9+ (内置标准库 + Pillow)
```bash
pip install Pillow
```

### 2. 单行运行生成 (Run Master Pipeline)
```bash
python3 scripts/generate_vi_system.py path/to/your_logo.png "Your Brand Name" output_vi_dir
```

### 3. 查看输出成果
运行完毕后，双击或在浏览器中打开 `output_vi_dir/brand_guidelines.html` 即可查阅完整的企业交互式 VI 规范手册。

---

## 📦 交付产物全集 (Deliverables Package)

```text
output_vi_dir/
├── brand_tokens.json                  # 机器可读标准设计变量（色阶、CMYK、WCAG审计、字体、网格）
├── tokens.css                         # Web UI 与 Tailwind 适配的标准 CSS 变量
├── brand_guidelines.html              # 交互式出版级品牌手册（支持深浅色切换、一键复制色值）
│
├── svg/                               # 生产级矢量源文件库
│   ├── business_card_front.svg        # 90×54mm 标准商务名片正面（深色尊享版）
│   ├── business_card_back.svg         # 90×54mm 标准商务名片背面（浅色信息版）
│   ├── employee_badge.svg             # 54×85mm CR80 员工工牌与挂绳矢量图
│   ├── meeting_room_frosted_film.svg  # 200mm 高度玻璃隔断防撞磨砂隐私腰线
│   ├── rollup_banner.svg              # 800×2000mm 发布会与展会标准易拉宝展架
│   ├── ios_app_icon_1024.svg          # iOS App Store 1024 连续曲率超级符号图标
│   ├── android_adaptive_background.svg# Android 自适应图标背景层 (432dp)
│   ├── android_adaptive_foreground.svg# Android 自适应图标前景符号层 (432dp)
│   └── favicon.svg                    # 浏览器矢量 Favicon 微标
│
└── prompts/                           # 3D 真实场景 AI 渲染提示词工程
    ├── photorealistic_vi_prompts.json # 结构化 JSON 提示词库
    └── photorealistic_vi_prompts.md   # 一键复制版 Midjourney v6 / FLUX.1 手册
```

---

## 📐 空间与数字规范细则 (Technical Specifications)

### 1. 核心场景工程参数对照

| 触点场景 | 推荐尺寸与规格 | 核心材质与施工工艺 | 光学与色温规范 |
| :--- | :--- | :--- | :--- |
| **公司大厦门头** | 占门楣净宽 50%-65% | 钛锌板幕墙底板 + 304精工拉丝金属背发光字 | 4000K 自然白光 LED 模组，夜间 150-200 Lux |
| **前台形象墙** | 视觉中心标高 1500mm | 意大利鱼肚白天然大理石/岩板 + 3D拉丝立体字 | CRI >= 90 高显色指数，内嵌柔和微漫射背光 |
| **走廊文化墙** | 3层模块化展板 | 磁吸亚克力展板 + 愿景金属字 | 3000K-3500K 线性洗墙灯无眩光照明 |
| **会议室磨砂腰线** | 高度 200mm，距地 1200mm | 65% 半透光进口磨砂防爆膜 + 电脑高精镂空雕刻 | 上下各留 2mm 品牌色彩透明导向切线 |
| **培训室/多功能厅** | 16:9 / 32:9 LED 屏 | 胡桃木演讲台正面镶嵌 3mm 精密拉丝金属铭牌 | 待机主视觉禁止大面积纯白，采用暗夜黑基底 |
| **发布会舞台巨幕** | 32:9 环形曲面屏 | P1.2 高刷新率 LED 地屏与主屏 + 镜面黑地台 | 融入品牌主色高光粒子，核心文案标高 > 2.2米 |
| **商务名片印刷** | 90mm × 54mm (标准开本) | 600g 进口英国纯棉卡纸 / 触感纸 | 标志局部微压凹 + 德国库尔兹烫哑金 + 滚金边 |
| **移动端 App Icon** | 1024 × 1024 px | 矢量 SVG，严格居中，外围留出 18% 环形呼吸区 | 顶部 15° 微弱环境光晕，杜绝粗糙渐变 |

---

## 📚 目录结构索引 (Repository Structure)

```text
brand-visual-system-master/
├── SKILL.md                           # Skill 主控入口文件
├── README.md                          # 项目中英双语总览
├── requirements.txt                   # Python 运行依赖
├── instructions/                      # 深度分步技术实操指南
│   ├── 01_logo_extraction.md          # 标志几何、色彩聚类与WCAG测算
│   ├── 02_digital_applications.md     # 线上应用：Web、App Icon、PPT、官网
│   ├── 03_environmental_signage.md    # 线下应用：门头、前台、文化墙、会议室、发布会
│   ├── 04_ai_rendering_director.md    # 3D 真实场景 AI 渲染提示词工程
│   └── 05_brand_guardian_audit.md     # Brand Guardian 品牌守护者质量门禁 (Gate A-E)
├── references/                        # 工业级参数标准速查
│   ├── vi_dimension_matrix.md         # 全球标准物理打印与数字屏幕规格表
│   ├── materials_and_craftsmanship.md # 空间工程材质（不锈钢/亚克力/LED）与特种印刷
│   └── color_conversion_and_tokens.md # 色彩模型互转数学公式与 DTCG 规范
├── scripts/                           # 核心自动化执行脚本
│   ├── extract_logo_dna.py            # Logo 色彩与特征提取器
│   ├── generate_vi_system.py          # Master 生成主控流水线
│   ├── stationery_generator.py        # 实体文具与空间导视矢量 SVG 生成器
│   └── app_icon_generator.py          # App Icon 与 Favicon 矩阵生成器
├── templates/                         # 模版库
│   └── ppt_master_spec.json           # 16:9 商业演示 PPT 7套母版版式配置
└── examples/                          # 实战示例与演示包
    ├── CASE_STUDY_KAISI.md            # 开思 (KAISI) 全案深度图文解析手册
    ├── sample_logo.png                # 示例输入 Logo
    ├── demo_brand_output/             # 演示品牌生成的全套 VI 资产包与 HTML 预览
    └── kaisi_brand_output/            # 开思 (KAISI) 真实企业生成的全套 VI 资产包
        ├── brand_tokens.json          # 开思标准设计变量 (科技蓝/阶梯金/碳黑)
        ├── tokens.css                 # Web CSS 与 Tailwind 变量
        ├── brand_guidelines.html      # 交互式出版级品牌手册 (含图片与色阶复制)
        ├── images/                    # 10 大全场景 8K 出版级效果图
        ├── svg/                       # 8 套生产级矢量源文件 (名片/工牌/腰线/展架)
        └── prompts/                   # 10 大场景 Midjourney/FLUX 提示词工程
```

---

## 📄 开源协议 (License)

本项目基于 [MIT License](LICENSE) 开源发布。欢迎企业、设计机构与 AI 开发者自由使用、二次开发与商业化集成。
