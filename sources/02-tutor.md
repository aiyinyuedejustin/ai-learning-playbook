# 一对一授课与苏格拉底

这一类来源讨论 AI 在授课时该怎么说话：一次只问一个问题，先让你试再给提示，不接受"我懂了"，卡住时退回去讲。有的是长期课程工作区，有的只是一段系统提示。它们的差别主要在三处：讲多少、问多少、什么时候停。

本类共 44 条，按评分从高到低排列。

## [Nick Saraev：让 AI 扮演 9 种角色](https://www.youtube.com/watch?v=FSXHk4hMrY8)

- 作者：Nick Saraev（YouTube）
- 方式：访谈、地图、苏格拉底、考官、检查、倾听、诊断、陪练、书记
- 产物：无固定产物
- 工具：任意聊天模型；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★★★（5/5）
- 原文存档：[视频字幕全文](raw/transcripts/FSXHk4hMrY8.md)

**做法。**他说多数人只用过"解释者"这一种角色（[03:36](https://www.youtube.com/watch?v=FSXHk4hMrY8&t=216s)）。另外八种是（访谈者和地图绘制者从 [07:54](https://www.youtube.com/watch?v=FSXHk4hMrY8&t=474s) 开始，倾听者和诊断者从 [17:01](https://www.youtube.com/watch?v=FSXHk4hMrY8&t=1021s) 开始）：访谈者（先问清目标、水平和考核方式）、地图绘制者、苏格拉底提问者、考官（逐题加难直到你答错）、检查者（只查过程，不改写）、倾听者（你口述、画图、写摘要，它对照原文打分）、诊断者（读你最近 N 次对话，找出反复出现的同一个误解）、陪练、书记员（整理你的乱笔记但不添内容）。他还要求 AI 帮你通过之后，回到起点不看提示再做一遍。

**可借鉴。**"诊断者读最近几次对话找同一个误解"和"通过后不看提示重做"是两个很少见、但很容易落地的动作。

## [mattpocock/skills：/teach 与 /grill-me](https://github.com/mattpocock/skills)

- 作者：Matt Pocock（GitHub）
- 方式：有状态课程工作区、最近发展区、追问对齐
- 产物：MISSION.md、RESOURCES.md、lessons/*.html、learning-records/、reference/
- 工具：任意读 SKILL.md 的 agent（npx skills add）；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★★★（5/5）
- 原文存档：[原文](raw/web/02-tutor/github-mattpocock-skills.md)

**做法。**`/teach` 把当前目录当成一门课的工作区：先问清你为什么学，写进 MISSION.md；强制外搜高可信资料写进 RESOURCES.md，不信模型的参数记忆；然后按最近发展区每次出一节 HTML 短课，课后写一条 learning-record 决定下一课学什么。`/grill-me` 是另一个 skill，一轮轮追问直到双方对计划的理解一致。整仓星数很高。

**可借鉴。**"目录即课程"和"先钉动机再找资料"是它最值得借的两点。评论区指出它缺掌握度验收和前置检测，用的时候要自己补上摸底和放行规则。

## [Matt Pocock："从初级到高级"用法帖及评论区批评](https://x.com/mattpocockuk/status/2064663221718425660)

- 作者：Matt Pocock（X）
- 方式：有状态课程工作区
- 产物：HTML 课
- 工具：任意 agent；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★★★（5/5）
- 原文存档：[帖子全文](raw/x/2064663221718425660.md)

**做法。**用法很简单：装好 /teach，新建一个工作目录，说 `/teach me ...`，然后一直跟着学。约 4.3k 赞、7k 收藏。评论区的批评集中在三点：没有掌握度测量（"他们怎么验证自己学会了"）；第一课满是没解释的缩写；前置知识检测才是难点，光讲得漂亮不会迁移。Pocock 的回应是"它还没摸到你的最近发展区，告诉它你没懂，它会调整"。

**可借鉴。**这组批评正好是一份"学习 skill 必须补的功能清单"：摸底、术语首次出现就解释、掌握才放行。

## [Explain This（@daniel_mac8）](https://x.com/daniel_mac8/status/2078146026993594727)

- 作者：Dan Mac（X）
- 方式：学习者画像、锚定已有知识的讲解、测验转卡
- 产物：LEARNER.md、Obsidian 讲解笔记、SRS 卡
- 工具：Claude Code skill、Obsidian；是否需要 MCP：不需要
- 依赖：依赖 Obsidian，思路通用
- 评分：★★★★★（5/5）
- 原文存档：[帖子全文](raw/x/2078146026993594727.md)

**做法。**先花 10 分钟访谈你，生成一份 LEARNER.md 画像。之后对任何论文或 PDF，写一篇锚定你已有知识的讲解，直接写进 Obsidian。每篇末尾有测验并打分，答错的题自动转成间隔复习卡，下周说"quiz me"再考。灵感来自 Geoffrey Litt 的演讲，约 250 赞、370 收藏。

**可借鉴。**LEARNER.md 这种"画像文件"可以复用到所有学习 skill；"只把答错的题变成卡"能大幅减少无效卡。

## [Claude Code output styles（Learning / Explanatory）](https://code.claude.com/docs/en/output-styles)

- 作者：Anthropic（官方文档）
- 方式：边做边学、讲解
- 产物：代码里的 TODO(human)
- 工具：Claude Code；是否需要 MCP：不需要
- 依赖：依赖 Claude Code
- 评分：★★★★☆（4/5）
- 原文存档：[原文](raw/web/02-tutor/code-docs-en-output-styles.md)

**做法。**Learning 风格会在回答里加 Insight 讲解，遇到有设计取舍的地方留下 `TODO(human)`，让你写 5–10 行再点评。Explanatory 只讲解不让你动手。设置写在 `~/.claude/settings.json` 的 `outputStyle`。

**可借鉴。**"在关键位置留空让人写"这个机制不依赖 Claude Code，任何 agent 都可以按这条规则执行。

## [X @gabriel1：征集"学得更快"的 custom instructions](https://x.com/gabriel1/status/1915161838129746270)

- 作者：gabriel1（X）
- 方式：提问技巧
- 产物：无
- 工具：任意聊天模型；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★★☆（4/5）
- 原文存档：[帖子全文](raw/x/1915161838129746270.md)

**做法。**他征集大家用来加速学习的自定义指令，评论区给出了不少小技巧：不问"X 是什么"而问"没有 X 会怎样"；在多个抽象层次分别解释；让 AI 扮演三个水平不同的学生，你当老师；卡住时先自己想一个类比再问对不对；先学会领域里的关键词。

**可借鉴。**这些技巧都很便宜，可以整理成一张"提问清单"放进 skill。

## [X @lukasen_xyz：反向费曼，讲给 AI 听](https://x.com/lukasen_xyz/status/2110867960185434502)

- 作者：lukasen_xyz（X）
- 方式：费曼讲解
- 产物：无
- 工具：任意聊天模型；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★★☆（4/5）
- 原文存档：[帖子全文](raw/x/2110867960185434502.md)

**做法。**先贴一小段原文，然后合上材料用自己的话讲；AI 每次只追问你漏掉的因果；最后把你讲错的地方对回原文的具体位置。他特别提醒，AI 说"你讲对了"不算通过。

**可借鉴。**"只追问漏掉的因果"和"错处对回原文位置"两条规则很具体，可以直接用。

## [Justin Sung：ChatGPT Study Mode 评测](https://www.youtube.com/watch?v=m3jNwwuvqx8)

- 作者：Justin Sung（YouTube）
- 方式：精确提问
- 产物：无
- 工具：ChatGPT Study Mode；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★★☆（4/5）
- 原文存档：[视频字幕全文](raw/transcripts/m3jNwwuvqx8.md)

**做法。**他实测了 4–5 小时：被动提问时，同一个概念卡了 30 分钟，比看 15 分钟 YouTube 还慢；主动找出自己哪里卡、精确描述后再问，2 分钟就通了（[16:30](https://www.youtube.com/watch?v=m3jNwwuvqx8&t=990s)）。他建议先自己学到有具体问题再用，不要顺着末尾"要不要换个方式讲"一路点下去，并且搭配图片。

**可借鉴。**"先定位自己卡在哪，再问"这个前置步骤可以写进每次答疑的规则。

## [Matt Pocock：/teach 发布帖](https://x.com/mattpocockuk/status/2063988995692900439)

- 作者：Matt Pocock（X）
- 方式：有状态课程工作区
- 产物：HTML 课
- 工具：任意 agent（npx skills add）；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★★☆（4/5）
- 原文存档：[帖子全文](raw/x/2063988995692900439.md)

**做法。**发布帖说可以学任何东西，从魔方到和声到软件基础，安装命令是 `npx skills add mattpocock/skills --skill teach`。约 2.8k 赞。评论区有人左边终端、右边 Godot、副屏放它生成的 HTML 课；也有人先 `/grill-me` 再 `/teach`。

**可借鉴。**"先 grill-me 对齐再 teach"的连用顺序可以直接采用。

## [kirilxd/claude-tutor](https://github.com/kirilxd/claude-tutor)

- 作者：kirilxd（GitHub）
- 方式：规划、讲授、测验、间隔复习
- 产物：学习计划、测验、复习日历、Web 面板
- 工具：Claude Code；是否需要 MCP：不需要
- 依赖：依赖 Claude Code
- 评分：★★★★☆（4/5）
- 原文存档：[原文](raw/web/02-tutor/github-kirilxd-claude-tutor.md)

**做法。**`/learn <主题>` 生成带资料的学习计划，然后讲课，`/quiz` 出自适应测验，按 SM-2 排复习，`/review` 做到期复习，还有一个 Web 面板看进度。约 140 星。

**可借鉴。**"计划、讲、考、排程"一条完整闭环，适合作为学习 skill 的最小功能集合参考。

## [bevibing/tutor-skills](https://github.com/bevibing/tutor-skills)

- 作者：bevibing（GitHub）
- 方式：资料建库、每轮出题、掌握追踪
- 产物：Obsidian StudyVault
- 工具：Claude Code、Obsidian；是否需要 MCP：不需要
- 依赖：依赖 Obsidian
- 评分：★★★★☆（4/5）
- 原文存档：[原文](raw/web/02-tutor/github-bevibing-tutor-skills.md)

**做法。**`/tutor-setup` 把你的资料生成一个 Obsidian StudyVault，`/tutor` 每轮出 4 道题、评分，并追踪每个概念的掌握程度。约 1.3k 星。

**可借鉴。**"每轮固定 4 题"让测验有稳定节奏，不会变成随兴聊天。

## [SenmuuuuW/universal-diagnostic-tutor-skill（中文）](https://github.com/SenmuuuuW/universal-diagnostic-tutor-skill)

- 作者：SenmuuuuW（GitHub）
- 方式：诊断卡点、掌握证据
- 产物：无固定产物
- 工具：任意 agent；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★★☆（4/5）
- 原文存档：[原文](raw/web/02-tutor/github-senmuuuuw-universal-diagnostic-tutor-skill.md)

**做法。**先判断你卡在前置概念、符号还是推理，再决定接下来是讲、问、练还是停。进下一步之前要有掌握的证据。约 250 星。

**可借鉴。**"卡点分三类"是很实用的诊断框架：前置没懂就补前置，符号不熟就补符号，推理不通才需要讲。

## [robotsatemyhomework：用 Claude 做一个不接受"我懂了"的导师](https://robotsatemyhomework.substack.com/p/the-ai-tutor-i-built-in-claude-that)

- 作者：Mia Kiraki（Substack）
- 方式：检索练习、苏格拉底
- 产物：Claude Project 指令
- 工具：Claude Projects；是否需要 MCP：不需要
- 依赖：依赖 Claude Projects，可移植
- 评分：★★★★☆（4/5）
- 原文存档：[原文](raw/web/02-tutor/robotsatemyhomework-p-the-ai-tutor-i-built-in-claude-that.md)

**做法。**她用 Claude Projects 搭了一个导师，核心规则是不接受"我懂了"，必须让你用自己的话说出来或做出来。文章列了用 AI 学习的四个陷阱，并引用了检索练习研究中 56% 对 42% 的保持率差异。指令可以直接复制。

**可借鉴。**"我懂了"不算数，必须给证据——这条可以作为每节课的结束条件。

## [Mr. Ranedeer AI Tutor](https://github.com/JushBJJ/Mr.-Ranedeer-AI-Tutor)

- 作者：JushBJJ（GitHub）
- 方式：个性化讲授
- 产物：无（对话）
- 工具：ChatGPT（GPT-4 时代）；是否需要 MCP：不需要
- 依赖：依赖 ChatGPT，已停更
- 评分：★★★☆☆（3/5）
- 原文存档：[原文](raw/web/02-tutor/github-jushbjj-mr-ranedeer-ai-tutor.md)

**做法。**一个可定制的长提示词，让 GPT-4 按你选的深度、学习风格、语气和推理框架来教你，有配置命令和课程计划。约 3 万星，是早期最出名的"AI 导师提示词"，作者已标注停止维护。

**可借鉴。**它的"深度等级 + 学习风格 + 语气"几个可调旋钮，可以变成自己 skill 里的偏好字段。

## [Crafting a Semi-Socratic Tutor with ChatGPT](https://www.socraticarts.com/blog/crafting-a-semi-socratic-tutor-with-chatgpt)

- 作者：Breanne Grover（Socratic Arts）（博客）
- 方式：半苏格拉底
- 产物：提示词
- 工具：ChatGPT；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★☆☆（3/5）
- 原文存档：[原文](raw/web/02-tutor/socraticarts-blog-crafting-a-semi-socratic-tutor-with-chatgpt.md)

**做法。**作者所在公司就叫 Socratic Arts，但她认为只靠提问来教会让人很挫败，所以设计了"半苏格拉底"导师：先问，学习者卡住时就直接讲一点。文章给出了这样设计的理由和提示词结构。

**可借鉴。**"问不出来就讲"是一个重要的退出条件，Eero 的 teach skill 里也有类似规则（精力不足就改讲授）。

## [Assigning AI: Seven Ways of Using AI in Class](https://substack.com/home/post/p-127669714)

- 作者：Ethan Mollick、Lilach Mollick（Substack）
- 方式：导师、教练、对练等七种角色
- 产物：提示词
- 工具：任意聊天模型；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★☆☆（3/5）
- 原文存档：[原文](raw/web/02-tutor/substack-home-post-p-127669714.md)

**做法。**列出 AI 在课堂上的七种角色：导师（增加知识）、教练（增加元认知）、导师型反馈者、队友、工具、模拟器，以及让学生来教的"AI 学生"，重点展开了教练和导师两种并给出提示词。导师提示词要求一次只问一个问题，先问学什么、什么水平、已经知道什么，不直接给答案而是用引导性问题让学生自己生成答案，学生表现出理解后要求他用自己的话解释或举例。他也坦言当时的 AI 导师会编造、会遗忘、不能把知识点连贯地串起来。

**可借鉴。**"一次只问一个问题"这条规则几乎所有好的导师提示词都有，可以放进默认规则。

## [Using AI to make teaching easier & more impactful](https://oneusefulthing.substack.com/p/using-ai-to-make-teaching-easier)

- 作者：Ethan Mollick（Substack）
- 方式：检索练习、间隔、例题、解释
- 产物：提示词
- 工具：任意聊天模型；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★☆☆（3/5）
- 原文存档：[原文](raw/web/02-tutor/oneusefulthing-p-using-ai-to-make-teaching-easier.md)

**做法。**他认为最好的学习方法并没有变，变的是 AI 能帮人准备那些费时的教学材料。文章给了五类提示词：生成多个例子、生成多种解释、找常见误解、出低利害小测、做间隔练习。

**可借鉴。**"让 AI 为同一个概念给多个例子和多种解释"可以用来对付"一种讲法听不懂"。

## [ChatGPT Study Mode 官方介绍](https://openai.com/index/chatgpt-study-mode/)

- 作者：OpenAI（官方）
- 方式：苏格拉底、分步、知识检查
- 产物：无（对话）
- 工具：ChatGPT；是否需要 MCP：不需要
- 依赖：依赖 ChatGPT
- 评分：★★★☆☆（3/5）
- 原文存档：[原文](raw/web/02-tutor/openai-index-chatgpt-study-mode.md)

**做法。**ChatGPT 的学习模式会先了解你的水平，再分步讲、穿插知识检查，不直接给作业答案。进度和记忆留在平台里，你手上没有自己的产物。

**可借鉴。**零配置可用；需要长期跟踪时要另外把学习记录导出成自己的文件。

## [beingMana：给孩子用的 Grok 辅导指令](https://x.com/beingMana/status/2090265695770779809)

- 作者：beingMana（X）
- 方式：苏格拉底、现实应用
- 产物：无（对话）
- 工具：Grok；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★☆☆（3/5）
- 原文存档：[帖子全文](raw/x/2090265695770779809.md)

**做法。**他公开了给孩子用的 Grok 指令：永远不先给答案，先提问、给小提示、确认理解，孩子说"直接告诉我"时也拒绝。另一组指令专门回答"这个知识在现实里怎么用"。

**可借鉴。**连“直接告诉我”都拒绝的强护栏，适合自律差的时候。

## [X @julianboolean_：Math Academy + 苏格拉底式 LLM](https://x.com/julianboolean_/status/2090571881753530735)

- 作者：julianboolean_（X）
- 方式：苏格拉底、直觉讲解
- 产物：无
- 工具：Math Academy + 任意 LLM；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★☆☆（3/5）
- 原文存档：[帖子全文](raw/x/2090571881753530735.md)

**做法。**他觉得 Math Academy 加一个普通 LLM 配苏格拉底提示，组合起来很强。唯一的改动是到了高阶内容时，让 LLM "给直觉"会很有帮助。

**可借鉴。**结构化平台负责顺序和练习，LLM 只负责答疑和直觉，这种分工很清楚。

## [X @gabriel1：学不快是技能问题](https://x.com/gabriel1/status/1913034792398131432)

- 作者：gabriel1（X）
- 方式：追问、复习旧对话
- 产物：无
- 工具：任意聊天模型；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★☆☆（3/5）
- 原文存档：[帖子全文](raw/x/1913034792398131432.md)

**做法。**针对"问 ChatGPT 学不到东西"的说法，他反驳说没人拦着你追问几百次、先想再问、回看旧对话做复习，学不快不是偏好问题，是技能问题。约 2.6k 赞。

**可借鉴。**"回看旧对话做复习"是一个零成本的复习来源。

## [X @drrobcincotta：个人 Journal Club](https://x.com/drrobcincotta/status/2087277731579146502)

- 作者：drrobcincotta（X）
- 方式：被面试、费曼讲解、隔几天再考
- 产物：笔记与链接
- 工具：任意聊天模型；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★☆☆（3/5）
- 原文存档：[帖子全文](raw/x/2087277731579146502.md)

**做法。**他认为让 AI 总结论文是浪费。更好的做法是：你自己读论文，AI 来面试和挑战你，再把你的回答写进笔记并建立链接，几天后再考同一篇。原话是"你思考，AI 只管记录和链接"。

**可借鉴。**读论文时角色反过来：人输出，AI 记录。

## [X @0xqiuqiuu 转述 Lencx：别让 AI 用小白口吻](https://x.com/0xqiuqiuu/status/2049685049818419219)

- 作者：0xqiuqiuu（X）
- 方式：专家视角讲解
- 产物：无
- 工具：任意聊天模型；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★☆☆（3/5）
- 原文存档：[帖子全文](raw/x/2049685049818419219.md)

**做法。**转述 Lencx 在分享会上的观点：多数人让 AI 用小白口吻、多打比方，其实用反了。应该让 AI 用专家视角讲，你看不懂的术语才是该深挖的地方。

**可借鉴。**和"一律讲给 12 岁孩子听"相反的一派，可以作为偏好选项之一。

## [Bhala-Srinivash/agent-tutor-skill](https://github.com/Bhala-Srinivash/agent-tutor-skill)

- 作者：Bhala-Srinivash（GitHub）
- 方式：讲解、例子、检查、练习、间隔复习
- 产物：~/.learn/ 学习档案、复习队列
- 工具：任意 agent；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★☆☆（3/5）
- 原文存档：[原文](raw/web/02-tutor/github-bhala-srinivash-agent-tutor-skill.md)

**做法。**每个概念按"讲解、例子、检查、练习"四步走，概念级记录掌握度，用 FSRS 排复习。可以绑定 PDF、URL 或代码当教材。

**可借鉴。**"概念级掌握度"比"课节级完成度"更细，适合清单式学习。

## [mordor-forge/study-skill](https://github.com/mordor-forge/study-skill)

- 作者：mordor-forge（GitHub）
- 方式：交互学习、间隔复习
- 产物：学习会话、复习调度
- 工具：Claude Code；是否需要 MCP：不需要
- 依赖：依赖 Claude Code
- 评分：★★★☆☆（3/5）
- 原文存档：[原文](raw/web/02-tutor/github-mordor-forge-study-skill.md)

**做法。**交互式学习会话加 FSRS-6 调度。约 46 星。说明比较简短，重点在把复习调度接进会话。

**可借鉴。**可以参考它怎样把 FSRS 状态存在本地文件里。

## [bevibing/socrates-skill](https://github.com/bevibing/socrates-skill)

- 作者：bevibing（GitHub）
- 方式：苏格拉底
- 产物：无（对话）
- 工具：Claude Code；是否需要 MCP：不需要
- 依赖：依赖 Claude Code，可移植
- 评分：★★★☆☆（3/5）
- 原文存档：[原文](raw/web/02-tutor/github-bevibing-socrates-skill.md)

**做法。**只提问、不给答案的苏格拉底 skill。linux.do 有人推荐它，理由是"teach 用着总是不得劲"。约 330 星。

**可借鉴。**想要"逼自己想"时单独开这个，而不是给 teach 加规则。

## [cdmorozov/claude-tutors](https://github.com/cdmorozov/claude-tutors)

- 作者：cdmorozov（GitHub）
- 方式：克制型辅导
- 产物：无（对话）
- 工具：Claude Code；是否需要 MCP：不需要
- 依赖：依赖 Claude Code
- 评分：★★★☆☆（3/5）
- 原文存档：[原文](raw/web/02-tutor/github-cdmorozov-claude-tutors.md)

**做法。**问概念就直接讲，不硬塞测验；做题时一次只给一个提示。约 150 星。

**可借鉴。**提醒设计者：不是所有提问都该触发测验，过度测验也会让人关掉工具。

## [FlorianBruniaux：learning-mode.md（CLAUDE.md 模板）](https://github.com/FlorianBruniaux/claude-code-ultimate-guide/blob/main/examples/claude-md/learning-mode.md)

- 作者：Florian Bruniaux（GitHub）
- 方式：学习模式规则
- 产物：CLAUDE.md
- 工具：Claude Code（可移植到 AGENTS.md）；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★☆☆（3/5）
- 原文存档：[原文](raw/web/02-tutor/github-florianbruniaux-claude-code-ultimate-guide-blob-main-examples-c.md)

**做法。**一份放进 CLAUDE.md 的学习模式模板，规定 AI 在学习场景下先解释思路、让你动手、再点评。所在的仓库是一本 Claude Code 使用指南，约 6k 星。

**可借鉴。**不想装 skill 时，一份 CLAUDE.md 也能把学习规则带进每次会话。

## [mustvlad/ChatGPT-System-Prompts：Socratic Tutor](https://github.com/mustvlad/ChatGPT-System-Prompts/blob/main/prompts/educational/socratic-tutor.md)

- 作者：mustvlad（GitHub）
- 方式：苏格拉底
- 产物：无（对话）
- 工具：任意聊天模型；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★☆☆☆（2/5）
- 原文存档：[原文](raw/web/02-tutor/github-mustvlad-chatgpt-system-prompts-blob-main-prompts-educational-s.md)

**做法。**一段很短的系统提示："你是一个永远用苏格拉底方式回应的导师，从不直接给答案，而是通过提问引导学生自己想出来，并根据学生的知识水平调整问题。"仓库约 1.2k 星，收了不少教育类提示词。

**可借鉴。**最小可用的苏格拉底提示，适合当基线对照。

## [Socratic tutoring（DeepakNess 笔记）](https://deepakness.com/raw/socratic-tutoring)

- 作者：DeepakNess（博客）
- 方式：苏格拉底
- 产物：提示词汇编
- 工具：任意聊天模型；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★☆☆☆（2/5）
- 原文存档：[原文](raw/web/02-tutor/deepakness-raw-socratic-tutoring.md)

**做法。**起因是 Dwarkesh 问"有没有好的苏格拉底辅导提示词"，作者把回复里出现的提示词和 Ethan Mollick 团队的相关论文、提示词整理成一页笔记。

**可借鉴。**想找现成的苏格拉底提示词时，从这里顺藤摸瓜比较快。

## [Gemini Guided Learning 官方介绍](https://blog.google/products-and-platforms/products/education/guided-learning/)

- 作者：Google（官方）
- 方式：引导式学习
- 产物：图、视频、闪卡
- 工具：Gemini；是否需要 MCP：不需要
- 依赖：依赖 Gemini
- 评分：★★☆☆☆（2/5）
- 原文存档：[原文](raw/web/02-tutor/blog-products-and-platforms-products-education-guided-learning.md)

**做法。**Gemini 的引导学习模式会配图、配 YouTube 视频、出闪卡，一步步带你学。有评测认为它容易滑向被动观看。

**可借鉴。**它把"配图"放在默认流程里，这一点可以借。

## [X @gabriel1：怎么用 ChatGPT 学 ML](https://x.com/gabriel1/status/1918431395644621033)

- 作者：gabriel1（X）
- 方式：提问
- 产物：无
- 工具：任意聊天模型；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★☆☆☆（2/5）
- 原文存档：[帖子全文](raw/x/1918431395644621033.md)

**做法。**他的答案是：别问我，问 ChatGPT。把你想问真人的问题全部拿去问它，他说这件事很难真正内化。

**可借鉴。**适合破除"不好意思问蠢问题"的心理障碍，方法本身很粗。

## [Claude 学习可视化教程（Imagine with Claude）](https://claude.com/resources/tutorials/imagine-with-claude-student-guide)

- 作者：Anthropic（官方）
- 方式：可视化、测验
- 产物：交互可视化
- 工具：Claude；是否需要 MCP：不需要
- 依赖：依赖 Claude
- 评分：★★☆☆☆（2/5）
- 原文存档：[原文](raw/web/02-tutor/claude-resources-tutorials-imagine-with-claude-student-guide.md)

**做法。**官方给学生的教程：想要可交互的东西就直接说 "make it interactive"，想被考就说 "quiz me"。

**可借鉴。**两句口令可以当默认触发词。

## [shauigewhite/learning-tutor](https://github.com/shauigewhite/learning-tutor)

- 作者：shauigewhite（GitHub）
- 方式：前测、后测、多种教法
- 产物：学习者画像
- 工具：Claude Code；是否需要 MCP：不需要
- 依赖：依赖 Claude Code
- 评分：★★☆☆☆（2/5）
- 原文存档：[原文](raw/web/02-tutor/github-shauigewhite-learning-tutor.md)

**做法。**五种模式，学之前有前测，学完有后测，提供三种不同教法，记录学习者画像。几乎没有星。

**可借鉴。**"前测加后测"可以量化一节课到底有没有效果。

## [Mohamed-El-Sharqawy/agent-tutor](https://github.com/Mohamed-El-Sharqawy/agent-tutor)

- 作者：Mohamed-El-Sharqawy（GitHub）
- 方式：辅导、测验、间隔复习
- 产物：Obsidian 复习队列
- 工具：Claude Code、Obsidian；是否需要 MCP：不需要
- 依赖：依赖 Obsidian
- 评分：★★☆☆☆（2/5）
- 原文存档：[原文](raw/web/02-tutor/github-mohamed-el-sharqawy-agent-tutor.md)

**做法。**辅导加测验，复习按 1 到 90 天的阶梯排，结果写进 Obsidian。星数很少。

**可借鉴。**固定阶梯（1、3、7、14、30、90 天）比 FSRS 简单，适合手动维护。

## [sbkriz/feynman-tutor](https://github.com/sbkriz/feynman-tutor)

- 作者：sbkriz（GitHub）
- 方式：费曼讲解
- 产物：学习者笔记
- 工具：Claude Code；是否需要 MCP：不需要
- 依赖：依赖 Claude Code
- 评分：★★☆☆☆（2/5）
- 原文存档：[原文](raw/web/02-tutor/github-sbkriz-feynman-tutor.md)

**做法。**角色反过来：你来讲，AI 追问你讲漏的地方，并把缺口记进学习者笔记。没有星。

**可借鉴。**"你讲、它追问"是费曼讲解最直接的实现。

## [Show HN: thinkqurio，给女儿写作业用的苏格拉底工具](https://news.ycombinator.com/item?id=47036610)

- 作者：thinkqurio 作者（HN）
- 方式：苏格拉底
- 产物：网页产品
- 工具：自研产品；是否需要 MCP：不需要
- 依赖：依赖该产品
- 评分：★★☆☆☆（2/5）
- 原文存档：[原文](raw/web/02-tutor/news-item-id-47036610.md)

**做法。**作者的女儿用普通聊天机器人写作业时只会要答案，于是做了一个只引导、不直接给答案的工具。评论区讨论了孩子会不会绕过护栏。

**可借鉴。**面对孩子或自律差的学习者，护栏要做在产品里，而不是靠提示词。

## [X @jonedmiston：看到 GPT-6 交互 UI 后想扔掉自己的 /teach-me](https://x.com/jonedmiston/status/2107925510571597876)

- 作者：jonedmiston（X）
- 方式：观点
- 产物：无
- 工具：无；是否需要 MCP：不需要
- 依赖：通用
- 评分：★☆☆☆☆（1/5）
- 原文存档：[帖子全文](raw/x/2107925510571597876.md)

**做法。**一句话的回应帖，说看到 OpenAI 的交互式 UI 后，自己做的 Claude /teach-me skill 可以扔了。没有展开。

**可借鉴。**反映出"交互讲解"正在被平台吸收，自己做 skill 的价值要放在记录、复习和放行上。

## [voidstackloop/expert-mentor](https://github.com/voidstackloop/expert-mentor)

- 作者：voidstackloop（GitHub）
- 方式：跨会话导师
- 产物：学习记忆
- 工具：Claude Code；是否需要 MCP：不需要
- 依赖：依赖 Claude Code
- 评分：★☆☆☆☆（1/5）
- 原文存档：[原文](raw/web/02-tutor/github-voidstackloop-expert-mentor.md)

**做法。**自称能按水平动态调整讲解深度、跨会话记住你会了什么。被 X 推广帖包装成"装上就成专家"，核实时只有 1 星，说明也很薄。

**可借鉴。**思路普通，主要作为"推广帖夸大"的例子保留。

## [3LivesLeft/sensei](https://github.com/3LivesLeft/sensei)

- 作者：3LivesLeft（GitHub）
- 方式：辅导
- 产物：无
- 工具：Claude Code；是否需要 MCP：不需要
- 依赖：依赖 Claude Code
- 评分：★☆☆☆☆（1/5）
- 原文存档：[原文](raw/web/02-tutor/github-3livesleft-sensei.md)

**做法。**同样出现在 X 推广帖里的学习 skill，核实时 0 星，内容很少。

**可借鉴。**仅作记录。

## [BlueBirdBack/english-coach：英语教练 skill（中文）](https://github.com/BlueBirdBack/english-coach)

- 作者：BlueBirdBack（GitHub）
- 方式：语言陪练
- 产物：无
- 工具：Hermes；是否需要 MCP：不需要
- 依赖：依赖 Hermes
- 评分：★☆☆☆☆（1/5）
- 原文存档：[原文](raw/web/02-tutor/github-bluebirdback-english-coach.md)

**做法。**一个运行在 Hermes 上的英语学习 skill。星数少。

**可借鉴。**语言陪练类参考。

## [zjlylcking/pangshu-ai-beginner-coach：胖叔 AI 入门老师（中文）](https://github.com/zjlylcking/pangshu-ai-beginner-coach)

- 作者：zjlylcking（GitHub）
- 方式：新手入门辅导
- 产物：无
- 工具：任意 agent；是否需要 MCP：不需要
- 依赖：通用
- 评分：★☆☆☆☆（1/5）
- 原文存档：[原文](raw/web/02-tutor/github-zjlylcking-pangshu-ai-beginner-coach.md)

**做法。**面向中文新手的学习 skill，从 AI 基础、提示词与需求表达，讲到 PPT 改进、截图排错和 vibe coding。星数少。

**可借鉴。**零基础入门的话题顺序可参考。

## [wilsondd-lab/nachuan-stu：初高中学习 skill 合集（中文）](https://github.com/wilsondd-lab/nachuan-stu)

- 作者：wilsondd-lab（GitHub）
- 方式：中学辅导
- 产物：无
- 工具：任意 agent；是否需要 MCP：不需要
- 依赖：通用
- 评分：★☆☆☆☆（1/5）
- 原文存档：[原文](raw/web/02-tutor/github-wilsondd-lab-nachuan-stu.md)

**做法。**给初中和高中生用的学习 skill 合集。星数少。

**可借鉴。**中学场景参考。

## [markbeachill/tutorprompts](https://github.com/markbeachill/tutorprompts)

- 作者：markbeachill（GitHub）
- 方式：导师提示词
- 产物：提示词
- 工具：任意 LLM；是否需要 MCP：不需要
- 依赖：通用
- 评分：★☆☆☆☆（1/5）
- 原文存档：[原文](raw/web/02-tutor/github-markbeachill-tutorprompts.md)

**做法。**给学生和老师用的 AI 导师提示词集合。星数少。

**可借鉴。**找提示词时的又一来源。
