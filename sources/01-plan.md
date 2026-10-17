# 摸底与规划

这一类来源回答"从哪里开始学、按什么顺序学"。共同的做法是先测出学习者已经会什么，再把目标拆成一张有前置关系的地图，只教刚好够得着的部分，掌握了才往下走。读这一类时，重点看它们怎么摸底、地图用什么格式、什么条件算"过关"。最后几条是成品课程的目录结构，可以当作排章节的模板。

本类共 20 条，按评分从高到低排列。

## [How I Use AI to Learn Things（摸底→规划→授课三段式）](https://www.youtube.com/watch?v=kzcI5F4tGiU&t=313s)

- 作者：Eero Alvar（YouTube）
- 方式：摸底、依赖图、逐点授课、随堂测
- 产物：Obsidian 学习日志（md）、Mermaid 图、SVG 配图、选择题
- 工具：pi 框架、Obsidian、子 agent（需 tmux）；是否需要 MCP：不需要
- 依赖：依赖 pi，思路通用
- 评分：★★★★★（5/5）
- 原文存档：[视频字幕全文](raw/transcripts/kzcI5F4tGiU.md)

**做法。**先用分级选择题对每条前置知识线做二分查找，同时找到"答对的下限"和"答错的上限"才算摸清边界（[5:13](https://www.youtube.com/watch?v=kzcI5F4tGiU&t=313s)）。然后派一个研究子 agent 摸清领域，画一张 Mermaid 依赖图，根节点是无条件成立的事实，终点是你的目标，你确认后才开讲（[6:07](https://www.youtube.com/watch?v=kzcI5F4tGiU&t=367s)）。授课时一次只走一个节点，按"为什么需要它、讲清或推导、连到已学节点、当场一道题"四步走（[6:56](https://www.youtube.com/watch?v=kzcI5F4tGiU&t=416s)）。演示用的是微分形式，整节课实时写进 Obsidian 笔记（[8:01](https://www.youtube.com/watch?v=kzcI5F4tGiU&t=481s)）。

**可借鉴。**二分查找式摸底和"画图逼 AI 想清楚"两招都不依赖 pi，可以直接写进任何 skill。评论区指出的代价也要记住：很费 token，完全零基础时摸底会全错。

## [amosblomqvist/learn（Eero 视频背后的仓库）](https://github.com/amosblomqvist/learn)

- 作者：Amos Blomqvist（GitHub）
- 方式：摸底、依赖图、逐点授课、随堂测
- 产物：md 日志、选择题、SVG/Mermaid 图
- 工具：pi 框架、Obsidian、tmux 子 agent；是否需要 MCP：不需要
- 依赖：依赖 pi
- 评分：★★★★★（5/5）
- 原文存档：[原文](raw/web/01-plan/github-amosblomqvist-learn.md)

**做法。**仓库本身就是一个 pi 配置目录，核心在 `skills/teach/SKILL.md`，写明了摸底规则、依赖图规则和逐节点授课循环。扩展里有 `quiz`（带标准答案、即时判对错的选择题）、`ask-user-question`（弹窗提问）、`md-log`（把一个 md 文件绑定到会话，所有输出实时写进去）。另有 `researcher`、`svg-maker`、`mermaid-maker` 三个子 agent，画图的子 agent 会亲自看一眼渲染结果。约 3.6k 星。

**可借鉴。**teach/SKILL.md 里的两条原则值得原样借：先讲"以后不会被推翻"的无条件事实；每一步都问"我自己怎么可能发现它"。md-log 的思路可以用普通 md 文件代替。

## [Justin Skycak：把一年的课压缩到更短的 7 步](https://x.com/justinskycak/status/2074212787690106923)

- 作者：Justin Skycak（Math Academy）（X）
- 方式：摸底、知识图谱、掌握放行、间隔复习
- 产物：个人知识画像、练习
- 工具：Math Academy（可脱离）；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★★★（5/5）
- 原文存档：[帖子全文](raw/x/2074212787690106923.md)

**做法。**他列了 7 步：先测出学生已经会什么，叠到知识图谱上得到个人画像；只教前置已掌握的"知识前沿"；最小剂量讲解后马上练习；严格执行掌握才放行，卡住就转到平行路线；用间隔重复和闭卷限时小测复习；用学新东西顺带复习旧东西。帖子约 1.4k 赞、1.4k 收藏，他在回复里说这套适用于任何层级分明的领域。

**可借鉴。**这是把一份知识点清单变成学习顺序最硬的规则集，"只学前沿、掌握才放行、卡住走平行路线、新课顺带复习旧点"可以直接写进 map.md。

## [How Math Academy creates its knowledge graph](https://justinmath.com/how-math-academy-creates-its-knowledge-graph/)

- 作者：Justin Skycak（博客）
- 方式：依赖图、掌握放行
- 产物：知识图谱
- 工具：无；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★★☆（4/5）
- 原文存档：[原文](raw/web/01-plan/justinmath-how-math-academy-creates-its-knowledge-graph.md)

**做法。**文章讲 Math Academy 怎么手工搭知识图谱：每个知识点标出前置关系和"包含"关系，学新点时顺带练到被包含的旧点。前置没掌握的点不会推给学生。

**可借鉴。**给清单里每个知识点标前置和类型（概念、机制、技能、记忆），就是一个简化版的 map.md。

## [The Math Academy Way（PDF）](https://www.justinmath.com/files/the-math-academy-way.pdf)

- 作者：Justin Skycak（PDF 书）
- 方式：掌握放行、间隔复习、检索练习、交错
- 产物：无
- 工具：无；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★★☆（4/5）
- 原文存档：[原文](raw/web/01-plan/justinmath-files-the-math-academy-way-pdf.md)

**做法。**一整本讲 Math Academy 教学法的书，覆盖知识图谱、掌握学习、间隔重复、交错练习和"用新课复习旧课"的设计。X 上有人把这本书丢给模型，一句话生成了带技能节点和依赖的交互学习页面。

**可借鉴。**可以整本喂给 AI 当"教学法规范"，让它按这套原则排课。

## [lowwwbank/anything-to-course](https://github.com/lowwwbank/anything-to-course)

- 作者：lowwwbank（GitHub）
- 方式：规划、检索练习、间隔复习、导师模式
- 产物：课程目录 md、答案目录、复习日程
- 工具：任意读 SKILL.md 的 agent；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★★☆（4/5）
- 原文存档：[原文](raw/web/01-plan/github-lowwwbank-anything-to-course.md)

**做法。**把资料先压成"可观察的能力、缺口和前置"，再拆成模块和课节，答案放在单独目录里物理隔离。每节课固定走"先尝试、讲原理、看例题、做对比、练习、检查点"。学习时进入导师模式，并生成 +1 天、+7 天、+30 天的复习日程。

**可借鉴。**课节模板和"答案物理隔离"都可以照搬；fork 后只要改 course-blueprint 和 practice-design 两个文件就能换领域。

## [sosplit/adaptive-learning-course（中文）](https://github.com/sosplit/adaptive-learning-course)

- 作者：sosplit（GitHub）
- 方式：访谈、摸底、方案确认、逐课练习
- 产物：本地网页课、JSON 答卷、学习档案
- 工具：任意 agent（可选本地 Python 服务）；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★★☆（4/5）
- 原文存档：[原文](raw/web/01-plan/github-sosplit-adaptive-learning-course.md)

**做法。**先访谈学习内容、目标、背景、时间和偏好，确认后才出定制摸底卷。根据摸底结果生成课程方案，必须由学习者确认才开课。每次只生成当前一节，交卷后逐题批阅，掌握了进下一节，没掌握回到本节。

**可借鉴。**"先访谈再出卷、方案必须确认、每次只生成一节"三条约束很实用，能防止 AI 一口气生成一整套没人看的课。

## [sai-7i/daxue-zhidao 大学之道（中文）](https://github.com/sai-7i/daxue-zhidao)

- 作者：sai-7i（GitHub）
- 方式：技术地图、单元制授课、掌握验证
- 产物：技术地图、课程进度 md
- 工具：6 种宿主（Claude Code、Codex 等）；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★★☆（4/5）
- 原文存档：[原文](raw/web/01-plan/github-sai-7i-daxue-zhidao.md)

**做法。**只能由用户手动调用。先联网调研技术生态，建一张可追溯来源的技术地图，再按你的真实目标逐单元讲解、评估、推进。仓库分两个分支：`guide` 负责教，`map` 只做路线规划不教内容。

**可借鉴。**把"规划"和"授课"拆成两个独立 skill，规划可以单独用。

## [zifengyuan6-star/xuexi-learning-skill（中文）](https://github.com/zifengyuan6-star/xuexi-learning-skill)

- 作者：zifengyuan6-star（GitHub）
- 方式：掌握学习、检查站、补充课、复习提醒
- 产物：主题文件夹、每课 md、进度.md、错题和遗漏记录
- 工具：CLAUDE.md（任意 agent）；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★★☆（4/5）
- 原文存档：[原文](raw/web/01-plan/github-zifengyuan6-star-xuexi-learning-skill.md)

**做法。**基于"2 Sigma"和掌握学习：每次只推进一小节，课后在检查站提问，按完全掌握、基本掌握、部分理解、尚未理解四档决定下一步。部分理解就生成补充课，尚未理解就拆卡点重讲。Plus 版另外记录错题和遗漏、安排复习，还能回答"多久没学这个主题了"。约 110 星。

**可借鉴。**四档掌握判定加"补充课"的分支设计很清楚，可以直接作为掌握放行的规则。

## [Justin Skycak：认知举重的三条原则](https://x.com/justinskycak/status/2070136427422314529)

- 作者：Justin Skycak（X）
- 方式：检索练习、掌握放行、间隔复习
- 产物：无
- 工具：无；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★☆☆（3/5）
- 原文存档：[帖子全文](raw/x/2070136427422314529.md)

**做法。**他把学习比作举重，三条原则是检索练习、掌握学习和间隔重复，对应"做够次数、用对重量、保持规律"。帖子很短，只是把三个概念并列。

**可借鉴。**适合当作整套方法的口号，放在 skill 开头提醒自己。

## [X @raphaeltraviss：一句话生成"技能节点 + 依赖"的学习系统](https://x.com/raphaeltraviss/status/2107836939218952281)

- 作者：raphaeltraviss（X）
- 方式：依赖图、交互探索
- 产物：单文件 HTML 学习页
- 工具：任意能写 HTML 的模型；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★☆☆（3/5）
- 原文存档：[帖子全文](raw/x/2107836939218952281.md)

**做法。**他说自己没给任何上下文，只说想学古典艺术，让模型读《The Math Academy Way》，生成一个带技能节点、节点间依赖和练习的学习系统，模型一次就做成了交互 HTML 页面。

**可借鉴。**把教学法 PDF 当提示词的一部分，比自己写一长串规则更省事。

## [koganei/learn-anything-skill](https://github.com/koganei/learn-anything-skill)

- 作者：koganei（GitHub）
- 方式：规划、讲授
- 产物：分级学习路径（md）
- 工具：Claude Code skill；是否需要 MCP：不需要
- 依赖：依赖 Claude Code，可移植
- 评分：★★★☆☆（3/5）
- 原文存档：[原文](raw/web/01-plan/github-koganei-learn-anything-skill.md)

**做法。**先自动调研，再把主题拆成编号路径：01–05 基础，06–09 进阶，10–11 高级，12–17 应用案例，然后分块授课。星数很少，但路径编号的做法很清楚。

**可借鉴。**"按基础、进阶、高级、应用分段编号"是一种简单好用的地图格式。

## [Sheriaties/adaptive-learning-skill（中文）](https://github.com/Sheriaties/adaptive-learning-skill)

- 作者：Sheriaties（GitHub）
- 方式：分层前置、递归学习、理解验证
- 产物：Obsidian 概念笔记、MOC 学习地图
- 工具：Claude Code / OpenClaw / Hermes，Obsidian；是否需要 MCP：不需要
- 依赖：依赖 Obsidian 目录结构
- 评分：★★★☆☆（3/5）
- 原文存档：[原文](raw/web/01-plan/github-sheriaties-adaptive-learning-skill.md)

**做法。**你说想搞懂 X，它先找出理解 X 之前必须懂的概念，按依赖分 2–4 层列出。每个前置你可以选详细学、简略了解、跳过或已掌握；选"详细学"就把它当新目标递归走一遍。每个概念先讲、再答疑、最后小测，通过才算学会，状态写进笔记的 `understanding:` 字段并用颜色标出。

**可借鉴。**"每个前置让学习者自己选深浅"和"递归到底再回来"很适合清单里依赖很深的知识点。

## [SugarMGP/study.skill 学习.skill（中文）](https://github.com/SugarMGP/study.skill)

- 作者：SugarMGP（GitHub）
- 方式：锚定目标、调研资料、生成课程、陪学、间隔复习
- 产物：课程目录、讲义、互动练习、复习排期
- 工具：任意 agent，本地课程播放器；是否需要 MCP：不需要
- 依赖：通用（播放器可选）
- 评分：★★★☆☆（3/5）
- 原文存档：[原文](raw/web/01-plan/github-sugarmgp-study-skill.md)

**做法。**五个阶段：先问清范围、基础、时间和材料约束；再查官方文档、源码和权威教程；然后生成课程概览和小节讲义；学习时用本地播放器展示讲义、图表和练习；最后按间隔重复安排复习，每天开课先查到期项。分速成导览、系统精讲、面试冲刺、考试备考几种模式。

**可借鉴。**"目标大就先画领域地图让你选方向，目标小就走快速教学"这个分流很实用。

## [X @gabriel1：现在可以自上而下学任何东西](https://x.com/gabriel1/status/2026945947352363127)

- 作者：gabriel1（X）
- 方式：观点、规划
- 产物：无
- 工具：无；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★☆☆（3/5）
- 原文存档：[帖子全文](raw/x/2026945947352363127.md)

**做法。**他说历史上学习最难的是知道该学什么、去哪找信息，难到我们让每个人读二十多年书。有了聊天模型，可以自上而下、有确定性地学任何东西。约 800 赞。

**可借鉴。**支持"先让 AI 给地图，再按需下钻"的做法，但要配合本目录里关于"AI 地图会漏分支"的提醒一起看。

## [X @nilslang：通用 AI 导师可行的前提](https://x.com/nilslang/status/2087671103208464586)

- 作者：nilslang（X）
- 方式：观点
- 产物：无
- 工具：无；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★☆☆☆（2/5）
- 原文存档：[帖子全文](raw/x/2087671103208464586.md)

**做法。**他认为通用 AI 导师能做成，前提是背后有足够的知识库和按学科设计的教学结构，比如 Coursera 这样有大量课程设计的平台。帖子只给了观点，没有具体做法。

**可借鉴。**提醒自己：没有"按学科设计的结构"，AI 导师很容易变成随问随答。

## [malberich/skill-tutor](https://github.com/malberich/skill-tutor)

- 作者：malberich（GitHub）
- 方式：摸底、规划、间隔复习、交错
- 产物：学习路径
- 工具：Claude Code 或 Claude.ai skill；是否需要 MCP：不需要
- 依赖：依赖 Claude，可移植
- 评分：★★☆☆☆（2/5）
- 原文存档：[原文](raw/web/01-plan/github-malberich-skill-tutor.md)

**做法。**把任意一个 Claude skill 或领域变成给人学的路径：先诊断你会什么，找出缺口，按起点定路径，再逐个链接讲内容，配合间隔复习和交错挑战。星数很少。

**可借鉴。**"把一个 agent skill 反过来当成人的学习目标"是个有意思的角度。

## [microsoft/ai-agents-for-beginners（课程结构参考）](https://github.com/microsoft/AI-AGENTS-FOR-BEGINNERS)

- 作者：Microsoft（GitHub）
- 方式：课程结构
- 产物：每课 README、视频、代码
- 工具：无；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★☆☆☆（2/5）
- 原文存档：[原文](raw/web/01-plan/github-microsoft-ai-agents-for-beginners.md)

**做法。**18 节课，每节课一个目录，里面有 README、视频和代码示例。它不是学习方法，而是一份结构清楚的成品课程。

**可借鉴。**想让 AI 帮你排章节时，可以把这种"每课一目录"的结构当模板。

## [Haozhe-Xing/agent_learning（课程结构参考）](https://github.com/Haozhe-Xing/agent_learning)

- 作者：Haozhe-Xing（GitHub）
- 方式：课程结构
- 产物：分章 md
- 工具：无；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★☆☆☆（2/5）
- 原文存档：[原文](raw/web/01-plan/github-haozhe-xing-agent-learning.md)

**做法。**一份 agent 学习路线图，按 RAG、工具、多 agent、评测等主题分章。属于内容型仓库，不涉及学习方法。

**可借鉴。**可以参考它怎么把一个大领域切成章节。

## [minicoohei/ai-agent-camp（课程结构参考）](https://github.com/minicoohei/ai-agent-camp)

- 作者：minicoohei（GitHub）
- 方式：课程结构
- 产物：几十个模块、lessons 清单
- 工具：无；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★☆☆☆（2/5）
- 原文存档：[原文](raw/web/01-plan/github-minicoohei-ai-agent-camp.md)

**做法。**几十个模块组成的课程，带一份 lessons 清单文件。和上一条一样，是成品课程而不是方法。

**可借鉴。**"用一个清单文件描述全部课节"的做法可以借来管理自己的 map.md。
