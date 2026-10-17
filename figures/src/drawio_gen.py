"""生成 skills-flow 和 repo-map 两张 Draw.io 图（.drawio 源文件）。导出：drawio -x -f png -s 2 -b 12 -o ../X.png X.drawio"""
from xml.sax.saxutils import escape
F="fontFamily=Noto Sans CJK SC;fontSize=13;html=1;"
class D:
    def __init__(s): s.c=[];s.n=0
    def box(s,i,t,x,y,w,h,fill="#ffffff",stroke="#666666",extra=""):
        s.c.append(f'<mxCell id="{i}" value="{escape(t,{chr(34):"&quot;"})}" style="rounded=1;whiteSpace=wrap;arcSize=12;fillColor={fill};strokeColor={stroke};{F}{extra}" vertex="1" parent="1"><mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>')
    def zone(s,i,t,x,y,w,h,fill):
        s.box(i,t,x,y,w,h,fill,"none","arcSize=3;verticalAlign=top;fontStyle=1;fontSize=15;")
    def edge(s,a,b,label="",color="#888888",extra="",dy=0):
        s.n+=1;g='<mxGeometry relative="1" as="geometry"/>' if not dy else f'<mxGeometry relative="1" as="geometry"><mxPoint x="0" y="{dy}" as="offset"/></mxGeometry>'
        s.c.append(f'<mxCell id="e{s.n}" value="{escape(label)}" style="endArrow=block;strokeColor={color};strokeWidth=2;labelBackgroundColor=#ffffff;{F}{extra}" edge="1" parent="1" source="{a}" target="{b}">{g}</mxCell>')
    def save(s,fn,name):
        open(fn,"w").write(f'<mxfile><diagram name="{name}"><mxGraphModel><root><mxCell id="0"/><mxCell id="1" parent="0"/>'+"".join(s.c)+'</root></mxGraphModel></diagram></mxfile>')

# skills-flow
d=D()
d.box("pref","preferences.md<br>我的偏好（每个 skill 先读）",360,10,300,50,"#fff2cc","#d6b656")
d.zone("zq","简单版",20,90,250,330,"#eef4fb")
d.box("quick","learn-quick 速读报告<br><br>给一个主题<br>→ 一份 md 报告<br>（可配 Draw.io 图、自测题）<br><br>读完就完",40,130,210,200,"#dae8fc","#6c8ebf")
d.zone("zf","完整版",290,90,720,330,"#f3f9ee")
d.box("probe","learn-probe<br>摸底",310,140,120,60,"#d5e8d4","#82b366")
d.box("nmap","learn-map<br>画地图",470,140,120,60,"#d5e8d4","#82b366")
d.box("teach","learn-teach<br>授课加小测",630,140,140,60,"#d5e8d4","#82b366")
d.box("diag","learn-diagnose<br>诊断误解",860,140,130,60,"#d5e8d4","#82b366")
d.box("track","learn-track 记录进度和缺口<br>learning/主题名/ goal.md · map.md · log.md · gaps.md · lessons/",310,300,680,70,"#ffffff","#82b366")
d.edge("probe","nmap");d.edge("nmap","teach")
d.edge("teach","diag","缺口多了")
d.edge("teach","nmap","缺前置","#d6604d","exitX=0.5;exitY=0;entryX=0.5;entryY=0;edgeStyle=orthogonalEdgeStyle;",dy=0)
d.edge("diag","teach","补前置","#d6604d","exitX=0.5;exitY=1;entryX=0.8;entryY=1;edgeStyle=orthogonalEdgeStyle;",dy=0)
for x in ["probe","nmap","teach","diag"]: d.edge(x,"track","","#bbbbbb","dashed=1;endArrow=open;")
d.edge("quick","probe","想深入","#6c8ebf","dashed=1;exitX=1;exitY=0.3;entryX=0;entryY=0.5;",dy=-12)
d.save("skills-flow.drawio","skills 怎么配合")

# repo-map
d=D()
d.box("goal","成品：skills/<br>我自己的学习助手<br>简单版 1 个 + 完整版 5 个",310,20,300,80,"#d5e8d4","#82b366","fontSize=15;fontStyle=1;")
d.box("pref","preferences.md<br>我的偏好，测完随时改",760,30,220,60,"#fff2cc","#d6b656")
d.box("ch","chapters/ 六章调研<br>为什么这么学：记忆、检索、<br>间隔、人机分工、工具栈",60,170,300,90,"#dae8fc","#6c8ebf")
d.box("src","sources/ 来源库<br>325 条别人的真实做法<br>方式 · 产物 · 工具 · 评分",560,170,300,90,"#dae8fc","#6c8ebf")
d.box("raw","网上几百个人的经验<br>X · YouTube · B 站 · GitHub · 博客 · 论文",310,320,300,60,"#f5f5f5","#999999")
d.edge("raw","src","收集")
d.edge("src","ch","归纳",dy=-12)
d.edge("ch","goal","原理")
d.edge("src","goal","挑做法")
d.edge("pref","goal","按我的习惯改",dy=-20)
d.save("repo-map.drawio","仓库地图")
