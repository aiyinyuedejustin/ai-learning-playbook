import os
CSS="""<style>body{margin:0;font-family:'Noto Sans CJK SC',sans-serif;background:#fff;color:#1f2937}
.w{padding:32px 40px;width:%dpx;box-sizing:border-box}h1{font-size:26px;margin:0 0 18px}
.row{display:flex;gap:14px;align-items:stretch}.box{border-radius:12px;padding:14px 16px;flex:1;font-size:15px;line-height:1.55}
.box b{display:block;font-size:18px;margin-bottom:6px}.arr{align-self:center;font-size:26px;color:#9ca3af}
.c1{background:#eef2ff;border:2px solid #6366f1}.c2{background:#ecfeff;border:2px solid #06b6d4}.c3{background:#f0fdf4;border:2px solid #22c55e}
.c4{background:#fffbeb;border:2px solid #f59e0b}.c5{background:#fdf2f8;border:2px solid #ec4899}.g{background:#f9fafb;border:2px solid #d1d5db}
.note{font-size:14px;color:#6b7280;margin-top:14px}.tag{display:inline-block;font-size:12px;padding:1px 8px;border-radius:9px;background:#111827;color:#fff;margin-right:4px}
.opt{background:#9ca3af}</style>"""
def page(w,body): return "<html><head><meta charset=utf-8>"+CSS%w+"</head><body><div class=w>"+body+"</div></body></html>"
F={}
F['overview']=(1400,"""<h1>用 AI 学新领域：五个环节</h1><div class=row>
<div class='box c1'><b>1 对齐</b>为什么学、学完能做到什么<br><span class=tag>必备</span>MISSION.md<br><span class='tag opt'>可选</span>grill-me 追问</div><div class=arr>→</div>
<div class='box c2'><b>2 拆章</b>大主题拆成模块和章节，每章有验收标准<br><span class=tag>必备</span>大纲<br><span class='tag opt'>可选</span>anything-to-course</div><div class=arr>→</div>
<div class='box c3'><b>3 短课</b>每次 25–50 分钟一节<br><span class=tag>必备</span>短课<br><span class='tag opt'>可选</span>Matt teach、pstack 讲代码</div><div class=arr>→</div>
<div class='box c4'><b>4 检索</b>当天闭卷自测，第二天讲回<br><span class=tag>必备</span>小测、讲回<br><span class='tag opt'>可选</span>Tutor 测验</div><div class=arr>→</div>
<div class='box c5'><b>5 间隔复习</b>讲回通过的才做卡<br><span class=tag>必备</span>Anki / FSRS<br><span class='tag opt'>可选</span>AnkiConnect</div></div>
<div class=row style='margin-top:18px'><div class='box g'><b>贯穿全程：学习记录</b>上次学到哪、哪里卡住、下次复习什么</div>
<div class='box g'><b>每天</b>复习到期卡 → 一节新课 → 闭卷自测 → 记薄弱点</div><div class='box g'><b>每周</b>不用 AI 的混合测验 + 一个小项目</div></div>
<div class=row style='margin-top:14px'><div class='box c3'><b>这样做</b>先自己想再问 AI；AI 只给提示；短会话、跨多天</div><div class='box c5'><b>别这样做</b>第一天学 8 小时；AI 先给完整答案；对话里重问一遍当复习</div></div>""")
F['01-cram-vs-spaced']=(1100,"""<h1>一次学完 vs 分散学习：记忆保留示意</h1>
<svg width=1020 height=380 font-family='Noto Sans CJK SC' font-size=14><line x1=70 y1=320 x2=990 y2=320 stroke=#374151 /><line x1=70 y1=20 x2=70 y2=320 stroke=#374151 />
<text x=10 y=30>记得</text><text x=10 y=320>忘了</text>
<g fill=#6b7280><text x=60 y=345>第 0 天</text><text x=230 y=345>第 1 天</text><text x=400 y=345>第 3 天</text><text x=600 y=345>第 7 天</text><text x=900 y=345>第 30 天</text></g>
<path d='M80 40 C 200 160, 350 260, 980 300' stroke=#ef4444 stroke-width=4 fill=none />
<path d='M80 70 C 150 150, 220 170, 245 175 L245 70 C 330 140, 390 150, 415 150 L415 65 C 520 110, 590 115, 615 115 L615 60 C 760 85, 880 95, 980 100' stroke=#22c55e stroke-width=4 fill=none />
<rect x=650 y=180 width=330 height=80 rx=10 fill=#f9fafb stroke=#d1d5db /><line x1=665 y1=205 x2=700 y2=205 stroke=#ef4444 stroke-width=4 /><text x=710 y=210>第一天连学 8 小时：当天最高，掉得最快</text>
<line x1=665 y1=240 x2=700 y2=240 stroke=#22c55e stroke-width=4 /><text x=710 y=245>每天短会话 + 隔天复习：每次回升，越来越稳</text></svg>
<div class=note>示意图，不是实测数据。依据：间隔效应（Cepeda 等）、检索练习（Roediger 与 Karpicke）、一口气看完衰减更快（Horvath 等）。</div>""")
F['02-roles']=(1100,"""<h1>AI 当教练，人当运动员</h1><div class=row><div class='box c2'><b>AI 负责：不必要的难</b>找资料、整理材料<br>起草大纲<br>讲解卡住的地方，一次一个提示<br>出题、判分、指出缺口<br>起草卡片、排复习日程</div>
<div class='box c4'><b>人负责：必要的难</b>拍板目标和取舍<br>选定权威材料<br>先自己读、先自己试<br>闭卷回忆、第二天讲回<br>删改卡片，每天清掉到期复习</div></div>
<div class=row style='margin-top:14px'><div class='box g'><b>四条硬规则</b>① 先自己想，再问 AI　② AI 不先给完整答案　③ 用自己选的材料　④ 对话里重问一遍不算复习</div></div>""")
F['02-teach-family']=(1200,"""<h1>同叫 teach，其实是三种东西</h1><div class=row>
<div class='box c1'><b>Matt 的 /teach</b>目标：花几周系统学会一门主题<br>形式：当前目录就是课程仓库，跨会话<br>产物：MISSION.md、RESOURCES.md、HTML 短课、学习记录<br>场景：「我要系统学 X」</div>
<div class='box c3'><b>pstack 的 /teach</b>目标：把一段代码讲明白<br>形式：单次讲解，不建课程<br>产物：讲解文字、架构图<br>场景：「这段代码怎么跑」</div>
<div class='box c5'><b>Tutor 类（claude-tutor 等）</b>目标：学过的过几周还记得<br>形式：学习者档案，跨会话<br>产物：学习计划、测验、复习日历<br>场景：「学完还要记得住」</div></div>
<div class=note>三者可以串在同一条流水线上：课程工作区负责教，讲代码负责读懂，Tutor 负责记住。不能互相替代。</div>""")
F['03-session']=(1200,"""<h1>一次 60 分钟的学习会话</h1><div class=row>
<div class='box g' style='flex:1'><b>0–10 分钟</b>不看材料默写<br><span class='tag opt'>AI 关</span></div>
<div class='box g' style='flex:1.5'><b>10–25 分钟</b>自己做题或读新材料<br><span class='tag opt'>AI 关</span>卡住 5 分钟再开</div>
<div class='box c2' style='flex:1.5'><b>25–40 分钟</b>处理卡住的地方<br><span class=tag>AI 开</span>每次一个提示</div>
<div class='box c2' style='flex:1'><b>40–50 分钟</b>按笔记出题判分<br><span class=tag>AI 开</span></div>
<div class='box c4' style='flex:1'><b>50–60 分钟</b>自己的话写最难点<br><span class=tag>AI 开</span>只打分</div></div>
<div class=row style='margin-top:16px'><div class='box c3'><b>第二天</b>不看材料讲回 → AI 按评分标准判 → 通过的做成卡片，不通过的换角度重讲、再隔一夜</div></div>
<div class=note>新内容不超过一次会话的一半时间；结束前关掉 AI 再默写一次。</div>""")
F['04-pipeline']=(1300,"""<h1>学习流水线：从信息来源到每天复习</h1><div class=row>
<div class='box g'><b>信息来源</b>YouTube、论文、博客、X</div><div class=arr>→</div>
<div class='box c1'><b>阅读器</b>Readeck、Readwise、Zotero<br>高亮、摘录</div><div class=arr>→</div>
<div class='box c2'><b>笔记库</b>Obsidian 或课程目录<br>自己的话写，链回来源</div><div class=arr>→</div>
<div class='box c3'><b>AI 导师</b>追问、出题、判分<br>讲卡住的地方</div><div class=arr>→</div>
<div class='box c5'><b>Anki</b>人审过的卡片<br>每天复习</div></div>
<div class=row style='margin-top:12px'><div class='box c4'><b>回流</b>到期没记住的卡 → 下次 AI 会话的薄弱点</div></div>
<div class=row style='margin-top:12px'><div class='box g'><b>学之前</b>grill-me / interrogate 拆章节、定验收标准</div><div class='box g'><b>学之中</b>Matt teach 或分章 agent：一节短课 + 测验</div><div class='box g'><b>学之后</b>arena 比较多种解法；Orca / Multica 并行实现</div></div>""")
F['05-scope-to-chapters']=(1300,"""<h1>从大主题到复习日程</h1><div class=row>
<div class='box g'><b>大主题</b>一堆材料<br>一个陌生领域</div><div class=arr>→</div>
<div class='box c1'><b>能力地图</b>学完能做到的可观察的事<br>MISSION.md</div><div class=arr>→</div>
<div class='box c2'><b>章节</b>按依赖排序<br>每章有入门诊断题<br>00-syllabus.md</div><div class=arr>→</div>
<div class='box c3'><b>课节</b>先尝试 → 原理 → 例题 → 练习<br>modules/</div><div class=arr>→</div>
<div class='box c4'><b>检查点</b>混合练习<br>99-checkpoint.md</div><div class=arr>→</div>
<div class='box c5'><b>复习日程</b>+1 天 / +7 天 / +30 天<br>review-schedule.md</div></div>
<div class=note>大纲：anything-to-course 或手写。每章课节：Matt teach。读代码：pstack。不要一次生成整本课。</div>""")
F['06-failure-modes']=(1200,"""<h1>七种常见的失败方式</h1><div class=row>
<div class='box c5'><b>1 流畅感错觉</b>读懂讲解当成学会了</div><div class='box c5'><b>2 没有间隔复习</b>笔记很漂亮，从不复习</div><div class='box c5'><b>3 一天学 8 小时</b>当天最多，忘得最快</div><div class='box c5'><b>4 把 AI 当拐杖</b>关掉 AI 就做不出来</div></div>
<div class=row style='margin-top:12px'><div class='box c4'><b>5 自动制卡泛滥</b>没审过的卡导入，队列爆炸</div><div class='box c4'><b>6 嫌慢关掉学习模式</b>AI 又变回答案机</div><div class='box c4'><b>7 工具栈太重</b>搭系统挤掉了学习</div></div>
<div class=row style='margin-top:12px'><div class='box c3'><b>对策</b>先自己想 · 短会话跨多天 · 讲回通过才做卡 · 从三样工具起步</div></div>""")
for k,(w,b) in F.items(): open(k+'.html','w').write(page(w,b))
