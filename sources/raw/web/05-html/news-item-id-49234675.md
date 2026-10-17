# HN：How I use LLMs to learn complex topics 讨论

- 链接：https://news.ycombinator.com/item?id=49234675
- 作者：laurentiurad
- 获取方式：Hacker News 帖子与评论全文

---

## How I use LLMs to learn complex topics（laurentiurad，835 分）

（讨论共收录 300 条评论，缩进表示回复层级）

原文链接：https://laurentiugabriel.github.io/blog/articles/how-i-use-llms-to-learn/

**ventana**：
The title is not representing what the post is about. “Use LLM to learn complex topics” here actually means that the author asks an agent to describe the problem area, and then implement a simple web-based simulation game, and by playing that game, the author actually learns about the topic and its constraints. They use chip making as an example.

That's actually a fun way to learn processes!

> **laurentiurad**：
> Thanks! The original title was "How I use LLMs to learn...", but somehow HN removed the "How" part. I even removed the initial post thinking it was a typo on my end and tried to post again, but I stumbled upon the same behavior.

> > **Anon84**：
> > HN likes to remove “How” and “Why” from titles. You need to edit them back right after you post it

> **lacedeconstruct**：
> Its fun but is it really effective ? I mean I checked the LLM one and I came out more confused about a topic I already know about, I find the best way to to learn using LLMs is to just generate an example try to somewhat get a mental model of how it works and then ground my understanding with traditional documentation and resources, its an iteration of a technique I used to do in college where I would read the textbook questions first to understand what is important and then read the chapter

> > **sixtyj**：
> > Game-based learning, described by Comenius, works if someone else prepares “a game” for you. E.g. like a dungeon master. :)
> > 
> > Otherwise you probably get more confused as you have mentioned.
> > 
> > On the other side, Peter Diamandis describes a situation where a bunch of kids were given a internet-connected computer and they had no teacher. Instead of it there was a “grandma” that checked kids from time to time.
> > 
> > After that there was a knowledge test that revealed “no teacher” approach was more efficient.
> > 
> > But it was a group, not an individual activity…

> > **ventana**：
> > I assume different ways of learning work for different people. For me personally, it's taking a piece of paper and drawing the diagram of how things work together; of if it's some math, then, again, using the pen and paper to follow the text. I can very much accept that for some people playing the simulation is a good way to touch the new problem space. I can easily imagine that for some topics, let's say, traffic signal automation, a careful simulation game will probably give more information than reading papers or manuals.

> > > **lacedeconstruct**：
> > > > a careful simulation game
> > > 
> > > Totally agree, unfortunately careful simulation games are very rare

**aswegs8**：
I mean, yeah, fun project. But that whole game could be like 15 mins of prompting.

**IshKebab**：
> What you get is a beautiful animation that is 100% accurate and free of hallucinations.

How do you know if you're learning this for the first time? Very risky to learn from LLMs. I've done it, but you have to keep your wits about you. Lots of "oh of course you're right - what I just told you was completely wrong".

**rickcarlino**：
I’ve been using LLMs to create readable rewrites of RFCs and specs that interest me. It is not precise enough for implementation use, but it has increased my understanding of the underlying RFC.

Another useful approach has been asking Codex to implement complex things, like a Kademlia DHT or BitTorrent client in a literate style with the explicit purpose to increase understanding by reviewing the source code.

Examples: https://rickcarlino.com/notes/note-dump-and-ai-summaries/index.html

https://github.com/RickCarlino/tiny-bt

**dcreater**：
YouTube has so many truly wonderful videos on chip production. I admire your approach but it seems like a lot of people are in this ai maxxing phase where they reach for ai for everything despite their being ready, high quality things already available for free

> **AlotOfReading**：
> I'm also not sure you can really learn chip production from widely available public information. It's a hugely complex industry where the details tend to shape larger strategies. For example, you can't really understand the relationship between Micron and TSMC without some awareness of the trade-offs of memory processes for peripheral transistors.

> **tayo42**：
> YouTube is just a big dump of information. Having a structured way to learning along with interacting helps you learn. Otherwise you're just binging information

**spacedcowboy**：
Another, possibly easier, way is to ask an LLM to give you a quiz on a topic, and then discuss your answers with it.

Surprisingly effective.

> **chasd00**：
> I had an internal company assessment I needed to pass before end of our fiscal year. The study material consisted of 10 ppt decks about 80 slides each (so around 800 total). I had an AI read all the decks and compose a study guide with quizzes along the way. It came up with a 100page word doc that I used in place of the decks to prepare. It worked very well for this including, like you said, quizzing me over various sections.
> 
> (Yes I confirmed it was ok to use AI with the material)

**user-**：
The little tool it outputted is nice, but click around the stages and the text is not high quality at all. The snippy titles, abbrievated explanations, I wish a few more iterations and thought was put into the actual main textual content. Especially for 'complex' stuff

**dwa3592**：
i looked at the animations, they look cool, and i don't think i will enjoy learning things that way. as someone else said, there's a lot of content already produced on these topics. i also think the level at which these animations are playing, they are actually hiding the 'complexity' of these topics.

**latent-l**：
Very cool, I like the visual learning nature of this and the auto play once starting. The game graphics are engaging which counts for a lot these days, I feel my attention span suffering after using agents for the past year.

I've been working on a similar process of pushing to github pages, but focused more on having "practice sessions" with coding blocks to test content. Using webassembly and mock servers to mock backend endpoints Here's one I built to build a full stack llm chat system in the browser.

https://model-systems-labs.github.io/latent/llm-systems/lessons/conversation-state/

**ultra_nick**：
Oh, I do similar, but using single page websites.

Last month, I read The Prince and had it make a text adventure campaign for me.

For a lot of other topics, I often just ask it to create a simple python example that I can run.

**fosterfriends**：
I love this idea!

**brcmthrowaway**：
His other project, https://aivestor.tech/, seems like a huge grift.

> **gavmor**：
> Or is it just an unproven attempt? Seems like a pretty straightforward value proposition. Caveat emptor.

> > **aswegs8**：
> > If you know anything about investing, you know it is highly likely to be either A a grift or B an innocent, but naive attempt.

> > > **gavmor**：
> > > I don't know anything about investing, but I know a lot about naivete. :)

> > > **8bitsout**：
> > > From the website:
> > > 
> > > "Quant Competitions Achievement
> > > 
> > > In 2024, I achieved 7th place at Quantiacs, a global quantitative trading competition. With a background in financial software, I built AIvestor to democratize AI-powered investing tools that were previously only available to institutions."
> > > 
> > > I have no idea of the legitimacy of Quantiacs, but for someone with these claims what they are selling is extremely unfaithful. Anyone with a sufficient knowledge of markets would understand the issues with what is being presented on the "portfolio" page, and the approach is bunk.
> > > 
> > > It appears that the product is based on some vibe-coded slop (https://github.com/LaurentiuGabriel/gpt-trading-agent). I personally would feel bad even thinking about trying to sell something like this to people.

> > > > **brcmthrowaway**：
> > > > "Democratize" in 2026 means "sell".

> > > > **laurentiurad**：
> > > > This post went a bit too far with the accusations and therefore I am responding. First of all, I am not sure why you felt the need to search for me on the Internet, considering the original post has nothing to do with this SaaS. Do you really have that much free time and you don't know how to fill the gaps that you start researching and potentially doxx people?
> > > > 
> > > > Quantiacs is absolutely a legit competition. If you are interested in quant trading it's impossible not to have heard about it. Here I can see that you have absolutely no clue about this field, which is fine, but don't act as if you're a market guru which "knows about current markets".
> > > > 
> > > > I don't know what knowledge you have about the current markets, these stocks shown on the landing page are picked by the agent. The SaaS I built is built on the OSS chatbot I created. I host it on a machine I pay for, I change the models frequently and you get support for any technical issues. People can still use the OSS agent, but they need to host it themselves, use their own API keys, do changes themselves etc.
> > > > 
> > > > I have no problem selling something that works for me and that I worked hard to bring up and I don't care what a random on the internet has to say, but do not spread misinformation about something that you have no idea on how it works.

> > > > > **8bitsout**：
> > > > > You literally have a link to your Github on your SaaS product - are you that dense? You included your whole profile on there. It took me no more than 5 minutes to click it, see that you have a repo related to your product, and view one source file of AI slop.
> > > > > 
> > > > > Anyway, I stand by what I said. Advertising with "Look, AI picked my stocks and number went up" is disingenuous.

> > > > > > **laurentiurad**：
> > > > > > There's no reference to AIvestor in the article I shared. You decided to dig through Google, GH and what not to find stuff that could potentially be used against me personally and you really failed, exposing yourself as a rando sore loser on the Internet.

> > > > > > > **8bitsout**：
> > > > > > > That's correct, there is no reference to AIvestor in the article you shared. However, the parent comment of this thread, the one I responded to and the one you are responding to, shares the link to your AI slop product. Once again, I did not have to dig through Google at all - it's all available on your product page. You're repeatedly proving how dense you are.

> **laurentiurad**：
> What does this have to do with the topic?

**fosterfriends**：
Is there a way we could turn this into a reusable skill?

> **laurentiurad**：
> Yes! I added it here: https://github.com/LaurentiuGabriel/learnscape

**f311a**：
What’s everyone’s opinion on learning new tech things in this day and age?
My opinion swings between positive and depressing vision of the future.

I still learn new stuff, but I’m afraid it won’t have any value in a year or so.

For example, I’m pretty good at optimizing low level stuff, but right now you can just ask LLMs to do so and they are pretty good at it. They will profile the code and suggest reasonable options like 90% of the time.

> **SketchySeaBeast**：
> > I still learn new stuff, but I’m afraid it won’t have any value in a year or so.
> 
> This is silly.  This would be like arguing that encyclopedias made knowing things pointless.  I learn new stuff for me.
> 
> Professionally, it's important to know enough to know if you're going in the correct direction.  Practically, tokens are going to continue to cost money and knowledge can save you tokens.

> **shannadige**：
> There’s still an immense value in training the brain to learn and be able to approach new problems with the sort of procedural thinking that LLMs enable. We can explore topics that we are curious about and develop that sort of “muscle” to continue asking questions when we have them. I have no fear that when those bigger (and existential) problems arise we’ll be well equipped to keep asking questions and figuring out ways to solve them.

> **SkyeCA**：
> > I still learn new stuff, but I’m afraid it won’t have any value in a year or so.
> 
> I have stuff to do now, the value of the knowledge in a year or two isn't important if it solves the issues I have today.

> **brudgers**：
> One possible value in learning new things is developing a habit of learning.
> 
> In particular it might be valuable to be in the habit of learning things that one is bad at *doing.*
> 
> Or not.

> **cautiouscat**：
> I can only speak for myself, so I hope this resonates with you.
> 
> I wasn’t even really concerned with optimizing low level code before LLMs and that wasn’t why I was hired either.
> 
> However following that low level thread: We can look at the reasonable options and immediately know if they’re reasonable or nonsense. Why? We know the code. Now zoom a level out, where I think our expertise really lies.
> 
> Building a complex system isn’t easy. There are customers with requirements, there are budgets, SLAs etc. Sometimes one customer needs X and one needs Y. Our expertise is taking all of this in, and producing something that balances all the different variables. It’s knowing that we’ll expect *X* events a second so we’ll need *Y* to ensure we can tolerate failure.
> 
> Is it possible LLMs will be able to do all of that too? Maybe. But then why would our customers need the enterprises they pay for?

> **eterm**：
> They're amazing at it, provided you keep asking the right questions.
> 
> Trust me when I say that in the hands of someone who doesn't have your experience, the LLMs would not be getting the results you get.
> 
> You might think what you're doing is trivial, it may be sessions that flow roughly, "Instrument this, okay this part is slow, profile this part, OK read the profile output and suggest a better approach".
> 
> But your experience will be steering it in the right direction, and you're probably unaware of just how much your experience is doing that guiding, as the LLM shoots off at 100mph, you feel like it's taking you with it, but you will be guiding it a lot more than you realise, and that's where learning and experience comes in, even if you're no longer operating at the lowest depth, your knowledge of that layer will be helping.
> 
> If nothing else, the experience to know when something is actually slow is a skill in itself. If a function takes 200ms, sometimes that's as quick as it can realistically go, and sometimes that's literally a million times slower than it could be, and there's actual skill and experience wrapped up in knowing what "slow" looks like.

> > **wonnage**：
> > “asking the right questions” is built on years of experience doing the things now being offloaded to AI
> > 
> > “asking the right questions” is also a moving target with each model release
> > 
> > People simply underestimate the value of doing the work and think that the end result is all that matters

> > > **RunSet**：
> > > > “asking the right questions” is built on years of experience doing the things now being offloaded to AI
> > > 
> > > https://en.wiktionary.org/wiki/eat_one%27s_seed_corn#English

> > **therepanic**：
> > So what should newcomers do who haven't yet gained enough expertise to ask LLMs the right questions?

> > > **lfx**：
> > > Newcomers have to do exactly the same what they did years and years ago. Practice the craft and gain experience by doing things.
> > > 
> > > And the craft is loose term, it can mean anything you like to get better at.

> > **AmbroseBierce**：
> > Except the steering itself is also disappearing, the same prompts from just 6 months ago now need much less steering, AIs are learning to even ask back in certain cases to persuade people  with no experience towards the most likely correct choice

> > **jack_pp**：
> > > Trust me when I say that in the hands of someone who doesn't have your experience, the LLMs would not be getting the results you get.
> > 
> > https://code.ffmpeg.org/FFmpeg/FFmpeg/issues/23049
> > 
> > So there's this 11 year old issue in a forgotten ffmpeg plugin and I fixed it with deepseek by putting it into a self-testing loop. Probably would have taken me a few weeks to even understand the initial code to begin with. I haven't done C work in a long ass time and have zero knowledge of even what sub pixel sampling means.
> > 
> > With DS4 took me a few days and a couple of dollars. And by few days I mean I checked on it a few minutes every half hour or so a few times.
> > 
> > I don't understand the code it wrote but it's been in production for a while now and no issues so it's good. Ended up speeding up our video processing pipeline by 20-30%.

> > > **9dev**：
> > > So while I do agree that it is cool you were able to do this, I‘ll say:
> > > 
> > > Sending in the patches but refusing to take responsibility for them is a surefire way to contribute to maintainer burnout. Please don’t do this. Either commit to fixing something and driving the PR to merge, or abstain from it entirely.
> > > 
> > > The bottleneck isn’t the speed of coding, and what you’re doing here is actively worsening the situation.

> > > > **jack_pp**：
> > > > idk if it's really worsening, someone who has the same issue can apply the patch. I understand why they rejected it but also I'm not willing to learn everything that DS4 did there since I don't plan on working on ffmpeg filters and the knowledge is pretty much useless to me outside this patch. Too much time commitment for.. fixing a filter no one really cared about for 11 years.
> > > > 
> > > > But you can see how the parent's comment doesn't really hold, I was able to achieve this while not knowing anything other than what I need fixed and making the LLM test itself towards that goal.

> **jazzyjackson**：
> I decided to learn watchmaking instead

> **catlifeonmars**：
> I don’t agree with the implication that there has to be a practical reason to learn new things. I enjoy learning new technologies because it’s fun.

> **8bitsout**：
> I mean, part of the reason the LLM can do that is because you know enough to direct the LLM to do so and verify the results to some degree, right? It's good to learn new things because:
> 
> 1. It satisfies you curiosity (and curiosity is always valuable)
> 
> 2. You can better utilize the LLM to expedite something you now have knowledge about
> 
> 3. You still improve as an engineer/programmer/prompter/whatever
> 
> I still think it's very important not to outsource everything to AI because there is a lot of value in learning and doing things yourself which is an important part of life.

> **simonw**：
> There's a big gap between being able to ask questions about something and *understanding* something.
> 
> The more things you understand, the higher the chance you'll spot a situation to use them in the future.
> 
> I think the best innovations come from times when someone is uniquely able to combine two of their previous experiences together. The more experiences you have in your back pocket the more combinations you have access to and the more likely you'll have a unique combination when the right problem comes along.

> **numpad0**：
> So you think building a warp drive is pointless because 99% of work, per your judgement, will be done by AI? Is your contribution meaningless and artifact useless? I wouldn't think so.

> **AnotherGoodName**：
> I sometimes get vague ideas for solving maths/science problems. They never pan out but i can talk in detail on group theory and advanced maths and science topics due to investigating such vague ideas over the years. These days the LLM shoots the ideas down instantly and honestly correctly, i know enough to know "yeah that's right, oh well" and move on. Which actually takes away a huge avenue of learning. I'm pretty torn on the outcome of this honestly.
> 
> I'm not 'wasting time' but I'm also not really learning.

> > **le-mark**：
> > I felt this. I had a feeling for a long time that spider solitaire was somehow related to knot theory (legal moves being Reidemeister move equivalents and untangling). Llm shot this idea down very quickly! It was freeing actually.

> > > **fluoridation**：
> > > Both of you are being overly dismissive of yourselves. Without either a proof or a program that proves the statement in question, I wouldn't trust the LLM. I wouldn't even trust if it produced citations, because I've already come across LLMs citing sources to back up statements without being able to find that information in the source (not saying it wasn't there, just that I was not able to find it).

> **tunesmith**：
> Generally speaking, the pattern is that people are overestimating how much "work replacement" will happen, and underestimating how much "work shifting" will happen.
> 
> What is fascinating is how you can witness it at so many levels of organization. One example: Employer executive get enamored with moving from labor to capital. They believe that by using LLMs, they can replace a lot of workers. At my place of employment, we have people that are surprised they can't file a Jira ticket describing a product ask, and have it kick off an implementation. You can build the skill to attempt that, but invariably you'll get back questions like "what do you mean by <x>" and "what do you want to do in this case, a, b, or c?"; questions that a product person or an exec are not well suited to answer.
> 
> In the past, programmers did that kind of interpretation and judgment call. So then you're in a quandary; who should do that work? Work that previously, you never imagined was an inherent part of what the replaceable code monkeys do at your beck and call?
> 
> And then, how do you hire for that? How do you find the training for the people that are experienced enough with... something... to know what a cohesive error response is, or what kind of telemetry strategy is best for that particular product and organization, what collection of product asks are incredibly complicated for what they're asking and can deliver 95% of the benefits at 5% of the work if we just do this instead, and whether you want to aim more towards thick or thin clients?
> 
> Who are those people? Wait, those are programmers? Wait, there's this whole collection of inherently human skills that we devalued, by not appreciating they were always quietly doing that for us in the past?
> 
> That's just one example. There's a repeating pattern of discovering where the work truly is, work that was embedded in manual patterns we might not have to involve ourselves with anymore, but is yet still essential. So the nature of our jobs changes massively, but the overall level of employment does not.
> 
> At least, not in the medium to long term. There is a lot of painful churn we have to suffer through first.

> > **Calazon**：
> > I agree with you in the broad strokes, but replacement by LLMs isn't the only way the level of employment can be reduced. If LLMs can make it so that two programmers can do the work that used to require five, that can result in a very large reduction in employment, even while having (some) programmers is still essential.

> > > **tunesmith**：
> > > On the bet that layoffs will result in programmers ending up at 40% of the staffing level they are now, I will take the over.

> > > > **Calazon**：
> > > > What sources do you think are good for this data for the recent past? My brief initial search is turning up a lot of contradictory data, probably because the sources are defining "programmers" differently from each other.

> > > **killingtime74**：
> > > Only if there is no further additional demand created by the now lower cost of doing the work. Take lighting as an example. As it has progressed from burning expensive candles to now leds, our demand for lighting has continued to increase.

> **laurentiurad**：
> The way learning new stuff rewires your brain cannot really be predicted, but the effects are positive.

> **kccqzy**：
> It depends strongly on the prompt. Like recently I was also doing some performance optimizations, and if I did not mention profiling none of the LLMs even profiled the code; they merely read the code and assumed, based on their own analysis of big-O time complexity. It is after I explicitly asked for profiling that the LLM started actually profiling.

> **ofjcihen**：
> I have staff ranging from 10 years of IR experience to right out of college.
> 
> I can tell you that there is an enormous gap in ability between them despite them both using LLMs for daily IR work.
> 
> The reasons aren’t complicated. The senior responders have tacit knowledge of how breaches evolve and what to look for which gives them a much better framework for where to employ the LLM.
> 
> The juniors will normally start from “here are some logs, look for weird” which is fine but leads to tunnel vision and a lack of confidence in their reporting.
> 
> I don’t mandate that anyone do work with or without an LLM. I hire seniors based on experience and juniors based on interest. But my experience has so far been that our best up and comers focusing more on learning the technologies instead of leaving those details to the LLM are developing their intuition and understanding faster and in a more robust manner.

> **maplethorpe**：
> I'm choosing to (mostly) switch off the news and continue learning things I find interesting anyway. Maybe the world will punish me for it at some point, but I guess I'll have to deal with that when it happens. The alternative is too depressing otherwise.

> **tarkin2**：
> Not good at subjects you have no previously learnt knowledge.
> 
> They tell you have "hit the nail on the head" when you really haven't.
> 
> They tell you have had a "great insight" when you are really haven't.
> 
> They give you the illusion of learning and progress but essentially give you faulty preconceptions will trip you up further down the road.
> 
> You can  ask the LLM to be more critical and less sycophantic but that only gets you so far:
> 
> They want you to continue using, being dependent on and feeding data into the LLM--your independence isn't a priority.

> **yoz-y**：
> Purely personal but as I get older I am tired of learning new things and would just rather learn old stuff.
> 
> Career-wise, this is terrible. But for me technology was polluted by the ever-growing greed.
> 
> For example I’d much rather actually learn assembly, than learn the nitty-gritty details of how LLMs work.

> **einpoklum**：
> If people don't learn, and write, and converse, about new tech, the LLMs will not have raw material to learn their slop from. And I am quite worried that this is the direction we're going in, with the lake of insight being sipped dry and a future of shallow cliches as LLM responses.

> **vilfred_sikker**：
> I'm also trying out a lot of different approaches, and generally I like the sparring I can get from LLMs but with the acceptance that they make mistakes and some things still need some fact checking. But the models are improving fast, so I'm positive about this approach just becoming better going forward
> 
> I'm working on a side-project called tech-professor.com which is a platform for learning. The content is built directly from the source code in your pull request and repositories you follow. So you can quiz yourself and your team based on the code you ship.
> It's in beta and a lot of changes are still on the way, but if you want to check it out and give feedback, feel free to sign up for free.

**royal__**：
The biggest thing I've learned from doing stuff like this is that there are no shortcuts. At some point or another, to truly learn something deeply, you've got to dig in to the boring details and do things the hard way. LLMs can help with this...but I find it's usually tempting to try and just offload the boring stuff to them, which doesn't work.

> **hahahacorn**：
> Having an initial higher level understanding across the domain is extremely useful to contextualize the deeper stuff. I think boring details is a very leaky characterization, but I'll continue with it.
> 
> In my experience it's infinitely easier and faster to learn deep, "boring" things when you understand how they relate to your shallow and wide understanding of all of the related components.
> 
> The LLM is merely a tool. And you can use it for domain discovery that enables efficient deep learning at an unprecedented rate or you can develop a cursory understanding of a topic and think yourself an expert.

> **ainch**：
> Quite - you still have to do the work yourself. I think LLMs are best placed to act as an eager tutor that doesn't mind discussing a topic ad nauseam until you're certain you understand it.

> **yoyohello13**：
> I’ve found that if I’m not struggling I’m not learning. If stuff is coming fast and easy that’s a sign that what I’m doing is not stretching existing skills enough.
> 
> It’s true of most things. Running, dieting, weightlifting being uncomfortable is a sign of progress.

> > **djaro**：
> > This is also why apps like Duolingo don't work for most users. They want to turn language learning into a fun, effortless game but effortless is fundamentally incompatible with learning.
> > 
> > Learning is uncomfortable. Reading a difficult (for you) text in a language you don't understand is exhausting and confusing. But that is where improvement happens.
> > 
> > Its even worse since Duolingo added a life system (not sure if they still use it), where you were only allowed to make 3 mistakes before having to recharge your energy. If you get everything right, you are not learning, you SHOULD be making mistakes constantly. That shows you're actually being challenged.

> > > **hlovdal**：
> > > > If you get everything right, you are not learning.
> > > 
> > > One of the teachers on the college I went to had a note on his door with "If you understand everything you're doing - you're not learning anything.

> **mhh__**：
> yes i've found that there are a few topics that i've really been able probably 10x my understanding of using LLMs, in particular in getting me over hoops that are hard to navigate when solo, BUT I have to be really careful for it to not just show me the answer all the time.

> **AdieuToLogic**：
> > The biggest thing I've learned from doing stuff like this is that there are no shortcuts. At some point or another, to truly learn something deeply, you've got to dig in to the boring details and do things the hard way.
> 
> This is the only path to mastery, or understanding if one prefers. There are no shortcuts to a person achieving deep understanding (a.k.a. "Aha!" moments).
> 
> Can a tool such as GenAI be beneficial to someone who already has done the work to understand? Absolutely. But it cannot infuse mastery into a person simply by its use.
> 
> Only the time and effort a person devotes can do that.

> **mfalcon**：
> The LLMs are a way to get quick feedback and getting it promotes quicker learning (if the feedback is good). Learning is difficult, sometimes I get blocked on something and before llms that could prevent me from learning some material, nowadays I have another tool to help me unblock and learn faster.
> 
> I think that could be called a shortcut, not in learning per se, but in the process of getting to learn.

**NBJack**：
My favorite way to learn infra topics at work right now is asking for a humorous analogy involving monkeys and bananas. I tend to remember the result, and it gives me reference points for new topics.

**wxw**：
> What you get is a beautiful animation that is 100% accurate and free of hallucinations.

I'm not sure I follow how this is actually guaranteed? The fact-checking process mentioned just seems to involve asking AI to review its own work.

> **dozerly**：
> All these LLM-as-review hype pieces don’t acknowledge that it’s turtles all the way down

> > **enraged_camel**：
> > What do you mean by this?

> > > **Gander5739**：
> > > If the output can't be trusted, and you use another llm whose output can't be trusted to check the untrusted output of the first llm, then you're back where you started.

> > > > **duncangh**：
> > > > Yeah this seems to me similar to how the mortgage backed security risk concentration occurred leading up to the global financial crisis. Whereby the risk from exposure to low grade / risky single mortgages was eliminated via diversification but the diversification was simply packaging all of the risky MBS’s together and in no way diversified or de-risked the entire portfolio

> > > > > **Terr_**：
> > > > > I'm hoping that the Big Horrible Realization comes sooner rather than later, when we have less collective damage and pain riding on it. (Plus I'd feel personally vindicated.)

> > > > > **cromka**：
> > > > > I don't see it. To me it's like having e.g. 3 drunk PhDs arguing between each other to settle on truthful answers to questions.

> > > > > > **DrewADesign**：
> > > > > > But the problem with LLMs is that they get the *facts* wrong. PhDs are PhDs because they’d look it up in an authoritative source, or actually find out through research and experimentation. The whole point is that facts aren’t a matter of opinion. The only people that argue over documented, findable facts are idiots that nobody should listen to.

> > > > **daishi55**：
> > > > Not really. Take hallucinations for example. If they are 1 in 100 (actually they are much rarer, but for the sake of argument), then the chances that 2 LLMs or even just 2 runs of the same LLM have the same hallucination is, well, a lot less than 1 in 100.

> > > > > **Terr_**：
> > > > > That rests on a false-assumption that the errors are statistically independent events, and have nothing to do with the shared nature of the judges.

> > > > > > **daishi55**：
> > > > > > Are there any reproducible hallucinations on any of the currently available OAI/Anthropic models? I’m not aware of any.
> > > > > > 
> > > > > > And even if they are related - if Opus 4.8 always has a 1:100 chance of a specific hallucination - then running the same model twice does indeed dramatically reduce the odds of an error in the final output.

> > > > > > > **Terr_**：
> > > > > > > If simply running things thrice-over was enough to stop "hallucinations" (and not incur other problems) we wouldn't be here talking about it today, it'd have been "solved" months or years ago.

> > > > > > > > **daishi55**：
> > > > > > > > I mean they have been solved practically I think. I use these things all day every day and haven’t seen a hallucination in a long time.

> > > > > > > **djhn**：
> > > > > > > Constant hallucinations. OpenAI:s latest on max settings. If you are to naively feed say, a short corpus of text to turn it into a parallel corpus in a few different languages, the original text gets subtly mangled and no longer matches the original. Say you have several hundred annotated sentences. Without hand-coding some regex to make sure that each sentence in the source column occurs in the original corpus you’re bound to get hallucinated sentences with an error rate that exceeds 1:100. Whatever you use as the output, JSON or XML, you will end up with columns that just repeat the original instead of translating it, especially for languages that are very close to each other or represent the same language.
> > > > > > > 
> > > > > > > Yes, LLMs can be SOTA for NLP, but you’re going to have to use them to write software or workflows that are more deterministic.

> > > > > > > **fluoridation**：
> > > > > > > Even if your conditions are granted, different LLMs can easily consistently hold divergent "worldviews". LLM A might consistently state that fact P is true (i.e. it will never hallucinate a string that states or implies ¬P), while LLM B consistently states that fact ¬P is true. You don't have a way out of this with these two, and adding a third LLM is an additional confounding factor, not a solution. You can't settle questions of fact by survey, you need to test or use reliable sources.

> > > > > > > > **daishi55**：
> > > > > > > > This is really a theoretical problem and not a practical one though. Practically, for everything I use these tools for today (complex low-level systems programming), hallucinations don’t even exist anymore.
> > > > > > > > 
> > > > > > > > When they don’t know something, they figure it out empirically. For things they already know, they are consistently correct.

> > > > > > **Systemerror7A69**：
> > > > > > It's also relying on the assumption that the checking LLM only ever corrects wrong statements and never incorrectly "corrects" an already correct statement, which might not always be the case as well.

> > > > **ex-aws-dude**：
> > > > No you don’t get it, I asked it specifically to make sure it’s accurate

> > > > **northern-lights**：
> > > > Unfortunately, I don;t think that can ever be fixed. For an LLM to know that it is not hallucinating about something, it must know that that statement(s) is/are true. Which it cannot infer due to Godel's Incompleteness theorems.

> > > **phatskat**：
> > > I read it as “if your LLM is being checked by another LLM, well then you need another LLM to check the checker. And can you really trust _that_ LLM? Probably should have an LLM to check the third one, and…”

> > > **furyofantares**：
> > > "Turtles all the way down" is a phrase of, I think, unknown origin (https://en.wikipedia.org/wiki/Turtles_all_the_way_down) about infinite regress or trying to patch up some bad theory by appealing to itself. Someone claims
> > > that what holds the Earth in place is that it sits atop a giant turtle, and a skeptic asks what holds the turtle up, and the response is that it's turtles all the way down.
> > > 
> > > Personally I think this is a bad characterization of using LLMs to fix up LLMs because while you can never guarantee results this way (as the quoted line claims here, which is worthy of criticism), it is, in practice, useful to use LLMs on top of LLMs. And there's no infinite regress. Auto-mode in Claude Code, for example, seems to me like it's been successful at making the system more safe than --dangerously-bypass-permissions without prompting the user for permissions constantly.

> > > > **dozerly**：
> > > > There are certainly uses where it’s good enough, but you can never be 100% certain of correctness in the way that people claim you can by stacking N layers of these models.
> > > > 
> > > > What triggered my response was the “just review the output with another LLM and it’s perfectly correct”

> > > > **TooSmugToFail**：
> > > > I would have bet it’s a Terry Pratchett quote, and it kinda is:
> > > > 
> > > > “"The turtle moves," said Didactylos. "The turtle is a giant reptile that swims through space. It doesn't have to stand on anything. Swimming is what turtles do. The idea that it has to stand on another turtle, and that turtle has to stand on another turtle, is just silly. It's turtles all the way down, and that's a logical absurdity."
> > > > 
> > > > Small Gods, 1992

> > > > > **furyofantares**：
> > > > > He's using it but if you CTRL+F the linked wikipedia page for 1967 you get someone using that exact phrase, or for 1882 above you get a pretty close version.

> > > **tclancy**：
> > > It’s a reference to Bernard Shaw, who once said that if we ever created a truly artificial mind it would be inside a turtle’s shell. Sturgill Simpson covered the track on his seminal work, Xeno’s Paradox.

> > > > **eyepea2007**：
> > > > an LLM tells me there is no evidence that Bernard Shaw ever said any such thing :)

> > > > > **arvid-lind**：
> > > > > It's Sturgill Simpson all the way down: https://en.wikipedia.org/wiki/Turtles_All_the_Way_Down_(song)

> > > > > > **tclancy**：
> > > > > > In my defense, I was suffering from white line fever.

> > > > > **tclancy**：
> > > > > Well sure, it was George Bernard Shaw, not the old CNN anchor. Also, turtles are tight lipped by nature.

> > > > **Dumblydorr**：
> > > > Might be a reference to the story at the beginning of A Brief History of Time, attributed to Bertrand Russell’s audience member.
> > > > 
> > > > Full story in the book

> > > > > **tclancy**：
> > > > > This guy remembers what I thought I was saying. In my defense I stole the whole thing from Stephen King’s It which I read … forty years ago, that can’t be accurate. Let me sort out my instruments and get back to you.

> > > **latexr**：
> > > Other comments have answered in the concrete what was meant, but to answer in the abstract, in case you’re unfamiliar with the expression:
> > > 
> > > https://en.wikipedia.org/wiki/Turtles_all_the_way_down

> **bryanrasmussen**：
> I could certainly envision a scenario whereby review would increase reliability but not how it would every guarantee 100%, there is a pretty big logical gap there.

> > **laurentiurad**：
> > In my experience it depends on how much in detail you want to go. Chip manufacturing is a really opaque industry, so in this particular case LLMs might not even have the training data. However, using it for a high-level introduction into something is usually pretty safe from hallucinations.

> **hn_throwaway_99**：
> Completely agree. While I didn't set things up to have AI review its output in a loop, my experience trying to build a specific acoustic testing rig with Opus 5 also aligns with the other "it's turtles all the way down" comment.
> 
> Opus 5 first built me a detailed plan, but a couple important details were either obviously wrong or felt unnecessary. I went back and forth asking for sources and more information probably like 4 times and *every* time it did the "in looking at things in more detail it appears my previous advice was incorrect" spiel. It just became exhausting at some point because it feels like it really lays bare how LLMs are just minimizing that loss function but don't actually "understand" anything. It was really useful as a search engine (it correlated some highly relevant source docs), but I just couldn't trust it to believe it was actually done at any step.

> > **knollimar**：
> > A second agent reviewing it adversarially resolves some context rot.  Whatever they trained these LLMs on will just infinitely double down so I break it with 1 layer of checking and then a judge who looks at facts, since the checker is adversarial.
> > 
> > I know it sounds silly but 1 layer ends uo being way worse than 2.

> **tempacct2cmmnt**：
> Agreed. Given how many significant errors LLMs make in my topic of expertise, despite my taking multiple error checking steps, the idea of catching 100% of hallucinations because you told the LLM to check itself is hilarious. It’s just a wild lack of insight: “I’m using the LLM to teach me something I don’t know about, I definitely have the knowledge base to spot any errors that might remain!”

> > **DrewADesign**：
> > Yeah. People with technical and/or tech business bonafides claiming that AI granted them expertise are so often taken at face value when they really shouldn’t be. Who told them that they were proficient — a chatbot? Someone who knows even less about the topic, so any expertise seems impressive? I’ll bet it wasn’t someone that actually knew what they were talking about. Even some tech reporters are tripping over themselves to be amazed, but don’t bother checking if they should be.
> > 
> > People don’t even have to be lying to be wrong about this stuff. Someone can learn enough about a topic to be halfway up Mt. Stupid in no time flat, and in doing so, think they not only *truly understand* the topic at hand, but might be *particularly adept* because they were such quick studies. People that know less are  impressed, because why wouldn’t they be? Anybody that knows more than them sounds like an expert. And people that know what they’re talking about cringe at the overconfidence,  and probably try not to engage: who wants to have to prove that someone’s boundless confidence is *entirely baseless?* Most of the time, they think the actual expert is full of shit because they think they’re the expert. It’s incredible how many times I’ve had people in tech confidently, even smugly “explain” design concepts and strategies to me that they did not actually understand, knowing I was an experienced, degree-holding designer… and they didn’t even have a chatbot’s lips on their ass telling them how smart and insightful they were.

> **a3w**：
> I thought after reading the title that the text was about learning something, yet the actual text seems to be about having a system do something for me.

> **spike021**：
> even if you say use RAG or something to a source you can trust, there's no guarantee the agent will still use exactly what the source has.
> 
> i can't even get agents to remember core instructions like "use jq instead of writing a python script to parse some json"..

> **63stack**：
> You can add "make no mistakes" to the end of the prompt and achieve the same result while burning less tokens.

> **lowsong**：
> Yep, that's impossible. The hard truth is that most people this lost to LLM psychosis cannot understand that fact. It's better to treat it like someone in a cult, arguing the facts isn't going to help if they refuse to accept them.

> **zahrevsky**：
> I don't do animations, but I have an answer. You research a topic well enough to be able to understand if the result is OK or not. Usually it means figuring out some sort of testing.
> 
> I'm researching causal inference right now, and my main goal was to make sure I understand how to test estimation on synthetic data.
> 
> Basically, it's the same way it works with people. If you delegate a task that you don't understand, and you can't have a credibility proof (i.e. doctors, lawyers), then you research a topic well enough to be able to (1) define the task and (2) verify the end result.

> **SwtCyber**：
> The "100% accurate and free of hallucinations" claim should probably be replaced with something much weaker

> **nedt**：
> I'm just looking at the rocker engine piece. The belt is running backwards. That's the first thing I'd expect it to get right or flag if it doesn't. Human in the loop is also the quality control. If that fails the rest might have similar issues.

> **rootlocus**：
> OP posted his rollercoaster tycoon inspired simulator that explained how chips are fabricated. Comments were full of people pointing out inaccuracies and hallucinations.
> 
> The problem with LLM explanations of unknown topics is that you literally cannot determine how right or wrong it is. I usually ask LLMs to bring references and they almost always admit they pulled random shit out of their ass and quickly appologize when evidence to the contrary surfaces.

**ElijahLynn**：
This is a great share, gonna come back to it.

Also worth mentioning that Matt Pocock has a /teach skill that creates interactive, learning sites for learning a new skill.

> **sathish316**：
> +1, you can customize it to learn any topic concisely, learn by doing, add challenges, add visual explanations
> 
> https://github.com/mattpocock/skills/tree/main/skills/productivity/teach

**0wis**：
Really neat idea, I think it is one of the best ways to exploit the combined building and explaining capabilities of LLMs.
I am currently building an app/game to explain friends and family concepts around wealth management and wealth building. Games are a great way to hide complexity while still including it in the « guide » you are making.

**meerita**：
I use LLMs to learn deep technical concepts. I really like them because I can spend countless hours a day understanding things and building an investigation file with all my findings. I code examples and test the findings. It has helped me understand basically anything.

I'm using LLMs right now to build a terminal browser, a GUI browser, and a PyTorch/LibTorch replacement. It's really fun to be able to learn and make progress this way. It's like reading multiple interactive books, where every concept can be explained again and again until I understand it.

**cautiouscat**：
I’ve written a skill that I basically feed what I’m looking to do, some ideas I had for accomplishing it and any other details like tech stack, etc.

The skill then riffs with me, judging my ideas and suggesting alternatives. We go back and forth until something useful comes out of it. This process isn’t unlike how I do normal development.

However, once agreed it breaks the work into “steps”. It then creates a tutorial for me, for those steps, explaining each line, why each change happens etc. I can then ask questions, muse about an alternative idea etc. Then I do the steps, and I’ve learned and gotten what I wanted to get done.

This has been how I’ve been learning Godot and making a game for the past month or so. I didn’t go in blind, I started with a course from GDQuest so I could feel confident guiding the tutorials. I will say though, having a tutor to bounce ideas off of has been really useful.

I still try to figure it out myself, consult the docs, discord etc. But if I’m stumped I’ll run my tutor skill and have some fun.

> **vorticalbox**：
> I’ve started doing a similar thing after reading a post on hn about manually applying the code so that you actually understand it.
> 
> I have done this for all my work this week and it works quite well.
> 
> For one it lets you actually query the LLM as to why, their plans give a high level not every single change and it allows you to correct it as you go and the plan will change.

**hathym**：
Too over engineered, few text paragraphs would suffice to understand the topic.

**SalaevAl**：
LLMs can help you understand a language, but they can't replace learning the vocabulary. Words and phrases still need to be learned the old-fashioned way: repetition

**tuvix**：
I don’t think I really agree with the author’s approach here, but I will say LLMs have been a huge help to me as I’ve been reviewing linear algebra and diving into signal processing. Anything in a textbook that I don’t fully grasp or am confused about, I just take a snapshot or copy paste then ask a model to derive it or explain it in different terms.

It reduces friction a ton, but at the end of the day I’m not skipping anything.

**8bitsout**：
I thought LLMs were a great tool for learning new topics - perhaps even complex ones. But overtime, I have had several frustrations with this. First, I get exhausted reading LLM prose. I really don't want to read anything generated by something like Opus 5 at this point. Second, as I dive deeper, I need a way to organize the information in a useful way as I begin to branch out in many different directions. I have tried to use the LLM to fix this by having it generate a web page with diagrams and organized information flow. It's an improvement, but I still run into the issues I described in my first pint - LLM prose is annoyingly dense, and the useful information gets lost in a bunch of noise. You can direct it do something like "use plain English and avoid LLM prose - provide only as much information as necessary to demonstrate the point", but it is once again only a marginal improvement.

And then I begin to think to myself that I should just read a book on the topic written by a trusted source who put a lot of effort into teaching the topic properly and presenting the information in a thoughtful way. So, I am back to books and mostly try to use LLMs to clarify certain questions or ideas I have.

> **copperx**：
> It's much better to feed the book to the LLM and ask questions as you read along, instead of asking the LLM to basically write a custom book for you from scratch.

> > **gb2d_hn**：
> > I came across the socratic method recently, and have used it to learn a couple of topics that I was having trouble getting to stick. There are some SKILL.md's available for it. It works for concepts as opposed to facts, and causes the model to guide you to answers through your own reasoning, which is both much more engaging than reading a wall of LLM text and helps the information stick.

> > > **hirako2000**：
> > > I was so annoyed I made a Socratic wrapper based on predefined curriculum:
> > > 
> > > https://adaptive.bounded.cc
> > > 
> > > Trying to diagrams/animations didn't yield good results even with frontier models. But pure text, any model does a decent job.

> > > > **hirako2000**：
> > > > I didn't expect this to be hit by hundreds of request per minute.
> > > > 
> > > > So it may be very slow or become unavailable, back end can't handle that, no caching whatsoever.

> > > **Hardwired8976**：
> > > Can you link the Skills.md?

> > > > **gb2d_hn**：
> > > > This is the one I used https://github.com/bevibing/socrates-skill - in the scenarios where I have used it, I have found it useful

> > > **logicallee**：
> > > what a time to be alive! "if you're having trouble understanding what your robot tutor is trying to teach you, you can ask it to guide you to the concepts using your own reasoning. This is both much more engaging than reading a wall of the robot's text and helps the information stick."

> > > **voidhorse**：
> > > The "Socratic Method" (aka maieutic) skills annoy me, precisely because when you read them they are the kind of low-effort, low-expertise crap someone who over relies on AI would naively come up with when tasked with the problem of coming up with skills for learning. "Hey the Platonic dialogues are pretty cool and smart, let's do that".
> > > 
> > > The body of literature on learning theory, and beyond that on specific types of learning and specific mediums such as learning from text is so rich there are *way* more useful models to draw from. Believe it or not, prellm, researchers in the textual learning field had already demonstrated you can achieve performance equal or better than novice tutors using pretty basic computer aids that follow specific hint/pump interaction structures. Guiding an LLM to use these findings has evidence backing it and is way better than telling it "i guess be like socrates". The problem is, to realize there might be richer more effective and highly researched ways of tackling the problem beyond the first fart of a thought you had one afternoon requires the deep respect for expertise and specialization that precisely basically everyone in the AI space right now fundamentally lacks.

> > > > **lambda**：
> > > > Can you provide some references to the research you're referring to? Sounds interesting but you haven't really provided enough information to find it.

> > > > > **pasc1878**：
> > > > > That is the point – you can't just provide the references in a short post here.
> > > > > 
> > > > > You need much more time and guidance.

> > > > > **gf000**：
> > > > > Ironically, LLMs are pretty good at finding stuff like that from vague descriptions. With that, I think the parent commenter meant Art Graesser's AutoTutor work based on the terminology used (hint/pump).
> > > > > 
> > > > > TLDR: Actual human tutoring sessions were recorded and analyzed and Socratic questioning was barely used at all. Instead the following pattern was observed:
> > > > > 
> > > > > Pump — "Uh huh?" "What else?" Costs nothing, so try it first.
> > > > > 
> > > > > Hint — points at the region of the answer. "What about the pumpkin's motion sideways?"
> > > > > 
> > > > > Prompt — fishes for one specific word, with the sentence frame supplied. "The pumpkin keeps moving forward at the same ___?"
> > > > > 
> > > > > Assertion — just says it. "It keeps the runner's horizontal velocity."

> > > > > > **voidhorse**：
> > > > > > Yes, you're on the money. And this is a perfect example of how people *should* use llms. Use them to deepen your own research and understanding rather than use them to glaze and implement the first naive idea that comes into your head (or the first idea they suggest as a response to a vague prompt, which typically is substantially worse than if you get them into the right vector space using jargon)

> > > **copperx**：
> > > > I came across the socratic method recently
> > > 
> > > This statement would out you as someone who didn't attend an elite school.

> > **trueno**：
> > i threw the entire sanderson cosmere into a RAG graph sorta deal just to see how it would do if i questioned an mcp server for it about a universe i know decently well. it was actually astoundingly good. was able to find easter eggs acrossed different books and answer dumb questions like "why is kaladin emo"

> > > **etherlord**：
> > > Sanderson is 100% in the training data

> > > > **trueno**：
> > > > damn it good point

> > > **malfist**：
> > > If you don't know why kaladin is emo, did you truly read the books lol. Every character has to deal with the stresses of war and most don't come equipped with good mental health to begin with, they're just normal people

> > > > **trueno**：
> > > > i was more or less testing to see how complete of an answer it could come up by scanning the whole semantic graph so i threw questions at it that spanned multiple books

> > **calf**：
> > LLM is still too verbose, a real person Socratic conversation can interact a couple sentences at a time, not spew 1-3 windowfuls of low density bullet points.
> > 
> > I even wonder if this behavior is due to next-token prediction architectures, somehow.

> > > **hirako2000**：
> > > There are ways to ground an LLM to be concise, and Socratic (method of inquiry, back and forth dialogue)

> > > **knollimar**：
> > > I don't understand some previous complaints. It's dense and verbose seem at ends to me.
> > > 
> > > I know you probably don't consider it dense but wondering if someone can shed insight.
> > > 
> > > I find them like empty calories, like programming youtube tutorials.  They maximize for feeling learnt instead of steady progress

> > > > **lelanthran**：
> > > > > I don't understand some previous complaints. It's dense and verbose seem at ends to me
> > > > 
> > > > It's dense along the wrong axis and verbose Along the wrong axis.
> > > > 
> > > > Like having acres of cardboard for dinner: you have too much dinner with not enough nutrition. Your dinner is plentiful and still not enough.

> > **schainks**：
> > This. Ask it to quiz you if you are feeling it.

> > **arbitrary_name**：
> > dumb question, but what is the best way to feed the book to the llm?
> > 
> > i run into context window limits, or practical limitations of digitizing the book

> > > **r17n**：
> > > Hoping you get answer to this. I have the same question.

> > > **copperx**：
> > > You need a non DRMd copy of the book. You don't have to feed it all at once, although with a 1M context limit it is doable. A few chapters at a time is enough, in my experience. An easy alternative is using NotebookLM (now Gemini Notebook), and that has worked brilliantly for me, but I haven't tested it for technical topics (for that I like the LLM to create graphs and e.g. interact with Mathematica, so I haven't tried it).

> > **gofreddygo**：
> > I have to agree with this. Completely relying on LLM for all your learning needs is a disaster. But being absolutely against use of LLMs isn't doing you any favors. This is where you don't have a formula but rely on you judgement and evidence of your having learnt something.
> > 
> > For example having an LLM summarize a dense topic and to find books so that you can filter faster and spend time reading those books works way better than having the LLM summarize the books or the topic (or even relying on second hand information). Another one is having the LLM quiz you on your topics of interest. With questions tailored to attack specific areas that you struggle with. Its wonderful at this, nothing I've used comes close to what an LLM can do here.
> > 
> > You define for yourself what your goals are, slowly refining them as you learn more, and use LLM as a tool. This ,I find works best for learning.

> > > **intrasight**：
> > > Make it your goal to teach a room full of other humans that topic. I guarantee you will know that material cold. I've done lots of technical training in my career and after teaching a class two or three times I find myself to be very competent in the topic.
> > > 
> > > It's long been the case that the best way to learn something is to teach something.

> > > > **PsylentKnight**：
> > > > > It's long been the case that the best way to learn something is to teach something
> > > > 
> > > > Which is pretty unfortunate for those that want to learn. I used to enjoy writing documentation at work, it was my favorite part of the job. And it did feel like it benefited me more than it benefited all the people that were (or weren't) reading my documentation. Now I can't really justify spending much time on docmentation when LLM's can do it in a fraction of the time and it's "good enough"

> > > > > **intrasight**：
> > > > > I got started as a software engineer working in the nuclear industry in the 80s. We measured our documentation in inches not pages, and it was all written by hand. And I'll bet you the documentation in the nuclear industry is still written by hand and not by LLMs.

> > > > > > **champagnepapi**：
> > > > > > I sure hope those docs aren’t written by LLMs for many reasons!

> > > > > > > **andrekandre**：
> > > > > > > i wonder if people who use llm's for business critical documentation would have the same opinion, and if so why?

> > > > > > > > **piloto_ciego**：
> > > > > > > > I have used LLMs for safety sensitive tech writing and so have people I know.  It’s pretty good at it, and you usually have a 95% ready to go product at the end of it.  The last 5% can pretty easily be filled in by technical experts with way less time spent battling the type writer.
> > > > > > > > 
> > > > > > > > Is it perfect?  No.  But it suffices most of the time in a pinch.
> > > > > > > > 
> > > > > > > > Can’t speak to the nuke industry, but it’s pretty good at aviation related things.

> > > > > > > > > **intrasight**：
> > > > > > > > > A good compromise would be to have the LLM write the outline. That also helps get over the activation energy of starting.
> > > > > > > > > 
> > > > > > > > > Then elaborate in small chunks so the human domain expert can remain focused during review.

> > > > > > > > > > **piloto_ciego**：
> > > > > > > > > > You don’t even really need to do that…
> > > > > > > > > > 
> > > > > > > > > > You tell it what you need, and it pretty much does all the work:
> > > > > > > > > > > please give me a 135 compliant maintenance manual, use the attached document as a primer, reference every part 135, 91, 43, and 65 reg as appropriate as well as the other included manuals.  Make sure to reference every requirement in the attached list of requirements.  Aircraft mx manuals are in the folder “mx-manuals” and our current forms are pdfs in the “forms” folder.  Remember our operation is <describe scope of operation here>, not a major airline.  Have fun!
> > > > > > > > > > 
> > > > > > > > > > This does surprisingly well and meets requirements at about 95% or better accuracy.  Typically the only problem I routinely is trying to make the manual like a Delta Air Lines manual instead of one for a small air taxi.

> > > > > **unethical_ban**：
> > > > > There is still value in experts distilling knowledge and crafting it to the audience. I'm a consultant in cybersecurity and someone asked me "give me a best practice framework for good policy hygiene". I'm sure an LLM could spit out some tips, but I've been on the industry 15 years and can write in 5 pages what an LLM wouldn't conceive of in that space.

> > > > **metal_am**：
> > > > That's pretty much the Feynman technique. It absolutely works.

> > > **qnleigh**：
> > > > Another one is having the LLM quiz you on your topics of interest
> > > 
> > > This is a great idea. I'm going to try it.

> > **SchemaLoad**：
> > Even with the latest models today, the hallucination rate is absurdly high on anything deeper than surface level knowledge or something that can be directly scraped from reddit.
> > 
> > And you notice when it's a topic you know well or something like software where you can immediately tell the options it's giving you don't exist on the page. Leading to the amusing statement "LLMs are bad at what I do but great at everything else".

> > > **unclebucknasty**：
> > > I've (elsewhere) written about this diminishing return effect on LLM utility in relation to increasing expertise.
> > > 
> > > The question: what's the net positive gain of turning people who know nothing in a given field into sub-novices, while weighing actual experts down with work slop and marginal returns?
> > > 
> > > And I wonder what the true cost is of arming so many novices with that level of dangerous knowledge.

> > > > **DrewADesign**：
> > > > The fact that some people get genuine value from LLMs when learning doesn’t contradict the fact that they’re Dunning-Krueger “expertise” generators. The fact that the person learning from them is in charge of ensuring they aren’t full of shit, which they frequently are, is an *inescapable flaw* in this process. I honestly think that reduces the value of these things to just above what you can find out with a search engine with most topics. Hey, great. An improvement is an improvement right? Is it an improvement worth trillions of dollars and screwing over writers and artists worldwide? Fuck no.

> > > > > **unclebucknasty**：
> > > > > Sounds about right.
> > > > > 
> > > > > Tangentially, but related: I'm old enough to remember when the spirit of your comment was pervasive on HN.

> > > > > > **DrewADesign**：
> > > > > > It wasn’t even all that long ago. I noticed around the time ChatGPT 3.5 was released I saw a significant change in tone regarding LLMs and diffusion models. I think that’s when some serious astroturfing started.
> > > > > > 
> > > > > > I’m old enough that I worked my first IT summer job the same year slashdot was founded. I’ve seen a lot of tech tribalism form and dissipate, and this one didn’t feel organic. My gut says a lot of the us-vs-them tension originated in a deliberate campaign to cast AI boosters as the tech industry in-crowd, and ‘other’ the people not on-board. Who knows.

> > > > > > > **unclebucknasty**：
> > > > > > > 1000% astroturfing—and across social media. Too many posts of the same quality at the same time(s). These things ran in cycles, spinning up and dissipating just as suddenly.
> > > > > > > 
> > > > > > > E.g. the entire framing to combat complaints about shortcomings was, "It's not the tech. It's you. You're just not doing it right. Wrong setup, wrong workflow, add this to your .MD, use loops, etc". Every complaint was immediately met with this same treatment by a swarm of vague bro-bots that materialized from the ether. The core message? Always the human's fault.
> > > > > > > 
> > > > > > > And, don't get me started on the waves of newly minted expert AI creators, making recommendations without showing a single example of what they'd supposedly built.
> > > > > > > 
> > > > > > > I'm sure some bandwagon organic creators tried to cash in on the genre, but encouraging that was also part of the point.

> > > > **champagnepapi**：
> > > > I think the true cost will be some catastrophic failures.
> > > > 
> > > > Just hoping folks don’t get hurt due to people not understanding what they’re doing with these things but believing they’re competent.

> > > > > **DrewADesign**：
> > > > > If that is the case, I seriously doubt the blame would ever touch the people that oversold this shit.

> > **voidhorse**：
> > This. This is exactly how I use them and I have had no issues so far. I read the book myself, then I point the LLM at it to ask questions about notions I might be struggling with.

> > **giancarlostoro**：
> > Whats funny about LLMs is they are trained from books, but they are also trained to not output books, so how much of an LLM skews its output because a perfectly normal sentence could be a quote in like 300 different books?

> > **sojournerc**：
> > I'm sorry, but why not just read the fucking book if you're interested?

> > **broast**：
> > I prefer to have the LLM ask me the questions

> > **peab**：
> > I also agree with this. LLMs are a great companion when reading a book to clarify things and dive into specific topics.
> > 
> > I'd imagine an application that uses LLMs will be created that better manages learning. It's just not clear what that UX is yet- it's obviously not just a chatbot

> **misiti3780**：
> I think AI is surprisingly good at this. I use voice mode while working out to learn complex topics, follow up with reading, and then go back to ask the LLM more questions. They excel at simplifying complex ideas and have endless patience. One hack I found is telling the LLM to test my knowledge by asking me questions—that gives me a clear idea of what to read next. Overall, they’re a great tool to use alongside traditional learning methods like reading books and working through practice problems.

> **rl3**：
> >*I really don't want to read anything generated by something like Opus 5 at this point.*
> 
> Personally, I find that its generated prose tends to have an undue weight to it, almost as if every topic I ask about somehow bears a heavy burden, or is otherwise *load-bearing*, to use its parlance.
> 
> Quite puzzling, really.

> > **roywiggins**：
> > It has a sort of metronomic quality. It never slows down or speeds up or modulates its tone. It plods forward at a relentless pace and never has a light touch with anything.
> > 
> > I think this is one reason why LLM text is pretty exhausting to read for long stretches.

> > > **rl3**：
> > > >*It has a sort of metronomic quality. It never slows down or speeds up or modulates its tone.*
> > > 
> > > It's possible that this quality you describe stems from the extensive training corpora utilized by the major AI labs. These almost certainly include work from the esteemed economist Jacob Silj:
> > > 
> > > https://www.youtube.com/watch?v=Poc1upTejD8

> > **PaulStatezny**：
> > Yes!
> > 
> > I have a personal theory: LLMs are *fundamentally* handicapped at perceiving what's going on in the mind of the human (this can't be "innovated away") and that's at the root of what makes them suck at conversation.
> > 
> > Next time you're chatting with someone, notice how much understanding is shared without anything being said. E.g. the other person might share something deeply disappointing, and they can tell without you even saying anything whether you get what they're going through. This unspoken-yet-communicated information guides the conversation. Or as another example: humans can read the room -- you walk into a room and immediately adjust your demeanor based on what you see and sense.
> > 
> > LLMs are totally blind to things like this, and this adds an *inescapable* awkwardness to interacting with them. I don't believe they'll ever grow out of this. Which thankfully implies more long term demand for humans instead of robots. :)

> > > **cromka**：
> > > Very well observed. I found one more thing: they fail to consider what a 3rd person might understand from your conversation, so when you ask it to dump stuff into a Documentation, they keep making references to facts you had previously discussed or to the train of thought, completely irrelevant to bystander.

> > > > **PaulStatezny**：
> > > > 100% -- this is *the worst*. Referencing all sorts of "words with made up contextual/analogous meanings" based on the conversation...outside of the conversation.
> > > > 
> > > > Does anyone have a read on if this is primarily a Claude issue, or if all LLMs do this?

> > > > > **cromka**：
> > > > > I think it's fundamentally and issue with LLMs, for this to not happen they'd have to constantly think "what does other person think right now/what's their state of knowledge" *AND* also apply that to am additional, third person which would be reading the Docs. They can't even do the first bit well. I think it's a limitation we'll have to live with.

> > > **cheesecompiler**：
> > > Tech guy discovers conversations with humans.

> > > **knollimar**：
> > > Even over phone calls you get a sense so unless it's in timing it isnt demeanor either

> > > **wannabe44**：
> > > No, they're just trained to impress the C-suite motherfuggers with dense vocab.

> > > **rustyboy**：
> > > This is basic empathy.  It's one of the key differences between a bad and good teacher.  People who can see where you're coming from and grasp how your mind is working and correct that train of thought.  Meanwhile the bad teacher will simply answer your question.  You keep on parroting rather than *understanding*.

> **varispeed**：
> >  First, I get exhausted reading LLM prose.
> 
> Often "be concise, to the point." is enough, but you can also paste it some stuff you like as an example text and ask to do style transfer.

> **lanfeust6**：
> LLMs help me refine my search. If I want to dive deeper into any topic, I can yield a strong list of primary sources relatively quickly.

> **cortesoft**：
> I have been using this tool for the past few months that was posted on here: https://github.com/devenjarvis/lathe
> 
> It generates tutorials for you, and serves a webpage that lets you complete them. It does a remarkable job.
> 
> It still has a bit of the LLM prose problem, but it does help you fine tune the ‘voice’ it uses.

> **c_moscardi**：
> Yeah, I am currently trying to work with Opus 5 to refresh myself on deep learning fundamentals, and... it's a mixed bag. I'm glad I already am familiar with the subject matter, as I can prompt for refinement and improvement. It is kinda following the Karpathy videos so far (a couple lessons in) but adding more math/derivations, which was what I asked for. It has trouble staying on topic, presenting information in a coherent/meaningful order, and providing all the context necessary to move through steps in its "course notes".
> 
> Like I said, I'm essentially continually prompting to refine the material. LLMs certainly continue to append, and never cut back. It just keeps spitting out additional content at me. So that's a bit annoying too. But I can basically get figure out what's going on with a few extra promps.
> 
> If youre curious what i've got so far... just be warned it is quite literally AI slop plus me continually prompting for clarification/cleanup etc. : https://github.com/cmoscardi/ai-for-ai

> > **novaleaf**：
> > opus 5 doesn't follow instructions that great.  probably needed that extra "creativity" to benchmax.   if you are stuck on anthropic, try Opus 4.8 or Fable5 a try with the same prompts.  very different results.

> **epolanski**：
> > LLM prose is annoyingly dense
> 
> It's just long. It just doesn't shut up. It's overly verbose. And you can't tell it to be concise or you degrade its quality.
> 
> If I ask what an integral is, the correct answer is that it is the continuos analog of a sum, generally used to calculate areas and volumes.
> 
> It should really be a single sentence, and then let me ask more about the terms I don't understand, and here's the beauty, in the previous one there can be only 5 terms I cannot know.
> 
> An LLM will vomit an entire page or more of explanation which isn't bad per se, but is an answer to something different: "give me a short introductory explanation to integrals". And that's not what I asked.

> > **oblio**：
> > The new Google Translate. They've made it slightly better at translating paragraphs of text but in many cases it's lost the basic function for translation: dictionary.
> > 
> > Try it out, fairly sure that if you out in 100 random words for 30 of them it will just refuse to translate them (it will copy paste the original word into the target language) or it will do silly things like use the target 4th dictionary definition instead of the primary one).

> > **onemoresoop**：
> > I call that vomit shotgun answers, text from which you have to filter out all the extra info the LLM wasn’t asked for. Luckily you can control that behavior and make it behave closer to what you want. Just ask the LLM how to ask for it.

> **thisisit**：
> I have been using LLMs to help me turn my journals into interconnected notes and sometimes it is so confusing to read the notes that it doesn't resemble any human would write. Its like the models are getting stronger while also losing its touch to write human sounding sentences on complex topics.

> **smnplk**：
> Have you tried using the caveman skill ? :D Might be worth a try if you dont like long prose https://github.com/JuliusBrussee/caveman

> **biophysboy**：
> It annoys me that the default AI mode is so tedious and longwinded. I read a lot of nonfiction - the house style of AI is basically marketing copy.

> **nullsanity**：
> This is on top of the issue of LLMs being a moron. like, I'm sure dumb people can learn stuff from them, but I'm sticking to books written by people who know what they're talking ahout and not vibed slop.

> **andy99**：
> The sycophancy is also a concern, it’s not really an impartial teacher, all its training is to suck up and maximize engagement rather than learning. The incentives are wrong.

> > **cromka**：
> > > all its training is to suck up and maximize engagement rather than learning
> > 
> > That's speculative, isn't it

> > > **adastra22**：
> > > No, that's a direct consequence (intended or not) of how RLHF works.

> **mikenew**：
> I've decided that the main thing I'm building is my own mental model. You can take notes, create docs, put graphs and websites together, but unless I'm just trying to generate some reference material the only real objective is to develop the understanding and intuitions inside my own brain.
> 
> So I have the LLM offer a very short explanation of something, and from there's it's just me asking questions. Anything that feels fuzzy or not fully internalized is something I poke at until I'm satisfied.
> 
> It really has helped me develop a sensitivity to what I understand vs what I don't, and the ability to drill into any part of it is amazing.

> > **hank1931**：
> > I do this too. I use Claude. I picked a voice I like. I go on a three mile walk. I will ask it questions about a topic that I want to learn about. If it starts telling me more than I want to hear right then, I will say "stop". It doesn't get offended. I then ask it something else. I find this very effective. I control it so it only explains to me what I want explained. If what it says sparks questions on a related topic I jump to a brand new topic. No personal tutor could keep up with this or adjust to exactly how I want to be addressed like Claude does. I'm very excited about the progress I'm making mastering new topics.
> > 
> > And yes, it is not that it is just presenting the facts. By me taking control of the direction the questions and answers go, I can flesh out my mental model. I won't retain every little thing it tells me. But I am much farther ahead than before.

> > > **le-mark**：
> > > Can you say what topics you’re using this method to learn? I think it would be more effective for some than others.

> **sscaryterry**：
> > want to read anything generated by something like Opus 5 at this point
> 
> I've stopped using CC because of it. I find it insufferable.

> > **puttycat**：
> > Opus 5's language is just terrible

> **agumonkey**：
> anybody adds some prologue about what style of answers are prefered ? i know i often try to change the linguistic patterns because i too (unsurprisingly) am tired of llm prose.

> > **esalman**：
> > I've heard people promoting LLM to use ASD-STE100 Simplified Technical English with some improvement.

> > > **agumonkey**：
> > > ha, nice, i'm gonna try that for a while

> **ethin**：
> Even if you tell the LLM not to use LLM pros they (still) do it. If you feed the Wikipedia article on signs of AI writing and tell them to use none of those signs they will also (still) do it. I have tried (many times) to get an LLM to explain a concept to me, or a process, or an algorithm or what have you, and every time they cannot help themselves. Either they use LLM pros, or they get so verbose that it all just becomes noise and I spend more time filtering out unnecessary jargon than I do reading let alone learning anything.

> > **cromka**：
> > I ask them to use Simple English and a jargon of the domain. This seems to work best for me.

> > **big_paps**：
> > For Gemini 3 this seems bit to be the case. If you use gems you get completely different personalities - so different that its almost scary. You can create gems which are really insulting, gaslighting or seemingly of a specific profession

> **j45**：
> You can change the prose that it outputs to anything you like.  ask the llm how.

> > **j45**：
> > Specifically, you can set the tone and style to match what you like or used to after asking it to interview you, create an output, and then use that output as the project description or document to refer to

> **yieldcrv**：
> Its aligned in getting you interested and frustrated about a topic enough to go to a primary source you would have never looked at

> **runarberg**：
> AI hater here. Too me this story is all to predictable. This is exactly how I thought using LLMs to learn would go. Or in simpler terms: *well duh*.
> 
> I'm actually going to make a prediction here as well. I think you will soon realize that using LLMs to clarify certain questions or ideas you have will turn out to have frustrations as well. And that you will soon direct those questions to either peers you know in real life or internet forums which are very likely to have a non-AI policy.

> > **andy99**：
> > > I'm actually going to make a prediction here as well. I think you will soon realize that using LLMs to clarify certain questions or ideas you have will turn out to have frustrations as well.
> > 
> > Much more likely that people will believe themselves to be an expert in a subject after having had a conversation with Claude about it.

> > > **knollimar**：
> > > Wild because people wouldn't do that with a friend.  Something about an LLM giving people info has this insidious stoleb valor to the LLMs work.  Like that wasn't your thought, you just google searched it.

> **KronisLV**：
> > First, I get exhausted reading LLM prose. I really don't want to read anything generated by something like Opus 5 at this point.
> 
> I’ve found the tone of Kimi K3 to be less obnoxious. Unfortunately it doesn’t wholly solve the issue, I don’t think any LLMs out there have a truly pleasant writing style, but at least not every assumption is “load bearing”.

> **treetalker**：
> So you want it to teach you *and* take notes for you?

> **SambhavGupta**：
> To get rid of the llm prose issue you can take a representative sample of its prose (say a question and its answer), rewrite the answer in the way you'd prefer, and add that to the system prompt; I did this to get my LLMs to compress down what they say, and now everything they say is very dense and to the point

> **cout**：
> I use the LLM to point me at relevant books and papers. But there is still a trust problem: I am trusting the LLM to point me at reliable, trustworthy sources.
> 
> I'm not sure I'm better off with humans though -- I'm not qualified to judge whether a source is a proper authority, not an I qualified to judge whether someone knows enough to point me to a reliable source.
> 
> It seems this is a fundamental epistemological problem to which there may never be an answer.

> **dbtc**：
> "hey LLM, I'm trying to learn about ___. I already know ___. My favorite authors are ___. Suggest some reading material."

> **unclebucknasty**：
> >*LLM prose is annoyingly dense, and the useful information gets lost in a bunch of noise.*
> 
> This problem doesn't get talked about enough and is second only to the hallucination problem IMO.
> 
> AI produces so much noise to wade through in order to find signal, and the more expertise you have in a field the more that costs. That noise directly subtracts *signifcantly* from productivity gains.
> 
> And, I think the problem is directly related to the hallucination problem. It feels very much like an effort to kitchen sink the response in order to provide some value among possible hallucinations.
> 
> It also seems to be a byproduct of Gen AI operation. It just fundamentally doesn't understand what it's outputting, so doesn't know how to narrow down to the most salient bits.

> **colordrops**：
> You can instruct it to be terse and even take on a specific voice if the standard prose bothers you.

> **frogperson**：
> I've found it helpfull to ask the LLM to generate a sylybus for the topic. treat the sylybus as a design doc for a price of software.  i find they do much better when they have subtasks to focus on. they can do big picture and small picture, but they can't do both at the same time.

> **jijji**：
> something to try that works really well is to put "explain this as if you're talking to a 5th grader" at the end of your request.... it just breaks down the text into more manageable sentences that can be understood by general audiences

> **planckscnst**：
> You can make something like the link below. I'd say it's a more than marginal improvement. It's still tiring, but it's much better according to my taste. I imagine everyone would have their own version of this for their own preferences.
> 
> It's a loop that uses adversarial review to check several dimensions of the writing:
> 
> https://github.com/Vibecodelicious/llm-conductor/blob/main/writing_guidance%2Fllm_writing_guidelines.md

> **wanderingmind**：
> Good to know other people who get migrane reading LLMs dense prose. I started reading books again recently, since everything online is polluted by LLM prose. What i realise, is that a human author, especially a teacher understands the learning pathways of new learners, they motivate the learning, and start from simplest concepts (a spherical cow), and then building all the complexities.  This helps us to emphasize on most important concepts, while throwing away unnecessary complexities. While reading LLM prose is like reading a research article, that is written to an expert in the area, that talks about bleeding edge, with full of jargons, caveats, that just is not conducive to the learning process for a new learner.

> > **resonious**：
> > To me, it's just Claude. The other models have their quirks but nothing is quite like Claude.
> > 
> > But even with Claude, it's it's really the prose getting in the way you can install the caveman plugin or tell it to use that "standard technical English" thing.

> > > **PaulStatezny**：
> > > Can you elaborate more on juxtaposing Claude's terrible prose with other LLMs?
> > > 
> > > Any more detail you can share? Do the others feel more "human"? Are there any that are particularly digestible/human-friendly?
> > > 
> > > I've been wondering for a while if this is just Claude because I mostly use Claude, so this is very telling.

> > > > **resonious**：
> > > > I wish I had something more methodical I could show. It's all subjective, but GLM-5.2 feels more human to me. Even GPT-5.6 Sol tends to be easier on the eyes for me (though the stereotype of it overengineering and no common sense are still true).
> > > > 
> > > > I tried using a new agent service recently and could tell immediately that it's powered by Claude due to the way it writes.

> > **tkel**：
> > Also they tend to assemble complex jargon in obtuse or  meaningless ways, which makes reading and parsing and understanding much more difficult. Tends to reveal that LLMs fundamentally do not have "understanding", just likely word  generation

> **khuston**：
> I never used office hours as a student, which I later regretted because it made me work longer and harder to perhaps achieve somewhat better understanding in some classes, but also I dropped every proof-based math course I ever took. Overall I think my education would have been stronger by attending office hours.
> 
> I view LLMs in education similarly to office hours. Some people abuse it to get homework answers without grappling with the material, but the optimal amount is not zero.
> 
> LLM certainly not a replacement for a book, where you get someone’s extended personal approach to a topic, thoughtfully organized, reviewed and edited, often times actual courses taught based on it, with answers checked and errata available online.

> > **relativeadv**：
> > I completely agree. I have vibe coded what i would consider to be some pretty weird things in the name of learning facilitation.
> > 
> > Perhaps the best example has been a native macOS app that is a completely custom text editor with built-in debugger, lsp support, fuzzy finder, etc stuff you'd expect. Inside the same app is a library of books i can read within the app completely formatted and for every chapter/section of each book that is a quiz to take (LLM generated of course), a "recitation" tab where i am asked a question and say outloud my response to the AI to evaluate me on and then finally practice problems to do within the custom text editor (these are usually programming books). The reader also has ai re-write built in.
> > 
> > As neat as this is, and i worked through K&R like this, i have ultimately fallen back on "just read the damn book and go to the AI when you've got questions."

> **hudn33**：
> Same. I usually just read the book along and ask questions on a specific part, rather than trying to get the LLM to produce an entire study guide for me. It seems to work better as a Q&A than a "teach me" advisor

> **bluejellybean**：
> This feels like the weirdest complaint to me. Just tell it to shorten its response.
> 
> Literally saying "one sentence response" solves most of this problem.

> **avilay**：
> I have had very similar experience! I wanted to learn Probablistic ML, checked out a couple of MOOCs, but didn't find any that were at my level - some were too advanced, some too beginner level. Claude was unable to one-shot a course, so I am now asking it to generate it module by module. But even here, it is not doing a very good job. I muddle through the concepts that it has written, do a whole bunch of back-and-forth, which tbh is exhausting, and then rewrite everything in my words so it actually makes sense to another human being.
> 
> > I get exhausted reading LLM prose
> 
> So much this! If I see one more sentence with the words "genuinely" juxtaposed with "load bearing" my head is going to explode!
> 
> btw, I am building the tutorial here for anybody interested in this topic: https://github.com/avilay/learn-probml

> > **coderatlarge**：
> > i’m personally deriving a huge amount of value from the custom materials fable is assembling for me. for example i asked it to write a focused expository math paper on reed solomon to accompany an implementation module that it wrote for me. it’s remarkably useful to steer it to create graphs and diagrams of exactly how you like the material presented. or the bibliography researched and cross-linked with the body or the order you want your questions addressed.
> > 
> > it also researched vision correcting displays for me and i can finally put that idea to bed - i was never really going to pick up an optometry textbook tbh.  plus it was able to pull together a bunch of geometric and physical context about light and the eye plugging exactly my personal knowledge gaps.
> > 
> > in general i suspect these materials might not be that interesting to others because they are so custom to my learning style and personal needs and preferences.
> > 
> > these are usually not one shot documents but rather many prompts deep before i get something I’m willing to sit down and read or study. but dramatically quicker than assembling it myself from primary sources.  i wouldn’t say it matches master expositors but then they’re not available to write on any topic i happen to need right now.
> > 
> > plus I’ll just have a live voice discussion with the system when i go for a walk and there are still things bothering me on a topic. it takes a little patience but if i’m in the mood it’s amazing.
> > 
> > i generally find that it can help track down specific references if i suspect hallucinations. but especially on factual topics my experience so far has been extremely encouraging.

> > > **avilay**：
> > > Good point. Same with me. Despite it being very tiresome, all the back and forth that I do with it really deepens my understanding of the topic. I have been on Opus so far, let me try Fable and see if it gets better. I haven’t tried voice either. Next time I go for a walk I’ll try that!

> > > > **coderatlarge**：
> > > > curious to hear about your findings!

> **QwenGlazer9000**：
> I have the exact same experience, so reassuring to know I'm not the only person who feels this way.
> 
> I will say, opus 5 is an *egregiously* bad case of this, but other LLMs have this too, just less bad.

> **StableAlkyne**：
> > LLM prose is annoyingly dense, and the useful information gets lost in a bunch of noise
> 
> This is my biggest gripe with reading AI-generated text as well (ignoring the meta issue of whether it's worth taking the time to read something that an author didn't think was worth the time to write). It's gotten to the point that weird AI-style analogies just take me completely out of the text and kill my interest.
> 
> And I can usually tolerate a lot of purple prose.

> **eru**：
> > First, I get exhausted reading LLM prose. I really don't want to read anything generated by something like Opus 5 at this point.
> 
> Agreed.
> 
> I find Opus 5, and even Fable, to be overly wordy in eg PR descriptions and code comments.
> 
> However, I suspect that's more to do with what they are trained to do by default than LLMs in general.  I have a little setup where I tell Claude to work together with Codex to tighten up prose and comments, and for me that produces much more palatable text that needs less human editing afterwards.

> **supriyo-biswas**：
> > I get exhausted reading LLM prose.
> 
> While my advice is specific to learning about codebases, the way I do it is to have it generate mock data and put it in the local development environment, and give me some exploratory commands, and then ask away. It's a machine after all, so I don't have to read its preceding prose to understand whether it did tell me something, it can just repeat it however many times I ask it, and the hands on commands etc. give me something to actually try and implement.

> **rDr4g0n**：
> LLMs can't "read the room" and infer how much context the audience already has, so they try include everything.
> 
> human conceptual thinking is very much a multi-dimensional graph, which relies on light "approximate" concepts that are "good enough". LLM AR token generation is extremely one dimensional and doesnt care about the "weight" of the concept behind a token.
> 
> LLMs hold billions of parameters in "mind" at once. humans hold like four "concepts".
> 
> This is the essential mismatch and the primary reason LLM conversation can be so painful and exhausting.
> 
> Explaining this and limiting "concepts" to four at a time tops is one of the very few AGENTS.md / system prompts I always use, and it has proven invaluable time and again.
> 
> Thinking traces show how effective this is at forcing the LLM to simplify its thinking.
> 
> [edit] Also, myself and nearly all of my peers are struggling to choke down the flaws of LLM tooling along with the benefits. the speed at which LLM adoption is being forced, without truly crafting them into quality tools first, is not ok, and not normal.
> 
> LLMs have stirred an inhumane hunger and fear. the tech is fine, but the way tech companies (creators and consumers) are behaving should be deeply questioned.
> 
> it's NOT normal. it's not ok.

> > **bumby**：
> > I’m curious where you get the estimate that humans hold “like four” parameters in their mind at once?

> > > **rDr4g0n**：
> > > updated the comment. i meant four "concepts". i dont reason about my own thinking in terms of parameters.

> > > **btown**：
> > > Cowan (2001) is an oft-cited paper proposing three to five "chunks" of capacity in human attention: https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/magical-number-4-in-shortterm-memory-a-reconsideration-of-mental-storage-capacity/44023F1147D4A1D44BDC0AD226838496
> > > 
> > > The full PDF is worth a read (Figure 1 may be of interest to many here): https://www.cambridge.org/core/services/aop-cambridge-core/content/view/44023F1147D4A1D44BDC0AD226838496/S0140525X01003922a.pdf/the-magical-number-4-in-short-term-memory-a-reconsideration-of-mental-storage-capacity.pdf
> > > 
> > > If "attention is all you need" then it's something we do indeed lack, in comparison to LLMs! But it's an interesting question: might machine cognition benefit from similar bottlenecks in an attention algorithm? Advancements like Kimi Linear seem to indicate that we're far from the finish line: https://arxiv.org/abs/2510.26692

> > **PaulStatezny**：
> > Would you be willing to provide an example (even a contrived one) of how this "four at a time" prompt changes the LLM's behavior?
> > 
> > I just want to understand more.
> > 
> > Also, would you be willing to share the actual text of it that you put in AGENTS.md?

> **xfq**：
> I think one problem is that books are not customizable, and many books are aimed at people with some certain knowledge. With LLMs, you can tell it what your knowledge level is and ask it to customize the answer for you. This is difficult to achieve with books.

> **umpalumpaaa**：
> Claude code has a „fork“ feature where you can fork an existing conversation and keep talking in the fork and then you can go back to the original of the fork. You can fork as many times as you want and let LLMs write to a markdown file to keep important facts and learnings - also good for agents to do research without expanding the context window

> **matheusmoreira**：
> > I really don't want to read anything generated by something like Opus 5 at this point.
> 
> Recently switched to OpenAI and I've gotta say Sol is so much  better at writing than Claude. Opus has a distinctive sentence structure and Fable somehow manages to be even more obtuse. The personality of these models really does come through...

> **SwtCyber**：
> I think there's an underrated difference between information generation and pedagogy here. LLMs are very good at producing more explanation, yet "more explanation" is often exactly what you don't need when learning something difficult

> **northern-lights**：
> I had the same problem - Opus models past 4.7 tend to inflate output tokens for no good reasons, introduce innumerable jargons and is a pain to read. Then, I cam across this: https://github.com/ayghri/i-have-adhd/blob/main/skills/i-have-adhd/SKILL.md
> 
> You can either install that skill or put the Rules section directly in your Global CLAUDE.md for Claude or Personalization setting for Codex and it should cut down the output verbosity by quite a fair bit.

> **Arn_Thor**：
> > generate a web page with diagrams and organized information flow.
> 
> Sounds like you'd be just as well off link-surfing Wikipedia?

> **tiberriver256**：
> You should read this article sir! Just scroll to the top of all these comments and check the title!

> **Nicholas_C**：
> > Second, as I dive deeper, I need a way to organize the information in a useful way as I begin to branch out in many different directions.
> 
> This is the issue with using ChatGPT as-is in the web app. I use ChatGPT/Claude/etc in the Notion web app now to organize my pages of knowledge and keep everything organized. That said, ChatGPT/Claude in Notion seems to produce inferior results than using them directly which is frustrating. I'm not sure why this is but perhaps LLMs in Notion have too much context and get bogged down.

**jdalsgaard**：
I guess we all learn in different ways. I prefer reading, and can fairly fast find the articles that make sense to me.

Colleagues often suggest podcasts and videos - I very, very rarely listen to them or see them.

The bandwidth is too low. It's not efficient and ultimately I'm bored.

This is a nice project, it looks cute. I watched some of the pages
 But I want more than that, more information, and faster - still a Wiki fan.

Also, step number 2 in the flow: have the LLM check itself... Naah, I don't believe that.

But you're not the only using gen ai like that. Take care.

> **dan_mctree**：
> Imo the podcast and the video are better served as background material for some other task. The low bandwidth becomes an advantage because it's often ok if you miss out on some parts due to lack of attention.
> 
> Indeed it's often a waste of time to just focus on talking people fully if you want to learn fast, reading and especially deliberate practice are better for that. But if you don't have the time, energy or focus, then listening to interviews in the background can be useful supplementally

**tolerance**：
If you're using LLMs to learn or for research, and at some point you don't end up engaging with an actual resource (books, papers, lectures, web pages, etc) then you're playing yourself.

> **gnarlouse**：
> Sorta. If its response is grounded in actual material, and you're thorough, it's not so risky. As with all learning, trusting one source is a risk in itself. Hell, I didn't even trust my physics textbooks in college. Physics.

**UltraSane**：
I recently used Opus to create a  learning plan in ClickUp for every Tailscale feature and it worked very well.

**wiremine**：
Personally I'm excited about these sorts of experiments. We all learn in different ways, and these sorts of techniques allow us to create "on-demand" syllabuses and lessons that fit our learning style and learning level.

It's not perfect, but I'm optimistic this will be a useful way to teach/learn in the future.

And, to be clear, I think this will be best utilized within a group/community setting. I don't think it will replace teachers or classrooms.

**throwaway63467**：
That seems like a terrible way to learn. It’s a neat animation but cmon, there’s like educational TV programs from the 80s that explain this so well, in Germany there’s “Sendung mit der Maus”, not sure if they have a segment on chip manufacturing. But in these clips you can at least see the real stuff instead of some half wrong animation, just let the LLM write a few paragraphs for you or better find an ACM article or book on the subject, probably still takes less time than coming up with that animation…

God does everything have to be productized and glorified as if you’ve invented a new way of learning. Read some books!

**foo42**：
I've been using them by reading some docs/wiki/tutorial, then when I think I understand something trying to do a rough explanation to the LLM and ask if I'm right. I'm usually making some analogy to something I already understand a little. I'm usually partially right but missing some key bits at the first pass. I go back and forward asking for explanations of various bits or asking for resources around the area I'm not understanding. Often times just discovering the relevant name for the area of study opens lots of doors. I basically use it like I would talk to a knowledgeable and patient teacher.

As for how useful it is to understand thins, I believe it's still useful and hope it will continue to be.

**zapataband1**：
"What you get is a beautiful animation that is 100% accurate and free of hallucinations."

Do you know it is free of hallucinations because you crossed checked it with the source material or because you told the LLM "don't hallucinate"

**reqo**：
Something that I have realized recently is that it has become so easy to get an answer to almost any question with the help of chatbots that its almost unnecessary to spend any effort thinking about the problem or the solution. I feel like before when I had to spend time researching a problem to find an answer I learned so many things around the topic itself which helped me understand the problem itself better and gained a deeper understanding. Today it feels like you can have an answer to the most complex questions you might have, yet you gain a superficial understanding of the topic and might forget about it quickly.

**CrzyLngPwd**：
AKA - How I skim read a lot and learn nothing of value.

**w10-1**：
Gamifying the presentation could make topics more accessible to others.  For me the overhead wouldn't help with my own learning.  Also I've been burned by just learning things mechanistically (e.g., coding, applying algebraic rules), so I'm leery of learning just by making flashcards or models of the topic.

I find LLM's do great for learning when I ask what are the principles, how the main applications work, what are the key drawbacks, where are the growth plates in the field, etc. - the kind of thing a good advisor points to.  Sometimes I have to ask it explicitly to use topological order of topics and show relations, which often highlights the gradient changes in the learning curve.  For pruning, it's surprisingly good applying philosophical heuristics - Occam's razor, or Derrida's differance (the difference that makes a difference), etc.

And finally, no learning is effective without problem sets, and for those LLM's at times get me over blocking issues.

The degenerate case is memorizing the glib phrases regurgitated back to me; they're helpful and functional enough to get me into real trouble!

**federico-peconi**：
not all knowledge can easily be translated into a pipeline alike game imho

**throwrioawfo**：
Gell-Mann Amnesia: the blog post

**mlpoknbji**：
My high hopes were quickly dashed at the step that involved turning a complex topic into rollercoaster tycoon.

**epolanski**：
> I personally find the style used by LLMs to explain things difficult to follow. It's just too simplistic

I also struggle with LLMs explaining things, but for the opposite reason.

I consistently have problems to get short, precise but plain/simple answers.

Instead I'm overwhelmed with walls of texts, often filled with jargon that is a mixture of imprecise and unneeded.

The style at which I learn better is by asking about stuff interactively. I ask you what something is, you give me a 3-4 sentences top answer. Then I explore and dig into the topic from your answer on the things I want to know better.

**madibo3156**：
This guy is severely milking it now. If learning means building an inaccurate and incomplete understanding of the topic then go hog wild. Otherwise https://news.ycombinator.com/item?id=49209049 sums up my feelings about the author's attitude.

**zatkin**：
I tend to ask the LLM for a single HTML page explanation, with a pedagogical approach. Something about dropping the word pedagogical leads to a more structured outcome, but I haven't quite figured it out why yet.

**jb1991**：
anyone using LLM to learn a new language? got any useful prompts for this?

**praveer13**：
I’ve been doing something similar (browser only interactive courses served from GitHub pages) to teach me topics from beginner to advanced

LLMs and systems intersection - https://kernelspace.naigap.com

Distributed systems - https://byzantine.play.naigap.com

> **dbrans**：
> These are high quality at first glance. the visualizations and exercises are helpful.
> 
> What is your process for creating these resources?

> > **praveer13**：
> > I just gave a simple prompt to Kimi k3 when it came out, and then just using it and asking it to improve based on my own taste/gaps etc so it’s a long drawn out process. I’m doing that for the first one, will iteratively keep improving it myself as I run through it. Maybe will post on HN after that.

**michaelmure**：
I wish there was a LLM tool to explore a topic recursively, as a tree or a mindmap. You would start with some high level concept (say "cryptography") then dig further and further to more specific topics.

I think that would be a way more natural way to explore than being stuck on the classic linear output of a LLM.

**QuantumNoodle**：
> I ask it to review the accuracy of the knowledge base it built in the previous step.

> [I ask it to build an interactive thing]

> I then push it to a new repo and enable GitHub Pages for it.

Congratulations. You are an echo chamber for LLMs. Use it to create, and verify, and post to then be scraped and trained on again.

**nightwalkerkg**：
My main issue with using AI as a learning platform is that unlike documentation, books, Youtube videos, there is not really a process of having someone "review the learning material". For example, I can always read the review of some book or ciriculum, the comments under a video, or if it's some for of open source documentation you can check the PRs and verify to some extent it's claim. With AI I can't really say what it has halucinated, because I am learning a new thing, I don't have that benefit of previously reviewed material.

> **j45**：
> You can ask the LLM to connect the dots to the sources before displaying it to you so you can see the proof in line.
> 
> You can ask the LLM how to do this.  Start with a topic you know well to get the mechanism working and trust it well.

> > **nightwalkerkg**：
> > Of course, and that is what I do, but it becomes and additional mental and time consuming effort. As an dumb example, if I am learning a new programming language and trying to grasp some concept, I'll check the docs, find the section and read it. I trust that the source in the docs has been already vetted by other devs and the authors. But if I ask the AI the same thing, I then need to verify it's claims usually by asking it to check if the info is true, and then possibly opening the source link (lucky for me Claude provides the links in the desktop app as footnotes). It's not a question about AI, it's about the trust I have of this tool, it builds over time, but as soon as the AI makes an assumption or a hallucination we are back down to square one.
> > 
> > I assume this will become less of an issue in the future as there is more trust between the AI tools and me.

> **ethin**：
> This is (exactly) why I very strongly tell people not to teach themselves with an LLM. Particularly from the ground up. If you do not understand the domain, you cannot learn from the model because you won't know what questions to ask and it certainly isn't going to answer all of them for you.

> > **bonoboTP**：
> > The LLM doesn't have to be the sole single only exclusive source you learn from. It's an addition to a mix. Nothing is a single definitive answer. Same way as many other things, like Anki flashcards or Duolingo or some YouTube channel, or some tutorial website or indeed a coursebook or an audio course or whatnot. Use multiple sources and use the strengths of each.

> > > **ethin**：
> > > What you describe is indeed the ideal method of learning. However, I think we both know that if LLMs are pushed as a learning device, people will substitute everything else for them (or companies will very strongly encourage that substitution).

