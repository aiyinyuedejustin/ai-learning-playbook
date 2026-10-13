# 2. 整体框架：五个环节与人机分工

## 五个环节

把各种做法放在一起看，一套能坚持下去的「用 AI 学新领域」流程，大致都由五个环节组成：

![五个环节总览](../figures/overview.png)

| 环节 | 回答什么问题 | 典型产物 | 常用工具 |
| --- | --- | --- | --- |
| 1. 对齐 | 为什么学，学完能做到什么 | `MISSION.md`：目标、成功标准、每周投入时间 | Matt 的 `grill-me` 追问；或手写 |
| 2. 拆章 | 这么大的范围先学什么、后学什么 | 大纲：模块、先后依赖、每章的验收标准 | anything-to-course；手写大纲 |
| 3. 短课 | 这一次学什么 | 25–50 分钟能学完的一节课 | Matt 的 `teach`；代码类内容用 pstack 讲解 |
| 4. 检索 | 真的会了吗 | 当天小测、第二天闭卷讲回 | Tutor 类的测验；费曼式讲回 |
| 5. 间隔复习 | 下个月还记得吗 | 卡片和复习日程 | Anki 加 FSRS，或其他间隔复习工具 |

前两个环节只在开始和每章结束时做，后三个环节每天循环。贯穿始终的是一份**学习记录**：上次学到哪、哪里卡住、下次该复习什么。有了它，每次打开 AI 不用从头解释背景。

这五个环节背后，是把「懂」拆成三道关：**当天着陆（小测）→ 过夜巩固（讲回）→ 长期调度（间隔复习）加真实迁移**。任何一关被「一天读完」跳过，都会在拿掉 AI 或几周之后暴露出来。Bastani 的实验、一口气看完的研究和间隔效应的研究，指向的都是同一个方向。

## 人和 AI 怎么分工

社区里的说法几乎一致：**AI 当教练（出题、给提示、找盲点），人当运动员（先做、先回忆、再问）。** 真正拉开差距的不是用哪个模型，而是有没有间隔复习和一个属于自己的材料库。

![人和 AI 的分工](../figures/02-roles.png)

| | 该做什么 | 不该做什么 |
| --- | --- | --- |
| AI | 解释难点、一次一题地测验、起草卡片、排复习日历、给你的答案打分 | 替你写完作业、先给完整答案、替你读完全文再总结给你背 |
| 人 | 先尝试、先默写、自己写笔记、审卡片、关掉对话再回忆 | 把「读懂了 AI 的解释」当成「我会了」 |

按环节展开：

| 环节 | AI 负责 | 人负责 |
| --- | --- | --- |
| 对齐 | 一轮轮追问，逼出模糊的地方 | 拍板目标和取舍 |
| 拆章 | 按材料起草大纲、标出前置知识 | 选定一两份权威材料，确认大纲 |
| 短课 | 讲解难点、换个角度、举例子 | 先自己读、先自己试 |
| 检索 | 出题、判分、指出缺口 | 先闭卷回答，再看反馈 |
| 复习 | 起草卡片、排日程 | 删改卡片，每天清掉到期的复习 |

这一分工在很多文章里反复出现，比如 Timtis 对比 ChatGPT、Claude、Gemini 三家学习模式的实测（<https://www.timtis.com/blog/how-to-use-ai-to-study-without-skipping-the-actual-learning/>）、Dafi 讲怎么用自己的课件约束 AI（<https://www.dafi-ai.com/en/blog/how-to-use-chatgpt-and-claude-to-study>）、GeniusPal 总结的七种用 Claude 学习的方法（<https://www.geniuspal.app/blog/ai-study/how-to-use-claude-to-study>），以及 Reddit 上 r/Anki、r/ChatGPT、r/studytips 里大量类似的回复。

## 四条硬规则

**1. 先检索，再解释。** 几乎所有高赞做法都要求：

1. 关掉 AI，先写下记得的内容（约 10 分钟）；
2. 对照笔记，只让 AI 补缺口；
3. 一次只测一题；
4. 会话结束时关掉对话，再默写一次。

这对应的就是 Roediger 与 Karpicke 的检索练习，以及 Dunlosky 综述里的两种高效用方法：练习测验和分散练习。

**2. AI 只给提示，不先给完整答案。** 这是 Bastani 实验里 Tutor 组没有吃亏的关键。

**3. 用自己的材料，不靠模型的记忆。** 上传课件、笔记、PDF，明确要求「只根据这些材料回答，材料里没有就说不知道」。linux.do 上推荐 Matt 的 `/teach`，理由之一就是它把模型的参数记忆当作不可信，先找高可信的资料写进 `RESOURCES.md` 再开始教（征集帖：<https://linux.do/t/topic/2761043>）。

**4. 对话里重问一遍不算复习。** Hacker News 上有人分享「我让 ChatGPT 像 Anki 一样考我」，回复一针见血：它可以像 Anki 一样提问，但它不是间隔复习系统（<https://news.ycombinator.com/item?id=44021924>）。正确的拆法是：AI 负责起草卡片、解释、换个问法、苏格拉底式对话；Anki 或其他 FSRS 工具负责排日程，对抗遗忘曲线。

## 同叫 teach，其实是三种东西

在 agent skill 的生态里，「teach」「tutor」「learn」这些名字被反复使用，但它们的目标、过程和产物差别很大，混用容易失望。至少有三套：

![三种 teach 的对比](../figures/02-teach-family.png)

| 维度 | Matt Pocock 的 `/teach` | pstack 的 `/teach` | Tutor 类 `/learn`（如 claude-tutor、agent-tutor-skill） |
| --- | --- | --- | --- |
| 目标 | 跨多次会话学会一门主题（语言、框架、瑜伽都行） | 真正听懂仓库里一段代码或一个子系统 | 形成可测、可复习的掌握程度，对抗遗忘曲线 |
| 过程 | 钉住目标 → 搜高可信资料 → 按「稍难但能做到」出短课 → 交互练习 | 用 `/how` 和 `/why` 挖证据 → 白话讲解，可以配图 | 计划 → 讲解 → 测验 → 用 SM-2 或 FSRS 排复习 |
| 状态 | 有状态：当前目录就是课程仓库 | 没有课程仓库，会话内讲解 | 有状态：学习者档案、`~/.learn/` 目录或网页面板 |
| 典型产物 | `MISSION.md`、`RESOURCES.md`、`lessons/*.html`、`learning-records/`、`reference/` | 口语化的讲解，加 mermaid 图或白板图 | 学习计划、测验、复习日历、进度档案 |
| 资料来源 | 强制外部搜索，不信参数记忆 | 代码加 git 记录、issue、文档等证据 | 可以联网查，也可以指定 PDF、网址或代码 |
| 测验 | HTML 课里可以嵌测验组件，强调存储强度 | 刻意不出测验，以理解为先 | 核心是自适应测验加间隔复习 |
| 什么时候用 | 「我要系统学 X 几周」 | 「这段调度代码怎么跑」 | 「学完还要记得住」 |
| 入口 | [mattpocock/skills](https://github.com/mattpocock/skills) · [teach 的 SKILL.md](https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/teach/SKILL.md) | [backnotprop/pstack](https://github.com/backnotprop/pstack) · [teach 页面](https://www.skills.sh/backnotprop/pstack/teach)；也可以在 Cursor 插件市场安装 | [kirilxd/claude-tutor](https://github.com/kirilxd/claude-tutor) 等，见第 4 章 |

一句话：**Matt 的是课程工地，pstack 的是讲代码的费曼，Tutor 类是记忆闭环。** 名字撞车，流水线却是正交的：可以串起来，不要互相替代。

### 同名不同物速查

除了这三套，还有几种做法也经常被叫作「教」或「学」：

| 名字 | 过程重心 | 主要产物 | 主要目标 |
| --- | --- | --- | --- |
| Matt 的 `/teach` | 多会话课程仓库，按最近发展区出课，管理资料 | HTML 课和 `MISSION.md` | 长期学会一门 |
| pstack 的 `/teach` | 单次把代码讲清楚 | 讲解 | 理解这段系统 |
| 费曼学习法加 AI | 隔天讲回，按评分标准判分 | 通过或不通过的结论 | 测机制是否过夜还在 |
| Knowledge Absorber | 读材料 → 核对事实 → 生成结构化笔记 | Markdown 和 HTML 笔记 | 把材料变成可教的笔记 |
| Learn Anything Quickly | 背景档案，每节课先回忆 | 背景档案和回忆队列 | 个人的检索式学习系统 |
| `/learn` gist | 固定六个阶段的进度机 | `progress.md` | 用习惯强制间隔 |

除此之外，还有几类常见工具，第 4 章会逐一展开：

- **知识吸收**：把长文、论文变成结构化笔记并配追问，如 Knowledge Absorber。
- **制卡**：把材料变成 Anki 卡片，如 anki-skill、learn-skill。
- **对齐与对抗**：开学前追问到范围清楚，学完找盲点，如 Matt 的 `grill-me`、pstack 的 `interrogate`。
- **给 agent 自己记**：如 SRSA，让 agent 自己做间隔复习，而不是给人背。

## 一天、一周、一个月的节奏

框架落到日程上，大致是这样：

```text
开始之前（对齐）
    用 grill-me 或一次访谈，写下 MISSION、成功标准、每周时间上限
    用 AI 深度研究起草学习地图 → 人钉住一两份权威材料写进 RESOURCES

第一周（画地图）
    80/20 地图：哪 20% 的内容决定 80% 的能力
    第一章必须「稍难但能做到」

每天（25–50 分钟，不是 8 小时）
    ① 间隔复习：Anki 到期的卡，加上次讲回没通过的点（10–15 分钟）
    ② 新课：一章或一节，不超过会话的 40–60%
    ③ 闭卷检索：自己默写，或单题测验
    ④ 只对缺口让 AI 解释（先给提示）
    ⑤ 记下薄弱点，约好「明天讲回」

第二天
    讲回 → 通过才做卡进 Anki；不通过 → 换角度再教 → 再隔一夜

每周
    交错混测；做一个最小的真实项目、真题，或去社区提一个问题
    更新背景档案、MISSION、学习记录；砍掉不再服务目标的支线

每月
    一次不用 AI 的远迁移测验；按「还要用多久」调整复习间隔
```

细节在下一章。
