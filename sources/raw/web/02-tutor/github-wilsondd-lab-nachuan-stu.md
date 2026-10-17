# wilsondd-lab/nachuan-stu：初高中学习 skill 合集（中文）

- 链接：https://github.com/wilsondd-lab/nachuan-stu
- 作者：wilsondd-lab
- 仓库说明：初中、高中生的学习skill集合 
- 星数：3
- 获取方式：GitHub README + SKILL/说明文件

---

## README

<p align="center">
  <img src="./assets/readme/hero.svg" width="100%" alt="纳川 Skills：在 TRAE CN 中把 AI 对话变成可保存、复述和回看的学习资料">
</p>

给准高中生和家长的 AI 学习增强包。安装到 **TRAE CN** 后，用自然语言调用两个 Skill，把抽象知识做成可核对的图解和可回看的教学视频。

## 先看真实产物

<p align="center">
  <a href="./assets/showcase/nachuan-tujie-speed-vs-acceleration.png"><img src="./assets/showcase/nachuan-tujie-speed-vs-acceleration.png" width="34%" alt="纳川图解生成的速度与加速度对比知识图"></a>
  &nbsp;&nbsp;
  <a href="./assets/showcase/nachuan-teachingvideo-montage.png"><img src="./assets/showcase/nachuan-teachingvideo-montage.png" width="62%" alt="纳川教学视频生成的声现象教学分镜"></a>
</p>

这两张图来自仓库现有模板和示例的本机渲染结果，不是概念效果图。生成后的知识内容仍需孩子复述、练习并用教材核对。

## 一次安装，两种学习产出

| Skill | 你会得到 | 适合解决 |
|---|---|---|
| [`nachuan-tujie`](nachuan-tujie/SKILL.md) | 1080×1920 竖版 PNG 知识图 | 概念对比、公式、步骤、时间线、思维导图 |
| [`nachuan-teachingvideo`](nachuan-teachingvideo/SKILL.md) | 1080p 教学视频或无声循环 MP4 | 物理过程、实验、公式推导、概念辨析 |

覆盖语文、数学、英语、物理、化学、生物、政治、历史、地理和高中预科。它们是 TRAE 学习工作台里的长期增强能力，不替代孩子思考，也不替代教材和教师。

## 3 分钟，在 TRAE CN 里跑通第一次

### 第 1 步：安装两个 Skill

在 TRAE CN 的终端中复制：

```bash
npx -y skills add wilsondd-lab/nachuan-stu --skill '*' --agent trae-cn --global --yes --copy
```

Node.js 是本地运行环境，安装一次即可。若终端提示找不到 `node` 或 `npx`，先到 [Node.js 官网](https://nodejs.org/)安装 LTS 版本，再重新执行上面的命令。

### 第 2 步：验证安装

```bash
npx -y skills list --global --agent trae-cn
```

列表里应能看到：

- `nachuan-tujie`
- `nachuan-teachingvideo`

### 第 3 步：在 TRAE 里直接说

```text
用纳川图解，做一张“速度 vs 加速度”的初二物理知识图。
```

或者：

```text
用纳川教学视频，做一个“声现象”的 60 秒教学视频。
```

第一次调用时，Skill 会检查本机环境。图解基础模式需要 Node.js、npx 和本地渲染组件；教学视频还需要 ffmpeg。首次下载渲染依赖时需要可用网络。

## 生成只是中间步骤

```text
孩子先说自己的理解
    ↓
让 AI 整理图解提纲或视频脚本
    ↓
家长和孩子一起审内容
    ↓
生成图解或视频
    ↓
孩子看着成果复述
    ↓
做一道相似题并回教材核对
```

AI 生成不是终点。能复述、能练习、能核对，才算完成一次学习。

## 环境与兼容性

<details>
<summary><strong>展开环境检测命令</strong></summary>

### 图解环境

```bash
node --version
npx --version
npx hyperframes --version
```

### 教学视频环境

```bash
python3 nachuan-teachingvideo/scripts/render_video.py --check-env
```

2026-07-15 的本机实测环境为 Node.js `v22.22.3`、npx `10.9.8`、HyperFrames `0.7.58`、ffmpeg `8.1`。这只是一次实测记录，不是对所有电脑和未来版本的保证。

</details>

<details>
<summary><strong>只装一个 Skill、克隆仓库或移除</strong></summary>

### 只安装图解

```bash
npx -y skills add wilsondd-lab/nachuan-stu --skill nachuan-tujie --agent trae-cn --global --yes --copy
```

### 只安装教学视频

```bash
npx -y skills add wilsondd-lab/nachuan-stu --skill nachuan-teachingvideo --agent trae-cn --global --yes --copy
```

### 直接克隆仓库

```bash
git clone https://github.com/wilsondd-lab/nachuan-stu.git
```

### 更新与移除

重新执行安装命令即可拉取当前仓库版本。需要移除时，先用 `skills list` 确认安装位置，再删除对应的全局 Skill；不同版本的 Skills CLI 参数可能变化，以命令行帮助为准。

</details>

<details>
<summary><strong>仓库目录</strong></summary>

```text
nachuan-stu/
├── nachuan-tujie/             # 知识图解 Skill
├── nachuan-teachingvideo/     # 教学视频 Skill
├── assets/readme/             # GitHub 首图
├── assets/showcase/           # 真实产物预览
└── update_scripts/            # 维护工具脚本
```

</details>

## 与《准高中生 AI 橙皮书》的关系

《准高中生 AI 橙皮书》以 TRAE CN 为 21 次亲子练习的主要工作台。纳川图解和纳川教学视频安装一次后，可以在不同学科反复调用，把一次对话继续变成能保存、复述和回看的学习资料。



## 文件 nachuan-teachingvideo/SKILL.md

---
name: nachuan-teachingvideo
description: 纳川教学视频 · 准高中生AI学习伙伴。输入一个学科概念（如"声现象""杠杆原理""光合作用"），自动生成动态教学视频。默认快速模式4步搞定：概念输入 → AI自动生成（分镜+脚本+场景一起出）→ 配音 → 渲染，零配置开箱即用。两种产出由 HyperFrames 本地渲染、共用同一个 index.html：① 配音教学视频 — 5段分镜 + 中文配音（默认系统内置，可选 Minimax）+ 字幕 + 完整 MP4（1080p，60-90s）；② 无声循环动图 — 同一内容的紧凑无声版 MP4（1080p，~32s，循环播放）。想要更高质量说"用专业模式"，启用8阶段管线 + 五维分镜 + 全部质量门。当用户提"教学视频""配音视频""教学动图""无声动图""循环视频""概念动画""纳川教学"或给一个学科概念要做成动态内容时，使用本 skill。
triggers:
  - 教学视频
  - 配音视频
  - 教学动图
  - 无声动图
  - 循环视频
  - 概念动画
  - 纳川教学
  - 知识点视频
tags:
  - education
  - video
  - hyperframes
  - teaching
  - 教学
  - 纳川
---

# 纳川教学视频 · 准高中生AI学习伙伴

## 一、定位说明

**纳川教学视频**是为准高中生和家长打造的AI学习伙伴，致力于**让抽象概念动起来**。

| 维度 | 说明 |
|------|------|
| **目标用户** | 准高中生（初三升高一）+ 家长 |
| **学科覆盖** | 初中全科 + 高中预科（物理、数学、化学、生物、语文、英语） |
| **教学理念** | 让抽象概念动起来 — 用动态可视化把难懂的知识点讲透 |
| **视频时长** | 默认 60-90 秒，适合短视频学习场景，碎片时间高效吸收 |
| **语言风格** | 亲切、清晰、鼓励性 — 像一位耐心的学长/学姐在讲解 |
| **开箱即用** | 零 API 配置即可生成完整视频（系统内置配音 + 本地 HyperFrames 渲染） |
| **全平台兼容** | macOS / Windows / Linux 全平台可用 |

**技术栈**：
- HTML + CSS + SVG 制作可视化内容
- GSAP 制作动画时间轴
- HyperFrames 本地渲染为 MP4
- AI 负责内容创作（分镜、文案、动画设计）
- 内置场景模板和设计系统，AI 填空即可

---

## 二、第一次使用：30秒能力体检

第一次使用时，先做一个快速检测，告诉你当前的能力状态。

### 2.1 自动检测本机能力

检测以下能力，然后给出一张"能力卡片"：

| 检测项 | 怎么检测 | 说明 |
|--------|---------|------|
| **Node.js** | 运行 `node --version` | HyperFrames 运行环境 |
| **HyperFrames** | 运行 `npx hyperframes --version` | 视频渲染引擎 |
| **ffmpeg** | 运行 `ffmpeg -version` | 视频编码（HyperFrames 依赖） |
| **配音能力** | 检测 Minimax Key / macOS say / Windows SAPI / pyttsx3 | 旁白配音 |

**检测命令**（AI 自动执行）：
```bash
python3 scripts/render_video.py --check-env
python3 scripts/tts_generator.py --check
```

### 2.2 能力卡片示例

检测完成后，向用户展示这样一张卡片：

```
┌─────────────────────────────────────────┐
│     纳川教学视频 · 你的能力卡片          │
├─────────────────────────────────────────┤
│                                         │
│  ✅ Node.js          v20.10.0           │
│  ✅ HyperFrames      可用（自动下载）     │
│  ✅ ffmpeg           已安装              │
│                                         │
│  🔊 配音引擎                            │
│     ✅ macOS say    Tingting（系统内置）  │
│     ⚡ 可升级       Minimax（配API Key） │
│                                         │
├─────────────────────────────────────────┤
│  你的等级：基础版（零配置可用）           │
│  可以做的事：                             │
│    ✅ 生成完整教学视频（系统配音）        │
│    ✅ 生成无声循环动图                    │
│    ✅ 5段分镜 + 字幕 + 1080p MP4         │
│                                         │
│  升级建议（配了效果更好）：               │
│    ⚡ 配置 Minimax API Key → 高清配音    │
│       约 0.01元/千字，非常便宜           │
└─────────────────────────────────────────┘
```

### 2.3 本地配音质量提示

如果检测到是系统内置配音（macOS say 或 Windows SAPI），自动提示：

> 当前使用系统内置配音，音质一般，但完全够用。
> 我们会自动把字幕做清晰做大，确保学生看得清楚。
> 想要更自然的配音，配置 Minimax API Key 就行，很便宜。

### 2.4 进阶选项一览

| 能力 | 免费版 | 进阶版 | 大概费用 | 怎么配置 |
|------|--------|--------|---------|---------|
| 视频渲染 | 本地免费 | 本地免费 | 0 元 | 装 Node.js + ffmpeg |
| 配音 | 系统内置 | Minimax TTS | 约 0.01 元/千字 | 设 `MINIMAX_API_KEY` |
| 生图 | TRAE 内置 | 外部 API | 约 0.1-0.5 元/张 | 设对应环境变量 |

### 2.5 一句话开始

- 就想用本地版？没问题，直接开始就行 👉
- 想升级？随时告诉我"配置配音API"

---

## 三、快速模式：4步出视频

> **适合人群**：第一次用、想快速出结果、追求效率
> **质量保证**：2道核心质量门（内容准确 + 视频可看），放心交付

### 3.1 四步流程

只需告诉AI一个知识点，剩下的自动搞定：

```
你说："做一个速度与加速度的教学视频"
    ↓
Step 1：概念输入 — 你给一个知识点，AI 自动识别学科和年级
    ↓
Step 2：AI 自动生成 — 分镜 + 文案 + HTML 场景一起出（5段结构）
    ↓
Step 3：配音生成 — 5级 fallback，零配置也能用
    ↓
Step 4：渲染交付 — 本地 HyperFrames 渲染成 MP4
```

### 3.2 AI 执行步骤详解

**Step 1：概念输入（你 → AI）**
- 用户给一个知识点名称
- AI 自动识别：学科、年级、章节
- 不确定时才问（默认：初二物理）

**Step 2：AI 自动生成内容**
1. 确定知识点拆解（拆成 3-4 个子概念）
2. 按模板写 5 段旁白文案
3. 选择对应场景积木
4. 生成完整的 index.html（基于 standard_16x9.html 模板修改）
5. 生成 storyboard.json

**Step 3：配音生成**
```bash
python3 scripts/tts_generator.py --storyboard storyboard.json --outdir audio/
```
- 自动选择最佳配音引擎
- 输出 5 段 mp3 + durations.json
- 时间轴数据同步到 index.html

**Step 4：渲染交付**
```bash
python3 scripts/render_video.py <项目目录>
```
- 自动 lint + validate + render
- 输出 MP4 文件
- 失败时有友好的错误提示

### 3.3 两种产出，一次搞定

两种产出**共用同一个 `index.html`**，靠 HyperFrames 变量 `mode` 切换——搭一次内容，两种都能出：

| 产出 | 规格 | 用途 | 命令 |
|---|---|---|---|
| **配音视频** | 1080p、60-90s、中文旁白 + 字幕 | 完整讲解，发视频号 / 给孩子看 | `--mode video` |
| **无声动图** | 1080p、~32s、无声、循环 | 公众号内嵌、知识点快速回顾 | `--mode silent` |

> 为什么不出 GIF？GIF 无帧间压缩，1080p 高清必然 >20MB。
> 公众号早已支持内嵌 MP4 自动播放，无声 MP4 = 1080p + 8~10MB，比任何 GIF 都清晰。

### 3.4 2道核心质量门

快速模式只保留最关键的两道检查，确保不踩坑：

| 质量门 | 检查什么 | 不通过怎么办 |
|--------|---------|-------------|
| **G1：内容准确性检查** | 知识点有没有错、公式对不对、术语准不准 | 自动修正后继续 |
| **G4：最终QA** | 视频能不能看、字幕清不清、能不能正常播放 | 快速修复后重新渲染 |

### 3.5 字幕优化（自动适配）

- 如果配音是系统内置的（音质一般），**自动把字幕做大做清晰**，确保学生能看懂
- 字幕默认位置：底部安全区，字号 32-34px，高对比度
- 字幕与旁白自动同步，时间轴精确到毫秒

### 3.6 什么时候问用户

快速模式默认一路自动往下走，**只有遇到这些情况才问你**：
- 不确定学科/年级（你说"浮力"，AI不知道是初二还是高中）
- 知识点超出了初中范围
- 渲染失败需要你帮忙排查
- 其他拿不准的地方

---

## 四、触发路由

| 用户说 | 做什么 |
|---|---|
| "教学视频" / "配音" / "讲解版" / "纳川" | 快速模式 → 配音视频 |
| "教学动图" / "无声" / "循环" / "公众号内嵌" | 快速模式 → 无声动图 |
| "视频和动图都要" | 快速模式 → 两个都出 |
| "用专业模式" / "详细点做" / "按完整管线来" | 进阶模式 → 8阶段完整管线 |

不确定时，**先问清楚概念 + 适用学段（默认初二物理）**，其他别问。

---

## 五、完整8阶段工作流（专业模式）

> **适合人群**：追求高质量、要发正式内容、想精细控制每一步
> **怎么启用**：说"用专业模式"或"按完整管线来"
> **包含内容**：8阶段管线 + 五维分镜 + 全部4个质量门

```
阶段0：研究拆解 ──→ 阶段1：概念提案 ──→ 阶段2：脚本撰写 ──→ 阶段3：分镜设计
   (质量门G1)          (质量门G1)          (质量门G1)          (质量门G2)

阶段4：资产准备 ──→ 阶段5：场景编排 ──→ 阶段6：渲染合成 ──→ 阶段7：质量验收
   (质量门G2)          (质量门G3)          (质量门G4)          (最终QA)
```

### 阶段 0：研究与拆解

**目标**：动笔之前把知识点彻底搞懂。

**执行**：
1. 翻查对应学段教材定义，确认知识边界
2. 挖掘 2-3 个常见误解（"误解优先法"的弹药）
3. 联想 2-3 个生活场景
4. 拆成 3-5 个子概念，按逻辑递进排序

**输出**：知识点清单 + 误解清单 + 子概念拆解

**质量门 G1-内容准确**：核心定义与教材一致，至少找到 1 个真实误解。

→ 详见 `references/storytelling.md`

### 阶段 1：概念提案

**目标**：确定钩子、叙事策略、整体结构。

**执行**：
1. 选钩子策略（默认：误解优先法）
2. 确定叙事弧线类型（误解优先型 / 引导发现型 / 递进讲解型）
3. 选定配色方案（从设计系统 4 套调色板中选）
4. 确定配音引擎（auto 自动选择）

**输出**：钩子文案 + 弧线类型 + 配色方案

### 阶段 2：脚本撰写

**目标**：写出 5-7 段旁白文案，每段配画面描述。

**执行**：
1. 按弧线类型写每段旁白（30-50字/段）
2. 每段配画面描述（布局 + 主体 + 出场顺序 + 动效）
3. 组装成 storyboard.json

**输出**：`storyboard.json`（完整分镜脚本）

→ 详见 `templates/narration_template.md`

### 阶段 3：分镜设计

**目标**：把脚本变成可执行的视觉蓝图——五维分镜。

**执行**：每个场景回答 5 个维度：
- **Subject**：画面核心主体是什么
- **Motion**：主体怎么动（入场方式、运动轨迹）
- **Scene**：布局、叠加层（chip/callout/ghost）
- **Spatial**：元素位置关系、视觉焦点
- **Camera**：景别（教学视频多为固定镜头）

**输出**：五维分镜描述 + 资产清单

### 阶段 4：资产准备

**目标**：生成所有素材文件。

**执行**：
1. TTS 配音生成（5 级 fallback）
2. 准备 SVG 素材（从组件库选）
3. 生成项目骨架（从模板复制）

**命令**：
```bash
python3 scripts/tts_generator.py --storyboard storyboard.json --outdir audio/
```

**输出**：`audio/` 目录 + 时间轴 `durations.json`

→ 详见 `references/audio_guide.md`

### 阶段 5：场景编排

**目标**：填充 HTML 场景内容，编写 GSAP 动效。

**执行**：
1. 复制 `templates/standard_16x9.html` 为 `index.html`
2. 替换配色变量（按选定调色板）
3. 修改 5 个场景的内容（SVG + 卡片文字）
4. 编写每个场景的 GSAP 入场动画
5. 同步时间轴（从 durations.json 读取）

**动效规范**：
- 动效四原则：缓入缓出、预备动作、超出回弹、分层错峰
- 每场景 ≥ 3 种 ease、≥ 2 个入场方向
- 用 `fromTo` 不用 `from`
- 环境动效挂在 tl 上，不能裸 `gsap.to()`

→ 详见 `references/design_system.md` 和 `references/svg_components.md`

### 阶段 6：渲染合成

**目标**：lint → validate → 渲染 → 产出 MP4。

**命令**：
```bash
# 配音视频
python3 scripts/render_video.py <项目目录>

# 无声动图
python3 scripts/render_video.py <项目目录> --mode silent
```

**执行步骤**：
1. Lint 检查（0 error 通过）
2. Validate 结构验证
3. HyperFrames 渲染
4. 输出 MP4 文件

→ 详见 `scripts/render_video.py`

### 阶段 7：质量验收

**目标**：最终全面检查，确保交付标准。

**检查项**：
- 渲染质量：无花屏、无卡顿
- 字幕同步：时间对齐、字号达标
- 配色合规：WCAG 对比度
- 文字布局：安全区内、无溢出
- 动效流畅：入场流畅、转场自然
- 音频质量：清晰、无杂音

**交付标准**：严重问题 = 0，轻微问题 ≤ 2 个

→ 详见 `references/quality_checklist.md`

---

## 六、模板使用说明

### 6.1 标准模板位置

```
templates/
├── standard_16x9.html       # 标准16:9横版视频模板（5个场景+GSAP）
├── scene_building_blocks.md # 场景积木库（10种常用场景）
└── narration_template.md    # 旁白文案模板
```

### 6.2 standard_16x9.html 模板结构

**已验证可直接渲染**：`npx hyperframes render` 一次成功。

```
场景 1：标题引入（icon + 大标题 + 子概念标签 + 副标题）
场景 2：概念一（左图右卡：SVG示意图 + info-card + callout）
场景 3：概念二（同上，用对比色区分）
场景 4：对比/问答（对比表格 + 底部提示）
场景 5：总结（大数字 + 总结卡片 + 徽章行）
```

**模板特点**：
- 1920×1080 横版（16:9）
- 莫兰迪暖橙色系（可替换为其他调色板）
- 包含人物 emoji、SVG箭头、SVG公式、卡片动效
- GSAP 时间轴已注册到 `window.__timelines`
- `data-duration` 设置总时长（默认 65s）
- `data-composition-id` 正确设置
- 5 段字幕自动同步
- 模糊叠化 + push-up 两种转场

### 6.3 使用模板的步骤

1. **复制模板**：把 `templates/standard_16x9.html` 复制为项目的 `index.html`
2. **改配色**：替换 `:root` 中的 CSS 变量（按设计系统调色板）
3. **改章节名**：修改 `.chapter-label` 的文字
4. **改场景内容**：逐个修改 5 个 `.scene` 的内容（SVG + 文字）
5. **改时间轴**：修改 `SCENES` 数组的 start/duration/subtitle
6. **改动效**：修改 `buildSceneN()` 函数中的动画编排
7. **改总时长**：修改根 `data-duration` 属性

### 6.4 场景积木库

10 种常用场景积木，AI 可直接挑选组合：
1. 标题引入页 (Title Scene)
2. 概念讲解页 (Concept Scene) — 最常用
3. 对比表格页 (Compare Table Scene)
4. 公式推导页 (Formula Derivation Scene)
5. 实验演示页 (Experiment Scene)
6. 生活应用页 (Real-world Scene)
7. 问答互动页 (Q&A Scene)
8. 时间轴页 (Timeline Scene)
9. 分类归纳页 (Classification Scene)
10. 总结收束页 (Summary Scene)

→ 详见 `templates/scene_building_blocks.md`

---

## 七、配音方案说明（5级 fallback）

### 7.1 五级 fallback 链

自动检测当前系统可用的最佳引擎，优先级从高到低：

| 优先级 | 引擎 | 支持系统 | 音质 | 需要配置 |
|:---:|------|---------|------|:-------:|
| 1 | **Minimax TTS** | 全平台 | 高清 | 需要 API Key |
| 2 | **macOS say** | macOS 仅 | 一般 | 零配置 |
| 3 | **Windows SAPI** | Windows 仅 | 一般 | 零配置 |
| 4 | **pyttsx3** | 全平台 | 一般 | 需 pip 安装 |
| 5 | **纯文本时长估算** | 全平台 | 无音频 | 零配置 |

### 7.2 零配置也能用

- macOS 用户：自动用系统自带的 say 命令（Tingting 中文女声）
- Windows 用户：自动用 PowerShell + System.Speech
- Linux 用户：自动降级到纯文本时长估算（生成静音占位音频 + 完整时间轴）

不管什么平台，**一定能生成完整的时间轴和视频**，只是配音质量不同。

### 7.3 升级到高清配音

设置一个环境变量即可升级：
```bash
export MINIMAX_API_KEY=你的API密钥
```

- 费用约 0.01 元/千字，一分钟视频约 0.0015 元
- 高清自然音色，接近真人朗读
- 脚本自动检测到 Key 就会优先使用

→ 详见 `references/audio_guide.md`

---

## 八、质量保证机制

### 8.1 四道质量门

| 质量门 | 阶段 | 核心检查 |
|--------|------|---------|
| **G1** | 脚本完成后 | 内容准确性 + 结构完整性 |
| **G2** | 分镜完成后 | 五维分镜 + 动效有效性 |
| **G3** | 场景编排后 | 设计规范 + 音画同步 |
| **G4** | 渲染完成后 | 渲染质量 + 最终 QA |

- **快速模式**：只启用 G1 + G4（2 道核心门）
- **专业模式**：启用全部 4 道质量门

### 8.2 内容准确性保证

- 核心定义交叉验证 2 个以上来源
- 物理/化学常量严格核对
- 公式、单位、术语规范检查
- 常见误解提前标注，避免误导

### 8.3 渲染质量保证

- 渲染前自动 lint 检查（0 error 才继续）
- 结构验证（validate）
- 失败时有详细的错误提示和排查建议
- 自动检测环境缺失，给出安装指引

→ 详见 `references/quality_checklist.md`

---

## 九、核心方法论

纳川教学视频融合了以下教学理念，快速模式也遵循这些底层逻辑：

| 方法论 | 在快速模式中的体现 |
|---|---|
| **误解优先法** | 默认用"很多人以为……但其实不是"开头，抓住注意力 |
| **讲解型弧线** | 5 段结构（标题→概念1→概念2→对比→总结），符合认知规律 |
| **Mayer 多媒体原则** | 图文结合、时空同步、信号强调、控制认知负荷 |
| **动效四原则** | 缓入缓出、预备动作、超出回弹、分层错峰 |
| **60-30-10 配色** | 60% 底色 + 30% 中性 + 10% 强调，视觉舒适 |

→ 详见 `references/storytelling.md`

---

## 十、常见问题

### Q：这个 skill 下载下来就能用吗？
A：是的。只要你有 Node.js 和 ffmpeg，零配置就能生成完整视频。系统自带配音也够用。

### Q：没有 API Key 也能用吗？
A：完全可以。Minimax API Key 只是提升配音质量，不是必需的。macOS 和 Windows 都有系统自带 TTS。

### Q：Linux 上能用吗？
A：能。Linux 上如果没有 TTS 引擎，会自动用纯文本时长估算兜底，生成完整时间轴和画面，只是没有配音。有 Minimax Key 的话就有高清配音了。

### Q：生成一个视频要多久？
A：60 秒视频，本地渲染大约 1-3 分钟（取决于电脑性能）。AI 生成内容大约 1-2 分钟。总共 3-5 分钟。

### Q：可以生成竖版视频吗？
A：当前模板是横版 16:9（1920×1080）。竖版 9:16 可以通过修改 CSS 尺寸和布局实现，原理一样。

### Q：模板渲染失败怎么办？
A：
1. 先运行 `python3 scripts/render_video.py --check-env` 检查环境
2. 运行 `--lint-only` 看 lint 错误
3. 检查 Node.js 和 ffmpeg 是否安装
4. 检查网络（首次运行需要下载 HyperFrames）

### Q：怎么改配音语速？
A：设置 `TTS_RATE` 环境变量，如 `export TTS_RATE=0.95`（稍慢更清晰）。

### Q：可以自定义模板吗？
A：完全可以。`templates/standard_16x9.html` 就是一个起点，你可以随意修改扩展。只要遵守 HyperFrames 的规范（单一时间轴、fromTo、data-duration 等），就能正常渲染。

### Q：为什么用 HTML + GSAP 而不是其他方案？
A：
- 学习成本低：前端开发者都熟悉
- 灵活度高：SVG/CSS 什么都能画
- 性能好：GSAP 是最快的 JS 动画库
- 跨平台：浏览器里就能预览
- HyperFrames 原生支持：渲染质量有保障

---

## 附录：文件索引

| 文件 | 用途 | 什么时候看 |
|------|------|-----------|
| `SKILL.md` | 主文档（本文件） | 第一次看，了解全貌 |
| `templates/standard_16x9.html` | 标准 16:9 模板（可直接渲染） | 写 HTML 场景时 |
| `templates/scene_building_blocks.md` | 10 种场景积木 | 选场景类型时 |
| `templates/narration_template.md` | 旁白文案模板 | 写脚本时 |
| `references/design_system.md` | 设计系统（配色/字体/动效） | 统一视觉风格时 |
| `references/svg_components.md` | SVG 动画组件库 | 画示意图时 |
| `references/storytelling.md` | 教学叙事方法论 | 构思内容结构时 |
| `references/quality_checklist.md` | 质量检查清单 | 做 QA 时 |
| `references/audio_guide.md` | 配音方案说明 | 配音相关问题时 |
| `scripts/render_video.py` | 视频渲染脚本 | 渲染视频时 |
| `scripts/tts_generator.py` | 配音生成脚本 | 生成配音时 |


## 文件 nachuan-tujie/SKILL.md

---
name: nachuan-tujie
description: 将初中全科及高中预科知识点制作成可检查的 9:16 教育信息图，包含文字提纲、HTML/SVG 排版、本地 PNG 渲染和教材核对流程。用于用户提出“纳川图解”“做一张信息图”“知识卡片”“学科图解”，或希望把数学、物理、化学、生物等抽象概念做成竖版知识图时。
---

# nachuan-tujie（纳川图解）

> 准高中生AI学习伙伴 · 初中全科知识图解 · HTML+SVG 可检查渲染 · 基础模式无需外部生图 API

---

## 基本信息

| 字段 | 值 |
|------|-----|
| **name** | nachuan-tujie |
| **description** | 纳川图解·准高中生AI学习伙伴。将初中全科（语数英物化生政史地）及高中预科知识点转化为9:16竖版教育信息图。用 HTML+SVG 绘制，便于逐项检查文字、公式和方向，并在本地渲染为 PNG。 |
| **triggers** | 做一张信息图、知识卡片、学科图解、物理信息图、化学信息图、做张知识图、画个知识卡片、把这个知识点做成图、纳川图解、nachuan-tujie |
| **tags** | education, infographic, knowledge-card, 初中, 高中预科, SVG, HTML, 本地渲染 |
| **mode** | 快速模式（默认）/ 专业模式 |
| **输出格式** | PNG（1080×1920，9:16竖版） |

---

## 定位

纳川图解是面向**准高中生**（初三升高一）的AI学习伙伴，把抽象的知识点变成一张**看得懂、记得住、能分享**的竖版信息图。

**核心优势：**
- **准确性可检查** — 用 HTML+SVG 绘制文字、公式和方向，生成后仍须按清单和教材复核
- **基础模式无需外部 API Key** — 本地渲染仍需 Node.js、npx 和首次下载依赖的网络条件
- **设计系统** — 内置莫兰迪配色和组件库，每张图都有专业质感
- **快速出图** — 快速模式3步搞定，输入知识点直接交付

---

## 第一次使用：能力检测

> **重要：** 第一次调用本skill时，必须先执行环境检测，确保渲染所需工具都已就绪。

执行以下命令检测环境：

```bash
# 检测 Node.js
node --version

# 检测 npx（随 Node.js 一起安装）
npx --version

# 检测 HyperFrames CLI（首次运行会自动安装，耐心等待）
npx hyperframes --version
```

**检测结果处理：**

| 工具 | 已安装 | 未安装/报错 |
|------|--------|-------------|
| Node.js | ✅ 继续 | 告诉用户去 https://nodejs.org 下载安装 LTS 版本 |
| npx | ✅ 继续 | 通常随 Node.js 一起安装，重装 Node.js 即可 |
| HyperFrames | ✅ 继续 | 首次 `npx hyperframes` 会自动从 npm 下载，无需手动安装 |

> 如果 HyperFrames 首次运行下载很慢，可以先执行 `npm config set registry https://registry.npmmirror.com` 切换到国内镜像。

---

## 快速模式（默认）：3步出图

用户只需要给一个知识点名称，其余全自动。

### 第1步：知识点输入

用户说："做一张关于[知识点名称]的信息图"

示例：
- "做一张关于速度vs加速度的物理信息图"
- "画个勾股定理知识卡片"
- "把光合作用做成图"

### 第2步：AI生成HTML

AI自动完成以下工作：

1. **学科识别** — 判断属于哪门学科（物理/数学/化学/生物/...）
2. **章节定位** — 确定在教材中的大致位置和难度
3. **知识点拆解** — 拆成3-5个核心子概念
4. **配色选择** — 从6套莫兰迪色系中选一套（见 `references/design_system.md`）
5. **模板选择** — 根据内容结构选模板：
   - 标准竖版（`templates/standard_9x16.html`）：概念+公式+易错点+总结，最通用
   - 左右对比（`templates/comparison.html`）：两个概念对比辨析
   - 三卡片（`templates/three_card.html`）：三个并列概念/方法/步骤
6. **内容填充** — 把文字、公式、示意图填入模板对应位置
7. **准确性自检** — 按 `references/accuracy_checklist.md` 逐项检查

**输出：** 一个完整的 HTML 文件，保存到用户工作目录。

### 第3步：渲染PNG

调用渲染脚本生成PNG：

```bash
# 方式一：使用 Python 脚本（推荐，有友好错误提示）
python3 scripts/render_png.py <输入HTML路径> <输出PNG路径>

# 方式二：直接用 HyperFrames CLI
npx hyperframes snapshot <输入HTML路径> -o <输出PNG路径> --width 1080 --height 1920
```

渲染完成后，把 PNG 文件路径告诉用户。

---

## 完整工作流程（专业模式 / 7步）

当用户说"用专业模式"时，启用完整7步工作流，质量更高但步骤更多。

### 阶段一：理解与规划（第1-2步）

**第1步：学科诊断**
- 识别学科、年级、章节
- 判断知识点难度和重要性
- 确定目标受众（初一/初二/初三/高中预科）
- 输出：学科诊断卡

**第2步：内容架构设计**
- 拆解核心子概念（3-5个）
- 设计类比/比喻（帮助理解的生活实例）
- 规划信息图结构（选择模板 + 自定义区域）
- 选定配色方案
- 输出：内容架构草图（文字版）

### 阶段二：创作与绘制（第3-5步）

**第3步：文案撰写**
- 标题（主标题 + 副标题）
- 概念卡片文案（每个子概念1句话）
- 公式/定理表述（准确、规范）
- 易错点提示（2-3个常见误区）
- 总结金句（1句话记住核心）
- 输出：完整文案稿

**第4步：SVG示意图设计**
- 根据知识点类型绘制示意图
- 物理：受力图、运动轨迹、电路图
- 数学：几何图形、函数图像、数轴
- 化学：分子结构、实验装置、反应过程
- 生物：细胞结构、生理过程、生态系统
- 所有图形用 SVG 精确绘制，坐标可计算
- 输出：SVG 代码片段

**第5步：HTML组装**
- 基于选定模板
- 把文案、公式、SVG示意图填入
- 调整间距、配色、排版
- 确保所有元素在 1080×1920 画布内
- 输出：完整 HTML 文件

### 阶段三：质检与交付（第6-7步）

**第6步：准确性检查**
- 按 `references/accuracy_checklist.md` 逐项核查
- 学科知识准确性（公式、定义、单位）
- 文字正确性（无错别字、无乱码）
- 图形准确性（方向、比例、标注）
- 不通过则返回第4/5步修改
- 输出：质检报告

**第7步：渲染交付**
- 渲染 PNG（1080×1920）
- 验证渲染结果（用 Read 工具查看图片）
- 如有问题，修改 HTML 重新渲染
- 交付最终 PNG 文件
- 输出：最终PNG + 知识点简要说明

---

## 模板使用说明

### 标准竖版模板 `templates/standard_9x16.html`

**适用场景：** 大多数单一知识点讲解

**结构：**
```
┌─────────────────────┐
│  标题区（学科徽章+标题+副标题）  │  ← 顶部 15%
├─────────────────────┤
│  概念卡片区（3张卡片）      │  ← 上中部 25%
├─────────────────────┤
│  公式区（核心公式+推导）     │  ← 中部 20%
├─────────────────────┤
│  易错点区（2-3个误区）      │  ← 下部 20%
├─────────────────────┤
│  总结区（一句话记忆）       │  ← 底部 20%
└─────────────────────┘
```

**使用方法：** 复制模板文件，替换 `<!-- 替换:xxx -->` 标记处的内容。

### 左右对比模板 `templates/comparison.html`

**适用场景：** 两个相似概念的对比辨析（如速度vs加速度、质量vs重量、动能vs势能）

**结构：**
```
┌─────────────────────┐
│  标题区              │
├──────────┬──────────┤
│  概念A    │  概念B    │  ← 左右两列对比
│  定义     │  定义     │
│  公式     │  公式     │
│  单位     │  单位     │
│  方向     │  方向     │
├──────────┴──────────┤
│  联系与区别总结       │
└─────────────────────┘
```

### 三卡片模板 `templates/three_card.html`

**适用场景：** 三个并列概念/方法/步骤（如三种物态变化、三种电路连接方式、三种化学反应类型）

**结构：**
```
┌─────────────────────┐
│  标题区              │
├─────────────────────┤
│  ┌───────────────┐  │
│  │  卡片1        │  │
│  └───────────────┘  │
│  ┌───────────────┐  │
│  │  卡片2        │  │  ← 三张卡片纵向排列
│  └───────────────┘  │
│  ┌───────────────┐  │
│  │  卡片3        │  │
│  └───────────────┘  │
├─────────────────────┤
│  总结区              │
└─────────────────────┘
```

---

## 渲染命令说明

### 推荐方式：Python 渲染脚本

```bash
python3 /path/to/nachuan-tujie/scripts/render_png.py input.html output.png
```

**特性：**
- 自动检测 Node.js 和 HyperFrames 是否安装
- 未安装时给出清晰的安装指引
- 渲染失败时显示错误原因
- 跨平台兼容（macOS / Windows / Linux）

### 备选方式：直接调用 HyperFrames CLI

```bash
# 基本用法
npx hyperframes snapshot input.html -o output.png

# 指定尺寸（9:16竖版）
npx hyperframes snapshot input.html -o output.png --width 1080 --height 1920

# 等待页面加载完成（如果有字体或外部资源）
npx hyperframes snapshot input.html -o output.png --wait 1000
```

### 备选方式：Puppeteer（Python 脚本内置 fallback）

如果 HyperFrames 不可用，脚本会自动尝试用 Puppeteer 截图。

安装 Puppeteer 的 Python 版本：
```bash
pip install pyppeteer
python -m pyppeteer-install
```

---

## 准确性保证机制

### 三层准确性保障

**第一层：内容生成阶段**
- AI 基于学科知识生成内容
- 公式用标准数学符号书写
- 单位使用国际标准单位
- 定义表述参照教材原文

**第二层：SVG精确绘制**
- 所有图形用 SVG 代码精确绘制，坐标可计算
- 物理矢量箭头方向严格正确
- 数学几何图形比例准确
- 化学结构式键角符合实际
- 文字用 HTML/SVG text 元素，降低生图文字乱码风险，渲染后仍需检查字体和内容

**第三层：自检清单**
- 生成后按 `references/accuracy_checklist.md` 逐项检查
- 涉及公式的：检查公式书写、单位、符号
- 涉及图形的：检查方向、比例、标注
- 涉及文字的：检查错别字、术语准确性
- 不通过的必须修改后重新渲染

### 学科自检库

每个学科有专门的自检要点，详见 `references/accuracy_checklist.md`。

---

## 常见问题

### Q1: 渲染失败，提示找不到 hyperframes？

A: 首次运行 `npx hyperframes` 会自动从 npm 下载。如果下载慢，可以先设置国内镜像：
```bash
npm config set registry https://registry.npmmirror.com
```
然后再运行渲染命令。

### Q2: 渲染出来的图片是空白的？

A: 可能原因：
1. HTML 文件路径不对 — 检查路径是否正确
2. 页面还没加载完就截图了 — 加 `--wait 1000` 参数
3. CSS 没加载 — 确保所有样式都是内联的，不依赖外部文件

### Q3: 中文字体显示为方块？

A: 系统缺少中文字体。安装以下任意一种字体即可：
- macOS：系统自带苹方，一般不会有问题
- Windows：系统自带微软雅黑
- Linux：安装 `fonts-noto-cjk` 或 `wqy-microhei`

### Q4: 怎么自定义配色？

A: 修改 HTML 文件顶部的 CSS 变量即可。6套预设配色见 `references/design_system.md`。

### Q5: 可以生成横版或方形的图吗？

A: 本skill默认输出9:16竖版（适配手机阅读）。如果需要其他比例，可以修改模板的 `width` 和 `height`，同时调整各区域的布局。

### Q6: 生成的图可以商用吗？

A: 生成内容的使用范围取决于你输入的教材、图片、字体和其他素材的授权条件。发布或商用前，请确认素材许可，并避免直接复制受保护的教材版面或插图。

### Q7: 为什么不用 AI 生图？

A: AI 生图在教育场景中可能出现文字乱码、公式错误或方向画反。HTML+SVG 便于逐项检查和修改，但不能替代教材核对；生成后仍要检查定义、公式、单位、箭头和过程。

---

## 目录结构

```
nachuan-tujie/
├── SKILL.md                    # 本文档
├── templates/
│   ├── standard_9x16.html      # 标准9:16竖版模板
│   ├── comparison.html         # 左右对比型模板
│   └── three_card.html         # 三卡片型模板
├── references/
│   ├── design_system.md        # 设计系统（配色/字体/间距）
│   ├── components.md           # SVG组件库（箭头/公式/卡片）
│   ├── accuracy_checklist.md   # 准确性检查清单
│   └── prompt_guide.md         # 内容创作指南
└── scripts/
    └── render_png.py           # HTML转PNG渲染脚本
```

