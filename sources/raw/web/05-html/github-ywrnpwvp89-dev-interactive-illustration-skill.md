# interactive-illustration-skill：科学可视化学习（中文）

- 链接：https://github.com/ywrnpwvp89-dev/interactive-illustration-skill
- 作者：ywrnpwvp89-dev
- 仓库说明：面向医学、生物、化学物理、工程、数学的科学视觉学习 Skill。
- 星数：2
- 获取方式：GitHub README + SKILL/说明文件

---

## README

# interactive-illustration

> Version 1.0.0 · Scientific visual learning skill for biology, medicine, chemistry, physics, engineering, and mathematics.

## English

`interactive-illustration` routes each visualization request into one of two modes:

- **Professional precise** — publication-, lecture-, competition-solution-, or presentation-ready static figures. Use code for exact geometry, coordinates, functions, data, vectors, circuit symbols, and engineering dimensions; use AI image generation only for conceptual visuals.
- **Interactive learning** — runnable HTML/SVG/Canvas/WebGL learning pages with controls, animation, synchronized formulas, explanations, reset behavior, and a static fallback. Use this mode when the learner needs to explore variables, spatial relationships, limiting cases, or common misconceptions.

The skill covers 24 scene templates and interactive learning models for mechanics, electromagnetism, waves/optics, and physics-competition methods. It asks the user to choose a mode only when the intended deliverables cannot be inferred reliably.

### Quick start

```bash
# AI-generated conceptual figure
python scripts/generate_image.py --prompt "..." --size 16:9 --resolution 2k

# Exact geometry or coordinate figure
python scripts/generate_geometry.py garfield --a 3 --b 4

# Interactive learning starter
python scripts/scaffold_interactive.py \
  --example spherical-basis \
  --output ./outputs/spherical-basis.html
```

See [SKILL.md](SKILL.md) for routing rules, [references/interactive-learning.md](references/interactive-learning.md) for interaction design, and [references/interactive-models.md](references/interactive-models.md) for the model catalog.

### Reference project

This project is an interactive-learning extension of the open-source project [liangdabiao/stem-illustration-skill](https://github.com/liangdabiao/stem-illustration-skill). The original scene templates and image-generation workflow are retained where applicable; the mode router, interactive learning specifications, scientific validation rules, and interactive starter are added here.

### License

Released under the [MIT License](LICENSE).

---

# 中文说明

面向物理、工程、数学的科学视觉学习 Skill。

先判断用户需要专业精细型静态图，还是交互学习型可视化页面，再生成科研示意图、教学插图、技术架构图或可操作的学习页面，覆盖生物、医学、化学、物理、工程、数学。

## 功能特性

- **24 个场景模板**：信号通路、细胞结构、质粒图、化学结构、流程、信息图、海报、剖视图、机械示意、物理示意、数学可视化、架构图等
- **6 个学科方向**：生物/医学/化学/物理/工程/数学
- **4 种风格变体**：academic / textbook / infographic / 3d-render
- **统一生图脚本**：自动兼容 OpenAI 同步 API 和 apimart.ai 异步 API
- **双模式路由**：专业精细型 / 交互学习型
- **交互学习页面**：原生 HTML/CSS/Canvas 球坐标示例，可作为三维教学可视化起点
- **学术诚信保护**：禁止用 AI 生成真实实验数据图

## 重点工具

- 数学严格几何图：`scripts/generate_geometry.py`
- AI 概念图：`scripts/generate_image.py`
- 交互学习示例：`scripts/scaffold_interactive.py`

## 目录结构

```
stem-illustration/
├── SKILL.md                         # Skill 核心规则
├── README.md                        # 本文件
├── .env.example                     # 环境变量模板
├── .gitignore
├── scripts/
│   ├── generate_image.py            # AI 概念图
│   ├── generate_geometry.py         # 严格几何图
│   └── scaffold_interactive.py     # 交互学习页面起点
└── references/
    ├── mode-selection.md            # 输出模式判断与追问
    ├── interactive-learning.md     # 交互学习页面规范
    ├── scientific-validation.md    # 科学正确性校验
    ├── interactive-models.md       # 力学/电磁学/波动/竞赛模型目录
    └── templates/                   # 24 个场景模板
        ├── 01-signaling-pathway.json
        ├── 02-experimental-workflow.json
        ├── 03-cell-structure.json
        ├── 04-data-infographic.json
        ├── 05-academic-poster.json
        ├── 06-concept-infographic.json
        ├── 07-timeline.json
        ├── 08-comparison-matrix.json
        ├── 09-cross-section.json
        ├── 10-hub-spoke.json
        ├── 11-hierarchical-tree.json
        ├── 12-cyclic-flow.json
        ├── 13-multi-panel-figure.json
        ├── 14-plasmid-map.json
        ├── 15-machine-mechanism.json
        ├── 16-physics-schematic.json
        ├── 17-chemistry-structure.json
        ├── 18-math-concept.json
        ├── 19-graphical-abstract.json
        ├── 20-lab-safety.json
        ├── 21-educational-poster.json
        ├── 22-step-by-step.json
        ├── 23-architecture-diagram.json
        └── 24-bilingual-diagram.json
```

## 快速开始

### 1. 配置环境变量

```bash
cp .env.example .env
# 编辑 .env，填入 IMG_BASE_URL / IMG_MODEL / IMG_API_KEY
```

### 2. 直接生图

```bash
# 异步模式（apimart.ai 推荐）
python scripts/generate_image.py --prompt-file ./prompt.txt --size 3:4 --resolution 2k

# 同步模式（OpenAI 兼容）
python scripts/generate_image.py --prompt "..." --size 1024x1536 --quality high
```

### 3. 生成交互学习页面

交互型输出不是普通图片，使用页面脚本生成：

```bash
python scripts/scaffold_interactive.py \
  --example spherical-basis \
  --output ./outputs/spherical-basis.html
```

打开 HTML 后可拖动旋转视角、滚轮缩放、调节 `r/θ/φ`，并切换球面、坐标曲线和三个局部基向量。复杂主题应以此为结构参考，先建立自己的数学状态模型，再扩展交互。

交互模型目录见 [references/interactive-models.md](references/interactive-models.md)，当前覆盖斜抛、简谐振动、碰撞、点电荷电场、带电粒子运动、高斯定律、波的叠加、驻波、双缝干涉、守恒律、量纲分析、极限情况和受力/能量法。

### 4. 作为 Skill 加载

将本目录放到 LLM Agent 的 skills 目录下，Agent 会自动按 SKILL.md 规则工作：

- 先判断专业精细型或交互学习型
- 专业精细型：收集学科/图表类型/受众/术语/尺寸/语言，匹配模板并输出视觉简报
- 交互学习型：提取学习目标、变量、不变量和反馈，生成可运行页面
- 只有专业精细型的概念图才调用 `generate_image.py`

## 保留模板速查

| 触发词 | 模板 | 场景 |
|---|---|---|
| 信号通路, pathway, 机制图 | [01](references/templates/01-signaling-pathway.json) | 信号通路/分子机制图 |
| 实验流程, workflow, 技术路线 | [02](references/templates/02-experimental-workflow.json) | 实验流程/技术路线图 |
| 细胞结构, 解剖图, organelle | [03](references/templates/03-cell-structure.json) | 细胞/解剖结构图 |
| 数据信息图, data infographic | [04](references/templates/04-data-infographic.json) | 数据可视化信息图 |
| 学术海报, conference poster | [05](references/templates/05-academic-poster.json) | 双语学术海报 |
| 概念图, concept infographic | [06](references/templates/06-concept-infographic.json) | 概念教育信息图 |
| 时间线, timeline, 科学史 | [07](references/templates/07-timeline.json) | 科学史时间线 |
| 对比, 比较, comparison | [08](references/templates/08-comparison-matrix.json) | 对比矩阵 |
| 截面, 剖视, cross-section | [09](references/templates/09-cross-section.json) | 截面/剖视图 |
| 中心辐射, hub spoke, 思维导图 | [10](references/templates/10-hub-spoke.json) | 中心辐射图 |
| 层级树, 分类树, taxonomy | [11](references/templates/11-hierarchical-tree.json) | 层级树/分类树 |
| 循环, cycle, 水循环 | [12](references/templates/12-cyclic-flow.json) | 循环流程图 |
| 多子图, multi-panel, figure 1 | [13](references/templates/13-multi-panel-figure.json) | 多子图组合 |
| 质粒, plasmid, 载体 | [14](references/templates/14-plasmid-map.json) | 质粒图/分子结构图 |
| 机械, 装置, 爆炸图 | [15](references/templates/15-machine-mechanism.json) | 机械/工程示意图 |
| 物理, 力学, 电路, schematic | [16](references/templates/16-physics-schematic.json) | 物理原理示意图 |
| 化学, 反应, 分子, synthesis | [17](references/templates/17-chemistry-structure.json) | 化学结构/反应机理 |
| 数学, 几何, 函数, math | [18](references/templates/18-math-concept.json) | 数学概念可视化 |
| 图文摘要, graphical abstract | [19](references/templates/19-graphical-abstract.json) | 论文图文摘要 |
| 实验室安全, lab safety | [20](references/templates/20-lab-safety.json) | 实验室安全/操作规范 |
| 教学海报, classroom poster | [21](references/templates/21-educational-poster.json) | 教学海报 |
| 步骤, step by step, protocol | [22](references/templates/22-step-by-step.json) | 步骤说明图 |
| 架构图, 神经网络, architecture | [23](references/templates/23-architecture-diagram.json) | 系统/算法架构图 |
| 双语, 中英对照, bilingual | [24](references/templates/24-bilingual-diagram.json) | 中英双语通用图 |

## 推荐尺寸

| 用途 | 比例 | 分辨率 |
|---|---|---|
| 期刊单栏图 | 4:3 | 2K |
| 期刊双栏图 | 16:9 | 2K |
| 垂直机制图（物理原理/层级树） | 3:4 | 2K |
| 学术海报（A0/A1） | 2:3 | 2K |
| PPT/幻灯片插图 | 16:9 | 2K |
| 正方形示意图 | 1:1 | 2K |
| 长流程横幅 | 21:9 | 2K |

## STEM Prompt 铁律（10 条）

1. **颜色用 hex 码**（`#10b981`、`#ef4444`、`#3b82f6`）
2. **方向显式声明**（`top-to-bottom`、`left-to-right`、`clockwise`）
3. **字体明确指定**（中文 SimHei/Microsoft YaHei；英文 Arial/Helvetica）
4. **术语标准化**（使用标准物理量、工程术语、数学符号和 LaTeX 公式）
5. **分辨率和比例**（期刊图 4K，PPT 2K）
6. **否定清单**（禁止虚构数据/认证/相互作用）
7. **标注规范**（激活实线、抑制虚线 T 型、磷酸化红圈 P）
8. **中英混排**（`线粒体 (Mitochondria)`）
9. **多子图编号**（A/B/C/D 加粗左上角）
10. **期刊合规**（禁止 AI 生成真实实验数据图）

详见 [SKILL.md](SKILL.md)。

## 使用示例

### 示例 1：生成一张物理原理图

**用户输入**：
> 帮我做一张阿基米德原理示意图，教材风格，垂直方向。

**Agent 响应**：
1. 匹配模板 `16-physics-schematic.json`，变体 `textbook`
2. 套用物理学科提示
3. 应用铁律 + 9 段 Prompt 结构
4. 输出视觉简报 + 完整 Prompt
5. 用户确认后调用：
   ```bash
   python scripts/generate_image.py --prompt-file ./prompt.txt --size 3:4 --resolution 2k
   ```

### 示例 2：生成整套论文 Figure

**用户输入**：
> 论文有 6 个子图（Figure 1A-F），需要做一套风格统一的期刊图。

**Agent 响应**：
1. 匹配 `13-multi-panel-figure.json` 或分别匹配各子图模板
2. **强制应用 Campaign Style Lock**（统一色板、字体、线宽、标注框）
3. 为每个子图分配不同角度/景别避免重复
4. 批量生图，确保风格一致

## 学术诚信

✅ **允许**：概念示意图、机制图、流程图、架构图、教学插图、海报

❌ **禁止**（AI 不能做的事）：
- 生成真实实验数据的统计图（散点/柱状/线图）→ 用 GraphPad/Origin/Python matplotlib
- 虚构实验数据、测量结果、工程认证或标准符合性

## 与 ecom-details-image 的关系

- **复用**：`scripts/generate_image.py`（统一 OpenAI/apimart 接口）
- **扩展**：物理/工程/数学场景模板、学术诚信规则、Campaign Style Lock
- **差异**：比电商图更严格（术语准确、方向正确、期刊合规、不可虚构）

## License

参考父项目https://github.com/liangdabiao/stem-illustration-skill。
无限进步！
感谢佬友 ： https://linux.do


## 文件 SKILL.md

---
name: interactive-illustration
description: 覆盖生物、医学、化学、物理、工程、数学的科学视觉学习 Skill；先判断用户需要专业精细图还是交互学习图，再生成概念图、精确图或可操作的交互式学习页面。
metadata:
  version: 1.0.0
---

# interactive-illustration

面向生物、医学、化学、物理、工程、数学的科学视觉学习 Skill。它既生成**科研示意图、教学插图、技术架构图**，也生成围绕理解目标设计的**交互式学习页面**。用户可以通过学科、模板和学习目标限定范围。

本 Skill 有两个输出模式：

- **专业精细型**：准确、规范、可用于讲义、论文、竞赛解析或正式展示的静态图。优先使用代码绘制严格几何、坐标、函数、数据和标准符号；概念性部分才使用 AI 生图。
- **交互学习型**：让用户通过拖动、旋转、缩放、切换图层、播放动画或分步操作理解变量关系的 HTML/SVG/Canvas/WebGL 页面。它不是一张普通图片，不能把交互需求直接翻译成文生图 Prompt。

## 首要路由：先判断输出模式

生图或制图前，先判断用户的主要目标是“表达成果”还是“理解概念”。详细判型规则见 [references/mode-selection.md](references/mode-selection.md)。

### 自动选择

- 出现“论文、讲义、出版级、矢量、打印、竞赛解析配图、精确比例、标准符号”等信号时，选择**专业精细型**。
- 出现“理解、直观、动态、拖动、旋转、调参、观察变化、为什么、做成动画”等信号时，选择**交互学习型**。
- 三维坐标、坐标变换、局部基向量、场、运动演化、参数耦合等内容，若用户没有明确要求静态成图，优先考虑**交互学习型**。

### 必要时询问

当用户只说“生一张图”且两种模式都合理时，只问一个问题：

> 这次更需要可直接用于讲义/论文的专业精细图，还是用于理解概念、可以拖动和调参的交互学习图？

不要为了补齐所有可选项而连续追问。只有当缺失的信息会改变输出模式、科学约定或最终文件格式时才询问；其余参数采用合理默认值并明确说明。

### 路由后的声明

开始生成前，用一句话告诉用户已选择的模式和原因。例如：

> 这个概念的关键在于观察参数变化，我会生成交互学习型三维页面。

## 交互学习型工作流

选择交互学习型后，读取 [references/interactive-learning.md](references/interactive-learning.md) 和 [references/interactive-models.md](references/interactive-models.md) 中与学科相关的条目，并按以下顺序工作：

1. 提取一个明确的学习目标，而不是只罗列要显示的对象。
2. 区分可控变量、派生量和应保持不变的量。
3. 选择最小而有教学价值的交互：滑块、拖拽、视角控制、图层开关、动画或分步按钮。
4. 先建立数学/物理状态模型，再生成页面，不让视觉效果反过来决定公式。
5. 输出可运行的 HTML 或项目目录，并同时提供静态预览、操作说明和关键结论。
6. 测试控件、边界值、公式联动、重置功能和常见误解提示。

对于球坐标、柱坐标、曲线坐标、三维向量场等主题，优先使用可旋转的三维视图；对于斜抛、简谐振动、碰撞、电场、磁场、波叠加、驻波、双缝干涉、守恒律、量纲分析和极限情况，分别采用模型目录中的控制量、不变量、视图和校验条件。截图中的球坐标示例可作为交互体验参考，但不能作为科学约定的来源。

交互页面应优先由代码生成。可使用随 Skill 提供的 [scripts/scaffold_interactive.py](scripts/scaffold_interactive.py) 作为起点；它内置球坐标基向量示例，可用于验证三维交互管线。AI 生图脚本只负责静态概念图或页面封面，不负责实现交互逻辑。

## 何时使用

- 用户要生成科研示意图、机制图、流程图、流程海报、教学插图、学术图、技术架构图
- 用户提供主题/论文/概念/数据，期望出一张图（不限于"科研"，包括科普、教学、产品技术图）
- 学科关键词触发：细胞、信号通路、质粒、化学反应、分子结构、力学、电路、光学、电磁、热力学、机械、装置、爆炸图、工程图、系统架构、算法、几何、函数、数学概念、信息图、海报、截面、流程图

## 不适用

- 真实实验数据图（散点/柱状/线图，学术诚信）→ 拒绝并提示使用 GraphPad/Origin/Python matplotlib
- 照片级写实（人像/风景/产品摄影）→ 用通用生图 skill
- 创意插画/卡通角色 → 用通用生图 skill

## 生图配置

复用 [scripts/generate_image.py](scripts/generate_image.py)，自动兼容 OpenAI 同步 API 和 apimart.ai 异步 API。

`.env` 字段：

| 字段 | 必填 | 说明 |
|---|---|---|
| `IMG_BASE_URL` | 是 | API 根地址 |
| `IMG_MODEL` | 是 | 图片模型 |
| `IMG_API_KEY` | 是 | API key |

模板：[.env.example](.env.example)（含 STEM 推荐参数说明）。

## 推荐尺寸

| 用途 | 比例 | 分辨率 |
|---|---|---|
| 期刊单栏图 | 4:3 | 2K |
| 期刊双栏图 | 16:9 | 2K |
| 垂直机制图（物理原理/层级树） | 3:4 | 2K |
| 学术海报（A0/A1） | 2:3 | 2K |
| PPT/幻灯片插图 | 16:9 | 2K |
| 正方形示意图 | 1:1 | 2K |
| 长流程横幅 | 21:9 | 2K |

## 专业精细型流程（Brief / Prompt 模式）

1. **收集最小输入**：学科、图表类型、目标受众、关键术语清单、尺寸/比例、语言
2. **匹配场景模板**（仅使用保留的模板，见 [references/templates/](references/templates)）
3. **选择变体**：`academic` / `textbook` / `infographic` / `3d-render`
4. **套用学科提示**（模板的 `category_tips`）
5. **应用 STEM Prompt 铁律**（见下）
6. **组装 9 段 Prompt**（见下）
7. **应用 Campaign Style Lock**（多图任务）
8. **自检**（见 QA 清单）
9. **输出视觉简报**（中文，含 Prompt + 调用方式）
10. **若用户明确要求生图** → 调用 `scripts/generate_image.py`

交互学习型不沿用这套静态 Prompt 流程，而是遵循上面的交互工作流。

## 最小输入

至少包含：

- **学科**：物理/工程/数学
- **图表类型**：模板 ID（如 `physics-schematic`、`machine-mechanism`、`math-concept`）
- **目标受众**：K-12 / 高中 / 大学 / 研究生 / 同行研究者 / 公众科普
- **关键术语清单**：物理量、工程术语、零件号、公式等需准确呈现的术语
- **尺寸/比例**：见上表
- **语言**：中文 / 英文 / 双语

## 通用 Prompt 结构（9 段）

1. **Type**：图表类型（scientific mechanism diagram / data infographic / system architecture / ...）
2. **Subject**：主题（具体内容）
3. **Layout**：布局（top-to-bottom / left-to-right / 2x2 grid / radial / ...）
4. **Style**：风格（flat vector / textbook illustration / 3D render / infographic / ...）
5. **Color scheme**：用 hex 码（`#2563eb`、`#10b981` 等）
6. **Labels**：字体（中文 SimHei/Microsoft YaHei；英文 Arial/Helvetica；公式用 LaTeX；物理量和工程单位规范）
7. **Quality**：4K / publication-ready / journal style
8. **Constraints**：禁止虚构、禁止错误方向、必须包含的关键元素
9. **Background**：white / dark / gradient / transparent

## STEM Prompt 铁律（10 条，**强制**）

1. **颜色用 hex 码**：矢量/力 `#ef4444`、速度/位移 `#3b82f6`、场/能量流 `#10b981`、数据主色 `#2563eb`
2. **方向显式声明**：`top-to-bottom vertical cascade`、`left-to-right horizontal flow`、`clockwise` / `counter-clockwise`
3. **字体明确指定**：中文 SimHei/Microsoft YaHei 粗体；英文 Arial/Helvetica
4. **术语标准化**：使用标准物理量、工程术语、数学符号和 LaTeX 公式；不要臆造术语或参数
5. **分辨率和比例**：期刊图 4K，PPT 2K；单栏 4:3，双栏 16:9，垂直机制图 3:4
6. **否定清单**：禁止虚构数据/认证/尺寸/参数/连接关系；禁止箭头方向错误
7. **标注规范**：矢量带方向和单位；电路使用 IEC/ANSI 符号；工程尺寸带单位；公式使用 LaTeX
8. **中英混排**：中文为主时英文括注；中英字号协调
9. **多子图编号**：A/B/C/D 加粗置于子图左上角
10. **期刊合规**：禁止用 AI 生成真实实验数据图（scatter/bar/line），仅限概念示意图

## 两阶段工作流（复杂任务）

### Architect 阶段（LLM 分析）

输出 **[VISUAL SCHEMA]**：

```
LAYOUT: 2x2 grid of 4 panels
PANEL A: [Top-left] Experimental workflow (5 steps)
PANEL B: [Top-right] Representative physics or engineering schematic
PANEL C: [Bottom-left] Quantification bar chart
PANEL D: [Bottom-right] Mechanism diagram
COLOR: Blue #2563eb primary, gray #6b7280 secondary
PANEL LABELS: A/B/C/D bold top-left
SHARED: Scale bar, statistical markers */**
```

### Renderer 阶段（LLM 转 Prompt）

将 Schema 翻译为 9 段 Prompt，套用铁律，生成最终生图 Prompt。

## ⚠️ 能力边界（重要：何时不要用本 Skill）

AI 生图模型（gpt-image-2、DALL-E、Midjourney、Stable Diffusion 等）是**模式匹配器**，不是几何引擎。它们能渲染"看起来对"的图，但**无法保证**：

- 平行线真正平行、直角真正是 90°
- 三角形真正全等（边长精确相等）
- 几何关系与公式严格对应
- 公式/文字无拼写错误

### ✅ AI 生图**适合**（推荐用本 Skill）

- 概念示意图、流程图、信息图
- 物理原理、工程结构和数学概念的概念示意图（几何不必精确）
- 机械结构剖视图（视觉清晰即可）
- 海报、封面、教学插图
- 风格化、装饰性、教学性图表

### ❌ AI 生图**不适合**（必须用代码生成或人工绘制）

- **数学严格证明图**（如勾股定理、欧几里得几何证明、向量/矩阵图）
- **坐标图、函数图像**（坐标系、抛物线、正弦曲线等）
- **精确构造图**（如圆的内接多边形、角平分线、相似三角形证明）
- **电路图、工程制图（精确符号、尺寸、公差或连接关系）**——除非只是教学示意图
- **数据图（柱状图/折线图/热图）**——必须用 matplotlib/plotly 等代码工具
- **交互式学习页面**——必须由 HTML/SVG/Canvas/WebGL 或其他可运行代码实现，不能只生成一张静态图片

### 🛠️ 严格几何/数学图的正确做法

使用 [scripts/generate_geometry.py](scripts/generate_geometry.py)（基于 matplotlib），或：
- **matplotlib** + `matplotlib.patches`：精确绘制多边形、角度标记、面积填充
- **TikZ / pgfplots**（LaTeX）：学术论文级数学图
- **GeoGebra**：交互式几何
- **Asymptote**：精确几何编程
- **desmos.com / Wolfram Alpha**：函数图像

**判断原则**：如果图需要"几何正确性"才能传达信息（数学证明、精确数据图、坐标变换）→ 必须用代码生成。如果图只需要"视觉传达"概念（流程、机制、结构）→ 可以用 AI 生图。

## 场景模板系统

保留的模板位于 [references/templates/](references/templates)，按场景编号：

| # | 模板 ID | 场景 |
|---|---|---|
| 01 | signaling-pathway | 信号通路/分子机制图 |
| 02 | experimental-workflow | 实验流程/技术路线图 |
| 03 | cell-structure | 细胞/解剖结构图 |
| 04 | data-infographic | 数据可视化信息图 |
| 05 | academic-poster | 双语学术海报 |
| 06 | concept-infographic | 概念教育信息图 |
| 07 | timeline | 科学史时间线 |
| 08 | comparison-matrix | 对比矩阵 |
| 09 | cross-section | 截面/剖视图 |
| 10 | hub-spoke | 中心辐射图 |
| 11 | hierarchical-tree | 层级树/分类树 |
| 12 | cyclic-flow | 循环流程图 |
| 13 | multi-panel-figure | 多子图组合（Figure 1A-F） |
| 14 | plasmid-map | 质粒图/分子结构图 |
| 15 | machine-mechanism | 机械/工程示意图 |
| 16 | physics-schematic | 物理原理示意图 |
| 17 | chemistry-structure | 化学结构/反应机理 |
| 18 | math-concept | 数学概念可视化 |
| 19 | graphical-abstract | 论文图文摘要 |
| 20 | lab-safety | 实验室安全/操作规范 |
| 21 | educational-poster | 教学海报（K-12/高校） |
| 22 | step-by-step | 步骤说明图 |
| 23 | architecture-diagram | 系统/算法架构图 |
| 24 | bilingual-diagram | 中英双语通用图 |

每模板字段：`id` / `name` / `keywords` / `trigger_phrases` / `prompt_template` / `defaults` / `variants` / `category_tips` / `examples` / `accuracy_tips` / `supports_image_reference`。

`references/interactive-models.md` 是交互学习型模型目录，不替代上述静态场景模板；交互任务应优先读取对应学科条目。

`20-lab-safety.json` 仅保留 `ppe` 与 `emergency` 变体。生物安全等级（BSL）和化学品安全（GHS/chemical compatibility）不属于当前安全模板变体；涉及这些内容时，应使用用户提供的机构 SOP 或专业安全资料，不凭空生成规范。

## 学科适配

| 学科 | 推荐模板 | 关键提示 |
|---|---|---|
| 生物/医学 | 01/03/09/19 | 对照权威数据库和术语；不虚构结构、相互作用或临床结论 |
| 化学 | 14/17 | 结构式、立体化学、反应条件和 IUPAC 命名必须核对；严格结构图优先代码绘制 |
| 物理 | 09/15/16 | 矢量箭头带单位；右手定则；P-V 图 |
| 工程 | 13/15/23 | 爆炸视图带零件号；ISO 标准；公差标注 |
| 数学/算法 | 11/18/23 | LaTeX 排版；算法流程；网络拓扑 |

## Campaign Style Lock（多图任务，**强制**）

整套论文 Figure、系列教学卡、教材插图集必须锁定：

- **固定色板**：2-3 主色 + 1 强调色，全部 hex
- **统一字体**：中文一种 + 英文一种
- **统一箭头/线条**：线宽、颜色、端点一致
- **统一背景**：纯白 `#FFFFFF` 或浅灰 `#F8FAFC`
- **统一标注框**：圆角矩形、半透明白底
- **禁止漂移**：不因新图而改变主色、字体、线宽

## 多子图组合规则

- 标签 A/B/C/D 加粗置于子图左上角
- 子图间风格统一（字体/线宽/配色）
- 共享坐标轴和比例尺
- 统计标记一致（*/**/***对应 p<0.05/0.01/0.001）
- 化合物编号、分子量标记跨子图一致

## 期刊合规与学术诚信（**强制**）

### 允许（概念示意图）

- 物理原理、工程结构、数学概念、流程图和架构图
- 教学插图、概念信息图、海报
- 理论模型示意、工作原理图

### 禁止（学术不端）

- **用 AI 生成真实实验数据的统计图**：散点图、柱状图、线图、箱线图
- 虚构实验数据、测量结果、工程认证或标准符合性
- 虚构认证、评分、销量、评价（电商同理）

→ 如用户要求，**拒绝并提示使用 GraphPad/Origin/Python matplotlib/seaborn**。

## 直接生图规则

用户明确要求“生图/出图/render/生成”时，先完成模式路由：

1. 如果是交互学习型，生成可运行的交互页面；不要把它伪装成普通 PNG。需要静态封面时，再额外生成一张概览图。
2. 如果是专业精细型，继续使用下面的 AI 生图或代码绘图规则。

专业精细型的 AI 生图规则：

1. 用 `scripts/generate_image.py` 调用 API
2. 命令示例：
   ```bash
   # 从 Prompt 文件生图
   python scripts/generate_image.py --prompt-file ./prompt.txt --size 3:4 --resolution 2k

   # 从 stdin/字符串生图
   python scripts/generate_image.py --prompt "..." --size 16:9 --resolution 2k

   # 参考图生图（图生图）
   python scripts/generate_image.py --prompt "..." --image ./reference.png --size 1:1
   ```
3. 生图前只确认会实质影响结果的参数：学科、模板 ID、变体、尺寸和风格。若用户已经给出或上下文已经明确，不重复确认。

## 科学正确性校验

所有输出都必须读取并遵守 [references/scientific-validation.md](references/scientific-validation.md)。特别是坐标系、角度约定、向量方向、单位、符号和奇异点不能依赖生成模型猜测。

## QA 自检清单（**强制**）

- [ ] 术语、公式、单位和符号准确
- [ ] 方向/箭头、坐标轴和参考系正确
- [ ] 工程零件关系、剖切方向和尺寸标注清楚
- [ ] 颜色符合色盲友好标准（避免纯红绿对比）
- [ ] 中文字笔画准确（放大 200% 核对）
- [ ] 未虚构实验数据/认证/相互作用
- [ ] 多子图编号一致（A/B/C/D）
- [ ] 已应用物理/工程/数学 Prompt 规则
- [ ] 已匹配正确场景模板
- [ ] 多图任务已应用 Campaign Style Lock
- [ ] 已选择合适尺寸和分辨率
- [ ] 已套用学科 `category_tips`

## 常见翻车点与防护

| 翻车 | 防护 |
|---|---|
| 物理量/单位错误 | 明确符号、SI 单位、正负方向和参考系 |
| 箭头方向错误 | Prompt 显式声明 `top-to-bottom` / `left-to-right` |
| 工程结构虚构 | 明确哪些是概念示意；不要声称符合认证或标准 |
| 配色刺眼/不专业 | 强制 hex 码；色盲友好；主色不超过 3 个 |
| 中文字乱码/缺笔画 | 指定 SimHei/Microsoft YaHei；放大 200% 核对 |
| 数据图造假 | 强制使用真实数据工具；AI 仅限概念图 |
| 整套图风格漂移 | 强制 Campaign Style Lock |
| **模型把甲主题渲染成乙主题** | Prompt 头部加 `PURE PHYSICS/ENGINEERING/MATHEMATICS illustration ONLY`，并明确禁止无关学科元素 |
| **结构式/小字渲染模糊** | 异步模式用 `--resolution 4k`；prompt 要求 `bold high-contrast labels at 24pt+` |
| **🚨 AI 生图无法保证数学/几何精确性** | **几何证明图、坐标图、精确构造图必须用 [scripts/generate_geometry.py](scripts/generate_geometry.py) 或 matplotlib/TikZ/GeoGebra 等代码工具生成。AI 生图只能用于"看起来对即可"的概念图。这是 Skill 的最关键限制。** |

## 输出格式（中文）

向用户输出时使用以下结构：

```
**【视觉简报】**

**学科**：物理（力学原理）
**模板**：physics-schematic
**变体**：academic（Nature 期刊风格）
**尺寸/分辨率**：3:4 / 2K
**目标受众**：研究生

**核心元素**：
- 物体、受力、坐标轴和参考系
- 力/速度矢量及 SI 单位
- 关键公式和边界条件

**配色**：
- 力/矢量 #ef4444
- 速度/位移 #3b82f6
- 场/能量流 #10b981

**Prompt**（英文，可直接用于生图）：
[Scientific physics schematic diagram, ... 完整 Prompt]

**调用方式**（如需生图）：
python scripts/generate_image.py --prompt-file ./prompt.txt --size 3:4 --resolution 2k
```

## 与 ecom-details-image 的关系

本 Skill 复用了 ecom-details-image 的生图脚本（统一 OpenAI/apimart 接口），并将场景限定为物理、工程、数学，同时保留学术诚信和科学准确性要求。

