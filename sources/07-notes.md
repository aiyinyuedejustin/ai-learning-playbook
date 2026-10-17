# 笔记与知识库

这一类关心学习留下的长期产物：Karpathy 式的 raw 加 wiki，Obsidian 库，几份 md 文件组成的学习状态，以及"今天学到了什么"仓库。评论区反复补充的一点是：知识库只是档案，学习要另外加一层（出卡、复习、追踪缺口）。

本类共 15 条，按评分从高到低排列。

## [Karpathy：LLM Knowledge Bases](https://x.com/karpathy/status/2039805659525644595)

- 作者：Andrej Karpathy（X）
- 方式：资料编译成 wiki、定期体检
- 产物：raw/ 原始资料、wiki/ 由 LLM 维护的 md
- 工具：任意 agent、Obsidian 作前端；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★★★（5/5）
- 原文存档：[帖子全文](raw/x/2039805659525644595.md)

**做法。**`raw/` 放原始资料，LLM 把它们"编译"成互相链接的 wiki，用 Obsidian 当前端浏览，问答结果再归档回 wiki，定期做 lint 体检。约 6.1 万赞、10.8 万收藏。评论区反复出现的补充是：这只是档案库，学习并没有发生在里面；有人在 AGENTS.md 里加了一层学习层，从概念文章自动出卡、用 FSRS 排期、用缺口追踪器生成研究清单。

**可借鉴。**`raw/` 加 `wiki/` 管"资料懂了没有"，再加一层学习目录管"你自己记住了没有"。

## [Karpathy：它让你省掉写，但省不掉读和想](https://x.com/karpathy/status/2041162213160091996)

- 作者：Andrej Karpathy（X）
- 方式：读原文、读摘要、读衔接分析
- 产物：wiki 条目
- 工具：任意 agent；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★★★（5/5）
- 原文存档：[帖子全文](raw/x/2041162213160091996.md)

**做法。**他补充自己的用法：每归档一份资料，都会读原文、读摘要，再读 LLM 对"这份资料和 wiki 已有内容怎么衔接、哪里新、哪里意外"的分析。原话的意思是 LLM 让你省掉写，但省不掉读和想。

**可借鉴。**让 AI 专门写"这份新资料和我已有知识的关系、哪里出乎意料"，比写摘要更有学习价值。

## [X @owenliang60：四个 skill 搭成的阅读飞轮（中文）](https://x.com/owenliang60/status/2026853452798898261)

- 作者：owenliang60（X）
- 方式：批判阅读、蒸馏、间隔复习
- 产物：Obsidian 里的"地图"（摘要加推理链）和"石头"（原子卡）
- 工具：Claude Code、Obsidian；是否需要 MCP：不需要
- 依赖：依赖 Obsidian
- 评分：★★★★☆（4/5）
- 原文存档：[帖子全文](raw/x/2026853452798898261.md)

**做法。**`/read` 做批判性拆解，`/insights` 做商业分析，`/note` 把内容蒸馏成"地图"（摘要加推理链）和"石头"（原子卡）存进 Obsidian，`/review` 按间隔复习出题、评分、排期。

**可借鉴。**"地图"和"石头"两层产物：一层管结构，一层管记忆，分工很清楚。

## [X @conjsslbm：log.md、open.md、plan.md 三个文件（中文）](https://x.com/conjsslbm/status/2105230345851588984)

- 作者：conjsslbm（X）
- 方式：记录提问、追踪卡点、定期出卡
- 产物：log.md、open.md、plan.md、Anki 卡
- 工具：任意 agent（他用 Opus）、Anki；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★★☆（4/5）
- 原文存档：[帖子全文](raw/x/2105230345851588984.md)

**做法。**他专门弄了一个学习工作区，规则很简单：学习时的提问原话全部记进 log.md；卡了多次的知识点记进 open.md；计划和资源放 plan.md；复习用 Anki，让 AI 定期根据这些文件生成闪卡。

**可借鉴。**三个文件就能撑起一套学习状态，"提问原话"还能拿来分析自己反复卡在哪里。

## [杰森的效率工坊：用 AI + Obsidian 精通一个领域（中文）](https://www.youtube.com/watch?v=s_HGV6xPZv0)

- 作者：杰森的效率工坊（YouTube）
- 方式：学习路径大纲、批量建库、MOC
- 产物：md 大纲、Obsidian 库、MOC
- 工具：Gemini Deep Research、NotebookLM、Cursor 类工具、Obsidian；是否需要 MCP：不需要
- 依赖：依赖 Obsidian
- 评分：★★★★☆（4/5）
- 原文存档：[视频字幕全文](raw/transcripts/s_HGV6xPZv0.md)

**做法。**先用 Gemini Deep Research 研究陌生领域，资料多时用 NotebookLM，输出一份 md 学习路径大纲：二级标题是宏观分类，三级标题是知识主题，列表项是原子知识点。然后用 Cursor 类工具（他用 TRAE，也提到 Claude Code 和 Gemini CLI）分四步批量建库（演示从 [07:43](https://www.youtube.com/watch?v=s_HGV6xPZv0&t=463s) 到 [08:14](https://www.youtube.com/watch?v=s_HGV6xPZv0&t=494s)）：文件夹、子文件夹加 MOC、每个原子点一篇带双链的笔记、总览 MOC。他强调 AI 只搭框架，内容要自己写，并定期回到 MOC 写总结。

**可借鉴。**"用编码 agent 批量建笔记库"比在 Obsidian 插件里一篇篇生成快得多；大纲的三级结构可以直接当 map.md 格式。

## [X @TheGEO_Lab：给 Karpathy 的知识库加一层学习](https://x.com/TheGEO_Lab/status/2040886266498109826)

- 作者：TheGEO_Lab（X）
- 方式：知识库加学习层
- 产物：AGENTS.md、自动闪卡、FSRS、缺口清单
- 工具：任意 agent；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★☆☆（3/5）
- 原文存档：[帖子全文](raw/x/2040886266498109826.md)

**做法。**在 Karpathy 帖子下回复：他们在 AGENTS.md 里写了一份带版本号的规范，每次会话 agent 都会读；从概念文章自动出闪卡，用 FSRS 排期，用缺口追踪器生成研究清单。原话是"Karpathy 描述的是档案库，我们加上了掌握"。

**可借鉴。**学习层可以只是 AGENTS.md 里的几条规则，不必另做工具。

## [charlie947/ai-second-brain](https://github.com/charlie947/ai-second-brain)

- 作者：charlie947（GitHub）
- 方式：资料编译成 wiki
- 产物：raw/ 与 wiki/
- 工具：Claude Code、Obsidian；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★☆☆（3/5）
- 原文存档：[原文](raw/web/07-notes/github-charlie947-ai-second-brain.md)

**做法。**Karpathy 式第二大脑的一个实现：原始资料放 `raw/` 不动，AI 维护 `wiki/` 里的链接页面。

**可借鉴。**想直接起步时可以拿来当目录模板。

## [Squared Away Life：用 AI 和 Obsidian 啃难书](https://www.squaredawaylife.com/posts/how-to-master-hard-books-with-ai-and-obsidian)

- 作者：Squared Away Life（博客）
- 方式：掌握套件
- 产物：全书地图、原子笔记模板、回忆题、闪卡、日程
- 工具：任意 LLM、Obsidian；是否需要 MCP：不需要
- 依赖：依赖 Obsidian
- 评分：★★★☆☆（3/5）
- 原文存档：[原文](raw/web/07-notes/squaredawaylife-posts-how-to-master-hard-books-with-ai-and-obsidian.md)

**做法。**让 AI 为一本难书生成"掌握套件"：全书地图、原子笔记的空模板、回忆题、闪卡和阅读日程。但读和写仍由人来做。

**可借鉴。**AI 只搭"空模板"，内容自己填，避免读 AI 摘要代替读书。

## [simonw/til：今天学到了什么](https://github.com/simonw/til)

- 作者：Simon Willison（GitHub）
- 方式：学完留一条
- 产物：每条一个 md
- 工具：GitHub；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★☆☆（3/5）
- 原文存档：[原文](raw/web/07-notes/github-simonw-til.md)

**做法。**"今天学到了什么"仓库：每学到一个小东西就写一篇短 md。Simon Willison 的 TIL 仓库已经积累了上千条，下一条 jbranchaud 的也是同类。

**可借鉴。**最轻的学习记录习惯，适合不想搭系统的人。

## [sundoubleday/four-question-learning：四问学习法（中文）](https://github.com/sundoubleday/four-question-learning)

- 作者：sundoubleday（GitHub）
- 方式：四问学习法
- 产物：学习笔记
- 工具：Claude Code 等；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★☆☆（3/5）
- 原文存档：[原文](raw/web/07-notes/github-sundoubleday-four-question-learning.md)

**做法。**从刘澜《学会如何学习》蒸馏出的 8 个 skill，以"四问学习法"为主框架，配 7 个子 skill。许可证是 CC BY-NC 4.0。

**可借鉴。**如果喜欢某本学习方法书，可以照这个思路把书蒸馏成 skill。

## [X @we_chat_tech：maxlearn，从你的聊天记录里学](https://x.com/we_chat_tech/status/2106382018506584463)

- 作者：we_chat_tech（X）
- 方式：从工作对话中出课和卡
- 产物：侧栏里的课、闪卡、测验
- 工具：Claude Code 改造版；是否需要 MCP：不需要
- 依赖：依赖 Claude Code
- 评分：★★☆☆☆（2/5）
- 原文存档：[帖子全文](raw/x/2106382018506584463.md)

**做法。**他问过 Claude Code 什么是 MVCC，一周后就忘了，于是做了 maxlearn：从你和 Claude Code 的聊天记录和兴趣里出课、出卡、出测验，放在侧栏里并做间隔复习。

**可借鉴。**"从你本来就在做的工作里学"，复习素材不用另外找。

## [Felipe Sinisterra：研究用第二大脑](https://www.felipesinisterra.com/blog/how-i-set-up-my-second-brain-for-research-with-ai)

- 作者：Felipe Sinisterra（博客）
- 方式：资料编译成 wiki
- 产物：Obsidian 研究库
- 工具：Claude、Obsidian；是否需要 MCP：不需要
- 依赖：依赖 Obsidian
- 评分：★★☆☆☆（2/5）
- 原文存档：[原文](raw/web/07-notes/felipesinisterra-blog-how-i-set-up-my-second-brain-for-research-with-a.md)

**做法。**讲他怎么按 Karpathy 的思路搭研究用的第二大脑，用 AI 维护资料间的链接。

**可借鉴。**可参考目录设计。

## [Notesmakr：用 Obsidian 学习](https://notesmakr.com/blog/how-to-use-obsidian-for-studying)

- 作者：Notesmakr（博客）
- 方式：笔记加间隔复习
- 产物：Obsidian 笔记
- 工具：Obsidian；是否需要 MCP：不需要
- 依赖：依赖 Obsidian
- 评分：★★☆☆☆（2/5）
- 原文存档：[原文](raw/web/07-notes/notesmakr-blog-how-to-use-obsidian-for-studying.md)

**做法。**一篇 Obsidian 学习指南，说得很直接：漂亮的关系图不等于记住，没有间隔复习，第二大脑就是一台精美的重读机器。

**可借鉴。**这句话可以作为所有笔记方案的警示。

## [jbranchaud/til](https://github.com/jbranchaud/til)

- 作者：Josh Branchaud（GitHub）
- 方式：学完留一条
- 产物：每条一个 md
- 工具：GitHub；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★☆☆☆（2/5）
- 原文存档：[原文](raw/web/07-notes/github-jbranchaud-til.md)

**做法。**与上一条同类的 TIL 仓库，按技术分目录。

**可借鉴。**目录分法可参考。

## [Readeck](https://readeck.org/)

- 作者：Readeck（产品）
- 方式：稍后读、高亮
- 产物：高亮、文章存档
- 工具：自托管服务；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★☆☆☆（2/5）
- 原文存档：[原文](raw/web/07-notes/readeck.md)

**做法。**自托管的稍后读工具，支持高亮和视频字幕。它不是间隔复习工具，在学习流程里负责"收集"。

**可借鉴。**先收集、再消化，把信息流和学习流分开。
