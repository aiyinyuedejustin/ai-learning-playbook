# linux.do：SRSA 发布帖

- 链接：https://linux.do/t/topic/1803656
- 获取方式：linux.do 帖子与回复（r.jina.ai 阅读模式）

---

Title: 【开源】我做了一个让 AI Agent 像人一样复习记忆的系统（SRSA） - Develop - LINUX DO

URL Source: https://linux.do/t/topic/1803656

Published Time: 2026-03-23T13:21:40+00:00

Markdown Content:
## post by cheanus on Mar 23

#### [](https://linux.do/t/topic/1803656#p-15525026-h-1)本帖使用社区开源推广，符合推广要求。我申明并遵循社区要求的以下内容：

*   **我的帖子已经打上 [开源推广](https://linux.do/tag/2234-tag/2234) 标签：** 是
*   **我的开源项目完整开源，无未开源部分：** 是
*   **我的开源项目已链接认可 LINUX DO 社区：** 是
*   **我帖子内的项目介绍，AI生成、润色内容部分已截图发出：** 是
*   **以上选择我承诺是永久有效的，接受社区和佬友监督：** 是

_以下为项目介绍正文内容，AI生成、润色内容已使用截图方式发出_

* * *

## [](https://linux.do/t/topic/1803656#p-15525026-h-2)背景

最近几周我看了很多大佬为AI设计的记忆系统，许多地方的思路十分新颖，不得不令人佩服。

然而，我想我们始终需要承认一件事，那就是环境是复杂的，记忆系统终会面临“遗忘”的问题，而这种问题的根源是复杂的，甚至不同记忆系统的问题源头各不相同。

如果从控制论的角度看，我们一直在尝试设计一个尽善尽美的开环系统，以应对环境中的种种噪声，但是否有这样一种可能：设计闭环反馈系统是一个更好的选择？

当前记忆反馈系统已经有了许多初步的雏形：

*   人在回路反馈：这是最简单的反馈，当AI第二次面对相同情景，却因记忆遗忘错误地执行了动作时，用户会干涉、指导AI，对AI形成记忆强化
*   定期记忆整理：典型案例是clawhub排名第一的技能self-improving-agent，这种反馈环路会在触发时让AI自动整理出错误、过时的记忆，并进行修复或强化

然而，第一种方法要求用户参与，很难做到定时重复的进行；第二种方法虽然能重复运行，但随着记忆系统越来越大，其效率也不可避免地下降。

有没有一种能够让AI定期高效复习、巩固记忆的反馈系统呢？我认为人类自己早已发明了这种技术——间隔重复。

如果你使用过Anki、背单词软件的话，你应该能明白本文接下来的内容了。如果说人类对抗遗忘的最佳方式是使用间隔重复算法，那么AI何尝不可呢？

## [](https://linux.do/t/topic/1803656#p-15525026-srsa-3)SRSA

Spaced Repetition Systems for Agents (SRSA) 是我这几天做的一个开源项目，它的核心理念十分简单——让AI用间隔重复算法（如FSRS）巩固记忆。

用户（或AI）可以生成一些问答卡片，让AI定期进行复习。复习时，AI会不断读取问题、看答案、自评、反思并更新记忆，越容易的卡片会越少复习，越困难的卡片会越多复习，从而实现定期高效的巩固记忆、克服遗忘。

该项目提供skill，方便agent接入，并且可以与任何记忆系统共存，以期提升原有记忆系统的效果。

从技术上讲，SRSA实现了一种离线强化学习，其更新的对象是记忆系统而非模型权重，并应用FSRS算法来减少复习次数和token用量。

[![Image 1: 图片](https://cdn3.ldstatic.com/optimized/4X/6/2/b/62bb89ff9dc6ab19f4bbc85d2347143201ce5c2b_2_551x500.png)](https://cdn3.ldstatic.com/original/4X/6/2/b/62bb89ff9dc6ab19f4bbc85d2347143201ce5c2b.png "图片")

项目主页：[SRSA](https://github.com/cheanus/SRSA)

萌新第一次开源项目，欢迎各位佬友提出意见反馈哈！如果觉得有帮助的话还望给个star~![Image 2: :star:](https://cdn.ldstatic.com/images/emoji/twemoji/star.png?v=15)

45 likes

[![Image 3: 浣熊](https://cdn.ldstatic.com/user_avatar/linux.do/hanuxxx/48/430624_2.png)](https://linux.do/u/hanuxxx "hanuxxx")

## post by systole_famous on Mar 23

没看懂，为啥 AI 需要复习？

重点是记忆有没有在上下文中吧。

## post by jingtai123 on Mar 23

## post by cheanus on Mar 23

## post by morusa on Mar 23

## post by cheanus on Mar 23

## post by shufu.yes on Mar 23

## post by light04 on Mar 23

## post by I-IronMan on Mar 23

## post by cheanus on Mar 23

## post by handsome on Mar 23

## post by cheanus on Mar 23

## post by cheanus on Mar 23

## post by cheanus on Mar 23

## post by light04 on Mar 23

## post by softs on Mar 23

## post by ELDment on Mar 23

## post by cheanus on Mar 23

## post by ELDment on Mar 23

## post by Ericoolen on Mar 23

## Load more posts below

