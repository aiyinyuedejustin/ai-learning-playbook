# Part C — 高星学习 Skills / 工具 + 大 Scope→章节 + 魔改适配

> 调研时间：2026-10-11（Asia/Tokyo / JST）  
> 星数来源：GitHub API 当日拉取（会随时间变；以链接为准）  
> 范围：agent skills、tutor、Anki、课程拆章 workflow；不限 skill，但本篇以**可安装/可 fork 的工具链**为主  
> 不做 Cloud Agent

---

## 0) 先钉死：同叫 teach，过程 / 产物 / 目标可以完全不同

社区里至少有 **三套** 都叫「teach / tutor / learn」，混用会踩坑。

| 维度 | **Matt `/teach`** | **pstack `/teach`** | **Tutor 类 `/learn`（如 claude-tutor / agent-tutor-skill）** |
|------|-------------------|---------------------|--------------------------------------------------------------|
| **目标** | 跨多会话学会一门主题（语言/框架/瑜伽…） | 真正听懂仓库里一段代码/子系统 | 形成「可测可复习」的掌握度，对抗遗忘曲线 |
| **过程** | 钉 MISSION → 搜高可信资料 → 最近发展区出短课 → 交互练习 | 调 `/how`+`/why` 挖证据 → 白话讲解（可配图） | 计划 → 讲 → quiz → SM-2/FSRS 排复习 |
| **状态** | **有状态**：当前目录=课程仓库 | **无课程仓库**；会话内讲解 | **有状态**：learner profile / `~/.learn/` / dashboard |
| **典型产物** | `MISSION.md`、`RESOURCES.md`、`lessons/*.html`、`learning-records/`、`reference/` | 口语讲解 + mermaid/白板图 | 学习计划、quiz、复习日历、进度档案 |
| **资料来源** | 强制外搜；不信参数记忆 | 代码 + git/issue/文档等证据 | 可 web research，或指向 PDF/URL/代码 |
| **测验** | HTML 课里可有 quiz widget；强调 storage strength | **禁止测验腔**（理解优先） | 核心：自适应 quiz + 间隔复习 |
| **何时用** | 「我要系统学 X 几周」 | 「Harbor 这段调度怎么跑」 | 「学完还要记得住」 |
| **星数/入口** | 整仓 **~285k★** [mattpocock/skills](https://github.com/mattpocock/skills) | 镜像仓 **~1.6k★** [backnotprop/pstack](https://github.com/backnotprop/pstack)（Cursor 插件市场另装） | 见下表各仓 |

**一句话**：Matt = 课程工地；pstack = 代码费曼；Tutor = 记忆闭环。名字撞车，流水线正交——可以串，不要互相替代。

---

## 1) 高星 / 高可见学习相关工具（带链接与星数）

按「你要它产出什么」分六桶。星数旁标 `★`；未上架或星很少的仍列，因**流水线设计**可魔改。

### A. 长期教学工作区（目录=课程）

| 项目 | ★ | 过程摘要 | 产物 | 链接 |
|------|---|----------|------|------|
| **mattpocock/skills · teach** | **285571** | MISSION→资料→HTML 短课；reuse-first 组件库 | 课程目录全套 | [repo](https://github.com/mattpocock/skills) · [SKILL](https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/teach/SKILL.md) |
| **koganei/learn-anything-skill** | 3 | 自动调研 → Foundations/Intermediate/Advanced/Use-case 章节路径 | 分级学习路径 + 分块授课 | [repo](https://github.com/koganei/learn-anything-skill) |

同仓协作向（不算「教课」，但常和 teach 连用）：`grill-me`、`research`、`handoff`、`wait-what`。

### B. 代码理解（Justin 已装 pstack）

| 项目 | ★ | 过程摘要 | 产物 | 链接 |
|------|---|----------|------|------|
| **backnotprop/pstack** | **1564** | `/how` 架构、`/why` 证据、`/teach` 合成、`/bro` 白话 | 讲解 + 图；无课程仓 | [repo](https://github.com/backnotprop/pstack) · [teach](https://www.skills.sh/backnotprop/pstack/teach) |
| sbkriz/feynman-tutor | 0 | **你讲、AI 追问缺口** | learner notes | [repo](https://github.com/sbkriz/feynman-tutor) |

### C. 完整辅导闭环（Tutor）

| 项目 | ★ | 过程摘要 | 产物 | 链接 |
|------|---|----------|------|------|
| **kirilxd/claude-tutor** | **137** | `/learn` 计划 → 教 → `/quiz` → SM-2 → dashboard | plan、quiz、复习、Web 面板 | [repo](https://github.com/kirilxd/claude-tutor) |
| **mordor-forge/study-skill** | **46** | 交互学习 + FSRS-6 | 学习会话 + 复习调度 | [repo](https://github.com/mordor-forge/study-skill) |
| **Bhala-Srinivash/agent-tutor-skill** | **11** | Explain→Example→Check→Practice；FSRS；源材料教学 | `~/.learn/` 档案 + 复习 | [repo](https://github.com/Bhala-Srinivash/agent-tutor-skill) |
| shauigewhite/learning-tutor | 0 | 五模式 + 前测/后测 + 三种教法 | learner profile | [repo](https://github.com/shauigewhite/learning-tutor) |
| Mohamed-El-Sharqawy/agent-tutor | 3 | 辅导 + quiz + 1–90 天阶梯；写 Obsidian | 复习队列 | [repo](https://github.com/Mohamed-El-Sharqawy/agent-tutor) |

### D. Anki / 间隔重复制卡

| 项目 | ★ | 过程摘要 | 产物 | 链接 |
|------|---|----------|------|------|
| **doasfrancisco/anki-skill** | **57** | 编码中提议原子卡 → 你批准 → AnkiConnect 写入 | Anki 卡 | [repo](https://github.com/doasfrancisco/anki-skill) |
| **HumphreySun98/Smart-Study-Agent** | **58** | 概念图 + FSRS + RL 选题 + Anki 导出 | quiz 库、`.apkg`、SQLite | [repo](https://github.com/HumphreySun98/Smart-Study-Agent) |
| guepardlover77/learn-skill | 2 | 材料→计划 + genanki `.apkg` + Obsidian | `.apkg`、md、SM-2 表 | [repo](https://github.com/guepardlover77/learn-skill) |
| Teach Anki（hengadev 等目录页） | — | 课中多类型卡，审完再写 Anki | 卡 + 账本 | [mcpmarket](https://mcpmarket.com/tools/skills/anki-spaced-repetition-tutor) |
| mkrech/anki-course-tutor-mcp | 1 | MCP 会话 + Anki 调度 | 会话/统计 | [repo](https://github.com/mkrech/anki-course-tutor-mcp-server) |

### E. 知识吸收 / Wiki 化

| 项目 | ★ | 过程摘要 | 产物 | 链接 |
|------|---|----------|------|------|
| **YuJunZhiXue/StudyAnalysis-Skills（Knowledge Absorber）** | **629** | 深读链接/文档 → Markdown+HTML「知识晶体」+ 导师模式 | 结构化笔记 + 侧栏测验 | [repo](https://github.com/YuJunZhiXue/StudyAnalysis-Skills) |
| wwwzhouhui/skills_collection（含 knowledge-absorber 变体） | **282** | Claude skills 合集 | 多 skill | [repo](https://github.com/wwwzhouhui/skills_collection) |
| **huifer/Claude-Code-KnowCraft** | **75** | 本地知识库 + SM-2 + 费曼 Agent | 笔记/测验/本地库 | [repo](https://github.com/huifer/Claude-Code-KnowCraft) · [linux.do](https://linux.do/t/topic/1403453) |

### F. AI 协作 / 「共赢」向（对齐、对抗、Agent 自记忆）

| 项目 | ★ | 过程摘要 | 产物 | 链接 |
|------|---|----------|------|------|
| Matt `grill-me`（同仓） | 见 A | AI 追问到设计树闭合 | 澄清后的计划 | [skills](https://github.com/mattpocock/skills) |
| pstack `interrogate` / `arena` / `swarm` | 见 B | 对抗评审 / 多方案竞赛 / 并行汇总 | 盲点报告、嫁接方案 | [pstack](https://github.com/backnotprop/pstack) |
| **cheanus/SRSA** | **22** | **给 Agent 自己**做 FSRS 记忆卡（不是给你背单词） | Agent 记忆复习日程 | [repo](https://github.com/cheanus/SRSA) · [linux.do](https://linux.do/t/topic/1803656) |

### G. 「大课 / 章节型」成品课（偏内容，非 skill，但可抄结构）

| 项目 | ★ | 结构 | 链接 |
|------|---|------|------|
| **microsoft/ai-agents-for-beginners** | **76903** | 18 课：每课 README + 视频 + 代码 | [repo](https://github.com/microsoft/AI-AGENTS-FOR-BEGINNERS) |
| **Haozhe-Xing/agent_learning** | **579** | Agent 路线图分章（RAG/工具/多 Agent/评测…） | [repo](https://github.com/Haozhe-Xing/agent_learning) |
| **minicoohei/ai-agent-camp** | **347** | 几十模块课程 + lessons manifest | [repo](https://github.com/minicoohei/ai-agent-camp) |

### linux.do 社区信号（非星数，但实装口碑）

| 帖 | 要点 | 链接 |
|----|------|------|
| 学习 skill 征集 | 常推 Matt teach + Knowledge Absorber | https://linux.do/t/topic/2761043 |
| grill-me 心得 | Matt 系列使用经验 | https://linux.do/t/topic/2952622 |
| Knowledge Absorber 填坑 | 加导师模式防「看完记不住」 | https://linux.do/t/topic/1770345 |
| AI Skills 快速获取知识 | 自改 skill 加速吸收 | https://linux.do/t/topic/1494565 |

---

## 2) 大 Scope → 章节：工具链与流水线

目标形态统一为：

```
大主题 / 材料堆
    → 能力图 / 大纲（observable outcomes）
    → 模块 / 章节（依赖序 + 前置诊断）
    → 课节（attempt → 原理 → 练习）
    → 检查点 / quiz
    → 间隔复习日程
```

### 2.1 专门做这件事的 skill（优先抄）

#### [lowwwbank/anything-to-course](https://github.com/lowwwbank/anything-to-course) · **22★**（设计最完整）

| 阶段 | 做什么 | 产物文件 |
|------|--------|----------|
| Capability map | 把材料压成可观察能力、缺口、前置 | （内嵌进 syllabus） |
| Course build | 按模块拆课；答案物理隔离 | `00-syllabus.md`、`modules/NN-*/`、`answers/` |
| Study mode | 先做后看答案；校准；tutor | `review-schedule.md`（+1d/+7d/+30d） |

单课标准流（学习科学硬编码）：attempt → principle → worked example → contrast → practice（支持渐隐）→ checkpoint。

**适合魔改点**：`references/course-blueprint.md`、`practice-design.md`、`study-mode.md` —— fork 后改模板即可适配 Harbor / 评测域。

#### Matt `/teach`（大纲隐式、章节=HTML lesson）

不强制一次吐出整本 syllabus，而是：

1. `MISSION.md` 钉「为什么学」  
2. 按最近发展区每次出 **一个** `lessons/000N-….html`  
3. `learning-records/` 像 ADR，驱动下一章选什么  

**大 scope 用法**：先自己（或用 anything-to-course）写出模块地图，再让 Matt teach **只负责某一章**，避免一次生成 40 课幻觉课。

#### Tutor 系（claude-tutor / agent-tutor-skill / learn-anything）

- `claude-tutor`：`/learn <topic>` → 带资源的计划（章节感）→ `/quiz` → `/review`  
- `agent-tutor-skill`：概念级 mastery + FSRS；可绑 PDF/URL/代码当「教材」  
- `learn-anything-skill`：显式 **01–05 Foundations / 06–09 Intermediate / 10–11 Advanced / 12–17 Use-case** 编号路径  

### 2.2 推荐组合流水线（个人可落地）

| 步骤 | 工具 | 产出 | 必备? |
|------|------|------|--------|
| 1. 钉目标与成功标准 | Matt `grill-me` 或手写 MISSION | 「学完能做什么」清单 | **必备** |
| 2. 大 scope → 大纲/模块 | **anything-to-course** 或手写 syllabus | `00-syllabus.md` + 模块序 | **必备** |
| 3. 按章授课 / 写课 | Matt teach（HTML）或 anything-to-course lessons | 课节文件 | **必备** |
| 4. 读代码子系统时讲清 | **pstack** how/why/teach | 心智模型（不进课程仓也可） | 代码向必备 |
| 5. 吸收长文/论文 | Knowledge Absorber | 知识晶体 | 可选→材料多时必备 |
| 6. 对抗「以为懂了」 | quiz（tutor）或 pstack `interrogate` | 测验 / 盲点报告 | **必备（防流畅幻觉）** |
| 7. 对抗遗忘 | FSRS/SM-2 tutor 或 Anki skill | 复习队列 / `.apkg` | **必备（跨周）** |
| 8. 沉淀进个人库 | KnowCraft / Obsidian / 自建 wiki | 可检索笔记 | 可选 |
| 9. Agent 自己记规矩 | SRSA / pstack reflect | Agent 记忆卡 / 改 skill | 可选 |

**不建议**：第一天用 AI 一口气生成 8 小时课然后不复习——流畅感 ≠ storage strength（Matt teach / anything-to-course / agent-tutor 都反复强调这一点）。

### 2.3 章节模板（可直接贴进你的课程仓）

```text
my-course/
├── MISSION.md                 # 为什么学、成功标准（2–5 条可观察行为）
├── 00-syllabus.md             # 模块地图、依赖、估计周次
├── modules/
│   ├── 01-foundations/
│   │   ├── 00-overview.md     # 产出、前置、入口诊断题
│   │   ├── 01-lesson-….md|html
│   │   └── 99-checkpoint.md   # 混合练习，不剧透方法名
│   └── 02-…
├── answers/                   # 与练习物理隔离
├── review-schedule.md         # +1d / +7d / +30d 或 FSRS 导出
├── anki/ 或 cards.md          # 可选制卡账本
└── learning-records/          # 学完一章写一条「非显然洞察」
```

---

## 3) 如何魔改 skill / workflow 适配个人（Harbor / 评测 / 未知领域）

### 3.1 魔改原则

1. **复制一份再改**（`npx skills add` 进项目，或 git fork），不要直接改市场只读包。  
2. **只改三处**：触发描述（description）、产物路径约定、领域词表（GLOSSARY）。  
3. **保留学习科学骨架**（先做后看、间隔、检索）；只换领域例子。  
4. **一门课一个目录**；pstack 继续装在全局，避免和 Matt teach 状态搅在一起。

### 3.2 按场景改什么

| 你的场景 | 改谁 | 怎么改 |
|----------|------|--------|
| 系统学 Meta-Harness / Harbor | Matt teach + anything-to-course | MISSION 写成「能独立复现某 bench 流程」；syllabus 按「概念→环境→跑通→改 skill→评测」分模块 |
| 读陌生代码 | pstack（已装） | 几乎不用改；大子系统用 `/teach`，细节用 `/how` |
| 论文/长文变可复习 | Knowledge Absorber → Anki | Absorber 出晶体后，用 anki-skill / learn-skill 抽原子卡 |
| 方案对齐 | grill-me / interrogate | grill 先钉范围；interrogate 找盲点；再交给 Multica/Orca 执行 |
| 防三分钟热度 | tutor FSRS + review-schedule | 把「每天新课上限」写进 NOTES（如每天 1 课 + 复习旧卡） |

### 3.3 最小魔改清单（复制 Matt teach 时）

- `MISSION-FORMAT`：加你的成功标准字段（例如「能讲清 Builder/Target 分工」「能在 Harbor 上跑通一条」）  
- `NOTES.md`：固定偏好——每天最长短课数、是否必须外链引用、中文/英文课  
- `assets/`：复用 quiz widget；换成你领域的示意图组件  
- **不要删** storage strength / ZPD / 引用要求——这是它比「让 AI 讲课」强的地方  

### 3.4 最小魔改清单（复制 anything-to-course 时）

- `course-blueprint.md`：模块命名改成你的域（如 `01-harness-concepts`）  
- `practice-design.md`：练习题型改成「改一段 adapter」「解释一份 episode JSON」  
- `study-mode.md`：tutor 会话时长改成 25–40 分钟番茄，强制结束去复习  

---

## 4) 必备 vs 可选组件（组装个人学习 OS）

### 必备（缺一容易「学了等于没学」）

| # | 组件 | 作用 | 推荐起点 |
|---|------|------|----------|
| 1 | **目标 / MISSION** | 防止无范围刷课 | 手写或 Matt grill→MISSION |
| 2 | **大纲 / 章节图** | 大 scope 可进度 | anything-to-course 或手写 syllabus |
| 3 | **短课单元** | 工作记忆友好 | Matt HTML lesson 或 ATC modules |
| 4 | **检索练习（quiz / 先做后看）** | 打流畅幻觉 | ATC checkpoint / claude-tutor quiz |
| 5 | **间隔复习** | 对抗衰减 | FSRS tutor 或 Anki |
| 6 | **学习记录** | 跨会话接着学 | `learning-records/` 或 learner profile |

### 强烈推荐（领域相关）

| 组件 | 何时要 | 推荐 |
|------|--------|------|
| 代码费曼层 | 主题含仓库/bench | **pstack**（已装） |
| 外源深读 | 论文、长文档多 | Knowledge Absorber（629★） |
| 人对齐 | 大 scope 易跑偏 | grill-me |

### 可选

| 组件 | 说明 |
|------|------|
| Web dashboard | claude-tutor 有；非必须 |
| Obsidian/Wiki 沉淀 | KnowCraft / 自建；卡片够用可先不做 |
| Anki 桌面 + AnkiConnect | 要出门背、多端同步时再上 |
| SRSA（Agent 自复习） | 优化 agent 记忆，不是你的主线 |
| 多 Agent 讨论（arena/interrogate） | 方案评审用；日常学课不必每次开 |
| 成品公开课（MS agents beginners 等） | 当「别人写好的章节」参考，不替代你的 MISSION |

### 反模式（绕开）

- 只装一个叫 teach 的 skill，期望它既讲代码又管 Anki 又拆大纲  
- 第一天生成整本课、零复习  
- 在日常写代码的 git 根目录跑 Matt teach（课程文件会污染仓库；单独开学习目录）  
- 用 Cloud Agent 批量「帮你学」——本调研明确不走这条；学习闭环需要**你本人做检索练习**

---

## 5) 按 Justin 现状的装配建议（短）

已有：**pstack**（代码理解层齐全）。

建议补齐顺序：

1. **必备大纲层**：fork / 安装 [anything-to-course](https://github.com/lowwwbank/anything-to-course)（22★，模板最好改）  
2. **必备课程层**：装 Matt [`teach`](https://github.com/mattpocock/skills)（285k★ 仓；单独学习目录）  
3. **必备记忆层**：二选一——[claude-tutor](https://github.com/kirilxd/claude-tutor)（137★，闭环完整）或 [agent-tutor-skill](https://github.com/Bhala-Srinivash/agent-tutor-skill)（FSRS 更现代）  
4. **材料吸收（可选但 Harbor 论文多时很值）**：[StudyAnalysis-Skills / Knowledge Absorber](https://github.com/YuJunZhiXue/StudyAnalysis-Skills)（629★）  
5. **制卡（可选）**：[doasfrancisco/anki-skill](https://github.com/doasfrancisco/anki-skill)（57★）若已用 Anki  

串法：`grill/MISSION` → `anything-to-course 大纲` → 每章 `Matt teach` 或 ATC lesson → 读代码时 `pstack teach` → 当天 `/quiz` → 按 FSRS/Anki 隔天回看。

---

## 6) 星数速查表（2026-10-11 JST API）

| Repo | Stars |
|------|------:|
| mattpocock/skills | 285571 |
| microsoft/ai-agents-for-beginners | 76903 |
| backnotprop/pstack | 1564 |
| YuJunZhiXue/StudyAnalysis-Skills | 629 |
| Haozhe-Xing/agent_learning | 579 |
| minicoohei/ai-agent-camp | 347 |
| wwwzhouhui/skills_collection | 282 |
| kirilxd/claude-tutor | 137 |
| huifer/Claude-Code-KnowCraft | 75 |
| HumphreySun98/Smart-Study-Agent | 58 |
| doasfrancisco/anki-skill | 57 |
| mordor-forge/study-skill | 46 |
| charlesjones-dev/ai-agent-plugins | 35 |
| lowwwbank/anything-to-course | 22 |
| cheanus/SRSA | 22 |
| Bhala-Srinivash/agent-tutor-skill | 11 |

更早的六类总览长文：`/workspace/learning-skills-survey.md`（与本篇互补；本篇补齐星数、teach 对照、拆章工具链、必备/可选）。

