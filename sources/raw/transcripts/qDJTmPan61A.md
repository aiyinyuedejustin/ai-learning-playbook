# 用 Claude Code 把 NotebookLM 深度集成到 Obsidian，补全你 Obsidian 的最后一块拼图！

- URL: https://www.youtube.com/watch?v=qDJTmPan61A
- Channel: 杰森的效率工坊
- Published: 2026-05-22
- Duration: 07:08
- Transcript: 本地语音识别 / local ASR, lang=zh, faster-whisper base
- Cite as: [mm:ss](timestamp link) — each line below starts with one

## Chapters

- [00:00](https://www.youtube.com/watch?v=qDJTmPan61A&t=0s) 效果演示：在 Obsidian 里直接调用 NotebookLM 的功能
- [01:40](https://www.youtube.com/watch?v=qDJTmPan61A&t=100s) 环境准备：AI Agent安装与 Obsidian 智能体插件
- [03:10](https://www.youtube.com/watch?v=qDJTmPan61A&t=190s) 安装 notebooklm-py、登录、配置skill
- [04:15](https://www.youtube.com/watch?v=qDJTmPan61A&t=255s) 验证安装：确认skill安装成功、登录成功
- [04:42](https://www.youtube.com/watch?v=qDJTmPan61A&t=282s) 实战工作流一：完全免费的 Deep Research
- [05:53](https://www.youtube.com/watch?v=qDJTmPan61A&t=353s) 实战工作流二：同步本地笔记到 NotebookLM，自动生成测验题、思维导图和语音播客
- [06:44](https://www.youtube.com/watch?v=qDJTmPan61A&t=404s) 总结与注意事项

## Transcript

[00:00](https://www.youtube.com/watch?v=qDJTmPan61A&t=0s) 如何将Notepo-RM的功能深度积设到OpCD﹑让你在OpCD中直接就可以使用所有Notepo-RM的功能。甚至直接调用Deprored Search为你做深度研究。我们先来看一下效果。在OpCD中我在AI对话课中发送指令,将我的OpCD笔记库中所有有关Cloud Code的知识笔记。上传道读不可AirRM中,并以这些笔记为来源,创建一份困难难度的测试题, 一部辩论形式的音频摘要和一份资讯途表。

[00:31](https://www.youtube.com/watch?v=qDJTmPan61A&t=31s) 将、生成的测试题以Markdown格式保存到5道OpCD中, 同时将音频摘要和资讯途表也保存到5道Op. 然后,然后,然后,然后,然后,这能体就开始调用相应的工具进行工作。这些功能都是是不可AirRM的功能。我们平时如果想要使用的话,是需要在宝业端登录的特布克AirRM并首动上传门的。而我现在要的只需要在OpCD中向AI发送指令,就可以直接调用的特布克AirRM的直接功能。我们来看一下生成的结果,

[01:15](https://www.youtube.com/watch?v=qDJTmPan61A&t=75s) 我们来到制式交锋。想像一下,你正在建造一栋高度智能化的金融城, 比如智普教M或者是DipSync,成功打通了CodeCode, 在中国大陆的本地化部属之后。今天,我就来为大家介绍如何使用CodeCode, 将NodeProper AirRM深度集成到OpCD中。所有的操作流程,我都整理成的门岛,最后会分享给大家。首先是工具的安装与环境搭建。你可以选择你喜欢的AI日子工具,比如CodeCode,OpenCode等等。

[01:49](https://www.youtube.com/watch?v=qDJTmPan61A&t=109s) 然后,我们会使用插件,将智能体工具集中的OpCD中。我在之前的视频中有详细详解如何为OpCD配置Code的插件以及以及AgentSkill,大家可以回看我的网期视频, 我们就来快速过一遍安装流程。目前主流程的插件有两个,一个是Code. 一个是AgentClide,具体的配置也很简单。

[02:21](https://www.youtube.com/watch?v=qDJTmPan61A&t=141s) 在第三方插件市场,下载?brt插件,然后插件设置界面点击i的BetaBlogging,填入插件名称,点击添加就可以了。然后,以Code.插件为例,在插件设置界面做一些基础设置, 比如把语言切换为中文,在如何充护你这里填入你的名字, ,就可以了。来到Code选项卡,如果你能够在命令行中正常啟动Code, 这里一般是不需要填给的那种,它会自动检测到Code的路径,

[02:52](https://www.youtube.com/watch?v=qDJTmPan61A&t=172s) 如果检测不到,在命令行中收入Weir.com.code,就可以插件路径, 然后把路径复制进来就可以了。回到Obsit.com见面,打开命令,运编把收入Code.打开聊天窗口, 在AI对话创中收入你好,AI进行回复,就说明配置成功了。接下来,我们要安装Notwork.org工具,首先我们要保证电脑上安装Python, 这个很简单,直接去Python官网向载,然后安装就可以了,没有什么特别的。然后打

[03:30](https://www.youtube.com/watch?v=qDJTmPan61A&t=210s) 等待安装完成,这里要注意,如果你是麦克系统,它有可能会提示是Extra.Mindage的Immortment这个错误,那紧续方法也很简单, 在刚才的命ga很简单,在刚才的命令后面添加两个参数就可以了。具体的命令我已经展示在屏幕上,安装好工具之后, 我们在命令行中运行Notwork.org控格LovV进行登录,它会自动打开这蓝器,让你登录Notwork.org。这里我们收入谷歌账号,我就不多做展示了,最后我们运行Notwork.org控制sql.

[04:01](https://www.youtube.com/watch?v=qDJTmPan61A&t=241s) 这个命令会为你的这种解工具安装一个AgentSql,这个sql其实很简单, 只有一个文件,你也可以手动复制到其他各种解工具中,比如HermesAgent或者是OpenCloth当中家。那么到此,我们就完成了所有的工具安装与环境大大界,我们在命令行中收入Notwork.org控格LovV,控格LovV, 如果提示身份业重成功,除了说,

[04:32](https://www.youtube.com/watch?v=qDJTmPan61A&t=272s) 像AI发送指定,列出你所拥有的所有Skills, AI列出的Skills中如果有Notwork.org这个sql, 就说名S在安装成功。接下来,我们就可以在Albusic里中使用任何词用Not Notwork,我列出了一些长运命令和使用长警在笔记中。接下来,我们来快速的常试两个工作流,首先, 我们调用Notwork.org的Departre Search深度研究功能, 对一个主题进行研究,然后把搜索到的文件资料

[05:03](https://www.youtube.com/watch?v=qDJTmPan61A&t=303s) 保存到Albusic里的笔记库中,同时让Notwork.org生成一份 PBT也是文导和研究报告,并保存到Albusic里跟幕录下。在Cloud.TV对话刊中,发送指定的制农体就开始工作了, 一般来说Departre Search需要15分钟左右来完成研究, 我们对视频进行一个加速,任务完成之后, 看到Departre Search搜索到的文件资料被保存到了RESERCH文件牙中, 同时,伤成了一份研究报告和一份也是文导, 那也是文导分别保存为了PBTF格式和PBT格式,

[05:36](https://www.youtube.com/watch?v=qDJTmPan61A&t=336s) PBT是可以直接进行编辑的, Notwork.org的Departre Search能完全免费, 而且一托于谷歌强大的搜索努力,对于Albusic里用后来说是非常实用的, 不然的话,

[06:47](https://www.youtube.com/watch?v=qDJTmPan61A&t=407s) 还是要注意一点,这个工具毕竟不是谷歌官方的工具, 未来会不会被谷歌封禁还不确定, 让大家且用且珍惜, 以上就是本期视频的全部内容, 大家如果在安装过程中遇到了什么问题, 欢迎随时给我留言, 视频中的文导资料可以在我的个人网站下载, 你可以在我的频道信息中找到我的个人网站, 记得点赞,关注,谢谢大家。
