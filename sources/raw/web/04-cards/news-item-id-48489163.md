# Show HN: fata，用间隔复习对抗 AI 编程造成的技能退化

- 链接：https://news.ycombinator.com/item?id=48489163
- 作者：djoume
- 获取方式：Hacker News 帖子与评论全文

---

## Show HN: Fata – Spaced repetition to fight skill rot from AI coding（djoume，124 分）

（讨论共收录 53 条评论，缩进表示回复层级）

原文链接：https://fata.dev

Hi HN, I'm Djoumé. I've been a developer for over 20 years, and like a lot of you I've been coding almost exclusively through an agent in the past few months.

It's been amazing to vibe code prototypes in any stack, but when it comes to building something reliable/scalable, I couldn't effectively guide the agent unless I knew the technology. And the scariest part is that I'm seeing a lot of my technical skills decreasing due to AI coding.

Reflecting on my journey, I also worry about how the new "AI native" generation of software developer is going to acquire technical depth.

So I built fata.dev: short daily spaced-repetition sessions for programming skills (Rust, CSS, React, Python, TypeScript, Architecture).

You can try it in the browser with no signup: https://fata.app/courses

It's an offline-first mobile app built with Capacitor, RxDB and Firebase. The first courses were painfully written by hand, but most content is now AI-generated. It takes about 3000 LLM calls to generate a course, and every code samples goes through compilation, linting, unit testing, AI and a final manual review.

Would very much appreciate any feedback on the product & website, what works and what could be better. Thanks!

**bluefirebrand**：
The copy on your website is kind of confusing imo

> fata builds the full-stack fundamentals to lead a coding agent through frontend, backend, and the technical design that holds up in production.

"Fata builds" sounds like it does the work, not like it trains you how to do the work. With how many "AI does the work for you" promises out there, it's confusing terminology

Anyways best of luck I suppose. I would rather run a drill press through my hand than use AI agents to write code for me, so I'm not your target audience

> **djoume**：
> Thanks for the feedback, much appreciated, will fix the copy.

**fragmede**：
How's your assembler? Run ar by hand lately?

> **djoume**：
> Does not happen often but now and then my basic x86/arm asm skills have been helpful to debug or just understand at a deeper level how something works.

> **jubilanti**：
> If you're trying to imply that knowing fundamentals of programming is now as obsolete as knowing fundamentals of assembler: this is a dumb thought-terminating cliche that adds nothing to the discussion and I'm sick of seeing it constantly in these threads.

> > **dsffdfsdds**：
> > React, python and Rust are not the "fundamentals of programming". Those are highly specific ephemeral instantiations of the more general knowledge you seem to be alluding to. They are the new COBOLs. We are not there yet, but the writing is on the wall pretty clearly if you ask me. Regular programming languages will indeed be as useful as knowing assembler in a couple of years, which is to say, pretty useful, but for many not necessary (anymore).
> > 
> > The main point is that these things are implementation details like assembler. Very interesting in and of themselves especially if you are on the spectrum and occassionally need to be looked at, but the knowledge is instrumental at best and useless baggage at worst. Validation is what matters. Code is useless cruft. If you can replace it all with "348348-23439 CALL(X(DDD)D)" somehow, that's great, as long as it works. I don't know why people get sentimental about wrangling syntax. We're in automation, we've been doing it to other people. We're now doing it to ourselves.
> > 
> > You see this point often because it is blatantly obvious for anyone that didn't build their identity around proficient wrangling of specific families of syntax.
> > 
> > I suspect the era of LLMs coding in "our languages" is a temporary abberation anyway. It's not necessary at all and in fact actively hampering their effectiveness. I'd say enjoy it while it lasts.

> > **kakacik**：
> > Do something helpful for community, don't want anything back, no ads, no monetization, for a change reader is not a product. Show it. Get shit on it by snarky depressed/envious folks.
> > 
> > Internet at its worst.

> > > **joshuat**：
> > > I don't disagree that they're not getting the best reception, but a freemium product is hardly a new/rare thing.

**royal__**：
I can understand that you want to make money from this, but hiding significant amounts of content behind 13 dollars a month feels a bit much. Especially when you acknowledge that most of that content is LLM generated. It's not just the advanced courses, it looks like it's pretty much all of them

Cool app though! I love the idea of coding Duolingo. But I think the price is going to turn most people off. Another problem I see is that it's not really clear how this is that much different from other similar apps out there.

> **djoume**：
> Thanks for the feedback. What similar app are you thinking of?

> > **royal__**：
> > Codecademy, Mimo, Enki. I'm not going to act like I know a lot about other options, and you do say that fata hits on  more advanced topics which these may not.
> > 
> > I do think you have a cool niche here that isn't being covered, maybe your landing page should include more information about the Duolingo-esque features? I just know that pulls me in a lot.

> > > **royal__**：
> > > For the record, btw, id DID download your app and I am going to spend some time using it. Other commenters here are talking about how spaced repetition isn't what's important, which is true in the same sense that you can't just use Duolingo to learn a language. But that doesn't make it useless.

> > > > **djoume**：
> > > > Completely agree and I tried to avoid the Duolingo approach which optimizes for "engagement" over learning. I would love to hear any feedback you have after using the app for a bit: djoume [at] fata.dev

**Falimonda**：
If you need to use an agent then you might as well just work SRS into your harness using something like https://srs.voxos.ai/

**AmblingAvocado**：
Coming at this as someone who has stepped away from coding more than once for multiple-year long stints due to various career choices - I think the concern of "skill rot" is overblown.

I stopped writing C++ professionally in the early 2010's. I came back to it in the early 2020's and it was extremely easy to pick up. Less like riding a bike, more like driving a car. The car got better over the last 10 years, but it still takes a bit of time to fully meld with the machine. The skills didn't rot, they just fell behind, and catching up wasn't a big deal.

I think the only "skill rot" people are facing today when coding by hand vs by agent is that you know you're doing something the hard way when you know there is another path of least resistance available - and that creates internal resistance to doing it the hard way. It's a mental block, not skill rot.

The one area I do find myself questioning is that my low level tech skills aren't growing - I'm building bigger projects that do more stuff across more areas, and as a result I'm touching lots of new technologies from a birds eye view and directing the agents to do stuff with them. I'm not personally gaining that experience of using those technologies, whereas if I were doing things the old way I would be deep in the weeds and have to know them in depth. But if I were doing things the old way I probably wouldn't be building such ambitious projects as a solo dev either.

IMO it's more like digging out the foundation with shovels vs using an excavator. You don't lose the shoveling skill by using the excavator, but you sure feel like a chump using a shovel when there's an excavator parked and ready next to the job site.

> **axus**：
> Maybe it only applies to people at the top of their game; pro atheletes and musicians need regular practice, the rest of us can use most of our skills without that.

> **stbtrax**：
> do you have any tips or strategies on picking up c++ after a long break?

> > **AmblingAvocado**：
> > For context, I was working in C++ when C++0x was considered exotic and a bunch of actually useful stuff was in boost, basically making boost mandatory - and the headache of setting up a project and tooling to do that was enough to push me to other languages for small projects.
> > 
> > When I picked C++ back up, I had a greenfield project I wanted to work on and I landed on this as a reference: https://github.com/AnthonyCalandra/modern-cpp-features. I just started working on my project and every time I ran into something where I knew other languages or libraries covered a gap, I would look through that guide and use it as a reference to bring it into my code. Smart pointers, auto types being two big ones. That, and threads, concurrency primitives - I remember hitting those and being like wow, you don't need a bunch of #IFDEF's to be cross platform anymore!
> > 
> > I also found there were header only libraries that were easy to vendor for things like json parsing, image processing, and thread pools. That saved me a lot of headaches, and created new ones! ha.

> **akoboldfrying**：
> This differs from my own experience with C++. I went from language-lawyer level knowledge (in some parts) while using it heavily (at work, at play and answering Stack Overflow questions on it) to forgetting quite basic stuff after a few years of no use at all. This was all before LLMs were on the scene. With that said, relearning is much faster than learning the first time, as the basic "shape" of things is still there in my mind.
> 
> In my defence, even Stroustrup acknowledges the language is too big and complicated, and it's continually getting bigger.

> > **AmblingAvocado**：
> > The big initial hump I recall was syntax for writing main and what to #include, then header guards. That, and getting clang up and running in a docker on windows so I could use new C++ features and flags that were blowing up with whatever compiler I got started on. Once I was able to iterate things started coming back quickly.

**fabled-out**：
This is very, very cool! Super impressed by what you've built.

As a non-programmer who is now doing a lot of vibe coding for myself these days (and feeling very scared about which of my vibe coded things will just randomly break one day haha...) I feel like what I'm missing isn't necessary language syntax skills, but rather the higher-level planning/organization/architecture capabilities that a seasoned software engineer acquires over years of seeing what scales vs. breaks in the real world.

Is there anything you would recommend I learn to start acquiring that knowledge (aka. the higher level knowledge a "vibe-coder" who doesn't manually code by hand would need)? I'll try out your clean architecture course, but would love to see more along those lines :)

Obviously I know nothing will replace real world SWE experience, but anything that could plug that gap even a tiny bit would be helpful and is something I'm willing to invest in.

> **djoume**：
> Thank you. Try out this course and let me know what you think
> 
> https://fata.app/courses/archClean
> 
> For me I found that I learn best when I have a concrete use case.

> **soperj**：
> Have you tried to understand the code that's being produced?
> 
> That'll go a long ways to actually helping your vibe coded thing not break, and also will make it easier to change things in ways that you actually want changed instead of throwing it into the black box again hoping for the best.

> **Atotalnoob**：
> You can change the output style of your AI agents, have them use a more learning and “tutor” style to improve your skills.
> 
> The coach could look at transcripts of old sessions and come up with real lessons for you to improve. Ask for book or article recommendations.

**mrmartineau**：
This is super cool and definitely something I can relate to. In fact, I recently built Reps, a daily coding puzzle, to help fight “skill rot” as you say. Try it out at https://reps.zander.wtf and let me know what you think.

> **djoume**：
> Very nice! I went with a different approach so that 1) I could make it usable on a phone and 2) It could work with any programming language/framework

**dvt**：
Engineering has never been, nor will it ever be, about "repetition" or "memorization." This is a relatively new fable invented by those that have participated in ritualistic interview hazing. Imo, there are, broadly speaking, two types of engineers: computer scientists, and programmers.

Computer scientists do science. The end result is a new algorithm or theorem, and they work with lots of math, proof systems, formal languages, and so on. This is a profoundly creative and collaborative process.

Programmers build products for end-users. The end result is the user experience, the bottom line, stars on Github, or whatever. This is also a process that constantly needs feedback, from teammates and from clients.

These are broad categories and sometimes they overlap: an operating system or database engineer might do a bit of both, depending on the hardware targeted or on various constraints. Sometimes you need to be a bit clever to get to your product goal.

This cleverness has nothing to do with memorizing keywords or solving interview gotcha questions. This cleverness can't be augmented by AI, and it can't be rotted by AI: it's something that's innate to people. Their internal curiosity just happens to manifest in the context of engineering because they love the craft.

In many ways, it's like reading a book. You can't "make someone" enjoy reading, some people are just boring and uncurious. In many ways, I feel that people that are threatened by AI are like this. AI is an incredible tool, but it feels like an autistic junior engineer. Sure, it might have memorized more library names or more syntax or can reference some little-known fact, but it fails to understand basic data flow. It doesn't grasp ergonomics, ease of use, etc., etc.

A tool like fata is great if you want to be an AI, but it won't turn you into a good engineer.

> **djoume**：
> Thanks for taking the time to comment. I agree that people have tendencies towards certain interests, I can't remember a time where I wasn't interested about computers, even long before I had access to one.
> 
> That being said, people are also inspired by other people or by products, and there are ways to make the learning more effective.
> 
> No tools is going to turn you into a good engineer, fata makes it easier to practice regularly and it's that practice that will make you improve your skills

> **jacques_chester**：
> Focusing on your first point: Memorization isn't everything. But it's not nothing either.
> 
> Sometimes it's nice to be able to just bang out some code without looking everything up. IDEs in an IDE-friendly language make this awareness accessible in the immediate frame, but don't necessarily help with having a mental menu of possibilities to choose from.
> 
> That said: I find spaced repetition utterly crushing, so I only use it very sparingly.

> **RealityVoid**：
> > Engineering has never been, nor will it ever be, about "repetition" or "memorization."
> 
> Having memory of how to do things and techniques and tools and patterns is absolutely important for solving problems. The very reason experienced engineers are just better at many classes of problems.
> 
> > This cleverness can't be augmented by AI, and it can't be rotted by AI: it's something that's innate to people
> 
> I argue "cleverness" is a learned and honed skill by exposure and exercise. I just reject the idea that some people are just incapable of original thought. They just didn't get the circumstances to flourish.

> > **dvt**：
> > > I argue "cleverness" is a learned and honed skill by exposure and exercise.
> > 
> > Even if I were to concede this point, it's certainly not honed by the kind of exercise that OP is advertising. We are deep in Max Howell's "invert a binary tree" territory here.

> > > **knollimar**：
> > > Doing leetcode absolutely makes your system design better and you don't deploy algorithms you don't know.
> > > 
> > > Invert a binary tree is kind of a strawman for the absolutist claim that you don't improve the cleverness by practice, but it's an example that not all the practice is useful

> > > > **watwut**：
> > > > > Doing leetcode absolutely makes your system design better
> > > > 
> > > > Only up to the pretty low point. After that, it becomes completely absolutely useless. And people collectively spent astonishing amounts of time training that for job interviews long after the "absolutely useless" bar was passed.

> > **danielmarkbruce**：
> > > Having memory of how to do things and techniques and tools and patterns is absolutely important for solving problems. The very reason experienced engineers are just better at many classes of problems.
> > 
> > At least in my experience, the best engineers have a vast catalog of problems and solutions, algorithms, architecture patters, data structures etc and almost nothing comes from scratch. The worst engineers do everything from scratch without much/any understanding that the problem they are facing (or a variation of it) has been solved before in 6 different ways with varying tradeoffs.

> > > **apsurd**：
> > > “Master all prior art before naively trying to do anything on your own” - also, very much does way more harm than good in a learning context. (it narrows the top of the funnel for no good reason)
> > > 
> > > The gripe seems to be the negative effect on the team, business/project outcome etc, sure work doesn’t pay you to write your own compiler.
> > > 
> > > But again, its such a disservice to learning to dictate a shape, largely academic, largely top down (vs bottoms up failing & flailing).

> > > > **danielmarkbruce**：
> > > > No one said anything about learning everything before doing anything, and nobody suggested they were told to do it or how they did it.
> > > > 
> > > > And, bad engineers can become good ones. All the good ones were terrible at some point....

> > > > > **apsurd**：
> > > > > Yes, the main issue I had was regarding how anyone can get good without first being bad. Your comment highlighted a very particular worst engineer persona, as if there was an obvious way they could have avoided it preemptively.
> > > > > 
> > > > > Since we’re talking about learning in particular, my callout is it’s in no way helpful to shame people that aren’t good at something. It’s counterproductive.

> **danielmarkbruce**：
> Engineering creativity does not come from a blank slate.... people create by combining primitives like APIs, algorithms, patterns, debugging techniques, product constraints, performance constraints, user needs, and blah blah blah.
> 
> You can argue that a particular primitive is bad or overemphasized but the ida that real engineering has nothing to do with repetition, memory etc is wrong.

> > **apsurd**：
> > Well, the inventory of primitives has to be earned. Else they can't actually be composed. Composition requires tacit knowledge. There's a learning pyramid thing that describes it. Just asked chatGPT to jog my memory (heh, heh)
> > 
> > <pre><code>    Remember → Understand → Apply → Analyze → Evaluate → Create
> > </code></pre>
> > citation: see "Bloom's Taxonomy"
> > 
> > Discussions on learning typically bring up the need for rote learning, repetition and vocabulary building. It is essential, but to focus on it "as the mechanism for learning" does more harm than good. It's necessary but in no way sufficient.

> > > **danielmarkbruce**：
> > > > It's necessary but in no way sufficient.
> > > 
> > > Sure, agreed.

> **hsuduebc2**：
> Sadly the "ritualistic interview hazing" is just reality how you can get ordinary job today. Usually it have nothing to do with the job itself, it almost always could be solved by just ordinary dialog but for some reason. I don't know if it was someone from HR or some proactive manager thought it would be a wise idea to do this type of tests.
> 
> I just started to perceive it as an contest full of stupid useless semi relevant bullshit questions when you win the job. I'm kinda invested in the hate, because I'm currently attending interviews.

**jraph**：
I can envision a way or two of avoiding AI skill rot... which could involve just doing the work by yourself actually xD

I hope you factor in the time you spend doing that spaced repetition thing when you evaluate your AI productivity boost...

> **djoume**：
> I do ~10 minutes per day, wouldn't really make a difference in my AI productivity boost calculation (which 10-20% boost BTW)

**jwpapi**：
Are you guys for real? A mobile app?

Who in the world who’s interested in this would do it on a mobile app.

> **djoume**：
> People often do their 10 minutes of daily fata.dev during their commute where mobile/offline access is ideal. The UX is optimized for mobile but you can also do it on your computer, it's a progressive web app that is installable as a desktop app:
> 
> https://fata.app

> > **jwpapi**：
> > I don’t think HN is the right place to post this and also I don’t think the title/slogin as fitting. This might be helpful to beginners, but nobody who’s scared of skill rot, will use this on a mobile app.
> > 
> > Honestly I think there is no benefit in any mobile coding app at all. It makes coding seem way more tedious than it is. I would rather recommend a book, laptop or youtube video than to do coding tasks on a phone keyboard.

**LowLevelKernel**：
Great lessons

> **djoume**：
> Thank you

**postalrat**：
Still building my new "approve" button skill.

**anythingworks**：
> 10000+ developers on this

this seems false given this just launched?

> **djoume**：
> This is true. A first version of the app was launched 2 years ago.(Android only, manually created courses, webdev only).

**nutifafa**：
at this point building is not the challenge fighting bugs and vulnerabilities is the challenge. try getdebug.dev it has a free cli tools to find, fix and enable you ship your code without someone taking advantage of it.

> **nutifafa**：
> it has the guide at https://github.com/getdebug-ai/cli

