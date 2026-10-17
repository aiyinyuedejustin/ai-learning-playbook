# HN：我因为 AI 失去了学新东西的能力

- 链接：https://news.ycombinator.com/item?id=47240612
- 作者：dokdev
- 获取方式：Hacker News 帖子与评论全文

---

## I lost my ability to learn anything new because of AI and I need your opinions（dokdev，24 分）

（讨论共收录 29 条评论，缩进表示回复层级）

I feel like I’ve lost my ability to learn because of AI. It is now so easy to generate code that it feels meaningless to focus and spend time crafting it myself. I am deeply sad that we may be losing the craftsmanship side of programming; it feels less important to understand the fundamentals when a model can produce something that works in seconds. AI seems to abstract away the fundamentals.

One could argue that it was always like this. Low-level languages like C abstracted away assembly and CPU architecture. High-level languages abstracted away low-level languages. Frameworks abstracted away some of the fundamentals. Every generation built new abstractions on top of old ones. But there is a big difference with AI. Until now, every abstraction was engineered and deterministic. You could reason about it and trace it. LLMs, on the other hand, are non-deterministic. Therefore, we cannot treat their outputs as just another layer of abstraction.

I am not saying we cannot use them. I am saying we cannot fully trust them. Yet everyone (or maybe just the bubble I am in) pushes the use of AI. For example, I genuinely want to invest time in learning Rust, but at the same time, I am terrified that all the effort and time I spend learning it will become obsolete in the future. And the reason it might become obsolete may not be because the models are perfect and always produce high-quality code; it might simply be because, as an industry, we will accept “good enough” and stop pushing for high quality. As of now, models can already generate code with good-enough quality.

Is it only me, or does it feel like there are half-baked features everywhere now? Every product ships faster, but with rough edges. Recently, I saw Claude Code using 10 GiB of RAM. It is simply a TUI app.

Don’t get me wrong, I also use AI a lot. I like that we can try out different things so easily.

As a developer, I am confused and overwhelmed, and I want to hear what other developers think.

**lhmiles**：
Block the dns on router for two weeks and you will feel alive again

> **dokdev**：
> LoL :) that makes sense, but what if there is a new AI model releases when I am offline.

> > **AnimalMuppet**：
> > You will not suffer much from not adopting a new AI model for two weeks after release.

**ljlolel**：
Claude is a VM. Programming languages are dead https://jperla.com/blog/claude-is-a-jit

> **dokdev**：
> As the article states, it is a "wild experiment". I wouldn't let AI control anything serious end to end. Also if Claude really becomes JIT, it is going to be an expensive one.
> 
> The idea is interesting though.

> **lioeters**：
> Claude is a blackbox created and owned by a corporation. Programming languages will never die as long as people value having control of their means of computation.

**krickelkrackel**：
It's like a gym that has automated weights, and just going there to watch them being moved - our mental muscles aren't trained anymore.

**emerkel**：
I hear you here. I really do.

I don't know where you are in your career, me I am on the backend. But all the time I was working the constant churn of new tools/languages/frameworks and so on, the race to keep up with the vendors just wore me out. And despite all that, building software honestly never changed much.

I have been working with both Codex and Claude, and you are right, you can't trust them. My best practice I have found is constantly play one off against the other. Doing that I seem to get decent, albeit often frustrating results.

Yes, the actual building of the code is either over, or soon to be over. The part that I always considered the "art." I often found code to be beautiful, and enjoyed reading, and writing, elegant code all the time I was working with it.

But the point of code is to produce a result. And it's the result that people pay for. As you mentioned with the evolution of development in your original post, the process and tools might have changed, but the *craftsmanship* in operation with those using them did not.

You make a fair point that this abstraction is different — prior layers were engineered and traceable, and an LLM output isn't. But I'd argue that makes the human in the loop more important, not less. When the abstraction was deterministic, you could eventually lean on it fully. When it isn't, you can never fully step away. That actually protects the craft.

Until AI becomes a "first mover" god forbid, where there is no human in the chain from inception to product, there will always be a person like you who knows where the traps are, knows what to look out for, and knows how to break a problem down to figure out how to solve it. After all, as I have always said, that is all programming really is, the rest is just syntax.

**al_borland**：
> Is it only me, or does it feel like there are half-baked features everywhere now?

This is the argument for actually learning, so you don’t ship half-baked code, because the AI isn’t good enough. The people who are telling you it is likely have a financial interest in pushing the narrative that AI will do it all.

> LLMs, on the other hand, are non-deterministic. Therefore, we cannot treat their outputs as just another layer of abstraction.

This is another problem. A lot of code is written so exactly the same thing happens every time. If AI is going in and changing the logic in subtle ways that aren’t noticed right away when updates are made, because no one understands the code anymore-that’s a problem. In hobby or toy apps, no one cares, but in production code and critical systems, it matters.

> **raw_anon_1111**：
> AI is not changing your logic after it produces your code, you aren’t putting your CLAUDE.md file as the only thing in your build system and rebuilding your code each time you deploy it.

**aristofun**：
Ive lost my ability to do basic and advanced arithmetic calculations or algebraic calculations in school.

That didn’t stop me from getting a phd.

If you think it’s all there’s to programming that llm spits out, then the problem is in you somewhere, not in llms.

**markus_zhang**：
For my personal projects, I use AI for discussion only. I treat it as a better Google and sometimes a *fake* psychiatrist. I don't really fully trust it, so I verify afterwards. If someone else wants to vibe code, I mean please do so as long as you enjoy the process. Personally I enjoy the coding process so I wouldn't want to copy/paste code, let alone letting it write directly in some editor.

For my work I use it extensively. I use Cursor as a senior engineer who breaks down problems and only writes the parts that interests me. I trust AI with other parts and do a review afterwards. AI prompting is a real skill. I don't like it but I don't like my work either.

> **geophph**：
> > I don't like it but I don't like my work either.
> 
> man. this actually seems so profound to me. I feel the same way overall as far as personal vs. work projects and AI use, but this wording hits it on the nose.

> > **markus_zhang**：
> > Yeah, my life is gonna be a hell lot better if I don’t have to work. This is the 3rd day of my first vacation of the year and I already feel a bit better.
> > 
> > Of course the more into a job the less flexible the vacations become. I probably don’t want to be a staff engineer or a lead for that reason. A senior engineer is the best thing in the engineering world, if you don’t like the job.

**geophph**：
I honestly share a lot of the same thoughts and I now feel dumber the more i use AI to build out things for me. It's made me lazy tbh. And sadly, it also helps me do the things at my job faster and "better", but only because "better" works since "good enough" is all that's needed. I get pretty lost if I think about it too deeply...

That said, in response to this:

> I am terrified that all the effort and time I spend learning it will become obsolete in the future

I am of the belief that there's no way that effort and time that goes into learning something like Rust will be wasted. You'll learn stuff and gather a sense for things that might not concretely be applied, but will be helpful when it comes to reasoning about whatever comes next language wise. Learning often is about the journey and not just the destination. I think it'd still be worth it.

Or at least ... that's what I tell myself now as I try to learn Zig.

**raw_anon_1111**：
Context:  I’m 51 years old, started programming in 1986 in assembly on an Apple //e, wrote C and C++ on every platform imaginable from mainframes to Windows CE devices between 1996 to 2012 and part of my job has always been to write production level code.

> *I am deeply sad that we may be losing the craftsmanship side of programming;*

Absolutely no company is paying you for your “craftsmanship”.  You are getting paid to add business value either by making the company more or saving the company more than your fully allocated cost of employment.

> *Until now, every abstraction was engineered and deterministic. You could reason about it and trace it. LLMs, on the other hand, are non-deterministic. Therefore, we cannot treat their outputs as just another layer of abstraction.*

The output of the LLM is deterministic code.  No one is using an LLM in production to test whether a number is even.

You can run unit and integration tests on the resulting code just like your handcrafted bespoke code.  When I delegated tasks to more junior developers, they weren’t deterministic either.

> *For example, I genuinely want to invest time in learning Rust*

I specialize in cloud + app dev consulting. I know CloudFormation like the back of my hand.  I’ve been putting off learning Terraform and the Amazon CDK for years.  Last year, I had a project that needed the CDK and then another project that required Terraform.  I used ChatGPT for both and verified they created the infrastructure I wanted.  Guess what I’m not going to waste time doing now? The client was happy, my company got paid, what’s the point?

> *As a developer, I am confused and overwhelmed, and I want to hear what other developers think.*

If you are an enterprise developer (like most developers are) your job has been turning into a commodity for a decade because their were plenty of good enough backend/full stack/web/mobile developers and it’s hard to stand out from the crowd. AI has just accelerated that trend.

This is no way meant meant to put myself as more than an enterprise developer who happens to know how to talk to people and “add on to what Becky said” and “look at things from the 1000 foot view”.

By definition, today, AI is the worse that it ever will be.

> **icedchai**：
> AI works really well for generating "infrastructure" code like Terraform. Most of it is cookie cutter, and if it isn't, there's a good chance you're probably doing something wrong anyway.
> 
> There's no "craftmanship" there. And I don't want there to be.

> > **raw_anon_1111**：
> > It works well for Python too and JavaScript and on a whim I had it create AppleSoft Basic code.  Trust me there is no “craftsmanship” in a LOB CRUD app or yet another SaaS app. Your CRUD enterprise code is just as cookie cutter.  You’re not doing anything groundbreaking.
> > 
> > Absolutely no one gives a damn  about “craftsmanship”.  I just got rave reviews from a customer for my completely  AI generated website for their internal use. I didn’t look at a single line of code and haven’t done any serious web development since 2002 in classic ASP.
> > 
> > The customer is happy.  My company is happy and they continue putting money in my bank account on the 1st and 15th.  I use to think like you. But I quickly grew out of it.

> > > **icedchai**：
> > > Heh. I think we agree. You may be referring to the OP.

**TowerTall**：
i don't get. yes, if you just prompt it "make me an app" you learn nothing but you probably also end up with an app that is crap as best.

I you instead "promote" yourself to architect or lead dev and you steer the ai as it it a team of junior dev you must manage you can learn a lot. not only will you have deep architecture discussion with ai where you, together, explore various approaches and ways to do things.

an if you do spec driven ai development where you write the specs you will end up with an app that resemble the way you prefer apps to be written.

Just because ai can cook something up in no time doesn't exclude you from being involved.

**bad_username**：
Sounds like you didn't lose the ability, you lost motivation. Why learn Rust, you say, if an LLM can crank out a Rust app for me, and it will be good enough?

LLMs may have removed the critical need for a SW engineer to know details, like the syntax of Rust or the intricacies of its borrow checking semantics. But LLMs, I maintain, didn't remove the critical need for an engineer to learn _concepts_ and have a large, robust library of concepts in your head. Diverse, orthogonal concepts like data structures, security concerns, callbacks, recursion, event driven architecture, big O, cloud computing patterns, deadlocks, memory leaks, etc etc. As long as you are proficient with your concepts, you will easily catch up with the relevant details in any given situation. Once you've ever seen recursion, for example, you will find no trouble recognizing it in any language.

That's the beauty of LLMs : you don't _have_ to be good at technical details any more. But you still have to be very good with concepts, not just to be able to use LLMs properly, but also _be in control_ of their work. LLM slop is dangerous not because of incorrect details like bad syntax. It is dangerous because it misplaces concepts: it may use a list where you need a hash map and degrade performance, it may forget a security constraint and cause a data leak, or it can be specific where it needs to be general, etc. An engineer needs to know and check the concepts if they want to remain in control. (And you absolutely do want that.)

But it is impossible, or very impractical, to just learn an abstract concept out of thin air. The normal way to learn a concept is to see its concrete instantiation somewhere, in all its detailed glory, and then retain its abstract version in your head.

So, the only way to stay relevant and stay in control is to have a robust concept library in your mind. And the only way to get that is to immerse yourself in many real technical situations, the details of which you must crack first, but free to forget later. That is learning, and that is still important today in the age of LLMs.

**sathishmg**：
I got the creativity back, by asking more questions :)

**Blackstrat**：
I've been reading these threads for a while and the one thing that is clear from all of them is that the individual is CHOOSING to surrender their intellectual expectations to the AI.  You don't have to make that choice.  Further, a developer's value increases exponentially the more familiar they become with the industry/domain of the company for which they are working.  No, no human will ever "write" code as quickly as the machine.  Nor will any machine ever understand what to build for a given application.  It has to be told.  As for the continuing level of abstractions?  While true, the best programmers didn't depend strictly on that abstraction.  They sought to understand the machine.  One fundamental problem that I encountered in my later management years was the number of people entering the field that had no business doing so.  Consequently, many lasted only a few years before giving up and trying something different.  I retired from the business after 40+ years and I knew plenty of greybeards that I would trust far more than any existing "AI" solution.

**satvikpendem**：
I don't get, just...stop using AI? Learn what you want regardless of AI, as knowledge is its own reward.

**digitalhobbit**：
I think it's all up to you what you make of this situation. For context: I've been programming for well over 40 years, and I've worked as a software engineer (or eng manager) for close to 30 years. I've gone through cycles of coding a lot and cycles of focusing more on architecture, product, or the business side. And I loved coding when I first started. Making pixels appear on the monitor felt magical back then. But coding got old over time, and I've found myself drawn to higher level concerns, including business, product, engineering architecture trade-offs, etc.

Lately, I've found this new AI assisted coding world immensely empowering. In the last few weeks, I've built web apps (e.g. Astro), an agentic pipeline (Python, Pydantic AI), a proof of concept for a roguelike game (C++ with libtcod), and I'm now working on a cross-platform desktop app in Tauri 2 (Rust and TypeScript). And I'm learning a ton. Not necessarily low level language details - I'm increasingly trusting those to the LLM - but application architecture, product design, marketing, agentic engineering, etc. I've found this genuinely empowering and haven't felt this motivated about application development in decades.

I'd say zoom out a level and see if you can find the joy in learning some of the higher level concerns.

**DarkTree**：
> I genuinely want to invest time in learning Rust, but at the same time, I am terrified that all the effort and time I spend learning it will become obsolete in the future.

I would say ask yourself this: Who would be better positioned to build a Rust application using LLMs, someone who has never learned Rust or someone who knows it well?

**kartika848484**：
skill issue

blaming ai for real?

**RedCats**：
This is actually a good thing, bro. Let's free up the mundane coding to handle marketing and uncover more opportunities

**bitbybit_ch**：
I think the anxiety often comes down to how we choose to use such tools. I’ve started following a similar philosophy to keep my skills sharp:

- I use AI primarily for a rough prototype, design elements, UI scaffolding, and quick proof-of-concepts. It’s great for seeing if an idea might work. But for the final product, especially the critical logic I write it by hand with some assistance AI autocomplete etc.

- Even when AI generates a snippet, I force myself to audit every line. It often feels unnecessary or slow, but it’s the only way to ensure I actually understand the codebase. If you can’t explain why a line of code is there, you’ve lost control of your software. Might work for now and might actually be ok for the product you are building but generally not a fan of it.

- This shift allows me to stop sweating the "dumb" recurring tasks and focus on the big-picture architecture. AI handles some boilerplate. I handle the systems design.

At the end of the day, I still want to be the one who built the software, not just the one who prompted it into existence. But the same way i don't want to set every bit in the software code for a web-app and use abstract languages i think it has it's spot to get more done.

Also of course instead of reading through hours of documentations i can read through a documentation summary that's most of the time good enough.

