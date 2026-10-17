# 卡片与间隔复习

这一类来源都和"学完之后怎么不忘"有关：间隔复习算法、Anki 和 AI 之间的桥（多数需要 MCP 或 AnkiConnect）、制卡原则，以及大量关于"该不该让 AI 做卡"的讨论。证据最硬的结论是：AI 只出初稿，人来审；先测再做卡，只给答错的做卡；每天新卡要设上限。

本类共 64 条，按评分从高到低排列。

## [Memory Machines：LLM 能从读者高亮里做出耐用的闪卡吗](https://memory-machines.com/report/)

- 作者：Andy Matuschak 等（研究报告）
- 方式：评测 AI 制卡
- 产物：报告、数据集、评测场
- 工具：无；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★★★（5/5）
- 原文存档：[原文](raw/web/04-cards/memory-machines-report.md)

**做法。**用读者在书里的高亮让多个模型生成闪卡，再由有经验的人评审。结论是相当比例（约 36%）的 AI 卡不可用，常见问题是考了不重要的细节、措辞含糊、离开上下文就看不懂。报告附带数据集和一个让模型比拼制卡的评测场。

**可借鉴。**如果要让 AI 制卡，至少要有人工审核这一步，并且把"三个月后还看得懂吗"作为审核标准。

## [Andy Matuschak：丢掉 1/3 AI 卡的成本比自己写 2/3 还高](https://x.com/andy_matuschak/status/2046640847161262574)

- 作者：Andy Matuschak（X）
- 方式：观点、制卡
- 产物：无
- 工具：无；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★★★（5/5）
- 原文存档：[帖子全文](raw/x/2046640847161262574.md)

**做法。**他说，审 AI 卡时丢掉三分之一带来的评估、不确定和烦躁成本，比他自己把另外三分之二写出来还高。评论区有人说生成的卡"看着很好，几个月后又困惑又烦"；有人举了一位数学家 6 年 2.5 万张卡、一半新卡是把旧卡再抽象的例子。共识是 LLM 只出初稿、人来迭代。

**可借鉴。**审卡本身也有成本，所以"少而精"比"多而全"更省力。

## [How to write good prompts（写卡指南）](https://andymatuschak.org/prompts/)

- 作者：Andy Matuschak（长文）
- 方式：写卡原则
- 产物：闪卡
- 工具：无；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★★★（5/5）
- 原文存档：[原文](raw/web/04-cards/andymatuschak-prompts.md)

**做法。**讲怎么写好间隔复习的问题：每张卡只考一个点、答案要精确、要用多个角度考同一个概念、要连到你在乎的事情上。Dwarkesh 早期就是把这篇整段粘进提示词让模型出卡。

**可借鉴。**最好的制卡提示词，就是把这篇文章放进上下文。

## [Lucas Soares：先测再做卡，只给答错的做卡](https://www.youtube.com/watch?v=RocA3wA3QjU)

- 作者：Lucas Soares（YouTube）
- 方式：先测再做卡、检索练习
- 产物：HTML 小测验、Anki 卡（直接写入数据库）、带时间戳的 Obsidian 摘录
- 工具：Claude Code skill、Anki、Obsidian；是否需要 MCP：不需要
- 依赖：依赖 Claude Code，思路通用
- 评分：★★★★★（5/5）
- 原文存档：[视频字幕全文](raw/transcripts/RocA3wA3QjU.txt)

**做法。**顺序是：自己先读一遍材料，让 Claude Code 用一个 skill 生成 HTML 小测验，做完看分数，只把答错的点交给 Claude Code，由 skill 直接写进 Anki 数据库，不经过导入文件。他明确说"把整篇文章贴进去自动出卡"是弱用法，因为卡片和你真正在意的东西对不上。看 YouTube 时，他用脚本拉字幕，再用一条 slash 命令摘出关心的段落，每条都带时间戳链接存进 Obsidian，卡片背面放一个指向该时间戳的来源字段。

**可借鉴。**"先测再做卡"是控制卡片数量和质量最有效的一条规则；卡片背面附原始出处链接，复习时忘了还能回到上下文。

## [Andy Matuschak：模型没有长期复习的品味](https://x.com/andy_matuschak/status/2046621455274869235)

- 作者：Andy Matuschak（X）
- 方式：观点、制卡
- 产物：无
- 工具：无；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★★☆（4/5）
- 原文存档：[帖子全文](raw/x/2046621455274869235.md)

**做法。**模型的盲区是"现在看着没问题、几个月后复习时看不懂"的卡，因为它从没体验过长期复习。后续更新提到新模型的分数没有明显变好。

**可借鉴。**审卡时专门问一句"脱离今天的上下文还能看懂吗"。

## [Andy Matuschak：练习题应该随时间变化并逐步加深](https://x.com/andy_matuschak/status/2046621459637031342)

- 作者：Andy Matuschak（X）
- 方式：动态练习
- 产物：无
- 工具：无；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★★☆（4/5）
- 原文存档：[帖子全文](raw/x/2046621459637031342.md)

**做法。**他的新方向是：练习题不应该是一成不变的卡片，而应随时间变化、逐步加深，并且知道你当前的上下文，这恰好是 LLM 擅长的。SuperMemo 作者 Wozniak 在回复里补充：别考公式本身，要考你能不能用对公式背后的直觉。

**可借鉴。**复习时让 AI 每次换一种问法、换一个场景，比反复翻同一张卡更接近"理解"。

## [Augmenting Long-term Memory](https://augmentingcognition.com/ltm.html)

- 作者：Michael Nielsen（长文）
- 方式：间隔复习读论文
- 产物：Anki 卡
- 工具：Anki；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★★☆（4/5）
- 原文存档：[原文](raw/web/04-cards/augmentingcognition-ltm-html.md)

**做法。**讲他怎么用 Anki 读论文：第一遍只为能读懂而做卡，反复几轮读同一篇，每轮都把新理解变成卡。他认为 Anki 让记忆变成一种选择。

**可借鉴。**"逐轮加深地读一篇论文、每轮补卡"是很好的读论文方法。

## [Dwarkesh：把一期播客做成闪卡和练习题网站](https://x.com/dwarkesh_sp/status/2049570394110390305)

- 作者：Dwarkesh Patel（X）
- 方式：制卡、练习题
- 产物：公开网站上的闪卡和练习题
- 工具：任意 LLM；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★★☆（4/5）
- 原文存档：[帖子全文](raw/x/2049570394110390305.md)

**做法。**他把一期硬核播客（Reiner Pope 讲推理经济学）整理成一个公开的闪卡和练习题网站，约 2.1k 赞、2.5k 收藏。评论区有人给出一种好题型：给出 3 个公开线索（API 价格、延迟目标、上下文长度），让学习者推断瓶颈在哪，再说出什么测量能证伪这个猜测。

**可借鉴。**"给线索、让推断、再说怎么证伪"的题型远比定义题有用。

## [X @iluciddreaming：为什么 AI 时代还需要继续用 Anki（中文）](https://x.com/iluciddreaming/status/2085968775585935421)

- 作者：iluciddreaming（X）
- 方式：观点、审卡
- 产物：Anki 卡
- 工具：Anki；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★★☆（4/5）
- 原文存档：[帖子全文](raw/x/2085968775585935421.md)

**做法。**长文总结为"AI 负责学得快，Anki 负责忘得慢"。他认为现在可选的不再是"手写哪些卡"，而是"审哪些 AI 卡"，同时提醒要防"欠卡螺旋"：新卡太多、复习越积越多，最后放弃。

**可借鉴。**每天新卡设上限，是防欠卡螺旋最简单的办法。

## [ankimcp/anki-mcp-server](https://github.com/ankimcp/anki-mcp-server)

- 作者：ankimcp（GitHub）
- 方式：AI 读写 Anki
- 产物：Anki 卡
- 工具：Anki、任意 MCP 客户端；是否需要 MCP：需要
- 依赖：需 MCP
- 评分：★★★★☆（4/5）
- 原文存档：[原文](raw/web/04-cards/github-ankimcp-anki-mcp-server.md)

**做法。**让 AI 助手直接读写 Anki 的 MCP 服务，现在推荐用 Anki 插件版（服务跑在 Anki 内部），STDIO 版适合 Claude Code 和 Cursor。约 500 星。

**可借鉴。**AI 和 Anki 之间最常用的桥。

## [nietus/anki-mcp：在聊天里被 Anki 考](https://github.com/nietus/anki-mcp)

- 作者：nietus（GitHub）
- 方式：聊天里考卡、找顽固卡
- 产物：Anki 卡、留存统计
- 工具：Anki、Claude 等 MCP 客户端；是否需要 MCP：需要
- 依赖：需 MCP
- 评分：★★★★☆（4/5）
- 原文存档：[原文](raw/web/04-cards/github-nietus-anki-mcp.md)

**做法。**35 个工具，包括 `quiz_me`（在聊天里一题一题考，结果写回 Anki）、`find_leeches`（找出总是忘的卡并修改）、`make_cards`（先预览再添加）和留存率统计。安装是一行 `claude mcp add`。

**可借鉴。**"找顽固卡并改写"是很少有工具做到的一步：总忘的卡通常是卡本身写得不好。

## [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki)

- 作者：open-spaced-repetition（GitHub）
- 方式：间隔复习算法
- 产物：无
- 工具：Anki；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★★☆（4/5）
- 原文存档：[原文](raw/web/04-cards/github-open-spaced-repetition-fsrs4anki.md)

**做法。**FSRS 算法的 Anki 实现，Anki 23.10 以后已经内置。它根据你的复习记录估计每张卡的记忆稳定性来排期，比老的 SM-2 更准。

**可借鉴。**用 Anki 就打开 FSRS；自己写复习工具也可以直接用它的开源实现。

## [Learning Persian with Anki, ChatGPT and YouTube](https://cjauvin.github.io/posts/learning-persian/)

- 作者：Christian Jauvin（博客）
- 方式：截图制卡、多种卡型
- 产物：Anki 卡（多种类型）
- 工具：Anki、ChatGPT、YouTube；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★★☆（4/5）
- 原文存档：[原文](raw/web/04-cards/cjauvin-posts-learning-persian.md)

**做法。**他学波斯语时，从 YouTube 课程视频里截图，一张截图做成几种不同类型的卡（只看正面、双向、听写等），ChatGPT 用来解释语法和造例句。卡片大多是带语法的短语，很少是单词。HN 约 260 分，评论里有人说做卡几个月就累了。

**可借鉴。**"同一份材料做成几种卡型"能从不同方向检索同一个知识点。

## [Andy Matuschak：Memory Machines 发布帖](https://x.com/andy_matuschak/status/2046621450304724993)

- 作者：Andy Matuschak（X）
- 方式：评测 AI 制卡
- 产物：报告
- 工具：无；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★☆☆（3/5）
- 原文存档：[帖子全文](raw/x/2046621450304724993.md)

**做法。**介绍 Memory Machines 报告、数据集和评测场的发布帖，是上面几条讨论的起点。

**可借鉴。**想看完整讨论时从这条进入。

## [Dwarkesh：把 Matuschak 写卡指南粘进提示词](https://x.com/dwarkesh_sp/status/1816172906705215841)

- 作者：Dwarkesh Patel（X）
- 方式：制卡
- 产物：闪卡
- 工具：Claude 等；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★☆☆（3/5）
- 原文存档：[帖子全文](raw/x/1816172906705215841.md)

**做法。**他早期的做法是把 Matuschak 的写卡指南整段粘进提示词，再让模型对访谈内容出卡。

**可借鉴。**简单有效：好的写卡原则本身就是最好的提示词。

## [nailuoGG/anki-mcp-server](https://github.com/nailuoGG/anki-mcp-server)

- 作者：nailuoGG（GitHub）
- 方式：AI 读写 Anki
- 产物：Anki 卡
- 工具：Anki（AnkiConnect）；是否需要 MCP：需要
- 依赖：需 MCP
- 评分：★★★☆☆（3/5）
- 原文存档：[原文](raw/web/04-cards/github-nailuogg-anki-mcp-server.md)

**做法。**通过 AnkiConnect 提供牌组、笔记类型、增删改卡等工具的 MCP 服务，约 250 星。

**可借鉴。**功能基础、稳定，适合只想"让 AI 把卡写进去"的人。

## [scorzeth/anki-mcp-server](https://github.com/scorzeth/anki-mcp-server)

- 作者：scorzeth（GitHub）
- 方式：AI 读写 Anki、复习到期卡
- 产物：Anki 卡
- 工具：Anki（AnkiConnect）；是否需要 MCP：需要
- 依赖：需 MCP
- 评分：★★★☆☆（3/5）
- 原文存档：[原文](raw/web/04-cards/github-scorzeth-anki-mcp-server.md)

**做法。**除了加卡，还把"到期卡"和"新卡"作为资源暴露给模型，并能更新卡片复习结果，约 190 星。

**可借鉴。**能让 AI 在会话开头先拿到今天到期的卡来考你。

## [VinayakHyde/claude-anki-flashcard-rules](https://github.com/VinayakHyde/claude-anki-flashcard-rules)

- 作者：VinayakHyde（GitHub）
- 方式：制卡规则
- 产物：Anki 卡
- 工具：Claude Code（~/.claude/rules）、Anki MCP；是否需要 MCP：需要
- 依赖：需 MCP
- 评分：★★★☆☆（3/5）
- 原文存档：[原文](raw/web/04-cards/github-vinayakhyde-claude-anki-flashcard-rules.md)

**做法。**一组放进 Claude Code 规则目录的制卡规范，分通用、数学（四层：定义、直觉、推导、应用）、编程、算法几类，配合 Anki MCP 使用。星数少，但规则写得具体。

**可借鉴。**数学卡的四层拆法可以直接借用。

## [wpwilson10/spacedrep](https://github.com/wpwilson10/spacedrep)

- 作者：wpwilson10（GitHub）
- 方式：无界面间隔复习
- 产物：Anki 数据库中的卡
- 工具：CLI、MCP；是否需要 MCP：需要
- 依赖：需 MCP（或 CLI）
- 评分：★★★☆☆（3/5）
- 原文存档：[原文](raw/web/04-cards/github-wpwilson10-spacedrep.md)

**做法。**CLI 加 MCP，直接读写 Anki 的 SQLite，FSRS 状态能和 Anki 互通，不需要打开 Anki 界面。

**可借鉴。**适合在服务器或 agent 里跑复习。

## [klutometis/srs-mcp](https://github.com/klutometis/srs-mcp)

- 作者：klutometis（GitHub）
- 方式：无界面间隔复习
- 产物：SQLite 或 Postgres 中的卡
- 工具：MCP；是否需要 MCP：需要
- 依赖：需 MCP
- 评分：★★★☆☆（3/5）
- 原文存档：[原文](raw/web/04-cards/github-klutometis-srs-mcp.md)

**做法。**大约 200 行代码包了一层 FSRS，存储用 SQLite 或 Postgres，完全不需要界面，适合放在云主机上，配合定时任务每天出题。

**可借鉴。**"自己的 FSRS 服务 + 每天定时出题"是一个不依赖 Anki 的方案。

## [bestnite/engram](https://github.com/bestnite/engram)

- 作者：bestnite（GitHub）
- 方式：自托管间隔复习
- 产物：闪卡
- 工具：自托管服务、MCP；是否需要 MCP：需要
- 依赖：需 MCP
- 评分：★★★☆☆（3/5）
- 原文存档：[原文](raw/web/04-cards/github-bestnite-engram.md)

**做法。**Go 写的自托管闪卡服务，用 FSRS v6 调度，自带 MCP。linux.do 上有发布帖。

**可借鉴。**想自托管又想让 AI 接入时可以考虑。

## [arashbehmand/learners-mcp](https://github.com/arashbehmand/learners-mcp)

- 作者：arashbehmand（GitHub）
- 方式：资料变地图、四阶段学习、制卡
- 产物：学习地图、Anki 包、md
- 工具：MCP；是否需要 MCP：需要
- 依赖：需 MCP
- 评分：★★★☆☆（3/5）
- 原文存档：[原文](raw/web/04-cards/github-arashbehmand-learners-mcp.md)

**做法。**把资料变成学习地图，然后按预览、讲解、提问、锚定四个阶段走，最后出卡，导出 .apkg 和 md。

**可借鉴。**"预览、讲解、提问、锚定"四阶段是一个清楚的课节模板。

## [kerrickstaley/genanki](https://github.com/kerrickstaley/genanki)

- 作者：kerrickstaley（GitHub）
- 方式：程序生成卡包
- 产物：.apkg 文件
- 工具：Python；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★☆☆（3/5）
- 原文存档：[原文](raw/web/04-cards/github-kerrickstaley-genanki.md)

**做法。**用 Python 生成 Anki 卡包的库，约 2.7k 星。很多学习 skill 用它导出卡片。

**可借鉴。**让 AI 写一段 genanki 脚本，就能在没有 MCP 的情况下批量出卡。

## [ObsidianToAnki/Obsidian_to_Anki](https://github.com/ObsidianToAnki/Obsidian_to_Anki)

- 作者：ObsidianToAnki（GitHub）
- 方式：笔记同步成卡
- 产物：Anki 卡
- 工具：Obsidian、Anki；是否需要 MCP：不需要
- 依赖：依赖 Obsidian
- 评分：★★★☆☆（3/5）
- 原文存档：[原文](raw/web/04-cards/github-obsidiantoanki-obsidian-to-anki.md)

**做法。**把 Obsidian 笔记里按格式写的问答同步成 Anki 卡，约 2k 星。

**可借鉴。**笔记和卡片放在同一个地方维护。

## [st3v3nmw/obsidian-spaced-repetition](https://github.com/st3v3nmw/obsidian-spaced-repetition)

- 作者：st3v3nmw（GitHub）
- 方式：Obsidian 内复习
- 产物：笔记内闪卡
- 工具：Obsidian；是否需要 MCP：不需要
- 依赖：依赖 Obsidian
- 评分：★★★☆☆（3/5）
- 原文存档：[原文](raw/web/04-cards/github-st3v3nmw-obsidian-spaced-repetition.md)

**做法。**在 Obsidian 里直接复习闪卡，新版本支持 FSRS，还可以把整篇笔记放进复习队列。约 2.6k 星。

**可借鉴。**"整篇笔记进复习队列"适合复习概念笔记而不是单个事实。

## [doasfrancisco/anki-skill](https://github.com/doasfrancisco/anki-skill)

- 作者：doasfrancisco（GitHub）
- 方式：编程时提议卡片、人批准
- 产物：Anki 卡
- 工具：Claude Code、AnkiConnect；是否需要 MCP：需要
- 依赖：需 AnkiConnect
- 评分：★★★☆☆（3/5）
- 原文存档：[原文](raw/web/04-cards/github-doasfrancisco-anki-skill.md)

**做法。**在你写代码的过程中，AI 提议原子卡，你批准后才通过 AnkiConnect 写入。约 57 星。

**可借鉴。**"AI 提议、人批准"是自动化和质量之间的平衡点。

## [HumphreySun98/Smart-Study-Agent](https://github.com/HumphreySun98/Smart-Study-Agent)

- 作者：HumphreySun98（GitHub）
- 方式：概念图、自适应选题、间隔复习
- 产物：题库、.apkg、SQLite
- 工具：本地应用、LLM；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★☆☆（3/5）
- 原文存档：[原文](raw/web/04-cards/github-humphreysun98-smart-study-agent.md)

**做法。**概念图加 FSRS，并用强化学习挑下一道题，最后可以导出 Anki 卡包。约 58 星。

**可借鉴。**"自动选下一题"是自适应练习的核心部件。

## [kevin2li/PDF-Guru：PDF 制卡（中文）](https://github.com/kevin2li/PDF-Guru)

- 作者：kevin2li（GitHub）
- 方式：PDF 转卡
- 产物：Anki 卡
- 工具：桌面应用、Anki；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★☆☆（3/5）
- 原文存档：[原文](raw/web/04-cards/github-kevin2li-pdf-guru.md)

**做法。**PDF 工具箱，其中 Anki 模块能把 PDF 的不同格式内容转成卡片，约 4k 星，在备考人群里很流行。

**可借鉴。**考试类资料多为 PDF，用它批量出卡再人工删减。

## [ChangingSelf/anki-prompt：中文制卡提示词](https://github.com/ChangingSelf/anki-prompt)

- 作者：ChangingSelf（GitHub）
- 方式：制卡提示词
- 产物：Anki 卡
- 工具：任意 LLM、Anki MCP；是否需要 MCP：需要
- 依赖：可选 MCP
- 评分：★★★☆☆（3/5）
- 原文存档：[原文](raw/web/04-cards/github-changingself-anki-prompt.md)

**做法。**中文制卡提示词合集，配合 linux.do 上的 Anki MCP 制卡流程帖使用，强调原子化和 HTML 字段格式。

**可借鉴。**中文语境下现成的制卡规范。

## [riddle.press：自动起草闪卡](https://riddle.press/auto-drafting-flashcards/)

- 作者：riddle.press（博客）
- 方式：高亮起草卡、同步
- 产物：Anki 卡
- 工具：Readwise Reader（Ghostreader）、Obsidian、Anki；是否需要 MCP：不需要
- 依赖：依赖 Readwise
- 评分：★★★☆☆（3/5）
- 原文存档：[原文](raw/web/04-cards/riddle-auto-drafting-flashcards.md)

**做法。**在 Readwise Reader 里用 Ghostreader 为高亮起草卡片，经 Obsidian 插件同步，再进 Anki。作者强调是"起草"，最后要自己改。

**可借鉴。**把"起草"和"定稿"分成两步。

## [HN：让 ChatGPT 像 Anki 一样考我](https://news.ycombinator.com/item?id=44021924)

- 作者：HN 用户（HN）
- 方式：讨论
- 产物：无
- 工具：ChatGPT；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★☆☆（3/5）
- 原文存档：[原文](raw/web/04-cards/news-item-id-44021924.md)

**做法。**有人说自己就让 ChatGPT 按 Anki 的方式考他。回复直接指出：它是 LLM，不是间隔复习系统，同一会话里偶尔再问一遍不等于按遗忘曲线排期。

**可借鉴。**聊天可以出题，但排期要交给真正的 SRS。

## [Show HN: fata，用间隔复习对抗 AI 编程造成的技能退化](https://news.ycombinator.com/item?id=48489163)

- 作者：Djoumé（fata 作者）（HN）
- 方式：每日编程小测、间隔复习
- 产物：每日 10 题
- 工具：fata.dev（网页、手机）；是否需要 MCP：不需要
- 依赖：依赖该产品
- 评分：★★★☆☆（3/5）
- 原文存档：[原文](raw/web/04-cards/news-item-id-48489163.md)

**做法。**作者写了 20 年代码，最近几乎全靠 agent，发现自己的技术能力在退化，而且不懂技术就指挥不好 agent。于是做了 fata：每天几分钟的编程知识间隔复习，覆盖 Rust、CSS、React、Python、TypeScript 和架构。HN 约 120 分。

**可借鉴。**"用 agent 写代码的同时，每天花几分钟复习基础"是一个容易坚持的习惯。

## [ankimcp/anki-mcp-server-addon](https://github.com/ankimcp/anki-mcp-server-addon)

- 作者：ankimcp（GitHub）
- 方式：AI 读写 Anki
- 产物：Anki 卡
- 工具：Anki 插件、MCP；是否需要 MCP：需要
- 依赖：需 MCP
- 评分：★★★☆☆（3/5）
- 原文存档：[原文](raw/web/04-cards/github-ankimcp-anki-mcp-server-addon.md)

**做法。**ankimcp 的 Anki 插件版本：MCP 服务直接跑在 Anki 内部，不需要另外装 AnkiConnect。约 90 星。

**可借鉴。**官方推荐的安装方式。

## [X @sonarforce：AI 卡适合入门，长期卡自己做（中文）](https://x.com/sonarforce/status/1968594255200530480)

- 作者：sonarforce（X）
- 方式：观点
- 产物：无
- 工具：无；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★☆☆☆（2/5）
- 原文存档：[帖子全文](raw/x/1968594255200530480.md)

**做法。**他认为 AI 制卡适合初学一份材料时降低门槛（卡片比大段材料更容易接受）以及检验学习成果；放进间隔重复系统长期滚动的卡，还是自己做更好。

**可借鉴。**可以按"入门卡用 AI、长期卡手写"来分工。

## [CamdenClark/anki-mcp-server](https://github.com/CamdenClark/anki-mcp-server)

- 作者：CamdenClark（GitHub）
- 方式：AI 读写 Anki
- 产物：Anki 卡
- 工具：Anki（AnkiConnect）；是否需要 MCP：需要
- 依赖：需 MCP
- 评分：★★☆☆☆（2/5）
- 原文存档：[原文](raw/web/04-cards/github-camdenclark-anki-mcp-server.md)

**做法。**另一个通过 AnkiConnect 连接 Anki 的 MCP 服务，约 80 星。

**可借鉴。**备选。

## [solidSpoon/anki-mcp（中文，词汇）](https://github.com/solidSpoon/anki-mcp)

- 作者：solidSpoon（GitHub）
- 方式：词汇卡
- 产物：带发音的 Anki 卡
- 工具：Anki、MCP；是否需要 MCP：需要
- 依赖：需 MCP
- 评分：★★☆☆☆（2/5）
- 原文存档：[原文](raw/web/04-cards/github-solidspoon-anki-mcp.md)

**做法。**面向词汇学习的 Anki MCP，支持自动生成发音、智能搜索和统计分析。星数少。

**可借鉴。**学语言时可以参考它怎么自动加发音。

## [crybot/obsidian-flashcards-llm](https://github.com/crybot/obsidian-flashcards-llm)

- 作者：crybot（GitHub）
- 方式：AI 从笔记出卡
- 产物：笔记内闪卡
- 工具：Obsidian、LLM API；是否需要 MCP：不需要
- 依赖：依赖 Obsidian
- 评分：★★☆☆☆（2/5）
- 原文存档：[原文](raw/web/04-cards/github-crybot-obsidian-flashcards-llm.md)

**做法。**在 Obsidian 里用 LLM 从当前笔记生成闪卡。

**可借鉴。**便捷，但要配合人工审卡。

## [ccmdi/obsidianki](https://github.com/ccmdi/obsidianki)

- 作者：ccmdi（GitHub）
- 方式：笔记变卡
- 产物：Anki 卡
- 工具：Obsidian、Anki、LLM；是否需要 MCP：不需要
- 依赖：依赖 Obsidian
- 评分：★★☆☆☆（2/5）
- 原文存档：[原文](raw/web/04-cards/github-ccmdi-obsidianki.md)

**做法。**从 Obsidian 笔记用 AI 生成 Anki 卡的工具。

**可借鉴。**和上一条类似，可以对比选择。

## [Brunimir/Knowledge-Factory](https://github.com/Brunimir/Knowledge-Factory)

- 作者：Brunimir（GitHub）
- 方式：笔记变卡
- 产物：Anki 卡
- 工具：Obsidian、Anki；是否需要 MCP：不需要
- 依赖：依赖 Obsidian
- 评分：★★☆☆☆（2/5）
- 原文存档：[原文](raw/web/04-cards/github-brunimir-knowledge-factory.md)

**做法。**把笔记加工成卡片的流水线工具。

**可借鉴。**可参考它的流水线拆分。

## [lukmay/simple-anki-sync](https://github.com/lukmay/simple-anki-sync)

- 作者：lukmay（GitHub）
- 方式：笔记同步成卡
- 产物：Anki 卡
- 工具：Obsidian、Anki；是否需要 MCP：不需要
- 依赖：依赖 Obsidian
- 评分：★★☆☆☆（2/5）
- 原文存档：[原文](raw/web/04-cards/github-lukmay-simple-anki-sync.md)

**做法。**轻量的 Obsidian 到 Anki 同步工具。

**可借鉴。**想要最少配置的同步时可以用。

## [guepardlover77/learn-skill](https://github.com/guepardlover77/learn-skill)

- 作者：guepardlover77（GitHub）
- 方式：材料变计划和卡包
- 产物：.apkg、md、SM-2 表
- 工具：Claude Code、Obsidian；是否需要 MCP：不需要
- 依赖：依赖 Claude Code
- 评分：★★☆☆☆（2/5）
- 原文存档：[原文](raw/web/04-cards/github-guepardlover77-learn-skill.md)

**做法。**把材料变成学习计划，用 genanki 生成卡包，同时输出 Obsidian 笔记和 SM-2 复习表。

**可借鉴。**一次性产出"计划、卡、笔记"三件套。

## [mkrech/anki-course-tutor-mcp-server](https://github.com/mkrech/anki-course-tutor-mcp-server)

- 作者：mkrech（GitHub）
- 方式：会话辅导加 Anki 调度
- 产物：会话记录、统计
- 工具：MCP、Anki；是否需要 MCP：需要
- 依赖：需 MCP
- 评分：★★☆☆☆（2/5）
- 原文存档：[原文](raw/web/04-cards/github-mkrech-anki-course-tutor-mcp-server.md)

**做法。**把辅导会话和 Anki 调度接在一起的 MCP 服务，星数很少。

**可借鉴。**思路是"复习也由导师主持"。

## [Notion 间隔复习模板](https://www.notion.com/templates/spaced-repetition-flashcards-2)

- 作者：Notion 社区（Notion）
- 方式：间隔复习
- 产物：Notion 数据库卡片
- 工具：Notion；是否需要 MCP：不需要
- 依赖：依赖 Notion
- 评分：★★☆☆☆（2/5）
- 原文存档：[原文](raw/web/04-cards/notion-templates-spaced-repetition-flashcards-2.md)

**做法。**用 Notion 数据库和公式做的闪卡模板，按下次复习日期筛出今天要复习的卡。

**可借鉴。**已经把笔记放在 Notion 的人，可以不换工具起步。

## [r/Anki：AI 做的卡有什么问题](https://www.reddit.com/r/Anki/comments/1bncpwy/to_the_people_who_used_chatgpt_to_create_cards/)

- 作者：r/Anki 用户（Reddit）
- 方式：讨论
- 产物：无
- 工具：Anki、ChatGPT；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★☆☆☆（2/5）
- 原文存档：[原文](raw/web/04-cards/reddit-r-anki-comments-1bncpwy-to-the-people-who-used-chatgpt-to-creat.md)

**做法。**r/Anki 上问用过 ChatGPT 做卡的人体验如何。常见回复是 AI 卡常常一张塞多个事实、违反最小信息原则，偶尔有事实错误，必须审。

**可借鉴。**审卡清单可以加上"是否只有一个事实"。

## [r/Anki：最高效的制卡方式](https://www.reddit.com/r/Anki/comments/1hov0v9/what_is_the_most_efficient_and_fast_way_to_make/)

- 作者：r/Anki 用户（Reddit）
- 方式：讨论
- 产物：无
- 工具：Anki；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★☆☆☆（2/5）
- 原文存档：[原文](raw/web/04-cards/reddit-r-anki-comments-1hov0v9-what-is-the-most-efficient-and-fast-way.md)

**做法。**讨论怎样快速做卡，回复里有人推荐用 AI 出初稿，也有老用户坚持做卡本身就是学习。

**可借鉴。**两种立场都在，按材料类型选择。

## [r/Anki：反对用 AI 做卡](https://www.reddit.com/r/Anki/comments/1j1rpfd/unpopular_opinion_you_shouldnt_use_ai_to_create)

- 作者：r/Anki 用户（Reddit）
- 方式：讨论
- 产物：无
- 工具：Anki；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★☆☆☆（2/5）
- 原文存档：[原文](raw/web/04-cards/reddit-r-anki-comments-1j1rpfd-unpopular-opinion-you-shouldnt-use-ai-t.md)

**做法。**标题是"不受欢迎的观点：不应该用 AI 做闪卡"，约 350 赞。从搜索摘要看，主流回复是"只靠 AI 做卡、又不核对正确性，大概是坏习惯，但某些场景可以"。正文未能直接读取。

**可借鉴。**和 Matuschak 的结论一致：AI 只做初稿。

## [r/Anki：用 AI 做卡的人能分享吗](https://www.reddit.com/r/Anki/comments/1nbwwm3/for_those_who_use_ai_to_create_flashcards_could)

- 作者：r/Anki 用户（Reddit）
- 方式：讨论
- 产物：无
- 工具：Anki；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★☆☆☆（2/5）
- 原文存档：[原文](raw/web/04-cards/reddit-r-anki-comments-1nbwwm3-for-those-who-use-ai-to-create-flashcar.md)

**做法。**征集用 AI 做卡的人的具体做法。相关讨论里有人说 AI 只要配合好提示词就能做出简短的卡，也有人说不严格监督就做不出好卡。正文未能直接读取。

**可借鉴。**可以从中收集别人的制卡提示词。

## [r/Anki：用 Readwise 自动把高亮变卡](https://www.reddit.com/r/Anki/comments/1hz2y2r/automated_highlighttoanki_cards_using_readwise/)

- 作者：r/Anki 用户（Reddit）
- 方式：高亮自动制卡
- 产物：Anki 卡
- 工具：Readwise、Anki；是否需要 MCP：不需要
- 依赖：依赖 Readwise
- 评分：★★☆☆☆（2/5）
- 原文存档：[原文](raw/web/04-cards/reddit-r-anki-comments-1hz2y2r-automated-highlighttoanki-cards-using-r.md)

**做法。**用 Readwise 把阅读高亮自动变成 Anki 卡。评论区提醒全自动会让卡片质量下降，中间需要一步"值不值得记"的筛选。

**可借鉴。**自动化流水线里要留一道人工筛选。

## [r/readwise：用 n8n 自动制卡](https://www.reddit.com/r/readwise/comments/1ic1uwa/guide_how_i_automated_flashcard_creation_with_n8n/)

- 作者：r/readwise 用户（Reddit）
- 方式：自动化制卡
- 产物：Anki 卡
- 工具：n8n、Readwise、GPT、AnkiConnect；是否需要 MCP：需要
- 依赖：依赖 n8n 与 Readwise
- 评分：★★☆☆☆（2/5）
- 原文存档：[原文](raw/web/04-cards/reddit-r-readwise-comments-1ic1uwa-guide-how-i-automated-flashcard-cre.md)

**做法。**一篇指南，用 n8n 串起 Readwise 高亮、GPT 生成和 AnkiConnect 写入。

**可借鉴。**想做全自动流水线时的参考搭法。

## [HN：用 MCP 把卡写进 Anki](https://news.ycombinator.com/item?id=44022205)

- 作者：HN 用户（HN）
- 方式：讨论
- 产物：Anki 卡
- 工具：MCP、Anki；是否需要 MCP：需要
- 依赖：需 MCP
- 评分：★★☆☆☆（2/5）
- 原文存档：[原文](raw/web/04-cards/news-item-id-44022205.md)

**做法。**同一讨论里有人分享用 MCP 让模型直接把卡写进 Anki。

**可借鉴。**和 Lucas Soares 直接写入 Anki 的思路一致。

## [HN：让 AI 起草闪卡](https://news.ycombinator.com/item?id=47063007)

- 作者：HN 用户（HN）
- 方式：讨论
- 产物：闪卡草稿
- 工具：任意 LLM；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★☆☆☆（2/5）
- 原文存档：[原文](raw/web/04-cards/news-item-id-47063007.md)

**做法。**讨论用 AI 给闪卡起草初稿，再由人修改的做法。

**可借鉴。**再次确认"AI 出初稿"是共识。

## [Show HN: Janus](https://news.ycombinator.com/item?id=46599896)

- 作者：Janus 作者（HN）
- 方式：资料转卡
- 产物：Anki 或 Mochi 卡
- 工具：自研产品；是否需要 MCP：不需要
- 依赖：依赖该产品
- 评分：★★☆☆☆（2/5）
- 原文存档：[原文](raw/web/04-cards/news-item-id-46599896.md)

**做法。**把 PDF、视频、笔记转成 Anki 或 Mochi 卡片的产品。

**可借鉴。**产品形态参考。

## [Show HN: Keepmind](https://news.ycombinator.com/item?id=44491043)

- 作者：Keepmind 作者（HN）
- 方式：AI 间隔复习
- 产物：闪卡
- 工具：自研产品；是否需要 MCP：不需要
- 依赖：依赖该产品
- 评分：★★☆☆☆（2/5）
- 原文存档：[原文](raw/web/04-cards/news-item-id-44491043.md)

**做法。**带 AI 的间隔复习产品发布帖。

**可借鉴。**产品形态参考。

## [Anki and GPT-3（Chrome 插件）](https://andrewjudson.com/spaced-repetition/2023/02/01/anki-chrome.html)

- 作者：Andrew Judson（博客）
- 方式：AI 制卡
- 产物：Anki 卡
- 工具：Chrome 插件、GPT-3、Anki；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★☆☆☆（2/5）
- 原文存档：[原文](raw/web/04-cards/andrewjudson-spaced-repetition-2023-02-01-anki-chrome-html.md)

**做法。**一个 Chrome 插件，选中网页文字后用 GPT-3 生成 Anki 卡。HN 讨论约 200 分，最高赞评论来自每天用 Anki 的人：认真做卡本身就是学习的关键部分，跳过这一步可能只剩死记硬背。

**可借鉴。**高赞评论本身就是一条很好的提醒。

## [V2EX：把笔记自动转换成 Anki 卡片（中文）](https://www.v2ex.com/t/1085137)

- 作者：Gabrielle70（V2EX）
- 方式：笔记转卡
- 产物：Anki 卡
- 工具：任意 LLM、Python；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★☆☆☆（2/5）
- 原文存档：[原文](raw/web/04-cards/v2ex-t-1085137.md)

**做法。**楼主的笔记是树形结构，希望 AI 能按目录层次生成卡片。回复里有人给出了 JSON 模板加 Python 脚本的做法。

**可借鉴。**"让 AI 先按固定 JSON 输出，再用脚本导入"是最稳的批量制卡方式。

## [V2EX：Anki 初体验，效率不高（中文）](https://www.v2ex.com/t/1184930)

- 作者：YanSeven（V2EX）
- 方式：讨论
- 产物：md 表格
- 工具：Anki、GPT；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★☆☆☆（2/5）
- 原文存档：[原文](raw/web/04-cards/v2ex-t-1184930.md)

**做法。**楼主让 GPT 把文档导出成 CSV 再导入 Anki，试了一阵觉得对他要记的几百条计算机命令来说效率不高，更愿意用结构化的 md 表格。回复里有人解释间隔复习要长期才见效。

**可借鉴。**不是所有内容都适合做卡；工具型知识有时一张速查表更合适。

## [X @belindmo：Obsidian 的 SRAI 插件](https://x.com/belindmo/status/1900536468638224748)

- 作者：belindmo（X）
- 方式：AI 间隔复习
- 产物：笔记内闪卡
- 工具：Obsidian；是否需要 MCP：不需要
- 依赖：依赖 Obsidian
- 评分：★★☆☆☆（2/5）
- 原文存档：[帖子全文](raw/x/1900536468638224748.md)

**做法。**发布 Obsidian 社区插件"spaced repetition ai"，可以加闪卡、让 AI 生成卡并在 Obsidian 内复习。约 180 赞。

**可借鉴。**Obsidian 用户的另一个选项。

## [cheanus/SRSA：给 agent 自己做间隔复习](https://github.com/cheanus/SRSA)

- 作者：cheanus（GitHub）
- 方式：agent 记忆
- 产物：agent 的记忆卡
- 工具：任意 agent；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★☆☆☆（2/5）
- 原文存档：[原文](raw/web/04-cards/github-cheanus-srsa.md)

**做法。**思路反过来：不是给人背，而是给 agent 自己做 FSRS 记忆卡，让它记住项目规矩。linux.do 上有发布帖。

**可借鉴。**当学习对象是"让 AI 记住你的偏好"时可以用这个思路。

## [arielbk/anki-mcp：和你的闪卡对话](https://github.com/arielbk/anki-mcp)

- 作者：arielbk（GitHub）
- 方式：聊天式复习
- 产物：Anki 卡
- 工具：Anki、MCP；是否需要 MCP：需要
- 依赖：需 MCP
- 评分：★★☆☆☆（2/5）
- 原文存档：[原文](raw/web/04-cards/github-arielbk-anki-mcp.md)

**做法。**让你在聊天里和自己的 Anki 卡片对话的 MCP 服务，星数少。

**可借鉴。**备选。

## [happymario123/srs-mcp](https://github.com/happymario123/srs-mcp)

- 作者：happymario123（GitHub）
- 方式：会话内复习
- 产物：卡片
- 工具：Claude、MCP；是否需要 MCP：需要
- 依赖：需 MCP
- 评分：★☆☆☆☆（1/5）
- 原文存档：[原文](raw/web/04-cards/github-happymario123-srs-mcp.md)

**做法。**在编程会话里做间隔复习的 MCP，用 SM-2，属于原型，0 星。

**可借鉴。**仅作记录。

## [qinrose/deepseek-to-anki](https://github.com/qinrose/deepseek-to-anki)

- 作者：qinrose（GitHub）
- 方式：对话里识别卡片
- 产物：Anki 卡
- 工具：浏览器扩展、AnkiConnect；是否需要 MCP：需要
- 依赖：需 AnkiConnect
- 评分：★☆☆☆☆（1/5）
- 原文存档：[原文](raw/web/04-cards/github-qinrose-deepseek-to-anki.md)

**做法。**浏览器扩展，自动识别 DeepSeek 对话中的卡片 JSON，一键加入 Anki。0 星。

**可借鉴。**"让模型按固定 JSON 出卡，再由插件写入"是不依赖 MCP 的做法。

## [TheGodOfKing/Notetocard-siyuan（中文）](https://github.com/TheGodOfKing/Notetocard-siyuan)

- 作者：TheGodOfKing（GitHub）
- 方式：笔记变卡
- 产物：Anki 卡
- 工具：思源笔记、Anki；是否需要 MCP：不需要
- 依赖：依赖思源笔记
- 评分：★☆☆☆☆（1/5）
- 原文存档：[原文](raw/web/04-cards/github-thegodofking-notetocard-siyuan.md)

**做法。**思源笔记的 Anki 制卡插件，星数少。

**可借鉴。**思源用户可以参考。

## [mirrorlious/anki-card-maker：考研考公制卡（中文）](https://github.com/mirrorlious/anki-card-maker)

- 作者：mirrorlious（GitHub）
- 方式：PDF 识别制卡
- 产物：Anki 卡
- 工具：桌面工具、Anki；是否需要 MCP：不需要
- 依赖：通用
- 评分：★☆☆☆☆（1/5）
- 原文存档：[原文](raw/web/04-cards/github-mirrorlious-anki-card-maker.md)

**做法。**面向考研考公的 Anki 制卡工具，支持 AI 辅助、PDF OCR 精准定位和大批量导入导出。星数少。

**可借鉴。**备考场景参考。

## [YiwenZ123/ielts-vocab-study：雅思托福词汇 skill](https://github.com/YiwenZ123/ielts-vocab-study)

- 作者：YiwenZ123（GitHub）
- 方式：词汇、间隔复习
- 产物：SQLite 词库
- 工具：Claude Code、SQLite CLI；是否需要 MCP：不需要
- 依赖：依赖 Claude Code
- 评分：★☆☆☆☆（1/5）
- 原文存档：[原文](raw/web/04-cards/github-yiwenz123-ielts-vocab-study.md)

**做法。**雅思和托福词汇学习的 Claude Code skill，用 SQLite 命令行工具存词和做间隔复习。0 星。

**可借鉴。**"skill 加一个小数据库"就能做复习，不必依赖 Anki。
