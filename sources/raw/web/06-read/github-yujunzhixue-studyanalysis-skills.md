# YuJunZhiXue/StudyAnalysis-Skills（Knowledge Absorber，中文）

- 链接：https://github.com/YuJunZhiXue/StudyAnalysis-Skills
- 作者：YuJunZhiXue
- 仓库说明：深度解析链接、文档或代码，生成“全能导师级”的教学笔记
- 星数：633
- 获取方式：GitHub README + SKILL/说明文件

---

## README

<div align="center">

# 📚 Knowledge Absorber (知识吸收器)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Version: 4.1.0](https://img.shields.io/badge/Version-4.1.0-green.svg)](CHANGELOG.md)

**通用 AI 技能模块 | 适用于 Trae, Claude, Gemini, VS Code Copilot 等环境**

[🇺🇸 English](README_EN.md) | [🇨🇳 简体中文](README.md)

---

**Knowledge Absorber** 是一个独立的“外挂大脑”模块。它赋予 AI 助手深度阅读、解析长文档并生成结构化知识晶体（Markdown + HTML）的能力。

</div>

---

## 🚀更新

> **v4.1.0 最新更新**

- **🎓 导师模式 (Mentor Mode)**：全新的交互式学习体验
  - **智能对话助手**：在生成的 HTML 页面中，点击"打开导师模式"按钮，即可与 AI 导师实时对话
  - **上下文感知**：导师模式完全理解当前知识卡片的内容，可以针对性地回答问题、深化理解
  - **本地 Relay 服务**：通过 `python scripts/mentor_relay.py` 启动本地中继服务（默认端口 8760）
  - **多模型支持**：兼容 OpenAI、Claude、Gemini 等任何 OpenAI 兼容的 API
  - **侧边栏设计**：优雅的侧边栏界面，不干扰正文阅读，随时呼出随时关闭
  - **对话历史**：保留完整的对话上下文，支持连续深入提问

- **💡 深度链接分析**：新增多源输入冲突对比功能，自动对比多源输入冲突，强化 AI 的事实校验能力

> **v4.0.0 之前的更新**

- **修复报错**：修复 MAC 中 pywin32 报错。
- **⚛️ 深度裂变模块 (Deep Fission)**：新增原子级矛盾分析与版本考据模块，用于揭示颠覆常识的结论（样式：`.fission-section`）。
- **🔍 严格搜索内化 (Strict Filter)**：HTML 交互升级，搜索框现在会**严格隐藏**不匹配的内容块，而非仅高亮，提供专注阅读体验。
- **🛡️ Mermaid 安全协议**：内置语法自动修正机制，强制转义特殊字符，杜绝图表渲染崩溃。

---

## 支持功能

- 支持多链接/文件同步抓取。
- 实现具备高对比度色彩的实时状态追踪与彩色终端任务看板。
- 新增 `【💡 深度链接】` 分析，自动对比多源输入冲突，强化 AI 的事实校验能力。

## 📂 跨平台移植指南 (Portability Guide)

本模块设计为 **"文件夹级即插即用"**。
不同的 AI 助手通常会扫描项目根目录下的特定配置文件夹。为了让其他 AI (如 Claude 或 Gemini) 识别此技能，你只需要**修改父目录的名称**。

### 📂 目录结构适配

假设你把 `skills` 文件夹放在项目根目录：

1.  **在 Trae 中使用** (默认):

    ```text
    Project_Root/
    └── .trae/              <-- 保持原名
        └── skills/
            └── knowledge-absorber/
    ```

2.  **在 Claude Projects 中使用**:
    - 将 `.trae` 重命名为 `.claude`。

    ```text
    Project_Root/
    └── .claude/            <-- 重命名为 .claude
        └── skills/
            └── knowledge-absorber/
    ```

3.  **在 Gemini Advanced / AI Studio 中使用**:
    - 将 `.trae` 重命名为 `.gemini`。

    ```text
    Project_Root/
    └── .gemini/            <-- 重命名为 .gemini
        └── skills/
            └── knowledge-absorber/
    ```

4.  **在 VS Code (Copilot/Cline) 中使用**:
    - 将 `.trae` 重命名为 `.vscode`。
    ```text
    Project_Root/
    └── .vscode/            <-- 重命名为 .vscode
        └── skills/
            └── knowledge-absorber/
    ```

> **💡 核心原理**：AI 助手通常有权限读取隐藏文件夹（以 `.` 开头）。只要路径正确，并明确指示 AI “使用这个技能”，它就能工作。

---

## 🛠️ 安装与使用 (Installation & Usage)

### 第一步：环境准备

确保你的电脑安装了 Python 3.8+。
在 `knowledge-absorber` 目录下运行：

```bash
pip install -r requirements.txt
```

### 第二步：何时调用 (When to Activate)

不要为简单的 Google 搜索使用此技能。请在以下“高认知负载”场景召唤它：

1.  **啃大部头**：当你面对数百页的 PDF、技术框架文档（如 BMad, React 源码）或古籍时。
2.  **需要知识晶体**：当你不仅要一个简单的总结，而是要生成可永久存档、排版精美的 HTML 卡片时。
3.  **多源交叉分析**：当需要同时对比抓取多个不同平台的链接（如知乎 + 博客 + 官方文档）进行深度真理锚定时。

### 第三步：调用机制 (Workflow)

你不需要手动运行复杂的命令行，只需在对话中**自然指令**，AI 会自动代理执行：

- **用户指令示例**：

  > “帮我深度解析这个链接：`https://docs.bmad-method.org/`”
  > “读取 `manual.pdf` 并按【机械透镜】拆解生成知识卡片。”

- **AI 的执行逻辑**：
  1.  **摄取**：并发调用 `scripts/content_ingester.py` 抓取并清洗内容。
  2.  **透镜分析**：根据 `SKILL.md` 中的协议（如机械透镜、意义透镜）进行深度推理。
  3.  **交付**：自动生成 `.md`（深度笔记）和 `.html`（可视化卡片）文件。

---

## 📦 产出物 (Outputs)

该技能会自动生成两种格式的文件（位于 `data/` 目录）：

1.  **Markdown 深度笔记 (`.md`)**：
    - 包含元数据、核心概念破冰、深度拆解、思维导图、避坑指南。
    - 支持”双文异构”（古文繁体/解释简体）或”技术栈模版”。
2.  **HTML 可视化卡片 (`.html`)**：
    - 精美的排版，适合分享或作为知识库归档。
    - 支持深色/浅色模式适配，代码高亮与 Mermaid 导图完美显示。

---

## 🎓 导师模式详解 (Mentor Mode)

### 什么是导师模式？

导师模式是 Knowledge Absorber 的交互式学习功能，让你可以在浏览生成的知识卡片时，随时与 AI 导师对话，深化理解、解答疑惑。

### 核心特性

1. **📚 上下文感知**
   - 导师完全理解当前知识卡片的所有内容
   - 可以针对具体章节、概念进行深入讲解
   - 自动关联相关知识点

2. **💬 智能对话**
   - 支持连续多轮对话
   - 保留完整对话历史
   - 可以追问、深挖、举例

3. **🎨 优雅界面**
   - 侧边栏设计，不遮挡正文
   - 支持深色/浅色主题
   - 响应式布局，适配各种屏幕

4. **🔌 灵活配置**
   - 支持任何 OpenAI 兼容的 API
   - 可配置模型、温度、最大 token 等参数
   - 本地运行，数据安全

### 使用步骤

#### 1. 启动 Relay 服务

在 `knowledge-absorber` 目录下运行：

```bash
python scripts/mentor_relay.py
```

你会看到：
```
Mentor relay listening on http://127.0.0.1:8760
```

> 💡 **提示**：Relay 服务是一个本地中继服务器，用于在浏览器和 AI 模型之间传递消息。它不会存储你的对话内容。

#### 2. 打开知识卡片

在浏览器中打开生成的 `knowledge_card.interactive.html` 文件。

#### 3. 配置 AI 连接

点击页面右上角的”打开导师模式”按钮，在侧边栏中：

1. 选择 API 类型（OpenAI / Claude / Gemini / 自定义）
2. 输入 API Key
3. 选择模型（如 gpt-4、claude-3-5-sonnet 等）
4. 点击”测试连接”确认配置正确

#### 4. 开始对话

配置成功后，就可以在输入框中提问了！例如：

- “请详细解释一下核心机制部分”
- “这个概念和 XXX 有什么区别？”
- “能举个实际应用的例子吗？”
- “我在实践中遇到了 XXX 问题，该怎么办？”

### 典型使用场景

1. **深化理解**
   - 对某个概念不太理解，请导师用更简单的语言解释
   - 需要更多的例子来加深印象

2. **扩展学习**
   - 询问相关的知识点
   - 了解更深层次的原理

3. **实战指导**
   - 询问如何在实际项目中应用
   - 请教遇到的具体问题

4. **对比分析**
   - 对比不同技术方案的优劣
   - 了解历史演进和未来趋势

### 配置说明

#### 支持的 API 类型

- **OpenAI**：GPT-4、GPT-3.5 等
- **Claude**：Claude 3.5 Sonnet、Claude 3 Opus 等
- **Gemini**：Gemini Pro、Gemini Ultra 等
- **自定义**：任何兼容 OpenAI API 格式的服务

#### 高级配置

在侧边栏的”高级设置”中，你可以调整：

- **Temperature**：控制回答的创造性（0-2，默认 0.7）
- **Max Tokens**：单次回答的最大长度（默认 2000）
- **System Prompt**：自定义导师的角色和风格

### 注意事项

1. **Relay 服务必须运行**
   - 如果没有启动 relay 服务，导师模式无法工作
   - 确保端口 8760 没有被占用

2. **API Key 安全**
   - API Key 仅存储在浏览器本地（localStorage）
   - 不会上传到任何服务器
   - 建议使用有额度限制的 API Key

3. **网络连接**
   - 需要能够访问对应的 AI 服务 API
   - 如果使用国内网络，可能需要配置代理

4. **仅用于阅读模式**
   - 如果只是阅读知识卡片，不需要启动 relay 服务
   - 搜索、主题切换等功能不依赖 relay

### 故障排查

**问题：点击”打开导师模式”没有反应**
- 检查 relay 服务是否正在运行
- 检查浏览器控制台是否有错误信息

**问题：测试连接失败**
- 检查 API Key 是否正确
- 检查网络连接是否正常
- 检查 API 端点 URL 是否正确

**问题：对话响应很慢**
- 可能是模型负载较高，稍等片刻
- 可以尝试切换到其他模型
- 检查网络延迟

---

## 🤖 技能协议 (Skill Protocol)

核心逻辑定义在 `SKILL.md` 文件中。
如果你想修改 AI 的思考方式（例如修改解析的深度、改变输出风格），请直接编辑 `SKILL.md`。

---

> **维护者**: Little Code Sauce
> **版本**: v4.1.0 (Mentor Mode Edition)


## 文件 knowledge-absorber/SKILL.md

---
name: knowledge-absorber
description: 深度解析链接、文档或代码，生成”全能导师级”的教学笔记（零基础直达精通）。具备”真理锚定”校验能力，自动识别幻觉与过时信息。支持国学风格渲染，自动清理广告和无用内容。
tags: [“learning”,”学习”,”analysis”,”分析”,”documentation”,”文档”,”knowledge-base”,”知识库”,”architecture”,”知识吸收”,”knowledge-absorber”,”verification”,”国学”,”classical-chinese”]
version: 4.5.0
---

# 用法

把链接、文档、图片或代码整理成一份可学习、可搜索、可继续提问的学习成品，并输出：

- `knowledge_card.md`
- `knowledge_card.interactive.html`

只需要一条命令：

```bash
python scripts/run_full_pipeline.py “<链接或本地文件路径>” [“<更多链接或文件路径>”]
```

示例：

```bash
python scripts/run_full_pipeline.py “https://example.com/article”
python scripts/run_full_pipeline.py “E:\资料\AI导论.pdf”
python scripts/run_full_pipeline.py “E:\资料\架构图.png”
python scripts/run_full_pipeline.py “E:\repo\main.py”
python scripts/run_full_pipeline.py “https://example.com/article” “E:\资料\补充说明.pdf”
```

也支持这种自然语言写法：

```bash
python scripts/run_full_pipeline.py “学习这个 https://example.com/article”
```

# 核心流程

本技能采用 **真理锚定协议 (Truth Anchoring Protocol)** 确保内容准确性。

## 第一步：智能摄取 (Content Ingestion)

运行脚本获取干净的内容。脚本会自动清洗 HTML 噪音、广告和无用内容，并处理多模态内容（PDF/OCR）。

**清理机制**：
- 自动移除广告、导航、页脚、社交分享等UI元素
- 过滤包含噪音关键词的短文本（登录、注册、下载、关注等）
- 识别并移除广告容器（通过class/id模式匹配）
- 不保留明显的UI元素和营销内容
- 不保留”谢谢大佬的支持”等打赏提示
- 不保留页面导航和推荐链接

## 第二步：真理锚定 (Truth Anchoring)

**”不要轻信任何文本，哪怕它看起来很专业。”**

在生成内容之前，必须先对摄取的内容进行**准确性校验**。

**验证流程**：
1. **提取核心主张**：识别文中所有关键事实性主张（具体数据、API用法、历史事件、绝对化论断）
2. **联网审计**：调用 `WebSearch` 验证每个主张，搜索必须包含当前年份（2026）以确保时效性
3. **生成校准报告**：构建”红队报告”，标注错误、过时或有争议的内容
4. **显式标注**：在最终输出中明确标注所有不确定或有争议的信息

**验证要求**：
- 每个关键主张都必须经过搜索验证
- 不得直接使用未经验证的原文内容
- 不得忽略明显的时效性问题（如”2020年最新”）
- 不得省略对绝对化论断的验证（”总是”、”从不”、”必须”）
- 不得在发现错误后不标注就直接使用

**标注规范**：
- 过时信息必须标注”[已过时]”
- 有争议内容必须标注”[存在争议]”
- 无法确认的内容必须标注”[待确认]”

## 第三步：生成教学内容

根据清洗后的内容和校准报告，生成多模态输出。

**内容适配**：
- **技术类**：使用现代清爽风格（Apple Design 风格）
- **国学/人文类**：使用水墨国学风格（传统中文字体、水墨背景、印章装饰）

**国学风格触发条件**：
当标题、来源、标签或内容前几段包含以下任一关键词时，自动应用国学风格：
- **经典文献**：论语、庄子、道德经、史记、诗经、易经、孟子、荀子、春秋、左传、礼记、周易、尚书、大学、中庸
- **学派思想**：国学、古文、佛、儒、道、哲学、人文、儒家、道家、佛家、法家、墨家、兵家、禅宗、理学、心学、玄学
- **历史人物**：孔子、老子、孟子、庄子、荀子、墨子、韩非子、朱熹、王阳明、程颐、程颢
- **文学体裁**：古诗、词、赋、骈文、散文、文言文
- **其他**：经史子集、四书五经、诸子百家、传统文化

## 第四步：质量验收 (Quality Assurance)

**交付前必须确认以下项目：**

1. ✅ HTML 包含 `<script>` 搜索逻辑
2. ✅ 国学模式下使用传统中文字体（宋体、思源宋体）和水墨风格
3. ✅ 包含 Mermaid 认知地图
4. ✅ 包含 5-8 个 FAQ
5. ✅ 内容已清理干净（无广告、无UI元素、无打赏提示）
6. ✅ 所有关键主张经过真理锚定验证
7. ✅ 不确定内容有明确标注

**不得出现以下情况**：
- 输出包含广告或营销内容的HTML
- 输出未经验证的事实性主张
- 国学模式下使用现代西文字体
- 省略搜索功能
- 省略Mermaid图表

**若任一项不符合要求，必须重新生成。**

# 输出位置与文件

脚本会在 `outputs/knowledge_YYYYMMDD_*` 下生成一个输出文件夹，且最终只保留两个文件：

- `knowledge_card.md`
- `knowledge_card.interactive.html`

# 导师模式（交互 HTML 可选）

导师模式需要本地 relay 才能在浏览器里调用模型：

- `python scripts/mentor_relay.py`（默认 `http://127.0.0.1:8760`）

如果只是阅读/搜索正文，不需要启动 relay。

# 支持的输入

- URL 链接
- PDF / Word / Markdown / TXT
- PNG / JPG / JPEG / WEBP
- Python / JavaScript / TypeScript / Java / C / C++ / Go / Rust 等代码文件
- 一次传入多个链接或文件

