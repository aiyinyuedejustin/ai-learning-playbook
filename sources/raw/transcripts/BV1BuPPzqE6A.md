# Claude Code + NotebookLM = 通关秘籍

- URL: https://www.bilibili.com/video/BV1BuPPzqE6A
- Channel: 云桥网络
- Published: 2026-03-04
- Duration: 10:08
- Transcript: 本地语音识别 / local ASR, lang=zh, faster-whisper small
- Cite as: [mm:ss](timestamp link) — each line below starts with one

## Transcript

[00:00](https://www.bilibili.com/video/BV1BuPPzqE6A?t=0) Coreco堪称全球最强研究助手,但只需配上这个神器,就能解锁它的全部潜能。现在大多数人用Coreco做研究,只会让它上网搜一下,然后起到搜回来的结果能凑合用。但咱们可以玩得更溜,因为如果如果用Coreco 只需花五分钟设置一下,就能在Coreco 里打造自动化工作溜, 可以抓取YouTube任意视频片段、提取字幕内容,然后把信息推送到一个免费又强大的现成那个系统, 让它把我们搞定所有繁重的分析和处理工作。最后把分析结果变成各种成品�PPT、信息图、波克要杀有杀,而且几乎不花一分钱,败币。

[00:34](https://www.bilibili.com/video/BV1BuPPzqE6A?t=34) 如果这听起来好的不像真的,你的怀疑很正常,但这次例外,所以今天我要给大家安理一个最被低估的AI神器, Notebook LAM。在今天的视频里,我就来演示如何强强联合Coreco和Notebook LAM,免费搭建一套研究系统,省下每月几百美刀的开发和维护费。我超想跟大家分享这个,咱们马上开始,咱们先来个实战演示,让大家看看怎么用Coreco炸干Notebook LAM的所有功能,我们甚至无需离开中端界面。接下来,这个指令会让Coreco执行一连串操作。第一步,我们会动用自定义的YouTube搜�,搜索功能,去搜罗关于Coreco技能的最新爆款视频。

[01:10](https://www.bilibili.com/video/BV1BuPPzqE6A?t=70) 大家别急,我稍后就给大家一展示这些技能,并教!教你们怎么搞到手。等我们找到视频链接后,我就让Coreco调用Notebook LAM功能,把这些链接统统扔给Notebook LAM去处理。接着,就让Notebook LAM对这些视频来个深度剖析,挖出最顶尖的跨扣技能都有哪些,然后,把这份判断报告给我弄回来。不光如此,我还得有个实实在在的铲出物。我不光要文字分析,还得要一张信息图,用手绘蓝图的那种风格,把对顶级技能的分析给可视画出来。

[02:10](https://www.bilibili.com/video/BV1BuPPzqE6A?t=130) 这些文字分析,还得出了排名前五的Coreco技能,就是大家现在看到的这些还包括他们使用方式的一些新趋势。接着,它就为我们生成了那份信息图,并且自动保存到了我们的项目文件家里。大家来看一下这份信息图。再强调一下,这背后是NanoBnanoPro在驱动,它实际上被称为,这里的文字和所有视觉设计都契合我们要求的风格,也就是那种手绘蓝图的风格,其次也是更重要的一点。所有这些内容都基于视频极其分析,而不是在那里瞎编。我们还能在Coreco里面看到,它抓取到的视频信息、标题、作者、播放量、时长和发布日期。

[02:46](https://www.bilibili.com/video/BV1BuPPzqE6A?t=166) 所有这些信息也都同步体现在Nodebook Allen里。我能看到它上传的所有原文件,也能看到所有的分析结果。还能看到我们要求生成的 the 蓝图 图指南,虽然这个演示看起来只是这项技术一个相当基础的应用,但我必须强调,将这两款工具结合使用的附加值不容小区。因为这远不只是为Nodebook Allen自动化资料来源处理而已,我们刚才做的这一切,其实也完全可以在Nodebook Allen 里手动操作,不是吗?我本来可以手动去YouTube上翻掌,把所有我想看的视频都找出来,然后一个个复制粘贴进去,最终也能拿到分析报告和成果交付。

[03:20](https://www.bilibili.com/video/BV1BuPPzqE6A?t=200) 能把这个过程自动化当然很棒,但它的意义远不止于此,关键在于我能轻松把所有分析结果无缝整合到我的Quad扣身态理,这种工作流的应用场景可以说是无穷无见。这套工具组合威力惊人的第二个原因,完全在于Nodebook Allen本身强大的实力。如果你想手动附建Nodebook Allen 的功能,它相当于把爬虫系统、Rag系统、分析系统和成果交付系统整合成一条龙服务,什么信息图表、演示文稿等等全都能搞定,那绝对会让人头疼的要命。我亲自试过,至少在研究环节用过N8n这类工具,这个过程一点都不简单,而且还得花钱。

[03:56](https://www.bilibili.com/video/BV1BuPPzqE6A?t=236) 而现在这整套方案完全免费,这也就是为什么我迫不及待想和大家分享。还有一个让你心动的理由,就是这套方案搭建起来超级简单,这正是我们接下来要介绍的内容。那么说到具体如何设置,你可能会想,嘿 Chase,我们究竟该如何将Nodebook Allen与Quad扣对接呢? 毕竟Nodebook Allen并没有提供公开的API接口,不过幸运的是早有高人想到了办法,他们已经帮我们搞定了这个难题。这位高人就是Tangling,今天我们就要站在巨人的正坊上,借助Nodebook Allen拍这个D-Hob倉库,他就能充当Nodebook Allen的非官方拍发那Pi。

[04:31](https://www.bilibili.com/video/BV1BuPPzqE6A?t=271) 不过,在配置Nodebook Allen之前,我们得先搞定整个流程的第一步,也就是从YouTube搜索并获取数据,这些数据正是我们要交给Nodebook Allen分析的。为此,我专门为Quad Code打造了一个YouTube搜索技能,它能帮你一键搞定所有步骤。这个技能基于一个拍发脚本,它调用了YTDLP这个依赖库,来帮我们抓取YouTube的视频源数据。所以,当我向它提问,比如,嘿,找找Quad Code相关的技能视频,它就相当于替我们上YouTube去搜索Quad Code技能这个关键词。

[05:01](https://www.bilibili.com/video/BV1BuPPzqE6A?t=301) 它能抓取视频标题、播放量、作者等所有关键数据。你现在,在Quad Code里看到的这个技能,就是用来教会Quad Code如何高效御用这个脚本的。现在,要让这个技能和脚本跑起来,有两招方法。第一种方法相当简单,你只需要打开Quad Code,然后告诉它,你想让它帮你打造这个自定义技能。这个技能要使用YTDLP这个工具,来创建一个定制的YouTube视频信息抓取工具。或者,如果你想要这个完整的YouTube 搜索技能的设置文档、MB文件,

[05:31](https://www.bilibili.com/video/BV1BuPPzqE6A?t=331) 你可以直接下载下来,然后丢给Quad Code,该文件记得私信免费获取。等你把YouTube搜索技能的配置文件下载下来之后,直接丢给Quad Code,让它开工干活。或者,你也可以手动输入提示词,让Quad Code帮你搭建。现在,咱们回到这里,把notebook and lamb的连接配置好。安装过程超简单的。安装方法很简单,咱们只需要复制这几行命令,然后粘贴到中端里。注意,如果你现在看的是Quad Code的窗口,那就错了。

[06:02](https://www.bilibili.com/video/BV1BuPPzqE6A?t=362) 你需要另外打开一个像这样的中端窗口,然后把那几条命令粘贴进去。等这几条出使安装命令执行完后,你需要往下滚动到这里。我们还需要在命令行里再运行一条命令,也就是这条notebook and lamb的登录命令。和之前步骤一样,另开一个中端窗口,把这个命令粘贴进去。这样就会在空楼软机里弹出一个新窗口。你只需要登录即可,你只需操作一次,就万事大吉了。现在,在你用notebook and lamb账号完成登录验证后,还有一步需要完成,那就是安装这个技能。

[06:33](https://www.bilibili.com/video/BV1BuPPzqE6A?t=393) 那么,要在Quad Code里安装这个技能没错吧? 你既可以在中端里运行这条指令,或者直接吩咐Quad Code去执行。所以,也要理解我们刚才完成了什么。我们在notebook and lamb这边完成了两项操作。一个是这个技能,另一个是程序的实际API。请记住,技能本质上就是提示词。它其实就是一段文本,指导Quad Code如何按特定步骤完成任务。因此,你在这里看到的所有信息,比如黑,我们是这样生成内容的。我们是这样创建notebook的。

[07:03](https://www.bilibili.com/video/BV1BuPPzqE6A?t=423) 这个技能就是在教Quad Code如何实现这些操作。所以,一旦安装完毕,你只需要告诉Quad Code, 黑,用notebook and lamb帮我创建些抽准卡、信息图或者换灯片吧。就这么简单,全程都用大白话沟通。如果你好奇这个程序具体能用来干吗? 诺,所有信息都在github仓库里。凡是能在notebook and lamb里手动完成的操作都能通过API配合其他工具来实现。大家看,除了网页界面,我们还能进行批量下赛, 保出色验、删卡等等功能。

[07:33](https://www.bilibili.com/video/BV1BuPPzqE6A?t=453) 所以,使用这个程序我们实际上能获得更多功能, 这比你单纯自己打开notebook and lamb能做的要多得多。那么,咱们就一步一步来实际操作一下, 好让你明白它到底是怎么运作。那么,首先就是这个youtube搜索技能。和所有技能一样,我们可以把它当作席杠命令来用, 或者直接用大白话,自然语言也行。但如果我输入yT-SURGE,你会看到这里有查询和数量, 这两个是怎么调整的。那么,我们要搜点啥呢? 嘿,咱们来找找qoud代码技能相关视频。在之前的演示里,我们是一股脑全搞定的,

[08:05](https://www.bilibili.com/video/BV1BuPPzqE6A?t=485) 但我觉得有时候拆开一步一步来会更有帮助, 这样你就能先亲眼看看你将要用的资料来源到底是啥。小,这就是它返回的搜索结果,随时都可以查看, 我们也可以亲自去查验这些youtube�恋阶。这些技能的妙处在于,它还能让你动息一些内情, 关于它找回来的这些内容,到底是怎么回事。那么,如果你觉得这些资料没问题了, 咱们就可以把它们导入到notebook.lamb里了。再强调一遍,你直接用大白话就行, 在notebook.lamb里新

[08:36](https://www.bilibili.com/video/BV1BuPPzqE6A?t=516) 新建一个笔记本,标题就叫Chase demo,把咱们刚找的这些资料用上。看,笔记本已经建好了,现在它正往里面填充资料呢。等了几分钟,20个资料就全都加在好了, notebook.lamb最多只支持50个资料。到了这一步,你想让notebook干啥都行, 那咱们就可以问了,根据这些视频, notebook.lamb觉得cocco最牛的一项技能是啥。再强调一下,这是库就库在, 所有这些分析活都外包出去了。看这分析的可不是cocco,cocco也没花代币token, 它只花了点代币token,用来给notebook.lamb发个请求,

[09:06](https://www.bilibili.com/video/BV1BuPPzqE6A?t=546) 再把结果拿回来。但所有烧脑的活都是谷歌干的, 钱也是他们掏的。所以,cocco拿到了notebook.lamb的分析结果, 我们在notebook.lamb里面就能直接看到, 所以,你随时可以点进notebook.lamb里面去合适, 比如,想看看它参考了哪些字幕片段, 这个操作流程对所有产出物都使用, 也就是说,你想要音频摘要, 思维导图,记卡片,信息图, 右边这看到的任何东西, 你只要跟cocco说一声,它就能帮你搞定。就这么简单,至于你怎么用这个研究流程,

[09:37](https://www.bilibili.com/video/BV1BuPPzqE6A?t=577) 全看你自己,但我必须得说, 这玩意儿真的太绝了,怎么夸都不够, 这是表面上看着挺简单, 但说实话,如果你试过处 the 这类问题, 特别是跟YouTube 视频打交道, 并且还想从这些些视频里整理出一个知识库, 好让cocco或者其他AI助手能进行交互,这其实挺难的,对吧, 不仅非常耗时,而且过程不稳定,容易出错,

[10:08](https://www.bilibili.com/video/BV1BuPPzqE6A?t=608) 但现在,notebook.lamb免费帮你把这些麻烦事
