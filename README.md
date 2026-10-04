# 🦓 Zebra Reader (斑马阅读条)

[中文](#-中文介绍) | [English](#-english)

---

## 🇨🇳 中文介绍

**Zebra Reader** 是一款专为 **ADHD（注意力缺陷）** 与 **阅读障碍（Dyslexia）** 人群设计的轻量桌面级“屏幕阅读引导尺”。

### 🌱 开发初心（Why I Built This）
在日常上课和查阅长文档时，我常常很难长时间维持专注，也很难快速把文字读懂并吸收。现实生活中其实有那种实体“物理阅读尺/遮挡板”，能帮人把视线牢牢锁在当前行；但在电脑上，很多工具要么只能做局部高亮，要么功能臃肿、遮挡交互，对我起不到实际的引导作用。

因此，我开发了这款轻量的阅读工具：**它可以像一层透明直尺一样悬浮覆盖在任何软件和页面之上，自由调节条带宽窄、行距、透明度与交替色彩，还支持全鼠标穿透。** 

这个小工具实实在在地改善了我自己的日常阅读体验。现在我将它开源出来，希望能给同样受注意力分散、跳行、视觉漂移困扰的朋友带来一点实在的帮助。

<!-- 如有录制的动图，放置在根目录并取消下行注释 -->
<!-- ![演示动图](demo.gif) -->

### ✨ 核心特性

- **实体阅读尺数字化**：采用明暗/交替色块结构模拟物理阅读尺，强力锚定视线焦点，防止大段长文阅读中的跳行、串行与走神。
- **全局鼠标穿透（Click-Through）**：浮窗悬浮在屏幕最上层的同时支持鼠标完全穿透，选词查词、划词翻译、点击网页链接或翻页完全不受干扰。
- **高度灵活的动态调节**：支持热键与鼠标实时微调条带宽度、行间距步长、显示位置以及遮罩透明度，自适应不同字体与排版。
- **全局置顶兼容**：无缝浮动在浏览器、PDF 阅览器、代码 IDE、Word、电子书等任意窗口之上。
- **绿色本地纯净**：原生 Python 构建，不占内存，无广告、无联网上传、零隐私追踪。

---

### 🚀 快速上手

#### 方式一：直接下载运行（推荐）
1. 前往本仓库右侧的 [Releases](../../releases) 页面。
2. 下载最新打包的压缩包（Windows 用户解压后直接双击运行 `ZebraReader.exe`）。

#### 方式二：通过源码运行
确保本地环境已安装 Python 3.8+：

1. 克隆代码仓库：
   git clone https://github.com/FelixLiu339/zebra_reader.git
   cd zebra_reader

2. 安装必要运行依赖：
   pip install -r requirements.txt

3. 运行程序：
   python zebra_reader.py

---

### ⌨️ 操作与快捷键指南

#### 快捷键 (Hotkeys)
- **`Ctrl + Y`**：显示阅读条 (Show)
- **`Ctrl + Q`**：隐藏阅读条 (Hide)
- **`Ctrl + Shift + H`**：显示此操作帮助手册 (Show Help)

#### 鼠标交互（显示状态下 / Mouse Interaction）
| 功能操作 | 操作方式 / 说明 |
| :--- | :--- |
| **移动阅读条** | 按住 **`Ctrl` + 鼠标拖拽** (Hold Ctrl + Drag) |
| **调整窗口大小** | 按住 **`Ctrl + Alt` + 拖拽边缘缩放** (Hold Ctrl + Alt + Drag edges) |
| **调整行距与条带** | 按住 **`Alt` + 双击** 进入调整模式：拖拽虚线调整，再次 `Alt + 双击` 退出保存 |
| **退出应用** | 任务栏系统托盘图标右键 ➔ 退出 |

---

### ⚠️ Windows 安全提示与免责声明（必读）

为什么运行时会弹出“Windows 已保护你的电脑 (SmartScreen)”？
本软件为个人独立开源的辅助工具。微软官方的商业代码签名证书（EV Code Signing）每年需花费数百美元，对于免费开源项目成本过于高昂。因此 Windows SmartScreen 会将尚未积累海量下载量的未签名软件标记为“未知发布者”。

正常启动方法：
首次运行时若弹出蓝色提示弹窗，点击界面上的 “更多信息” (More info) -> 点击 “仍要运行” (Run anyway) 即可正常使用。

安全与隐私承诺：
本项目核心代码完全开源在当前仓库中，本地运行，不含任何广告插件、后门或后台遥测追踪代码。若有顾虑，欢迎直接审阅源码并在本地通过 Python 环境独立运行。

---

### ☕ Buy Me a Coffee (支持与赞助)

如果你觉得 Zebra Reader 确实改善了你的阅读体验，帮助你更好地集中精力工作与学习，欢迎请我喝杯咖啡支持后续功能维护与跨平台适配！非常感谢你的认可与温暖 ❤️

| 微信 / 支付宝 (Alipay / WeChat) | MobilePay |
| :---: | :---: |
| <img src="Alipay.png" width="220" alt="Alipay" /> | <img src="mobilepay QR.jpeg" width="220" alt="MobilePay" /> |

---

<br>

## 🇬🇧 English

**Zebra Reader** is a lightweight, minimalistic desktop reading tracker designed specifically for **ADHD** and **Dyslexia** users to combat line-skipping, visual drift, and cognitive fatigue.

### 🌱 Motivation
During lectures and heavy document reading, I often struggled to maintain continuous focus and found it hard to process dense text quickly. In physical life, guided reading strips and reading rulers help keep your gaze anchored to a single line; however, most digital tools on the market only offer basic text highlighters, which didn't truly solve the problem for me.

So, I built Zebra Reader: **a customizable, lightweight reading ruler that floats over any application, letting you freely adjust strip height, spacing, colors, and opacity—all with full mouse click-through capability.**

It made a genuine difference in my own daily workflow. I am making it open-source in the hopes that it can help anyone else navigating similar attention and reading challenges.

### ✨ Features

- **Digital Reading Ruler**: Uses high-contrast alternating stripes and masks to anchor visual attention and prevent skipping lines.
- **Global Click-Through**: Transparent overlay allows interacting with text, clicking links, and flipping pages beneath without moving the ruler.
- **On-the-Fly Customization**: Dynamically tweak stripe height, spacing, positioning, and opacity via hotkeys to match any typeface or line height.
- **Always-on-Top Floating Layer**: Stays smoothly layered over web browsers, PDF readers, IDEs, and e-readers.
- **100% Offline & Private**: Zero background bloat, no telemetry, and zero data collection.

---

### 🚀 Getting Started

#### Option 1: Direct Download (Recommended)
1. Navigate to the Releases section on the right side of this repository.
2. Download the latest binary archive (Windows: extract and double-click `ZebraReader.exe`).

#### Option 2: Run from Source
Requires Python 3.8+:

1. Clone repository:
   git clone https://github.com/FelixLiu339/zebra_reader.git
   cd zebra_reader

2. Install dependencies:
   pip install -r requirements.txt

3. Run application:
   python zebra_reader.py

---

### ⌨️ Controls & Shortcut Reference

| Action | Control / Details |
| :--- | :--- |
| Move Reading Bar | Mouse drag or mouse wheel / arrow keys fine-tuning |
| Adjust Height / Spacing | Expand or contract stripe thickness to match line heights |
| Opacity Control | Adjust contrast to ease eye strain while maintaining context |
| Toggle Click-Through | Enable/disable mouse pass-through for unobstructed interaction |
| Show / Hide | Global hotkey to quickly summon or hide the ruler |
| Exit Application | Right-click the system tray icon -> Exit |

---

### ⚠️ Security Notice & Disclaimer (Important)

Why does Windows show "Windows protected your PC" (SmartScreen)?
Zebra Reader is an independent, free open-source project. Official commercial code-signing certificates require costly annual subscriptions that are impractical for free community utilities. As a result, Windows flags newly released, unsigned binaries as coming from an "Unknown Publisher".

How to Run:
On the warning prompt, click "More info" -> click "Run anyway".

Security Statement:
Every line of code is open and verifiable directly inside this repository. The application contains zero telemetry, makes no external network requests, and is entirely safe to run. You are always welcome to inspect the source code and run it directly with your Python interpreter.

---

### ☕ Buy Me a Coffee

If Zebra Reader brings ease and focus to your reading routine, consider buying me a coffee to support continued maintenance and development. Thank you for your support! ❤️

| Alipay / WeChat Pay | MobilePay |
| :---: | :---: |
| <img src="Alipay.png" width="220" alt="Alipay" /> | <img src="mobilepay QR.jpeg" width="220" alt="MobilePay" /> |

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
