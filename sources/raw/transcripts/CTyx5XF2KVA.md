# 硅谷顶尖 AI 大佬如何搭建个人AI知识库？从0开始用Claude Code + Obsidian搭建Karpathy的LLM Wiki知识库

- URL: https://www.youtube.com/watch?v=CTyx5XF2KVA
- Channel: 杰森的效率工坊
- Published: 2026-04-14
- Duration: 14:23
- Transcript: 人工字幕 / manual captions, lang=zh-Hans
- Cite as: [mm:ss](timestamp link) — each line below starts with one

## Chapters

- [00:00](https://www.youtube.com/watch?v=CTyx5XF2KVA&t=0s) 为什么传统RAG不好用了？Karpathy的LLM Wiki到底是什么
- [01:16](https://www.youtube.com/watch?v=CTyx5XF2KVA&t=76s) 解析三层架构与三个核心AI操作
- [02:58](https://www.youtube.com/watch?v=CTyx5XF2KVA&t=178s) 第一步：在Obsidian里建立基础的文件结构
- [04:44](https://www.youtube.com/watch?v=CTyx5XF2KVA&t=284s) 配置 CLAUDE.md，给AI智能体立好规矩
- [05:40](https://www.youtube.com/watch?v=CTyx5XF2KVA&t=340s) 用 Obsidian Web Clipper 收集学习资料
- [06:17](https://www.youtube.com/watch?v=CTyx5XF2KVA&t=377s) Ingest (摄取)：看AI怎么全自动帮你写Wiki笔记
- [09:01](https://www.youtube.com/watch?v=CTyx5XF2KVA&t=541s) Query (查询)：怎么向AI提问并沉淀出新知识
- [10:55](https://www.youtube.com/watch?v=CTyx5XF2KVA&t=655s) Lint (巡检)：一键查出孤立笔记和死链，保持系统健康
- [12:22](https://www.youtube.com/watch?v=CTyx5XF2KVA&t=742s) 配合 Obsidian 官方 CLI 进一步省 Token 的思路
- [13:02](https://www.youtube.com/watch?v=CTyx5XF2KVA&t=782s) 使用智能体的避坑建议（Token消耗与幻觉问题）
- [13:58](https://www.youtube.com/watch?v=CTyx5XF2KVA&t=838s) 总结与配套开源资料获取

## Transcript

[00:00](https://www.youtube.com/watch?v=CTyx5XF2KVA&t=0s) 前OpenAI联合创始人 AI大神卡帕西最近提出了他的个人AI知识库理念LLM Wiki 他摒弃了传统的RAG 转向了一套极简的LLM Wiki系统那今天我们就用Claude Code和 Obsidian来实现卡帕西的这套系统我们会亲手创建三个skill 配置Claude.md文件然后让AI智能体为我们构建一整套Wiki架构我会把所有用到的skill配置文件以及整个知识库都打包上传到我的GitHub上

[00:31](https://www.youtube.com/watch?v=CTyx5XF2KVA&t=31s) 供大家下载那我们就正式开始首先卡帕西的理念到底是什么简单来说就是把要学习的资料和文章通过AI智能体比如Claude Code转换成Wiki 形式的Markdown笔记库那最好的实现就是Obsidian 然后在这个编译后的笔记库中利用AI进行持续的学习与探索把每次学习和总结的重要内容再次积累到知识库实现知识的复利同时对笔记库进行定期的维护和体检保持系统健康

[01:02](https://www.youtube.com/watch?v=CTyx5XF2KVA&t=62s) 那传统的RAG系统每次问答都是重新搜索知识库没有任何记忆和积累而LLM Wiki则是持久化的维护一个知识库这也是智能体时代个人 AI知识库的必然形式卡帕西的理念简单来说就是三层架构外加三个核心操作那三层架构首先原始资料层那这个很好理解就是我们平时收集或策划的文档集合那包括剪藏的网络文章要学习的论文文献转录的YouTube视频等等

[01:33](https://www.youtube.com/watch?v=CTyx5XF2KVA&t=93s) 那卡帕西列举的主要工具就是Obsidian Web Clipper 那这个我在之前的视频中也讲过很多次了那第二层则是Wiki层也就是AI智能体对原始资料进行深入分析后生成的Markdown文件目录包含摘要实体概念对比分析等那同时还包含索引与日志文件第三层就是schema架构规范那实际上就是智能体工具的配置文件比如你使用Claude Code 那么就是CLAUDE.md 使用OpenCode 就是AGENTS.md

[02:03](https://www.youtube.com/watch?v=CTyx5XF2KVA&t=123s) 作用是告诉智能体工具具体的工作流程和规范那整个架构的实现实际上就是智能体工具加Obsidian 那我们今天用的是Claude Code加Obsidian 在Obsidian中使用Claudian插件集成Claude Code 那这些工具我在之前的视频中已经讲过很多次了大家可以回看我之前的视频三个核心操作分别是 ingest摄取、query查询、lint巡检 ingest摄取就是让智能体把原始资料充分消化并编译成Markdown格式的Wiki笔记库

[02:34](https://www.youtube.com/watch?v=CTyx5XF2KVA&t=154s) 那query查询就是由你对AI进行提问从而对知识库进行深入的学习并把学习整理的内容积累到知识库中而lint巡检则是对知识库架构的维护包括双向链接的关联数据空白的填补孤立页面的发现等等那这三个操作我们会做成3个agent skill 那接下来我们就正式上手实现这个知识库那整个知识库的架构我已经展示在屏幕上了我们在电脑端创建一个空白的文件夹作为项目文件夹

[03:05](https://www.youtube.com/watch?v=CTyx5XF2KVA&t=185s) 然后分别创建raw Wiki和 assets这三个子文件夹 raw就是原始资料的收集层那这个其实和我们以前使用Obsidian是非常类似的我一般都取名叫inbox 那在raw文件夹里面我们创建了几个子文件夹用于分类分别存放网页剪藏的文章专业的论文文献和研报视频和播客的转录文章等等那另外我们要创建一个archive文件夹那这些资料被分析完毕后会归档到archive文件夹

[03:36](https://www.youtube.com/watch?v=CTyx5XF2KVA&t=216s) 那Wiki文件夹内要创建索引文件 index.md和日志文件log.md 然后创建几个子文件夹分别是concepts存放的是方法论 entities存放的是实体概念 sources存放的是针对原始文件一对一提炼出来的摘要 syntheses存放的是你用AI进行深度的学习与探索后保存下来的知识积累那assets就不用说了那熟悉Obsidian的同学应该都知道存放的是媒体资源也就是图片和附件之类的内容

[04:07](https://www.youtube.com/watch?v=CTyx5XF2KVA&t=247s) 那在Obsidian的设置中我们要把附件文件夹路径设置为这个assets文件夹那么到此我们就完成了文件夹结构的创建我们用Obsidian打开这个文件夹然后打开Claudian插件或者直接用Claude Code打开这个文件夹都是一样的那直接输入/init 也就是初始化命令那Claude Code就会创建一个CLAUDE.md 配置文件以及.claude文件夹那这里如果你使用的是OpenCode 那么创建的就是AGENTS.md文件的原理都是一样的

[04:38](https://www.youtube.com/watch?v=CTyx5XF2KVA&t=278s) 大家也可以回看我之前的OpenCode的视频那么到此整个文件夹结构就创建完毕了我们打开CLAUDE.md 把它自动生成的英文内容都删掉然后按照我们的需求写入一些中文的约束那CLAUDE.md 就是一个普通的Markdown文件包含了整个项目的核心规范你可以直接把你的要求列出来然后让AI帮你写那在CLAUDE.md 我们主要约束以下几个内容首先就是目录结构的权限边界告诉智能体我们创建的三个文件夹都是做什么用的

[05:09](https://www.youtube.com/watch?v=CTyx5XF2KVA&t=309s) 并且规定智能体的编辑权限其次我们要详细地告诉智能体在Wiki文件夹中生成内容的时候要遵守什么样的规范以及在写入index索引文件和log日志文件的时候要遵循什么样的格式再就是生成Markdown笔记的时候要遵循什么样的规则那么到这就基本足够了那这个CLAUDE.md文件对应的就是卡帕西里面中的Schema架构规范这一层那么我们的知识库已经搭建完毕现在我们就开始做深入的学习

[05:41](https://www.youtube.com/watch?v=CTyx5XF2KVA&t=341s) 我们在浏览器端安装 Obsidian Web Clipper这个插件然后设置插件的保存路径为我们的Obsidian知识库的raw 文件夹的articles子文件夹中然后你就可以在你浏览网页文章的时候进行剪藏了你也可以手动把你下载的学习资料放置到raw文件夹中那我们以AI提示词工程这个知识领域为例子我这里收藏了一些有关提示词工程的网页文章和论文包括Gemini的提示词策略谷歌的提示词工程白皮书

[06:12](https://www.youtube.com/watch?v=CTyx5XF2KVA&t=372s) 那还有一个经典的5C 架构的提示词框架论文在准备好学习资料之后我们就可以执行第一步知识的摄取了我们在.claude文件夹中的skills 文件夹里创建一个叫Ingest的文件夹在这里面新建一个skill.md文件然后打开这个文件我们来手动撰写一些skill内容在开头的yaml元数据部分添加name和description字段然后开始撰写skill正文这个技能主要就是告诉AI如何对raw

[06:42](https://www.youtube.com/watch?v=CTyx5XF2KVA&t=402s) 文件夹下的原始资料进行分析和编译并生成Wiki内容那主要包含的就是skill的触发逻辑执行的步骤以及约束和注意事项那大家看到这个skill可能会很头疼但实际上这个skill的编写是我使用 skill Creator这个技能来帮我完成的那skill Creator是Anthropic发布在他们官方GitHub仓库中的skill 那这个skill是专门帮你撰写skill的你只需要把你的需求告诉智能体智能体就会调用这个skill Creator来帮你创建相应的skill

[07:15](https://www.youtube.com/watch?v=CTyx5XF2KVA&t=435s) 那如果大家还是嫌麻烦那可以直接来GitHub 下载我的整个知识库里面就有写好的skill 和Claude.md配置文件那整个流程就是让智能体深入分析原始文件整理并撰写相应的Markdown文件并建立双向链接同时更新index索引文件和log日志文件那最后在所有文件处理完毕后把原始文件移动到archive文件夹中那么我们就来看一下执行效果在智能体窗口中直接输入/ingest

[07:46](https://www.youtube.com/watch?v=CTyx5XF2KVA&t=466s) 就可以触发skill流程那这里我们在Claude Code里转接的是Kimi K2.5模型那有关Claude Code的转接方法我在以前的视频中有讲那卡帕西也说过你使用Codex或者OpenCode 这些智能体都是可以的那原理都是一样的智能体处理这些文件需要一定的时间我们来对视频进行一个加速那另外我也要提醒大家大规模的文件读写是非常消耗token的大家要注意自己的token使用量那我们可以看到智能体对原始文件进行分析后撰写了对应的Markdown文件

[08:17](https://www.youtube.com/watch?v=CTyx5XF2KVA&t=497s) 然后更新了index索引文件和log日志文件那最后把原始文件归档到了archive文件夹中那智能体列出了执行完成的任务列表包括创建的文件核心知识发现以及重要标注我们点开知识图谱看到整个提示词工程相关的概念都被创建在了知识库中并建立了非常好的双向链接那点开对应的笔记就能够查看到具体的内容了那我们再来看一下索引文件那索引文件中按照分类列出了知识库中的详细索引结构

[08:49](https://www.youtube.com/watch?v=CTyx5XF2KVA&t=529s) 而log日志文件中清晰地记录了本次操作所处理的内容和创建的文件清单那这两个文件在后续都有着重要的作用那么到此第一个步骤也就是知识的摄取就完成了那接下来我们就可以针对这些知识进行深入的学习了我们可以向AI进行提问来深入地探索并学习有关提示词工程的相关内容那这里我们来创建第二个skill 也就是query 那这个skill相对比较简单主要就是要求AI在回答问题之前永远都要先读取index

[09:20](https://www.youtube.com/watch?v=CTyx5XF2KVA&t=560s) .md这个索引文件定位到问题的相关内容然后深度阅读目标文件并对问题进行回答如果生成了有价值的内容要询问用户是否把内容保存到知识库那这一点也是LLM Wiki的核心理念那让知识不断的积累不断的进化实现知识的复利那这里我也规定了智能体在把这些高质量内容保存回知识库的时候所要遵循的规范以及内容模板那么我们回到智能体的窗口向智能体提问那结合5C这个提示词框架

[09:53](https://www.youtube.com/watch?v=CTyx5XF2KVA&t=593s) 来为我设计一个提示词主要功能是用于撰写 Markdown格式的知识笔记我们可以看到智能体的回复非常的详尽不但根据5C框架生成了提示词还生成了使用案例并询问我是否把这个提示词保存回知识库啊我们这里输入确定保存回知识库然后智能体就把刚才的这篇内容保存到了Wiki文件夹下的syntheses文件夹内同时还创建了双向链接并更新了index索引和log日志文件你还可以要求智能体对知识库中

[10:24](https://www.youtube.com/watch?v=CTyx5XF2KVA&t=624s) 相关的知识点的矛盾进行挖掘或者探索特定的知识盲区结合你的实际工作来为你进行战略规划那这一步你还可以充分利用Obsidian的功能来生成各种各样的产出结果比如卡帕西就建议可以让AI 来生成marp格式的幻灯片那当然我们也可以生成Canvas结构图或者是Excalidraw图表那这些类型的内容在我上一期视频中有详细的讲解大家可以回看我上一期的视频那么到此第二个步骤query也就完成了

[10:55](https://www.youtube.com/watch?v=CTyx5XF2KVA&t=655s) 那随着知识库越来越庞大你的知识库也需要定期的进行维护和体检那这里就是卡帕西理念的第三个步骤巡检lint 那lint这个单词啊对于程序员来说非常熟悉也就是对代码进行健康检查是否符合代码规范那针对个人知识库也是一样的检查页面之间的矛盾已经被新资料取代的老旧信息检查没有加入双向链接的孤岛笔记或者笔记中的死链以及缺乏独立页面的重要概念那定期生成知识库的体检报告

[11:27](https://www.youtube.com/watch?v=CTyx5XF2KVA&t=687s) 我们在skills文件夹内创建一个新的skill 取名叫lint 在skill.md中写入相关的要求告诉智能体该如何分析我们的知识库那这里当然要优先读取index 索引文件和log日志文件然后再扫描完整个知识库后生成一份检查报告并给出下一步的修复计划那在这里我们加入了一些约束让智能体只生成报告然后在用户确认后才进行修复和修改而不是自己自行对笔记进行修改

[11:58](https://www.youtube.com/watch?v=CTyx5XF2KVA&t=718s) 那我们回到智能体的窗口直接输入/lint 那智能体就开始扫描整个知识库并进行健康检查了那最后生成了完整的报告我们在报告中可以看到未同步的索引以及多个死链同时还有一个知识冲突那智能体还列出了下一步的行动计划如何对这些问题进行修复那通过这样的方式就可以让我们的知识库保持长期的健康那么到此整个流程就已经介绍完毕了那上述实现方法可以说是一个最简单的入门级的实现

[12:29](https://www.youtube.com/watch?v=CTyx5XF2KVA&t=749s) 那实际上我们还可以做很多功能上的扩充比如集成Obsidian CLI工具那这一点在卡帕西的文章中也有讲那卡帕西就建议使用一些CLI 工具来辅助AI更高效地操作Wiki 有关Obsidian CLI这个官方命令行工具以及skill 在我之前的视频中也有详细的讲解大家可以回看我的往期视频那我接下来也会在这 3个skill中加入技能链约束智能体在检索知识库的时候使用Obsidian CLI skill 那这样可以大大降低token的消耗

[13:00](https://www.youtube.com/watch?v=CTyx5XF2KVA&t=780s) 并提升任务的准确性卡帕西表示自己在 40万字左右的知识库中这套理念运行得非常良好那持续的进化和积累特别适合中小团队和个人做深度的学习和研究那除非你是企业级一样非常庞大的知识库否则RAG永远都只是现用现搜的冷冰冰的机器那总体说来卡帕西的核心理念描绘的是在智能体时代个人知识管理的必然形态人类只做高价值的信息筛选与战略提问

[13:30](https://www.youtube.com/watch?v=CTyx5XF2KVA&t=810s) 而AI接管所有繁琐的节点编织我个人还是想要强调两个注意事项那第一个就是注意token的消耗那智能体对token的消耗是有目共睹的非常的高大家一定要注意这一点那另外一点就是要注意AI幻觉的问题那如果大模型在某次处理中产生了幻觉那么这个错误同样会被保存到知识库中未来的学习和推理都会以此为基础导致错误被无限放大那么以上就是今天视频的全部内容那视频中的笔记大家可以来我的个人网站下载

[14:02](https://www.youtube.com/watch?v=CTyx5XF2KVA&t=842s) 你可以在我的频道信息中找到我的个人网站整个知识库我都打包上传到了GitHub上那包括视频中所使用的提示词工程的原始资料大家可以直接下载下来进行尝试你可以在我的视频描述中找到我的GitHub仓库地址那如果有任何的问题欢迎给我留言那记得点赞关注谢谢大家
