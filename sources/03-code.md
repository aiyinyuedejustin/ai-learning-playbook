# 编程边做边学

编程是"必须亲手做"的技能，也是 AI 最容易代劳的领域。这一类既有对照实验（AI 帮你写代码会让你少学到什么），也有让 agent 讲代码、留空让你写、把仓库变成课程的工具。共同的结论是：只问概念、要代码就要讲解、bug 先自己修。

本类共 23 条，按评分从高到低排列。

## [Anthropic：AI 辅助如何影响编程技能的形成（RCT）](https://www.anthropic.com/research/AI-assistance-coding-skills)

- 作者：Anthropic（研究）
- 方式：对照实验
- 产物：论文
- 工具：无；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★★★（5/5）
- 原文存档：[原文](raw/web/03-code/anthropic-research-ai-assistance-coding-skills.md)

**做法。**52 名工程师学一个新的 Python 库（Trio），一组用 AI 一组不用，之后不用 AI 做测验。AI 组平均 50%，对照组 67%，差距主要出在 debug。研究把 AI 组的用法分成六种：全委托、渐进依赖、反复让 AI 修 bug 的三种得分低；只问概念、生成后追问为什么、要代码时附带讲解的三种得分接近对照组。论文是 arXiv 2601.20245。

**可借鉴。**六种用法的划分可以直接写成编程学习时的规则：只问概念，要代码就要讲解，bug 自己先修。

## [Simon Willison：Interactive explanations](https://simonwillison.net/guides/agentic-engineering-patterns/interactive-explanations/)

- 作者：Simon Willison（博客）
- 方式：线性讲解、动画讲解
- 产物：交互 HTML 动画
- 工具：任意编码 agent；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★★★（5/5）
- 原文存档：[原文](raw/web/03-code/simonwillison-guides-agentic-engineering-patterns-interactive-explanat.md)

**做法。**读代码时先让 agent 写一份线性讲解，还不懂就让它做一个动画演示。他用这个办法看懂了词云的阿基米德螺旋布局。文章属于他的"agentic engineering patterns"系列。

**可借鉴。**"文字讲不懂就要一个动画"是低成本、高收益的升级步骤。

## [zarazhangrui/codebase-to-course](https://github.com/zarazhangrui/codebase-to-course)

- 作者：Zara Zhang（GitHub）
- 方式：代码库变课程、应用型测验
- 产物：单文件 HTML 课程
- 工具：Claude Code skill；是否需要 MCP：不需要
- 依赖：依赖 Claude Code，可移植
- 评分：★★★★★（5/5）
- 原文存档：[原文](raw/web/03-code/github-zarazhangrui-codebase-to-course.md)

**做法。**把一个仓库变成单文件 HTML 课程，左边是代码、右边是白话讲解，带动画和"应用型测验"（不是问定义，而是问遇到某个情况该改哪里）。约 5.7k 星。

**可借鉴。**"应用型测验"的出题方式值得借：问"要改 X 该动哪个文件"比问"X 是什么"更能检验理解。

## [论文：How AI Impacts Skill Formation（arXiv 2601.20245）](https://arxiv.org/abs/2601.20245)

- 作者：Shen、Tamkin（Anthropic）（arXiv）
- 方式：对照实验
- 产物：论文
- 工具：无；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★★☆（4/5）
- 原文存档：[原文](raw/web/03-code/arxiv-abs-2601-20245.md)

**做法。**上一条研究的论文版本，给出了实验设计、六种交互模式的定义和各组分数。AI 组遇到的错误少了约三倍，作者认为"错误正是技能形成的地方"。

**可借鉴。**"少遇到错误就少学到东西"是编程学习里最该记住的一句话。

## [backnotprop/pstack：/how、/why、/teach、/bro](https://github.com/backnotprop/pstack)

- 作者：backnotprop（GitHub）
- 方式：读代码、分层讲解
- 产物：讲解文本、架构图
- 工具：Claude Code、Cursor 插件；是否需要 MCP：不需要
- 依赖：依赖 Claude Code / Cursor
- 评分：★★★★☆（4/5）
- 原文存档：[原文](raw/web/03-code/github-backnotprop-pstack.md)

**做法。**一组读代码用的 skill：`/how` 讲架构怎么跑，`/why` 去 git、issue、文档里找证据解释为什么这样设计，`/teach` 把两者合成讲解，`/bro` 用大白话再讲一遍。另有 `interrogate`（对抗评审找盲点）、`arena`（多方案比较）。它没有课程仓库，是一次性讲清。约 1.6k 星。

**可借鉴。**和 Matt 的 /teach 同名但用途正交：一个是"讲清这段代码"，一个是"跨多天学一门课"。

## [Simon Willison：Linear walkthroughs](https://simonwillison.net/guides/agentic-engineering-patterns/linear-walkthroughs/)

- 作者：Simon Willison（博客）
- 方式：线性讲解
- 产物：带真实代码片段的 md 文档
- 工具：任意编码 agent、showboat 工具；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★★☆（4/5）
- 原文存档：[原文](raw/web/03-code/simonwillison-guides-agentic-engineering-patterns-linear-walkthroughs.md)

**做法。**让 agent 按执行顺序逐段讲一个代码库。他用自己的 showboat 工具把真实代码片段 exec 进文档，避免 AI 自己抄错代码。

**可借鉴。**讲解文档里的代码必须来自真实文件，而不是模型复述，这一条对所有代码讲解都适用。

## [ktaletsk/learn-codebase：反 vibe coding 的苏格拉底代码导师](https://github.com/ktaletsk/learn-codebase)

- 作者：ktaletsk（GitHub）
- 方式：苏格拉底、读代码
- 产物：无固定产物
- 工具：Claude Code 等（npx skills add -g）；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★★☆（4/5）
- 原文存档：[原文](raw/web/03-code/github-ktaletsk-learn-codebase.md)

**做法。**用苏格拉底方式带你理解一个代码库，不替你读，而是提问引导你自己去找入口、追调用链。作者明确把它定位为"反 vibe coding"。约 85 星，装好后用 `/learn-codebase` 触发。

**可借鉴。**接手陌生仓库时，用提问代替总结，能真正建立心智模型。

## [X @HowToPrompt__：Anthropic RCT 的通俗解读](https://x.com/HowToPrompt__/status/2055670039723102473)

- 作者：HowToPrompt__（X）
- 方式：解读
- 产物：无
- 工具：无；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★☆☆（3/5）
- 原文存档：[帖子全文](raw/x/2055670039723102473.md)

**做法。**把 Anthropic 实验的六种用法讲得最清楚的一条二手帖。评论区补了两句：@kekkodamato_ 说"他们外包的不是代码，是思考"；@GayGuillaume7 说"那 17% 的差距，你会在凌晨 2 点 AI 宕机时发现"。也有人质疑样本小、结论下得太宽，以及卖 AI 的公司发这种研究的立场。

**可借鉴。**适合拿来给别人解释为什么要限制 AI 帮你 debug。

## [Simon Willison：用 ChatGPT 和 Copilot 学 Rust](https://simonwillison.net/2022/Dec/5/rust-chatgpt-copilot/)

- 作者：Simon Willison（博客）
- 方式：项目驱动、边做边问
- 产物：Advent of Code 解答
- 工具：ChatGPT、Copilot；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★☆☆（3/5）
- 原文存档：[原文](raw/web/03-code/simonwillison-2022-dec-5-rust-chatgpt-copilot.md)

**做法。**他用 Advent of Code 题目学 Rust，遇到编译错误和概念问题就问 ChatGPT，Copilot 帮补语法。文章记录了 AI 解释错误信息很有用，但也会自信地给错答案。HN 上有讨论（33872369）。

**可借鉴。**"用一组有标准答案的小题目学新语言"天然自带验收。

## [DieselZhang/repo-mastery](https://github.com/DieselZhang/repo-mastery)

- 作者：DieselZhang（GitHub）
- 方式：代码库课程、掌握放行、间隔复习
- 产物：md 与 HTML 课程
- 工具：Claude Code；是否需要 MCP：不需要
- 依赖：依赖 Claude Code
- 评分：★★★☆☆（3/5）
- 原文存档：[原文](raw/web/03-code/github-dieselzhang-repo-mastery.md)

**做法。**把仓库变成从"怎么用"到"架构"再到"实现"的分层课程，每层之间有确定性的掌握关卡，过了才能进下一层，并配间隔复习。输出 md 和 HTML。星数很少。

**可借鉴。**"用法、架构、实现"三层是给代码库排课的好骨架。

## [X @suraj_sharma14：15 件不让 AI 把我变笨的事](https://x.com/suraj_sharma14/status/2105183362583515333)

- 作者：suraj_sharma14（X）
- 方式：先写方案再看 AI、错题本
- 产物："AI 错在哪"笔记
- 工具：无；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★☆☆（3/5）
- 原文存档：[帖子全文](raw/x/2105183362583515333.md)

**做法。**15 条习惯里最有用的几条：写 prompt 前先写 3 行自己的解法，再和 AI 的对比；每周手动 debug 一次；每月从零写一个东西；记一本"AI 错在哪"笔记。评论区认为只有第一条自带可对比的记录，其余都只是意愿；"错题本"被称为个人 eval 集。

**可借鉴。**"先写 3 行自己的方案"是成本最低、又能留下证据的习惯。

## [X @thrialectics：Claude Code 当数学和编程家教](https://x.com/thrialectics/status/2029601998492881381)

- 作者：thrialectics（X）
- 方式：目录化辅导、诊断、间隔复习
- 产物：每个主题一个目录
- 工具：Claude Code、CLI；是否需要 MCP：不需要
- 依赖：依赖 Claude Code
- 评分：★★★☆☆（3/5）
- 原文存档：[帖子全文](raw/x/2029601998492881381.md)

**做法。**每个主题建父目录和子目录，用 CLI 小工具做诊断，再配间隔复习，把 Claude Code 变成数学和编程语言的个性化家教。

**可借鉴。**"每个主题一个目录"让学习状态可以跨会话保存，这和 Matt 的 /teach 是同一个思路。

## [linux.do：Sonnet 4.5 和 GLM-4.7 当导师学 einsum](https://linux.do/t/topic/1363792)

- 作者：shinoun（linux.do）
- 方式：苏格拉底、代码骨架填空
- 产物：TODO 代码骨架
- 工具：Claude、GLM；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★☆☆（3/5）
- 原文存档：[原文](raw/web/03-code/linux-t-topic-1363792.md)

**做法。**作者用同一套苏格拉底导师提示，分别让 Sonnet 4.5 和 GLM-4.7 教他 einsum。导师给出带 TODO 的代码骨架让他填，再追问。他发现 GLM 的讲解出现了错误，Sonnet 更稳。

**可借鉴。**"给骨架、留 TODO"和 Claude Code 的 Learning 风格是同一个机制；模型本身的准确性也要考虑。

## [linux.do：AI 写完我手动 debug 再手写一遍](https://linux.do/t/topic/1359955)

- 作者：Eddy1（linux.do）
- 方式：先读 AI 代码、手动 debug、手写重做
- 产物：手写代码
- 工具：任意编码 agent、IDE；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★☆☆（3/5）
- 原文存档：[原文](raw/web/03-code/linux-t-topic-1359955.md)

**做法。**作者学 Java 后端的做法是：让 AI 写完一个功能，自己在 IDEA 里一步步 debug 看懂，再关掉 AI 手写一遍。回复里有人认同，也有人觉得效率太低。

**可借鉴。**和 Anthropic 实验的结论一致：亲手碰过错误才学得会 debug。

## [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x)

- 作者：codecrafters（GitHub）
- 方式：从零重写
- 产物：代码项目
- 工具：无；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★☆☆（3/5）
- 原文存档：[原文](raw/web/03-code/github-codecrafters-io-build-your-own-x.md)

**做法。**按"自己写一个 Git、数据库、解释器……"整理的教程合集，星数极高。和 AI 结合的方式是：选一个项目当学习主线，AI 只在卡住时提示。

**可借鉴。**项目型学习的现成题库。

## [Learning programming in an age of LLMs（HN 讨论）](https://news.ycombinator.com/item?id=49723873)

- 作者：Mark Seemann（ploeh）（HN）
- 方式：观点、讨论
- 产物：无
- 工具：无；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★★☆☆（3/5）
- 原文存档：[原文](raw/web/03-code/news-item-id-49723873.md)

**做法。**Mark Seemann 的文章讨论在 LLM 时代学编程还要不要从基础练起，HN 上约 260 分。讨论里两派都有：一派认为基础练习不可替代，一派认为可以从读 AI 代码开始，但要有意识地做"不用 AI"的练习。

**可借鉴。**"有意安排不用 AI 的练习"是两派都认同的折中。

## [Claude Code 官方插件 learning-output-style](https://github.com/anthropics/claude-code/tree/main/plugins/learning-output-style)

- 作者：Anthropic（GitHub）
- 方式：边做边学
- 产物：代码里的 TODO(human)
- 工具：Claude Code；是否需要 MCP：不需要
- 依赖：依赖 Claude Code
- 评分：★★★☆☆（3/5）
- 原文存档：[原文](raw/web/03-code/github-anthropics-claude-code-tree-main-plugins-learning-output-style.md)

**做法。**Learning 输出风格的插件版，用 SessionStart hook 在每次会话开始时注入学习模式的指令，效果和 /output-style Learning 相同。

**可借鉴。**想在项目级默认开启学习模式时用插件版。

## [Nitzan94/claude-code-skills：AI tutor 等](https://github.com/Nitzan94/claude-code-skills)

- 作者：Nitzan94（GitHub）
- 方式：辅导
- 产物：md
- 工具：Claude Code；是否需要 MCP：不需要
- 依赖：依赖 Claude Code
- 评分：★★☆☆☆（2/5）
- 原文存档：[原文](raw/web/03-code/github-nitzan94-claude-code-skills.md)

**做法。**一组 Claude Code skill，包括 AI tutor、sync-context、skillify（把一次对话沉淀成 skill）。星数少。

**可借鉴。**skillify 的思路（把学会的东西变成 skill）可以和学习记录结合。

## [X @Pluvio9yte：一句话让 ChatGPT 教你 vibe coding（中文）](https://x.com/Pluvio9yte/status/2000094545212747924)

- 作者：Pluvio9yte（X）
- 方式：访谈式入门
- 产物：无
- 工具：ChatGPT；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★☆☆☆（2/5）
- 原文存档：[帖子全文](raw/x/2000094545212747924.md)

**做法。**只给一句提示："你是一名经验丰富的程序员和架构师，擅长用 Claude Code、Codex、Cursor 做 vibe coding，我有计算机基础，想入门，你需要教我。我们来聊一下。"约 540 赞。

**可借鉴。**"我们来聊一下"让 AI 先问你，而不是直接倒出一篇教程。

## [X @Rustallintsla：30 天从零学软件开发（中文）](https://x.com/Rustallintsla/status/2053706425981886849)

- 作者：Rustallintsla（X）
- 方式：项目驱动
- 产物：个人项目
- 工具：任意 AI 编码工具；是否需要 MCP：不需要
- 依赖：通用
- 评分：★★☆☆☆（2/5）
- 原文存档：[帖子全文](raw/x/2053706425981886849.md)

**做法。**一个完全没有编程基础的人记录了自己用 AI 学 30 天的感受：一开始无从下口，后来一点点问、一点点做。帖子以感受为主，方法细节不多。

**可借鉴。**可以作为"零基础时摸底会全错"的真实例子。

## [Shipyard：Claude Code 输出风格与结对编程](https://shipyard.build/blog/claude-code-output-styles-pair-programming/)

- 作者：Shipyard（博客）
- 方式：边做边学、结对
- 产物：无
- 工具：Claude Code；是否需要 MCP：不需要
- 依赖：依赖 Claude Code
- 评分：★★☆☆☆（2/5）
- 原文存档：[原文](raw/web/03-code/shipyard-blog-claude-code-output-styles-pair-programming.md)

**做法。**实测几种输出风格，结论是 Learning 风格最适合结对编程式的学习：AI 讲思路、留空让你写。

**可借鉴。**确认 Learning 风格的适用场景。

## [wizardengineer/airev：AI 代码改动的终端审阅工具](https://github.com/wizardengineer/airev)

- 作者：wizardengineer（GitHub）
- 方式：审阅 AI 代码、间隔复习
- 产物：行内评论、复习卡
- 工具：终端 TUI、MCP；是否需要 MCP：需要
- 依赖：需 MCP
- 评分：★☆☆☆☆（1/5）
- 原文存档：[原文](raw/web/03-code/github-wizardengineer-airev.md)

**做法。**在终端里审阅 AI 生成的代码改动，带结构化行内评论、间隔复习和基于 MCP 的 agent 反馈。0 星。

**可借鉴。**"审 AI 代码时顺手把学到的东西做成复习卡"是有意思的组合。

## [jiangxihu071112-hue/c-learning-skill-codex：C 语言学习 skill](https://github.com/jiangxihu071112-hue/c-learning-skill-codex)

- 作者：jiangxihu071112-hue（GitHub）
- 方式：交互教程、练习
- 产物：教程与练习
- 工具：Codex；是否需要 MCP：不需要
- 依赖：依赖 Codex
- 评分：★☆☆☆☆（1/5）
- 原文存档：[原文](raw/web/03-code/github-jiangxihu071112-hue-c-learning-skill-codex.md)

**做法。**给 Codex 用的 C 语言学习 skill，含交互教程、例子和练习。0 星。

**可借鉴。**少见的 Codex 专用学习 skill。
