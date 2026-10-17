# 矽谷大神 Karpathy 筆記術！十分鐘學會如何用 Claude Code 建立個人知識庫

- URL: https://www.youtube.com/watch?v=FdSO1Yhr76I
- Channel: Paula 寶拉
- Published: 2026-04-14
- Duration: 11:39
- Transcript: 本地语音识别 / local ASR, lang=zh, faster-whisper base
- Cite as: [mm:ss](timestamp link) — each line below starts with one

## Chapters

- [00:00](https://www.youtube.com/watch?v=FdSO1Yhr76I&t=0s) Karpathy 分享的方法在社群上瘋傳
- [00:36](https://www.youtube.com/watch?v=FdSO1Yhr76I&t=36s) 原始貼文重點：Wiki 會自己成長、會自己健檢
- [01:39](https://www.youtube.com/watch?v=FdSO1Yhr76I&t=99s) 系統架構：Raw、Wiki、Index、Log、claude.md
- [02:58](https://www.youtube.com/watch?v=FdSO1Yhr76I&t=178s) 需要的工具：Obsidian + Claude Code
- [03:33](https://www.youtube.com/watch?v=FdSO1Yhr76I&t=213s) 建立 Obsidian Vault 並初始化資料夾結構
- [05:27](https://www.youtube.com/watch?v=FdSO1Yhr76I&t=327s) 用 Obsidian Clipper 收集文章
- [06:44](https://www.youtube.com/watch?v=FdSO1Yhr76I&t=404s) 讓 Claude 讀文章、自動建立 Wiki
- [07:17](https://www.youtube.com/watch?v=FdSO1Yhr76I&t=437s) Graph View 看跨文章的自動連結
- [07:52](https://www.youtube.com/watch?v=FdSO1Yhr76I&t=472s) Wiki 頁面結構：Concepts、Entity、Source
- [08:29](https://www.youtube.com/watch?v=FdSO1Yhr76I&t=509s) 實際用法：問問題、找知識缺口、AI 補資料
- [09:53](https://www.youtube.com/watch?v=FdSO1Yhr76I&t=593s) 這方法跟傳統 RAG 的差異
- [10:43](https://www.youtube.com/watch?v=FdSO1Yhr76I&t=643s) 四個限制與適用場景
- [11:22](https://www.youtube.com/watch?v=FdSO1Yhr76I&t=682s) 總結

## Transcript

[00:00](https://www.youtube.com/watch?v=FdSO1Yhr76I&t=0s) 两片文章丢进去,AI自己产生这个,不用整理,不用分类,不用剪资料库,细股大成,分享的方法,在社群上风船,今天实际作为次给你看。因为没有一个情况,看到片,看到片文章觉得这个好重要,我一定要记住,结果两个离拜之后,完全想不起来再难看到的。或是你很认真,纯的说,千节图,全部丟到符记软体,一个月后打开看,慢慢的说,千,但完全不知道该从何开始着起。还有另外一个更常见的问题,A文章讲的一个概念,B文章从完全不同的角度也提到同认识。

[00:31](https://www.youtube.com/watch?v=FdSO1Yhr76I&t=31s) 但因为他们存在不同的地方,你不会发现这两个东西有关联。最近,Aun'tree 可怕自己,之前特斯拉的AI负责人,也是OP&AI的共同创办人之一,在X上面分享的这个方法来解决这个问题。- 它的做法是,B文章就给AI读完之后,自动成立成一个Weeky,有摘药,有目录,有概念资线的连接,全部存在你自己的电脑上,就是一段markdown的档案。但它在推文里面讲到几个,我觉得很关键的点。

[01:29](https://www.youtube.com/watch?v=FdSO1Yhr76I&t=89s) 它自己用这一套方法,整理的大概100篇文章,它说本来以为要用到REC,结果靠LLM自己维护,所以你就够了。在开始时就之前,我们先了解一下这个系统的重点,这样等一下Demo的时候会更容易理解。整个知识库,它就是一个Obsynian的主要的资料夹。第1个叫做ROW,就是你丢东西进去的地方。文章PDF或是你任何想要整理的原始资料,全部都先放在这,你可以把它想象成它就是一个收件杂。

[02:00](https://www.youtube.com/watch?v=FdSO1Yhr76I&t=120s) 第2个是We 就是AI帮你整理好东西的地方,它会把ROW里面的资料拆成一夜一夜的Weeky,每一夜都有摘药,有的标签,有连接到其他相关页面。然后Weeky资料备里面会有一个index,这个很关键,它就是整个知识库的目录列出所有的页面和分类。 AI每次要找资料的时候,不需要一天就要把所有的党案都读一遍,它只需要先读这个index,就知道要去哪里找。这也是为什么这个方法,就算有几百夜的资料差讯速度还是很快。

[02:31](https://www.youtube.com/watch?v=FdSO1Yhr76I&t=151s) 那还有一个Log,AI每次帮你做什么,多了哪 哪篇文章,新政的拿级也Weeky改的什么连接都会记在这边, 像你回头翻的时候也翻得到,AI自己下次也知道之前做过什么,不会重做。最后还有一个Cloud 点MD档,这个是给AI看的说明书,它告诉AI这个转案是什么,资料怎么整理Weeky该怎么写,每次你开Cloud 扣的时候,它会都会先读这个党案,所以它每一次都知道自己该做什么。那怎么开始呢,工具只需要两个,第一个Opc 点一个免费的笔记软体,

[03:03](https://www.youtube.com/watch?v=FdSO1Yhr76I&t=183s) 它的功能就是就是让你用图的方式子看到笔记之间的关联到Opc 点点MD下载就可以了,完全免费。第二个是Cloud 扣,AI 的引擎,负责读文章做整理,建立连接, 就是两个,安装步骤可以参考我之前的影片,放在资讯栏, 照着做几分钟就可以装好了,接下来我会一步一步带你做出, 如果你不想要错过之类的AI使用招学,还没订阅的话,帮我按一下订阅, 我是宝拉这个频道,专门分享AI工具的时侧跟招学,

[03:33](https://www.youtube.com/watch?v=FdSO1Yhr76I&t=213s) 好,安装Opc 点之后,我们就打开它,然后我们点击建立, 那名字这边我们就随便取那这边一样是开启我刚刚使用的AK Demo 的资料� 夹,那我们就打开中端机,然后输入Cloud,

[04:09](https://www.youtube.com/watch?v=FdSO1Yhr76I&t=249s) 然后我们把可拍子以它的概念贴进去, 那我们回到X 的画面,那这边就是它的Prom 放在Gist里面, 那我们就点击它,点击它说我们就会到这个画面, 那这个就是它的 promp 的内容, 底下其实有非常多人在讨论他们自己是怎么去做的, 有兴趣的话可以稍微看一下, 那我们就回到最上面的地方点

[04:45](https://www.youtube.com/watch?v=FdSO1Yhr76I&t=285s) 就全选复制,回到endigofity 的画面,我们就贴上它,然后请靠根据这个概念, 帮我建立好整个资料库的炸构, 那这边就稍微等它一下,好,它建立完成了, 那我们可以看到说它这边带我建立了这个rode 资料夹, 那里面有这个 ss,那还有这个 wiki 的资料夹, 还有这个 index 的所引业面,还有这个 logo 是它这次出实, 画这个记录,然后我们也可以打开靠点 mbi 看一下, 那你可以看到它写了很多这个专案的用途, 就是资料该怎么整理 wiki 的一些格式规范,

[05:16](https://www.youtube.com/watch?v=FdSO1Yhr76I&t=316s) 就是刚刚讲给iI看的说明书,以后每次打开靠扣, 它都会先�do 这个文件,不需要我们重复解释, 这是一个 what 者党实在做什么, 好,那架构已经建立好了, 那怎么样把文章放到我们 wiki 里面呢, 最方便的方法就是装一个 chrome 的擴充功能, 叫做 obsidian clipper, 那我们就把它加到 chrome, 那新增完成之后能把它按定损,

[05:47](https://www.youtube.com/watch?v=FdSO1Yhr76I&t=347s) 那我们这边找两篇文章, 那第一篇 便nawag 保典的作者, 讲的是阅读是学习的基础, 从你喜欢的东西开始读, 那我们这边就点损 obsidian 的这个擴充套件, 那我们在这个地方能把它改成我们的rode, 就是我们知道夹名称, 然后点击加到 obsidian, 那我们就可以看到说, 它在这个rode 的地方呢, 它有把它存取进来, 那我们来加第二篇文章,

[06:20](https://www.youtube.com/watch?v=FdSO1Yhr76I&t=380s) 那第二篇文章呢也是纳娃的写的, 讲的是你要找到属于自己的专属之时, 那种做起来, 你像是在玩别人看起来像是在工作的能力, 那么我们样点选 obsidian 的套件, 然后把它修改成rode, 那 add to obsidian, 那样就会这样子 ingest 进来, 那我们就回到我们 antigraphy 的画面, 来操作 cloud

[07:10](https://www.youtube.com/watch?v=FdSO1Yhr76I&t=430s) 然后我们就在上面加进木路里面, 那我们就稍等它一下, 那这边 cloud 扣跑完了, 我们就回到 obsidian 的画面看一下, 那可以看到说它这边已经有建立了这个 graph, 那我们可以看一下这个 graph view, 就是两篇文章呢, 它其实都产生了各自的节点, 但有一些它是有跨过去, 比如说,这个持续学习的部分呢, 它就是把这两个关联抓出来, 然后形成一个共同的节点, 那这就是这一套系统,

[07:41](https://www.youtube.com/watch?v=FdSO1Yhr76I&t=461s) 我们叫厲害的地方, 就是 aii 其实也把我们发现这两篇文章的共同点, 然后自动把它们连在一起, 那你丢了文章越多呢, 这种跨文章的点节却越多越有用, 那看完 graph 之后呢, 我们来看一下 wiki 面的内容, 那 concept 它就会把刚刚那两篇文章中的一些概念呢, 独立成一个页面出来, 分别解释它的定一个一个一个一个一个一个, 那 entity 的部分呢, 它就是会把刚刚两篇文章中有提到的这个, 人物啊,

[08:12](https://www.youtube.com/watch?v=FdSO1Yhr76I&t=492s) 记录它是谁跟哪些概念有关的一些内容, 那壽司的部分呢, 就是把我们丢进去每一篇原始文章, 记录这篇文章讲了什么, 它对应到哪一些salt 概念跟一些重点, 那三种页面之间互相点节, 就是我们的这个 graph 显示出来的画面, 那有什么关系, 一个是在讲准程, 一个是在讲读书, 这两件事情想要问它说它是什么接起来的,

[08:44](https://www.youtube.com/watch?v=FdSO1Yhr76I&t=524s) 那么就输入这样的内容, 等它的回复。那这种画文章的问题呢, 自己读完不一定会想到这样的连接, 但是AI可以, 所以它就會根据我们放进去的这些资讯去, 把我们做回�'s 复。那我可以再问一个更具体的问题,就是, 如果我现在不知道自己的 专属, 那那娃會陣營我怎麼做那他就會綜合兩篇文章來回答我的問題那娃就是認為就是先培養這個好奇心

[09:17](https://www.youtube.com/watch?v=FdSO1Yhr76I&t=557s) 然後找你喜歡的東西那觀察自己做什麼事情上是在玩別人像是那就可以幫我們找到哪一些知識是我們可以補充的然後他也可以來幫我們搜尋一下所以他第三個跟進階的做法就是他可以幫我們去找一些資料做補充

[09:49](https://www.youtube.com/watch?v=FdSO1Yhr76I&t=589s) 那這就是這個Wiki的這個實際的用法如果你有在關注AI技術可能聽過Rag這個名詞那他就是讓AI去搜尋資料庫來回答問題那可Pathlete呢他這個方法跟傳統Rag最大的差異他完全不需要上量資料庫跟營賓頂傳統Rag要把文章協成一塊一塊轉換成上量純淨資料庫查詢的時候是靠相似度去搜尋設定門檻也比較高那這個方法呢就是有一堆mark到檔案加上一個index

[10:20](https://www.youtube.com/watch?v=FdSO1Yhr76I&t=620s) AI靠著獨木路跟連結找資料不靠相似度做搜尋那好處就是設定簡單為互容易成本基本上就是AI的頭管費用壞處就是他有規模上限制他實測大概100篇文章是沒問題的但如果你要處理上萬份文件那就可能需要真的Rag系統了這大部分的個人使用者來說我覺得這個方法實就蠻夠用的那我們就按照慣例來說一下限制第一個Coco需要錢它需要付費訂閱才可以做使用

[10:50](https://www.youtube.com/watch?v=FdSO1Yhr76I&t=650s) 那Obsidian則是免費那第二個Ingress需要時間每篇文章大概要跑幾分鐘如果你一次丟有30篇進確的話可能要等10到15分鐘那第三個它比較適合個人的規模如果幾十遍到幾百遍是沒問題但如果是上萬份文件的話可能就需要使用其他的工具那第四個支持庫月大月花頭肯因為

[11:20](https://www.youtube.com/watch?v=FdSO1Yhr76I&t=680s) 如果你是使用API機費的話這個成本就會很客觀 OMJREKOPASSY這個方法兩個資料夾上一個AI就搞定了那如果您的影片的話就直接開始吧先丟兩三篇文章進去看看效果如何那今天這集就到這邊歡迎在底下留言告訴我你想聽什麼主題按讚訂閱開啟小鈴鐺我們下次見
