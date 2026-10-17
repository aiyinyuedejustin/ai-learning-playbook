# Reddit r/learnprogramming：ChatGPT 不是好的学习工具

- 链接：https://www.reddit.com/r/learnprogramming/comments/1dw1gou/chatgpt_is_not_a_good_tool_for_learning
- 作者：u/Nice2Inch（r/learnprogramming，1019 分，340 条评论）
- 获取方式：Reddit 帖子与评论全文（取自 Arctic Shift 公开存档）

---

## 帖子：ChatGPT is not a good tool for learning

Click baity title.  

I'm a Software Engineer that's currently mentoring an intern and my intern's reliance on ChatGPT is not a good sign. This intern is tasked with writing some test automation in a framework we're both unfamiliar with, so there is bit of learning we have to do.  
  
The problem is that, the other week, my intern was having issues writing a for loop in the new framework. His first and only idea was to ask ChatGPT how to write a for loop in said framework. And well, ChatGPT's solution was wrong so then the intern went to ask me what the problem was. Well first google result gave me the syntax for the for loop, which fixed the problem.  
  
  
My issue is that people who are learning or trying to get junior/entry level software engineering positions are relying on a service that gives wrong answers and take it as fact. There was no attempt to google the answer by my intern, and if they had the issue would have been solved in 30 seconds.
And this intern will be starting their 4th year of CS at big university in the US.  
  
If my manager was to ask my opinion on hiring this intern as full time employee, I would not recommend hiring just because of their reliance on ChatGPT and poor debugging skills (which include googling). Had my intern attempted to google first, my opinion would be a bit more positive.  

On a side note, in my industry (fintech), if you copy paste code into ChatGPT to debug, you will be fired. It may be more relaxed for other fields, but other should be aware that exposing proprietary code to outside parties/applications is a huge security risk.
  

  
**EDIT**  
I'd like to clarify that this is not an anti-AI post. But rather a warning to those that rely heavily on AI to learn how to program. Don't rely solely on AI if you're having issues, use other resources such as google/stackoverflow/official documentation, etc. And yes, my team provided the framework documentation and I did tell my intern to try searching google/documentation next time.

## 评论（共收录 372 条，缩进表示回复层级）

**u/nutrecht**（590 分）：
I think the biggest issue by far with LLMs is that because it appears smart, people think it is. It's really just a dumb statistical model. Almost everyone doesn't really understand what it is. And all these people seem to vastly overestimate what it can do. So your intern really is one of the 'victims' of this.

> **u/Individual-Praline20**（39 分）：
> Totally agree with you on that…

> > **u/tominator93**（1 分）：
> > Yeah, this is an issue. I’m an established software engineer with coming up on 10 years of experience, and for me GPT has been amazing: a really solid sounding board that gives insightful answers 80-90% of the time. 
> > 
> > However, a decade of in the trenches engineering has given me really good intuition for bullshit answers, and I can usually tell extremely quickly when GPT is going out on a limb and giving me nonsense. 
> > 
> > I have no idea how I would have gotten along if this had launched when I was just starting to program.  We’ll have to see what sort of culture grows up in teaching programming to new hires in a world where GPT exists, we’re in the very early stages here.

> **u/8thdimensionalcat**（77 分）：
> Agreed I have so many classmates who use chatgpt for like electronics/math related questions when it’s just spitting out the most probable *looking* answer and 90% of the time it’s wrong. It’s decent at coding stuff but I always double check

> > **u/alfadhir-heitir**（15 分）：
> > It's awful at coding stuff

> > > **u/hoppity51**（31 分）：
> > > It's really not bad at all if you understand the project you're working on and the software you're using. It's saved me a tremendous amount of time.
> > > 
> > > The only major issue with its code generation is if you are using the free version. That version still tries to use a lot of deprecated functions.
> > > 
> > > It is also really helpful for learning a new technology. You just can't prompt it the same way you would if you just wanted code generation.

> > > > **u/alfadhir-heitir**（5 分）：
> > > > No. Its awful. If the tool requires you to have full knowledge of the project to do something than it's not much of a tool - those are supposed to abstract away stuff
> > > > 
> > > > ChatGPT is decent for menial work and as a fast Google so you don't have to really think about how to boil your problem down into a short sentence
> > > > 
> > > > That's pretty much all it can do accurately for the time being. And it won't get better until further advancements in AI tech pop up

> > > > > **u/delicious_fanta**（1 分）：
> > > > > Isn’t that literally the definition of a tool though? Intellij requires me to have full knowledge of the project as well. It just makes things faster and easier.
> > > > > 
> > > > > If you are expecting the llm to write your entire code base for you, while simultaneously reading your mind, that might be your disconnect there.
> > > > > 
> > > > > It’s not able to do that, and no reasonable person thinks it can. What it does do, however, is get some of the mundane stuff out of the way, can generate a solid function if you provide very specific instructions, help debug error codes, give you advice on migrating your gitlab project, help you learn python, etc.
> > > > > 
> > > > > It’s not perfect at any of those, as op calls out, but it is definitely good enough to be very useful and be a speed booster if your expectations are realistic and you figure out how to use it for what it’s good at.
> > > > > 
> > > > > After all, it is just a tool.

> > > > > > **u/alfadhir-heitir**（7 分）：
> > > > > > IntelliJ abstracts away a whole config build toolchain - autoconf - plus a bunch of debugging and LSP stuff so you can focus solely on your project 
> > > > > > 
> > > > > > So... Your point does not hold

> > > > > > **u/awkreddit**（4 分）：
> > > > > > People keep saying "it's a tool" as if that makes it a good tool. It's an awful tool. It's unreliable and doesn't let you know when it's misleading you. IntelliJ doesn't lie. It's a terrible tool.

> > > > > **u/theCamelCaseDev**（6 分）：
> > > > > I find it to be an amazing tool personally. Yeah it might not be the most amazing tool that does all the work for you when coding, and i think that's where a lot of people's opinions are formed. I've found google to be pretty trash these days, and stackoverflow also doesn't really help with anything complicated.
> > > > > 
> > > > > A lot of people I've found also only use the free version which I'll agree is trash.
> > > > > 
> > > > > I do a lot of architecture related work these days and using it as a coworker to bounce ideas off of is very helpful for me. Saves me a whole lot of time, and saves others time as well since I don't have to interrupt them.

> > > > > **u/hoppity51**（1 分）：
> > > > > I don't understand your point. How can you or GPT or anything solve your problem if you don't know what it is? You still have to understand what you are doing to effectively use any tool.
> > > > > 
> > > > > I also don't understand your second point. If I know conceptually how to solve the problem, I can give the snippet of related code to GPT, tell it what to do, and it mostly does just that. I now only have to make a few small edits instead of scrolling through documentation and articles. How is this not abstracting anything away? 
> > > > > 
> > > > > if you are giving it problems that you can't reduce down, it probably won't be able to help you that much. That's not what it's for, at least not at the moment.

> > > > **u/Nimweegs**（2 分）：
> > > > Honestly I find using a tutorial or a beginners guide way more useful than prompting chatgpt when starting a project in a tech I'm unfamiliar with.

> > > > > **u/hoppity51**（1 分）：
> > > > > I would not use GPT to setup environments unless you already know how to set-up that specific environment anyways. There's a lot more examples of coding a specific function than setting up an environment in this exact way with these exact dependencies. Use the documentation to set it up.

> > > > > **u/Agitated-Soft7434**（1 分）：
> > > > > So true. Not only are you getting actually good info and code that works. Your also getting context, and comments left on the guide which may fix any issues your having with potentially outdated code.

> > > > **u/Linkario86**（9 分）：
> > > > It really depends what you're working it. So far it's rarely been generating useful Code, but it definitely helps getting some information you want, which would be awful to google for.

> > > > > **u/vivals5**（1 分）：
> > > > > I'd say in my experience it's definitely terrible at getting information, but usually decent at generating useful code - even if not entirely correct at first. The information it gives is 99% of the time complete bullshit. Code is at least close to correct. I often use it to create kind of templates for my code that I just slightly modify and save a lot of time with it. But sure, anything complex and it's likely going to fail hard anyways.

> > > > > > **u/Linkario86**（1 分）：
> > > > > > Maybe it comes down to prompt engineering? Don't know. I always tell it something like "you are an expert <current topic role> ...". For boilerplate template it is absolutely useful in terms of code generation. But since I'm mostly working on an already built application, it's really hard to get any useful generated code out of it.

> > > > > > > **u/vivals5**（1 分）：
> > > > > > > It's definitely good at **seeming** like an "expert at <current topic>", but unless it's something about everyday stuff almost everyone already knows it spews so much incorrect bullshit, while making it sound correct to someone who's not already familiar with the <current topic>. Actually, what it usually gets correct are programming related questions in my experience. That makes sense too, since the LLMs are probably trained with a bunch of manuals and textbooks about those topics. Other topics tend to be full of inaccuracies.
> > > > > > > 
> > > > > > > On the topic of the OP, I do think it's a great tool to be used for learning programming, it just gets misused a lot. Once you already have a built application it makes sense the AI wouldn't be too useful since it likely won't be familiar with your app specifically.

> > > > > > > > **u/Linkario86**（1 分）：
> > > > > > > > Well yeah, in another comment I said it's useless if you're unfamiliar with the topic.

> > > > **u/HonestyReverberates**（1 分）：
> > > > On big projects it can't handle context at all. Constantly forgets and writes stuff badly. Gemini 1.5 is a little better with the context but the code isn't great. And Claude 3.5 I've yet to test, but planning to do so with a decent sized project.

> > > **u/pyordie**（58 分）：
> > > It's awful at coding **complex** stuff.
> > > 
> > > If it's coding a simple project or problem that a student typically has to write for a class, it's pretty good (which is why it's killing academia). 
> > > 
> > > Why? Because those problems and their answers and explanations have been posted online hundreds of thousands of times. Which is why it starts to fall apart very quickly as the project size and complexity increase - that's when you really start to notice that it's just guessing (because it's always guessing).
> > > 
> > > So it's fine if you need a quick introductory preview of a topic. I use it like I use google. I just take everything it gives me with a huge chunk of salt, same as everything on the internet.
> > > 
> > > What I can't fathom is how people try to debug their code with it. Such an insanely terrible habit.

> > > > **u/_nepunepu**（1 分）：
> > > > I work in controls and ChatGPT doesn’t know what to do as soon as you ask it something very slightly uncommon.
> > > > 
> > > > A few months ago, I asked it how to program a seal-in circuit in ladder logic (an extremely simple PLC programming pattern) and it gave me a random diagram.
> > > > 
> > > > Few weeks ago I heard the free model had been updated so I tried again, and this time it did show me a correct seal-in circuit. Then I asked it how to make a toggle (another very simple pattern) and it gave me gobbledigook again.
> > > > 
> > > > There are lots of Python tutorials and code that the model has scraped so it’s pretty good at tutorial level Python. It can’t do ladder logic at all.

> > > > **u/nicehatharry**（1 分）：
> > > > Sometimes it's just awful at coding stuff. I've gotten wrong answers to very simple coding questions from ChatGPT, sometimes because it hallucinates incorrect syntax, sometimes maybe because it doesn't distinguish language/library versioning well? It's hard to say. I find it most helpful to treat the output as if it's pseudocode.

> > > > **u/awkreddit**（9 分）：
> > > > You can't use it like you'd use Google, that's the point. You won't have comments or context to help you see if what it says is true, false or even applicable. Google gives you context and comments.

> > > > > **u/OneShoeBoy**（1 分）：
> > > > > That’s why I prefer the bing chat, it gives you links and references to where it’s pulling its info from. I use it like a research assistant (if I use it at all).

> > > > > **u/Asrikk**（0 分）：
> > > > > Technically, you *can* ask ChatGPT to cite sources. It just doesn't by default and most people don't bother challenging its answers. I've fiddled around with different prompts and found it to be relatively accurate with *educated* input. Though, that's the problem with it and academia. The inputs aren't educated.

> > > > > > **u/ShangBrol**（3 分）：
> > > > > > I guess they improved on that, but a year ago or so I was getting always invalid links when I asked for sources. ChatGPT was very good at inventing realistic looking links.

> > > > > > **u/Souseisekigun**（1 分）：
> > > > > > Well, yes, but the sources it gives you are made up. That's one of the way the academics catch the students using AI.

> > > > > > > **u/Asrikk**（1 分）：
> > > > > > > No, they aren't. It will literally source relevant documentation or sources. You can specifically ask it for more sources as well. Again, that goes to my point of *educated* input. If you take what it says at face value without knowing how/being able to check then that's not an educated use of it.

> > > > **u/DaFlamingLink**（6 分）：
> > > > Even in that situation I've found that it's usually faster to just do it myself tbh. The other day I tried to generate a quick `jq` command which seemed like the ideal use case (well documented, fast iteration time, well defined parameters). After 20 minutes of back and forth I gave up, quickly referenced the man pages, and got it done in 10
> > > > 
> > > > It's like walking someone through a PR without the benefit of that person becoming self-sufficient in the future

> > > > **u/Fresh4**（1 分）：
> > > > Using it to debug is a bad habit but if I’m doing so I’m pretty desperate anyway. I usually find that by typing out my problem and specifying all my context to the bot gets me halfway there, like when you’re doing the whole rubber duck method.

> > > > > **u/Ok-Switch-1167**（2 分）：
> > > > > In the past I've started to type out my problem and what I'm trying to fix. Before I pressed enter, I thought of the solution to the problem. So in that case it's a great tool 🤣.

> > > > **u/Any-Astronomer9420**（1 分）：
> > > > The Code is mostly awful and double.

> > > > **u/_alter-ego_**（1 分）：
> > > > It is not at all killing academia in the sense of replacing it or making it useless, but it is making huge damage(cost / loss / efficiency) because it makes it very difficult for teachers to assess the level / comprehension of the students: Even those who didn't understand anything in class can now easily produce solutions (homework, exams...) that make (unaware) teachers think they understood (and that require even aware teachers to make much more elaborate, "costly" checks of the stuff they have to grade). This is a big problem. Because tests and grades are not there to "punish" but in order to allow the teacher as well as the student to know what isn't yet understood and has to be studied more. People always forget that the goal is to convey competences, not diplomas.

> > > > **u/PlanResponsible5011**（1 分）：
> > > > I would also say that is great for testing simple/not very complex functions. But you have to be specific on what the use case you want to test and have knowledge on the testing framework to review the solution.
> > > > For frontend development testing works great, for understanding code also is great, to suggest simple code is also good at, providing basic examples of X framework. 
> > > > I have found that in terms of code copilot works better for me, also for legal stuff, but I do use a combination of google/copilot/chatgpt and so far my experience has been very good 👍🏾

> > **u/AyakaDahlia**（24 分）：
> > The math solutions it spits out can be so incredibly sus hahaha. Gotta just assume whatever it says is wrong and find the errors, ie you may as well have just not used it at all!

> > > **u/Dennarb**（25 分）：
> > > Realistically in order to effectively use LLMs for these types of things you have to have enough knowledge to know how to do the task without AI assistance. That way you can identify and correct erroneous results, but unfortunately most people relying on it for everything don't have that foundational knowledge...

> > > > **u/AyakaDahlia**（5 分）：
> > > > Yup. I was explaining that to a student I was tutoring just the other day. Don't know if they took it to heart, but one can hope.

> > > > **u/Iggyhopper**（6 分）：
> > > > This is called the "knowing *what* to Google" with industry terms.

> > > > **u/moratnz**（3 分）：
> > > > The best example of using LLM in education I've heard of is someone who set an assignment of 'get chatgpt to write an essay on X topic. Mark their essay and submit the marked essay as your assignment'.

> > > **u/tuskernini**（8 分）：
> > > i was talking with pi about a subject in the social sciences. i was pleasantly surprised at some of the answers it was giving me, so i asked it to recommend some literature for further reading. it gave me the names of books and articles that sounded amazing. i was so excited.
> > > 
> > > none of the fucking books/articles existed. pi made them up. and i start researching the subject we were speaking of, and turns out pi gave me some completely misleading information.

> **u/Minute-Angel**（2 分）：
> Thank you - this is exactly what it is but nobody listens (especially the VCs/investors)

> **u/Visual_Collar_8893**（15 分）：
> One would hope that a CS should have decent critical thinking skills to understand this.

> > **u/10ioio**（1 分）：
> > People that whine about others "critical thinking" are usually have their own massive blind-spots I've noticed. 
> > 
> > 
> > I think it has to do with "the man who really knows something knows that he knows nothing at all."

> > > **u/Visual_Collar_8893**（1 分）：
> > > No one in this world is without blind spots of some sort. No one.

> **u/DryBoysenberry5334**（5 分）：
> I’ve had good results personally with using it to organize my own research. That is I’ve got a ton of PDFs, webpages, ebooks, and other references materials. I had it write neat little summaries for everything, and now I can go and ask it stuff like “which item has this information in it” and it works wonderfully.
> 
> I would not trust it for a second to do any actual research though as it’s often wrong or seems to try to answer what it thinks you want to hear. (I understand it’s not actually thinking)
> 
> It’s sped up my hobby writing significantly, and as someone with ADHD that will often get easily distracted by my own reference materials it’s a good boon. 
> 
> This is the ONLY practical and applicable use I’ve found so far. 
> 
> I’ve tried to have it do simple programming tasks, and it has serious trouble remembering “okay we’re not using python 3.10” by itself that tells me this stuff isn’t ready for real programming yet. It can do stuff, and it works pretty good when it’s a language it’s got loads of training data for, but it makes the weirdest mistakes and continues making them even after explaining the problem.

> > **u/ghosts_dungeon**（1 分）：
> > They're good at finding and creating. They don't do so well with negatives. They're basically a living metaphor of, don't think of an elephant.

> **u/xHeylo**（9 分）：
> I've been saying for years, Computers are Idiots, because they only do exactly what they are told to
> 
> Garbage in, Garbage out
> 
> Most data of heavily engaged with posts were this heavily engaged not because the Post was correct, but because it most likely is an extreme or objectively wrong take
> 
> This leads to LLMs being trained on bad data leading to bsd outputs
> 
> For all not sufficiently advanced programs to be classified as real Artificial Intelligence the Output is predictable, and even if the program includes a generative Neural Network it's still just code, the Neural Network is just an interpreter to optimize (probable) desired outcome, but if either the Interpreter is crap or the Question that is to be interpreted is crap, the Outcome will necessarily be crap

> > **u/awkreddit**（15 分）：
> > It's not just about the training set. It's about the fact that it's a language model, not a knowledge database. It knows which words are not likely to follow which other words, that's all. It doesn't not have access to knowledge as you would conceive, like a documentation or sources etc. Only to a giant database of words and most likely next word. Saying these tools would work if the data was better is fundamentally misunderstanding the tech it uses and also could lead to thinking a better training would fix the issue, but it can't. Because that's not how it works.

> > > **u/xHeylo**（5 分）：
> > > Yea it's basically pulling an elaborate auto complete 
> > > 
> > > And if you go 15 words down auto complete it will have all the words of a functioning sentence, but there is probably little meaning in there (excluding very common phrases unique to you)

> > > **u/Dzekistan**（1 分）：
> > > But it has access to knowledge in a way. Inside weights of the neural connections.

> **u/minngeilo**（8 分）：
> A swe intern should have the smartness to realize this. Anyone worth a penny in the field knows not to over rely on LLMs, and it should be an aide at best.

> **u/AnalysisFast5007**（2 分）：
> I've found the less experience people have working as professional software engineers, the more certain they are that AI can do all their coding for them. 

> **u/geteum**（1 分）：
> Don't say this on r/singularity people will loose their minds

> **u/idiotnoobx**（-1 分）：
> It’s not just a dumb statistical model… that’s over simplifying  it

> **u/kyo-dev**（4 分）：
> totally agree. I use it for small little things or automation. But honestly, It's way more useful to read documentation or read some stack overflow answer.
> 
> I think AI and LLM are very good until they're not. You have something hard to do and spend more time explaining the issue that working on the solution.

> **u/NightflowerFade**（-1 分）：
> On the other hand, people who call LLMs a "dumb statistical model" tend not to have a good understanding of how the human brain works

> **u/Segfault_21**（1 分）：
> i couldn’t have explained it better. it disgusts me the  people who actually rely on it for EVERYTHING.

> **u/kodaxmax**（1 分）：
> Victim is the right word to. these companies are intentionally advertising it as skynet AI. when it's really just a search engine with procedually generated results based on a database formed from machine elarning.

> **u/catinterpreter**（-1 分）：
> Literally no-one in the world is qualified to comment on the intelligence of ChatGPT. There's no saying one way or another.

> **u/CodeTinkerer**（1 分）：
> It's not that dumb.  I've written code in 20 minutes that would have taken me more than an hour of Googling to look up the syntax.  But because I *can* program, I can see where the errors are.
> 
> For example, in that 20 minute example, I gave TOO many details in what I wanted the LLM to do.  It got "confused" and gave me bad code.  I tried to steer it in the right direction, but it was already on the wrong path.
> 
> Instead, I had to make a simpler request to the LLM (starting from scratch) and gradually add one detail at a time, and iterate the solution to what I actually wanted.  But I knew I had overloaded the LLM and I had to start again to get the answer I wanted.
> 
> Even with course correction, I saved time because I knew what I wanted, but it was in a language I don't use regularly.

**u/stiky21**（11 分）：
GPT is a glorified Google search that is personalized by word tokenization from the prompt you give it. so I don't know what you're trying to say here.

The better you're prompting skills are, the more accurate of an answer you may get. It's no better than using stack overflow and seeing all the terrible ideas people post on there.

AI ooga booga.

FWIW - a lot of colleges and universities are now teaching people how to use GPT (some even have their own custom LLM's like Harvard) and even have courses in programs designated for learning how to use AI.

> **u/Alarming_Ad_9931**（9 分）：
> It's not a fear issue. It's unreliable and it's answers are becoming more prone to hallucination. It's making people dumber, and providing more issues we need to fix.
> 
> If it gave reliable answers it would be a more effective tool for learning. Look at the curve for it's math ability. It's gotten WORSE at math, not better. 
> 
> I stopped using it because for SQL it just gave me bullshit answers.

> > **u/superman0123**（-7 分）：
> > Prompting skill issue

> > > **u/Alarming_Ad_9931**（2 分）：
> > > Reliance on ChatGPT is a skill issue.

> > **u/stiky21**（-2 分）：
> > I don't use it for math mainly because of what you said, it's very silly and I just don't need it thank you my Calculator (form of AI).
> > 
> > It's learned off of already written code, so getting mad at people using AI is just getting mad at the person that originally wrote the code that it is sourcing from. Just like generative art, the reason it sucks with drawing hands is because the majority of people suck at drawing hands.
> > 
> > I found it okay with SQL but a some of the times it's using really old code (SQL Plus vs Oracle) that just weren't relevant to what I was using.

> > > **u/patrickbrianmooney**（1 分）：
> > > > my Calculator (form of AI).
> > > 
> > > A calculator is one of many tools that is not a "form of AI." Hammers, cars, and syringes are also not "forms of AI."
> > > 
> > > > so getting mad at people using AI is just getting mad at the person that originally wrote the code that it is sourcing from
> > > 
> > > No. The problem is that the "AI" recombining code is doing so in a way that doesn't understand the underlying structure of the code, becuase that's how "AI" works.
> > > 
> > > "AI" coding tools have similar problems even when they are trained on carefully curated collections of good code, because "AI" doesn't understand, well, anything, including code structure. "AI" tools like LLMs are statistical predictive text models, not understanding devices.
> > > 
> > > > Just like generative art, the reason it sucks with drawing hands is because the majority of people suck at drawing hands.
> > > 
> > > No. The reason "AI" sucks at drawing hands is because it doesn't understand hand structure. "Ai" has the same problem drawing hands even when it's trained on carefully curated training sets, all of which come from people with good hand-drawing skills. Similarly, the recent "AI" picture that kept getting roasted because the woman in the picture had two torsos and five boobs didn't get created that way because too many samples in the training set were women with two torsos and five boos. It's because "AI" doesn't understand anything, including human body structure and painting techniques.

> > > > **u/stiky21**（0 分）：
> > > > Just say you don't know. It's a lot easier.

> > > > > **u/patrickbrianmooney**（1 分）：
> > > > > I do know.
> > > > > 
> > > > > Take your own advice.

> **u/Quickndry**（3 分）：
> Tbf, he was presenting a case on which chatgpt failed and a Google search didn't. Now it might be because of the prompt of the intern, but overall I agree that googling is a skill people should not replace with chatgpting, but rather complement it. His intern failed to do so, as others are likely to do as well. His criticism has its validity.
> 
> To add my own two cents, the main problem is not chatgpt, it is the user.

> > **u/stiky21**（-1 分）：
> > Loved your last line and I agree wholeheartedly.
> > 
> > And I also agree that Googling is a skill that is fading because of these AI models. 
> > 
> > I can't tell you how many times I've had a new person come in and I say Google and they don't even know how to properly format a Google search to get the correct answers let alone how to filter results and etc.

> **u/Withnogenes**（3 分）：
> Because that's the absolute fantasy of a technocratic government. Technology will solve every problem we have. And while universities are heavily dependent on financial aid, you'll get a ton of scientists trying to secure there income. I'm in Germany and it's a absolute clusterfuck. As if politics get to decide what science should look like.

> **u/NatoBoram**（0 分）：
> > GPT is a glorified Google search
> 
> No, that's Bing Chat, which uses ChatGPT.
> 
> ChatGPT, on its own, is a bullshit generator.

> **u/Nimweegs**（7 分）：
> Juniors and interns don't know if the presented code is shit or good. That's the issue. It's taking away the entire process of designing the code and thinking about pitfalls and edge cases.

> > **u/stiky21**（2 分）：
> > When I was learning Rust in the beginning, GPT was a big help, but it wasn't until I read the Rust Book that I realized it was spitting out "code that works" vs "the right way".
> > 
> > So I fully understand your position on this 👍

**u/EitherIndication7393**（1 分）：
I’m a complete novice so feel free to correct me if I’m wrong, but aren’t there other tools besides ChatGPT that can be used *instead* of ChatGPT?

Also, I know that conducting a quick Google search is helpful too, but I’m working on being very wary of the first things that pop up as a result.

> **u/scoby_cat**（3 分）：
> Stack overflow?

**u/storm_the_castle**（33 分）：
Reliance on LLMs is making people dumber.

> **u/Snoo_4499**（9 分）：
> People said the similar with calculators then computers/Internet then smart phones and autocorrect and now llm. If the person wants to learn nothing stops them, if they don't like to learn then everything will stop them. There is a saying in my language that says "khane mukh lai junga le chekdaina" which translates to "your long mustach will not block the food which you want to eat"

**u/ShrimpFood**（325 分）：
Yeah I’ve been saying this.

Teachers make grade school students learn multiplication and division on paper before you’re allowed to use the calculator so you actually *learn* the fundamentals of what’s going on. 

Yes the calculator is faster but if you don’t know how a graph function actually works, you won’t necessarily know when it’s appropriate to use it

Even if ChatGPT was right 100% of the time it’s still better (and more ecological) to learn how to find the documentation for a for-loop without having to ask it lol

> **u/oldwellprophecy**（61 分）：
> That’s how I think about ChatGPT. It’s a calculator at the end of the day and I find it very helpful for certain things like that but it can’t replace how I get to an idea or finding a new project to work on

> > **u/monsto**（14 分）：
> > I think of it like a person that is sitting right next to you, there to answer your questions. And just like that person, the llm can be wrong, misunderstand the question, give you the wrong context for things, etc. 
> > 
> > And also just like a person sitting next to you, youhave to have a basis of knowledge of wtf you're even doing so that you get a yellow flag when shit doesn't sound right... So then you can ask "where's the docs for that."  
> > 
> >  That will usually clue in the llm when it's wrong.

> > > **u/awkreddit**（5 分）：
> > > It feels like asking the person next to you, which is why everyone is using it. But it's not like that, because that person can actually understand what it's taking about, probably has followed the same courses as you etc. It's a bad tool to ask questions which require knowledge to answer

> > > **u/xenomachina**（13 分）：
> > > >And also just like a person sitting next to you, youhave to have a basis of knowledge of wtf you're even doing so that you get a yellow flag when shit doesn't sound right... So then you can ask "where's the docs for that."
> > > 
> > > The thing that get tricky with LLMs is that while a real person will also give you a wrong answer occasionally, LLMs are experts at giving answers that seem correct. They will pretty much always give an authoritative sounding answer (unless you run into the content controls). With an LLM you can't jut rely on "they sound pretty confident", "that sounds like a reasonable answer", or "they're pretty smart, so they probably know what they're talking about", which are all things we're used to doing when getting answers from people.
> > > 
> > > So using an LLM is fine, as long as you have a way to independently verify the answer it gives you. Always assume there's a significant chance that the answer it gave you only *looks* correct.

> > > > **u/WushuManInJapan**（1 分）：
> > > > But also, if you get a wrong answer and can't do problem solving and troubleshooting, I don't think you'll ever be a decent programmer.

> > > > **u/AntiqueFigure6**（10 分）：
> > > > To some degree you can evaluate how likely an answer from a person is to be correct based on their confidence (I admit not always) but you can never do that with an LLM because it always sounds confident no matter what.

> > > > > **u/sur_yeahhh**（2 分）：
> > > > > This is a VERY good point.

> > > > **u/RealFocus8670**（1 分）：
> > > > As I learn, when I use chat gpt I follow up with at least 3 more sources around the topic presented by chat gpt

> > > > > **u/xenomachina**（1 分）：
> > > > > You'd better verify that those sources actually exist and say the same thing ChatGPT says, because it can and does make up sources.

> > **u/_zenith**（36 分）：
> > A calculator which sometimes gives wrong answers… and not in the way a calculator might, because you formulated what you meant wrongly (forgot a bracket set, for instance) … but just straight up wrong

> > > **u/kodaxmax**（11 分）：
> > > yes it's more like a search engine than a calculator. you need to know how to filter out bad and irelevant results and how best to phrase things  for good answers.

> > > > **u/-ry-an**（4 分）：
> > > > This, it's google on steroids

> **u/rdditfilter**（6 分）：
> I use it all the time. It's a great shortcut when it works, but it doesn't always work, so if you're depending on it completely you're gonna have a bad time. 
> 
> You just gotta be able to recognize that it's fallible, and then have a backup plan ready to "do it the hard way"
> 
> I'm sure OPs intern learned their lesson, hopefully whoever is mentoring them taught them how to properly troubleshoot their solutions.

> **u/WushuManInJapan**（3 分）：
> I will play a little devils advocate and say I sympathize with OPs intern a little. For whatever reason, Google's search algorithm has recently been utter shit for me. I've had to switch to bing god forbid. It rarely shows what I'm looking for unless I specifically am looking for stack overflow or reddit posts. Outside of those, it pretty much never gives me specific results.
> 
> Also, I think chatgpt is really good for giving it a line of code and asking what that line specifically does in great detail.
> 
> But if the intern is asking how to do a for loop, I think they need to learn the basics of coding in a more traditional sense like a book or a course. It's like the first thing you learn after setting variables, and I imagine they have some CS degree program they are currently in and should have taken at least a single programming course before taking the internship.

> > **u/10ioio**（1 分）：
> > I agree with this perspective. 
> > 
> > 
> > They were asking ChatGPT for the syntax of a for loop in a specific language/framework, which is a perfectly reasonable thing to be looking up if you're not sure of the quirks of the language you're using. ChatGPT can do this for most languages, but I think some less common languages it just isn't trained well on. The only time ChatGPT is going to totally mess up the syntax of a for loop is if it's in a language/framework/library it's not well-trained on, which sounds like the case here.
> > 
> > 
> > I think OP forgets that ChatGPT is brand new and everyone is still figuring out what it's good for or not good for in their own career.

> **u/beachandbyte**（1 分）：
> They would just be asking Google for the documentation anyway.

> **u/Teawhymarcsiamwill**（1 分）：
> Fair point though heard calculator used to be a job aswell.

**u/ShopBug**（21 分）：
It's just another tool that one can have various levels of skill in. 

10 years ago, he'd be googling this. And if he wasn't good at using Google, it would be the same outcome. 20 year old code from stack overflow often doesn't work, either.

**u/VisibleSmell3327**（8 分）：
I have my suspicions that a new dev on my team (started in a senior position) is using ai and just copy pasting. His stand up offerings sound scripted, like he just asked chatgpt how to refactor this class and read out all the wordy shite it spits out inbetween code snippets. Then his code seems to ignore all of our house style all the time despite being there 6months+.

> **u/Nimweegs**（0 分）：
> I would wreck that motherfuckers PR

**u/TheHollowJester**（18 分）：
This just reads like "I'll have job security forever".

> **u/StrixLiterata**（6 分）：
> Same. TBH between being late to graduate and my ADHD I'm often insecure about my chances of finding a job, but every time I read something like this  I breathe a sigh of relief knowing that not being reliant on "AI" makes me a better programmer than a big slice of new hires.
> 
> Besides the logic-building aspect, coding on your own, especially on projects, and double especially with teammates, teaches you very quickly some basics of how to keep your code orderly and readable. I wouldn't call mine quite Clean Code, but at least having variables and methods grouped by accessibility and type makes it relatively easy to find what I need.

> > **u/TheHollowJester**（8 分）：
> > I looked up a white paper about mental health issues in SWEs some time ago. I can't find it now, but IIRC something like 8% of the industry has ADHD (vs estimated 2.5% in adults in general population). I was looking mostly at depression and anxiety so I might be misremembering, but I'm pretty sure it was overrepresented.
> > 
> > You'll fit right in :)
> > 
> > Probably the biggest two level-ups that I got were outside of thinking at code:
> > 
> > * I stopped being afraid of asking stupid questions.
> > 
> > * I realized that it's a team sport - and a lot of the team are non-technical people: stakeholders/product people, support, sales people, UX and UI designers etc. etc. 
> > 
> > Basically: if you know what clarifying questions to ask the non-tech people, and how to explain things in a simple way but without losing the core of the subject, you end up being an asset :)

> > > **u/AyakaDahlia**（2 分）：
> > > We're good at hyperfocusing, which is perfect for coding haha. Coding also provides all sorts of new and interesting problems and novel situations to keep our interest.

> > > > **u/Zozi-_-**（2 分）：
> > > > This. And I read about one guy who talked about his ADHD attributed to him not being too afraid of just start problem solving, testing and changing things. Basically the ability to jump straight in, a lot quicker than most “normal people”. 
> > > > 
> > > > For me personally I always keep thinking and philosophizing during breaks and when I’m off work if I’m working on something tough that I haven’t solved yet. Hyperfocus going into overdrive etc. And hopefully I don’t trigger burnout from this. But I love what I do and love digging deeper into weird stuff. 
> > > > 
> > > > 
> > > > I’m a junior dev, and I used to prompt ChatGPT for most “silly” concept-like questions. Light questions were I had a thought and wanted to know best practice stuff. Pros and cons using foreach vs for loops, can this code turn into a one-liner LINQ expression? 
> > > > 
> > > > And other times I just used it in case some unknown built in method was mentioned. Then I could go to the dev docs and read about it. 
> > > > 
> > > > It didn’t take long until ChatGPT was out of the question, and not only because of confidentiality but also due to OOP and the multitude of classes I would need to copy paste for a minuscule chance of getting a decent reply. 
> > > > 
> > > > So less and less prompting now. 
> > > > 
> > > > And I have to mentioned I started working at the same time as another junior who used ChatGPT all the time… and I can already see that the early prompting for answers on his part has hampered his problem solving skills. Most of the tickets we work on are too complex to query and he has kinda started to just sit and wait for the answer to magically appear or something.

> > > > > **u/TheHollowJester**（2 分）：
> > > > > > And hopefully I don’t trigger burnout from this.
> > > > > 
> > > > > Burnout is no joke; I know that people treat it seriously, but in practice it's kinda like if you were into running and torn your achilles tendon. It can fully heal with proper treatment, but it takes time and professional treatment + when you get back you're gonna doubt your skills for some time.
> > > > > 
> > > > > I thought my sabbatical to treat burnout would take a month - it took three (+ therapy, + meds) before I got to the point where I would be productive and could start looking for a job again. 
> > > > > 
> > > > > (This is obv anecdotal and there will be high variance here).
> > > > > 
> > > > > If I may offer some advice, things that would have helped me avoid burnout:
> > > > > 
> > > > > * Be very rigorous about taking your time off (and ideally just go for vacation). It's a necessity like exercise, getting enough sleep, eating nutritious food - maintenance for your body.
> > > > > 
> > > > > * It's ok to do some overtime either if there's a real need for it (emergency, real deadline e.g. to comply with new laws) or if you're doing it "for yourself" (need more money; making up time to finish early on another day; you're just having fun). But: always get paid, and never do it for long stretches of time. Already two weeks will take their toll.
> > > > > 
> > > > > * If you get into the habit of delivering ambitious features/products ahead of the time and everyone - including yourself - is super impressed with how hard you work? This is a warning sign, ponder if you're overdoing it. Imagine what you would think if a friend was working as hard - if you'd be concerned about them, you should be concerned about yourself.
> > > > > 
> > > > > Sorry for rambling, I know you already know this, but sometimes hearing it from someone else helps.

> > > > > > **u/Zozi-_-**（2 分）：
> > > > > > Thank you very much much for your insight and advice. 
> > > > > > 
> > > > > > Considering I’ve only been working as a dev for about 4 months after a 12month trainee/internship I feel like I’m not currently in a danger zone. And my excuse is that I’m genuinely interested and curious. I spent 10 years in a very different field, and 5 of those I wanted to get into software and programming. So when I’m finally doing it I am over the moon! 
> > > > > > 
> > > > > > Every task is fun, and I enjoy digging into 10year old code, debugging and tweaking stuff to both learn and solve things. 
> > > > > > 
> > > > > > I just happen to lose track of time and coffee breaks have gone past me. I’m so focused that I more often than not realize that I’m past a full day and sometimes I only leave work when my family messages me about when I’m coming home. 
> > > > > > 
> > > > > > And most days my mind is completely fried when I leave. So I think your comment is very important for me to know about. Maybe use a pomodoro timer and force myself to get these small but massively helpful breaks. 
> > > > > > 
> > > > > > Burnout is probably something that creeps up and hits like a truck when it shows up?

> **u/Nice2Inch**（13 分）：
> Just to clarify, I'm not anti AI. My issue is that people are entering the software engineering workforce rely completely on AI and didn't even try to use google. If my intern had done an additional google search (1st result is stackoverflow and 2nd result is the official documentation which both provide the answer) I wouldn't have made this post.

> > **u/hoppity51**（1 分）：
> > It does mostly sound like y'all just picked a bad intern though

> > **u/AyakaDahlia**（1 分）：
> > Personally, Google is the first thing I turn to. ChatGPT is somewhere down the list.

> > **u/Aaod**（8 分）：
> > How the hell can people like this find jobs and I can't? Compared to these people I am some coding genius.

> **u/Graphacil**（0 分）：
> the copium is intense in most programming subs, just like the art subs

> > **u/TheHollowJester**（-2 分）：
> > If you say so champ. You're extremely articulate and definitely not terminally online so I should take you seriously :V

**u/AHardCockToSuck**（1 分）：
Yet

> **u/ObeseBumblebee**（1 分）：
> I don't think it will ever get much better. Not without new technology. LLMs will always have the weakness of bad information polluting their model and giving bad or broken answers. It's a great tool and I disagree with OP that it can't be a tool for learning. But it will always come with the caveat that there is a significant chance it is confidently wrong.

> > **u/AHardCockToSuck**（1 分）：
> > Just wait until the singularity

> > > **u/ObeseBumblebee**（1 分）：
> > > Probably will be waiting a long ass time

**u/ballbeamboy2**（107 分）：
As a Junior dev. If you have a good problem solving skills, you can ask ChatGPT to write code for you since you already know how to solve them but you dont know/forget the syntax or some methods in that languages.

However sometimes ChatGPT gives bullshit answers, if it does , then I have to rely on googling, read the docs , and so on ..

> **u/ddproxy**（63 分）：
> As a Sr Dev, I ask ChatGPT to generate boilerplate functions, switches based on lists, very basic algorithms as starting points, generate doc-blocks, reduce the complexity of something that should have been simple in the first place. But syntax, best practices, math or performant code - I've generally been deep in the docs or experimenting/code-diving. There is opportunity with LLMs to help with those aspects if trained properly or given the context but it's definitely not there yet or 'safe' to pass that much IP context, nor efficient to take in such a large context.

> > **u/CodyTheLearner**（6 分）：
> > This is similar to my workflow. If I find I’m stuck integrating an idea I extract the boilerplate for what I wanna do and manually integrate the logic. I’ve even copy and paste specific pages or portions of documentation in tandem with my code and discuss improvements alternative approaches etc.

> > **u/Won-Ton-Wonton**（14 分）：
> > As a dev (no work experience, but I don't think I'm Jr. enough to say Jr. anymore), I really only use ChatGPT for 3 things on the regular: prototype, dummy data, and copypasta type work.
> > 
> > For copypasta, if I realize a whole bunch of things should be in `<li>` tags, I might copypasta every item and tell it to put it all in that with `ml-6 px-4 shadow rounded etc` (yes I know I can use `[&>*]` instead—not the point) and work on something else as it chugs along. Coming back to it when I'm done on the other stuff.
> > 
> > As for prototyping... do I need a pagination component? Great, gimme some code ChatGPT. I'm gonna replace probably 90+% of it anyways, but I need to see how it looks with 10 items on the page versus 20 items and don't care if it looks pretty right now. I might not even want pagination, maybe I actually want all items. It's a prototype.
> > 
> > Finally dummy data is truly where I use it the most. Gimme 20 items following X schema. Glorious. Absolute treasure. **Gimme an about us page for X company so that I don't need lorem ipsum for the thousandth time.** It's a game-changer. This is truly what LLMs exist for. Making up the crap public relations would normally argue over for 6 weeks (/s), but I get to style it up off rip looking something similar to what they're going to write anyways.

> > > **u/ILovePitha**（1 分）：
> > > I feel the same.

> > **u/ThePoliticalPenguin**（1 分）：
> > I often hear this, and I wonder what version of GPT the person is actually using. I've had similar experiences with 3.5 and 4o, but regular 4 (paid) has been far more consistent.

> > **u/Zerocrossing**（5 分）：
> > This very accurately mirrors my own feelings about LLMs. They're great at automating some tedious tasks, but if you aren't skilled yourself, over-reliance on them will produce some of the worst code you've ever seen, and in some cases will cost you more time than you would have spent had you gone for a more traditional google route.

> > **u/beagle204**（0 分）：
> > I have \~15 years full stack experience. ChatGPT 4o is actually a really great tool at some stuff. It's great for Regex, xpath, taking code from language A to language B, generating unit tests. there's a host of things it's pretty great for. A lot of stuff I would give to a junior i can just feed to gpt and good a good-enough result. 
> > 
> > I think for me personally. I don't know if i've ever copy/pasted something directly from gpt without going over it and changing it. It's awful at naming variables imo for example, or coupling logic into single functions. It has a tendency i guess in my opinion to do too much. But like, the jist of it is there.
> > 
> >   
> > Honestly, I actually hate the rhetoric around LLMs, oh LLMs are just stats, or LLMs are just guessing what you want. It's verifiably false and damagingly reductive. I don't think juniors should be avoiding gpt either. Would you tell a junior dev to code everything in notepad because the IDE does too much. Or maybe dont use this extension because it's too helpful? Never. It's "Use this extension because it helps you here", "This keyboard shortcut will make you faster when doing this", and "This IDE is great for this language". GPT has to be a part of the conversation otherwise i think THEN you get into the place where juniors over-rely on it. People need to understand it's a powerful tool and how to use it. I think it's up to the senior guys on the team to convey that message.

> > **u/10ioio**（1 分）：
> > If you pay for GPT you can "create a custom GPT" upload all your docs as a "knowlege base" and it uses retrieval augmented generation to based on the document you give it. Results in way more accurate answers.

> **u/BobbyTables829**（19 分）：
> I did this and it's not so good.  Typing things out on your own is just not the same as copy pasting.  You are much more likely to remember it again if you type it up yourself.
> 
> It took me two years of employment to figure this out

> > **u/_PacificRimjob_**（12 分）：
> > Depends on the syntax. Year later, I still never remember the order for cronjobs. I used to always go to a site for it then type it, now I paste my bash script to GPT and say "put this to run every 2nd at 0200" or something. That and regex I can never remember.

> **u/ghosts_dungeon**（1 分）：
> As someone with bad ADHD and somewhat dyslexic, I sometimes get an error compiling a single line and can't figure it out. It's usually a symbol is backwards or something but my brain keeps autocorrecting it when I see it so I never notice. These are when I just paste that random line and ask, what's wrong with this line. Most of the time it has no idea what I'm even attempting to do but it picks up on my typos.

**u/Individual-Praline20**（3 分）：
Posting proprietary code to ChatGPT is like posting it to a public website, open to everyone. No difference. If you don’t understand that, you don’t belong in development. 🤷 I would definitely trade all these shitty  AI tools with similar websites than StackOverflow. Because they are usually built from actual experience and expertise, not from words matching statistics… Of course you need to take everything from the web with a grain of salt, but AI tools are much less useful, the chance to get a correct answer is much much lower.

> **u/ResilientBiscuit**（6 分）：
> No, it's not, you can explicitly tell it to not save the history and to have it not used for training purposes.

> > **u/_zenith**（2 分）：
> > Has this been verified by a third party? Or is it “trust me bro”

> > > **u/ResilientBiscuit**（2 分）：
> > > It is in their EULA.
> > > 
> > > 
> > > Unlike posting to a public website where there is no liability and no one responsible, OpenAI is a valuable company with a lot of revenue. They are actually liable for not living up to their conditions.
> > > 
> > > 
> > > Any time you give you data to someone there is some risk, but a lot of companies use cloud services for various aspects of their business.
> > > 
> > > 
> > > Doing it when the contract says they can't use your data is worlds different than posting it to a public website.

> **u/Won-Ton-Wonton**（0 分）：
> Well, there actually is a difference. And if you don't understand that you don't belong in security.
> 
> ChatGPT has 2 versions: the public facing and the enterprise facing.
> 
> If you have the enterprise-facing and ChatGPT uses your data to train it, or otherwise publicly exposes it, you get to have the wonderful experience of suing them into the ground. Just as if GitHub publicly exposed your private repo you pay money to keep private.
> 
> If you don't have the enterprise-facing... your company is stupid as hell. Skill issues on security's part.
> 
> If the risk of the enterprise-facing is too great, then you security team is either overly protective or your technology is serious business, potentially worth more than OpenAI to begin with, and really shouldn't be exposed even to external enterprise software.
> 
> As for the chances of ChatGPT being right versus StackOverflow... eh. It's about the same, honestly. Which makes sense, given ChatGPT was trained on all the data of StackOverflow. The difference is I need to pray a mod doesn't say, "This is answered 7 years ago", when it clearly was not.

**u/random_troublemaker**（65 分）：
While LLM usage in this case has regulatory implications due to fintech, I think the actual core skill issue here is approach flexibility.


There was a lockpicking Youtuber called BosnianBill who worked in situations like police searches, and one of the things he taught is that it's crucial to keep changing your approach when it starts to fail. Locked door, try a latch slip. Nothing, bust out the lockpick gun. If that doesn't work, start raking. If that fails, probe the individual pins. Still nothing, bounce your tool with bitch picking.


Your Intern tried the first thing that came to their mind, saw it fail, and went to the next tool they knew of, to reach out to a coworker for help. They avoided the worst-case of getting stuck and spinning his wheels. I think they may still develop to be a good coder if you can encourage them to develop their research skills- there was a time when Google Fu wasn't a universal skill, that time seems to have returned, and teaching them to not rely on just their first hammer will help fill that critical problem solving toolkit for the future and become a valuable worker.

> **u/_PacificRimjob_**（25 分）：
> Yea, everyone demonizes GPT and much of it is warranted because the marketing causes a lot of situations like OP sees where people only use GPT, and yet everyone uses IDEs with built in bug-checkers that were demonized 10 yrs ago. New tools always come with new teething problems. What separates good and bad workers is if people take time to learn what the new tool does well and to be aware of the limitations. It's no different than all the oldtimers who act like new workers with powertools don't know "how to really work" because they built everything with a chisel.

> **u/Won-Ton-Wonton**（10 分）：
> 100% this right here.
> 
> Their mentor has a skill issue and that skill is being a mentor.
> 
> Your job isn't to bitch about your trainee's inability to Google Fu. Your job is to bitch when your trainee refuses to Google Fu after you show them your Google Fu mastery.
> 
> Their trainee clearly has no Google Fu. They have ChatGPT Karate and it failed them. They went to their wise master, and their master failed to teach them the art of Google Fu. They will now be stuck with ChatGPT Karate.

> **u/tutoredstatue95**（11 分）：
> Google skills and LLM skills aren't that different.
> 
> Prompting google to spit out the stackoverflow result is pretty comparable to prompting ChatGPT to produce the answer. Knowing if the answer is correct, how to adapt the answer to your needs, and actually using the correct prompts are all shared skills. I agree that it's not an immediate red flag if the intern was asking for help, it would have been a good time to simply ask: "what else did you try?" 
> 
> If the work wasn't time sensitive, which it shouldn't be for an intern, it was an excellent opportunity to teach them to fish.

> > **u/Inetro**（0 分）：
> > Keyword searching on a search engine for metadata tagged posts is not anywhere near the generative AI approach of prompting a LLM. You can pretty quickly tell if a SO post is worth looking at based on rating and amount of discussion around it. There is no human validation to the generated code an LLM is giving you. The human validation of a highly rated post with updates for various language version updates is so much more valuable to me than a "this is probably what you're looking for" generated code block that I have to dissect.

> > **u/Clueless_Otter**（1 分）：
> > I think a major difference, though, is that Stackoverflow is usually going to have multiple answers and will have multiple real people in the comments discussing each answer, its relative merits, if it works but should be avoided, if there's a strictly better way to do it, etc. Meanwhile an LLM is just going to give you one answer and that's it, unless you try to wring out, "Are there any other ways to do it?" or whatever out of it, but the more wringing you do the more likely you are to get a total BS answer.

> **u/Alive-Bid9086**（-1 分）：
> Ehh - The intern had only one year left of college. 
> 
> I am really oldschool. We had the documentation on paper in binders when I started to work. There were no search indexes, Alta-Vista was a great search engine when it arrived.
> We had to read the manuals and understand them.
> 
> Today, google helps you with both examples, tutorials and manuals.
> 
> If the person was interested in programming, he would have known how to lookup with google. A person witgout interest will not make a good job.

> **u/RadiantShadow**（9 分）：
> While I agree on the importance of approach flexibility, a CS student who is about to graduate should have more problem solving tools in their proverbial toolbox than "ask AI" or "ask a co-worker". Those are handy tools, but they are both tools that do not require them to understand the problem themselves. I think OP is right to not recommend such an intern for employment in their current state, because at that stage in their studies, the student shouldn't need a company to teach them the importance of "try at least two things before giving up and asking someone else who may be busy with their own tasks".

> **u/teerre**（1 分）：
> There's no way the "second best solution" is waste someone's time when, in OP's own words, the first google result already answered the question. It's very likely OP's junior learned nothing from this exchange. You can't just keep searching for quick answers. You need to do the work yourself. That's how you learn.

**u/Ok-Switch-1167**（1 分）：
I couldn't agree more. I started learning about a year ago and relied on chat gpt to start with. I'm now facing the consequences of this a year later. It's not the syntax I struggle with, it's writing algorithms. So I basically had to start again months later. 

Chat GPT looks like a great tool for learning, but it's actually the opposite later on down the road. I still find myself thinking about asking chatGPT for help the first instance something doesn't work first time. But the problem is, when people do this, they aren't learning the actual skill you need when developing, which is **problem solving**

I would rather struggle for hours or days trying to fix something than get chatGPT to give me answer.

> **u/thisdude415**（2 分）：
> There's also a question of whether you're trying to build something or trying to learn programming. 
> 
> It's like any other tool. 
> 
> To use an analogy...
> 
> If you want to get stronger at lifting up rocks, don't use a wheelbarrow. 
> 
> But if you need to move a lot of rocks ASAP, you should use a tool, rather than going to the gym. You go to the gym today so that you can move rocks more quickly tomorrow. And the additional strength will also make it easier and faster to use tools.

> > **u/Ok-Switch-1167**（1 分）：
> > That's an important point to make. I program as part of my job, but I'm also not employed as a software dev, I work as a scientist. So I'm in a good position where I'm not necessarily rushed to fix bugs or push out software week after week.

**u/ObeseBumblebee**（31 分）：
Chat GPT is a fine learning tool if you recognize that it's often wrong and double check and understand every line of code it writes and expect it to be wrong. It's great at pointing you in the right direction and keeping you moving forward. But it shouldn't be the only tool you use.

I think you're being a little harsh on the intern though. They're learning and making mistakes. That's their job as an intern. Most interns suck at debugging. It's a learned skill that can take years of experience to master. It's your job as his senior to get him up to speed on what tools are reliable.

> **u/Nice2Inch**（1 分）：
> I know I'm the one who is supposed to mentor the intern and help them learn, but they had just finished their 3rd year of a CS degree. Yes, I have more experience than the intern, but for a syntax issue they should have checked in more places than just ChatGPT. Although I didn't mention it in the original post, at the start of this project, we gave the intern links to the official documentation of the framework. So they had reference material, but simply chose to ignore it and use ChatGPT only.

> > **u/AyakaDahlia**（2 分）：
> > Man, I love official documentation lol! It can be dense and difficult to read through, but it's usually not that hard to find what you're looking for. And if you don't quite understand it, now you have much more precise search terms for Google or to write a prompt for chatGPT.
> > 
> > edit: And a lot of the time I'll come across stuff that I don't necessarily need but looks interesting. Sometimes I'll be working on something else and then I'll suddenly remember wait, I think there's a thing for this!

> > **u/Graphacil**（-2 分）：
> > This is clearly a skill issue, whether on your part or your intern's and not a chatGPT issue. What a dumb post.

> > > **u/Nice2Inch**（1 分）：
> > > Oh for sure it's a skill issue. The problem is that a 3rd year CS student, that is in an internship to get a job, attempted to debug their issue with only ChatGPT. This intern is supposed to be one of the best out of 100s of applicants. It just seems like too many people today are using ChatGPT/LLMs to do the critical thinking for them.

**u/Lyesh**（6 分）：
Honestly Google is usually worse than just RTFM, esp these days. Reading docs is a bit of a skill, but well worth developing. There are also proprietary environments that have little to no documentation online

**u/EfficientMongoose780**（2 分）：
Yeah I really want to get rid of this habit recently I just asked for the first time on stack overflow and I got to learn something from there  as well I really want to stop using gpt as my go to tool if my code doesnt work

**u/MrFavorable**（1 分）：
The temptation of asking ChatGPT for answers is so high and requires little effort. It makes me wonder how these people would survive when I was a kid and services like ChaCha were huge because not all kids had smartphones in the 2010’s. Good was my primary method to learn something and all it required was a little digging around.

> **u/CodyTheLearner**（-2 分）：
> I think part of it is ease of accessibility. 
> 
> Old tech heads grew up manually doing so much of what is automated, the sneaker net, for example manually transferring a DLL’s guts from a working machine to get the application working on a new desktop. If you wanted something, you usually had to work for it. This problem just turned away folks who didn’t care that much. 
> 
> A lot of the younger people are in a different situation. Old heads grew up in using the equivalent of chisels and hand saws to build some amazing stuff. AI is the CNC power tool equivalent. I can’t be upset they aren’t good at using hand tools if they never had a reason to get a deep education. A lot of these folks are the same ones who wouldn’t have engaged at all 20 years ago. 
> 
> It’s about their perspective for me. Totally different Operating system and knowledge level from me.

> > **u/awkreddit**（1 分）：
> > Come on. ChatGPT is not old enough to talk about generational gap.

**u/Draegan88**（1 分）：
I find it hard to believe it got a for loop wrong. I use it to learn new syntax all the time and it’s quite good at it. I just test everything to make sure it’s right. Works like a charm. 

**u/BobbyTables829**（23 分）：
Man I use it to clarify documentation all the time. 

"Do I need to use a for loop to reverse a string using c#?, or is there a built in function?"

Asking it things like that saves so much time, and you can remember what it tells you for the future.  It's just faster than googling, and faster at finding built in functions you may be forgetting or missing out on.

It's fine if you see it at a tool for learning and not as an instructor.

> **u/No_Lemon_3116**（9 分）：
> I don't know that it really saves time. Like, I just googled `c# reverse string` and the top result is SO with the answer. I think it takes the same time as asking a bot, but with the difference that if there's a wrong answer, there's also comments on it, as well as other suggestions. Bot responses come with no feedback and they often don't offer alternatives.
> 
> I can appreciate that some people just like the conversation model more, and it might be easier to use with followup questions because it can remember context for you which can simplify your queries.
> 
> I work with LLM's from several different services that help with coding-related tasks and some are better than others, but they get so much wrong that I would never use them personally (I can understand why some people might, though). Top Google results and SO answers are often wrong, too, so I don't think this is so much of a new problem as some people seem to, but I do feel like those services fare much better when the top answers are wrong, whereas LLM's are likely to waste more of your time if they don't initially get it right.

> **u/TomWithTime**（2 分）：
> Using it to actually learn is fine. The title calls itself click bait for a reason. What's bad is trying to leverage its current capabilities to do the work for you. That's how you make sure you don't learn and produce bad code 
> 
> >not as an instructor
> 
> It could probably play this role better than people trying to use it to do the work for them lol
> 
> >Asking it things like that saves so much time,
> 
> Just make sure it's not lying. I used Google's ai (Gemini) to ask it a super basic question about Google's language (golang) and it gave me the wrong answer! Like guessing wrong on a yes or no question about whether the language had a certain feature

**u/abbh62**（9 分）：
No difference in when you likely learned and took the first solution from SO.  The more alarming part is not trying to keep figuring it out themselves, or doing more research

**u/jumpmanzero**（1 分）：
>I would not recommend hiring just because of their reliance on ChatGPT and poor debugging skills (which include googling).

I mean, yeah... they should be able to Google.  Clearly.  But at this point in history, they should also probably be able to ChatGPT a bit. I've been doing some retro-programming (for NES), which is mostly new to me - and ChatGPT has been the fastest path sometimes.  Or, obviously, sometimes I google, or even (shudder!) read proper documentation.

Anyway, I find this overall take hilarious.  It's not long ago that people would have written the same post about programmers who rely on Google (or StackOverflow, or Usenet) for everything.  An intern who didn't try Googling first is a bit bizarre, but it's not like bad interns are a phenomenon that just came along with AI.

**u/dopecleric**（14 分）：
Yeah don’t fall into the trap of having it write code for you. My approach has been to ask it what it thinks about code that I’ve written and see how it thinks I can improve it, or make it cleaner. It is often helpful when used as a tool for improvement rather than a crutch to do your work for you.

> **u/Snoo_4499**（4 分）：
> Yes, its good at debugging

**u/Maleficent_Fudge3124**（12 分）：
I want to see the research on this stuff before i decide one way or another. 

I don’t think abacuses 

Or calculators

Or computers 

Or smartphones

made humans dumber

Learning and understanding tools is one of reasons humans are so smart

… but we have to learn and understand the correct way to learn with tools to be smarter. 

Educators in institutional learning *love* to say these things… but they don’t want to learn to use the new tools because it threatens their jobs or would force them to change the way they teach. 

That’s why institutional education is often so far behind industry. Or spends time teaching theory so students are forced to learn on the job or train themselves in practical skills afterwards. 

Swapping from punch cards to IDEs has not made computer programmers dumber. 

As we make better tools and learn to use them, we fet vastly more productive. When the next generation learns to learn with generative AI (and its limitations) they will step up how smart/productive they are. 

We just have to be the ones to teach them how to use them carefully.

> **u/b00tymagik**（1 分）：
> Necro, but who tf cares.
> 
> This is the most salient answer on this sub imo. 
> 
> quick anecdote:  
> I made beats for 10+ years and originally wanted to create \*everything\* from scratch, the synths, drums, everything. And looked down on ppl who used too many 'premade' sounds as 'less than'. Fast forward 10 years, and those ppl i thought of as 'lesser artists' were running laps around me and made some of my favorite songs.
> 
> Now older and wiser, anytime I want to do something, I say fk all the 'shoulds'. Get ur shit done and completed with every tool available. Bring ur ideas to life however you choose.   
>   
> B/c at the end of the day no one cares how 'clean' an app was made, or how long someone spent sketching and underpainting on a canvas, or how many hours you spent crafting a synth. They only care about the result and I only cared about doing something the 'right' way or the 'real' way bc I placed too much of my self worth into those labels and was able to rest on my laurels and turn my nose up at everyone taking 'shortcuts'.
> 
> For me, topics that relate in this way, were all about swallowing my pride; and realizing all the ideas of 'proper art' were just stories I told myself.
> 
> So now, if I want to paint a large mural outside for everyone to see, who tf cares if i used ai to gen the image, and a projector to project the stencil. Literally no one cares, especially if it looks nice and I get to the fun part of painting faster.   
>   
> Especially, as these thoughts pertain to this \*\*\*rapidly\*\*\* changing world. Thoughts of the 'proper methods' in \*most\* scenarios is only hampering actualization of \*your\* goals and ideas.

**u/Miginyon**（1 分）：
I agree on how rubbish chatGPT is, learned that the hard way trying to get it to teach my new stuff. And I was lazy with it. Got nowhere. Found copilot was making me dumber. Got rid of it all.


That being said I wouldn’t write this guy off yet.

I’d ask him if he’s working on any side projects at home on the weekend.

If the answer is no, then yeah, not employable, his heart isn’t in it.

If the answer is yes then I’d suggest to him that he build an entire project just using chatGPT. 

The only way to know how bad it is is to let it take you as far as it can. When it can take you no further and you realise it’s a just down to you. Then you fall apart cos you have zero idea what is going on, and you realise that this isn’t sustainable.

**u/derpado514**（0 分）：
I'm using Microsoft co-pilot for a learning project and it's honestly a pain in the ass more than half the time.

I noticed it regurgitates stuff from web pages I'm actively looking at..basically top 3 google search results based on my prompt....

How long before companies forget about this trend and move on? This just the blockchain phase all over again, but more annoying...

**u/aRandomFox-II**（49 分）：
So... did you tell your intern all this? If you don't give them feedback they'll never learn what they did wrong.

> **u/GabbarSinghPK**（16 分）：
> Thanks for this comment. I am looking for at least 1 comment like this.
> 
>  That's the most important thing a mentor has to do to the intern. They take time to understand the industry and unlearn their old practices. It's the OP's duty as a mentor.

> > **u/Agitated-Soft7434**（9 分）：
> > The post was edited and they said they did explain to the intern afterwards why its not a good idea/bad practice.

> **u/falling-faintly**（1 分）：
> Does anyone really need to be told that there are other solutions out there? To look at google or the documentation? I feel that should not have to be told to anyone in a paid position. GPT is brand new. It’s not like documentation or google is some long lost ancient aliens technology.

> > **u/aRandomFox-II**（0 分）：
> > https://xkcd.com/1053

**u/Potche**（0 分）：
I find it invaluable for researching in cybersecurity studies. For instance, I don't have to comb through any search results or webpages for learning about static vs. dynamic analysis or SDLC or any terms for that matter. I've also used it to break down Linux commands and fundamentals so I can peice it together on my own to get a complete understanding

**u/PsCustomObject**（3 分）：
I am rather seasoned (45yo) so while not using it to teach myself fundamentals I have noticed it made me way lazier than I should be.

Just this morning I was writing some stored procedures and I ended up using Gemini, ChatGPT is blocked for me, until I realized how much time I wasted ‘fixing’ poor written code, in the same amount of time I would have finished my tasks for he day :)

Apart from my personal experience I completely agree, people are relying way too much on the tool.

I mean yes it is nice and I find myself using it in place of google for looking up something, programming unrelated usually, but people specially in IT are using it as a substitute for proper ‘training’ (in whatever form).

**u/StrixLiterata**（9 分）：
A friend of mine tried to pass a coding exam at Uni with Copilot and got caught in the act.

I offered many times to teach him C++ and mentor him for the exam, but he insisted to go for the "easy" road.

RIP

> **u/Nimweegs**（3 分）：
> Good riddance

**u/HunterIV4**（2 分）：
>His first and only idea was to ask ChatGPT how to write a for loop in said framework.

The issue here isn't that he used ChatGPT, the issue is that it was his *only* idea. Using an LLM as a first point of discovery isn't necessarily a bad thing; I've been programming for 20 years and I use it.

If the answer is wrong or doesn't work, I then Google it or check the docs. I'm sorry, but if you are a professional and being paid by a company, you need to use whatever tool is most efficient because they are paying you for your time. If ChatGPT gives you the answer in 10 seconds, and Google takes 10 minutes, you are wasting your company's money and being less efficient.

ChatGPT isn't wrong often enough to make at least an initial check useless.

>My issue is that people who are learning or trying to get junior/entry level software engineering positions are relying on a service that gives wrong answers and take it as fact.

I mean, you'd have the exact same issue with Stack Overflow or Reddit. Sifting through BS is a core internet skill. Again, the problem is with *how* the tool is being used (blind trust), not the fact that the tool is being used at all.

>Had my intern attempted to google first, my opinion would be a bit more positive.

Why? What if ChatGPT happened to have the relevant information in the training data but the first few Google results were a bunch of BS that took a long time to sift through? I've been using ChatGPT for months and it's *way* more reliable for general programming questions than Google by far.

>On a side note, in my industry (fintech), if you copy paste code into ChatGPT to debug, you will be fired. It may be more relaxed for other fields, but other should be aware that exposing proprietary code to outside parties/applications is a huge security risk.

Sure, but it's not like there aren't solutions to this. You could locally host Llama 3 and get results close to the same quality as ChatGPT without ever exposing your code to external sources.

I'm not saying you *should* do this, but LLM's aren't going away and this sort of thing is going to be as common as Google within the next few years.

Also, even in fintech, most of your code isn't directly relevant to security. If someone can crack your system because you exposed some database CRUD code to OpenAI, you have more serious security problems than posting code to ChatGPT. There is secure open-source software, and the idea that general code exposure would create security vulnerabilities is a huge red flag indicating that the codebase already isn't secure.

Source obfuscation is one of the least reliable methods of security. If reading your source code allows people to access your systems, you already have a security failure. There are exceptions, of course, like token generation algorithms or any built-in tokens, but no company in the financial sector should rely on hidden source code for data security.

I work for a market research company. I'd probably be fired if someone reading any of my source code could expose customer data or gain unauthorized access to our systems.

I had to do some research because I couldn't believe this sort of thing was standard in fintech. But it appears to be as exposed source could expose security vulnerabilities. That's absolutely terrifying to me, but at the same time, it's probably cheaper to hide vulnerable code than actually spend the time to write secure code in the first place.

**u/the_p0wner**（1 分）：
We'll, he's dumb, interview the next in line and move on, no?

**u/ArthurKasparian**（2 分）：
I've had decent success learning new concepts and having it explain things in simpler terms, but I would not trust it with any coding or actual work.

**u/Won-Ton-Wonton**（2 分）：
>His first and only idea was to ask ChatGPT

Skill issues. Something you should expect from a 3rd year CS student. They probably don't even realize they're overly reliant on it... much like 3rd years were overly reliant on StackOverflow pre-AI days.

>Had my intern attempted to google first, my opinion would be a bit more positive.

Yes, obviously. Also, sounds like they're not 'your' intern. Maybe pedantic, but you didn't hire them as an intern.

It is more accurate to say you're 'their mentor'. It honestly reflects poorly on you as a mentor if you're not directly telling them to stop using ChatGPT. Think if you were the manager discussing hiring them and your subordinate said, "Well, they overly rely on ChatGPT." If you as manager asked yourself, "Did you show them how to look up docs and encourage them to do that instead?" What would your response be?

If it isn't, "Yes, I showed them the docs and they still used ChatGPT." Well... that's a skill issue on your part.

This intern has spent the last 3 years in learning mode. Learning is probably the last thing they want to be doing (even though it's the right thing to do). It's understandable that they're trying to find a way out of the situation.

It's your job as a mentor to help them understand they have no other choice. It's their job as an intern to accept and assimilate your advice.

**u/Kalex8876**（1 分）：
Well if chat gpt gave a wrong code, wouldn’t one know by running it? If it’s wrong, you can ask chat gpt again again and if it’s just printing the same nonsense. Google and probably see it on stack overflow? I think the bigger issue with your internet is not looking at other resources rather than using chat gpt to code

**u/Amrootsooklee**（5 分）：
Teach them how to read documentation.

**u/DogOfTheBone**（1 分）：
It's a great tool when you already know how to code and want a little buddy to speed your workflow up.


Otherwise...yeah, oof.

**u/TheWobling**（2 分）：
I’d like to think you tried to educate him on what you explained here.

**u/jexxie3**（2 分）：
I mean… the same could be said for stack overflow. At least they tried SOMETHING before finding you. It sounds like a pretty easy learning experience. “Hey next time try googling this before reaching out to me.” If they don’t follow that instruction, then there’s a problem.

**u/AnotherNamelessFella**（0 分）：
Well chatgpt can write programs and solve a good number of problems.

I believe everybody has used it, and can attest for themselves. What works for them and what doesn't.

I find that you need to use chatgpt like a small child who is helping a carpenter (you're the carpenter and chatgpt is the small child). You break down the tasks into smaller tasks for it, and then know how to reassemble everything into one.

If you feed it huge tasks or implementations, then that will be too much for it, and the code will have a lot of errors. And this is the issue most people have

**u/MundaneValuable7**（1 分）：
Yeah, I have no idea what these people who say they use it for everything are doing.  Anytime I ask it something even remotely complex it lies and I end up wasting more time than if I had just used Google.

**u/thisdude415**（1 分）：
It sounds like the problem is your intern not knowing how to RTFM, not that ChatGPT is not a good tool for learning. I bet if you had copied and pasted that page of the docs into ChatGPT, that it would have easily solved the issue. 

I've built some pretty incredible things over the last couple years, and ChatGPT (and Claude) has been an incredible resource. I had never had success getting anything beyond some MATLAB and Arduino C++ in grad school, but with ChatGPT, I feel like I can tackle almost anything.

Do they get things wrong? Absolutely. But they get things right pretty often, and they are a great sounding board, as long as you know to check the actual documentation for whatever you're working with.

Since ChatGPT's release, I've built Python backends on AWS Lambda, websites, Wordpress plugins, a native iPhone / iPad / macOS app, and even made a beautiful new macOS app just this week (granted, not very big--maybe 800 LOC for the macApp, and another 150 for the backend).

But the thing is, people still need to do what people do best -- using common sense, stepping back and asking what's the best way to approach this, and recognizing that LLMs are great at language: namely, they are great at translating between English and code, and between languages. But they are actually quite bad at logic unless they have ingested similar logic before.

**u/AnonPogrammer**（1 分）：
How did your company hire an intern that's this bad?

**u/dalcowboiz**（1 分）：
Realistically long term the models will improve and your junior's method will work more often

**u/BringAmberlampsXD**（4 分）：
Funny enough, I'm a junior QA and asked ChatGPT for a solution to read the contents of a CSV in Cypress earlier this week. I tend not to bother because it often seems inaccurate, but thought I'd give it a go.

The solution it offered apparently won't work at all, and Cypress has a method for reading the file already. I remain skeptical of LLMs.

**u/KarimMaged**（0 分）：
I think ChatGPT is an excellent tool as long as you understand what it is capable of and what it isn't. 

It gives many wrong answers, especially when the question isn't right. If one always take its answers critically then it is useful. but if you take its answers as if it is bible then that is a problem.

**u/Ok_Pineapple_388**（1 分）：
I think the biggest problem is not using it for learning, it's using it to think for you. I use it exclusively to have somebody to go back and forth with until i understand a concept from top to bottom, and don't allow it to give me answers in code, or to give me anything i don't already have. I just ask it if my understanding is correct

**u/jamesbond69691**（1 分）：
This is why I don't currently use AI for coding assistance. Not because I think it is dogshit and will hallucinate me answers (it did, but that is not the point), but because I still have things to learn and commit to memory.

**u/JuneFernan**（24 分）：
A post by someone a generation older than you:


"Google is not a good tool for learning"

> **u/Metabodiru**（-4 分）：
> I think most of the posts from people talking about how bad ChatGPT is at helping someone learn coding are from those who do not have a paid ChatGPT subscription.

> > **u/dopadelic**（3 分）：
> > This, although the free version has access to GPT-4o now.
> > I'm a software engineer and was surprised that none of my colleagues tried the subscription and they all had varying amounts of disdain for it.

> > > **u/Small_Pay_9114**（0 分）：
> > > I’m not a software engineer, but have a quantifiable experience with databases, data science  and python. The OPs post kinda pisses me off Will ChatGPT get you 100% of the way?  No. But it’s pretty funny watching all the software engineers (I know in real life as well) not use ChatGPT literally because of their ego. You can build highly complicated mvps quickly now with ChatGPT. Drop the ego. Tech is just a tool to build more tools, and I see that to many developers place to much value on the tool itself instead of the outcome.

> **u/awkreddit**（-4 分）：
> That parallel is wrong and you don't understand.

> > **u/JuneFernan**（0 分）：
> > Yes I do.

**u/HumorHoot**（1 分）：
it does make mistakes quite often

i mostly use it to fix syntax (or remind me of how the syntax is) when jumping between coding languages

also for figuring out what packages can do what. i often have no idea what to look for, so i just ask it, then i got the name, and i can google it and figure out if its what works for me - usually it is.

**u/hotboii96**（1 分）：
Honestly, if you can't write a for loop as a student or intern, you don't have anything with the job to do.

**u/NatoBoram**（1 分）：
> On a side note, in my industry (fintech), if you copy paste code into ChatGPT to debug, you will be fired. 

It's important to note that this is *very* job-specific.

For example, my job is to send other people's codebases to ChatGPT for code reviews.

**u/elpinguinosensual**（1 分）：
I’m new to this industry (in school right now) but a really similar thing happens in my current field (healthcare). Young people just coming into the workplace don’t seem to have much in the way of problem solving skills or critical thinking. I think it’s difficult to convey to new grads that critical thought is a skill you have to learn, not some innate thing that only smart people have. Like, at least attempt to solve a problem yourself before seeking help. Respect the other persons time.

**u/DIRTYWIZARD_69**（1 分）：
I’ve only used ChatGPT to explain code or breaking it down if I’m having trouble understanding it.

**u/tweakydragon**（0 分）：
I’ve found it is really good at helping you get started in things that you kind of know or know about and giving you the right language to move ahead. 

Especially when I’m trying to go across multiple tools or APIs to get some info. 

Oh crap is xxx variable a slug, tag, blob, etc when I make this API call? With ChatGPT you can describe your problem and it can go “oh when you are working in this tool that term is referred to a Y. 

It feels like Google is really helpful if you know exactly what you are looking for. 

The code isn’t always the cleanest or work all the time, but it has surprised me from time to time with how it went about solving the problem and I can use that as the starting point.

**u/ThekawaiiO_d**（0 分）：
I tend to ask chat gpt first as well but if that is wrong . I would rather scour the earth before I ask any higher up for help. To not even give google and try before asking is just lazy.. There are also 3 other llms if chatgpt doesn't give you working code. He needs to use every tool be it books, google, llms.. The answer is there try every possible route before asking. Only after after you have exhausted all avenues do you ask.

**u/notislant**（0 分）：
For me if im playing with a new personal project it saves me a lot of time.

'What are some good libraries to use if I want to do__'.

Then ask it for simple code to do __. If it works its great. If it doesnt I usually just try to debug it on my own. If that fails I check the docs or google.

(One thing its amazing for is niche stuff with almost no documentation, but apparently enough public github repos to learn from).

It saves me a lot of time and even using it this way you likely dont learn as much without.

But the biggest issue with it imo is right at the start of learning programming. You become helpless and unable to problem solve or debug anything when you just ask the AI all day. No basic debug/problem solving skills is just crazy.

You'll see a post in this sub every day as well about 'learning via chatgpt is great, I copy paste blocks of code'.

**u/chipper33**（3 分）：
You wouldn’t hire them based on this single instance? C’mon, that doesn’t mean they necessarily suck at everything they’re trying to do.

**u/tdifen**（1 分）：
It's going to be tough for new developers for sure. I will say though good grads are still going to write good code as they will have an understanding of how code flows together. It will be the grads who come out of university where each line of code is a struggle to write who will be overly reliant on it.

I'm sure there were conversations around developers 25 years ago about a new wave of grads who just google everything and copy paste out of stack overflow instead of reading technical books around a language.

It's a new way to learn but it's not a perfect tool. Anyway my 2c :).

**u/PetalEnjoyer**（2 分）：
I heard a story of a guy who had 1 developer working for him.. after months of work, he released the project - just to find out that it's full of bugs and completely not functional.. it later turned out that the developer wasn't really a developer, but a guy using chatgpt for everything.. 

it cost him hundreds of thousands of dollars + wasted time

**u/InternationalPlan325**（0 分）：
It's a great tool. Def better than not having it at all. People that like to default to saying stuff like this as a means to dissuade someone from using it are the same people on here that are much more likely to respond with a "correction" of someone else's comment rather than just being helpful on their own accord.

Obviously, chatgpt and other LLMs alike come with a learning curve like everything else does. You eventually will learn to ask the right questions, set up the initial prompts you want it to use, etc. Eventually, you move on to other language models and figure out which ones work the best for you depending on the situation.

I've been learning things much faster and more efficiently since chatGPT hit the scene. And also have the confidence to try things I never would before because now I'm confident that I can figure things out if it all goes awry.

**u/kaungzayyan**（1 分）：
ChatGPT never returns an optimized solution and the code never follows best practices. My approach to use ChatGPT is to ask for the generalized code and scan through it, then read the official documentation for that topic and write the code myself.

**u/nakedpagan666**（1 分）：
I am about to start school for IT so no anecdotes on that yet but I had ChatGPT tell me my (clearly) parsley sprouts were basil. I was trying to identify other sprouts in my unlabeled planter and you could clearly tell it was parsley.

**u/akoOfIxtall**（2 分）：
i use it when i have an idea of what to do but not how to do, then i ask how to do such thing and adapt into what i'm doing, had enough wrong code given to me when i tried asking about C#...

**u/PSMF_Canuck**（9 分）：
Going to be blunt - if you have a developer intern that can’t figure out how to write a for loop - no matter what the framework, you need to get better at choosing interns.

> **u/Zozi-_-**（1 分）：
> Try removing intellisense as well and see how it goes :)

> **u/ricamnstr**（3 分）：
> To be fair, if they’re using an automated test framework like Robot, there can be a little bit of a learning curve, cause it’s like writing in pseudo bash, and the amount of spaces you need between a keyword and argument is not intuitive.

**u/Hari___Seldon**（1 分）：
Yet another reminder that a CS degree is not meant to produce software engineers who are ready to make meaningful code contributions immediately.

**u/emefluence**（7 分）：
Developing for 30 years. Learned a bunch from it. It's an excellent learning aid. Maybe you're not using it as well as you could?

**u/Nimweegs**（1 分）：
I'm running into much of the same issues with a junior I'm trying to mentor. During a session he even had the balls to pull up chatgpt, prompt it with some code and tried to decipher it / copy paste stuff. I asked him if he even understood half of it. It's a major turn off getting asked to help someone, finding time and trying to guide them (not feeding them the answers mind you) and then this happening because he can't put 2 and 2 together. I wouldve been so happy if instead of a prompt that gave him some Code - he'd googled and ended up on docs or a tutorial and said hey I'm going to study this for a while. 

Juniors (and interns alike) please stop using chatgpt. Use this time to educate yourself, your productivity isn't the most important thing.

Learn how to debug, the tools are awesome these days. Click through methods, set break points, examine the state of the application trhoghh its callstack. Read the javadoc for fucks sake.

If you don't understand some documentation or if it's too verbose or whatever: paste that into chatgpt and ask it questions. It's a language model, it predicts the next token. That's what it's good at.

I'm genuinely about to ban this entire goddamn tool. Part of becoming a software engineer is making mistakes, being stuck, scrounging docs, learning how to formulate a proper question so next time you encounter something similar you will recognize it: not mindlessly paste snippets into some tool.

**u/No_Run8454**（1 分）：
This is very true I attest to this, I totally stop learning from ChatGPT this time, and holy shit the understanding of lecture notes really made me look at my dumbfounded self in previous sems. ChatGPT taught me to memorise, but never the whole context of understanding. Only useful thing is for citation and sentence restructuring.

**u/Jackmember**（1 分）：
Ive discussed this topic lots with my professor.

Based on the experiences I, both in terms of using it myself and seeing how others use it in various workplace enviroments, have made we both came to fairly similar conclusions.

And in that I tend to agree. Text transformers like ChatGPT bear an inherent risk, due to them being able to hallucinate. With enough knowledge on the subject you can fairly quickly discern if what it says is plausible. However, you might understand what it does but never why. And once you leave the realm of well understood problems, youre suddenly stranded.

I found that students, apprentices and other (mostly) inexperienced devs approach transformers very naively. This means that they treat the result from the AI like puzzle pieces and slot them in. If it still doesnt work, they generate another piece and keep going so long until there is a solution. They know what the individual piece does and maybe what the whole should do. But they have never made enough effort so to to learn what their code does.   
*^(This has already been a problem with spoonfeeding on stackoverflow, except now its exaggerated with lies.)*

My university has accepted that AI will now always be part of a students tools and they are acting accordingly. However, they also want to advise students how to best use AI. Unfortunately, my professor has not yet come to a definitive conclusion, so theres not much I can say or point towards. All thats apparent is that it makes you lazy.

With that said, I did come to the conclusion that there are methods to make AI an actually helpful companion. The Socratic Method is one of those, to turn ChatGPT into your rubber duck. Writing E-Mails is another. Having AI write code for you to use, is not one of them.

**u/Fluid-Leg-8777**（1 分）：
Depends, if chat gpt is the edge/bing one, then it will answer based on the like 10 first results on google

Ussualy forums like reddit, math exchange or stackoverflow

Or the documentiation of the thing you are trying to learn, as its ussualy the first result

Tought, it lacks when the topic is niche, like Beyond all reason and noita modding (<i tried)

Tough, you could download the docs page and feed that to chat gpt, but at that point you might just as wellbe your own chat gpt and read it yourself 🤷‍♂️

**u/Linkario86**（1 分）：
Yeah if they start out it's bad. I find it a useful tool for myself when I touch a bit unfamiliar stuff, but as long as I can just extract the parts I need despite the incorrectnes of the rest, it helps me to proceed a bit faster than googling. I don't thing any LLM I tried ever produced something that I could basically copy paste into my Code. Not even Github Copilot, except for some extremely common simple properties.

**u/counts_per_minute**（2 分）：
I am absolutetly not a developer but I have a job that puts me behind a desk with a computer most of my shift. This job benefits a ton from data visualization and automating some redundant data entry. We have some crufty APIs that were implemented by and for a whole different group with different location and goals.

Using LLMs has enabled me to do things that our local factory values and saves time. These are things that add real value to the "boots on the ground" who are never considered when the company uses real developers for their high level reasons. There is still some "skill" involved because I know enough to know the right questions to ask it, no one else at my level knows what an API is, or that they even exist (I dug them out of vbs macros and chrome's developerer view), how to use command line, wtf is json, and the arcane jq commands to turn the API requests into a scriptable csv generator ( most here work in excel). 

I just happen to be a Homelabber in my personal life, I seem to dabble in all aspects of technology yet have always had a dislike for the syntactical nature of most code, I find making fish shell scripts very natural but thats about it. In my case Im completely reliant on LLMs at the current time, but its "enough" that is carved out a "development" niche in an area that needs some but doesnt get the resource allocated. Pragmatically this whole thing may make a significant impact in QoL for 40 employees and possibly my income.

**u/chihuahuaOP**（1 分）：
I'm actually worry becouse some of the thing I learned while reading answers in stack overflow is how bad and dangerous my ideas are.

**u/LordZarama**（0 分）：
As an intern myself and also a User of LLMs i actually agree, partially. ChatGPT is great for getting a field or getting condensed information on an unfamiliar topic. It can also help with repetitive and boring tasks in familiar languages. I've learned python before the whole AI thing took off, so I would say I have decent beginner googleing skills and would manage perfectly fine without LLMs but it's just very convenient to ask questions in plaintext and also receive what looks to be the right answer. I love to use it for GUI generation. Because it's so much code that's repetitive that I frankly don't like it too much. But other stuff is simpler to do by hand, especially if it depends on a bunch of code that the LLM doesn't understand. Sometimes, the things it generates are plainly not usable, so it's definitely necessary to know what you do before asking an LLM to do it for you.

**u/AyakaDahlia**（1 分）：
I was just tutoring a student the other day who I had to give a little mini lecture about AI code generation. I think he understood, but who knows if he'll follow through. 

It doesn't help that most of the professors at my school have students use replit, such had AI code completion on by default. It's just a massive crutch that cripples the learning process at an early and critical stage. 

On the other hand I've seen students who seemed like they were afraid to Google for answers. Not a bad attitude to have in school, but you also need to learn how to use your resources. I've tried to show a few how to Google for and use official documentation. I doubt any of them started using that resource, but at least they've had exposure to it.

Also, as I'm a student tutoring other students, if you guys have any criticisms or suggestions they're more than welcome.

**u/Klutzy_Act2033**（1 分）：
I see this as a persistence problem rather than a problem with ChatGPT. I suspect your intern would have gotten stuck if they had chosen to Google and the first link wasn't helpful or they didn't understand it.

I run into this with junior techs frequently where if the first attempt doesn't work, they ask for help instead of doing further research. I think it's a fairly natural consequence of not having a good sense of what you know, and don't know. "This should work and it didn't so it's probably me I'll ask the other guy"

**u/RexDraco**（1 分）：
I tried with an open mind using chatgpt for programming. lots of potential , but it isn't a good crutch. I so far use it mostly for asking questions like its a flawed human being, creative questions or the likes, but real information when there is a real answer, it is the last tool I think of. exception is when I ask it things that are easy to fact check, which I do see often it gets wrong.

**u/Scimir**（1 分）：
I work as an system engineer and we face the same challenges with many of our junior staff. 
ChatGPT is always the first and last source of information to most of them.

Personally I find it quite astounding how fast researching a problem or trying to find logical connections moved aside for LLMs.

Most of our senior team members also use ChatGPT but it makes a big difference if you understand the underlying matter and simply use it to reduce typing time. Sadly that also seems to convince all the other staff that LLMs are the best tool in every situation.

When thinking about it I am not looking forward to the next round of interviews.

**u/heythisispaul**（1 分）：
Yeah, I've found myself in a similar situation. I think juniors tend to conflate "learning how to code" with "getting a solution".

I find that especially at that level, most of the time your tasks are simple, and are usually just small parts broken down into bite-sized pieces so they fit in a scope that is manageable for them. They fail to understand that the true value of them doing the task is not the end result, but *the fact that they learned how to complete the task.*

AI can be such a helpful tool to bootstrap a good developer, but it's important to understand these fundamentals before understanding why that bootstrapping is so valuable.

I think this problem has existed for a long time - I suppose it's not that functionally different from people just ripping the first SO result they find when they Google, but the rise if AI has made asking and receiving contextually relevant data that you didn't have to think through yourself much easier.

**u/warpigz**（1 分）：
Sometimes the first Google hit is right and sometimes it's wrong. Sometimes the first ChatGPT response is right and sometimes it's wrong.

Both can be good learning tools. If the user can't switch to different sources of info to get the right solutions for their problems that's a user issue.

**u/great_gonzales**（1 分）：
A LLM should be viewed as nothing more than a knowledge search tool. It can be unreliable and people need to know how to search for knowledge in other locations if the LLM fails to find the relevant knowledge

**u/WhatsYourCoreValue**（1 分）：
I think your post touches on something important, which for me has to do with assessing problem solving skills at an intern level context. 

What does academia, and the industry, view as crucial problem solving skills in the field of software engineering nowadays for interns? Is it good grades? Is it being able to solve Leetcode and HackerRank problems? A project portfolio that clearly shows potential? All of them?  

(I'm genuinely curious to know since I'm not a programmer myself)

**u/JadeDragon02**（1 分）：
Just wondering, what is the opinion on like copilot from github?

**u/davewritescode**（1 分）：
It’s a horrible tool for learning.  It’s only real use is to build quick prototypes

**u/pinkwar**（1 分）：
What am I missing here?   
For...loop and basic syntax should be prime time for LLMs. That's where they excel the most.

**u/SpiritRaccoon1993**（0 分）：
I started learning with ChatGPT, really had some steps forward. Because of a more or less useless manual it was the only solution.

But as soon as you are in need of complex codes and grow out of cout and printf ChatGPT is useless. A great tool for knowing how not to do it.

**u/jupiter3738**（1 分）：
Im no expert but chatgpt has been amazing in helping me learn to code. It’s pretty damn stupid and it can’t write code for shit but i think it’s an amazing thing to be able to ask any question no matter how stupid and at least get an attempt at an answer. You can’t just copy and paste its code expecting it to work of course, but sometimes it generates good ideas or at least gives insight on what the real question is I should be asking/googling/researching. And if not, we “conversate” and figure it out. And on the occasion it does end up generating a working chunk of code, you don’t just use it and move on… you gotta study it and understand why it works and then improve it if possible. Shit I might do that even if the code doesn’t work. If I see it suggest a function I’ve never used before, I usually decide it’s time to figure that shit out and read up on the official documentation. It’s also been great for debugging, finding stupid mistakes, typing out repetitive shit, and probably best of all, explaining the functionality of mine and/or other people’s code.

> **u/SukaYebana**（1 分）：
> >  i think it’s an amazing thing to be able to ask any question no matter how stupid and at least get an attempt at an answer.
> 
> This

**u/Puzzleheaded_Low2034**（1 分）：
My experience is that it can compliment learning, you'll just have to review, understand and test its output - so then, the question is, is that process faster than writing it yourself? Sometimes it is, sometimes it isn't. 

Learning bad habits from a *bad programmer mentor* is worse.

**u/vikmaychib**（0 分）：
ChatGPT is a great tool for learning if you are aware of its flaws and train yourself into the topics of prompt engineering.

**u/shuckster**（1 分）：
It’s a great tool for learning. 

Just don’t ask it to print code: only lesson and revision plans.

Write your own code.

**u/wellred82**（1 分）：
I've had a few people suggest not to bother learning to code because chat gpt can just do it for you.

**u/Helix_Aurora**（1 分）：
My general rule of thumb goes something like:

1.) Never ask a Chatbot for something that you can get a definitive answer for quickly on Google.  
2.) Anything harder than that is actually probably too hard for a Chatbot to do reliably.

3.) If you can't validate a solution, don't use a Chatbot.  
4.) If you can't validate a solution faster than you could write it yourself, definitely don't use a Chatbot.

**u/Pipero_**（0 分）：
Honestly this is such a poor post. People always are defensive towards new methods/technologies.

In 10 years time someone will be posting here about how their intern sucks cause they used whatever new technology there is instead of ChatGPT(or other AI tool).

Less posts like this more uplifting and helping others to improve.

**u/IUpvoteGME**（1 分）：
ChatGPT is great when you already know what it is going to say, and you have the experience to validate it. But being able to find errors in it's work is key. That means understanding the fundamentals first, this cannot be skipped.

**u/TheMihle**（1 分）：
As someone that is studying in uni now and have tested different things.  
(What I learn most from)  
I find the most effective to use both Google(stack overflow or documentation), AND ChatGPT.  
I dont get it to program for me.

Sometimes I find the result I get in google, that I dont understand because its too advanced/expect a level of understanding I dont have yet. Then I use ChatGPT to try to get it to explain it differently. If I understand ChatGPT explanation better AND it match up with the stuff I found via google that I then should understand more, then its golden.

Basically use ChatGPT for ExplainLikeIAmFive.

One example was that I didnt quite have an intuitive understanding via Google results of what a Bean/Autowired in Java/Spring boot, but ChatGPT helped me getting that in a way that made what Google results said made much more sense.

**u/Pikachamp1**（0 分）：
I'm sorry, but unless you are teaching your intern exactly what you're telling us here, the over-reliance of your intern on ChatGPT is overshadowed by your failure as a mentor. Based on how you talk about your intern and the situation it sounds like you didn't teach him but please correct me if I'm wrong becausevI sure hope I'm just misreading your recounting style. But apart from that I fully agree that ChatGPT is a tool with pitfalls that are often overlooked, so we need to steer our Junior colleagues and future software developers into the right direction there. It's actually linked to a effect well understood within psychology (the more assertive you talk about something, the more likely it is that people will believe what you say, even if it's utter bs). And unfortunately ChatGPT is trained to always be assertive.

**u/xvelez08**（1 分）：
LMAO this is a wild take. It’s the perfect learning tool, that’s EXACTLY what it’s good for. A quicker search engine. 

No, you can’t just copy and paste code. But you can generalize and ask how to do certain things and then apply them to your situation. Same thing you’d do when searching stack overflow. You couldn’t just type in your team’s code and get an answer. Only difference is chatGPT does it 100x faster. 

Lastly, absurd take on Googling. What happens when they Google and use the generative AI answer Google gives? Will you be upset about that?

**u/Normal_Vacation_4002**（2 分）：
can I be your mentor?

**u/J1618**（1 分）：
I would say that you have to know programming to get the most out of chatgtp and ai bots, if you don't know you take what they say as the example to follow, and it might be something wrong, unnecessarily convoluted, outdated, etc.

If you already know how to program you can see where it goes wrong, use it as a starting point for what you want and then fix it yourself, read the documentation of the packages, etc.

**u/Hillgrove**（0 分）：
would your view had been different had they asked an LLM first, Google second? To me ChatGPT is a better search engine, and when it fails I use Google/SO/YT etc.

**u/0_Ouroboros_0**（1 分）：
What most people fail to realize is that ChatGPT or AI in general, in its current state, can only be used as a crutch, not a wheelchair.

It can help you walk if you put in the effort. But it's not going to drag you around with bare minimum effort.

**u/PerceptionLive8446**（1 分）：
Of course we can’t *rely* on ChatGPT or AI, but we can *use* it just as much as we *use* Google. It’s kinda ridiculous actually that you’re criticizing your intern (who’s an intern, btw. He shouldn’t be as knowledgeable as you, Mr Engineer…), but then you yourself go hop on Google - which can also be wrong and misleading with its results. 

Point the finger at yourself first - learn the job a bit better before thinking you can take on an intern - and if that intern trusts ChatGPT more than he trusts you, well, maybe it’s a you problem? Show him how amazing you are, to the point he stops having a work affair with AI. 

Poor intern probably feels trapped and just wants to be better. I use ChatGPT all the time for coding projects, and I simply *correct it* when it’s wrong. AI needs to learn too, ya know. Use the tool, and use it well! It’ll speed up your work hundreds of percent. 


AI and ChatGPT powered coding - all the way! Only people scared of it or hating on it are those who *know* they’re gonna lose their jobs in 5 years.

End rant. But I’m right.

**u/Thaerious**（1 分）：
To be fair to ChatGPT, if your intern Googled the wrong answer, they wouldn't have known it then either.  University teaches how to learn, it sounds like your intern didn't.

**u/B-Rythm**（1 分）：
I graduate with my AS in Software Development in February. No school for the summer and am looking for an internship. Would you happen to have anything available?

**u/SometimesFalter**（1 分）：
A tool being wrong can help you be right. Obviously if you copy paste code you're gonna get bad solutions but if you use it to discover APIs, get ideas, etc you're gonna go far.

**u/Own-Pickle-8464**（1 分）：
I think the problem lies in people's critical thinking / problem solving skills.

ChatGPT ain't perfect by any stretch of the imagination, but if your intern's first impulse was learned helplessness (well, I didn't get the answer on the first try, oops!), that's more of an issue.

**u/Vandercoon**（1 分）：
Have you tried asking dumb questions in a place like Stack Overflow as a complete beginner? 

The downfall of toxic devs is something I can’t wait for to be honest. 

I can’t code but I’ve made an iOS game, web app, in the process of a Godot game, countless scripts in python for helping me do meaningless tasks thanks to ai. 

Is it the best way? Maybe not. Is it safe and accessible? Absolutely.

**u/JuZNyC**（1 分）：
I have a few friends who used CHATGPT previously and now don't know a single thing when they try to code a project without it. I like using CHATGPT for debugging because it can see through my own implicit biases when reading my own code but other than that I never use it.

**u/recapYT**（4 分）：
Your post doesn’t really make sense.

You are talking like all answers on stack overflow are correct or plug and play.

Assume for a second the intern didn’t use ChatGPT but used stack overflow but it didn’t work, would you make a post about it?

I could also pull a wrong answer from google, is Google also not a good tool for learning?

Infact, ChatGPT can create study plans and suggest books and resources for learning, isn’t that a useful thing?

Anything that can give you information can be a good tool for learning. These things are tools but you are treating them like they are omniscient.

**u/kagato87**（1 分）：
A while back in one of the sql subs a user had asked why chatgpt switching a cte to a subquery fixed their query.

It didn't.  The LLM did fix the query, but it ALSO downgraded the cte the error was in to a subquery, masking what it had fixed from inexperienced eyes.

Readability is king.  Their original query was easy to fix.  The "fixed" one was actually hard to figure out.

**u/haragoshi**（0 分）：
I think that’s too critical. ChatGPT is right most of the time. There are other times that it is extremely wrong.  Sometimes you can check it with a google search and others you can’t. It’s worth dealing with the odd times when it’s wrong.

**u/unus-suprus-septum**（1 分）：
Please tell my programming 1 students. I had such a good class going. Llm's have ruined it
 Now everyone is failing programming 2 because the chat their way through programming 1.

**u/HashDefTrueFalse**（1 分）：
About 5 months ago one of my juniors, fresh from a bootcamp with no other software background to give context, spend a whole day on a task to show an enable/disable feature footer that persisted front end. No problem, it's not priority. He isn't asking me any questions and I'm not checking in closely as I've stuff to do.

He comes to me on the second day, no progress made. Turns out the very first thing he'd done was ask ChatGPT to build him a React component with a toggle, then add persistence etc. The nonsense it spat out looked fine but, of course, didn't work at all. He then spent the rest of the day "fixing" that code (not sure how exactly). In his mind he wasn't stuck, he was fixing it, so he wasn't asking for help. Code that didn't need to be fixed, because it was fundamentally not suitable even if it had done what he described. Basically the blind leading the blind.

Because of this, and issues with another junior pasting code with secrets into it, now heavily discourage my junior devs from using AI tools to generate code.

It's shit at writing code. It's shit at debugging code. At present, it's a glorified billion dollar Buzzfeed article and blog post generator. I really can't wait for the hype to die down because I feel like the quality of everything online is suffering at the moment.

**u/Mood-Rising**（1 分）：
I tell people learning to program to avoid built in string methods until they have a basic understanding of how they work. As a Sr dev I rarely copy and paste code unless I’m the one that wrote it. A big part of being a good developer is reducing unknowns, and LLMs are just a big black box. New developers don’t know enough to understand the code that gets spit out or the larger consequences of adding that code to the codebase.

In short, if you don’t take the time to understand the code you are contributing, you aren’t learning and you are likely offloading work onto the rest of the team via code review and bug fixes.

**u/red_dog007**（1 分）：
It has the same issue, maybe even worse than "dumb" search.  You have to know what to ask and ask in such a way to get answers you are looking for.  It is amazing how bad people are at this.  

If you can't ask AI to write a loop, it's gotta be a terrible question. So far in my experience, getting code out of LLM is about the best thing, and maybe only thing, it is good at. I've been having copilot do some assists for me, and when I do it is essentially copy and paste.  Even when I ask something specific on what I need around the code I already have without giving it my code, I get a pretty much copy and paste answer. 

Just like google-fu is a real skill, ai-fu is going to be a real skill.

> **u/DAGRluvr**（1 分）：
> LLM’s haven’t seen new data in years in terms of what they have access to. Most solutions you get even with an ide based LLM like copilot have been deprecated for years.

**u/DOUBLEBARRELASSFUCK**（1 分）：
ChatGPT is great for doing something you know how to do for you.  It saves typing, and even if it's wrong, you can fix it faster than typing the whole thing.  I'll never manually code a menu again.

**u/Not_invented-Here**（1 分）：
When I was learning another language before Google translate was a thing, my brain had to be engaged more to figure out the word, I had to look it up, figure out the pronunciation etc. More neurons were being used and I retain those words a lot better and more fluently than nowadays when Google translate just tells me stuff

**u/cursedpoetic**（1 分）：
Just ask it to perform complex math. It will fail miserably everytime.

**u/PatternsComplexity**（1 分）：
I want to preface my comment that I am not bashing you or the intern.

I don't agree with your title though. I think GPT is good for learning.

I don't know why the hell people ask ChatGPT "how do I do x".

Don't do it. First tell it to go online and check the online documentation for what you're working with. This way it will pull actual, proper data that it will then base its answers on.

At that point it's not ChatGPT telling you how something works, it's the documentation doing it instead. ChatGPT only parses that documentation and gives you answers to whatever questions you have about it.

You know... using a text model for text processing, like it should be used.

Second of all, I've heard so many times "ChatGPT can't do math". Yes, it can't do math for shit. But you need to be a complete ape to not figure out that all you have to say is "use Python to do all the math for this problem" and then "now write a test that challenges the validity of this code".

Can it still be wrong? Sure, but you reduce the chance by orders of magnitude, compared to just directly telling it to do math.

I've successfully learned the basics for electronics engineering and created a tazer fully off of ChatGPTs knowledge. Besides, whenever it hallucinates you can kinda tell. Sure you might miss it, but the hallucination usually looks out of place or over-confident.

And a side-note: So many people try to use ChatGPT 3.5 or 4o. The first one is worse than a toddler and the latter is overconfidence gallore when you communicate with it in text. It was designed for real-time voice communication but they haven't released that part yet, so this 4o model is in this limbo of being faster than 4 but having real issues with hallucinations and repetitiveness.

**u/Xemptuous**（1 分）：
Definitely sucks for learning. I had a class where we needed to make an ANN to simulate an XOR. I did it from scratch in Zig. My classmate used chatGPT. She literally has 0 idea what happened, and according to her, will never be able to do it again. I refused to use GPT cus I actually wanted to learn, and now I can implement it again if need be. 

I just use it for simple stuff I can't be bothered with, like generating large maps and lists, or making sample INSERT statements based off DDL. Other than that, I'd rather struggle and fail in order to learn.

**u/Asrikk**（1 分）：
ChatGPT is only useful in the right hands. If you're educated on the subject enough to challenge its answers, it can back itself up and cite sources. Which makes it a better tool for expedience for experienced people. I wouldn't rely on it as a learning tool. Plus its obvious erosion of research skills is a major problem.

**u/classy_barbarian**（1 分）：
This is literally just this week's post about how "AI Sucks, we asked it to write code for us and the code was bad! therefore AI has no practical uses"

**u/B1SQ1T**（1 分）：
How did he even get the internship if he couldn’t write a for loop..?

**u/amitjain679**（1 分）：
If you have a good knowledge about specific topic and using help of chatgpt, it's great. Otherwise, it is bound to create problems.

Chatgpt is smart but not everything it says is going to be true. So if you are completely reliant on chatgpt, it is bound to create issues for you.

**u/In_Viv0**（1 分）：
I started coding (statistical – Stata and R) just before ChatGPT was widely available. I also don’t have much formal  training in coding. I’m finding using ChatGPT and copy/pasting the lot is similar to copy/pasting chunks of other people’s code that doesn’t do exactly what I want (“copy/pasting code is bad for learning”). I found the best is being able to understand the documentation and using it. The problem is the latter is also the slowest option, and the less you know, the harder it is to use it. And if you don’t know how to do it in the first place, you have to read a lot to find what you need. Or even better – understanding the fundamentals first, then using the documentation.  The trade off – it’s slow, but you also learn for the future, as understanding what you’re doing is the fastest option. If you can predict the future, you learn things you’ll use regularly.  Asking someone for help is also great because they can tell you things you didn’t even think you needed to know – especially if it’s on the job and they are doing similar. The catch is, it uses up other people’s time. 


In reality, all approaches have their place and you shouldn’t rely on one. Sometimes I find myself wasting half a day on ChatGPT code, and then I google it, up comes the vignette of a useful package with an example of almost what I want to do combined with enough info to make the changes I want. Other times I wasted time trying to understand documentation, and ChatGPT uses something I haven’t considered, and gives it to me faster. And of course, there is how you use ChatGPT.

**u/oosacker**（1 分）：
I asked Copilot how to write SCSS and it came up with trash

[https://imgur.com/gallery/github-copilot-fail-btPQo3y](https://imgur.com/gallery/github-copilot-fail-btPQo3y)

**u/Slodin**（1 分）：
I hate how the dumb thing lies to you. It’s great when it works, but it doesn’t know how to tell you. Yeah I don’t know lol.

So yeah. You got to know your stuff using it.

**u/Snoo_4499**（1 分）：
I think its good at debugging. It sometimes write garbage code and lets not talk about maths but its god at debugging problems 😅.  But I've not done very very complicated project so idk.

**u/Gr1pp717**（1 分）：
It being wrong is a good thing.  They have to take the time to understand what direction it was going and why it was wrong.  That takes understanding.  Finding the answer on google does not.  

I think of AI like asking a coworker or buddy for help.  They don't know enough details to give you a concise answer, but can help give you ideas.  Point you in the right general direction.   Struggling a little on your own is helpful, yes.  But only to a certain degree. 

That said, if they're throwing their hands up after copy-paste doesn't work, that's a problem.

**u/aaRecessive**（1 分）：
I've recently started learning react having most of my experience in data science. I'm more than capable of learning the fundamentals and quickly developing, but wanted to try learning via chat gpt as I have yet to use the shiny new toy for serious development.

With gpt-4o, it is correct the first or second time for 99% of inputs. Despite the extensive explanations it would give, I found myself becoming progressively more reliant on the LLM as the project grew. The biggest issue I faced is since I didn't write the code, when I need to change something I have to study how every file links to know where I should make the change. Had I written the code myself, I would intuitively know how the project works, and where I should make the change.

It's ironic because you would think chat gpt would enable rapid development, but you end up having to argue with a chat bot to get it to do what you want instead of just writing the code outright. It's definitely faster (and safer, and more efficient, and future proof) to learn legitimately.

**u/LowerMathematician32**（16 分）：
Boy, I'm sure glad I didn't get stuck with you as an intern. 


You had an opportunity to mentor someone, but you instead decided to sit by idley for someone who could have benefited from your guidance to make a mistake, and then, instead of helping them correct their deficiencies, you let them run into a brick wall to ensure that they looked incompetent.


My suspicion is that you wanted to prove to the intern (or perhaps yourself) that *your* approach was better.


If I were managing *you*, based on your inability to effectively collaborate with junior subordinates, I would, at best case, not recommend you for promotion to a senior position.

**u/not-halsey**（1 分）：
I find GPT good for code snippets or quick architecture concepts. But only if I can verify it. Only once have I used code from GPT where I didn’t fully grasp what it was doing. 

I have had it make up functions that don’t exist. Or generate extremely redundant code

**u/GabbarSinghPK**（3 分）：
Sorry to move a little off, if you aren't satisfied with the way he/she is learning. I think you should also invest some time in their growth and mentor them how to learn the correct way. 

When I was an intern, my mentor never told me how to learn and took me a couple of months to learn stuff and debug the right way (or maybe a better way).

As a mentor you would also be successful if you were able to make them a better engineer. I would suggest to treat an internship as a 2 way contract - the intern has to learn and upskill along with the primary way of getting things done with an intern. 

I am posting this comment, just because you have mentioned that you are not going to recommend them to convert to full-time. And it remembered my initial days in the industry.

**u/branh0913**（1 分）：
I had a manager and he did not know how to code. He only knew how to generate code from GPT. So had to constantly go behind him and correct his code.  I told him he need to start learning how to code on his own.  His dependence on GPT was annoying.  For the record I do have a paid version of GPT.  And I still think it produces pretty awful code.  And co-pilot was so annoying I had to turn it off months ago.

**u/ChihuahuaCaca**（1 分）：
Fuck AI. Everyone should boycott and actively oppose anything to do with it. It will be the downfall of mankind and is already taking away countless jobs. It’s alarming that more isnt being done to stop this. Society needs to wake up and stop being complacent, and i dont wanna hear a damn thing about it making things easier for us.

> **u/SukaYebana**（1 分）：
> there's zero change that would ever happen, we have to adapt or perish

**u/TransportationCute47**（1 分）：
It does pretty good with coding ( ! well it also depends on what you prompt) but gives you complex solution even though you can write the code in fewer lines.

**u/coldpoint555**（1 分）：
I think this reflects more on you as the mentor and your character than the intern. How you treat your co-workers reflects your personality.

For example take ANY other profession. Like a mechanic. Somebody with years of experience doesn't even realize how skilled he is because it's easy as breathing. And the new guy doesn't have those skills. He looks incredibly stupid to the mentor right? But the mentor doesn't realize he was also that STUPID at the start.

The question now is what the mentor will do. **Gatekeep** and have aggresssive attitude or be patient, kind and teach the young guy? 

And in software EVERYONE IS A JUNIOR AT SOMETHING. Guess what big shot. You don't know SHIT about the new framework either. But you solved it? How? Because you learned problem solving skills. Teach them to the next guy and don't be an asshole.

**u/Gabe_b**（1 分）：
 No,  it isn't, it's a nice rubber duck though

**u/AtmosphereWhole4010**（1 分）：
I don’t look for exact answer from chat gpt. I’m gonna implement the code on my own. But using its as the tool to have an 101 look into the fields or an assistant that connect notes or help me organize my understanding. In those cases, it work really well

**u/Any-Astronomer9420**（1 分）：
Haha the same with a colleague, he always use GPT for All Things. When he got introduction from me, He Copy it and Post it into GPT. So long until he gets a great result but the code looks like shit.

**u/kodaxmax**（0 分）：
It's a fine tool for learning. But self directed learning and research is a skill in itself. If your just trying to plagerize then honestly chatGPT is probably gonna give you better more relevant code than a google search.

Let's be real, every dev relies on google atleast occasionally. this is no different. You just need to be able to filter out the bad results and learn the best way to phrase queries to get what your looking for. For instance for looking up basic syntax for a loop, your best just googling an example or looking at the docs. But if your trying to find out how to sort a list of objects by one of their variables chatgpt is often going to give you a personalized answer that fits your specific use case better than google or the docs. If it doesn't then your gonna have to ask a detailed question on reddit or stack voerflow or whatever.

**u/ParticularContact226**（1 分）：
Please can you mentor me.

**u/krav_mark**（1 分）：
Learn your intern to look at the framework documentation first.

**u/Zuler**（0 分）：
I still think ChatGPT is a great tool for learning, as long as you take the results with a grain of salt and back it up with your own research!!

**u/Sharks58uk**（1 分）：
Thanks for this post and the comments. It's really good to see the different perspectives here.

I teach introductory programming courses at a University in the UK and generative AI is a really difficult problem - especially when trying to develop foundational knowledge. 

Ultimately we cannot stop students from using AI and when students graduate they will be using AI in some form so I think we need to embrace AI tools but also emphasise that students need to be able to understand and adapt the generated code, and to treat it with a healthy dose of skepticism. 

It's a very difficult problem - and I think it's taken us all a bit by surprise but I hope we'll be able to find a solution that is appropriate.

**u/DunkyFarf**（1 分）：
I used it to learn without any issues. I never expect or accept any code from GPT, I ask for explanations and terms to look up.

**u/Teekoo**（1 分）：
It was great for when I was learning iOS and coming from android side. Speeded up my development.

**u/SukaYebana**（0 分）：
Maybe you was supposed to give him some guidance? AI is great tool and i would argue it's even more effective than google. You should tell your intern that he should rephrase questions given to AI so it accelerate his learning and prevent dull copy pasting It's all about prompts

**u/NeighborhoodFlimsy72**（1 分）：
I asked chatgpt how to subnet (I had already worked it out) but keen to see if it knew / could do it ;), gave me the wrong answer 3 times and it changed its answer three times with a “I apologise that was wrong, this is right”. I feel a lot of younger people will be relying on it as a learning tool rather than learn themselves, which will have a negative impact on them and employers long term. 

I’m not saying all the AI information provided will be wrong but it definitely isn’t what our children should be learning from.

**u/CancerRaccoon**（1 分）：
I am 100% with you. 

I mentored 2 entry level devs in the past 3 years. The first one had become already semi-Independent by the time gpt and copilot came out. For him these are tools to handle boilerplate code or to generate documentation.

The second guy came a year ago. Competent, smart, but 100% reliant on AI tools. With him, since we didn't interact that much in the implementation phase of a ticket, the real progress took place during code reviews.

Do code reviews people!

**u/GCSS-MC**（1 分）：
Just like any tool, it's useless if you don't know how to use it properly. This isn't a new concept for tools.

**u/Gigusx**（0 分）：
ChatGPT isn't good for learning if **you** are not good at learning. If you are, then ChatGPT is going to help you learn. Your intern's thinking process when encountering a problem already shows that he's in the former category.

Btw, I've never heard of anyone getting a wrong syntax for a loop. That'd be the first.

**u/chajo1997**（0 分）：
ChatGPT is great for speeding things up but you have to know what you want and how you want it before asking AI. The answers it gives need guidance every time and it tends to make a lot of spaghetti. 
It definitely isnt meant for learning but instead as a tool to help you build and setup things faster. It really helps when you are thrown into an ongoing project.

**u/Puzzled_Wave6244**（0 分）：
I’ve been using google, stack overflow, Microsoft docs, and countless books to learn different programming solutions in C# for about 12 years now.

But I have never learned more than I have in the past year or so since using ChatGPT to help. These books and forums can’t re-explain things to you in a way that make sense like chat does. It’s just so helpful for me. 

To be fair, the stuff we are doing at work is not groundbreaking or anything. We just need backend business logic for process manufacturing. It’s all simple stuff, but as an EE I can’t know both jobs. Software development is an added skill. 

Vett out the examples it gives you. Test and go.

**u/FabioSxO**（1 分）：
Yeah, I have been in the start of my learning journey and totally noticed that ChatGPT makes easy mistakes. People might fall for it because the AI appears 100% confident because it can not know whether they are wrong or right.

**u/-ry-an**（0 分）：
I disagree with the title sir. It sounds more like a him problem.

Chatgpt speeds up your workflow easily 3x if you know how to use it.

It can give you solutions, but it can also teach you. Everything you said in your post was correct. It sounds more like a lazy intern than an AI issue.

I'm literally using it to build a fully functioning app in a language and framework I've never used. I'll admit, it doesn't always give the right answers, but if you ask the questions in the correct manner, it's pretty good for basic to mid level concepts. It's up to the individual to do some extra research, then you can make the decision whether to implement or not.

**u/Voxelman**（1 分）：
In my opinion it depends, how useful ChatGPT can be. It depends on your prompt. It depends what you ask and how you ask. If you are very specific and precise an AI can be useful.

But I wouldn't bet on it

**u/jucestain**（2 分）：
This is how you can tell its not truly "intelligent" and thus does not pass the turing test (for anyone who is "intelligent" at least). The wide and expansive scope and instant recall is impressive (where machines way out perform humans, and a good tool) but just making shit up lets you know its not really reasoning about stuff, its just doing some pattern matching of things its seen before. 

I will say if chatgpt makes up function and method calls in a library that might be a sign those method calls should be there or should be renamed though.

**u/B4Beta**（1 分）：
I am an Infrastructure Engineer with 20 years experience.
Chat GPT is saves  my time reading the logs, detecting the patterns and as second opinion where I come with solution.
However if it is used as a source of only truth or asking to come with a solution which you have no prior knowledge then it is grievous mistake.
A couple of times it offered a solution which could break the codes or scripts.

So, if someone purely relies on chat GPT to do job then yes, I don’t think that person is ready to take a job.

**u/Gilly8086**（1 分）：
I think lack of debugging skills is a stronger concern than reliance on ChatGPT!

**u/Astrovet**（1 分）：
I am in a software developer course, my teachers stress HEAVILY that chat gpt is a last resort when google/stackoverflow doesn’t have a solution/similar problem, and when we do use chat gpt we are urged to ask it for a hint, and not the full answer.

**u/warriors91**（1 分）：
Might not have worked well in your framework but it’s spot on in most, like PowerShell, Java, .net, etc.  so I disagree with your assessment.  AI bumps each human resource one category.  Beginner, Average, Great, Superstar, Master.

**u/artlthepolarbear**（1 分）：
I've been using it as a source of how to start my learnings and research into a project, basically super Google. How do i do x within Y for z results from there. Cause ain't no fuckin way I'm gonna read 1000 of man pages to be able to find the exact bs I want done.

**u/Forsaken_Library_722**（1 分）：
very insightful seeing your post! I am actually doing research around how AI could help interns/entry-level engineers. Would anyone be up for a 30 minutes virtual chat? sign up here: https://forms.gle/8DkisKV3HfrcfPMn9.

My take is that if there would be a dedicated AI product designed to teach interns, this would be a life saver. On one hand it would make the intern feel more confident and boost his skills, and for the mentor, it would save some time.

**u/Musicklover**（1 分）：
Will using a privately run AI system curtail the privacy issues? Is that the only fear on running an AI in a corporate environment? @Nice2inch

**u/Floflolesbonstuyaux**（0 分）：
Just like with any other given tool there are people that can fully use it to their advantage and those that cannot use them properly. In my opinion, as long as you pay a very close attention to the way you use chatGPT and which information you disclose it can be a good help. 

Not perfect, true, but it does help in some cases. Whenever you're stuck and can't achieve what you want, people should automatically ask a real person or read the documentation to try and find the solution.

**u/Equal_Ad_3805**（1 分）：
I'm still trash at programming, but I've found that AI is a great rubber-duck. That's it. I don't use it for anything else, if I have a specific coding issue I look it up. It's not that bad if you use it correctly, but it severely atrophies my critical thinking when I just go to it first for answers.

**u/10ioio**（0 分）：
Likely more of a brain fart, and a moment in time, than something worth starting a whole angry mob about. I don't think the world is ending because an intern asked you a question he probably could've googled. This is probably the first time ChatGPT has failed them, and they probably already learned their lesson without you needing to drag them through the mud on reddit. 

The paid version of ChatGPT usually does quite well when the problem is basic and the language is common. I can see where the intern might've had success asking ChatGPT how to make a for loop in Java vs Python vs C++ and getting totally correct answers. So I can see why the interns first instinct wasn't "GPT doesn't know for loop syntax." I literally never ran into that issue until I started using frameworks/libraries GPT didn't have as much training on, so I 100% understand where the intern is coming from. 


The other thing is that sometimes people just know they'll get a better answer, more nuanced and more tailored answer from asking a person. I understand you're probably an introvert and don't like answering questions, but some people really do like asking a person about some things. It's always bothered me when there's a culture of shaming people for asking questions. I think that type of company culture a recipe for disaster because newer employees are prone to mess things up by not asking questions.

**u/skat_in_the_hat**（1 分）：
> There was no attempt to google the answer by my intern  
  
You know whats funny as hell? I've been in the industry for a long time, and using Unix based operating systems before google was a thing. When google came around, and the answer was wrong, they would immediately get on IRC and want help. We used to bitch about people not even opening the man page, or properly reading the error to try and figure out what the issue could be. This is your version of that.

**u/camslams101**（1 分）：
Cope

**u/falling-faintly**（1 分）：
I’ve definitely been seeing this. Had a cloud engineer who needed to migrate some data using an CLI tool. He just keeps spamming commands provided to him by chat GPT never thinking to just google the man page and read about what each of the options he is passing to the tool are doing. Just totally stumped when it doesn’t work. 

Its mind boggling really

**u/4skhole**（0 分）：
I would argue for someone like myself who is learning Python as my first language. It is helpful “training wheels” learning how the code / syntax is supposed to work. ChatGPT fills in the holes with explanations I can understand.

**u/freekayZekey**（1 分）：
yup, people wouldn’t even know if the code is actually correct or if they’re missing caveats. using an LLM to learn almost anything makes zero sense to me; how do you know if you’re asking the correct questions?

**u/consistant_error**（1 分）：
The problem really comes from a lack of understanding about how LLM's work. Tools like ChatGPT can be great to whip up some quick code if it's in a framework/language you already understand. Then you can easily see if something is wrong or out of place. 

If I use AI tools, I try to use something like Bing, where it actually uses online sources rather than guessing from training data. Even then, of course, it can still be wonky.

I think schools should start integrating education about not just basic neural network structure but also teach a basic understanding of LLM's. Might help teach newer/junior devs that 'AI' isn't just magic.

**u/Prototypz**（1 分）：
It definitely a double edge sword, which relies heavily on the type of questions you ask it. When I ask questions, I always make sure to be thorough. For example if I didn’t understand how to write a for-loop. I wouldn’t directly ask it to write a for-loop. I would break it down, why, where, when, how to use it, and never directly ask it to write my code for me. Its not end all be all tool, many times I still watch videos, or read documentation just to really solidify the subject into my head.

**u/PineappleLemur**（1 分）：
That's a user problem not AI tool problem.

He's trying to learn something from scratch with 0 background and apparently no brain to search for multiple sources to confirm that is how X is supposed to work.

It's a great learning tool and a great search tool (not talking about GPT specifically, AI tools for coding in general) as well. Knowing how to use it and what to look/ask for is the same as knowing how to use Google and how to evaluate a correct answer before copy pasting and see if it runs.

**u/UbiquitousFlounder**（1 分）：
I occasionally use it myself, but my questions are kinda like 'explain x to me on a high level' or 'I'm trying to do x but I'm not sure if it's possible, am I correct?' Asking it to write code is just asking for trouble as it may be using examples of not working code it has harvested from stock overflow

**u/matureUserName_**（1 分）：
I only use chat gpt to help me understand my own question, then I’ll go deeper with google and docs. 

**u/thr0w4w4y4lyf3**（0 分）：
I entered into a similar argument on here, where some described ChatGPT as “the ultimate teacher” even to the point they said being in a university classroom isn’t better.

The point is, asking an LLM to give you statistically likely output based on a question, isn’t an understanding of it being correct. An LLM model does not know it is correct. 

I mean there are many other factors and AI can be a great tool, but if it’s used as a learning tool, it’s like choosing someone to teach you who is self taught but also makes things up because they don’t really understand the material and will agree with you if you argue enough. Oh and they are always confident. So you’d never know what they are wrong about.

**u/CodeSmitty**（0 分）：
As someone teaching myself how to code at 35 years of age. I can say, people do need to understand that chatgpt can help with certain things. However, it should not be used as a tool to correct code. I have actually experimented with it for a small project I was working on. Most of the time chatgpt returned the wrong code, after many attempts of telling it. "This doesn't work." It dlivered something usefull. 

Whereas a quick google search was much more clear. Now one thing I did find chatgpt really usefull for. Was pasting code I found on like stackoverflow or docs. Asking it to explain this code to me peice by peice. 
That, it did really well on. It did help me understand certain keywords, functions etc. So I wouldn't say chatgpt is all bad, but people are using it too much for the wrong situations.

**u/KalebRasgoul**（0 分）：
I work with people who already had the exact same attitude way before Chatgpt existed. They were totally unable to even think about using a search engine to find the answer and instead went straight to ask coworkers.

The tools are not the problem. The people are the problem.

**u/__init__m8**（2 分）：
Yes it's bad, even if it gives you something it can be wrong and negatively reinforce you because it blindly agrees too often.

I do use it at work though for documentation. It can digest and answer questions quickly, though I'll still reference.

**u/SedTecH10**（1 分）：
Just my opinion, Getting answer from ChatGPT only works when you had an idea of thing you are chatgpting.

**u/chiapetti64**（1 分）：
I'm not that experienced in coding, but one day I made ChatGPT rewrite my simple calculator program, it added SO MUCH trash like defining and a lot of things that you can use, but are not convenient for begginners. And it also sucks at coding so it is not even worth it xd

**u/RTEIDIETR**（0 分）：
Your interns scenario has nothing to do with chatGPT, it has something to do with whether a person knows how to use new technology or not.
ChatGPT is perfect for giving someone a quick knowledge in a new field. Whether to solely rely on it or not depends on the person. 

Your intern is just straight out lazy not googling and just give up when chatGPT spits out the wrong answer which can be pretty common.

**u/DustinKli**（0 分）：
I would be curious what question he asked that ChatGPT got wrong with a simple for loop.

**u/wobblat**（1 分）：
Don't use ai to write your code kids 😃👍

**u/Nathan_Calebman**（0 分）：
Sounds mostly like you and your internt just suck at using ChatGPT, and it almost sounds as if you were using 3.5. 


The correct way if you want specific standard syntax is to ask ChatGPT to first do the search and then create the code. If it still doesn't work you just ask it to analyze why, to correct it, and to give you the links to the sources it used. Seriously, who in IT still uses Google!?

**u/Ah-Elsayed**（0 分）：
Gemini is better than ChatGPT when it comes to programming questions. It has its own mistakes as well, but its answers are much better based on my own experience.

**u/Kidzmealij**（1 分）：
This makes me feel good bc I have been trying to learn this on my own without ChatGPT and it’s always felt like I’ve been so far behind everyone. Right now my biggest hurdle is getting an internship.

**u/Southern-Painter-234**（1 分）：
Thnank you

**u/Impressive_Fact_2804**（1 分）：
I heavily used GPT, when I started learning. Because everyone else did / does. But I quickly noticed, that I started getting a form of learned helplessness. I had a problem, asked GPT and if the solution didn’t work (which is quite common for programming questions), I sat there not knowing what to do.

I now only hse GPT to find good variable name ideas, writing actual text for users to read and thats it. Oldschool googling leads me to dead ends too, but I started just looking somewhere else again, instead of asking GPT over and over getting the same wrong answers with a confident tone.


tldr: use gpt for non-concrete things that don’t have to be exact, use documentation and google for actual oroblem solving

**u/MarchingNight**（0 分）：
On one hand, I never use ChatGPT for any scripting. I just use wiki's and forums for guidance.

That being said, it *is* a resource. I mean, copy/pasting something in a script blindly probably isn't going to work, but at least he did try to use a different resource other than *you*. In fact, when he tried to find an answer on the internet and it failed, all you did was lookup a different answer on the internet, and this time it just so happened to work. Saying that you wouldn't hire the guy as a full time employee just because he didn't check google first is a poor way to make a decision as important as that.

**u/Nok1a_**（0 分）：
Saying that it´s like saying 20years ago using stackoverflow dont help, because you go there an people give you the answer. If yout inter it´s stupid no matter what tool he is using will still stupid, what I mean chatgpt it´s a great help but does not know how the code in your current situation works and which are the issues/goals you need.

  
I mainly use it, for spelling checking and to explain me stuff, sometimes if Im stuck dont know how to do something I throw it there and not only once have given me a right answer but it give me ideas which is what I need, because I find out stackoverflow it´s useless in a 90% it´s just stupid people measuring their dicks on how fancy or intricate can they do something, instead of helping the people and those who try to help and explain are the few there.

  
You could tell your intern to use chatgpt as a consultation, to explain to him concetps he does not understand or for him to explain the concept to chatgpt and he will tell him if its right or not, something I do quite often when Im not sure if I get a concept or not

**u/_alter-ego_**（1 分）：
I confirm. Its crazy... how they (students and (I guess) employees nowadays) think it would do the job for them... Why would one teach/hire them if it worked that way? They should've tried to play a game of chess against chatGPT first, to clearly see its obvious limits and not take answers for granted truth without heavy double-checking.

**u/Plus-Dust**（1 分）：
I've been (vaguely) concerned that this might be happening. This sinister thing about CGPT is that it basically never admits it doesn't know (I have never gotten it to say that actually), and all it's answers sound convincingly reasonable. If I ask it about technical stuff in a field I don't know very well, like say paleontology, it sounds 100% smartypants to me. It's only when I ask it about CompSci that I can see the parts that are right, the parts that are wrong, and the parts that are "right" but not really best practice.

I use CGPT like a enhanced search engine, and I think that's how it should be used in programming ideally. Sometimes if Google is not turning up exactly what you want, CGPT can get you started on things to Google. For example today I asked it to write a program that plays sound in ALSA in C. I've never worked directly with ALSA before, so this was helpful to get started. Then I looked up the functions it used in the ALSA docs (which are kind of terrible autogened doxygen garbage btw), and fairly significantly refactored it's code into a proper C++ class with threading and a sound queue and everything.

The original program CGPT spit out actually worked the first time, but was doing some shoddy stuff with confusing variable names, an unnecessary memcpy() for every sample frame, etc.

Some of the junior people I've worked with are already outputting questionable code, maybe this can make it better, but I wonder if just being given the answer helps them learn as much, and it's probably better to be learning from good examples rather than mediocre examples in the first place. I know that when something is already working, it's tempting to just wrap it up and not check into what exactly e.g. snd\_pcm\_hw\_params\_calloc() is doing and why it's there.

The other thing I've found CGPT semi-useful for, is to bounce implementation ideas off of when you're stuck. However for the most part, I've found it pretty terrible at data structure design (anything you'd put in a .h file basically), so it's really more like it might say something that gives ME an idea than that it's likely to come up with the perfect solution on it's own. I've accomplished the same thing by just talking to non-programmer friends, really. If you are just learning, doing this may help introduce you to concepts such as hashtables or spanning trees, but don't expect it to come up with an optimum design on these higher-level view kind of tasks -- even though it may not be obvious it's not a great design if you don't have a lot of experience.

**u/Big-Nerve7994**（1 分）：
I am teaching myself programming and I exhaust all possible resources and even then remain skeptical of AI. Not only can it be wrong but often it generates verbose and overcomplicated code whereas I could come up with a much more elegant solution with a little effort on my own part. Degrees are nice but they don't necessarily guarantee a willingness to learn.

**u/Background-Dust8901**（1 分）：
100% agree. About the 6 months ago I was in the same boat where as soon something goes wrong I'll ask GPT and sometimes I'd solve my problems but mostly i'd ending spending more time on it.I decided that I won't go to gpt anymore at least until my search get good, and I did the first month was so harsh others would solve in an hour but it'd take my 6 hours or even today to find and solve and my friends would make fun of me but that was worth.  
  
It the difference I noticed is that my other friends would have no clear idea how the thing works, while on the other hand since I started using StackOverflow i'd solutions but also what prons and cons because on StackOverflow you just don't get solutions but the benefits and other information that real people have used in production ready app.

Now my first go to approach is to just ask google and most of the thing I find instantly

**u/Fit_Rent8519**（1 分）：
LLMs are great, but only for generating templates.

I use them to get me going, but you need to understand what they are doing. They can get your foot in the door, and that’s about it. 

It’s a great tool to refresh on stuff you know, like asking it “what are the key things to remember for (x, y, z) framework” or “compare different hashing algorithms for me”

Sure I can google this, and figure it out from that. But ChatGPT offers a good launch pad to then google from.

**u/candyspace**（1 分）：
I treat ai as a sidekick developer you bounce ideas off but not always rely on everything they say to be “correct”. I agree that the juniors need to just dig through docs more than asking AI for a tldr.

**u/Wild_Leadership7092**（1 分）：
I totally agree. At the end it’s an LLM model and it just gets words nicely sorted together. ChatGPT does not understand the context or even what you tell it to do. At the same time, it could be used as an assistant but not the main character in your life! 
Do not make CHATGPT replace your mind or how you think. It is a virus once you fully depend on it, your brain will stop working.

**u/CClairvoyantt**（1 分）：
Yeah, simple/specific things should definitely be googled. It's guaranteed to waste less time, than wait for gpt to generate an answer. And potentially a false answer at that. Additionally, when you're just learning a concept, you can bet that there's at least one stackoverflow post about it, making the googling really quick. I personally use gpt pretty much only when the context needed to give with the question is way too large for a google query.

**u/Holiday-Locksmith-80**（1 分）：
I absolutely understand this… when I started my coring journey, there was not even Stack Overflow around lol
What I’ve observed is that in uni they also don’t teach the real fundamentals of object oriented languages. If you know how to handle languages like C++ you can handle almost any other modern language out there. What’s more important though, is logical and stable problem solving…

**u/Immediate-Flow-9254**（1 分）：
I think you're right, it's more useful for expert devs who can tell bullshit from real code; although anyone who knows how to double check things should be okay.

**u/Frederic12345678**（1 分）：
I rely on chat gpt google stack overflow. Solving a problem should be the only concern of a SE. People like you bashing on interns because they used chat gpt and delivering this universal truth that who doesn’t use this tools is better it’s just none sense. If fishermen would keep using bear hands while catching fish just because using a fish rod is too easy and you can get a shoe every now and then we would have no sea food on the table at all.

**u/radioactiveoctopi**（1 分）：
Yeah there should be an initial learning phase.  I do use chatgpt but I can tell it when it's wrong....also more so than asking how to do something I'll give it code and ask "why?" "how?" "can this be shortened".  I definitely noticed that it could become a crutch and avoided that over time as I've gotten more familiar.

**u/Teawhymarcsiamwill**（1 分）：
Its interesting  that you found it on Google that quickly and chatgpt wasn't able to find it.

Unfortunately so far I haven't found a problem it couldnt help with. 

Trouble shooting with gpt normally goes:
Ask the question/Provide code.
Try solution
Provide error code.
Try solution again.

If that doesn't work then you'll need to understand it yourself in more detail to break it down for the AI.

Have you face many problems AI couldn't solve?
I'm looking find the limitiations of these tools so I can focus on what they are bad at.

**u/textherun**（1 分）：
well , its good to make your work faster and smother, but for learning NOPE never recommend....

**u/SashaSyrup**（1 分）：
It's absolutely terrible for learning.  It contradicts itself and , more often than not, straight up gets facts completely wrong.

**u/PotatoNeither6272**（1 分）：
I stopped using chatgpt cuz it giving wrong answers for SIMPLE questions!! 2+2= you wont believe 320!!!

**u/WeekendMagus_reddit**（1 分）：
Your intern didn’t want to learn. He wanted to cheat and get the job done.  I’m not judging him, just saying.

**u/Psychological-Bag151**（1 分）：
I think you have to have a basic understanding of the fundamentals and programming patterns before asking chat gpt for any help. This ensures when chat GPT says something wrong you can actually notice it.

**u/stopbreathinggethigh**（1 分）：
Something similar happened to me at school. It was our english exam and we had to prepare a speech. It was stated that we can speak about anything but if we dont have anything to speak about anything, 3 topics would be given. I was nervous so I ended up speaking at the later half and what I observed is that everyone has chatgpt open in their phones asking it to write one of those three topics. All I did tho was head to wikipedia and quickly learn the highlight details about the Kawasaki Ninja ZX4R, then I spoke about it and I passed.

