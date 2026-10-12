# Part B — 社区怎么用 AI 学未知领域（实操帖调研）

> 调研时间：2026-10-11（JST）  
> 范围：YouTube / Reddit / X / linux.do / Hacker News / 研究与长文  
> 关键词：learn with ChatGPT/Claude、AI tutor、Anki AI、second brain learning、how I learn with AI  
> 方法：WebSearch + X `search_posts_all` + 关键页抓取。**未使用 Cloud Agent。**

---

## 0. 一句话结论

社区共识几乎一致：**AI 当教练（出题、给提示、找盲点），人当运动员（先做、先回忆、再问）。**  
真正拉开差距的不是模型，而是有没有 **间隔复习（Anki/FSRS）** 和 **自己的材料仓库（笔记库）**。  
第一天学 8 小时却没第二天复习计划 = 典型「三分钟热度」失败模式。

---

## 1. 社区共识（跨平台反复出现）

### 1.1 角色分工

| 角色 | 该做什么 | 不该做什么 |
|------|----------|------------|
| AI | 解释难点、一次一题测验、生成草稿卡、排复习日历、对你的答案打分 | 替你写完作业、先给完整答案、替你读完全文再总结给你背 |
| 人 | 先尝试 / 先默写、自己写原子笔记、审卡、关掉聊天再回忆 | 把「读懂 AI 解释」当成「我会了」 |

出处密集出现于：

- [How to Use AI to Study Without Skipping the Actual Learning](https://www.timtis.com/blog/how-to-use-ai-to-study-without-skipping-the-actual-learning/)（对照实测 ChatGPT Study Mode / Claude Learning / Gemini Guided Learning）
- [Dafi：用自己的课件 grounding](https://www.dafi-ai.com/en/blog/how-to-use-chatgpt-and-claude-to-study)
- [GeniusPal：Claude 七种学法](https://www.geniuspal.app/blog/ai-study/how-to-use-claude-to-study)
- Reddit r/Anki / r/ChatGPT / r/studytips 大量同构回复

### 1.2 「先检索，再解释」是硬规则

几乎所有高赞做法都要求：

1. **关掉 AI，先写回忆**（10 分钟）
2. 对照笔记，只让 AI 补缺口
3. **一次一题**测验
4. 会话结束再做一次 **closed-chat recall**（聊天关掉再默写）

对应学习科学：Roediger & Karpicke 检索练习；Dunlosky 2013 高 utility = practice testing + spaced practice。

### 1.3 Anki / SRS 是「记忆层」标配，不是可选项

HN、Reddit、X、linux.do 几乎同一条线：

> ChatGPT 可以 **像 Anki 一样提问**，但它 **不是** spaced repetition 系统。—— [HN: "I just let chatgpt quiz me anki style"](https://news.ycombinator.com/item?id=44021924)

正确拆法：

- AI：制卡草稿、解释、换问法、苏格拉底对话  
- Anki（或 FSRS 同类）：排程、对抗遗忘曲线  

### 1.4 用自己的材料 grounding，不信参数知识

- 上传课件 / 笔记 / PDF，明确要求「只根据这些材料；不在里面就说不知道」
- linux.do 推 Matt `/teach`：参数知识当不可信，先找高信任资源写进 `RESOURCES.md` 再教  
  → [linux.do 征集帖](https://linux.do/t/topic/2761043) · [mattpocock/skills](https://github.com/mattpocock/skills)

### 1.5 小剂量、多天，而不是一天暴冲

共识节奏（多源合并）：

- 工作日 25–45 分钟一块，周末略长  
- 每块里：**复习旧的 → 学新的 → 短测验**  
- 间隔：1 / 3 / 7 / 14 天回看薄弱点  
- 见 [Personal AI Use：四星期间隔计划 prompt](https://personalaiuse.com/articles/ai-for-learning-skills/)

---

## 2. 争议（两边都有硬证据）

### 2.1 「AI 导师碾压课堂」 vs 「无护栏 ChatGPT 伤长期成绩」

| 证据 | 结论 | 链接 |
|------|------|------|
| Harvard / Kestin et al.，Scientific Reports 2025，物理课定制 AI tutor | 比课堂 active learning **中位学习增益 >2×**，用时更短，动机更高；**长期保持力还在跟进研究** | [Harvard Gazette](https://news.harvard.edu/gazette/story/2025/10/what-if-ai-could-help-students-learn-not-just-do-assignments-for-them/) · [Nature Sci Rep PDF](http://nature.com/articles/s41598-025-97652-6.pdf) |
| Bastani et al.，PNAS 2025，近千人高中数学 | 无护栏 GPT-4：练习分 +48%，**拿走 AI 后考试 −17%**；带护栏的 GPT Tutor 基本消掉伤害 | [PNAS](https://www.pnas.org/doi/10.1073/pnas.2422633122) · [作者 PDF](https://hamsabastani.github.io/education_llm.pdf) |

**社区解读（X / 博客共识）：**  
同一模型，护栏/用法不同 → 结果可以相反。哈佛那条是 **为教学设计的 bot**；PNAS 那条是 **像普通 ChatGPT 一样给答案**。  
X 上也有人同时转这两类结果，例如 [amussis 引用 Harvard](https://x.com/amussis_xyz/status/2106345100271833197) 与 [另一条 RCT「有 tutor 不等于学到」](https://x.com/amussis_xyz/status/2107008632239935998)；[getjotit 摘要「45 天后 ChatGPT 组更差」](https://x.com/getjotit/status/2100400161524482394)。

### 2.2 AI 制卡：省力 vs 破坏「做卡即学习」

- 赞成：批量生成、统一格式、MCP 直写 Anki —— [linux.do Anki MCP 流程](https://linux.do/t/topic/1510992)、[HN MCP→Anki](https://news.ycombinator.com/item?id=44022205)、[r/Anki 制卡帖](https://www.reddit.com/r/Anki/comments/1hov0v9/what_is_the_most_efficient_and_fast_way_to_make/)
- 反对 / 警告（Anki 老兵反复说）：
  - AI 常违反 **minimal information principle**（一张卡塞 3–4 个事实）  
  - 「自己做卡本身就是思考」—— [linux.do Anki+AI 讨论](https://linux.do/t/topic/371988)  
  - 正确姿势：**先学懂 → AI 出草稿 → 人删改原子化 → 再进 Anki**

### 2.3 LLM 对话当 SRS？

HN 直接打脸：「It's an LLM, not an SRS.」同一会话里「偶尔再问一遍」≠ FSRS 排程。见 [HN 44021924](https://news.ycombinator.com/item?id=44021924)。

### 2.4 Second brain 美学 vs 考试/技能成绩

[Notesmakr：Obsidian 学习指南](https://notesmakr.com/blog/how-to-use-obsidian-for-studying) 说得很直：漂亮的 graph ≠ 记住。没有间隔复习，第二大脑就是「精美的重读机器」。

---

## 3. 高赞 / 高信号实操做法

### 3.1 纸笔做题 + 摄像头喂给 ChatGPT（Noah Tye）

- 在纸上做题 → 文档相机拍 → 自定义工具贴进 ChatGPT → 拿反馈（区分誊写错 / 代数错 / 概念错）  
- 推文高互动（约 1 万赞级）：[x.com/noahlt/status/2108675665373589841](https://x.com/noahlt/status/2108675665373589841)  
- 综述：[AGI Hunt 摘要](https://agihunt.info/en/p/1a1234d1520dd91c81de9b50ddd)

**为什么火：** 强制「人先产出」，AI 只批改 —— 完美贴合 Bastani 的护栏哲学。

### 3.2 60 分钟标准会话（多源合成，Timtis 最完整）

| 分钟 | 做什么 | AI |
|------|--------|-----|
| 0–10 | 默写该主题 | 关 |
| 10–25 | 做题 | 关（卡 5 分钟以上才开） |
| 25–40 | 卡点题 | Tutor 模式，一次一个 hint |
| 40–50 | 按笔记出题 | 问并判分 |
| 50–60 | 用自己的话写最难点 | 严格打分，禁止代写 |

来源：[timtis.com](https://www.timtis.com/blog/how-to-use-ai-to-study-without-skipping-the-actual-learning/)

### 3.3 苏格拉底 + 制卡 + Anki（HN / Reddit 标准栈）

1. LLM 当 Socratic tutor（Kagi Study model / Claude Learning / ChatGPT Study Mode）  
2. LLM 出 **草稿** 闪卡  
3. 导入真 SRS（Anki / Mochi）  
4. 可选：MCP / AnkiConnect 让对话中直接插卡  

- [HN: first drafts of flashcards](https://news.ycombinator.com/item?id=47063007)  
- [Show HN: Janus](https://news.ycombinator.com/item?id=46599896)（PDF/视频/笔记 → Anki/Mochi）  
- [Show HN: Keepmind](https://news.ycombinator.com/item?id=44491043)

### 3.4 Readwise → AI → Anki 流水线

- Ghostreader 在 Reader 里草稿卡 → Obsidian 插件同步 → Anki：[riddle.press](https://riddle.press/auto-drafting-flashcards/)  
- n8n + Readwise + GPT + AnkiConnect：[r/readwise 指南](https://www.reddit.com/r/readwise/comments/1ic1uwa/guide_how_i_automated_flashcard_creation_with_n8n/) · [r/Anki 同款](https://www.reddit.com/r/Anki/comments/1hz2y2r/automated_highlighttoanki_cards_using_readwise/)

评论区常见提醒：全自动 = 卡片质量崩；中间要有「是否值得记」的过滤。

### 3.5 Obsidian mastery kit / Karpathy-style wiki

- AI 生成「掌握套件」：全书地图、原子笔记 stub、回忆题、闪卡、日程 —— **人仍负责读与写**  
  → [Squared Away Life](https://www.squaredawaylife.com/posts/how-to-master-hard-books-with-ai-and-obsidian)
- Karpathy LLM Wiki：`raw/` 不动，`wiki/` 由 AI 维护链接页  
  → [charlie947/ai-second-brain](https://github.com/charlie947/ai-second-brain) · [Felipe Sinisterra 研究第二脑](https://www.felipesinisterra.com/blog/how-i-set-up-my-second-brain-for-research-with-ai)

### 3.6 linux.do 中文圈高频推荐

| 东西 | 干什么 | 链接 |
|------|--------|------|
| Matt `/teach` | 目录当跨会话课程，HTML 课 + RESOURCES.md | [topic/2761043](https://linux.do/t/topic/2761043) |
| Knowledge Absorber | 长文 → 知识晶体 (MD+HTML) + 导师模式 | 同帖 |
| Anki MCP + 制卡提示词 | 原子卡、HTML 字段、助记 | [topic/1510992](https://linux.do/t/topic/1510992) |
| SRSA | **给 Agent 自己**做 FSRS 复习（不是给人背） | [topic/1803656](https://linux.do/t/topic/1803656) |
| Engram | 自托管 FSRS 闪卡 + MCP | [topic/2984954](https://linux.do/t/topic/2984954) |

### 3.7 厂商「Tutor Mode」三件套（2025 中齐发）

| 产品 | 强项 | 弱点 |
|------|------|------|
| ChatGPT Study Mode | 先摸水平、分步、知识检查 | 系统指令偶发漂移 |
| Claude Learning | 苏格拉底、顶回假设；Code 有 Learning style | 感觉慢，容易被关掉 |
| Gemini Guided Learning | 图、YouTube、闪卡 | 容易滑向被动看 |

来源：[timtis 对照表](https://www.timtis.com/blog/how-to-use-ai-to-study-without-skipping-the-actual-learning/)

### 3.8 YouTube / 视觉向

- 「How To Use ChatGPT For Studying」类长视频仍是入口流量：[示例](https://www.youtube.com/watch?v=qrUImmmxrvg)  
- X 高 bookmark 帖：用 ChatGPT 出信息图/概念图/时间线 —— [AiWithAyesha](https://x.com/AiWithAyesha/status/2107435901605548376)（约 280 赞 / 268 bookmark）  
- 警告：视觉材料若不接 recall，就会变成「好看的被动消费」。

---

## 4. 失败模式（「三分钟热度」解剖）

社区与研究反复点名的坑：

### 4.1 流利感幻觉（illusion of fluency）

读完 AI 清晰讲解 → 当下觉得懂了 → **第二天早上什么都不剩**。  
Timtis 实测：lazy「粘贴→抄答案」会话「感觉高效，次日几乎零残留」。

### 4.2 无 SRS 的「学习系统」

- 只建 Obsidian 图谱、不排复习  
- 只用 ChatGPT「再问一遍」当复习  
- 结果：第一周很猛，第三周牌组/笔记堆死、再也不开  

### 4.3 一天 8 小时 binge

违反间隔效应。Dunlosky：cramming 赢当场、输一周后。  
健康节奏：短会话 × 多天 × Anki 每日 overdue。

### 4.4 AI 当拐杖（Bastani「crutch」）

练习时有 AI → 分很高；考试/独立任务 → 比从未用过 AI 的人还差。  
警告信号（Timtis）：

- 关聊天就解不出同类题  
- 会话结束只有整洁答案、没有草稿  
- 每次从粘贴题目开始  
- 笔记全是未读材料的 AI 摘要  
- 考前自信爆棚、考场空白  

### 4.5 自动制卡洪水

批量导入未审的 AI 卡 → 复习队列爆炸 → 弃坑。  
Anki 社区口诀：**宁少勿滥；一张一事；人必须过目。**

### 4.6 Tutor 模式一键关掉

感觉慢 → 切回普通 Chat → 又变答案机。护栏是意志力问题，不是功能问题。

### 4.7 工具栈过重

Obsidian + 12 插件 + n8n + 本地 LLM + 双向同步……建系统本身变成项目，学习对象被挤掉。  
r/ollama 有人自问「是不是被工具复杂度骗了」：[帖子](https://www.reddit.com/r/ollama/comments/1sv9bqr/am_i_building_a_feasible_localfirst_ai_study/) —— 回复建议：先只做读/问/提案，写回 vault 要 dry-run。

---

## 5. 必需品 / 可选 清单（社区实际在用的栈）

按「学习流水线」分层，而不是按品牌。

### 5.1 总览

| 层级 | 必需？ | 干什么 | 社区常用选项 |
|------|--------|--------|----------------|
| A. 阅读 / 捕获 | **强推荐** | 存文章/论文/视频文字，高亮 | Readwise Reader、**Readeck**（自托管）、浏览器稍后读、Zotero（论文） |
| B. 第二大脑 / 笔记库 | **强推荐**（要跨周学） | 原子笔记、链接、课程状态 | **Obsidian**、Logseq；Matt teach 工作区目录；Karpathy `raw/`+`wiki/` |
| C. AI 导师 | **必需** | 解释、苏格拉底、出题、打分 | ChatGPT（Study Mode）、Claude（Learning）、Gemini Guided；本机 Coding agent 的 teach/how |
| D. 间隔复习 | **必需**（要抗遗忘） | 排程复习 | **Anki**（+AnkiConnect）、Mochi、Obsidian Spaced Repetition 插件、Engram |
| E. 制卡桥 | 可选→半必需 | 高亮/笔记 → 草稿卡 | Ghostreader、Chat→Anki 扩展、Anki MCP、n8n 流水线、pstack/Matt 类 skill |
| F. Agent 编排 | 可选 | 拆章节、并行调研、对抗评审 | Matt teach / grill-me；pstack arena/interrogate；Multica Squad / Orca（执行向）；本机 Claude Code skills |
| G. 语音 / 纸笔外设 | 可选 | 降低摩擦 | 文档相机（Noah 流）、Voice mode 口语、手写板 |

### 5.2 必需品（最小可行学习系统）

三件套就够起步，社区「能坚持三个月」的人大多没超过这个：

1. **一个 AI 聊天（开 Tutor/Learning 模式）**  
2. **一个 SRS（几乎总是 Anki）**  
3. **一个放材料的地方**（哪怕先是一个文件夹 + Markdown；Obsidian 是最常见升级）

没有第 2 件 = 三分钟热度高危。  
没有第 3 件 = 每次对话从零解释背景，无法跨会话累积。

### 5.3 强烈推荐（一周内加上）

| 件 | 理由 |
|----|------|
| Read-later（Readwise / Readeck / 同类） | 未知领域信息流太碎；先捕获再消化 |
| AnkiConnect 或 MCP | 把「对话里冒出的难点」变成卡的摩擦降到最低 |
| Tutor 模式固定开着 | 对抗「答案机」默认 |

Readeck 定位：自托管稍后读 + 高亮 + 视频字幕，**不是** SRS —— [readeck.org](https://readeck.org/)

### 5.4 可选（有明确痛点再上）

| 件 | 何时值得 |
|----|----------|
| Obsidian ↔ Anki 同步插件 | 笔记里已经在写 Q::A，不想双处维护 |
| n8n / Make 自动化 | 日更高亮量 > 手动审卡能力，且愿意维护管道 |
| Zotero | 主战场是论文 |
| Matt `/teach` 工作区 | 一门主题要学数周，需要 MISSION.md / 课次累积 |
| Knowledge Absorber | 经常吞长 PDF/长文，要「知识晶体」 |
| pstack `teach`/`how`/`why` | 对象是**代码**，要分层讲解（≠ Matt 课程） |
| pstack `interrogate` / Matt `grill-me` | 方案对齐、找盲点（协作共赢，不是背诵） |
| SRSA | 你要强化的是 **Agent 记忆**，不是人脑 |
| Multica / Orca | 学习产出要变成多 agent **执行**（实现/对比），不是讨论本身 |
| 本地 LLM 全栈 | 隐私/离线刚需；否则复杂度常 > 收益 |

### 5.5 怎么串起来（推荐拓扑）

```
[信息流]
  YouTube / 论文 / 博客 / X
       │ 稍后读 / 下载
       ▼
[阅读器] Readeck / Readwise / Zotero
       │ 高亮、摘录、（可选）AI 草稿卡
       ▼
[笔记库] Obsidian 或 teach 工作区
       │ 自己的话写原子笔记；链到来源
       │
       ├──────────────► [AI 导师] Claude/ChatGPT Study
       │                  苏格拉底 / 出题 / 打分 / 解释卡点
       │                       │
       │                       ▼ 审过的原子卡
       └──────────────► [Anki] 每日复习（抗遗忘）
                              │
                              └─ overdue 回灌到下次 AI 会话的「薄弱点」
```

**Agent 编排插在哪：**

- **学之前：** grill-me / interrogate —— 把大 scope 拆成章节与验收标准  
- **学之中：** Matt teach / 分章 agent —— 每章一次短课 + 测验  
- **学之后：** arena —— 同一练习多解对比；或 Orca/Multica 把「已理解的设计」变成并行实现  

### 5.6 针对「大 scope → 章节 + 和 AI 共赢」的串法

社区可复用模板（合成，非单一帖）：

1. **定范围**：人用一句话目标 + 截止日期；AI 输出章节大纲（必须可验收）  
2. **grill-me / interrogate**：逼出假设与盲点，改大纲  
3. **每章独立小工作区**（Matt teach 风格）：`MISSION.md`、资源、课次 HTML、学习记录  
4. **每章结束产物**：  
   - 5–15 张 **人审过的** Anki 卡  
   - 1 页自己的话总结（可进 Obsidian）  
   - 3 道「关 AI 能做」的练习  
5. **每日 Anki**；每周用 AI 只复习「又忘的卡」做二次解释  
6. **项目落地**（可选）：用编码 agent 把该章变成可运行 demo —— 这才是「共赢」而不是「陪聊」

### 5.7 反模式栈（看着全，必死）

- 同时开 3 个笔记软件 + 2 个 SRS + 全自动制卡且不审  
- 只有 second brain、没有每日 Anki  
- 只有 ChatGPT，没有材料库、没有间隔  
- 第一天装 20 个 skill，零章节验收标准  

---

## 6. 平台信号速览

| 平台 | 气氛 | 代表性链接 |
|------|------|------------|
| **Reddit** r/Anki | 制卡质量洁癖；AI 草稿 OK，滥导不行 | [制卡效率](https://www.reddit.com/r/Anki/comments/1hov0v9/what_is_the_most_efficient_and_fast_way_to_make/) · [AI 制卡幻觉](https://www.reddit.com/r/Anki/comments/1bncpwy/to_the_people_who_used_chatgpt_to_create_cards/) |
| **Reddit** r/ObsidianMD / r/PKMS | Obsidian=源；Anki=复习引擎；单向同步 | [Obsidian+Anki](https://www.reddit.com/r/ObsidianMD/comments/1vzic42/anyone_using_obsidian_anki_together_for_spaced/) · [GPT in Obsidian](https://www.reddit.com/r/PKMS/comments/1nj4b22/how_ive_been_using_gpt_in_obsidian_to_actually/) |
| **HN** | SRS 原理洁癖；Show HN 工具多 | [Janus](https://news.ycombinator.com/item?id=46599896) · [LLM≠SRS](https://news.ycombinator.com/item?id=44021924) |
| **linux.do** | skill/MCP 实战；Matt teach + Absorber + Anki MCP | [2761043](https://linux.do/t/topic/2761043) · [1510992](https://linux.do/t/topic/1510992) |
| **X** | 病毒式个人 workflow + 产品软广混杂；筛「纸笔+反馈」类 | [Noah Tye](https://x.com/noahlt/status/2108675665373589841) · [Nature/Harvard 传播](https://x.com/burkov/status/2104598517356339418) |
| **YouTube** | 入门教程多、深度系统少；适合当引流再回文字系统 | [ChatGPT studying guide](https://www.youtube.com/watch?v=qrUImmmxrvg) |

---

## 7. 可直接抄的「反三分钟热度」检查表

每天（5–20 分钟也行）：

- [ ] Anki overdue 清完（或明确跳过原因）  
- [ ] 至少一个「关 AI 默写/做题」片段  

每学一章：

- [ ] 有验收标准（能解释 / 能做题 / 能教别人）  
- [ ] ≤20 张新卡且已人工删改  
- [ ] 来源记在笔记里（能回溯）  

每周：

- [ ] 回看「又忘的卡」主题，只开 AI 补洞  
- [ ] 砍掉不用的工具/插件一个（防栈膨胀）  

---

## 8. 与 Part A / skill 调研的接口

| 你已有 / 已看过 | 在本流水线中的位置 |
|-----------------|-------------------|
| pstack `teach` / `how` / `why` / `bro` | **C 层**：代码对象的即时讲解（≠ 跨周课程） |
| pstack `interrogate` / `arena` | **F 层**：盲点与多方案 |
| Matt `/teach` | **B+C**：跨会话课程工作区 |
| Matt `grill-me` | **F**：人对齐大纲 |
| Knowledge Absorber | **A→B**：长文晶体化 |
| Anki + MCP | **D+E** |
| Multica Squad / Orca | **F 执行侧**：学完后的实现与派活，不是记忆层 |

---

## 9. 源列表（本调研点击过或检索命中的高信号源）

**长文 / 研究**

- https://www.timtis.com/blog/how-to-use-ai-to-study-without-skipping-the-actual-learning/  
- https://www.pnas.org/doi/10.1073/pnas.2422633122  
- https://hamsabastani.github.io/education_llm.pdf  
- https://news.harvard.edu/gazette/story/2025/10/what-if-ai-could-help-students-learn-not-just-do-assignments-for-them/  
- https://www.dafi-ai.com/en/blog/how-to-use-chatgpt-and-claude-to-study  
- https://www.geniuspal.app/blog/ai-study/how-to-use-claude-to-study  
- https://personalaiuse.com/articles/ai-for-learning-skills/  
- https://partnerinai.com/blogs/best-way-to-learn-with-chatgpt-a-study-system-that-sticks  
- https://notesmakr.com/blog/how-to-use-obsidian-for-studying  
- https://www.squaredawaylife.com/posts/how-to-master-hard-books-with-ai-and-obsidian  
- https://www.felipesinisterra.com/blog/how-i-set-up-my-second-brain-for-research-with-ai  
- https://riddle.press/auto-drafting-flashcards/  

**论坛**

- https://linux.do/t/topic/2761043  
- https://linux.do/t/topic/371988  
- https://linux.do/t/topic/1510992  
- https://linux.do/t/topic/1803656  
- https://linux.do/t/topic/2984954  
- https://news.ycombinator.com/item?id=44021924  
- https://news.ycombinator.com/item?id=47063007  
- https://news.ycombinator.com/item?id=46599896  
- https://news.ycombinator.com/item?id=44491043  
- https://news.ycombinator.com/item?id=44022205  
- https://www.reddit.com/r/Anki/comments/1hov0v9/what_is_the_most_efficient_and_fast_way_to_make/  
- https://www.reddit.com/r/Anki/comments/1hz2y2r/automated_highlighttoanki_cards_using_readwise/  
- https://www.reddit.com/r/readwise/comments/1ic1uwa/guide_how_i_automated_flashcard_creation_with_n8n/  
- https://www.reddit.com/r/ObsidianMD/comments/1vzic42/anyone_using_obsidian_anki_together_for_spaced/  
- https://www.reddit.com/r/PKMS/comments/1nj4b22/how_ive_been_using_gpt_in_obsidian_to_actually/  

**X**

- https://x.com/noahlt/status/2108675665373589841  
- https://x.com/burkov/status/2104598517356339418  
- https://x.com/AiWithAyesha/status/2107435901605548376  
- https://x.com/amussis_xyz/status/2106345100271833197  
- https://x.com/amussis_xyz/status/2107008632239935998  
- https://x.com/getjotit/status/2100400161524482394  

**工具 / 仓库**

- https://github.com/mattpocock/skills  
- https://github.com/charlie947/ai-second-brain  
- https://readeck.org/  
- https://github.com/lukmay/simple-anki-sync  

---

## 10. 调研局限

- X 搜索噪声大（产品软广多），已优先保留有具体 workflow 或指向 RCT 的帖。  
- YouTube 以检索摘要为主，未逐条看完长视频逐字稿。  
- 「高赞」跨平台不可比（Reddit 分、X 赞、linux.do 回复是不同尺度）；本文按 **方法可复现性** 加权，不以单一点赞数为唯一排序。  
