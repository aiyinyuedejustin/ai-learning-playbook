# 4. 细节二：工具栈与社区的实际做法

这一章分三部分：先讲必备和可选的工具，怎么串成一条流水线；再讲社区里被反复验证的具体做法；最后按产出分类，逐个介绍学习相关的 skill 和项目。

## 最少需要三样

社区里能坚持三个月以上的人，工具大多不超过这三样：

1. **一个 AI 聊天**，学习模式开着。
2. **一个间隔复习工具**，几乎都是 Anki。
3. **一个放材料的地方**，哪怕只是一个文件夹加几个 Markdown 文件，常见的升级是 Obsidian。

少了第二样，三分钟热度的风险最高；少了第三样，每次对话都要从零交代背景，没法跨会话积累。

一周之内值得加上的三样：

| 工具 | 理由 |
| --- | --- |
| 稍后读工具（Readwise、Readeck 或同类） | 陌生领域的信息很碎，先收集再消化 |
| AnkiConnect 或 Anki MCP | 对话里冒出的难点，可以几乎零摩擦地变成卡片 |
| 学习模式固定开着 | 对抗「答案机」这个默认状态 |

Readeck 是一个自托管的稍后读工具，支持高亮和视频字幕，但它不是间隔复习工具：<https://readeck.org/>

## 按层看工具

### 从学习方法的角度：最小可用的一套

| 层 | 必备 | 干什么 |
| --- | --- | --- |
| 动机与范围 | 一份 `MISSION.md`（或背景档案） | 陌生领域先回答「为什么学、学完能干什么」 |
| 可信来源 | `RESOURCES.md`，加至少一本权威书、官方课程或综述 | 不信模型的参数记忆，AI 只负责导航 |
| 工作区 | 一个 git 目录，或 Claude Project、Obsidian 库 | 保存跨会话的状态：课、记录、弱项 |
| 导师协议 | 固定的系统提示：先检索、再反馈、只给提示 | 防止变成拐杖；可以用 Learn Anything Quickly 的「操作系统」、Dafi 的五步或 Learning Harness 的流程 |
| 间隔引擎 | Anki（FSRS）或同类工具 | 事实和定义的长期调度，AI 不能替代 |
| 时间盒 | 日历上的短会话（25–50 分钟），加第二天的讲回时段 | 同时对抗三分钟热度和一天 8 小时 |

### 从流水线的角度：每一层用什么

| 层 | 是否必需 | 干什么 | 常见选择 |
| --- | --- | --- | --- |
| 阅读与收集 | 强烈推荐 | 存文章、论文、视频字幕，做高亮 | Readwise Reader、Readeck、浏览器稍后读、Zotero（论文） |
| 笔记库 | 跨周学习时强烈推荐 | 原子笔记、链接、课程状态 | Obsidian、Logseq；Matt `teach` 的课程目录；Karpathy 式的 `raw/` 加 `wiki/` |
| AI 导师 | 必需 | 讲解、苏格拉底式追问、出题、打分 | ChatGPT Study Mode、Claude Learning、Gemini Guided Learning；本机编码 agent 的 `teach`、`how` |
| 间隔复习 | 要抗遗忘时必需 | 排复习日程 | Anki（配 AnkiConnect）、Mochi、Obsidian 间隔复习插件、Engram |
| 制卡桥 | 可选，量大后接近必需 | 高亮和笔记变成卡片草稿 | Ghostreader、对话到 Anki 的浏览器扩展、Anki MCP、n8n 流水线、制卡类 skill |
| Agent 编排 | 可选 | 拆章节、并行查资料、对抗评审 | Matt 的 `teach`、`grill-me`；pstack 的 `arena`、`interrogate`；Multica Squad、Orca（偏执行）；本机 Claude Code 的 skill |
| 外设 | 可选 | 降低输入摩擦 | 文档相机、语音模式、手写板 |

### 其他可选组件

| 组件 | 什么时候加 | 例子 |
| --- | --- | --- |
| 阅读和材料吸收 | PDF、长文多，需要多来源对比 | Knowledge Absorber、Zotero、浏览器剪藏 |
| 笔记关系图 | 概念关系复杂，要写综述 | Obsidian 卡片盒笔记、主题索引页 |
| 笔记到卡片的桥 | 制卡量上来了 | ObsidianKi、Yanki、flashcards-obsidian、Knowledge-Factory、[simple-anki-sync](https://github.com/lukmay/simple-anki-sync) |
| 课程生成 skill | 要把大范围章节化 | Matt 的 `/teach`（放在单独目录，别和 pstack 的 teach 混） |
| 代码讲解 skill | 学一个仓库或系统 | pstack 的 `how`、`why`、`teach` |
| 对齐 skill | 开学前定范围，防止跑偏 | `grill-me`：把「学什么」问到清楚 |
| 对抗评审 | 方案或理解找盲点 | pstack 的 `interrogate`、`arena` |
| 模型选择 | 长课用推理强的模型；制卡、批改可以用中档的 | 辅导会话用强模型；批量制卡用便宜模型 |
| 编排层 | 多个 worker 并行查资料 | Multica Squad 或本地并行；学习主线仍要人亲自做检索 |
| 社区 | 需要判断力和真实世界的反馈 | Reddit、linux.do、专业论坛；Matt 的 `teach` 也明确建议去社区 |

## 怎么串起来

![学习流水线](../figures/04-pipeline.png)

```text
[信息来源] YouTube / 论文 / 博客 / X
     │ 稍后读、下载字幕
     ▼
[阅读器] Readeck / Readwise / Zotero
     │ 高亮、摘录，可选 AI 起草卡片
     ▼
[笔记库] Obsidian 或课程目录
     │ 用自己的话写原子笔记，链回来源
     ├──► [AI 导师] Claude / ChatGPT 学习模式
     │       追问、出题、打分、讲卡住的地方
     │          │
     │          ▼ 人审过的原子卡片
     └──► [Anki] 每天复习，对抗遗忘
                │
                └─ 到期没记住的卡，回到下次 AI 会话当薄弱点
```

Agent 编排工具插在三个位置：

- **学之前**：用 `grill-me` 或 `interrogate` 把大范围拆成章节和验收标准。
- **学之中**：用 Matt 的 `teach` 或分章的 agent，每章一节短课加测验。
- **学之后**：用 `arena` 对同一练习比较多种解法；或者用 Orca、Multica 把已经理解的设计并行实现出来。

## 社区里被反复验证的做法

### 纸笔做题，AI 批改

Noah Tye 在纸上做题，用文档相机拍下来，通过自己写的小工具贴进 ChatGPT，让它给反馈，并区分是抄错、代数算错还是概念错。这条推文互动量在万级：<https://x.com/noahlt/status/2108675665373589841>。AGI Hunt 有一篇摘要：<https://agihunt.info/en/p/1a1234d1520dd91c81de9b50ddd>

它火的原因很简单：强制人先产出，AI 只负责批改，正好符合 Bastani 实验里「只给提示」的思路。

### 苏格拉底式辅导加 Anki

Hacker News 和 Reddit 上的标准组合：

1. 大模型当苏格拉底式导师（Kagi 的 Study 模型、Claude Learning、ChatGPT Study Mode）；
2. 大模型起草闪卡；
3. 导入真正的间隔复习工具（Anki 或 Mochi）；
4. 可选：用 MCP 或 AnkiConnect，让对话里直接插卡。

相关讨论和工具：

- 用 AI 起草闪卡的讨论：<https://news.ycombinator.com/item?id=47063007>
- Show HN: Janus，把 PDF、视频、笔记转成 Anki 或 Mochi 卡片：<https://news.ycombinator.com/item?id=46599896>
- Show HN: Keepmind：<https://news.ycombinator.com/item?id=44491043>
- 用 MCP 直接写入 Anki：<https://news.ycombinator.com/item?id=44022205>

### Readwise 到 Anki 的流水线

- Readwise Reader 里的 Ghostreader 起草卡片，通过 Obsidian 插件同步，再进 Anki：<https://riddle.press/auto-drafting-flashcards/>
- n8n 加 Readwise 加 GPT 加 AnkiConnect 全自动跑：[r/readwise 的指南](https://www.reddit.com/r/readwise/comments/1ic1uwa/guide_how_i_automated_flashcard_creation_with_n8n/)，以及 [r/Anki 上的同款](https://www.reddit.com/r/Anki/comments/1hz2y2r/automated_highlighttoanki_cards_using_readwise/)

评论区常见的提醒：全自动会让卡片质量崩掉，中间要有一步「这条值不值得记」的过滤。

### 用 AI 维护笔记库

- **掌握套件**：让 AI 给一本难书生成全书地图、原子笔记骨架、回忆题、闪卡和日程，但读和写仍然由人来做。<https://www.squaredawaylife.com/posts/how-to-master-hard-books-with-ai-and-obsidian>
- **Karpathy 式 LLM Wiki**：原始材料放在 `raw/` 不动，AI 维护 `wiki/` 里的链接页面。<https://github.com/charlie947/ai-second-brain>；Felipe Sinisterra 讲了自己做研究用的第二大脑：<https://www.felipesinisterra.com/blog/how-i-set-up-my-second-brain-for-research-with-ai>
- r/PKMS 上有人分享怎么在 Obsidian 里用 GPT 真正学进去：<https://www.reddit.com/r/PKMS/comments/1nj4b22/how_ive_been_using_gpt_in_obsidian_to_actually/>
- r/ObsidianMD 上的共识是 Obsidian 当源头、Anki 当复习引擎、单向同步：<https://www.reddit.com/r/ObsidianMD/comments/1vzic42/anyone_using_obsidian_anki_together_for_spaced/>

### linux.do 中文社区常推的东西

| 东西 | 干什么 | 链接 |
| --- | --- | --- |
| Matt 的 `/teach` | 目录当跨会话课程，HTML 课加 `RESOURCES.md` | <https://linux.do/t/topic/2761043> |
| Knowledge Absorber | 长文变结构化笔记（Markdown 加 HTML），带导师模式 | 同上 |
| Anki MCP 加制卡提示词 | 原子卡、HTML 字段、助记 | <https://linux.do/t/topic/1510992> |
| SRSA | 给 agent 自己做 FSRS 复习，不是给人背 | <https://linux.do/t/topic/1803656> |
| Engram | 自托管的 FSRS 闪卡，带 MCP | <https://linux.do/t/topic/2984954> |

其他值得看的帖子：

- `grill-me` 使用心得：<https://linux.do/t/topic/2952622>
- 给 Knowledge Absorber 加导师模式，解决「看完记不住」：<https://linux.do/t/topic/1770345>
- 自己改 skill 加速获取知识：<https://linux.do/t/topic/1494565>
- KnowCraft 介绍：<https://linux.do/t/topic/1403453>

### YouTube 和视觉化

- 「用 ChatGPT 学习」这类长视频仍是主要入口，例如：<https://www.youtube.com/watch?v=qrUImmmxrvg>
- X 上收藏很多的帖子：用 ChatGPT 生成信息图、概念图、时间线（AiWithAyesha，<https://x.com/AiWithAyesha/status/2107435901605548376>）。
- 提醒：视觉材料如果不接上回忆练习，就会变成好看的被动消费。

## 两个有争议的话题

### AI 制卡：省力，还是破坏了「做卡就是学习」

赞成的一方：批量生成、格式统一、MCP 直接写进 Anki。见 [linux.do 的 Anki MCP 流程](https://linux.do/t/topic/1510992)、[Hacker News 上的 MCP 写 Anki](https://news.ycombinator.com/item?id=44022205)、[r/Anki 的制卡效率讨论](https://www.reddit.com/r/Anki/comments/1hov0v9/what_is_the_most_efficient_and_fast_way_to_make/)。

Anki 老用户反复提出的警告：

- AI 常常违反「最小信息原则」，一张卡塞三四个事实；
- 自己做卡本身就是思考（[linux.do 的 Anki 加 AI 讨论](https://linux.do/t/topic/371988)）；
- 有人用 ChatGPT 做卡后发现了错误和编造的内容（[r/Anki 的讨论](https://www.reddit.com/r/Anki/comments/1bncpwy/to_the_people_who_used_chatgpt_to_create_cards/)）。

比较稳的做法：**先学懂，AI 起草，人删改拆小，再进 Anki。**

### 第二大脑的美感 vs 真正的成绩

Notesmakr 说得很直：漂亮的知识图谱不等于记住了。没有间隔复习，第二大脑就是一台精美的重读机器。<https://notesmakr.com/blog/how-to-use-obsidian-for-studying>

## 学习相关的 skill 和项目

按「你要它产出什么」分组。有些项目关注的人不多，仍然列出，因为它们的流程设计值得借鉴和改写。

### 课程工作区：目录就是课程

| 项目 | 过程 | 产物 | 链接 |
| --- | --- | --- | --- |
| mattpocock/skills 的 `teach` | 目标 → 资料 → HTML 短课；优先复用已有组件 | 整套课程目录 | [仓库](https://github.com/mattpocock/skills) · [SKILL.md](https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/teach/SKILL.md) |
| koganei/learn-anything-skill | 自动查资料 → 按基础、进阶、高级、应用分章 | 分级学习路径和分块授课 | [仓库](https://github.com/koganei/learn-anything-skill) |

同一个仓库里，常和 `teach` 一起用的协作类 skill：`grill-me`、`research`、`handoff`、`wait-what`。

### 讲代码

| 项目 | 过程 | 产物 | 链接 |
| --- | --- | --- | --- |
| backnotprop/pstack | `/how` 讲架构，`/why` 找证据，`/teach` 综合讲解，`/bro` 说大白话 | 讲解和图，不建课程 | [仓库](https://github.com/backnotprop/pstack) · [teach](https://www.skills.sh/backnotprop/pstack/teach) |
| sbkriz/feynman-tutor | 你来讲，AI 追问缺口 | 学习者笔记 | [仓库](https://github.com/sbkriz/feynman-tutor) |

### 完整的辅导闭环

| 项目 | 过程 | 产物 | 链接 |
| --- | --- | --- | --- |
| kirilxd/claude-tutor | `/learn` 出计划 → 讲解 → `/quiz` → SM-2 排复习 → 网页面板 | 计划、测验、复习、面板 | [仓库](https://github.com/kirilxd/claude-tutor) |
| mordor-forge/study-skill | 交互学习加 FSRS-6 | 学习会话和复习调度 | [仓库](https://github.com/mordor-forge/study-skill) |
| Bhala-Srinivash/agent-tutor-skill | 讲解 → 举例 → 检查 → 练习；FSRS；可以用你给的材料教 | `~/.learn/` 档案和复习 | [仓库](https://github.com/Bhala-Srinivash/agent-tutor-skill) |
| shauigewhite/learning-tutor | 五种模式，前测和后测，三种教法 | 学习者档案 | [仓库](https://github.com/shauigewhite/learning-tutor) |
| Mohamed-El-Sharqawy/agent-tutor | 辅导加测验，1 到 90 天的复习阶梯，写进 Obsidian | 复习队列 | [仓库](https://github.com/Mohamed-El-Sharqawy/agent-tutor) |

### Anki 和间隔复习制卡

| 项目 | 过程 | 产物 | 链接 |
| --- | --- | --- | --- |
| doasfrancisco/anki-skill | 写代码时提议原子卡 → 你批准 → 通过 AnkiConnect 写入 | Anki 卡片 | [仓库](https://github.com/doasfrancisco/anki-skill) |
| HumphreySun98/Smart-Study-Agent | 概念图、FSRS、用强化学习选题、导出 Anki | 题库、`.apkg`、SQLite | [仓库](https://github.com/HumphreySun98/Smart-Study-Agent) |
| guepardlover77/learn-skill | 材料变学习计划，用 genanki 生成 `.apkg`，加 Obsidian 笔记 | `.apkg`、Markdown、SM-2 表 | [仓库](https://github.com/guepardlover77/learn-skill) |
| Teach Anki | 课上生成多种题型的卡，审完再写入 Anki | 卡片和记录 | [目录页](https://mcpmarket.com/tools/skills/anki-spaced-repetition-tutor) |
| mkrech/anki-course-tutor-mcp-server | MCP 会话加 Anki 调度 | 会话和统计 | [仓库](https://github.com/mkrech/anki-course-tutor-mcp-server) |

### 知识吸收和整理成 wiki

| 项目 | 过程 | 产物 | 链接 |
| --- | --- | --- | --- |
| YuJunZhiXue/StudyAnalysis-Skills（Knowledge Absorber） | 深读链接或文档 → Markdown 加 HTML 结构化笔记，带导师模式 | 结构化笔记和侧栏测验 | [仓库](https://github.com/YuJunZhiXue/StudyAnalysis-Skills) |
| wwwzhouhui/skills_collection | Claude skill 合集，含 Knowledge Absorber 的一个变体 | 多个 skill | [仓库](https://github.com/wwwzhouhui/skills_collection) |
| huifer/Claude-Code-KnowCraft | 本地知识库加 SM-2 加费曼式追问 agent | 笔记、测验、本地库 | [仓库](https://github.com/huifer/Claude-Code-KnowCraft) · [linux.do](https://linux.do/t/topic/1403453) |

### 协作：对齐、对抗和 agent 自己记

| 项目 | 过程 | 产物 | 链接 |
| --- | --- | --- | --- |
| Matt 的 `grill-me` | AI 一直追问，直到设计树里每个分支都有答案 | 澄清后的计划 | [skills](https://github.com/mattpocock/skills) |
| pstack 的 `interrogate` / `arena` / `swarm` | 对抗评审；多方案竞赛；并行汇总 | 盲点报告、合成方案 | [pstack](https://github.com/backnotprop/pstack) |
| cheanus/SRSA | 给 agent 自己做 FSRS 记忆卡，不是给你背单词 | agent 的记忆复习日程 | [仓库](https://github.com/cheanus/SRSA) · [linux.do](https://linux.do/t/topic/1803656) |

### 可以参考结构的成品课程

这些不是 skill，而是已经写好的课程，可以借鉴它们的章节结构：

| 项目 | 结构 | 链接 |
| --- | --- | --- |
| microsoft/ai-agents-for-beginners | 18 课，每课有说明、视频和代码 | [仓库](https://github.com/microsoft/AI-AGENTS-FOR-BEGINNERS) |
| Haozhe-Xing/agent_learning | 按 agent 学习路线分章：RAG、工具、多 agent、评测等 | [仓库](https://github.com/Haozhe-Xing/agent_learning) |
| minicoohei/ai-agent-camp | 几十个模块的课程，加课程清单 | [仓库](https://github.com/minicoohei/ai-agent-camp) |

linux.do 的学习 skill 征集帖里，被推荐最多的是 Matt 的 `teach` 和 Knowledge Absorber。

## 什么时候再加可选项

| 工具 | 值得加的时机 |
| --- | --- |
| Obsidian 和 Anki 同步插件 | 笔记里已经在写问答对，不想两边维护 |
| n8n 等自动化 | 每天的高亮量超过手动审卡的能力，而且愿意维护流水线 |
| Zotero | 主要读论文 |
| Matt 的 `teach` | 一门主题要学几周，需要 MISSION 和逐次积累的课 |
| Knowledge Absorber | 经常要啃长 PDF 和长文 |
| pstack 的 `teach`、`how`、`why` | 学的对象是代码，需要分层讲解 |
| pstack 的 `interrogate`、Matt 的 `grill-me` | 方案对齐、找盲点 |
| SRSA | 想强化的是 agent 的记忆，不是人脑 |
| Multica、Orca | 学完要把东西做出来，交给多个 agent 并行实现 |
| 全本地模型 | 有隐私或离线的硬需求；否则复杂度通常大于收益 |
| 网页面板 | claude-tutor 自带；不是必需 |

Reddit r/ollama 上有人问自己是不是被工具复杂度骗了（<https://www.reddit.com/r/ollama/comments/1sv9bqr/am_i_building_a_feasible_localfirst_ai_study/>），回复的建议很实在：先只做读、问、提建议；要写回笔记库时，先试跑一遍看看会改什么。
