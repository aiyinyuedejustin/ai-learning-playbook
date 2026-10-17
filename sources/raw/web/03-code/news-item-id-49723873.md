# Learning programming in an age of LLMs（HN 讨论）

- 链接：https://news.ycombinator.com/item?id=49723873
- 作者：moneroloop2018
- 获取方式：Hacker News 帖子与评论全文

---

## Learning Programming in an Age of LLMs（moneroloop2018，263 分）

（讨论共收录 195 条评论，缩进表示回复层级）

原文链接：https://blog.ploeh.dk/2026/09/16/on-learning-programming-in-an-age-of-llms/

**Trusteando**：
IMHO, I think that it could be better if the question about how to learn programming in the age of LLMs were asked to someone who is learning now by using LLMs. Someone who learned programming  thirty years ago can perhaps  give you only one side of the coin, whereas someone learning today  from scratch using LLMs could give you good advice on what the real difficulties are  and where the main drawbacks lie. Combining both views would give a better idea of the landscape.

> **sixtyj**：
> Difficulty is too many technologies available. So a beginner needs something/someone that teaches principles.
> 
> I have realized that simplier (boring) is better. E.g. simple html5  css combo is better instead of trying to navigate in JS frameworks.

> > **lolakutty**：
> > >simple html5 css combo
> > 
> > HTML is not a programming language IMHO. Javascript running in browser is not very interesting either.

> > > **jaapz**：
> > > Javascript running in the browser is an amazing tool to learn programming as everything you need is right there in the program that's already installed anyway.
> > > 
> > > No True Scotsmanning someone over that (especially someone who wants to learn something new) is a bit weird, IMHO

> > > **sixtyj**：
> > > Don’t catch me by word :)
> > > 
> > > Would you prefer starting with compiling a program or running a python script? Imho for beginners it is too heavy, even a python that is so hyped recently.

> > > **raddan**：
> > > As a programming languages researcher I disagree. HTML is not just a programming language (a declarative one), it literally has the word “language” in the name. The world of programming languages is much larger than general purpose languages.
> > > 
> > > Also, whether JavaScript is interesting is a matter of opinion. Given that for a long time it was the only web language, I’d say that makes it interesting. It’s also in my opinion a poorly designed language but that also makes it “interesting” because its behavior is sometimes hard to predict.

> > > > **Izkata**：
> > > > If we're talking about what's in the name, then keep going: it's a language yes, but it's a markup language, not a programming language.

> > > > **rudolftheone**：
> > > > > It’s also in my opinion a poorly designed language but that also makes it “interesting” because its behavior is sometimes hard to predict.
> > > > 
> > > > Following this logic, any broken device is equally interesting as its behavior is sometimes hard to predict, isn't it?

> > > > > **raddan**：
> > > > > Yes

> > > **utopiah**：
> > > > Javascript running in browser is not very interesting either.
> > > 
> > > Damn... that's honestly a shocking thing so say, if only for the fact that you can run in JS other languages. But even then, if you could "only" run JS it gives you access to a high level language but also all kind of inputs, from a keyboard and mouse, obviously, all the way to MIDI, hand tracking in WebXR, etc and all kind of outputs, e.g. screen, obviously, but also 6DoF XR, but you also get low level access to actual hardware. Totally anecdotal but I was precisely in my other browser window accessing my XR headset via adb via ... JavaScript in the browser, thanks to WebUSB. You can also run parallel computations via shaders but also WebGPU. The amount of things you can do is really mind blowing. You mind not like the syntax or some decision about the language itself but that somehow it's not interesting to have access to all that and more from any browser window is just surprising to me.
> > > 
> > > Last but not least, all that is done with 0 installation. You start a device, open the browser window, open the console and voila, you get a development environment instantly.
> > > 
> > > I just find it incredible.

> > > > **lolakutty**：
> > > > To me the Turtle programming language lot more interesting than Javascript in a browser. Sure JS has all the capabilities, but as I child, all I wanted to was to turn pixels on and off on the screen. With *only that knowledge*, and my imagination, I felt I could build whole worlds on the computer.
> > > > 
> > > > That is what makes something interesting and intriguing. Once I had the taste of that first pixel, and I was hooked.
> > > > 
> > > > But look at JS/Canvas stuff? I still need to look up how to put a single pixel on a canvas. I am not sure it is even possible!
> > > > 
> > > > (Btw, do you know that in those times, graphics libs could read the color back from an onscreen pixel? Now I can do collision detection for my games!)
> > > > 
> > > > But you might say "But that is the wrong way!" and "You won't be able to do much that way", Who cares, I want to have *my way*, with out having to do a ton of stuff that is *seemingly* orthogonal to what I am trying to do..

> > > > > **utopiah**：
> > > > > You can have the best of both Worlds today thanks to https://snap.berkeley.edu namely block based visual programming, no syntax error, no installation (even works offline once loaded) and you can make the turtle move... but you don't have to stop there, you can make your own blocks... and those blocks can even be JavaScript so that when you inexorably get bored of what was once an exciting turtle, you can leverage all that but control it with a GamePad or whatever weird things I listed before.
> > > > > 
> > > > > To be clear though, I am NOT advocating for JavaScript, I'm just arguing its potential, today, is nuts.

> > **octantes**：
> > There is something to this.
> > 
> > But I think at least in front-end engineering, the bigger question is what a new dev values.
> > 
> > LLMs make the browser itself easier to understand in depth, if that's something you want. Building in vanilla-everything, no deps, is now doable at speed and scale for beginners too.
> > 
> > Once you understand the web stack and the principles, you can migrate to any framework and understand their "magic" fast. I think that's not a bad learning path at all, if you use it well, and results in a more competent web-dev than the previous pre-LLM cycle produced.
> > 
> > But if the beginner values output aesthetics and speed more than building their mental model, it is possible to spend years building things without developing any understanding.
> > 
> > For me, at least, the more interesting question is how can we make beginners more interested in the former path than the latter.

> **Barrin92**：
> >whereas someone learning today from scratch using LLMs could give you good advice on what the real difficulties are
> 
> if we're talking about the LLM usage as described in the article, they can't do that by definition because they're not learning. You can replace the word "model" in the article with "guy I hired on fiver" and there would be no difference. They outsourced the building of a product.
> 
> If you're having robots lift weights for you at the gym it's a moot point to ask what the real problem with your form is, you don't even have one.
> 
> You can use an LLM as a kind of tutor to ask it questions the same way you'd google, but you can't actually substitute the programming if you want to learn programming

> > **Trusteando**：
> > For example he could tell you about how the LLM destroyed the main database (source of data for him) and  so you should prompt the LLMs for how to avoid losing all your data. Real experiences help but not painless.

**japhyr**：
I'm the author of Python Crash Course, and I got this exact same email this week. I was thinking of writing a public response as well, because any attempt to sincerely answer these questions takes something along the lines of a full post. It's also worth a public response because many people who are getting into programming for the first time right now are asking variations of these same questions.

> Do I think that AI enables people to develop faster than they can keep up?

Absolutely. That's the core of this person's email, and everyone else who asks similar questions. Just five years ago, the only way to build a working project of moderate complexity was to learn the basic to intermediate concepts required to make an MVP. Now, if you can steer an LLM reasonably well, you can quickly build an MVP that goes well beyond your own understanding of the implementation.

I don't think anyone has clear answers to all the questions brought up in this email. I think people can learn faster than they used to, because they can make connections between different areas faster than they used to. But it requires skill and discipline in how you learn, and how you work. You have to intentionally build your understanding as you build your projects.

> **pluc**：
> > I think people can learn faster than they used to
> 
> Agree, but that only applies for people who were experienced developers before AI took over. Let's see in 5-10 years what our caliber looks like when you skip the foundations.

> > **DrewADesign**：
> > If you’re just talking about *learning a programming language*  I think you need to be quite judicious in your AI usage.
> > 
> > In my experience, people learn programming languages best by overcoming frustrating roadblocks. You often end up learning something important, even if it’s just about your mindset or approach, that landed you there. This is the difference between someone with a wet signature on their comp sci diploma and someone with a few years under their belt.
> > 
> > A lot of people start with tutorials and cargo-cult their way through solving their first problems, but eventually need to learn how to do things the tutorial code can’t. It seems like the AI coding tools can could perpetually make things that could be bashed together well enough to sorta solve a problem and think “oh I’ll just learn about that later,” and then never learn about it at all. If your goal is to make some quick tool to help you with something at work in a different field, well, touchdown. If you’re trying to *learn the language,* fail.

> > > **busssard**：
> > > >> If you’re trying to learn the language, fail.
> > > 
> > > AI-coding tools are the deepl/gtranslate of coding.
> > > they might help you understand a foreign website/text better but you wont learn the language with it. and you will continue to be reliant on them until you learn the language. So when you dont have internet access etc.
> > > 
> > > For programming, this was already true for many programmers before LLM. I wasnt able to do much without access to stackoverflow. especially with more complex tasks that i had no experience working with before.
> > > Its one thing to figure out an elegant solution to a concrete task, but often it was remembering integrations, libraries, adapters and packages i dindt often work with.
> > > 
> > > So i agree fully, learning a language takes time. The central question is, why are you learning the language?
> > > for personal development? for understanding the process the LLM is solving for you? for deep optimization?
> > > 
> > > i can do a fluent translation from german to english for my GF, but sometimes its too exhausting and i paste a text into a translator (or llm) and just read the english text.
> > > The same is true for coding. When nuance is important you might want to have a skilled programmer look over what you generated.
> > > 
> > > BTW does anyone use the LLM to directly generate assember code :D

> > > > **testerius**：
> > > > Yes, there is a funny PR in open source project about refactoring source code to assembler code or even machine code 0s and 1s. I do not remember exactly but I remember I LOLed hard when I saw it.

> > > **ahalay-mahalay**：
> > > I’ve seen people here learn programming languages by building a compiler, but my go-to project is usually the ICFP 2006 contest. It has a well defined scope, it is entertaining, gets you into the advanced concepts pretty fast as you debug and optimize performance.

> > > **prajish**：
> > > Completely agree with the failing part. It's in these moments of "failure" and "struggle" that learning actually happens.
> > > Productive failure is a well researched concept in education - https://pubmed.ncbi.nlm.nih.gov/31089856/

> **senko**：
> > *Just five years ago, the only way to build a working project of moderate complexity was to learn the basic to intermediate concepts required to make an MVP.*
> 
> > *Now, if you can steer an LLM reasonably well, you can quickly build an MVP that goes well beyond your own understanding of the implementation.*
> 
> Somewhat agree. Five years ago you could build an MVP without understanding how to open TCP sockets or how to parse HTTP headers. You didn't need to understand relational databases, let alone B-trees or cache locality. You didn't need to know how to install Linux.
> 
> Now you don't need to understand the details of connecting to Stripe or Auth0 or setting up a Kubernetes cluster.
> 
> > You have to intentionally build your understanding as you build your projects.
> 
> Some things you need to understand-others, not so much. Depends on what you're doing, the scale, risks, etc, but that's always been the case.

> > **skydhash**：
> > That’s the power of abstraction when there’s a good API around something to hide the internal that doesn’t matter much at an higher level. You only need ‘open’ and ‘read’ instead of dealing with disk access and file system trasversal.
> > 
> > But those abstraction are deterministic in nature, so there’s a very good guarantee of their behavior. Someone using LLM and not caring about the generated code is just asking for trouble. The code may work, but there’s no guarantee about its behavior (including error handling and edge cases).

> > > **bbmatryoshka**：
> > > non deterministic abstraction are absolutely useful, outside of software sector they have been used since the start of civilization ("a worker" is a very very non deterministic abstraction, outside from the most basic tasks)

> > > > **skydhash**：
> > > > I’m sure that in every case where there such non deterministic abstraction, it’s been always statistically or with a lot of hand waving. So with a heavy dose of expected errors.
> > > > 
> > > > Pro LLM users don’t want to talk about the error margins of whatever practice or product they’re putting out.

> > > > **juvvel**：
> > > > > "a worker" is a very very non deterministic abstraction, outside from the most basic tasks
> > > > 
> > > > Sure but we (usually) don't fool ourselves into believing otherwise. The problem with AI is that it suggests near-perfect intelligence with reproducible results. So many people are not acknowledging the fundamental limitations of LLMs, whereas we all have an intuition for the limitations of humans.

> > > > > **Terr_**：
> > > > > In addition to the reliability/security aspect, there's the claim to expertise and unwarranted confidence. We also don't (usually) fool ourselves into believing that the manager *has gained the skills and expertise* of the worker, simply because they gave abstract orders and a good result was achieved.
> > > > > 
> > > > > In other words, "I can code because I prompt an LLM" is like "I can do metalworking because I sign the paychecks of a blacksmith."

> > > > > > **juvvel**：
> > > > > > Well said!

> > > **falcor84**：
> > > > The code may work, but there’s no guarantee about its behavior (including error handling and edge cases).
> > > 
> > > But the painful reality is that we never had any such guarantees in industry code to begin with; despite decades of writing on software engineering best practices, software from the biggest companies is often bug ridden.
> > > 
> > > My experience might not be representative, but when I do my "old man yells at clouds" routine (which I do multiple times a day), it's a lot more often targeted at Microsoft and Google software than at "vibe coded slop".

> > > > **trey-jones**：
> > > > This is exactly true in my experience.  I find myself trusting the LLM better than I ever trusted a development team to deliver accurate work.  Just like you would managing a team of junior developers, you have to keep an eye on the output, but I think the agent is more transparent about that than your team would be.  And it works faster, and you don't have to deal with emotional meltdown or active sabotage if you criticize in the wrong way.
> > > > 
> > > > The trick for the guy controlling the agent is to know about the gotchas that one would normally encounter when doing the work.  Asking the right questions and mentioning the right things to pay extra attention to can make all the difference.
> > > > 
> > > > I think that's why it will be much more difficult for people to learn how to make software now.  Those of us who have been doing it for years and years have experience that is valuable in steering the LLM.  It will be hard for people new to software to get that same experience.  But then things are changing so quickly right now, everything I just wrote my be irrelevant in a week.

> > > > > **skydhash**：
> > > > > > find myself trusting the LLM better than I ever trusted a development team to deliver accurate work
> > > > > 
> > > > > That’s the main issue. You’re talking about the development side guarante, while the most important is the user side guarantee. There’s a lot of talk about liking LLM interaction, but no comments about the software quality, which for a lot of SaaS has gone downhill. It’s why they emphasized LoC and number of PRs but hide the number of bug tickets.
> > > > > 
> > > > > Which is why the most enthusiastic comments are about projects not released yet. Greenfield and released projects are different.

> > > > > > **Izkata**：
> > > > > > > but no comments about the software quality, which for a lot of SaaS has gone downhill. It’s why they emphasized LoC and number of PRs but hide the number of bug tickets.
> > > > > > 
> > > > > > And here's some numbers (gathered from telemetry over time) showing that: https://www.faros.ai/blog/ai-acceleration-whiplash-takeaways
> > > > > > 
> > > > > > Here's someone's breakdown (with some things from the full report that aren't in the Faros blog post), showing how it's even worse than first impressions: https://unessays.substack.com/p/talk-is-cheap

> > > > **Tanjreeve**：
> > > > >My experience might not be representative, but when I do my "old man yells at clouds" routine (which I do multiple times a day), it's a lot more often targeted at Microsoft and Google software than at "vibe coded slop".
> > > > 
> > > > As in you get more mad at software you actually use being broken than software that you aren't using and just exists in blogposts?

> > > > > **falcor84**：
> > > > > I personally work a lot with vibe coded software, both my own and of others. And I do encounter a lot of issues, but in general they annoy me less than the enterprise engineered ones.

> > > > **NateEag**：
> > > > > it's a lot more often targeted at Microsoft and Google software than at "vibe coded slop".
> > > > 
> > > > What makes you confident the Microsoft and Google software isn't vibecoded slop?
> > > > 
> > > > Certainly Microsoft has made a lot of noise about all their software being LLMgen these years, and also gotten into hot water with their users for Windows 11's crappiness.

> > > > > **falcor84**：
> > > > > Very good point. I would respond that I saw the deterioration several years before vibe coding became a thing, but maybe they did have a head start on the tech.

> > > > > > **Tostino**：
> > > > > > That was them killing the QA team that really kicked off the apparent to end users lack of quality.

> > **aposm**：
> > There's a pretty significant difference there, even in some of the examples you picked to make your point. TCP and HTTP are well defined standards that, for all their flaws, were designed and conceived to be useful abstractions that you didn't need to understand deeply in order to use. The things that LLMs allow novices to skip nowadays aren't designed with that in mind, and generally aren't something you can just skip over without getting yourself into hot water later. If you mess up Stripe or Auth0 setup because you don't understand the implications of the boilerplate the LLM spit out, you can very easily get your whole app compromised or end up on the hook for a lot of fraudulent credit card charges, etc.
> > I see the point you're making and I don't entirely disagree, but I think current iterations of LLM coding tools still make it far too easy for beginners (or even fairly experienced engineers) to convince themselves that a detail falls into the former category of abstractions they can safely skip understanding, when they're very much the latter.

> > > **moomoo11**：
> > > imo that’s a good thing and people will gravitate towards companies that build actually good platforms.
> > > 
> > > with a bunch of competition, the best will be incentivized to not have these noob tier issues.

> > **7speter**：
> > >Now you don't need to understand the details of connecting to Stripe or Auth0 or setting up a Kubernetes cluster.
> > 
> > Ehhh, if you're smart you want to at the very least gloss over the details, and look at the code being generated by whatever model you're using for this solution.

> > **musebox35**：
> > > Some things you need to understand-others, not so much.
> > 
> > This is the core of the matter though, knowing what you need to understand and what you can ignore is the actual programmer's skill. It requires you to have a clear mental picture of both what you are trying to build and what the underlying machine will do when you are finished.
> > 
> > You need to understand the abstractions, but also where they leak, when they won't match reality, and how. This is why knowing computer architecture and assembly helps you to optimize your code even if you are coding in a high level language.
> > 
> > The problem with coding agents is that they are tuned to work on all contexts so they always fill an underspecified request by optimizing the average case and often without stating all the assumptions that they make. So you still need to understand what you specified and what got filled in automagically by the agent. My experience is that they (even the paid frontier models) are poor judges of the most important assumptions they make, which will might be corrected by a prompt or a tool output in which case it is fine. Otherwise it will be ignored and steer the model into a weird loop. It then tries to fix things but can not do so since its mental model is totally broken now.
> > 
> > Do not get me wrong, I am so happy to let the agent handle tool building (especially those that involve a web UI) and fill in the CLI command line argument parser. But every time I trust the agent by relying on it to drive the mental model of what we are doing, I got seriously bitten. Well, maybe that should not be surprise me, but I can understand the confusion of less experienced programmers and non-coders. It must really be frustrating to be able to build so much, but also not to be able to fix seemingly small issues.

> > > **pferde**：
> > > That's just it. *you* didn't "build so much", you didn't build anything. You asked someone (or something) to build it for you.
> > > 
> > > How can people look at LLM-generated code and think "this is mine, I made this" is beyond me.

> > > > **FuckButtons**：
> > > > I’m in two minds about this, in some sense they did and it’s the same way in which the C code I write is mine, but the assembly underneath is an artifact of my intent, but I owe the compiler authors for it. On the other hand the cognitive distance between my C and the assembly is likely lower, but that’s because I’ve spent time staring at what was generated in order to figure out why my code was misbehaving. Which is itself not that dissimilar to figuring out how to get better at writing code with llms.

> > > > > **Terr_**：
> > > > > I think the difference involves how many layers of stuff someone claims is "theirs" and whether that claim of credit and expertise is valid.
> > > > > 
> > > > > Imagine a coworker writes some decent C code, but then at a meeting they start taking credit for the bytecode and the default optimizations done by the compiler.
> > > > > 
> > > > > That's analogous to people who write LLM prompts and then claim the same level of authorship over the code which was all generated and edited on an indirect level.

> > > > > **pferde**：
> > > > > If you ask LLM to code something for you, and you then work on the code, then yes, there is partial ownership. Just like if you had asked another, maybe junior, developer to write a piece of code, and then you helped them make it better.

> > > > **huurtehoog**：
> > > > Agree wholeheartedly.
> > > > 
> > > > I'd like to add: we can't know a priori what will be needed to be known and what can safely remain behind an abstraction you just use.
> > > > 
> > > > That is revealed when our mental models grind against reality. Avoiding that friction at all costs is a problem because it will happen and you'll be unprepared when it becomes unavoidable.
> > > > 
> > > > Trusting some abstractions that have earned it but not all is how we deal with it. Limit your focus, and adapt. If you just trust all abstractions thrown in front of you until something breaks irreparably, you will be (person or organization) between a rock and a hard place and without any knowledge or skill on how to get out of that predicament.
> > > > 
> > > > That to me is the biggest risk in accepting the fallacy of general automation.

> > > **Fr0styMatt88**：
> > > Fixing stuff by driving an LLM to do it seems like a distinct skill unto itself.  It’s kind of this blend of your normal debugging skills, carefully managing what goes into the LLM and carefully constructing your requests.
> > > 
> > > For me at least it’s the one thing that feels like a novel new skill to learn more than anything else.  Normal LLM prompting feels like just an extension of the mental process I’d use when coding and designing in a way that trying to get the LLM to fix things kind of doesn’t.

> > > > **musebox35**：
> > > > I agree that it is a bit weird, kind of coding in natural language but also not exactly like that. Maybe as the agents stabilize and there are proper new tools for this new process we can relax a bit and it will become the new normal. For now it feels like surfing over an ever changing seascape, exciting but tiring at the same time.

> **rickydroll**：
> I suspect my opinion on this won't be very popular, but it's like driving a car. If you're going to learn how to drive four wheels, you should start by taking the motorcycle safety course and learn on two wheels first. We can discuss why later.
> 
> Taking that concept to programming, I wouldn't start with a desktop or a web app. I would start with a little embedded system like an ESP32 or one of the small Raspberry Pi controllers (2350). I've come to this opinion because of the people I've mentored as they improved their code-writing skills. The ones who did best were the ones who started with embedded systems.
> 
> I believe you have to get down and dirty with the machine to understand the code and what it's doing. If you're making a motor controller work, you can use an LLM to generate code using a library or some cut-and-paste MicroPython code. But when it doesn't work, you have to break out the cheapy mini scope you got from Amazon and look at the waveforms.
> 
> Seriously, get your hands dirty at the controller level; understand queues as driven by hardware, not hidden in a library. Or, even simpler: you need to understand why the blinking lights are blinking, but not the way you thought they would.
> 
> If I were writing a course on programming, I would give students deliberately and increasingly wrong cut-and-paste code and leave the solution as an exercise to the reader.

> **ltononro**：
> I think there might be a take on learning with AI vs the pressure to develop fast.
> AI could be an amazing tool to learn.
> But who wants to learn when you had to deliver 3 days ago?
> The corp culture is kind of what is killing it. Not sure how things are going in universities tho.
> If you stop and use it to learn, take time, ask questions. I am sure you can learn a shit ton out of it, most people were learning in the beginning when you had to copy/paste/debug in chatgpt.
> If I had to answer to this, I'd say that learning has become optional, helpful, but optional. Not in the sense that it is not good to learn it (or anything), but in the sense that you need to opt to learn it, and to do so you will have to sacrifice speed.
> Do what I say makes sense?

> > **beej71**：
> > I'd quip this summary, only half tongue-in-cheek: "the goal was never to learn things".

> > > **ltononro**：
> > > well, does it all boil down to capitalism?

> **rgoulter**：
> > Now, if you can steer an LLM reasonably well, you can quickly build an MVP that goes well beyond your own understanding of the implementation.
> 
> Pre-LLM, I'd distinguish between e.g. "I know Python" and "I know this codebase". So if I wrote a codebase in Python I'd be familiar with it, if someone else wrote a codebase in Python I'd be familiar with the Python. -- An LLM coding agent can give a codebase in Python very quickly.
> 
> With a newbie, they'd be familiar with neither; but an LLM coding agent can give them a full solution written in Python.
> 
> I'd say that this power from LLM coding agents blurs the distinction, in some sense. But to an extent it's always been the case that abstractions allow programming without a *full* understanding of everything down to atoms.
> 
> People 'can' learn faster than they used to. But I'd think those who are curious to learn will be able to have better results than those who only have a shallow understanding.

**dingdongditchme**：
I think bill gates summarized it pretty well in a recent letter [1]. There are pro's and con's to every new technology. Learning can be greatly accelerated with the use of llm's but you have to use them the right way. Just like calculators help further down the line, they do not help you when you are still trying to learn the basic concepts of arithmetic. I personally think I have found a way of working with llms that really accelerates getting stuff done while i am still able to learn. It means reading more, and (although I hate this in part) reading generated text. What is infuriating is when I suspect people writing to me with generated text, it is insulting and should be banned. Makes me want to spend more time offline (probably a good thing in my case).

[1]https://www.gatesnotes.com/home/home-page-topic/reader/a-turbulent-ai-era-and-critical-choices-to-make

> **cicko**：
> I'm sure people said the same thing about fire, some 100s of 1000s of years ago.

> > **dingdongditchme**：
> > certainly! There are pro's and con's to fire still today. Us fireless plebs prefer a life much closer to nature, eating our meat raw and bathing in the mud.

**Razengan**：
I said this in different ways before and got shoveled because of the way I said it:

None of us know how to farm, not even the chefs who cook for us at a restaurant or fast food joint, but we eat every day and nobody's going around making people feel guilty about not knowing how to till soil and sow seeds..

In programming and other creativity, most people's skills will [have to] change/evolve into managing, directing, dictating, knowing what you want, describing it, and focusing on the end product and iterating,

instead of wrestling with why the f is a string a pointer to a pointer to a character

just like we don't track the phases of the moon and seasonal rainfall before we can have a nice salad to eat.

> **latexr**：
> > I said this in different ways before and got shoveled because of the way I said it
> 
> Are you sure that was the problem? Because to me it seems like it’s the argument which doesn’t hold. You’re engaging in what is called a False Equivalence.
> 
> https://en.wikipedia.org/wiki/False_equivalence
> 
> Those things are not the same. Crucially, the food you buy at the store or restaurant is heavily regulated, provenance established, safety checks in place. When there’s a widespread issue, we have systems in place for recalls. The differences don’t stop there, and you can’t ignore them just because the processes so ingrained and well established that you forget they’re there.

> > **skydhash**：
> > > the food you buy at the store or restaurant is heavily regulated, provenance established, safety checks in place. When there’s a widespread issue, we have systems in place for recalls
> > 
> > I live in a country where those things are not regulated and you have to be really careful to not buy something that would send you to the hospital.

> > > **latexr**：
> > > And would you not agree that is a bad thing?

> > **Razengan**：
> > > *False Equivalence* or whatever
> > 
> > So is claiming "if people don't keep learning the absolute basics about everything they'll be stupid and useless"
> > 
> > Bruh we don't know shit about farming, how to milk an animal, we don't know how to mine, how to smelt ore, yet every day we enjoy the benefits of other people or machines doing those activities.
> > 
> > None of those people go around chastising us the way "real coders" are doing now. Though when automation entered their profession they probably grumbled similarly too… or did they? or were they glad of having to do such jobs a little less often?

> > > **latexr**：
> > > > So is claiming "if people don't keep learning the absolute basics about everything they'll be stupid and useless"
> > > 
> > > That’s not a false equivalence, there’s nothing being compared there. Also, I have no idea who you’re quoting, but it sure as hell isn’t me and I can’t find a match online for that phrase. Looks like a straw man argument.
> > > 
> > > > Bruh we don't know shit about
> > > 
> > > I’m not your “bruh”, and when you say *we* you mean *you*. Either way, you’re just rehashing the same false equivalence despite saying “so is” (implying you do think the first argument is indeed a false equivalence) so I have no idea why you’re back to that.

> **amelius**：
> Yeah but should programming issues become "how can I be more friendly to the waiter so they give me what I want?"
> 
> That's not what I want programming to become. I'd choose a different profession then. Maybe I'd become a surgeon because the AI labs haven't cracked robotics yet. And the people in general look up to surgeons and down to IT people, but that's another story.

> > **unified101**：
> > Sadly, you will have to choose another profession, and as your example shows, the better paying ones need 10 years of gruntwork to get there.

> **xeyownt**：
> In which language a string would be a pointer to a pointer to a character?
> 
> Even in C, string literals are simply a sequence of null-terminated char, no pointer involved.

> > **Razengan**：
> > fuck idk man what I was thinking lol (or I saw `char *` but don't remember where) but this shit is on the same level as the "a monad is just a monoid in the category of endofunctors" meme by now
> > 
> > See I'm a full-time coder (since before AI) and even I'm not sure about this shit! I didn't need to be!
> > 
> > Is every professional programmer who doesn't know assembly language and machine code today "dumb"?
> > 
> > Just accept that as technology moves on, some basic essentials become "baked" into the tools we use, and at the end of the day all that matters is what you make with it.
> > 
> > It's OK to use a fork without learning how to mine and smelt ore first.

> > **BlueGreenMagick**：
> > I'm being pedantic, but JavaScript string is often internally implemented using Ropes, which is arguably a pointer to a pointer to a character.

> **diehunde**：
> That’s one of the worst analogies I’ve seen lately

> **derpyzza**：
> ...string's aren't a pointer to a pointer to a character. they're pointers to characters directly.
> 
> maybe you need to wrestle with that concept some more...

**duendefm**：
I'm a software engineer, I do software development but also system maintenance, and I do handle networking and telephony systems, and work with some juniors. Working with AI is problematic. It can speed up you but at the same time delay you. For the system maintenance part sometimes you need to do a lot of stuff fast and in various machines and you can't just count on a cloud based AI oracle  (that takes time) to do your job for you. And the same time, the more you use it as a oracle, the less competent you get. If you are an expert, I would say in any area, you do benefit from using AI as a tool but it easily can become a double edged sword and make you less proficient. For juniors, it can make them rapidly produce stuff that is impressive and works ok for sites and some visual stuff, but it's impossible for a junior to become an expert if they get stuck in the AI using loop. For AI to cause a clean impact, I would say that we would have to live in a world where software engineering didn't matter. That is, the choice of databases, high availability systems, the programming languages themselves.

> **bigfishrunning**：
> > we would have to live in a world where software engineering didn't matter.
> 
> As an engineer who works very hard to do the right thing, I'm beginning to worry that software engineering doesn't matter. I write code that i think about a lot, understanding every line. It's not perfect, but I try to make sure my code is maintainable and well structured. I work much slower then my colleagues who produce unmaintainable slop at an alarming rate. In my career, no customer has ever complained about code structure or quality. It feels like I'm sinking in quicksand in an industry that's dying.

> > **duendefm**：
> > It's not about what the customer complains or notices at short term, is about having a quality system that can be augmented without accumulating same kind of debt. I can give a simple example. I have a coder here that filled the crontab of a server with periodic tasks. One of them was doing +200 failed requests per second and shutdown one of our routers. The router wrote so much logs that it changed the health of its internal disk from 15% to 85%. He doesn't even know what the crontab is. This kind of stuff is bound to happen more and more because the more you use AI to vibe, the more disconnected you get from the technology. And that's why I say, the only way that yolo vibecoding could work is if the base stuff didn't matter.

> > > **bigfishrunning**：
> > > > It's not about what the customer complains or notices at short term, is about having a quality system that can be augmented without accumulating same kind of debt.
> > > 
> > > I agree with this wholeheartedly, but convincing nontechnical management of this fact has been extremely difficult. It was hard in the days of the stackoverflow copy-paste monkeys, and it's even harder in the age of LLMs.

> > > > **juvvel**：
> > > > Some people cannot be convinced of this, but some can, as long as you don't use technical language to describe the issue. Essentially, instead of saying "we need to prevent technical debt and have a maintainable software architecture" one needs to say stuff like "software quality enables a faster time-to-market for new features and less customer churn". i.e. put it in business-y terms.

> > > > > **sanderjd**：
> > > > > Yes, but then it's really important to demonstrate that this is true. If they invest in what you propose, time to market for new features needs to actually become faster, or customer churn needs to actually decrease. It's not enough to put the proposal in business-y terms, it has to actually effect the claimed improvements to the business.

> > > > **sanderjd**：
> > > > You have to pick metrics to show management that they understand the importance of, and then be able to demonstrate degradation in those metrics when you don't do what you propose, and improvements when you do. Accomplish this and you'll build trust.
> > > > 
> > > > Too often, what happens is that the proposed benefit is vague and not empirical, and then the benefit is not actually realized by a large investment into it, destroying trust.

> > **juvvel**：
> > Of course customers do not care about code quality in and of itself. Just like they don't inherently care about the type of seam used for a garment. But they do care if their clothes fall apart after two washes. People care if software is buggy or slow or becomes harder to use or more expensive over time. And the way we know how to mitigate that is by ensuring code quality (it's definitely not the only factor, but an important one).

> > **PaulStatezny**：
> > Agree and disagree.
> > 
> > There have always been software companies that care about quality, and those that don't.
> > 
> > Many who don't care about quality exist because their products are forced onto their users. (Due to footholds from enterprise relationships, regulation, etc.) I bet slop will abound in these kinds of companies, but their codebases and products were already terrible anyways.
> > 
> > ---
> > 
> > But research reliably shows users do care about things Just Working™ and feeling polished. With few exceptions, if software feels *at all* buggy or doesn't look visually amazing, you won't acquire/retain that many users.
> > 
> > Natural selection will teach hard lessons to the industry. Customers will notice things feeling "off" on products where AI slop is allowed to abound, and they'll flee to companies with sane approaches.
> > 
> > A sane approach: Humans actually guide the direction of the code which means they have to understand + review the code and course correct bad decisions. This doesn't mean agentic coding goes away, but it means this mad rush for insane velocity goes away.
> > 
> > ---
> > 
> > Compare vibe-coded apps you've interacted with against world-class polished apps like Spotify, Gmail, Slack, etc. Those apps aren't obviously showing signs of AI slop, because the organizational structure is in place in those companies to prevent engineers from just throwing slop over the fence. Those engineers are doing agentic coding but are being forced to go at a sustainable pace.
> > 
> > The industry will eventually be forced (by the reality of business results) to recognize that this is the only approach that will lead to success.

> > **sanderjd**：
> > Sometimes it matters and sometimes it doesn't. The hard part is figuring out which is which. The most effective engineers are those who maximize the amount of time they spend picking the right point in the trade-off at the right times. Choosing a preferred point on the continuum and sticking to that at all times simplifies decision making (itself a useful thing!) but it's not the optimal strategy.
> > 
> > There are a couple ways out of this conundrum. One is to try to get really good at picking the right point on the continuum as much as possible, which is essentially a forecasting problem (and thus it's really hard!). I think the somewhat easier choice is to pick roles that align well with your style. If you have a deliberate and near-perfection preference, you can seek to work on projects where there is no question of the importance of correctness. If you prefer the opposite, you can work on prototypes and zero-to-one type projects, and that will be more satisfying (and less catastrophic).

> **throwaway219450**：
> I think it's more about inertia than anything else. I know the dishwasher will take less than 5 minutes to unload, but I put it off anyway. Problem is the AI can take action immediately, and that's very alluring. I'm sure there's research on exactly where that breakpoint lies. My current goal is to try and spend 15-30 minutes attempting to solve a task when I feel myself reaching for the AI.
> 
> One of three things tends to happen. Often it's something that is resolved in a matter of minutes, in which case it was laziness. Or, it's something that will take more time, say up to an hour, but the act of starting has conferred a sense of ownership that I don't want to give up to an LLM. Else, it looks like a much more complex problem and worth re-assessing, and potentially brainstorming with a model.

**AnodicElegy**：
"The same kind of argument was used when China was admitted to the World Trade Organization. And indeed, lots of new jobs were created, just not in the Western world."

China's entry into the WTO is really not a good evidentiary example for AI causing mass unemployment. Unemployment in the U.S. had already been increasing at the time, peaked soon after, decreased to well below the point it had been at China's entry, and only went up again during the Great Financial Crisis, which had nothing -- or at least very little -- to do with competition from China. That's not to say that jobs weren't lost, even en masse, but they were replaced, and U.S. unemployment has been near record lows in recent years. China's WTO entry is a supporting point, not a counterpoint, to the idea that jobs lost to AI will be replaced by new ones.

https://fred.stlouisfed.org/series/UNRATE

> **wuisce**：
> > That's not to say that jobs weren't lost, even en masse, but they were replaced
> 
> That's what the article was implying with:
> 
> >  Yes, new jobs were created, but often not for those people who lost their jobs. Coal miners didn't just become programmers overnight.
> 
> The point is that middle-income (industrial) jobs were replaced with less, higher-income (service/knowledge/advanced industrial) jobs, with virtually zero overlap between the two in terms of workers. This is why certain regions across the West (US Rust belt, Northern England etc.) were devastated and have become so immiserated.

**lordnacho**：
I think it's still important for young people to learn coding without the LLM. they need to see the little pieces before they can build big structures. It will be like calculators, just on a bigger scale: you learn how arithmetic works, and then you rely on the calculator when you are multiplying large numbers.

My guess is it will probably take some time to incorporate LLM use into education. People who are graduating right now have a problem, being between two worlds. Those graduating in a few years might have chance to figure out what to do.

> I may have built a system that is above my own level of understanding

If I venture into an unknown area, I end up where the letter-writer ends up when he is visiting programming. Suppose I am curious about an advanced math topic, like Navier-Stokes. The LLM's answer to the news about the new advance last week is strewn with words I don't understand. Asking about anything produces another essay with more things, a loop that never closes. If it were my specialist area, I imagine I would eventually hit some point where the explanation connects to something familiar.

I think this is the wall people run into when they don't have the fundamentals. You eventually get to a point where the machine is asking you for decisions that you won't know the consequences of, and when you are trying to clarify, you end up in a massive rabbit hole. It's not that different from asking a real expert about their area, they will eventually ask you to clarify something that means something to them, but not to you.

I learned programming the slow way. I would run into phrases like "memory barrier" or "green thread" and find an article using the keywords, which led to more searches, which led to more...

There are also many false dawns. Early on, after some success writing some trading strategies, I thought I had it, in the sense that I would be able to write any program required. But it wasn't true, I would run into an iceberg from time to time. Huge areas of knowledge that I hadn't come across.

Obviously I'm not claiming I finally know everything, but LLMs have arrived at a very convenient time for me. For the things I build, there is rarely anything that I don't understand at a fundamental level. When it asks me something, it's an incidental question: what decision should we make? What are the superficial changes that are needed to fit the architecture to the desired product?

I am essentially using LLM as a very quick junior, who knows how the OS works well enough to compile things and analyze logs. These are things that would take a lot of attention in the old days because they can break on very small errors, but the direction was known from the start, and thus for me (having paid the learning cost already) it is just a matter of waiting for the AI to get the code into the desired state.

I have a somewhat usable experience. I was asked to build a trading system a few years ago, which would connect to certain exchanges and show an orderbook. This kind of thing is bread and butter, but writing it up at a new firm would still take weeks.

In recent engagements, I've simply declaratively told the LLM what properties I wanted to see in the solution, waited, and answered a few questions. Since the architecture is the same, there weren't a lot of real decisions. The time difference is immense.

**MichaelRo**：
>> "About a year ago I became fascinated by AI-assisted programming. Despite having no formal CS background, with LLMs I managed to build a fairly large TypeScript/JavaScript system [...] At first it felt almost magical: [...]

It's comical how these people claim first person: "I built". Look: having a LLM shit you some code is in no way different than paying some third world country dude on Upwork 5 bucks to build you "a Facebook clone" or whatever preposterous claim of grand software. In fact at this point it's cheaper to pay that third world country team than a LLM.

And yet before the advent of LLMs noone ordering a job on Upwork was delusional enough to claim "I built it". Although it's the same magical process, like the magic ring in fairy stories. You put the ring on your finger, rotate it and make a wish and the ring makes it appear. Well, for 5 bucks or something.

But nowadays every half witted retard with 50 bucks to spend goes to a LLM and has some "Facebook clone" spitted out and claims "I BUILT THIS!". You haven't built shit, and you know nothing!

Fortunately, reality strikes sooner or later but boy am I tired of Lord of The rings claims.

**lolakutty**：
Sorry, programming is still fun. LLMs can't change that.

> **unified101**：
> I'm curious - how do you explain the fact that as you look all around you, lesser number of devs are having fun?

> > **klausa**：
> > Because their job stopped, to a large degree, involving programming.

> > **dragonelite**：
> > Because for a lot of millenials and older developers coding/making thing by hand was the fun part. The endless meetings, scrum rituals, code reviews etc were the annoying parts of the job.
> > 
> > Now they took away coding by hand, so what's there to enjoy? In a field that was already sensitive to burn out and churn taking the joy from the daily routine doesn't help with that.
> > 
> > Only thing you can do is get in build something for 2 years hope you got bought by big tech before the pile of slop code collapses on itself.

> > > **asp_hornet**：
> > > > The endless meetings, scrum rituals, code reviews etc were the annoying parts of the job.
> > > 
> > > Those are all self inflicted and not a necessary part of the job.

> > **johnnyanmac**：
> > It has less to do with the devs having fun at their job and more to do with if they'll even wake up to go to their job tomorrow. Layoffs are never fun.

> > **utopiah**：
> > Maybe you are thinking of programming at work. If so it might be legitimate but that's not what they addressed, they didn't say programming at work is fun.

> **asp_hornet**：
> I agree. Possibly more fun than ever. Bugs are being caught earlier through AI review, higher quality and quantity of tests, features are going out faster, bad decisions can be easily course corrected and bike shedding is dropping dramatically.
> 
> I miss the romanticism of trad coding but shipping better solutions to my customers was the goal. Hard to argue things aren’t better when AI is used intelligently by experienced people.

> > **sashank_1509**：
> > > I miss the romanticism of trad coding but shipping better solutions to my customers was the goal.
> > 
> > True, every child grows up with the dream of maximizing shareholder value, I’m so glad they can achieve that now. /s

> > > **asp_hornet**：
> > > Ok. Replace “customer” with “end user”

> **gps372**：
> Fully agree. With LLM being able to solve every problem, getting deep into a problem all by yourself becomes a passion side project. Now might be a real test of how much you love programming.
> 
> Your enterprise wants the work done, done fast and reliably. Your productivity goals have increased, just like invention of motors would increased goals of carriers who were earlier doing their job via more manual efforts like pedaling. But still people love cycling, but they largely "don't have to" rely on it to do their job.
> 
> Similarly, now you simply don't have a dependency to love programming to increase your productivity.

> **vasvir**：
> I certainly hope so.
> 
> But LLMs do not need to change that. Sufficient marketing can change the perception of decision takers and middle managers to: Oooh, they can do that.
> 
> That is all that it takes.

**cortic**：
>I may have built a system that is above my own level of understanding.

I feel like that about a lot of code i did myself;  If you don't structure things very logically and really think about your comments;  A few months or years will leave you with a hell of a learning curve to understand what you created.

AI actually helps with this, if you have the right prompt injections.  I feel like the correct way to handle AI is to take a step back in abstracting problems.

I'm very use to collapsing subroutines to make things readable, maybe even further back from this though, the issue is words become too vague to be useful at these scales.

**mentos**：
My biggest issue with halting AI progress right now is we are in a dangerous place where AI is only just good enough to be dangerous. So I see an argument to continue development until its competent to depend on.

> **Calazon**：
> The problem is that by default progress might look like an increase in power without a corresponding increase in safety. That could be catastrophically dangerous.

**sreekanth850**：
I'm doing this. After getting started with LLM coding, I became super interested in learning to code, just out of passion. I walked out of engineering thinking physics was elite, but now I understand how passionate I am about building things, and how boring quantum mechanics was. Better late than never.

**SK35**：
ai will mitigate but not fully remove coders

**altern8**：
It was much easier in the Age of Empires II Expansion Edition. Miss those times, too... :-/

**dude250711**：
*"...I'd seriously consider learning carpentry, metalworking, gun-smithing..."*

Those sound like hobbies? Outside of apocalyptic/utopian scenarios that is.

> **Calazon**：
> They'd be hobbies in most utopian scenarios too.

**bborud**：
I am starting to see how many developers actually need to re-learn programming in the age of LLMs.

A while back Claude went down in the middle of a somewhat frantic initial deployment of a product to production at a company where a friend of mine works.  And suddenly nobody was able to do anything.  Because nobody had actually read the code and had no idea how it worked.

So essentially: much of their day to day work now depends entirely on the availability of a couple of frontier LLMs.

**Aldipower**：
I still differentiate between code monkeys, coders, programmers, hackers and software developers/engineers. Software development is not coding alone, you need to follow best practices and principles to create a stable, maintainable and trustworthy product, one that _you_ or your company owns. Maybe "code monkeys" (which is a minority) are replaceable. But for now, LLM cannot have a wider vision for your products future. The willingness of building something durable is totally human. To make this possible professional software developers are still mandatory and they will be for a long time. And yes, I think is it possible to learn those best practice and principle without coding. But I think this is very hard and boring.

> **skydhash**：
> Building software for me has always been about creatin a set of concepts (data structures, basic behaviors) out of the primitives of the platform (language, libraries,…) and then coordinate their behavior according to the requirements.
> 
> Based on comments here, LLM users belong in two categories: Those that don’t understand the previous paragraph and those that believe they can get the concepts and coordination out of prompts and specs.
> 
> But for both of them, there’s a common trait, which is not caring about maintenance. And you can observe this today where most AI projects either don’t survive the public release or have to revert to more traditional methods.

**jdw64**：
Programming education in the LLM era will be different from what it is now. Many of the learning methods emerging now are the practices of a "good senior programmer."

But realistically speaking, choosing LLM programming ultimately means pouring out an enormous amount of code, and it's difficult to verify all of it. Common sense says that if you produce 10,000 lines in an hour, you can't read all of it, and even if you do read it, you'd have to rewrite it. The problem is that LLM code differs from human abstraction. Or more precisely, it lacks a programmer's habits, so it's hard for me to maintain.

Clearly, programming in the LLM era will be different. The problem is that I can't get a sense of what that way of doing things actually is.

I think that low-priority frontend work will probably be handled by LLMs, while only complex animation work will be handled by humans, and humans will end up working only on things like payment modules, which are hard to fix if something actually goes wrong.

LLMs are now better at optimization than most people.

**jokoon**：
As long as you have critical thinking, it's fine.

So I would say it accentuates the gap between good developers and bad ones.

A sharp sense for logic and causality etc is what differentiates.

**mintflow**：
Recently I start to do some hobby project by learning Common Lisp to understand more about the libraries I used on app

I read the document and sometimes use LLM as a quick search engine because I am tired of every query on google that use AI to summarize

The project goes slowly but seems the basics I grasped over the years help a lot

So perhaps it still worth to learn by hand with trial and fail

I agreed with the author that one must learn deep above the abstraction and I truely think programming still a thing even the agentic coding is getting powerful

**jijji**：
AI LLM systems, i.e. perplexity.ai, are very good at tutoring someone about how something works, i.e. advanced math, and when done in a loop can be very useful at tutoring, better than youtube videos I've seen on the same subject.  The one thing I will usually request in (in the case of math), is to suffix the prompt with "explain this in terms a 9th grader would understand", and this is good enough to explain something in simpler terms with various breakdowns that can be understood by anyone to tutor yourself in alot of subjects using this method.  This can be applied to programming, auto repair, construction, almost any subject at this point.

**0xbadcafebee**：
For those struggling with the idea of staying relevant as a human programmer, think about other jobs first. What jobs are there today that humans work on, despite technology making humans obsolete?

Mostly humans are replaced at physical labor (although even then not entirely). Human computers and punchcard operators, switchboard and telegraph operators, typesetters/letterpress/linotype operators, draftsmen, photo retouchers, film developers and projectionists, pneumatic tube operators, record-pressing/mastering engineers, the horse-drawn transportation industry, handloom weavers and embroiderers, coopers, wheelwrights, blacksmiths, key cutters, bookkeepers, payroll clerks, proofreaders... This is just a tiny list.

Technology replaces the least efficient parts first, and humans remain to do things that're harder or more expensive to automate safely or reliably. A human who used to build something by hand, transitions to a human who operates a machine to build, then designs or prepares work for the machine, and finally maintains the machine that does it all. For many automated jobs, people now perform maintenance, operations, or design work, that could be done by machine, but we either require or prefer a human do it.

For those remaining jobs, you often still need special skills. But it's no longer a herculean task to perform the work, and the jobs are more specialized and less skilled in general. We still need those jobs, or those automated things simply wouldn't function. Someone has to build them, someone has to maintain them, and someone has to operate them, and each of those requires skill.

So human programmers, systems engineers, designers, architects, operators, etc, will all be very necessary over the next 50 years. You will still need to know the languages, compilers, networks, computers, etc work. You just won't be manually typesetting anymore, or manually weaving the digital cloth. Someone will need to get into the guts of the machine from time to time.

**js8**：
I answered this to myself - stop worrying about LLMs. It's pretty simple: due to Curry-Howard isomorphism, programming languages are just notations for some type of formal logic.

Now ask yourself a question, what language do you want to maintain the programs in? Do you think natural language is going to be easier and more maintainable than formal logic?

The answer is no. So you need programmers, people who can read the formal description and adapt it to new requirements.

LLMs are amazing technology, but the truth is - natural language just kinda sucks. Therefore, you don't really need them (see also https://en.wikipedia.org/wiki/AI_effect ).

I think people love LLMs for the same reasons they love magicians. But just like the magician employs a hidden trick, LLM just runs some algorithm you don't see or understand.

So worrying about LLMs taking programming job is kinda like worrying that a magician will take a warehouse worker job, because they can levitate stuff. Meanwhile, we already have automated programmer - it's called a compiler.

> **jappgar**：
> No offense, but "natural language sucks" is the refuge of the illiterate logician.
> 
> Complex language is clearly superior in nature. We're now finding out that that is true in computation as well.

> > **js8**：
> > I am not sure what your counterargument is. But in mathematics and computation, people have tried for at least 150 years to move away from natural language, and figure out stable foundations that can be externalized. I think there is a good reason for that - you save time correcting errors due to different interpretation.

> > **mrits**：
> > Extraneous and ambiguous is superior? Or are you talking about hypothetical new spoken languages?

> > > **jappgar**：
> > > Yes. Ambiguity is a feature, not a bug.

> > > > **osmukka**：
> > > > Isn't code supposed to be exact? Pretty much the opposite of ambiguous.

> > > > **mrits**：
> > > > I don't think it's a feature or a bug. It is an indicator of an extremely poor spec though.

> > > > **datsci_est_2015**：
> > > > Yes all of my the customers of my accounting software love the ambiguity of how it will react to them processing entries.
> > > > 
> > > > You’re not saying anything with substance, but I guess that’s not surprising given your stance on LLMs.

> > **johnnyanmac**：
> > We are in fact finding out precisely why natural language sucks in real time, as we have all kinds of catastrophic errors with people who think this is finally the time for complex language to prevail over pesky nerd language. The only difference is that more people seem to prescribe to the "you're holding it wrong" handwave when said catastrophes are pointed out.

> > > **jappgar**：
> > > Plenty of catastrophes are available under pure logic as well. The only catastrophes they prevent are accidental ones.
> > > 
> > > Natural language can build civilization around "do unto others as you would have done unto you".
> > > 
> > > Logic cannot encode morality, precisely because it is unambiguous.

> > > > **johnnyanmac**：
> > > > You are right, and that is precisely the issue. When complex logic fails, we don't usually blame the machine. When natural language fails, we as of late seem to be trying to anthropomorphize a machine that cannot be held accountable. As if understanding natural language suddenly means it understands morals.

> > > > **ux266478**：
> > > > I can appreciate your original point, but this degenerated into naivete. The is-ought problem exists in (and was formulated for) natural language, and ambiguous formal languages are childsplay. There are further problems (ignorance of the consequences of reality being finite, misunderstanding the operative layers of interpretation) but these two alone are disastrous by themselves. Don't mix up convention with implicit substance. There's a very basic philosophical lesson you're missing, and I'll let you in on the secret: The labels aren't actually descriptions of any property. The distinction is indoor baseball. Notations, syntax, semantics. What you want is signal, and you can transmit that any way you want. Writing and drawing were once the same thing. Still are.

> > **juvvel**：
> > Well, almost all scientific domains have developed a form of structured and formal language, because natural language is too ambiguous. There's "code" everywhere, not just in programming.

> > **lioeters**：
> > No offense but you're just making statements without backing it up with anything. "Clearly superior", "finding out that is true"..
> > 
> > How are you going to prove what you said? Natural language is not enough for that purpose. You need formal logic, quantifications, specifications, the foundation of programming. Superior to what, and according to what metrics? What truth in computation are you talking about, and how can we know and confirm it? Not with natural language, but with numbers, mathematics, the building blocks of logic.

> > > **jappgar**：
> > > Superior just means "above" or "on top of". Natural animals don't communicate in logical terms, even if their dna is a logical sequence.

> **0x445442**：
> I agree with this but what I've been trying to answer the last few months is if there was an optimal language for the spec. As with you, I don't think it's English Markdown, but I don't think it's Java either. I also don't think it's Gherkin, Lisp perhaps? I'm still searching.

> > **js8**：
> > Well.. I think this is a big open problem in philosophy.
> > 
> > On one hand, you have things like Lean (calculus of inductive constructions), these are relatively simple formal logics (just in more practical notation) that let you define any conceivable type, which is akin to specification.
> > 
> > On the other hand, there is a rich set of modal and fuzzy logics that can help with aspects of reasoning in natural language. I think these can be defined in the former, but nobody has really made a good agreement as to how.
> > 
> > So the main difficulty is for any such language to gain traction, people who speak it.
> > 
> > Instead, we trained LLMs and they came up with something (evolved to reason). I think the future philosophical research will need to answer what exactly do LLMs bring to the table in terms of formalization of natural language.

> > **layer8**：
> > In any case, it should be a formal language, and we haven’t finished exploring that space. I don’t expect that we will have anytime soon.

> **jeremyjh**：
> LLMs do not execute natural language. Natural language describes a problem or request, and LLMs generate and test formal logic they predict will satisfy the request.

> > **js8**：
> > I disagree with each sentence for a different reason.
> > 
> > LLMs interpret (so, "execute" in a way) natural language in the sense they have internal logic that assigns to the sequence of tokens in context a next token. If we delineate the input and output  into a series of logical statements, we can think of it as a program that builds a logical statement from a list of input statements. So it encodes derivation in some logical system.
> > 
> > However, the internal logical system is informal in the sense that the above rules are not guaranteed to be sound on the fragment of classical logic encoded in the natural language. It is a close approximation, though, so it often works.
> > 
> > To add, half of my problem with natural language would be resolved by agreeing on exact definitions, which is kinda what LLMs do internally. However, they don't surface this formalization very well(even with open weights it's difficult), which makes it pretty unusable.

> > > **jeremyjh**：
> > > > LLMs interpret (so, "execute" in a way) natural language
> > > 
> > > You could say the same thing about human programmers, but I've never heard anyone say they think that programmers "execute" Jira tickets.
> > > 
> > > >  they have internal logic that assigns to the sequence of tokens in context a next token.
> > > 
> > > I don't think this means what you think it means, because it has almost no information content relevant to what we're discussing. The probabilities that are most relevant at the level we're discussing are satisfying a reward function from post-training, which approximates to:
> > > 
> > > "What is the likelihood the solution the agent is pursuing will be marked correct by the automated grader based on the full prompt and other context provided?"
> > > 
> > > It still has to predict the next token but that isn't based on a likelihood of that token appearing in a corpus of internet text consumed in pretraining. That was eons ago. Every predicted token is shaped by the probabilities of the *predicted solution*, which must already be very specific and shaped completely by the request and associated context that is built during investigation of the same.

> > > > **js8**：
> > > > "You could say the same thing about human programmers, but I've never heard anyone say they think that programmers "execute" Jira tickets."
> > > > 
> > > > Yes I could. We have "executives", for starters. And first "computers" were actual humans.
> > > > 
> > > > "That was eons ago."
> > > > 
> > > > Yes, technically I should call them LRMs (large reasoning models) not LLMs. But that doesn't seem relevant here, to my point they encode some logic (which we want to be close to classical logic, i.e. behavior of words like "true", "and", "not" and so on matches).

> > > > > **jeremyjh**：
> > > > > That isn't what executives do, and I'm not talking about semantics. If you believe that the term "token predictor" has any relevance when discussing the capabilities of these models, you are misinformed. That is the inner, inner loop and it is simply the substrate through which reasoning and action is expressed.

> > > > > > **js8**：
> > > > > > I agree with the 2nd sentence onwards, and I think I expressed it in the other comments I made here. I am not really sure what was your point about "execution", though. Humans might have inner interpreter loops as well.

> > **layer8**：
> > When you want to change the resulting program (“formal logic”), you generally don’t change the prompt and regenerate everything (like you would do with source code). Instead, you provide new natural-language instructions to have the LLM perform the change. This means that you don’t have a reproducible specification *on the level where you are describing the specification*. Therefore the thing that you are maintaining is not a natural-language artifact, it’s effectively still the formal description (program code).
> > 
> > And that’s why the parent comment is saying that we need people that understand the thing that is being maintained, i.e. the program code, which is the source of truth about what is being maintained.

> > > **jeremyjh**：
> > > > we need people that understand the thing that is being maintained
> > > 
> > > We do for a lot of software today, but not all of it. I think in a year we'll need them for less, but I'm not sure how much less.
> > > 
> > > This claim isn't supported or justified by talking about natural language versus formal language. For the last 50 years or so the people shaping a lot of software in the most important ways are often using *only* natural language.
> > > 
> > > The product manager doesn't understand the code today. They write PRDs and Jira tickets and comments in Slack, and software comes out. They have people test the software, report bugs, more software comes out. Eventually they decide its close enough to their vision to ship, without ever understanding or looking at any of the code. They can do that with human programmers or agent programmers. The former holds up better in larger systems, but I don't see any evidence for the proposition that this is due to the limits of natural language.

> > > > **layer8**：
> > > > Developers are making a lot of important decisions in detail that the product manager has little understanding of, and these often lie exactly in the disparity between natural and formal language. What the product manager writes isn’t a full specification of the system.

> > > > > **jeremyjh**：
> > > > > That’s true, and LLMs also can make a lot of these decisions correctly.

> **ds_opseeker**：
> re: natural language sucks.
> 
> prof.dr.Edsger W.Dijkstra's views:
> https://www.cs.utexas.edu/~EWD/transcriptions/EWD06xx/EWD667.html
> 
> I humbly add my own.
> 
> Natural language is valuable for the things it doesn't say. The ambiguity is core to the functionality. Which can be very helpful when navigating social complexities.
> 
> And then written language is also valuable for the things IT doesn't say. Under the theory that 90% of communication is non-verbal, then writing lets you say things without having to communicate that other 90%. Which can be very helpful when negotiating something, for example.

> > **js8**：
> > I would agree with EDW, and I have argued here in a similar way.
> > 
> > I am not against use of NL in negotiation or poetry. If you find ambiguity useful there, be my guest. But engineering specifications, mathematics, as well as other sciences or even philosophy would IMHO benefit from more rigor.
> > 
> > I also strongly disagree with the notion that logical or programming languages cannot express ambiguity. (It actually took me many years to understand.) I used to think you need something like fuzzy logic or probability, but that's unsatisfactory in some ways. Eventually, I settled for a really simple understanding of the problem.
> > 
> > Take lambda calculus for instance. I define the term to be ambiguous iff it has a normal form. So it is ambiguous if it expects additional argument, which resolves (part of or all) the ambiguity. Terms with no normal form are completely unambiguous, their "output" is completely given.
> > 
> > In classical logic, this corresponds to formulas that are conditioned on additional assumption. Again, the extra assumption can resolve the ambiguity.
> > 
> > So it is kind of my conviction (although we could show that by translating an LLM as a program into LC) that all the words in natural language can be formalized  as sufficiently complicated lambda terms, that all have normal forms and react to each other in a way that resolves some ambiguity without ever resolving all of it.

> > **1718627440**：
> > I wanted to bookmark this essay, only to find out I already had! Thanks.

> **sanderjd**：
> I totally agree with the skepticism that we'll ever get to a point where natural language becomes the "formalism" and stop needing people who understand the actual formalism underneath. And I agree that you don't *need* LLM based tools.
> 
> But things that you don't *need* can still be (and often are) incredibly *useful*. Nobody *needs* an IDE, nobody *needs* vim or emacs or bash or even compilers or assemblers.
> 
> But we have all those tools and they are useful. That is, their utility is net positive.
> 
> Using LLMs to generate code currently also has (wildly) net positive utility. Maybe that will change because some part of the calculation changes. But this is the situation right now.

> > **jopsen**：
> > Also not everything needs to be formal.
> > 
> > I might want the REST API for a webshop to be solid, payment and checkout process, sure.
> > 
> > But the UI. So long as the LLM doesn't falsify product information, why customize the layout, theme, look and feel for each and every single customer.
> > 
> > Okay, maybe don't, but point is: you could take bigger risks, you maybe don't need to review UI changes as much.

> > > **apsurd**：
> > > The bit about "but the UI" sounds like a developer thinking "UI is a solved problem" in the same way MBAs are told "coding is a solved problem".
> > > 
> > > Product people do seem to think it worth exploring "personalized software for everyone" like literally each person gets their own custom UI. This does sound like a support mess but it's not obviously wrong when you think about the Microsoft Word alternative.

> > **js8**：
> > I agree LLMs are useful tools, but I am dismayed by a lot of cargo-culting around them, which happens because we don't understand them. I think we will have much better tools when we understand what is the expectation and what is the algorithm they run.
> > 
> > Somebody else said that the magician analogy was poor. I like magic tricks, but it took many years of cultural change (influenced by people like Houdini, Randi, Penn & Teller) to stop illusionists (and mentalists) make claims they have supernatural abilities, or people believing it on their own (a magician pretending to be able to catch a bullet was shot by an audience member who didn't understand the distinction).
> > 
> > It is detrimental, I think, to treat LLMs as if they have magical abilities ("superintelligence") rather than understanding they just run some clever algorithm. The fear for (programming) jobs comes from that framing; nobody fears of their job because of compilers, since compilers are understood.
> > 
> > (And it actually runs against kind of "socialist" framing of the problem, which I agree with, that is why should people be worried about the jobs in the first place, when society is getting richer as a result of better tools?)

> > > **sanderjd**：
> > > I see what you're saying, but I don't really think understanding how they work is the problem. We do understand how they work. You can go read the many papers that have been published as the technology has been developed. It is not mysterious. We don't need to understand the "clever algorithm", we already understand that. The sense of mystery is because the results of the algorithm are non deterministic, and because the number of parameters that determine the outcome is so large that it appears to exhibit emergent behavior.
> > > 
> > > I guess I agree with your general premise that tools we use should not be treated as magic. But I don't think this is a problem to be solved, it's possible to learn how these things work, and people should definitely do that.

> > > > **js8**：
> > > > I disagree we understand LLMs, your view is quite reductionist. It's like saying we understand human brain because we understand physics and evolution, or that we understand some program because it's just a binary code in a known instruction set.
> > > > 
> > > > I think Dennett's theory of intentionality (see https://en.wikipedia.org/wiki/Intentional_stance) applies here. We do understand LLMs from physical stance (ML algorithm and inference), but we don't fully understand them from design stance (it's internal workings have been evolved so it's hard to tell the functional units) and from the intentional stance they are a complete mystery.
> > > > 
> > > > And I talk about obstacles to this understanding elsewhere in this thread.

> **tucnak**：
> > It's pretty simple: due to Curry-Howard isomorphism, programming languages are just notations for some type of formal logic.
> 
> Thank you, this made me chuckle!

> > **js8**：
> > Not really sure if it's sarcasm, but let me make a side remark.
> > 
> > It's really stunning how much more effective the "Standard ML" notation (embraced by Haskell, Lean etc.) is compared to writing proofs in classical logic.
> > 
> > This "UX problem" is, I think, the reason why is mathematical community embracing automated provers maybe 50 years later than they could have. Automated people wanted the better language, but the mathematicians largely resisted.
> > 
> > So seeing this, it would be preposterous for me to think that any language, natural or not, has the last say in this. We're gonna be stuck with learning new languages and formalisms for a long time.

> **ActorNightly**：
> Your analogy is poor, and you are missing a very important fact.
> 
> Most of the human written code, in places where that code needs to make money, is decidable either entirely or in large parts. I.e without running the code, you can take a domain of inputs and build a complete range of outputs solely by looking at the code.
> 
> The way that works in your head is that you are effectively doing a compilation to a logical like structure, which then you can use to infer what the output will be from what the input is, and its a direct mapping that is invertible and separable,  so if you know what the output should be, you know what the input is, you can pinpoint the exact location where it breaks. Thats how humans write code.
> 
> If thats not clear, imagine a piece of code that splits strings by spaces, deletes the empty strings, and returns the number of words in a string. The fact that you can say that if you want 3 words, there should be maximum 2 sequences of continous spaces between words, is you effectively transpiling that program into a latent space inside your brain neurons and inverting it.
> 
> LLMs essentially do this, with the added advantage of having been trained on a HUGE number of codebases, so they can recognize patterns that a human cant.
> 
> Where LLMs struggle is complex behavior - they can't simulate things like a human can and choose the best course of action. Even harnesses for agentic loops that can auto run and debug code can't match what a human can do in this regard (hence why self driving still sucks rn).
> 
> So moving forward, being a good coder isn't going to be about writing code, or even about prompting LLMs. Its going to be all about whether or not you can design good custom agentic loops, which necessarily involves knowledge of the model at hand (i.e what words you have to use to get it to do the right thing). This will be especially true as investment into "private" inference grows where companies will be using smaller models that have less detailed RL and thus will need much more guidance to do the right thing.

> > **js8**：
> > I disagree, to keep it short, what you're describing is not understanding, it's superstition. And I think it's a wrong direction of engineering, relying on some sort of irreproducible expert intuition, one that has been successfully replaced by enlightenment and scientific method.
> > 
> > There are 3 major obstacles in understanding LLMs:
> > 
> > 1. They use inscrutable internal language of embeddings
> > 
> > 2. They communicate in natural language which is itself ambiguous
> > 
> > 3. The weights and training inputs are being hidden as a "trade secret"
> > 
> > "with the added advantage of having been trained on a HUGE number of codebases"
> > 
> > This doesn't really mean much unless we understand what is the quality and relevance of these sources for the problem at hand. Without this understanding it's just a superstition.

> > > **ActorNightly**：
> > > >They use inscrutable internal language of embeddings
> > > 
> > > No different than the electrical signals in the intermediate neurons in your brain that comprises the latent space where all the processing happens
> > > 
> > > >They communicate in natural language which is itself ambiguous
> > > 
> > > They lack one-shot precision, sure, but it doesn't matter. They are precise enough with refinement over multiple prompts.
> > > 
> > > >the weights and training inputs are being hidden as a "trade secret"
> > > 
> > > For frontier models that make the company money through api pricing, sure. There are plenty of open source models that can be used for the same tasks, which have open weights.
> > > 
> > > >This doesn't really mean much unless we understand what is the quality and relevance of these sources for the problem at hand.
> > > 
> > > All of the modern models are RL trained on specific tasks when it comes to coding. I.e the initial training run learns to predict the next token based on context, from all the available texts, but then the RL runs specifically train the model in a harness where it produces code and RLed to produce correct code with specific formatting.

**risyachka**：
>> Yes, new jobs were created, but often not for those people who lost their jobs

This is the most obvious thing so many people who claim "new jobs were created" miss.

Yeah sure, new jobs will be created. But not for 90% of those who lost them (and most likely not for the one who claims this). You either won't have time, or energy or else to learn it and compete etc. Sure a small % of people will transition, a massive amount will not.

**agentultra**：
“I built a thing with AI and I don’t understand it. I want to make changes and fix things and have no ability to theorize why it fails or how to fix it.”

Oh my. See, you have to be able to program it yourself before you can build it with an LLM. Otherwise you have no way of judging the output. AI isn’t going to make you a programmer.

Learning to program is.

Interesting article. My advice is to do it the old fashioned, hard way. There’s no royal road to knowledge, skill, and learning.

> **JeremyNT**：
> > *Interesting article. My advice is to do it the old fashioned, hard way. There’s no royal road to knowledge, skill, and learning.*
> 
> I had a colleague tell me "it's not vibe coding when a programmer does it."
> 
> I fully believe there's still value in understanding the internals of software and the patterns developers use to structure it, but I do wonder for how much longer any of this knowledge will be more than of academic interest.

> **meowface**：
> A lot of successful startups start out with good ideas and atrocious, unmaintainable code. Current LLMs kind of let you speedrun that. Dutifully slapping more and more mud onto their week-old ball of mud. The sacred, canonical ball of mud they must faithfully preserve at all costs.
> 
> But the product will probably work decently enough. And as long as the humans are sufficiently devoted to testing and nitpicking and improving the product design and UX choices made by the LLM, they can get away with not caring much about its system design.
> 
> Also, by the time the code really needs to be rewritten (1 - 3 years), the latest models will probably be noticeably less bad at this. Humans who are persistent enough in their attempts to tip the model away from these basins already see at least some success.
> 
> Combined with other general improvements, model companies will probably find ways to do more post-training on not just "can it complete all of these isolated coding tasks with a 100% pass rate" but "can it consistently inhabit a mindset that values the art of elegant code and simple, clean architecture as an intrinsic goal over a very long time horizon". Perhaps in a way where a harness instruction can make the model especially tap into that mode.
> 
> You're right that even in years from now an experienced programmer will get better results with an LLM than a non-programmer will, but I think with each passing year that gap will slowly shrink. Learning programming will always only ever help, but if the non-programmer actually has sufficiently good ideas that they want to start working on immediately, it probably actually is a better use of their time to make the initial version before knowing anything about software development and then to teach themselves (real) software development as they continue working on things. I think this would be the case even if LLMs never got any better than they are today, and I think they're almost definitely going to get way better at programming than they are today.

> > **agentultra**：
> > I think the harnesses might get better. And the alignment and pre training. But I don’t think the LLMs will get much better… I don’t have any sources for that though. Just napkin math.
> > 
> > At the end of the day, even if it gets to 99.9999% reliably generate what an experienced programmer would expect… you still need to be an experienced programmer to know what to want and how to specify it.
> > 
> > I think the experience, institutional knowledge, and process knowledge are never going to be replaceable.
> > 
> > You’ll still need to learn what a cache miss is and how the heap works and when to use skip lists and all that. Otherwise you will just generate slop. An AI system is not able to replace a human.

> **xboxnolifes**：
> We're relearning why you do math by hand before you use a calculator, and why you (usually) dont get internet access during tests even though in the real world you can quickly look things up.

**utopiah**：
(sorry pasting from 4 days ago but IMHO perfect fit)

The same reasons we keep on teaching kids to read, write, do math, sketch, take photos, etc ... because it is fun, empowering and important.

Most of them will never become professional actors, authors, mathematicians, artists, photographers, etc ... and yet they will rely on those skills, on their own or combined, pretty much every single day of their lives.

https://news.ycombinator.com/item?id=49664034

**aethertap**：
This is an issue that's very real for me right now because I'm in the middle of teaching my own kids programming, and we've been working on it for years at this point. I'm watching AI seemingly invalidate the premise behind learning all of it. It's been a pretty depressing change to be honest, because I love programming and watching this happen is hard.

So, I've changed my approach with my own teaching. I'm having them do three things that I'm hoping will prepare them to work in the world they're going to be entering soon:

1. Always have a handmade project going, and work on it without AI assistance even if it's painfully slow.

2. When working with AI, treat it as a compiler that operates on data structures, algorithms, and architectural requirements rather than source code. You have to understand the theoretical pieces of what you're building before you instruct it to assemble them.

3. Use the AI as a powerful tool to grow your own knowledge of algorithms and troubleshooting. Whenever a problem crops up, it's an opportunity to come up with a few hypotheses of what the actual issue is. Don't let the model do it first. I have them actually write these down in our custom kanban tool as issue cards, and then they use the model to investigate how close they came to the true issue.

I'm hoping this will give them something similar to my experience of debugging over a lifetime of coding. The knowledge that seems to be most valuable that I bring to the table when coding with AI is in recognizing quality/maintainable code architectures, and "seen that before" debugging experience.

We just started this so I don't have much in the way of results yet, and it feels risky to even allow it into the curriculum. I don't think that it makes sense to hide from it though, so this is our best shot.

> **sesteel**：
> I came back from retirement for a couple reasons, one as a hedge against the stock market due to AI.  Two, the camaraderie built by working with other people.  Three, the opportunity to mentor young people.
> 
> AI has made the whole situation suck.  Stock market is stressful due to energy and AI.  AI has left people working alone managing agents.  Any advice regarding development best practices I give to young people might have made sense 3 years ago, but hardly matters now.  I look around at all these young people and wonder if they are going to be okay.  It has only served to make me feel depressed and put a name and face to any future displacement.
> 
> It all seems so pointless.

> > **aethertap**：
> > Yeah, it's really hard to keep pushing honestly. I have no idea where this is going to end up, but I think there will still be space for higher-quality, more interoperable tools for quite a while. I'm also coaching them to treat software as a thing they can use to boost their real careers, not as a thing that will be a career.

> **vouaobrasil**：
> The real problem is that the environment for healthy learning is gone. At least when I was a kid, there's something magical about having an environment where nobody knows what the hell is going on and the learning is, to use your words "painfully slow". I guess we've been trained to think that way with all this modern technology, but back in the day, it didn't matter whether the final result was accomplished or not. All that mattered was the fun of trying to get something to work.
> 
> Nowadays AI shifts the emphasis to the final product, and frankly that's boring. Kids will use it because it's there, because it gives that initial result really quickly and we're hardwired for that. But it removes that cool environment of having a blank slate and just seeing things happen all on your own accord.
> 
> Companies might like AI for the short-term gains but we're doing the entire planet a disservice by having even invented AI, in my opinion. We're all being trained to be producers.
> 
> Can a person like you create a little microcosm of learning that can work? Maybe, but I get the feeling that programmers these days are being blinded by the fun of AI and forgetting that there's actually more to life satisfaction than having fun.

**yogthos**：
I would argue that learning a high level language like Clojure is most productive now that LLMs exist. I'm going to make a bold prediction that imperative programming is effectively dead now. LLMs are very good at writing the implementation details, dealing with syntax quirks, and the boilerplate.

What you still have to understand are high level concepts like which algorithm is appropriate to use for a particular problem, or which data structure is a good fit for the data. How to organize your logic at scale and how data flows through the system. These are the kinds of things you need to be able to do to evaluate whether a solution an LLM came up with is sound or not.

So, you still need to learn and practice writing code to develop the intuition for these things, but you don't really need to worry about the nitty gritty of it. And a language like Clojure is a perfect fit here.

**ah1508**：
A good question might be: what do I want to be ? A good prompter ? It's like someone who used to bee a good chef but is now good at ordering at uber eats. Even for a junior: being a good prompter may not be enough.

We tend to think that we make a program, but (writing) the program also makes us what we are. It is what we do that defines what we are. "I think, therefore I am".

I don't see a career path for a prompter. I don't see the benefit for an organization to rely on people who don't understand what they do nor how the programs that keep the organization running works.

That being said, "the man and the machine" can be a powerful combination, like when we drive a motorbike. For me the cooperation with a LLM could work like this: if there is 50 features I write the code for 25 of them and write stubs (classes, methods) for the 25 others, with comments that will be the prompt. The AI audits what I write, gives suggestion, find blind spots and learn best practices from my code. Then I do the same kind of review on the generated code and the AI learns from my review. An AI can even, with luck, suggest a completely new way to solve a problem (see AlphaGo vs Lee Sedol move#37 in game#2) and then I learn something.

Working like that will make me better at reading code (after all Linus spend a lot of time in reading code, it is a good skill to have) while the AI gets better as well. I don't delegate everything and keep practicing, I keep myself up to date, the AI learns from me and I get peer review from the AI. And the codebase does not become a mess (=technical debt) that only another AI can maintain while token prices increases.

> **LastTrain**：
> Prompting is an intermediate situation at best anyway. I think the most lucrative AI field going forward is going to be liability litigation since there will be only a small handful of AI companies, each the size of small nation states, who will need to be held accountable for what they unleash.

> > **fwip**：
> > It will be a lot cheaper for the AI companies to pay lobbyists for a few years, so that they no longer have to take accountability.

**RugnirViking**：
one thing ive found fascinating recently was re-taking some of the best tutorials i've ever taken (catlike coding, libtcod roguelike, etc), and asking astra to just transpile them into other technologies, stacks, or languages. Including all the garden paths, false starts, and dead ends, because the tutorial author included those intentionally. I had it copy graphics across where they're a screenshot of software, and reproduce diagrams with interactivity to show how graphs/shapes/values change as inputs are varied.

Another key thing to ask it to preserve is the nature of how we are asked to edit files. Sometimes its "replace x method with this" and then an explanation, but sometimes its "change the check at the top of suchandsuchafile to handle the new method signature", which of course forces the user to follow with and try things themselves instead of blindly copy and pasting

I certainly feel I gain insight into new technologies the same way I did with the original tutorials

Worth noting before anyone gets any ideas the resulting documents are purely for ones own consumption, publishing such things would be a moral injury against society in general and the original author specifically. If they wanted it to be made, they could just do it themselves.

**dack**：
i might never know what it's like to learn programming after LLMs became powerful (I started programming in ~2002).  But if someone forced me to give advice to such people, I'd say just start building things and stay curious.

That means, use LLMs to build whole sites and then dig in where you are curious. Look at the code, ask your LLM how it works and keep digging until you understand how the program is constructed. A benefit is that you're looking at a REAL program, not a toy example. And also, if your program stops working well (bugs or perf issues), you can debug it with the LLM and start asking it to teach you why things were slow and the concepts behind it.

I think you can basically build your own on-the-fly curriculum these days and do it with a real-world example WHILE you build cool stuff.

I think the biggest barrier will be motivation - many people don't want to be curious, and they just want it to work. they won't learn anything that way.

**threepts**：
I think a person who still knows how to code manually, learning from raw documentation and trial and error can hold massive leverage over people who don't.

**qtqtqt**：
> You can add a comment to this post by sending me a pull request.

Interesting.

**travthedev**：
How much programming knowledge do you think someone should know before they can comfortably say they are a solo developer? (in this age of AI coding)

**rgbrgb**：
I've been thinking about this in the context of learning new languages and tech. In pre-LLM days it was fun to sometimes try to implement a new idea in a new language or stack and build up an understanding by trial and error. You'd have to accept that it will be slower to get going than a familiar set of tools and maybe only trade out one old tool at a time in this way.

Now the pace of dev with something new is so rapid and fun that it's hard to not skip even basic things with a new stack. I swapped postgres (old reliable) for clickhouse (first use) in a project and saw a massive speedup of my workloads, but I really have to go down the socratic rabbit hole to understand why and even then it's a different level of understanding vs having to read the readme, quickstart, install it myself, rewrite queries by hand. TBH though, pre-LLM I probably would have just plodded along with postgres and built a hacky auto-indexer thing, so in a way the agentic coding helps me explore more territory but encourages less depth.

No strong conclusions. Like OP, I'm just spitballing / trying to understand this new world too.

**twinwest**：
I am curious that would there be any new programming language being invented in the age of LLMs, as LLM is about probability and need to trained on a large dataset to perform. It looks like the incentive is less while it costs more to create a new programming language.

**aj7**：
I have a hard time understanding the problem here. I view ai as a tool. Like a steam shovel, electric drill, etc. You can pick up any tool, and try to use it.  With the the drill, you’ll have modicum of success, until the drill spins in the chuck. Then you’ll learn to tighten the chuck more, and have more success. Try to solo on a steam shovel with no training, and there will likely be trouble. Vibe coding without understanding underlying syntax is similar.

**nico**：
> After months of refactoring I had an uncomfortable realization: I may have built a system that is above my own level of understanding. When everything works, that gap is almost invisible. When it doesn't, it becomes very real.

> "Sometimes I genuinely don't know what to do next without asking another model. That made me wonder whether I spent a year building a product, or partly building the appearance of one: something sophisticated enough to work, but which I don't yet understand deeply enough to truly own

This is always the reality for a sufficiently complex system. We only have an illusion of understanding

Now, more specifically about this feeling, it’s the way a lot of managers feel as well. They can only ask others to fix/change things, and they don’t really understand how/why things break in the code. Even if they lead the whole team to build the product

> **avgDev**：
> Accurate.
> 
> I've wrote a rather large system that runs a medium business, solo. When a bug pops up, I feel unfamiliar with the code. It was all written by hand with 0 LLM usage.
> 
> It is normal to feel this way. However, I am still very capable of resolving the issues in a timely manner. Adding any new big features is a big undertaking and usually involves a lot of refactoring to fix the dumb decisions I've made.

> > **rsolva**：
> > I have this feeling whenever I read my own (no llm) code that I wrote 6 months ago. Sometimes a couple of weeks is enough to feel alienated from my own, well considered code, that I spent a lot of time crafting with love.
> > 
> > That is why I try to make good, high level descriptions of what is going on at several levels of a project. Funny thing is, I just kept on doing this with llms, using AGENTS.md at almost any subdir of a project. It works for me, and it seems to work for the llms too.

**ferguess_k**：
> Still, I doubt that it's possible to significantly speed up human learning. The bottleneck is hardly the teachers nor the materials, but how fast a human brain can absorb new knowledge.

I completely agree with it. LLM might be able to 10x the number of PRs, and maybe that is actually is fine for the company because it doesn't care too much about verifications and such. It just wants to ship something that works. But individuals still learn at approximately the same speed. My brain still needs to hit some walls, scream at itself and assimilate the failure and success of my past, to actually learn something new. LLM does help by serving as a very good search engine if I can't Google it easily, but no more than that.

I'm also very happy that OP said "I don't know" a few times.

**jopsen**：
To me software engineering was often about: how do we structure the project so that the crappy code the other students/co-workers write don't break everything?

Not because everyone writes bad code. They do, at-least the do first time you read their code. You only think someones code is decent when you spent 3 hours trying to refactor their PR, and realized that the compromises they made were perhaps reasonable.
(This is an important lesson to learn)

Whether code written by others is poor or not is also besides the point.
You cannot keep everything in a large project in context (biological or not).

Software engineering (not computer science) is about: managing complexity. Structure your project in layers or abstractions or packages or silos or verticals or objects or whatever.

But break complexity into bits, so that everything isn't in mind all the time.

Nothing new about that. And poor engineering can be papered over with hard work. It's just easier to reach the point where poor engineering really bites ;)

> **devin**：
> At an even more fundamental I tend to think about software as managing _risk_, where complexity is just one component. A large portion of my career has been about making difficult decisions around accepting particular sorts of software risk to reduce other types of risk, like my coworkers continuing to receive paychecks, for example.

> > **ulrikrasmussen**：
> > Put even simpler: code is a liability, and understanding is an asset.
> > 
> > It's easy to add more code, but it also increases the risk, especially if you are the only one who understands how it works. As more people on the team understand it, the risk decreases. It becomes less likely that the code interacts in an unexpected way with other parts of the system, and it also becomes more likely that the existence of the code is justified because noone felt the need to replace it.
> > 
> > If you fire the team and replace it with another, you now have a lot of code and zero understanding. That understanding first has to be mined before you can close the asset/liability gap.
> > 
> > In the age of LLMs, it becomes easy to produce 10x as much code as before, but I don't think you can put the same multiplier on how fast you can increase the understanding. It may even be <1 if you are not being mindful about your LLM use.

> > > **devin**：
> > > I think a lot of people will tell you that now it's much easier because they can just ask their LLM how it works, but in practice I don't think people are able to absorb enough from these purely need-based interactions to arrive at understanding that translates into sustained long-term increases in productivity for large projects.
> > > 
> > > The thing I keep seeing is greenfield AI projects built by ill-conceived, self-styled software factories. They grow incredibly quickly, and then reality sets in and the pace slows. Demonstrating this is difficult. There are real productivity increases to be had here no doubt, but the long tail is still expensive.

> > > > **ulrikrasmussen**：
> > > > Exactly. And LLMs will only accelerate your rate of understanding so far by helping you find and organize information, at the end of the day you are still limited by your own mental bandwidth.

> **ActorNightly**：
> The difference is, the total cost for a human to write/modify code files is much higher than for an LLM. A lot of time has been spent designing program languages so that human time is more optimized. LLMS dgaf if the code is structured cleanly or is a mess.
> 
> So even if you end up with a mess of a codebase, as long as you define your test cases and they all pass, what is in the middle doesn't really matter.

> **rjbwork**：
> And building the correct structure for your problem/program is still a huge part of the job.  If you completely delegate structure, you still get a clusterfuck.
> 
> I have found working with LLM's is best when I provide as much structure and constraints as possible, and reduce the degrees of freedom that the LLM can exercise, so that it is forced to fit its logic inside the structural boxes I have laid out.
> 
> If you just delegate everything to the LLM to get an absolute morass.

**j45**：
Learning to program is learning to think and still important to learn.

The current state of vibe or assisted / automated coding is still improving, it sometimes still can end up like cowboy coding gone wild.

**so-cal-schemer**：
A good place to start:

https://sarabander.github.io/sicp/

**sashank_1509**：
If you were an average tailor in 1700s, you would have to transition into operating sewing machines in a sweatshop. Same for coders, time to transition into the intellectual sweatshop, this one at least seems to be more comfortable.

Coutures are still hand made by tailors, a lot of it hand sewn without a machine. It’s the same with LLMs, GPT Astra max thinking and it still mostly looks and feels like Slop. That slop is probably fine for 90% of software products but not for 10% of remaining high quality software. Decide which part you think you can / want to join.

**Oscalemor**：
Feels like the former classic software engineers will go deeper into the technical stack, moving away from frontend/design and flashy things

**BatchJob**：
My earnest, non-sarcastic advice to anyone considering learning to code is to find something else that interests you.

While there is possibly some time left before the software industry implodes, hobbyist software will also get steamrolled so I would in the strongest terms possible guide someone to find something that makes them happy and to pursue it.

The software industry as it exists today is a sad bag of regret and disappointment being papered over by opportunists of the worst kind.

Save yourself the trouble.

**purpleflashing**：
Finally a thread to traumadump my anxieties!

I have been trying to learn programming unsuccessfully for many years (I still ocasionally get a burst of energy, try something, then eventually abandon it halfway). In the end, I just accept that I don't have the kind of thinking that makes this effort enjoyable and I cannot achieve anything good.

But, to be fair, LLMs also don't solve any problems for me in any meaningful way. I have to do a little bit of very simple coding at work and I would say that I struggle with LLMs as much as I do when I try to solve them by myself. The code works in a moment but when it gets extended, it breaks, I spend a lot of time troubleshooting. Last week I had to rewrite the code myself as my attempt to prompt fixes with LLMs just kept adding bugs -- I can't say my rewrite is any good (I need to traverse graphs and I don't know how to do it properly so I just used whatever algorithm I found in a book lol), it will probably break the next week when I need to change it or add something but I hope at least I'll be able to fix it faster as I have roughly an idea what's happening.

I haven't measured how much time I spend on things with or without LLMs but the subjective experience is pretty poor -- I work in an "engineering-heavy" company, the constant feeling of not understanding my own work among people who have master things that are 10x more complex is pretty depressing. When I program something poorly, I can at least explain what I did and what my idea was, even it was a bad one, waking up to build failures and spending an entire day relearning my own project is not good, man.

As for the obvious argument -- "you're using it wrong" -- I might be? I did try to learn prompting and I don't think I do any obviously stupid stuff like specifying a persona. At this point I feel half-insane as a frequent sentiment is that non-programmers can generate code for functioning software with LLMs, perhaps it's low quality code but it works. Except for me -- a non-programmer who fumbles it every day! I don't even need anything complicated -- they're Python extensions for a Sphinx project!

