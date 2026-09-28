# 02. 线上与数字全场景应用系统规范指南 (Digital Application Suite)

本指南详述由 Logo 衍生生成的全套数字触点规范，涵盖 Web UI 设计变量、App Icon 矩阵、多端 Favicon、16:9 PPT 商业演讲母版、官网展示头图与社交媒体全矩阵。

---

## 🌐 一、Web UI 设计变量 (Design Tokens) 与 CSS 架构

系统自动输出可直接导入 Tailwind CSS、Style Dictionary 或原生 CSS 的 `tokens.css`：

### 1. 核心变量结构
- `--brand-primary`: 主品牌色 HEX；
- `--brand-primary-rgb`: RGB 通道值，便于配合 `rgba(var(--brand-primary-rgb), 0.15)` 制作微透悬浮光晕；
- `--brand-secondary`: 次级辅助色；
- `--brand-accent`: 转化按钮与行动强调色；
- `--surface-canvas`: 页面背景色（亮色为浅灰冷白，暗色为深邃 Slate/Navy）；
- `--surface-card`: 模块卡片底色；
- `--shadow-glow`: 基于主色计算的品牌柔光阴影（Brand Glow Effect）。

### 2. 标准交互组件状态
- **核心按钮 (Primary Button)**: 背景填入 `--brand-primary`，白字，悬浮状态（Hover）明度微调 10%，激活态（Active）缩放 0.98；
- **次级按钮 (Secondary Button)**: 背景填入 `--brand-secondary`；
- **行动转化按钮 (CTA Accent Button)**: 背景填入 `--brand-accent`，配合高能转化场景；
- **描边按钮 (Outline Button)**: 1.5px 品牌主色线框，透明底，悬浮时平滑填充 10% 透明度光晕。

---

## 📱 二、App Icon 与 Favicon 多端矩阵系统

### 1. iOS App Store 标准图标
- **画板基准**: `1024px × 1024px`，矢量 SVG 绘制；
- **圆角规范**: 遵循 Apple 连续超椭圆（Squircle Continuous Curvature, 导角半径约 224px）；
- **构图法则**: 核心超级符号置于中央，符号主体占比在 **60% ~ 68%** 之间，外围留出充分环形边距；
- **光影质感**: 顶部 15° 微弱的环境光晕（Ambient Top Highlight），杜绝低端厚重高光。

### 2. Android Material You 自适应图标 (Adaptive Icons)
- **规格分层**: `432dp × 432dp`，分设前景色（Foreground）与背景色（Background）两层矢量图；
- **安全可见区**: 中心直径 `264dp` 内为绝对安全区，在各类启动器（圆形、圆角矩形、水滴形）裁切下均不丢失关键元素。

### 3. Web Favicon 套装
- `favicon.ico`: 内嵌 16x16, 32x32, 48x48 像素位图；
- `favicon.svg`: 现代浏览器无限缩放高保真矢量标牌；
- `apple-touch-icon.png`: 180x180 像素，iOS Safari 添加至主屏幕专用；
- `android-chrome-192x192.png` 与 `android-chrome-512x512.png`: PWA Progressive Web App 官方清单引用标准。

---

## 📊 三、PPT / Keynote 商业演示 16:9 母版系统

提供包含 7 套核心版式的标准化母版逻辑：

| 页面序号 | 母版版式类型 | 视觉重心与排版规范 |
| :--- | :--- | :--- |
| **01** | **发布会/提案封面 (Cover)** | 深色深邃背景，大号品牌几何符号水纹浮雕，居中 48pt 主标题 + 20pt 副标题 |
| **02** | **结构大纲页 (Agenda)** | 左侧 1/3 沉淀品牌主色色块与章节序号，右侧 2/3 清晰陈列 4-5 个关键议程卡片 |
| **03** | **章节过渡页 (Section Break)** | 纯品牌主色大色块或大面积深色，居中显示超大章节阿拉伯数字与醒目大字 |
| **04** | **双列对比内容页 (2-Col Body)** | 标准内容页，顶部保留 24pt 章节导航标尺，左侧现状痛点卡片，右侧方案成果卡片 |
| **05** | **三列卡片版式 (3-Col Grid)** | 三等分并列容器，顶部带有彩色圆角微标与 18pt 小标题，底托浅灰微投影 |
| **06** | **关键数据与图表页 (Metrics)** | 超大字号（64pt）数字指标展示，搭配对比色向上增长箭头与折线/柱状图占位 |
| **07** | **封底与问答致谢页 (Closing)** | 与封面呼应，居中放置品牌横版 Logo，附带官网域名、企业服务热线与二维码 |

---

## 💻 四、官网展示与多设备视角模型 (Website Hero & Mockups)

- **响应式视口规则**: 桌面端（1440px/1920px）、平板端（768px-1024px）、移动端（375px-430px）；
- **Hero 头图构图**: 左侧 55% 宽度用于震撼性 Value Proposition 标语与快速注册表单，右侧 45% 用于立体悬浮 3D 界面透视 Mockup（MacBook Pro + iPhone 16 Pro 联动透视）；
- **超级符号背景运用**: 在主头图深色背景后方，以 5% ~ 8% 超低不透明度平铺放大的品牌标志几何弧线，形成隐形潜意识品牌心智烙印。

---

## ✉️ 五、数字社交物料与富文本邮件签名

### 1. 全媒体社交主页封面
- **微信公众号头图**: 900px × 383px（注意次条 200x200 小图联动）；
- **LinkedIn 企业主页横幅**: 1584px × 396px（左下方预留 200px 避让圆形企业头像）；
- **Twitter / X 顶部横幅**: 1500px × 500px；
- **小红书横版封面**: 1080px × 1440px 竖版与 1080x720 横版。

### 2. 标准富文本 HTML 邮件签名
- 包含标准化企业 Logo、发件人姓名、中英文职位、手机号、官方域名、公司地址与保密声明（Confidentiality Notice）；
- 严格采用内联样式与表格排版（Table-based HTML），杜绝在 Outlook、Gmail、Apple Mail 中排版崩溃。

### 3. 虚拟会议高清背景 (Zoom / Teams / 飞书)
- 尺寸：`1920px × 1080px`（16:9）；
- 画面：现代化极简商务空间与模糊化办公室落地窗，右上角常驻半透明品牌 Logo，中间偏左位置留空给人像摄像头，避免 Logo 被参会人头部遮挡。
