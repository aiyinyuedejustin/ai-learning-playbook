# 读资料与 NotebookLM

这一类是"手上有一堆资料，怎么借 AI 读进去"。NotebookLM 是最常见的工具，但几位作者都提醒：AI 画好的导图会替你跳过整理这一步，而整理本身就是学习；更好的用法是让它出卷、考你。另有几个把资料变成可溯源知识库的开源工具。

本类共 18 条，按评分从高到低排列。

## [Justin Sung：用 NotebookLM 学得更快](https://www.youtube.com/watch?v=LBQz1KmFOUc)

- 作者：Justin Sung（YouTube）
- 方式：读资料、精确提问
- 产物：NotebookLM 的导图、闪卡、测验
- 工具：NotebookLM；是否需要 MCP：不需要
- 依赖：依赖 NotebookLM
- 评分：★★★★☆（4/5）
- 原文存档：[视频字幕全文](raw/transcripts/LBQz1KmFOUc.md)

**做法。**他认为 NotebookLM 准确性高、视频概览不错，但在他熟悉的领域里，AI 生成的思维导图"分类有逻辑但没意义"，双人播客不分轻重，闪卡和测验没有间隔调度。核心警告是：整理信息的过程本身就是学习，拿 AI 画好的导图来学，等于跳过了这部分思考。建议在设置里打开默认关闭的 Learning Guide（[38:15](https://www.youtube.com/watch?v=LBQz1KmFOUc&t=2295s)），并且先找出自己的缺口再带着具体问题去问。

**可借鉴。**导图最好自己画、至少自己改；AI 生成的结构只当参考。

## [James Blue：用 NotebookLM 学任何东西的完整流程](https://www.youtube.com/watch?v=TBKjg9ObgY4)

- 作者：James Blue（YouTube）
- 方式：预热、看结构、追问、自测、讲出来
- 产物：音频概览、思维导图、信息图、学习指南、幻灯片
- 工具：NotebookLM；是否需要 MCP：不需要
- 依赖：依赖 NotebookLM
- 评分：★★★★☆（4/5）
- 原文存档：[视频字幕全文](raw/transcripts/TBKjg9ObgY4.txt)

**做法。**四步：上传资料后先听音频概览预热，再读原文；用视频概览、思维导图和信息图看清结构，检查信息图有没有错本身就是一次深加工；散步时听深度对谈，用互动模式插话追问"为什么"，再生成学习指南做简答题；最后做闪卡和跨来源混合测验，生成幻灯片对着空房间讲一遍，卡住就回去补。

**可借鉴。**"检查 AI 做的信息图有没有错"和"对着幻灯片讲一遍"是两个把被动材料变成主动练习的动作。

## [X @agintender：NotebookLM 以试代学（中文）](https://x.com/agintender/status/2036282274048868512)

- 作者：agintender（X）
- 方式：检索练习、分级试卷
- 产物：初中高三套试卷、讲解视频
- 工具：NotebookLM；是否需要 MCP：不需要
- 依赖：依赖 NotebookLM
- 评分：★★★★☆（4/5）
- 原文存档：[帖子全文](raw/x/2036282274048868512.md)

**做法。**让 NotebookLM 按初级、中级、高级出三套卷，放进历年真题，刷完再让它生成讲解视频复盘。约 470 赞。评论区一针见血："底层是主动回忆，提取练习本身就是最强的巩固方式。"

**可借鉴。**把 NotebookLM 的用法从"总结"换成"出卷"。

## [karpathy/reader3：读书三遍法](https://github.com/karpathy/reader3)

- 作者：Andrej Karpathy（GitHub）
- 方式：先自己读、再让 LLM 讲、再问答
- 产物：本地阅读器
- 工具：本地网页阅读器、任意 LLM；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★★☆（4/5）
- 原文存档：[原文](raw/web/06-read/github-karpathy-reader3.md)

**做法。**一个很轻的本地 EPUB 阅读器，方便把章节复制给 LLM。他的读书方法是三遍：先自己读一遍，再让 LLM 解释和总结，最后做问答。约 3.9k 星。

**可借鉴。**"先自己读"这一步放在 AI 前面，避免一上来就看总结。

## [learn-from-materials：把资料变成可溯源的知识库](https://github.com/dmoshehun-prog/learn-from-materials)

- 作者：dmoshehun-prog（GitHub）
- 方式：资料建库、可溯源
- 产物：离线学习网页、md
- 工具：任意 agent skill；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★★☆（4/5）
- 原文存档：[原文](raw/web/06-read/github-dmoshehun-prog-learn-from-materials.md)

**做法。**把 PDF、书、PPT、网页变成可溯源的知识库，同时输出离线学习网页和 md，并且把原文事实和模型补充的内容分开标注。约 1k 星。

**可借鉴。**"原文事实和模型补充分开标注"是防幻觉的好办法。

## [YuJunZhiXue/StudyAnalysis-Skills（Knowledge Absorber，中文）](https://github.com/YuJunZhiXue/StudyAnalysis-Skills)

- 作者：YuJunZhiXue（GitHub）
- 方式：深读、真理锚定、导师模式
- 产物：md 与 HTML"知识晶体"、侧栏测验
- 工具：Claude Code 等；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★★☆（4/5）
- 原文存档：[原文](raw/web/06-read/github-yujunzhixue-studyanalysis-skills.md)

**做法。**读链接、文档或代码，先做"真理锚定"校验，再用叙事方式输出 md 加 HTML 的"知识晶体"。后来加了导师模式，针对晶体内容追问，防止"看完记不住"。约 630 星，linux.do 上常被推荐。

**可借鉴。**"读完马上被追问"把阅读变成检索练习。

## [Tina Huang：我怎么用 AI 快速学东西](https://www.youtube.com/watch?v=TUalmf9bByA)

- 作者：Tina Huang（YouTube）
- 方式：目标、找资料、先做题预热、逐层加深、落地
- 产物：学习指南、单人播客稿
- 工具：Perplexity、NotebookLM、AI Studio；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★☆☆（3/5）
- 原文存档：[视频字幕全文](raw/transcripts/TUalmf9bByA.md)

**做法。**五步框架：定目标；用 Perplexity 搜 Reddit 上别人用过的资料（[14:20](https://www.youtube.com/watch?v=TUalmf9bByA&t=860s)）；用 NotebookLM 生成学习指南并先做题预热；一层一层加深；最后落地做项目。她让 AI 写只保留定义、概念和完整例子的单人播客稿，然后 2–3 倍速听（[16:54](https://www.youtube.com/watch?v=TUalmf9bByA&t=1014s)），因为觉得双人播客太水。视频有赞助段落。

**可借鉴。**"先做题再学"的预热，以及把资料改写成自己偏好的形式。

## [X @jinglian：NotebookLM 只读了 4 本书中的 1 本（中文）](https://x.com/jinglian/status/2009428326989877696)

- 作者：jinglian（X）
- 方式：实测
- 产物：PPT
- 工具：NotebookLM；是否需要 MCP：不需要
- 依赖：依赖 NotebookLM
- 评分：★★★☆☆（3/5）
- 原文存档：[帖子全文](raw/x/2009428326989877696.md)

**做法。**他让 NotebookLM 根据 4 本书做 PPT，结果发现它实际上只用了其中 1 本的内容。

**可借鉴。**多份长资料时要检查它是否真的用了每一份。

## [Karpathy：把 LLM 送去上学（讲解、例题、练习）](https://x.com/karpathy/status/1885026028428681698)

- 作者：Andrej Karpathy（X）
- 方式：观点
- 产物：无
- 工具：无；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★☆☆（3/5）
- 原文存档：[帖子全文](raw/x/1885026028428681698.md)

**做法。**他说教科书由三部分组成：讲解、例题和练习题，训练 LLM 也应该如此，而练习题是最缺的。反过来看，人学习时也不能只读讲解和例题。

**可借鉴。**"讲解、例题、练习"三件套是检查一份学习材料是否完整的简单标准。

## [vitalysim/the-knowledge-guy：把一本书变成 skill](https://github.com/vitalysim/the-knowledge-guy)

- 作者：vitalysim（GitHub）
- 方式：书变 skill、两层结构
- 产物：两层 Claude Code skill（约 3K token 概念图）
- 工具：Claude Code；是否需要 MCP：不需要
- 依赖：依赖 Claude Code
- 评分：★★★☆☆（3/5）
- 原文存档：[原文](raw/web/06-read/github-vitalysim-the-knowledge-guy.md)

**做法。**把一本 PDF 或 EPUB 用 map-reduce 处理，变成一个两层的 Claude Code skill：上层是约 3K token 的概念地图，下层是按需加载的章节细节。约 27 星。

**可借鉴。**"约 3K token 的概念地图"可以作为一本书的速查表格式。

## [Show HN: Bloomy，K-12 的 AI 掌握学习](https://news.ycombinator.com/item?id=48981136)

- 作者：Alex Southmayd（HN）
- 方式：诊断缺口、个性化路径、苏格拉底导师
- 产物：学习路径、课程
- 工具：Bloomy 平台；是否需要 MCP：不需要
- 依赖：依赖该产品
- 评分：★★★☆☆（3/5）
- 原文存档：[原文](raw/web/06-read/news-item-id-48981136.md)

**做法。**YC 公司 Bloomy 的发布帖：先诊断学生的技能缺口，放到个性化路径上，配合标准对齐的课程和一个不直接给答案的苏格拉底 AI 导师，目标是用 AI 解决 Bloom 的"2 sigma 问题"。HN 约 100 分。

**可借鉴。**"诊断、路径、导师"三件套就是 Skycak 那套方法的产品化。

## [NotebookLM 学生功能介绍](https://blog.google/innovation-and-ai/models-and-research/google-labs/notebooklm-student-features/)

- 作者：Google（官方）
- 方式：读资料、自测
- 产物：闪卡、测验、学习指南
- 工具：NotebookLM；是否需要 MCP：不需要
- 依赖：依赖 NotebookLM
- 评分：★★☆☆☆（2/5）
- 原文存档：[原文](raw/web/06-read/blog-innovation-and-ai-models-and-research-google-labs-notebooklm-stud.md)

**做法。**官方介绍 NotebookLM 给学生的功能：从上传的资料生成闪卡、测验和学习指南。

**可借鉴。**了解功能边界用。

## [NotebookLM 闪卡与测验帮助页](https://support.google.com/gemininotebook/answer/16958963?hl=en)

- 作者：Google（官方文档）
- 方式：自测
- 产物：闪卡、测验
- 工具：NotebookLM；是否需要 MCP：不需要
- 依赖：依赖 NotebookLM
- 评分：★★☆☆☆（2/5）
- 原文存档：[原文](raw/web/06-read/support-gemininotebook-answer-16958963-hl-en.md)

**做法。**说明怎样在 NotebookLM 里生成和使用闪卡与测验。

**可借鉴。**确认导出能力时查这里。

## [wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)

- 作者：wwwzhouhui（GitHub）
- 方式：skill 合集
- 产物：多种 skill
- 工具：Claude Code；是否需要 MCP：不需要
- 依赖：依赖 Claude Code
- 评分：★★☆☆☆（2/5）
- 原文存档：[原文](raw/web/06-read/github-wwwzhouhui-skills-collection.md)

**做法。**Claude skill 合集，其中有 Knowledge Absorber 的变体。约 280 星。

**可借鉴。**找中文 skill 时的一个入口。

## [Claude Code + NotebookLM（B 站，中文配音）](https://www.bilibili.com/video/BV1BuPPzqE6A)

- 作者：云桥网络（转载）（Bilibili）
- 方式：资料收集外包、生成学习产物
- 产物：信息图、闪卡、幻灯片
- 工具：Claude Code、NotebookLM（非官方 API）；是否需要 MCP：不需要
- 依赖：依赖 NotebookLM
- 评分：★★☆☆☆（2/5）
- 原文存档：[视频字幕全文](raw/transcripts/BV1BuPPzqE6A.md)

**做法。**一个中文配音的转载视频。演示用 Claude Code 的 YouTube 搜索 skill 找视频（[01:10](https://www.bilibili.com/video/BV1BuPPzqE6A?t=70)），再通过一个非官方的 NotebookLM 接口把链接全部丢进 NotebookLM 分析，生成信息图（[02:10](https://www.bilibili.com/video/BV1BuPPzqE6A?t=130)）。安装过程见 [05:31](https://www.bilibili.com/video/BV1BuPPzqE6A?t=331)。最后提到闪卡、思维导图、音频摘要都能这样让 Claude Code 代为生成（[09:06](https://www.bilibili.com/video/BV1BuPPzqE6A?t=546)）。重点在研究流程，学习环节很少。

**可借鉴。**"重活交给 NotebookLM，agent 只负责调度"能省 token；但要知道非官方接口可能失效。

## [X @AiWithAyesha：用 NotebookLM 做主动学习的 7 个提示](https://x.com/AiWithAyesha/status/2111041089566392803)

- 作者：AiWithAyesha（X）
- 方式：费曼、二八、主动回忆、概念图
- 产物：提示词
- 工具：NotebookLM；是否需要 MCP：不需要
- 依赖：依赖 NotebookLM
- 评分：★☆☆☆☆（1/5）
- 原文存档：[帖子全文](raw/x/2111041089566392803.md)

**做法。**把费曼技巧、二八法则、主动回忆、间隔复习、概念图和自测各写成一个 NotebookLM 提示。约 90 赞。属于模板化的"7 个提示"帖子。

**可借鉴。**提示本身不坏，但信息量低。

## [X @aiSkillMarket：推荐 learn-from-materials（中文）](https://x.com/aiSkillMarket/status/2103150345861890069)

- 作者：aiSkillMarket（X）
- 方式：推荐
- 产物：无
- 工具：无；是否需要 MCP：不需要
- 依赖：通用
- 评分：★☆☆☆☆（1/5）
- 原文存档：[帖子全文](raw/x/2103150345861890069.md)

**做法。**介绍 learn-from-materials 的推荐帖，说它不是总结 PDF，而是把一堆资料变成可以继续学习的知识库。0 赞，账号名像 skill 推广号。

**可借鉴。**直接看仓库。

## [hx101700/memoflow：录音转写 skill](https://github.com/hx101700/memoflow)

- 作者：hx101700（GitHub）
- 方式：录音转写
- 产物：Word、Excel、md 转写稿
- 工具：Codex、Qwen-Audio；是否需要 MCP：不需要
- 依赖：依赖 Codex
- 评分：★☆☆☆☆（1/5）
- 原文存档：[原文](raw/web/06-read/github-hx101700-memoflow.md)

**做法。**交互式录音转写 skill，用 Codex 加 Qwen-Audio 生成 Word、Excel 和 md 草稿。和学习的关系是：讲座或课堂录音可以先转成文字再学。

**可借鉴。**把音频材料变成可检索的文字。
