# Part A：用 AI 加速「未知领域」学习（含记忆衰减）— 调研笔记

> 生成日期：2026-10-11（Asia/Tokyo）  
> 范围：文章 / 博客 / 论文 / 学习科学哲学 + AI 辅导实践；**不限于 skill**。  
> 原则：每条尽量带链接与日期；反驳「第一天一口气学 8 小时」。

---

## 0. 一句话结论

**AI 最适合砍掉「不必要的难」（找资料、生成练习、给反馈、排日程），绝不能砍掉「必要的难」（检索、间隔、交错、费力解释）。**  
记忆会衰减；第一天灌 8 小时只抬短期流畅感，长期留存靠「短会话 + 第二天 explain-back + 间隔复习」。无起来的链路是：

**定任务 → 元学习地图 → 分章课 → 当日测验 → 次日讲回 → 制卡进 Anki → 真题/真项目 → 社区校验。**

---

## 1. 核心学习科学（哲学层）

| 概念 | 主张 | 对 AI 学习的含义 | 关键来源 |
|---|---|---|---|
| **间隔效应（Spacing）** | 同样总时长，分散多次 > 一次塞满 | 禁止 binge；排 1d / 3d / 7d / 多周的再测 | Cepeda et al. 2008；Smolen et al. *Nat Rev Neurosci* 2016 |
| **检索练习（Retrieval）** | 从记忆里掏出 > 再读一遍 | AI 先逼你答，再给反馈；禁止先给完整答案 | Roediger & Karpicke 2006；Dunlosky 2013「高效用」 |
| **交错练习（Interleaving）** | 相似主题混练，利于辨别 | 后期会话混题；前期可 block 学低相似技能 | Carvalho & Goldstone；Chen et al. 2021 系统综述 |
| **合意困难（Desirable Difficulties）** | 练习时更难 → 之后更牢 | AI 流利讲解会制造「学会了」幻觉 | Bjork；*The Effortless Trap* arXiv 2606.26181 |
| **最近发展区（ZPD）** | 刚好差一点、有脚手架才能跳上去 | AI 要动态加/撤提示，别一上来给全解 | Vygotsky；2025–2026 多篇 AI scaffolding 实验 |
| **刻意练习（Deliberate Practice）** | 明确目标、重复、即时信息反馈、在舒适区外 | AI 当教练：一次只纠一个点，保留练习量 | Ericsson 1993；后续 AI+技能训练 RCT |
| **流畅度 ≠ 存储强度** | 当下觉得会 ≠ 下周还会 | Matt teach / LAQ 都强调 storage strength | Bjork；Matt Pocock teach skill |

### 1.1 间隔有多「优」？

Cepeda, Vul, Rohrer, Wixted, Pashler（2008，*Psychological Science*）对 1350+ 人：最优复习间隔随**最终测验延迟**变——测验越远，最优间隔越长（约为延迟的约 5–20%）。  
→ 「今天狂学、明天考」可以很短间隔；「三个月后还要用」需要数天到数周的 gap，而不是一天 8 小时。  
链接：https://journals.sagepub.com/doi/10.1111/j.1467-9280.2008.02209.x

### 1.2 Dunlosky 效用排序（2013）

十种技术里，**只有「练习测验 + 分散练习」评高等效用**；重读、划线低效用。  
链接：https://www.psychologicalscience.org/publications/journals/pspi/learning-techniques.html  
科普：https://www.scientificamerican.com/article/what-works-what-doesn-t/（Scientific American）

---

## 2. 方法清单（过程 / 产物 / 目标）

> 同类叫「teach」也拆开：目标、过程、产物可以完全不同。

### A. 长期教学工作区（跨会话课程）

| 方法 | 过程 | 产物 | 目标 |
|---|---|---|---|
| **Matt Pocock `/teach`** | 当前目录当课程仓：先问清 MISSION → 搜可信资源进 RESOURCES → 按 ZPD 出短课 HTML → 写 learning-records → 维护 reference 速查 | `MISSION.md`、`RESOURCES.md`、`lessons/*.html`、`learning-records/*.md`、`reference/*.html`、`NOTES.md` | 跨多天把「知识+技能+智慧」钉在真实动机上；强调 storage strength |
| **Stuart Dalrymple LAQ（Claude Project）** | Project Instructions=OS；Brain File=背景/目标/80-20 地图；每会话先 recall | Brain File、Recall Queue、会话日志 | 用检索主导的个人 LMS；跨会话校准难度 |
| **Claude `/learn` skill（社区 gist）** | 6 阶段 14 步：进度文件 → 间隔复习 → 当前步 → 更新 progress → 建议下次间隔 | `progress.md`、各阶段产物 | 把 SRS + Feynman + 刻意练习嵌进 agent 会话节奏 |

- Matt teach：https://github.com/mattpocock/skills （SKILL.md 当前可查）  
- LAQ：https://www.stuartdalrymple.com/learn-anything-quickly.html （2026-04）  
- `/learn` gist：https://gist.github.com/distinctgrey/68334b52802164ec2e673f5365e3e5ff

### B. 代码 / 机制理解（单次讲透）

| 方法 | 过程 | 产物 | 目标 |
|---|---|---|---|
| **pstack `teach` / `how` / `why` / `bro`** | 对着仓库或 diff 分层讲：怎么跑 / 为何如此 / 大白话 | 讲解文本、架构图、简化复述 | **理解现有系统**，不是建长期课程 |
| **Feynman + AI 次日讲回** | Day0 读课+小测 → 睡觉 → Day1 闭卷讲回 → AI 按 rubric 判 PASS/FAIL | 讲回稿、缺口清单、再教计划 | 测「机制是否过夜还在」 |
| **Knowledge Absorber** | 摄取 URL/PDF/代码 → 真理锚定校验 → 叙事透镜 → 出 MD+HTML 晶体 | `knowledge_YYYYMMDD_*.md/html` | 高认知负荷材料 → 可存档教学笔记 |

- Feynman+AI：https://learningharness.org/feynman-technique-with-ai （2026-09-12）  
- Knowledge Absorber：https://github.com/YuJunZhiXue/StudyAnalysis-Skills

### C. 检索 / 间隔 / 制卡

| 方法 | 过程 | 产物 | 目标 |
|---|---|---|---|
| **AI 生成检索题（课堂实证）** | LLM 从讲义出题 → 段末低利害测验 → 即时反馈 | 题库、周准确率 | 把 retrieval 塞进真实课 |
| **个人 AI 导师 + 分布式检索** | GPT 从教材出微题 → 建学生 grasp 模型 → 个性化间隔 | 微题、grasp 分数、成绩提升 | 实施「人人不同」的 spaced retrieval |
| **Memdora / FSRS-6 类 SRS** | 阅读处一键制卡；17 种认知交互；FSRS 调度 | 卡组、独立调度状态 | 降低制卡摩擦、提高认知参与 |
| **Obsidian → Anki 桥** | 笔记原子化 → 只抽可测事实制卡 → AnkiConnect | 概念笔记 + 卡组（分家） | PKM 管关系，SRS 管事实 |

- LLM retrieval 题：https://arxiv.org/pdf/2507.05629v2.pdf（约 2025）  
- UniDistance AI tutor：https://dl.acm.org/doi/10.1007/s10639-024-12888-5（期刊；抓取摘要标 Jan 2025）  
- Memdora：https://arxiv.org/abs/2607.25096（2026-07/08）  
- ObsidianKi：https://github.com/ccmdi/obsidianki ；Knowledge-Factory：https://github.com/Brunimir/Knowledge-Factory

### D. 脚手架 / ZPD 动态辅导

| 方法 | 过程 | 产物 | 目标 |
|---|---|---|---|
| **阶段感知 LLM tutor** | 新手：样例+脚手架；进阶：自解释提示并淡出 | 对话日志、心理努力、深层参与指标 | 按技能阶段改支持强度 |
| **动态 ZPD 脚手架（数学证明）** | 四层动态调节提示 vs 静态 prompt | 更低外在负荷、更好远迁移 | 动态 ZPD > 静态「一直讲」 |
| **有护栏的 GPT Tutor（Bastani）** | 只给 hint、不给完整答案 | 练习分↑、无辅助考试不掉 | 防「拐杖效应」 |

- Learner-stage-aware tutor：https://dl.acm.org/doi/10.1007/978-3-032-29763-1_39  
- ZPD scaffolding PDF：http://www.stemmpress.com/uploadfile/202602/e7447b357f0c63e.pdf（2026）  
- Bastani et al. PNAS：https://www.pnas.org/doi/10.1073/pnas.2422633122（2025-06-25）

### E. 元学习 / 对齐 / 共赢协作

| 方法 | 过程 | 产物 | 目标 |
|---|---|---|---|
| **Ultralearning 元学习 + AI Deep Research** | 先画技能树/专家课表，再进真练 | 研究简报、子技能清单、练习设计 | 解决「未知领域不知从哪学」 |
| **Scott Young：必要难 vs 不必要难** | AI 砍不必要难，保留检索/建模/练习 | 实践清单（22 条） | 防 AI 把必要努力也砍掉 |
| **Matt `grill-me`** | 一轮轮追问决策树直到心智模型对齐 | 共享理解（不一定是文档） | 人–AI 共赢：先对齐再产出 |
| **pstack `interrogate` / `arena`** | 多角度对抗评审 / 多方案嫁接 | 盲点表、合成方案 | 找自己看不见的洞 |
| **Dafi 式会话协议** | 先闭卷回忆 → 比笔记缺口 → 只讲缺口 → 单题测验 → 记弱项 | 弱项列表、2 天后复习计划 | 45 分钟会话模板 |

- Ultralearning+AI：https://www.scotthyoung.com/blog/2026/04/29/ultralearning-ai/（2026-04）  
- 22 Thoughts：https://www.scotthyoung.com/blog/2025/05/13/22-thoughts-on-using-ai-to-learn-better/（2025-05）  
- grill-me：https://www.skills.sh/mattpocock/skills/grill-me  
- Dafi：https://www.dafi-ai.com/en/blog/how-to-use-chatgpt-and-claude-to-study（2026-09-26）

### F. 制卡 / 吸收 / 复习产品形态（简述）

- **Anki + FSRS-6**：调度算法；AI 只负责生成/润色卡，不负责「替你回忆」。  
- **Zettelkasten + SRS 分家**：笔记管关系，卡片管可测原子事实（SmartRecall 文，2025–26 实践文）。  
- **Knowledge Absorber 导师模式**：HTML 晶体旁开 mentor relay，针对卡片追问。

---

## 3. 反例：「第一天学爆 8 小时」为什么不行

| 证据 | 说了什么 | 对 binge 的打击 |
|---|---|---|
| **Binge watching → 记忆**（Horvath et al., *First Monday*, 2017-09） | 一口气看完即时记忆强，但比每日/每周观看**衰减更快**，主观享受也更低 | 「当日爽」≠「以后还在」  
  https://firstmonday.org/ojs/index.php/fm/article/view/7729 |
| **Cepeda 2008 最优间隔脊线** | 要长期保留，复习 gap 应随目标保留期拉长；零间隔（等同塞在一起）最差 | 8 小时连轴 = 近似零间隔 |
| **Roediger & Karpicke 2006** | 5 分钟后：重读更好看；2 天/1 周后：测验组完胜 | 当日自评会骗你；次日才见真章 |
| **Bastani PNAS 2025** | 无护栏 GPT：练习 +48%，**拿走 AI 后考试 −17%**；有护栏 tutor 几乎不伤 | 「AI 陪练很猛」可以是假进步 |
| **Effortless Trap / AI 削弱合意困难** | 流利讲解去掉 productive struggle → 能力幻觉 | 一天刷 8 小时 AI 讲解 = 高流畅、低存储 |
| **Scott Young 2025–26** | 必要努力（检索、建模、练）不可外包；Directness：别用模拟练替代真环境 | 未知领域更忌「只和 AI 聊、不上真料」 |
| **Feynman+AI 文（2026-09）** | 同日讲回测的是短期；**次日讲回**才测巩固后记忆；失败则改角度再教，再隔夜讲回 | 正确节奏是「跨夜」，不是「通宵」 |

**操作化反 binge 规则（可写进个人协议）：**

1. 单日**新材料 ≤ 会话 40–60%**（第一周后更严）；其余给检索/订正/混练。  
2. 每个概念：**当日小测 → 次日 explain-back → 通过才制卡**。  
3. 弱项进入间隔队列（1 / 3 / 7 / 14 天或 FSRS），禁止「全塞进 day1」。  
4. AI **禁止在你尝试前给完整答案**（Bastani 护栏）。  
5. 用真实产出（小项目、真题、对社区提问）做 Directness 检验。

---

## 4. 栈与串接（必备 / 可选 → 一条未知领域链路）

### 4.1 必备品（Minimal Viable Learn Stack）

| 层 | 必备 | 干什么 |
|---|---|---|
| **动机与范围** | 一份 `MISSION.md`（或 Brain File） | 未知领域先回答「为什么学、学完能干什么」 |
| **可信源** | `RESOURCES.md` + 至少 1 本权威书/官方课/综述 | 不信任模型参数记忆；AI 只做导航 |
| **工作区** | 一个 git 目录（或 Claude Project / Obsidian vault） | 跨会话状态：课、记录、弱项 |
| **Tutor 协议** | 固定系统提示：先检索、再反馈、护栏 hint | 防拐杖；可用 LAQ OS / Dafi 五步 / Learning Harness |
| **间隔引擎** | Anki（FSRS）或等价 SRS | 事实/定义的长期调度；AI 不替代调度 |
| **人的时间盒** | 日历上的短会话（25–50 min）+ 次日讲回槽 | 对抗三分钟热度与 8 小时 binge |

### 4.2 可选项（按需求加）

| 组件 | 何时加 | 例子 |
|---|---|---|
| **阅读器 / 摄取** | PDF、长文、多源对比 | Knowledge Absorber、Zotero、浏览器剪藏 |
| **PKM 图谱** | 概念关系复杂、要写综述 | Obsidian Zettelkasten；MOC |
| **笔记→卡桥** | 制卡量上来 | ObsidianKi、Yanki、flashcards-obsidian、Knowledge-Factory |
| **课程生成 skill** | 要章节化大 scope | Matt `/teach`（单独目录，勿与 pstack teach 混） |
| **代码讲解 skill** | 学仓库/系统 | pstack `how`/`why`/`teach` |
| **对齐 skill** | 开学前定范围、防跑偏 | `grill-me`：把「学什么」问到对齐 |
| **对抗评审** | 方案/理解找盲点 | pstack `interrogate` / `arena` |
| **Agent 选型** | 长课用强推理；制卡/批改可用中档 | 辅导会话：Claude/GPT 强模型；批量制卡可便宜模型 |
| **编排层** | 多 worker 并行调研 | Multica Squad / 本地并行；**学习主链路仍要人在环做检索** |
| **社区** | 需要「智慧」与现实反馈 | Reddit / linux.do / 专业论坛（Matt teach 明确建议） |

### 4.3 推荐仓库结构（未知领域一仓）

```text
learn-<domain>/
  MISSION.md                 # 为何学、成功标准、时限
  RESOURCES.md               # 可信源 + 状态（未读/已核）
  NOTES.md                   # 偏好、护栏、代理环境
  curriculum/
    00-map.md                # 80/20 地图 / 章节树
    chapter-01.md ...
  lessons/                   # 或 Matt 式 HTML 短课
  learning-records/          # 洞见 / 误区 / 任务变更 ADR
  reference/                 # 速查：术语表、公式、API
  crystals/                  # Knowledge Absorber 输出
  weak-items.md              # 当日弱项 → 喂给 SRS
  progress.md                # 上次会话、下次建议间隔
```

Obsidian 可把同一结构当 vault；Anki deck 建议命名 `learn-<domain>`，卡字段带 `Source:: [[note]]`。

### 4.4 Agent / Workflow 怎么配

| 角色 | 建议 | 注意 |
|---|---|---|
| **主编导师** | 一个长期 Project / 目录会话（LAQ 或 `/teach`） | 持有 Brain/MISSION；每会话先 spaced review |
| **摄取工** | Knowledge Absorber 或「读 PDF→晶体」提示 | 产出要过真理锚定 / 人抽查 |
| **出题工** | 「只从 RESOURCES 出检索题」 | 人先答；错题进 weak-items |
| **判卷工** | 次日 Feynman grader（持有课文+rubric） | 禁止补全你的句子 |
| **制卡工** | 仅对 **PASS 的概念** 出 WHAT/HOW/WHEN 卡 | 错解制卡 = 间隔强化错误 |
| **对齐工** | 开课前 `grill-me` 一次 | 产物是共享心智模型，不是长文 |

**不要用 Cloud Agent 替你「学」**（本次调研要求）；并行 agent 只适合**搜资料、对比源、生成草稿题**，最终检索和讲回必须本人。

### 4.5 串成一条「未知领域」链路（端到端）

```text
Day −1  对齐
        grill-me / 访谈 → 写 MISSION + 成功标准 + 每周小时数上限
        AI Deep Research → 草稿地图 → 人钉住 1–2 个权威源进 RESOURCES

Week 0  元学习
        80/20 地图（LAQ Brain 或 curriculum/00-map.md）
        划 ZPD：第一章必须「稍难但可做」

每日循环（25–50 min，禁止 8h）
        ① 间隔复习：Anki + 上次第日讲回失败项（10–15 min）
        ② 新课：一章/一课（Matt lesson 或晶体+导师）≤ 会话 40–60%
        ③ 闭卷检索：自写 / 单题测验（Dafi 步 1+4）
        ④ 只对缺口要 AI 解释（护栏：hint 优先）
        ⑤ 记 weak-items；预约「明天讲回」

次日
        Explain-back → PASS 才制卡进 Anki；FAIL → 换角度再教 → 再隔夜

每周
        交错混测；Directness：一个最小真项目 / 真题 / 社区提问
        更新 Brain/MISSION/learning-records；砍掉不再服务使命的支线

每月
        远迁移测验（无 AI）；回看 Cepeda：按「还要用多久」调间隔
```

**与「第一天学爆」对照：**  
链路把「懂」拆成三关——**当日着陆（小测）→ 过夜巩固（讲回）→ 长期调度（SRS）+ 真实迁移**。任何一关被「一天读完」跳过，都会在拿掉 AI 或数周后暴露（Bastani / binge / spacing 证据同向）。

---

## 5. 同名不同物速查（teach 族）

| 名字 | 过程重心 | 主产物 | 主目标 |
|---|---|---|---|
| Matt `/teach` | 多会话课程仓 + ZPD + 资源 | HTML 课 + MISSION | 长期学会一门 |
| pstack `/teach` | 单次把代码讲清 | 讲解 | 理解这段系统 |
| Feynman+AI | 次日讲回 + rubric | PASS/FAIL | 测机制留存 |
| Knowledge Absorber | 摄取→锚定→晶体 | MD/HTML | 材料变可教笔记 |
| LAQ | Brain + 每课先 recall | Brain / Queue | 个人检索型 LMS |
| `/learn` gist | 固定 6 阶段进度机 | progress.md | 习惯强制间隔 |

---

## 6. 精选书目 / 长文索引（带日期）

| 条目 | 日期 | 链接 |
|---|---|---|
| Dunlosky et al. 高效学习技术综述 | 2013 | https://www.psychologicalscience.org/publications/journals/pspi/learning-techniques.html |
| Cepeda et al. 间隔脊线 | 2008 | https://journals.sagepub.com/doi/10.1111/j.1467-9280.2008.02209.x |
| Smolen et al. spaced learning 机制 | 2016 | https://www.nature.com/articles/nrn.2015.18 |
| Horvath et al. binge 与记忆 | 2017-09 | https://firstmonday.org/ojs/index.php/fm/article/view/7729 |
| Make It Stick（书） | 2014 | https://www.hup.harvard.edu/books/9780674419377 |
| Bastani et al. AI 无护栏伤学习 | 2025-06-25 | https://www.pnas.org/doi/10.1073/pnas.2422633122 |
| Scott Young 22 Thoughts | 2025-05 | https://www.scotthyoung.com/blog/2025/05/13/22-thoughts-on-using-ai-to-learn-better/ |
| Scott Young Ultralearning×AI | 2026-04 | https://www.scotthyoung.com/blog/2026/04/29/ultralearning-ai/ |
| UniDistance AI tutor 案例 | ~2025 | https://dl.acm.org/doi/10.1007/s10639-024-12888-5 |
| LLM 检索题课堂研究 | 2025 | https://arxiv.org/pdf/2507.05629v2.pdf |
| Memdora AI-SRS | 2026-07/08 | https://arxiv.org/abs/2607.25096 |
| LAQ | 2026-04 | https://www.stuartdalrymple.com/learn-anything-quickly.html |
| Dafi 学习用法 | 2026-09-26 | https://www.dafi-ai.com/en/blog/how-to-use-chatgpt-and-claude-to-study |
| Feynman+AI 次日讲回 | 2026-09-12 | https://learningharness.org/feynman-technique-with-ai |
| Effortless Trap（合意困难×AI） | 2026（arXiv 2606.26181） | https://arxiv.org/pdf/2606.26181.pdf |
| AI Ed：retrieval/spacing/interleaving | 持续更新 | https://edtechdev.github.io/aied/concepts/retrieval-spacing-interleaving/ |

---

## 7. 给 Justin 的直接建议（落地）

1. **大 scope 章节化**：单独开 `learn-<topic>/`，用 Matt `/teach` 或手写 `curriculum/`；别和 pstack 的代码 `teach` 混在一个 skill 名下理解。  
2. **已装 pstack**：读 Harbor / 代码用 `how`/`why`/`teach`；找盲点用 `interrogate`。  
3. **抗衰减最小闭环**：当日测 → 次日讲回 → PASS 才进 Anki；会话长度封顶。  
4. **护栏写进 NOTES.md**：AI 不得在尝试前给全解；新材料占比上限；每周一次无 AI 迁移测。  
5. **共赢**：开课前 `grill-me` 对齐使命；学的过程中人负责检索，AI 负责出题、判卷、摄取、排程。

---

*本文件为 part-a（学习科学 + AI 方法 + 栈串接）。后续 part 可补：YouTube/Reddit/X/linux.do 社区案例深挖、具体 prompt 库、与 Harbor 评测工作流的嫁接。*
