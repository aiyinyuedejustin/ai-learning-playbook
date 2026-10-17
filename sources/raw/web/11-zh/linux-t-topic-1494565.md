# linux.do：用 skill 快速获取知识

- 链接：https://linux.do/t/topic/1494565
- 获取方式：linux.do 帖子与回复（r.jina.ai 阅读模式）

---

Title: 利用AI Skills来快速获取知识！！！（修改调整内容） - 搞七捻三 - LINUX DO

URL Source: https://linux.do/t/topic/1494565

Published Time: 2026-01-21T07:14:27+00:00

Markdown Content:
## post by Y_yuHou on Jan 21

2026-01-21更新公告

> **添加因为某些网站有反爬机制无法访问的情况，优化了输出的内容**

2026-01-21晚九点更新公告

> **修改了整体架构，添加内容**

2026-01-22早上更新公告

> **增加了读取txt,doc功能**

2026-01-23更新公告

> **修复了知乎反爬无法访问机制，增加认知校准**

[![Image 1: image](https://cdn3.ldstatic.com/original/4X/e/c/9/ec9d80dd08bd07199df000a5f21edf3c32043bc8.png)](https://cdn3.ldstatic.com/original/4X/e/c/9/ec9d80dd08bd07199df000a5f21edf3c32043bc8.png "image")

  

[![Image 2: image](https://cdn3.ldstatic.com/optimized/4X/3/8/a/38a3d18f83db60d4aed15c9bc4cb2f0da067e24c_2_660x500.png)](https://cdn3.ldstatic.com/original/4X/3/8/a/38a3d18f83db60d4aed15c9bc4cb2f0da067e24c.png "image")

  

[![Image 3: image](https://cdn3.ldstatic.com/original/4X/1/e/3/1e3645b2cfc28075afa525f15b64c46366fb3b4d.png)](https://cdn3.ldstatic.com/original/4X/1/e/3/1e3645b2cfc28075afa525f15b64c46366fb3b4d.png "image")

2026-01-25更新公告

> **更新增加解析进度条，更新多链接解析，多链接读取内容**

2026-01-25晚上更新公告

> **更新本地搜索，更新口诀，更新流程图，更新深度裂变**

[![Image 4: image](https://cdn3.ldstatic.com/optimized/4X/e/e/0/ee0a64e1147993438182662d452b484ce5aa2137_2_690x164.png)](https://cdn3.ldstatic.com/original/4X/e/e/0/ee0a64e1147993438182662d452b484ce5aa2137.png "image")

  

[![Image 5: image](https://cdn3.ldstatic.com/optimized/4X/e/f/1/ef1470272ca240345f48182d50402efdc570912b_2_481x500.png)](https://cdn3.ldstatic.com/original/4X/e/f/1/ef1470272ca240345f48182d50402efdc570912b.png "image")

[YuJunZhiXue/StudyAnalysis-Skills： 深度解析链接、文档或代码，生成“全能导师级”的教学笔记](https://github.com/YuJunZhiXue/StudyAnalysis-Skills)

github访问不了的各位可以查看gitee

[yangyuhou/StudyAnalysis-Skills](https://gitee.com/ymoran/StudyAnalysis-Skills)

**本人目前正在修改，由于有的网站有反爬机制，比如知乎，正在尝试修改SKills**

如果可以的各位尽可能star一下

> **![Image 6: :light_bulb:](https://linux.do/images/emoji/twemoji/light_bulb.png?v=15) 注意**
> 
> 
> 如果不生成文件，请将SKills中的data文件删除，这是最重要的，让他重新自己创建即可！！！
> 
> 
> 下面部分是在Skill中的调用方式

 此部分是用来看何时启动skill的
> **何时调用 (When to use)**
> 
> 
> 当出现以下任一场景时，请立即激活本技能：
> 
> 
> 1.   **显式学习指令**：
> 
> 
> *   用户明确要求：“学习这个”、“深度分析”、“深度学习”、“解析”、“解释这个概念”、“存入知识库”。
> 
> *   用户要求：“把这个讲清楚”、“教我怎么用”、“总结并生成笔记”。
> 
> *   关键词触发：只要用户提到“学习”或“分析”配合某个对象，必须激活。
> 
> 
> 
> 1.   **复杂多模态输入**：
> 
> 
> *   用户提供了一个或多个 URL 链接（尤其是包含大量信息或图片的链接）。
> 
> *   用户上传了文档文件（PDF, Word, Markdown, TXT）。
> 
> *   用户上传了图片（PNG, JPG），且图片内容包含大量文字或图表（如架构图、思维导图）。
> 
> *   混合输入：同时包含链接、文字描述和图片。
> 
> 
> 
> 1.   **代码深度解析**：
> 
> 
> *   用户选中或上传了代码文件，并询问：“这段代码是怎么跑的？”、“架构是怎样的？”。
> 
> 
> 1.   **隐式教学需求**：
> 
> 
> *   用户表示困惑：“我不理解这个概念”、“太难了，看不懂”。
> 
> *   用户需要降维打击：“用大白话解释一下”、“给个小白能懂的例子”。

实话说，我也经常被那些长得离谱的技术文档搞得头大。再加上现在的技术更新太快，资料一个接一个，代码库看的两眼迷茫。

尤其是每次想静下心学点东西的时候，没过半小时就放弃了，这种感觉真的很让人沮丧。

> 在记忆心理学里，这被称为**“认知负荷”**。我们的大脑在同一时间能处理的信息量是非常有限的。如果资料里充斥着大量冗余信息、凌乱的逻辑，大脑会消耗掉绝大部分能量来理清这些噪音，导致你根本没力气去真正“学习”。

* * *

[![Image 7](https://cdn3.ldstatic.com/optimized/4X/9/e/2/9e20b8474dc1318c18d6db457d0bb85d53df4b7e_2_500x500.jpeg)](https://cdn3.ldstatic.com/original/4X/9/e/2/9e20b8474dc1318c18d6db457d0bb85d53df4b7e.jpeg)

所以我开始尝试把这些“费劲”的环节交给 **Skills** 来处理。

比如当我面对一个几万字的 GitHub 项目文档时，我不会直接去读，而是先运行我编写的`knowledge-absorber`Skills 。这个Skills帮我完成了最痛苦的部分：

*   自动过滤掉啰嗦的客套话和重复的背景说明。

*   只抓住最核心的架构逻辑和关键 API。

*   把深奥的术语换成小白都能听懂的直白话语。

功能基本上就是给链接，给图片，给文档，给PDF给你读取，如果是长文本会自己截断，然后会生成Html和md两个格式文件，比如说你不爱看md，可以直接把html拖入到浏览器观看 比如这篇文章很多字，看不懂说的什么

[![Image 8](https://cdn3.ldstatic.com/optimized/4X/0/e/e/0ee4678fcf180791dbc316f300a207e8af4123ee_2_690x461.png)](https://cdn3.ldstatic.com/original/4X/0/e/e/0ee4678fcf180791dbc316f300a207e8af4123ee.png)

那么使用SKills来完成 效果图如下：

[![Image 9](https://cdn3.ldstatic.com/optimized/4X/b/d/b/bdbb4c3fdd931d10532db699768e5967ee24103d_2_531x500.png)](https://cdn3.ldstatic.com/original/4X/b/d/b/bdbb4c3fdd931d10532db699768e5967ee24103d.png)

* * *

说到底，现在的知识获取已经不是拼体力，而是拼谁更会利用工具来“武装自己”。

把那些繁琐、消耗能量的活儿交给AI，交给Skills，把最宝贵的注意力留给真正的思考。这才是这个时代最不焦虑的学习方式。

祝愿大家能够有完美的知识获取体验！！！

386 likes

read  12 min

## post by handsome on Jan 21

## post by boris20190 on Jan 21

## post by bkjyyy on Jan 21

## post by Papain233 on Jan 21

## post by Y_yuHou on Jan 21

## post by shuawag on Jan 21

## post by Liquor on Jan 21

## post by shiuing on Jan 21

## post by zone on Jan 21

## post by yi_zero on Jan 21

## post by Y_yuHou on Jan 21

## post by Y_yuHou on Jan 21

## post by zhecai on Jan 21

## post by mymartini on Jan 21

## post by zzjbattlefield on Jan 21

## post by noyyy on Jan 21

## post by zhaohs on Jan 21

## post by unique123 on Jan 21

## post by Y_yuHou on Jan 21

## Load more posts below

