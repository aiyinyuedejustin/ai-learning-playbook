# 交互式讲解与 HTML

文字讲不懂时，让 AI 做一个能动手玩的页面、动画或模拟。这一类收集了这种做法的理由、示例和代价（更费 token、错误答案也会显得更可信）。用好交互讲解的通用三步是：先预测，改一个输入，再用自己的话解释结果。

本类共 16 条，按评分从高到低排列。

## [Geoffrey Litt：Understanding is the new bottleneck](https://www.geoffreylitt.com/2026/07/02/understanding-is-the-new-bottleneck.html)

- 作者：Geoffrey Litt（博客）
- 方式：讲解文档、测验、微型世界
- 产物：讲解文档、测验、交互微世界
- 工具：任意 agent；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★★★（5/5）
- 原文存档：[原文](raw/web/05-html/geoffreylitt-2026-07-02-understanding-is-the-new-bottleneck-html.md)

**做法。**他在 AI Engineer 大会上的演讲文字版：当 agent 写越来越多的代码，人的瓶颈变成"理解"，要理解才能参与。他给出几种让 AI 帮你理解的技术：让它写讲解文档、出测验、做可以玩的微型世界。Explain This 等工具就是受它启发。

**可借鉴。**把"理解"当成一个需要专门投入的环节，而不是写代码的副产品。

## [Using Claude Code: The unreasonable effectiveness of HTML](https://claude.com/blog/using-claude-code-the-unreasonable-effectiveness-of-html)

- 作者：Thariq（Anthropic）（官方博客）
- 方式：交互讲解
- 产物：单文件 HTML
- 工具：Claude Code（任意模型可做）；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★★☆（4/5）
- 原文存档：[原文](raw/web/05-html/claude-blog-using-claude-code-the-unreasonable-effectiveness-of-html.md)

**做法。**主张让 agent 输出 HTML 而不是 md：可以放 SVG 图、交互控件、页内导航。代价是 token 更多、生成更慢、diff 难审。

**可借鉴。**讲解类内容用 HTML，需要长期维护的笔记仍用 md。

## [Laurentiu Raducu：How I use LLMs to learn complex topics](https://laurentiugabriel.github.io/blog/articles/how-i-use-llms-to-learn)

- 作者：Laurentiu Raducu（博客）
- 方式：知识库、核对准确性、做模拟游戏
- 产物：知识库、GitHub Pages 上的模拟游戏
- 工具：编码 agent（plan 模式）；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★★☆（4/5）
- 原文存档：[原文](raw/web/05-html/laurentiugabriel-blog-articles-how-i-use-llms-to-learn.md)

**做法。**他先用 plan 模式让 AI 建一份主题知识库，再专门检查它的准确性；然后让 AI 做一个低多边形风格的模拟游戏（例如讲芯片产业的 ChipTycoon），发布在 GitHub Pages 上，并在游戏里加挑战。HN 约 830 分。高赞评论有两类：读 LLM 的长文很累；希望作者展示"现在能解决什么以前解决不了的问题"。

**可借鉴。**"做一个能玩的模拟"是把被动阅读变成主动探索的好办法；评论区的"展示你能解决什么"可以当验收标准。

## [html-effectiveness 示例集](https://thariqs.github.io/html-effectiveness/)

- 作者：Thariq（网页）
- 方式：交互讲解
- 产物：HTML 示例
- 工具：无；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★☆☆（3/5）
- 原文存档：[原文](raw/web/05-html/thariqs-html-effectiveness.md)

**做法。**上一篇文章配套的示例页面集合，展示了交互图、可调参数的演示等。

**可借鉴。**想给 AI 一个"做成这样"的参考时可以直接给链接。

## [X @ozarktrent：在全局提示里要求"适合时做个交互 HTML"](https://x.com/ozarktrent/status/2108076595877691514)

- 作者：ozarktrent（X）
- 方式：交互讲解
- 产物：交互 HTML
- 工具：任意模型；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★☆☆（3/5）
- 原文存档：[帖子全文](raw/x/2108076595877691514.md)

**做法。**他在全局提示里加了一句"如果合适，就做一个交互 HTML 和可视化，让我能触摸式地理解"。他很喜欢效果，但 token 消耗变得很大。

**可借鉴。**"只在合适时"这个条件很重要，否则每个回答都会变成网页。

## [OpenAI：GPT-6 与 Intelligent UI](https://x.com/OpenAI/status/2107894997538525580)

- 作者：OpenAI（X）
- 方式：交互回答
- 产物：交互界面
- 工具：ChatGPT；是否需要 MCP：不需要
- 依赖：依赖 ChatGPT
- 评分：★★★☆☆（3/5）
- 原文存档：[帖子全文](raw/x/2107894997538525580.md)

**做法。**ChatGPT 的回答本身可以是可视化和可交互的界面，约 2.4 万赞。评论区有两条对学习有用的建议：让学习者先预测、改一个输入、再用自己的话解释结果；交互式答案也会让错误答案看起来更可信，需要附上"怎么算出来的"。

**可借鉴。**"先预测、改输入、再解释"是用好任何交互演示的三步法。

## [X @MaxLenormand：Zarr 格式的交互讲解](https://x.com/MaxLenormand/status/2079556266880315564)

- 作者：MaxLenormand（X）
- 方式：交互探索
- 产物：交互讲解网页
- 工具：任意编码 agent；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★☆☆（3/5）
- 原文存档：[帖子全文](raw/x/2079556266880315564.md)

**做法。**他说自己靠动手玩来学，所以做了一个可交互的页面讲解 Zarr 数据格式怎么工作。

**可借鉴。**把"做一个交互讲解"本身当成学习任务，做的过程就是学。

## [Cognitive debt is leverage](https://vivekhaldar.com/articles/cognitive-debt-is-leverage)

- 作者：Vivek Haldar（博客）
- 方式：观点
- 产物：无
- 工具：无；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★☆☆（3/5）
- 原文存档：[原文](raw/web/05-html/vivekhaldar-articles-cognitive-debt-is-leverage.md)

**做法。**回应 Geoffrey Litt 的演讲。他认为"认知债"（agent 写代码比我们理解得快）不一定是坏事，就像财务杠杆，可以有意识地承担，在需要时再偿还，也就是在关键处补理解。

**可借鉴。**提醒自己：不必理解一切，但要知道哪些地方必须理解。

## [Show HN: learn-thing，用 AI 生成学习思维导图](https://news.ycombinator.com/item?id=41898076)

- 作者：aotakeda（HN）
- 方式：思维导图
- 产物：带链接的思维导图
- 工具：网页应用、Ollama 或在线模型；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★☆☆（3/5）
- 原文存档：[原文](raw/web/05-html/news-item-id-41898076.md)

**做法。**输入一个主题，LLM 生成一张学习思维导图，每个子主题带学习链接，可以接本地模型。HN 约 170 分。评论里有人希望它能变成"进度地图"，加上自己的笔记并推荐资料。

**可借鉴。**思维导图可以作为摸底前的"领域地图"。

## [HN：How I use LLMs to learn complex topics 讨论](https://news.ycombinator.com/item?id=49234675)

- 作者：HN 用户（HN）
- 方式：讨论
- 产物：无
- 工具：无；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★☆☆（3/5）
- 原文存档：[原文](raw/web/05-html/news-item-id-49234675.md)

**做法。**上一篇文章的讨论串，约 830 分。有人说读 LLM 文字很累、分支太多需要组织方式；有人吐槽这已经是第五十篇"我怎么用 LLM 学习"，却没有一篇展示学完之后能做什么。

**可借鉴。**"学完能做什么"是这类方法最常缺的部分。

## [interactive-illustration-skill：科学可视化学习（中文）](https://github.com/ywrnpwvp89-dev/interactive-illustration-skill)

- 作者：ywrnpwvp89-dev（GitHub）
- 方式：科学可视化
- 产物：交互插图
- 工具：Claude Code 等；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★☆☆☆（2/5）
- 原文存档：[原文](raw/web/05-html/github-ywrnpwvp89-dev-interactive-illustration-skill.md)

**做法。**面向医学、生物、化学、物理、工程、数学的科学视觉学习 skill，生成交互插图。星数少。

**可借鉴。**理科概念配交互图的现成提示。

## [Claude artifacts 说明](https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them)

- 作者：Anthropic（官方文档）
- 方式：交互讲解
- 产物：artifact 页面
- 工具：Claude；是否需要 MCP：不需要
- 依赖：依赖 Claude
- 评分：★★☆☆☆（2/5）
- 原文存档：[原文](raw/web/05-html/support-en-articles-17153992-what-are-artifacts-and-how-do-i-use-them.md)

**做法。**说明 Claude 的 artifacts 怎么用，包括把交互页面发布出来分享。

**可借鉴。**做好的讲解页可以发布成链接，方便以后复习。

## [aotakeda/learn-thing](https://github.com/aotakeda/learn-thing)

- 作者：aotakeda（GitHub）
- 方式：思维导图
- 产物：思维导图
- 工具：Next.js、Ollama；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★☆☆☆（2/5）
- 原文存档：[原文](raw/web/05-html/github-aotakeda-learn-thing.md)

**做法。**上一条的开源仓库。

**可借鉴。**可以自己部署。

## [jingx8885/lovjpn：日语歌逐句拆解学习页（中文）](https://github.com/jingx8885/lovjpn)

- 作者：jingx8885（GitHub）
- 方式：逐句拆解、跟读
- 产物：学习网页（对齐表、跟读、原曲同步）
- 工具：任意 agent；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★☆☆☆（2/5）
- 原文存档：[原文](raw/web/05-html/github-jingx8885-lovjpn.md)

**做法。**面向中文母语者的日语学习 skill，把任意日文或日语歌生成逐句拆解、对齐表、跟读练习，并和原曲同步的学习页。

**可借鉴。**"用自己喜欢的材料生成学习页"能提高动机。

## [X @baotiao 转发 Understanding is the new bottleneck](https://x.com/baotiao/status/2088148152822251636)

- 作者：baotiao（X）
- 方式：转发
- 产物：无
- 工具：无；是否需要 MCP：不需要
- 依赖：通用
- 评分：★☆☆☆☆（1/5）
- 原文存档：[帖子全文](raw/x/2088148152822251636.md)

**做法。**转发 Geoffrey Litt 文章的帖子，约 400 赞、480 收藏，说明这篇在中文技术圈也传播很广。

**可借鉴。**直接读原文即可。

## [shawnancy/lang33：33 天语言自学网站生成器](https://github.com/shawnancy/lang33)

- 作者：shawnancy（GitHub）
- 方式：句型练习
- 产物：语言自学网站
- 工具：网站生成器、AI 导师；是否需要 MCP：不需要
- 依赖：通用
- 评分：★☆☆☆☆（1/5）
- 原文存档：[原文](raw/web/05-html/github-shawnancy-lang33.md)

**做法。**生成一个 33 天的语言自学网站，包括句型工作台、可核验的数据管线、双语界面和多个 AI 导师角色。0 星。

**可借鉴。**"把一门课生成成一个网站"的又一例子。
