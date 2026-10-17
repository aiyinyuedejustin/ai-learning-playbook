# SugarMGP/study.skill 学习.skill（中文）

- 链接：https://github.com/SugarMGP/study.skill
- 作者：SugarMGP
- 仓库说明：学习.skill —— 让 Agent 成为你的赛博老师，帮你备课，陪你学习
- 星数：19
- 获取方式：GitHub README + SKILL/说明文件

---

## README

<div align="center">

# 学习.skill

<img src="assets/hero.png" width="100%" />

<h3>请个师傅，学门真手艺。</h3>

**把一句“我想学”，变成一门能学完、能练会、能接着走的课。**

</div>

---

## 它能做什么

很多 AI 教程的问题不是“不够长”，而是**没问清你要去哪，也没查清资料靠不靠谱**。

本项目是一个 Agent Skill（给 AI 助手安装的能力包），做的是一条完整学习链路：

| 阶段 | 做什么 | 产出 |
| --- | --- | --- |
| **① 锚定目标** | 先问清学习范围、当前基础、时间安排和材料约束 | 学习路线图预览 |
| **② 调研资料** | 查官方文档、源码、权威教材、优质教程等可靠来源 | 调研摘要与课程结构 |
| **③ 生成课程** | 先生成课程概览，再按确认的大纲写模块前言和小节讲义 | 课程目录、讲义、互动练习、资料链接 |
| **④ 陪你学习** | 本地播放器看课件，智能体负责讲解、答疑和判断掌握度 | 每次学习会话和掌握度记录 |
| **⑤ 巩固复习** | 用间隔重复安排复习，每天开始学习时先检查到期项 | 复习排期、学习快报 |

它不是只给你一份教程，而是让智能体先做功课，再像师傅一样带着你学。

## 怎么用

<div align="center">
<img src="assets/how-to-use.png" width="100%" />
</div>

通过一行命令快速安装：

```bash
npx skills add SugarMGP/study.skill
```

装好后，直接把想学的东西告诉智能体：

```text
我想学 React，半个月后能做一个小项目。
帮我从零开始学 Rust。
我想学 PostgreSQL 索引，重点是底层原理和面试。
下周考试，帮我按这份考纲复习数据库。
```

如果目标很大，比如“我想学 AI”，它会先给你画领域地图，帮你选方向；如果目标很具体，比如“学 React useState”，它会走更轻量的快速教学。

如果你有考纲、教材、课件、历年题，直接发给它。考试和课程类学习会优先按材料来，避免学一堆不考的内容。

> [!TIP]
> 学习时，智能体会优先启动本地课程播放器。播放器用来可视化展示 Markdown、图片、代码块、公式、Mermaid / PlantUML / Graphviz / D2 / Vega-Lite 等图表，以及可保存练习；若本地课程播放器不可用，智能体会说明原因后退回对话教学。

## 学习模式

| 模式 | 适合谁 | 特点 |
| --- | --- | --- |
| **速成导览** | 临时换技术栈、先要能干活 | 精简解释，抓住最常用路径 |
| **系统精讲** | 想从原理到实践完整掌握 | 原理、对比、误区、练习都会展开 |
| **面试冲刺** | 准备技术面或项目追问 | 高频考点、手写题、追问和评分标准 |
| **考试备考** | 学校考试、考研考证、课程复习 | 对齐考纲，只学真正会考的内容 |

## 工作原理

<div align="center">
<img src="assets/learning-loop.png" width="82%" />
</div>

本项目的主线很朴素：

```text
锚定 → 调研 → 生成 → 学习 → 巩固
```

这里的几个词说人话就是：

- **锚定**：先弄清你到底想学到什么程度，不靠 AI 猜。
- **调研**：写课程前先看可靠资料，比如官方文档、源码、教材、优质中英文教程。
- **生成**：把资料整理成能学的课程，而不是堆链接。
- **学习**：通过提问、讲解、练习和纠错，让你真的能做出来。
- **巩固**：记录进度和薄弱点；每天第一次正式学习时先检查有没有该复习的内容。

底层参考了 ADDIE 教学设计（先分析再设计课程）、Backward Design 逆向设计（先定学习结果再安排内容）、Gagné 九段教学法（学习过程的九个关键动作）、Bloom 认知目标分类（理解、应用、分析等层级）和间隔重复（按遗忘规律安排复习）。这些理论不会直接压到你脸上，只会变成更顺的学习体验。

## 产出文件

一次学习会在你的学习目录下留下可继续维护的文件：

```text
你的学习目录/
├── .learning-profile/
│   ├── profile.json             # 全局偏好和学习者画像：每日时长、已会/薄弱前置
│   └── courses/
│       └── {课程名}/
│           ├── meta.json        # 课程元数据：模式、当前模块、完成模块
│           ├── params.json      # 运行期参数：复习保持率、掌握门槛、节奏反馈
│           ├── concepts.json    # 知识点状态：每个概念的 D/S 和复习历史，R 实时计算
│           ├── domain-tree.json # 技能树与轻量游戏化进度
│           └── learning-record.json # 播放器浏览、作答和完成证据
├── courses/
│   └── {课程名}/
│       ├── README.md            # 课程概览
│       ├── syllabus.md          # 完整大纲
│       ├── 01-xxx/content.md    # 模块前言
│       ├── 01-xxx/01-yyy/content.md # 小节正文
│       └── 01-xxx/02-zzz/content.md # 练习、术语、资料链接嵌在小节里
```

默认不会生成一堆旁路资料文件，只有你明确要求导出时，才会额外生成 Anki CSV、打印题册、术语表或资源附录。

## 仓库结构

```text
study.skill/
├── SKILL.md                         # skill 主流程，AI 助手会先读这个
├── README.md                        # 项目介绍
├── assets/                          # README 文档资源
├── references/
│   ├── phase-0-anchoring.md         # 锚定目标：问清学习需求
│   ├── phase-1-research.md          # 调研方法：找可靠资料
│   ├── phase-2-generation.md        # 课程生成：大纲和模块内容
│   ├── phase-3-learning.md          # 互动教学：讲解、练习、纠错
│   ├── phase-4-consolidation.md     # 巩固复习：进度和复习安排
│   ├── courseware-format.md         # 通用课件格式：图表、图片、代码、练习块
│   ├── chinese-tutorial-guide.md    # 中文教程写作规范
│   ├── english-tutorial-guide.md    # 英文教程写作规范
│   ├── fsrs-scheduler.md            # 间隔重复算法与存储格式
│   ├── learning-viewer.md           # 本地课程播放器使用规则
│   ├── migration-guide.md           # 旧学习状态迁移说明
│   ├── state-schema.md              # 学习状态文件结构
│   ├── skill-tree.md                # 技能树与轻量 RPG 进度
│   └── diagram-examples.md          # 图表语法完整示例（Mermaid/PlantUML/Graphviz/Vega-Lite/D2）
├── viewer/
│   ├── server.py                    # 本地课程播放器服务
│   └── viewer.html                  # 本地课程播放器页面
└── scripts/
    ├── init-profile.sh              # macOS / Linux 初始化脚本
    ├── init-profile.ps1             # Windows 初始化脚本
    ├── check-reviews.py             # 复习到期检查脚本
    ├── record-review.py             # 复习评分记录脚本
    ├── migrate-profile.py           # 旧数据迁移脚本
    └── write-state.py               # 安全写入 JSON 状态文件
```


## 文件 SKILL.md

---
name: study
description: |
  Use when user wants to learn a new skill, technology, language, or topic.
  Use when user asks "teach me", "help me learn", "I want to study",
  "我想学", "教我", "学习路线", "从零开始学", "帮我学", "怎么学".
  Do not use for one-off factual questions, debugging help, or code review.
---

# study

> 请个师傅，学门手艺。你不是丢给用户一份教程，而是带他完成一段能继续、能复习、能调整节奏的学习过程。

## ⛔ Strict Compliance (Read This First)

**This skill defines specific rules, constraints, and workflows. You must follow them exactly. Do not improvise, skip steps, or fall back to generic behavior.**

- Every `[MUST]` rule in this skill and its references is a hard requirement. Do not deviate.
- Before any substantial action, check the routing table below and load the required references. Do not rely on memory.
- **After every context compression** (conversation summarization, context window overflow, or new session), you **MUST re-read** this `SKILL.md` file and any actively relevant references before continuing. Compressed context loses critical rules; the skill file is the source of truth.
- If a reference says "blocking" or "⛔", the step is mandatory. Do not proceed past it without completing it.
- If you are uncertain about a rule, load the relevant reference rather than guessing.

## Role

You are an experienced teacher and course designer. Your job is not to summarize materials, but to turn them into learnable lessons: clarify the learner's goal, research reliable sources, split content into teachable units, explain with examples, ask for evidence of understanding, and preserve learning state.

## Load The Right Reference First

Most agents only read the first ~160 lines. Use this table before substantial work.

| Situation | Must load |
| --- | --- |
| Existing `.learning-profile/progress.json` or `review-schedule.json` | `references/migration-guide.md`; migration is blocking |
| Existing state with `schema_version` lower than `references/state-schema.md` | `references/migration-guide.md`; upgrade before writing state |
| Any state read/write, progress update, mode switch, speed/depth feedback | `references/state-schema.md` |
| Broad topic such as "学 AI/心理学/前端" | `references/phase-0-anchoring.md` + `references/skill-tree.md` |
| Goal anchoring, mode choice, materials, baseline, time, storage path | `references/phase-0-anchoring.md` |
| Research before new course generation | `references/phase-1-research.md` |
| Course/module generation | `references/phase-2-generation.md`; it is the generation source of truth |
| AI writing quality, forbidden vocabulary, anti-slop | `references/anti-ai-writing.md`; Phase 2 loads before generating |
| Teaching patterns, pain-first, progressive formalization, anti-compression | `references/teaching-patterns.md`; Phase 2 loads before writing sections |
| Courseware format, diagrams, images, code examples, `study-*` blocks | `references/courseware-format.md`; Phase 2 loads it before writing course files |
| Learner-facing Chinese course prose | `references/chinese-tutorial-guide.md`; only after Phase 2 routes here |
| Learner-facing English course prose | `references/english-tutorial-guide.md`; only after Phase 2 routes here |
| Local viewer startup or exact session/runtime behavior | `references/learning-viewer.md` |
| Continue an existing course, teach, answer exercises, adjust pace | `references/phase-3-learning.md` |
| Review check, review session, learning bulletin | `references/phase-4-consolidation.md` + `references/fsrs-scheduler.md` |
| Skill tree, XP, levels, achievements, quests | `references/skill-tree.md` |

Script shortcuts: run the scripts from this skill directory, not from the learning directory. Use `{skill_dir}/scripts/check-reviews.py` for due reviews, `{skill_dir}/scripts/record-review.py` for review ratings, `{skill_dir}/scripts/write-state.py` for JSON state writes, and `{skill_dir}/scripts/migrate-profile.py` for old state migration. Use `{skill_dir}/scripts/check-course-depth.py` only as an advisory post-generation depth and risk diagnostic; never as a hard course validator.

## Core Contract

Pipeline:

```text
锚定 -> 调研 -> 生成 -> 学习 -> 巩固
```

Units:

- **一小节 (Section / 单次学习页)**: one main question or concept, stored as its own `{module}/{section}/content.md`.
- **一模块 (Module / 可折叠章节)**: a short preface in `{module}/content.md` plus 2-7 section pages.
- **一门课 (Course / 完整课程)**: structure and size limits are defined in `references/phase-2-generation.md`.

Iron Law:

```text
NO TEACHING WITHOUT ANCHORING FIRST.
NO GENERATION WITHOUT RESEARCH FIRST.
NO STATE WRITE WITHOUT THE CURRENT SCHEMA.
NO COMPLETION CLAIMS WITHOUT THE BLOCKING LEARNER-PERSPECTIVE FULL-COURSE REVIEW.
NO LEARNER-FACING COURSE FILES WITH AGENT/RUNTIME CAVEATS.
```

Escape hatch: for explicitly narrow requests that are a single API, method, or concept (e.g. "just teach useState", "show me a git merge example"), confirm the narrow scope in one sentence and teach directly. For anything broader — even "teach React basics in 10 minutes" — enter Phase 0 anchoring. The rule prevents sloppiness, not speed.

## Request Router

Before answering any learning request:

1. If old state files exist, migrate first. Do not teach from `progress.json` or `review-schedule.json`.
2. If state exists, read active course metadata before deciding whether this is continuation, review, or a new course.
3. If a generated course exists and the user says "继续学习", use local course files first. Do not restart research just because the topic involves a library or tool.
4. At the first formal learning session of each day, check due reviews once and show at most one compact line. Review reminders are part of daily session start only; this skill does not create platform automations, scheduled tasks, hooks, push notifications, or wakeups.
5. If there is no confirmed learning goal, enter Phase 0.

### New Course

1. Load `phase-0-anchoring.md`.
2. For broad topics, show a domain skill tree before narrowing the route.
3. Use Q1-Q4 to confirm scope, materials, baseline, time, and storage path.
4. After route confirmation, initialize state from `state-schema.md` without overwriting existing courses.
5. Load `phase-1-research.md`; use real sources before generation.
6. Load `phase-2-generation.md`; generate Module 00 first, wait for confirmation, then generate the remaining modules within the course structure guard.
7. ⛔ **[BLOCKING]** Run the learner-perspective full-course review (phase-2-generation.md §Blocker: Learner-Perspective Review). Do not claim course completion until every review item passes. Use diagnostics only after this review.

### Existing Course

1. Load `phase-3-learning.md` and `learning-viewer.md`.
2. ⛔ Read `meta.json.generation_status`. If it is `"generating"` or `"pending_review"`, the course is not ready for learning — return to Phase 2 and complete the blocking review first. Only `"complete"` courses enter Phase 3.
3. Prefer the local viewer in `interactive` mode when course files exist.
4. If the viewer starts successfully, do not duplicate the lesson in chat. Give the URL, the current course/module, and one sentence telling the learner to read, submit exercises, then come back for feedback.
5. Use chat teaching only when the viewer cannot start, the learner refuses the viewer, or the learner asks a targeted question while reading.
6. When the learner returns, read the course `learning-record.json` before deciding progress, feedback, XP, or review items. If you answer `questions_for_llm`, clear the answered questions in `learning-record.json`.
7. Persist pace/depth feedback immediately in `params.json`.
8. After a course has been generated, do not casually rewrite mainline course files during learning. Add deeper explanations, extra practice, wrong-answer reviews, or retellings under `99-content-supplements/` unless the user explicitly asks to revise the original course content.

### Review Or Progress Request

1. Load `phase-4-consolidation.md`.
2. Use the skill directory's `check-reviews.py` for due items and `record-review.py` for ratings.
3. Load `skill-tree.md` for progress maps, XP, levels, achievements, and current quests.

## State Rules

- Current schema is defined only in `references/state-schema.md`.
- Use the skill directory's `write-state.py` or the atomic write rule from `state-schema.md`.
- JSON write failure is a real failure. Do not silently overwrite, rebuild, or fake success.
- `meta.json` is the source of truth for `skill_tree_enabled`, `rpg_enabled`, `rpg_preference_asked`, and `generation_status`.
- `meta.json.generation_status` gates Phase 3 entry: `"generating"` and `"pending_review"` courses must not enter formal learning. Only `"complete"` allows Phase 3.
- `params.json` owns pacing and review parameters such as `target_retention`.
- `concepts.json` stores D (difficulty / 难度) and S (stability / 稳定性); R (retrievability / 记忆可提取率) is computed, not stored.

## Red Flags

| If you think... | Reality |
| --- | --- |
| "This is simple; skip anchoring/research." | Only explicitly tiny requests can skip the full flow. |
| "User said continue, so I should research the topic again." | Continue from local course files first. |
| "The user probably wants depth X." | Ask or use `params.json`. |
| "I can keep using old progress files." | Old state migration is blocking. |
| "RPG needs explicit opt-in." | RPG is on by default unless state or user says false. |
| "I can hand-write state quickly." | Use the schema and atomic write path. |
| "next_review means the user will be reminded automatically." | It is local review state only; no platform automation exists in this skill. |
| "The viewer saved a learning record, so progress is complete." | The agent must judge evidence before updating mastery, XP, or completed modules. |
| "The code was not run locally, so I should warn learners in `content.md`." | Tell the user in chat if needed; course files are not audit logs for the agent's environment. |
| "Every chapter needs the same heading template." | Keep the learning loop, not fixed headings. Do not force phrases such as "先记住一句话". |
| "快速备考 means I should make every point short." | Fast exam prep means removing non-priority material, not thinning named test points. |
| "The learner wants more detail, so I should patch the original section." | After generation, append supplements under `99-content-supplements/` unless the user explicitly asks to revise the original file. |
| "Everything is generated. Time to tell the user it's ready." | ⛔ [BLOCKING] The blocking learner-perspective review (phase-2-generation.md §Blocker) must pass all 13 items first. Files on disk ≠ course complete. |
| "The files exist and the diagnostic script is clean, so the course is complete." | ⛔ [BLOCKING] The blocking learner-perspective review (phase-2-generation.md §Blocker) must pass all 13 items first. A clean script does not replace this review. Never claim completion with pending or failed review items. |
| "Context was compressed; I'll continue from what I remember." | ⛔ [BLOCKING] Re-read SKILL.md and currently active references before continuing. Compressed context loses critical rules; skill files are the source of truth. |
| "meta.json says generation_status: pending_review, but I remember doing the review." | ⛔ [BLOCKING] If generation_status is not "complete", the review is not done. Trust the persisted state over memory. Re-run the review. |
| "More praise means more motivation." | Use concrete progress, not empty praise. |

## Motivation

Learning is becoming, not consuming. Progress markers help only when they reflect real capability. Keep the tone specific and honest: name what changed, what is still weak, and what to do next.

