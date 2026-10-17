# Show HN: Bloomy，K-12 的 AI 掌握学习

- 链接：https://news.ycombinator.com/item?id=48981136
- 作者：alexsouthmayd
- 获取方式：Hacker News 帖子与评论全文

---

## Launch HN: Bloomy (YC S26) – AI-powered mastery learning for K-12（alexsouthmayd，102 分）

（讨论共收录 107 条评论，缩进表示回复层级）

Hi HN, I’m Alex Southmayd, the founder of Bloomy (https://bloomylearning.com) – an AI-powered mastery-learning platform for K-12 students. Bloomy provides students with an AI tutor alongside adaptive curriculum (right now Math, English Language Arts, and Writing).

How it works: we diagnose students’ skill gaps, place them on personalized learning paths, and give them standards-aligned lessons and a Socratic AI tutor that scaffolds their learning without just giving away the answer.

The goal is to solve the Bloom 2-sigma problem (https://en.wikipedia.org/wiki/Bloom%27s_2_sigma_problem) with AI.

Short launch video: https://tinyurl.com/bloomylearning

Longer product demo: https://youtu.be/XHvoKt6qMeo

Families access for Bloomy: https://bloomylearning.com/families

I started as a teacher. I taught 7th-grade English and writing with Teach For America, and every day I struggled to deliver differentiated instruction to 30 students with 30 different sets of needs. Some students needed remediation, some needed acceleration, and many needed a tutor sitting next to them helping them reason through the next step.
Benjamin Bloom’s two-sigma result—that one-on-one tutoring can produce much better outcomes than conventional classroom instruction—always felt intuitively true to me. The hard part was making that kind of attention affordable and available to every child.

Then AI changed the cost curve. When I saw schools such as Alpha organize academics around mastery rather than seat time, the model clicked. If you’ve heard of Alpha School, that is directionally the kind of learning model that inspired us. But I kept thinking about the families and schools that already exist: homeschool families, microschools, hybrid schools, and regular classrooms where most children are today.

Most students and teachers see learning gaps at the wrong resolution. They get a grade, percentile, benchmark score, or broad standard—not “this is the next skill this student should learn.” Existing personalized-learning products often feel like digital worksheets: they provide plenty of practice, but not much diagnosis or teaching. Very few have AI tutors providing the core instruction.
Bloomy starts with a diagnostic—we integrate with third-party assessments and provide our own—and creates a learning path for each student. Students work one skill at a time, receive a short lesson, practice at an adaptive difficulty, and only move forward after demonstrating at least 90% mastery. The learning path updates as the student works, based on their performance and our knowledge graph of skill prerequisites (built in collaboration with Learning Commons / Chan Zuckerberg Initiative).

Each skill has three stages. Base Camp teaches the concept with worked examples. Climb provides guided practice and Socratic support. Summit is an independent ten-question mastery assessment with no hints or AI assistance. Students need to achieve 90% on the Summit to advance. If they struggle too much, they’ll be routed to a different skill better suited for their level.

BloomyBot is not a blank chat window but rather a live, interactive, and observant digital tutor. During practice, it receives the active passage or problem, the question, the student’s attempt, an authored explanation, and relevant misconception context. It follows a scaffolded tutoring ladder: first asking what the student tried, then pointing toward the concept, suggesting a strategy, working through one step together, and only providing heavier scaffolding after the student has struggled, adapting to and learning from the student along the way. Students can interrupt it, and we’ve begun to roll out multilingual support for Spanish, French, and a few other more niche languages that customers have asked for.

We currently use a variety of Anthropic and OpenAI models for BloomyBot. The tutor is restricted to the current lesson, redirects unrelated questions, limits conversation length, and is unavailable during mastery assessments. The language model does not choose the curriculum or decide whether a student has mastered a skill.

That separation is important. A conventionally “helpful” AI response can be a bad tutoring response: if it gives away the answer, the student completes the task but may not learn anything. Our goal is not to build a homework-answering chatbot. It is to put AI inside a structured loop of diagnosis, instruction, practice, feedback, and independent mastery.

LLMs can still be wrong, and we do not claim our constraints eliminate that. We reduce the surface area by grounding BloomyBot in authored lesson content, keeping it on topic, logging conversations, and removing it from assessments. Teachers and parents can review tutoring activity, students can report problems, and safety signals trigger human alerts and a backup audit.
We also do not see Bloomy as a replacement for teachers, parents, or human tutors. A good human tutor is better. The narrower question we are testing is whether, during a bounded learning session a student would already be doing, a context-aware tutor can provide better help than static “correct/incorrect” feedback. Longer term, the question becomes more whether a student would perform better with one-on-one AI tutoring (at least in certain aspects of the curriculum) than with many-to-one instruction in a medium- or large-sized classroom.

Bloomy is now being used across several settings: traditional districts, charter schools, hybrid schools, microschools, homeschools, and families looking for additional academic support. In an early pilot at a charter school in Massachusetts serving ~150 students in grades 6 through 8, students averaged roughly 1.8 times the expected winter-to-spring NWEA MAP growth. This was an observational pilot, not a randomized study, so we treat it as an encouraging signal rather than proof that Bloomy caused the difference.

Parents and teachers can see what a student has mastered, what is in progress, and where support may be needed. We have found that adults generally do not want another generic score; they want to know which small number of skills deserve attention this week.

Bloomy makes money through family subscriptions and school licensing. ELA costs $39/month or $279/year per learner, and Writing Studio costs $19/month or $139/year. Math is scheduled to launch July 31 at the same price as ELA. Schools and microschools pay per student, with pricing varying by subject coverage, enrollment, rostering, and implementation needs.

Because children use Bloomy, we collect learning responses, progress data, and tutoring conversations. We do not sell personal information, use child data for behavioral advertising, or permit model providers to train general-purpose models on identifiable child data sent by Bloomy. We have Zero Data Retention agreements with both Anthropic and OpenAI. Parents and schools can request access, export, correction, or deletion under the applicable account or school agreement.

More background on me: after Teach For America, I taught and designed GMAT and GRE curriculum for Manhattan Prep / Kaplan, led the driver acquisition team for Lyft’s New England markets, completed an MBA at Stanford, and led AI transformation projects at McKinsey (so when models finally became good enough this past January to achieve the kinds of things I am pursuing with Bloomy, I was in the right place at the right time to begin building). Bloomy brings together the different parts of my career that I care most about: educational outcomes, learning design, building products, and getting useful technology into people’s hands.

I’d especially value feedback from parents, teachers, engineers working on child-facing AI, and people who have built tutoring, assessment, or adaptive-learning systems. Does the separation between guided AI help and independent mastery make sense? Where do you see the greatest potential with AI in education? Where are our safeguards insufficient? What evidence or product behavior would you need to trust something like this with a student?

Certainly there are many dangers and pitfalls we must beware of, too, but I believe we can really move the needle in K-12 (for the first time in a long time) if we use AI responsibly and intelligently.

**_doctor_love**：
*> What evidence or product behavior would you need to trust something like this with a student?*

I would need the product to not exist. I don't want this anywhere near a child. I want humans instructing humans, teaching empathy, connection, and - most importantly - learning to learn.

Anything short of that is just building Brave New World. Electroshock the kids if they reach for forbidden knowledge.

I'm sorry to be so negative since I'm sure you worked hard on this but I find all products in this category to be 100% reprehensible.

"Computer-assisted learning. What an insult, to have the computer teach the human."

- Russ Ackoff

> **alexsouthmayd**：
> I appreciate your honesty! I agree that having a talented human teacher for every student would be ideal.
> 
> Many of our schools just don't have the teacher headcount to deliver meaningful instruction to their students. Some schools (one non-profit in Africa, for instance) have to choose between having no teacher or having Bloomy.
> 
> Are you putting forward that you'd prefer the former? No judgment if so, just trying to understand your framework here.

> > **great_psy**：
> > As ai replaces more and more jobs, there should be plenty of humans available to teach. Even if the teachers are ai assisted themselves.

> > > **alexsouthmayd**：
> > > This is a very interesting point I've heard from one other very smart person in this space. It will be interesting to see how that plays out.

> > **barefootford**：
> > If there is really no teacher around, the premise is 7 year old kids will show up to teacher-less classrooms and then hop on a computer for a few hours (a whole day?) and willingly sit through hours of tutoring? Rather than just leaving and having recess all day?

> > > **alexsouthmayd**：
> > > Ha, free recess all day sounds nice :)
> > > 
> > > The more accurate way to describe these situations is overwhelmed teachers with overflowing classrooms where students are left to their own (rather than schools fully absent of an adult).
> > > 
> > > Recommended Bloomy usage is ~30 mins per core subject. So certainly not the whole day. I have my own very strong misgivings about screen time for kids.
> > > 
> > > So the idea in this situation is individualized instruction of skills that can adapt live to a student, in a concentrated and limited period of tech time. Hopefully this creates a better outcome than the status quo.

> > **_doctor_love**：
> > I would want to solve the problem way upstream. Obviously I want children to receive education.
> > 
> > I would also say that looking at the problem like it's teacher headcount that's the issue is assuming a specific education model. If there is only 1 teacher and 300 students, you can't meaningfully do a lecture-style one-way transmission of information. That's outdated anyway and not what the students need.

> > > **alexsouthmayd**：
> > > I like that you're touching on a bit of Horizon 3 education here! I agree that the model is antiquated and is long overdue for an upgrade.

> > > > **_doctor_love**：
> > > > You bet. Like I wrote to 'dang I'm really not trying to hate on what you're doing, just offering my very candid take on products like this. I care very much about education and I'm happy to see someone trying to do something about it. In that sense I applaud your efforts and hope that Bloomy leads to some good outcomes for somebody. I simply feel that more AI is not the answer.

> > **andai**：
> > >Some schools have to choose between having no teacher or having Bloomy.
> > 
> > Right. I remember in high school, when I learned about Anki, being amazed by it. I remember thinking, well, we could replace most of the time I'm spending here, so inefficiently, with a few minutes of Anki per day. Wouldn't that be nice!
> > 
> > Took me a while to realize, well, learning isn't exactly the main point of school. If it were, they might invest a little more effort into making sure people actually remember what they learn! (Ebbinghaus isn't exactly cutting edge stuff.)
> > 
> > So I remember thinking, rather cynically, well what we're doing here could be replaced with an app! (For context this was in the 2000s.) Not that I thought education *should* be just an app, obviously, but rather, my complaint was that what I was getting was strictly inferior to one.
> > 
> > I had hoped that the advent of AI would open up fully personalized learning tracks, but instead what we seem to have gotten is technology being used to surveil children all day (a bit of an unpleasant thing to train them for, no?), and to ensure they are conforming even more tightly to someone else's ideas about how they ought to be spending their time.
> > 
> > To clarify, I think that someone else telling me what I'm supposed to be interested in[0] (with threat of punishment no less) is deeply offensive to the basic fact of *being an organism*, but how inefficiently it's being done is a second insult on top of the first one.
> > 
> > That being said, I welcome innovation in this space.
> > 
> > ---
> > 
> > [0] I later discovered *Education On The Dalton Plan* in my school library, being apparently the first person in the school's existence to borrow it. The main idea of the book being that if the child directs his/her own learning, they're liable to actually learn something.
> > 
> > My school *was* a Dalton school, at least ostensibly, but most of the ideas in the book were illegal in my country. (And new laws passed while I was there squeezed it even further!) Turns out what I was after had been tried, over a century ago, but the government decided it was simply too offensive that the average person should be allowed to decide how they're going to spend their time -- at such an early age, no less!

> > > **alexsouthmayd**：
> > > Yes—and the whole hypothesis here is that teaching could be more efficient than it currently is!

> **calebm**：
> Just because it's computer-assisted doesn't mean the computer is doing the teaching (any more than saying a gun killed someone). The people behind it are the teachers, and the computer-assisting is a way to amplify that teacher's reach (like a YouTube video).

> > **_doctor_love**：
> > [flagged]

> > > **dang**：
> > > Your GP comment was borderline against the site guidelines, since you basically went straight to shallow dismissal, flamebait, and generic ideological battle. I didn't respond with a moderation comment because I understand this topic brings up strong feelings and there's a lot to say on all sides.
> > > 
> > > Your reply here, though, is flat-out against the site guidelines and it's not ok to post like that to HN, least of all in someone's launch thread (whether it's a YC startup or not).
> > > 
> > > No more of this please. You're welcome to make your substantive points thoughtfully, but if you'd first review https://news.ycombinator.com/newsguidelines.html and take the intended spirit of this site more to heart, we'd appreciate it.
> > > 
> > > Edit: your previous comment was a personal attack as well: https://news.ycombinator.com/item?id=48981467. Please stop this.

> > > > **_doctor_love**：
> > > > *> your previous comment was a personal attack as well: *
> > > > 
> > > > Brother, I meant what I wrote.
> > > > 
> > > > That said, I'll cool off for a bit. I'm not here to rain on anyone's parade but as you said, products like this stir extremely strong feelings on my end. I find the framing offensive, exploitative, and dehumanizing.

> > > > > **dang**：
> > > > > Personal attacks aren't ok whether you meant what you wrote or not.
> > > > > 
> > > > > I get that you feel strongly about this - probably most of us share these feelings in some form; I know I do. We just need to talk about the topic thoughtfully and respectfully, and not assume that someone with different views doesn't care about kids (for example) or doesn't share the same concerns.
> > > > > 
> > > > > Let's put it this way: I appreciate the thoughtful component of your comments - we just need you to cool off on the attacking component.

> > > > > > **_doctor_love**：
> > > > > > Clearly we have different definitions of what constitutes an attack, that said, I know you're fighting an eternal uphill battle on HN so I'll rest my case.
> > > > > > 
> > > > > > I will say that I find some of this kind of moderation very confusing. I feel that I often see folks going way harder than anything I've said today and there's no moderation hand-slaps visible. Possibly the sensitivity is greater here since it's a Launch HN thread, so I appreciate that. But please take my feedback for what it's worth and reflect on it a bit.

> > > > > > > **dang**：
> > > > > > > > *very confusing. I feel that I often see folks going way harder than anything I've said today and there's no moderation hand-slaps visible.*
> > > > > > > 
> > > > > > > You're quite right and of course it's confusing. But it has a simple, unsatisfying explanation: we can't read everything that gets posted here, let alone moderate it all. There's far too much for us to read even 10% of what gets posted here.
> > > > > > > 
> > > > > > > If you see a post that ought to have been moderated but hasn't been, the likeliest explanation is that we didn't see it. You can help by flagging it or emailing us at hn@ycombinator.com.
> > > > > > > 
> > > > > > > https://hn.algolia.com/?dateRange=all&page=0&prefix=false&query=likeliest%20explanation%20by%3Adang&sort=byDate&type=comment
> > > > > > > 
> > > > > > > Btw, I'm going to try an experiment and respond to your GP comment with a non-moderation reply, just because I find the topic interesting, and also in the hope of communicating what I said above: the thoughtful component of the conversation is fine. (No obligation to reply of course.)

> > > > > > > > **_doctor_love**：
> > > > > > > > *> Btw, I'm going to try an experiment and respond to your GP comment with a non-moderation reply, just because I find the topic interesting, and also in the hope of communicating what I said above: the thoughtful component of the conversation is fine. (No obligation to reply of course.)*
> > > > > > > > 
> > > > > > > > I had logged off to chill out a bit so missed that you wrote this. Sorry to admit my ignorance but I don't know what this means? I appreciate your engaging with me fwiw.
> > > > > > > > 
> > > > > > > > I'm sucked back into work for most of the rest of the day so if you don't see a reply from me that's why, I'm not off stewing in a huff.

> > > > > > > > > **dang**：
> > > > > > > > > Sorry, it just took me a long time to write what I wanted, plus I'm on a flight with slow wi-fi. It's there now: https://news.ycombinator.com/item?id=48982399.
> > > > > > > > > 
> > > > > > > > > No worries—I appreciate the exchange!

> > **alexsouthmayd**：
> > Great point. The responsibility and consequences of the tech (both bad and good) rest upon the humans who designed it.

> **blast**：
> This position is so extreme, you'd have to have called Reader Rabbit "electroshocking kids" as well.

> **pixel_popping**：
> So you are against a child learning by himself with a book?

> > **alexsouthmayd**：
> > I love self-learning. I read a lot of books as a kid (at one point my dad even got mad at me because I was ignoring him while reading yet another book).
> > 
> > At the same time, I believe -- and have seen firsthand as a teacher -- that many students need instruction to learn certain concepts. Even if they don't need instruction, they need a framework or structure to learn within. (One of the big challenges I had to solve early on during my TFA time was classroom behavioral management -- it doesn't matter how good your pedagogy is if your kids won't listen to you).
> > 
> > Great teaching involves modeling a new skill or concept, providing some amount of training wheels, and then seeing it through to independent mastery. Is there a lot that a student can learn on their own simply by reading? Absolutely. Kids should read more books.

> **jrflo**：
> LLM assisted education =/=> no empathy is taught human-to-human

> > **alexsouthmayd**：
> > I have a slightly different perspective based on how I've observed schools use Bloomy. Focused use of Bloomy has allowed teachers to deliver higher-touch support to students who need it most (it also helps that our system identifies common learning patterns so teachers can conduct small-group instruction).
> > 
> > Human empathy is not optional, but rather required. Furthermore humans need to make the connection between the academic skill that's being taught and the real world application or relevance of that skill.
> > 
> > So LLM-assisted education has the potential to help humans be MORE empathetic and deliver the higher-leverage aspects of education only humans can do, while freeing them up from some of the inefficient many-to-one skill instruction for discrete concepts.

> > > **dang**：
> > > (If I'm reading it correctly then "=/=>" means "does not imply", i.e. you and jrflo are agreeing.)

> > > **alexsouthmayd**：
> > > I misread this -- yep I agree with the original statement!

> **dang**：
> This problem has been around a long time. Like many other HN users, years ago in primary school I became a problem for my teachers because the curriculum was too easy for me.
> 
> The school dealt with it by sitting me in front of a big box of color-coded dossiers called the SRA Reading Laboratory [1, 2] and telling me "read these at your own pace". The boxes looked just like this: https://sites.google.com/view/objects-of-school-days-past/sra-reading-kit and may well have been kicking around since the 1960s.
> 
> The trouble was that "at your own pace" was code for leaving me alone in front of a box. I don't recall the reading being either interesting or hard, but it solved the problem for my teachers, since I wasn't the type to act out in class. The real lessons I got out of it were lessons in isolation and drudgery.
> 
> Looking back, I badly needed contact with an adult who could teach me things. That didn't happen—not then, and not much in later school years either. Was it the schools' fault? They simply didn't have the resources to give me the human  instruction I needed.
> 
> Surely all agree that children need human contact, empathy, connection, meaningful teaching. But it doesn't help children if we hold to those principles without facing how resource-constrained this problem is. If we do that, then many children end up with nothing, or next to nothing, as happened to me long ago.
> 
> Years later, when I read a little history, older novels, and the like, I learned how the nobility had educated their children: not just with dedicated personal tutors but different ones for different subjects. That's what one would do if one could afford entirely human, entirely interactive instruction, and of course it was only available to the 0.0001%. When I read those passages I felt envy and shame at not having what I would (to this day) call a real education, and those feelings have never entirely gone away.
> 
> My point with this anecdote is: I don't think I would have been worse off if they had sat me in front of a computer instead of a box of boring readings produced by education researchers. And if the computer had had software that could adapt to me and my interests, so much the better. At least I would have learned things, even though I still would have suffered from lack of human connection that, at that age, I was unaware how much I needed.
> 
> [1] https://en.wikipedia.org/wiki/Science_Research_Associates
> 
> [2] https://hackeducation.com/2015/03/19/sra

> > **andai**：
> > >Look back, what I clearly and badly needed was contact with an adult who could teach me things. That didn't happen, and in fact happened very little in my later school years as well. Was it the schools' fault? They simply didn't have the resources to give me the human contact I needed.
> > 
> > When I was in school I remember thinking, when the futuristic utopia we envisioned in the 2000s arrives, a great deal of people will teach. It will be normal for professionals in all fields to spend some portion of their time teaching. How could it be otherwise, in a civilization which intends to preserve its knowledge and wisdom?
> > 
> > I remember asking my math teacher for applications and she mumbled a non-answer with some embarrassment. It was only years later that I realized, well my god, she's never stepped foot outside of a school in her entire life, no wonder she doesn't know about applications. It would have been nice, I think, to have had some contact with folks who had!
> > 
> > (Later still, I realized that I had reinvented the father from first principles...)

> **andai**：
> What's your take on Anki?

> > **alexsouthmayd**：
> > I've personally both had and seen great success with the Anki approach for specific terms (e.g., vocab flash cards). Spaced repetition is built into Bloomy based on similar principles. A little harder to get right as you're now spacing out skills/concepts rather than just word/definition/context. Something we hope to fine tune over time.

**dprkh**：
What is your approach to evaluating LLM outputs?

> **alexsouthmayd**：
> A few things:
> 
> First, every BloomyBot response streams through an inline safety classification, and then an independent second-pass audit sweeps every stored message — a deterministic rule layer merged with a separate LLM classifier, taking the highest-severity result. It flags three categories (crisis, distress, inappropriate) across every language we support, and confirmed flags alert the teacher and school. We also constrain what the model is allowed to do: the tutor won't reveal answers, and it's completely absent from Summit assessments — so an LLM output never decides whether a student has mastered a skill. That comes from scored assessment performance against our 90% threshold.
> 
> Second, a nightly cron job runs across all BloomyBot interactions to flag erroneous outputs (so far, none) and safety alerts (these happen real-time anyway, but the cron job is a backup).
> 
> Third, I sample the interactions manually. I've read most interactions so far (although this will become much harder with more scale).
> 
> Finally, we are building structured evals to draw inferences across grade levels, skills, common misconceptions, etc. Ideally we will be able to identify the optimal level of scaffolding to help students achieve mastery, but that will take more data and time.

> > **KomoD**：
> > Was this comment generated? Your other comments use "--" instead of an em dash... or were all of them generated, but you forgot to replace them with "--" in this one?
> > 
> > See: https://news.ycombinator.com/newsguidelines.html
> > 
> > > Don't post generated text or AI-edited text. HN is for conversation between humans.

> > > **alexsouthmayd**：
> > > I've been extremely inconsistent in my dashes today as I flip between different devices :)

**motoxpro**：
Happy that this is being tried. I find it weird, sad, unfortunate, etc. that everyone in tech thinks about scientific discovery and drug discovery as AIs boon to society over education.

Every quality of life metric (life expectancy, income, etc) goes up with better education. I guess it’s because most people in tech grew up in neighborhoods with nice schools and went to college so they don’t think about it.

Anyway, great luck.

> **alexsouthmayd**：
> Thanks! I think people are rightfully skeptical about EdTech and AI -- esp. with kids. But we also need to try to innovate in this space, and I believe (from my experience as a teacher as well as my experience seeing students learn on Bloomy) that there is great potential here.

**Recursivedude**：
There's a place for AI to help people, but given there's no shortage of humans it's difficult to see why we are so egar to replace them. The constant affirming nature of AI coupled with the restrictive nature of the safety layer makes AI both mentally dangerous and politically dangerous.

> **alexsouthmayd**：
> AI is certainly not a monolith. Many aspects and use cases of AI are dangerous -- fully agreed.
> 
> As others have commented, it would be better if we could give every student their own personal tutor. Until that's possible, I believe AI can be helpful in education, as long as it's responsibly designed and monitored.

**verdverm**：
Childhood psychologists are warning about giving Ai to children, very similar to social media and generally screen time.

How does this factor into your business?

> **alexsouthmayd**：
> I just posted something pretty relevant to this in a different comment. Totally agree with the dangers. 2 important points:
> 
> 1. Not all AI is the same. I see 2 MECE categories in education: AI that does all the thinking/execution for you (the outsourced brain), and AI that is designed to fulfill specific coaching/tutoring roles. If we design AI to ask great questions and find the Socratic thread with students, we can actually make students think harder and learn faster.
> 
> 2. Social media is full of cheap dopamine. See my comment about 'effortful dopamine' for my perspective on this.

> > **hasteg**：
> > I agree that using AI as a "tutor" to help teach yourself things is very useful and works great, I've been doing that myself quite a bit. How do you stop students from being able to just use it as a second brain? I assume there's some sort of guardrails you have so it won't just give the answer? How do you ensure that there's an adequate amount of "struggle" that the kids are going through before just explaining the answer? I feel that that would be the challenging piece of the puzzle.

**cynicalpeace**：
The fastest, most surefire way to nuke your child's brain is to give them a screen.

There is certainly room for software to design a curriculum for the parent or teacher to use. We have tried (and failed) to find such a thing for our homeschool curriculum.

But giving the kid a screen? If you're even a midge honest with yourself, a screen will de-educate your child, leading to the opposite of the intended consequence.

> **alexsouthmayd**：
> I empathize with the screen time concerns - the reality is most kids in classrooms are already on screens, which are doing very little to move educational outcomes (from what I can tell based on the NAEP evidence).
> 
> And then you also have kids at home who are on TikTok or Instagram reels - combining screen time with easy dopamine.
> 
> Some kids using Bloomy decide to use it at home in lieu of social media time. I'd take that as a win. Cheap dopamine erodes focus and mental resilience. Bloomy focuses on ‘effortful dopamine.' We structure the experience so that students generate reward by conquering academic challenges, training the brain to find satisfaction in effort, patience, and mastery rather than passive consumption.
> 
> I'd be curious to see data that can isolate the relationship between educational outcomes and small bursts of high-quality instruction delivered via tech. That's one longer-term outcome we're trying to demonstrate. So far our efficacy results (still early pilots, but correlative) appear to be incrementally positive.

> > **cynicalpeace**：
> > Regardless of the content on the screen, the screen time is bad for kids.
> > 
> > Even desiring pixel-represented "data" for this fact that is obviously observable irl is itself perhaps a result of excessive screen-time, leading to spreadsheet brain, but I can gratify you with these studies: [1], [2], [3], [4], [5]
> > 
> > Of course, no study will exactly disprove the claim that there is *some* possible content that is a net positive for kids, akin to how no study can prove that unicorns don't exist. But this is exactly the kind of brain-melt, culturally destructive kind of thinking you could expect for demanding "data" for every obvious fact.
> > 
> > Screen time is simply bad for kids. Don't give your kids a screen. Give them a ball, a stick, a book, etc
> > 
> > [1] https://jamanetwork.com/journals/jamapediatrics/fullarticle/2808593
> > [2] https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2821176
> > [3] https://red.library.usd.edu/cgi/viewcontent.cgi?article=1002&context=se-fp
> > [4] https://jamanetwork.com/journals/jamapediatrics/fullarticle/2821940
> > [5] https://pubmed.ncbi.nlm.nih.gov/32202633/

> > > **alexsouthmayd**：
> > > Thanks! I’ll have a read. Appreciate your taking the time to source and share these.

> **tekne**：
> Eh.
> 
> On one hand -- phones are evil, and the world is no longer 2004.
> 
> On the other hand, I would *not* be the same person if I didn't get that laptop.

**scoriiu**：
curious how the tutor handles a kid who's confidently wrong. from the description the ladder kicks in at the first sign of struggle, which sounds like it's built to prevent mistakes rather than use them. kapur's productive failure work points the other way, students who commit to a wrong approach and then get shown exactly where it breaks tend to keep the concept. the ones who got steered away before making the mistake don't.

does bloomybot ever just let a wrong approach play out and do the postmortem after? also when a struggling student gets rerouted to an easier skill, can you tell that apart in your data from one who was thirty seconds away from the useful kind of failure? the summit gate tells you they arrived. it doesn't tell you whether the help in the middle did the teaching.

> **alexsouthmayd**：
> Good questions. I like that you're digging into the mechanics.
> 
> First principle: BloomyBot does not proactively engage the student unless they make 3 mistakes in a row in "Climb" (the practice portion). Then it engages them.
> 
> Otherwise, students can engage BloomyBot when they feel they need assistance.
> 
> If the student is confidently wrong and attempts to answer a question, they'll see the feedback that they're wrong, with an explanation. They can then clarify with BloomyBot. The goal here is (as you reference) to cultivate productive struggle. So we DO want the student to try their approach.
> 
> On getting rerouted to easier skills: students get 1 chance to attempt and fail a Climb. Enough questions wrong in a row (assuming they're trying) = signal that they either aren't ready to learn the skill or that they didn't pay attention to the instructional portion in Base Camp. We give them the benefit of the doubt and assume the latter. If they fail Climb a second time, they get routed to a prerequisite skill.
> 
> The Climb gates Summit through Bayesian Knowledge Tracing. Wilson et al. (2019) derived an “85% rule” from formal models of learning: training is most efficient when learners succeed at about 85% of attempts. So Bloomy uses BKT (Corbett & Anderson, 1995) to update each student’s estimated per-skill mastery after every response, and routes students to skills within their Zone of Proximal Development.

> > **scoriiu**：
> > that's a clean answer thanks. the 85% rule for BKT routing is more principled than most. the one thing i'd still watch is wether summit mastery still holds or decays over time, since BKT can't tell "build the schema" from "learned to pass the gate". thanks for the detail.

> **nubg**：
> do you think running LLM output through .lowercase() will hide the fact that you are posting AI generated comments?

**theodorewiles**：
I am here to tell you HELL YES and TAKE MY MONEY. I am such a fan of the idea of using AI to help give personalized and structured AI lessons in the hands of students and let them cook!

- It looks like you are gating family access to K-3 for now and I think that's right. I wouldn't really be comfortable giving my first-grader a live chatbot. Maybe I would think about whether there are other non-persona modalities that could still be self-directed (i.e. I am uncomfortable with a chatbot interface on this for a six year old but gamified flash cards with options could be different).

- I think the other issue is with motivation. I have various duct-tape versions of these types of agents and the thing about it is if you're doing the learning right it can be HARD. So I would think about using motivational interviewing or other techniques to help keep the user coming back and motivated.

- I would really think about the assessments here too. Many people are worried about LLMs ruining student evaluations, but if you could bake in reliable, flexible exams that gauge user progress (even for something like a "Did you read this" quiz) I would bet teachers would like it. There is likely so much you could do on student progress observability and e.g. structuring team-based projects or having targeted student working groups to hash out hard concepts in a targeted way, etc.

This is such an interesting market and use case too because the educational system might be very structurally set up to the current pedagogical staffing model (think about the incentives for teacher's unions and administrators). If you think it will be hard to change that system as quickly as you want I would also try to have an offering direct to families / home-schoolers. I think there is also a cottage industry of tutors that might benefit. Maybe partnering with the textbook publishers? I'm sure there are some "Teach your kids better" influencers that would get you into some feeds?

> **theodorewiles**：
> Other thoughts:
> 
> - I think the other mistake I see here is trying to over-engineer a deterministic learner path instead of giving the AI more free reign on best next interaction and a set of goals it needs to accomplish through the session; it can feel more responsive and free-form that way from the learner's POV. 
> - If you had voice here you could also make the screen optional. In my experience typing out long answers to questions can take a while too - so a voice mode might be helpful for learners.  It would also be cool if people could take a 'photo of their work' for e.g. math equations done by hand.
> - To the earlier point on family end-market, an interesting idea is modeling bloomy - have some grown-up oriented courses so you can learn with / side-by-side with your child? Just an idea.

> > **alexsouthmayd**：
> > Funny you say that. We actually just released a voice mode that allows students to engage, interrupt, and even switch languages.
> > 
> > I'd love to design this to a greater extent throughout the experience so Bloomy becomes voice-first (where applicable).

> **alexsouthmayd**：
> Thanks for the support!
> 
> On motivation: we have something called Bloomy Bucks. Kids earn these for getting questions right, mastering skills, and being consistent. They can then redeem them for privileges that the teacher/school/parent sets (e.g., homework pass, game time, whatever). This is part of the effortful dopamine that I, personally, think is the right approach to motivation. A lot of people will disagree with me on this, but I think that some amount of extrinsic motivation (something we've already been doing for quite a long time with letter grades) can cultivate intrinsic motivation. One specific application of this is that students can earn up to 1 Bloomy Buck for a meaningful interaction with BloomyBot on a given question.
> 
> On assessments: imagine if we could get rid of assessments and just have live diagnosis happen all the time? With enough data from practice and mastery, that should be possible.
> 
> We have an offering for homeschoolers, indeed. Bloomy is reimbursable in ~15 states right now through ESA-type scholarships. Great ideas!

**383toast**：
Great idea and execution but the design language seems like general llm-generated tailwind. I think you guys are missing a huge opportunity to make the design reinforce the product positioning.

> **alexsouthmayd**：
> This is interesting, can you say more?

> > **paisawalla**：
> > I spent some time researching how to teach commodity LLMs to pose geometrically correct figures and challenges, for the purpose of teaching middle school trig. I originally wanted exactly what you've described here, using AI to unlock Bloom mastery. There's a decently large surface area I covered before shelving the project. Happy to share my lessons with you

> > > **alexsouthmayd**：
> > > That would be great. Please fill out your information on the below contact form, & I will follow up with you!
> > > 
> > > https://www.bloomylearning.com/#demo

> > **cocoflunchy**：
> > I think 383toast is talking about your landing page design which has very strong AI-generated design vibes (blue-green gradients, rounded rectangles with a colored border on the left...)
> > There are a bunch of skills you can find online to improve on this if you want to keep designing with Claude, and the latest generation of models are better (Fable/GPT5.6).
> > 
> > Check https://github.com/jakubkrehel/skills or https://github.com/emilkowalski/skills (more around animations), maybe https://github.com/leonxlnx/taste-skill (didn't try it)

> > > **alexsouthmayd**：
> > > I'll check them out, thank you for your suggestions!

> > > **docheinestages**：
> > > I got the same vibes. I really wish YCombinator would mentor startups on design. Unfortunately, most of the landing pages in their startup directory look like raw AI designs.

**orsenthil**：
For education, isn't the problem we are trying to solve the one with motivation, values and emotional handling? The tools, play a part, but it is engulfed by the real problem mentioned before. How are you going to deal with it?

> **alexsouthmayd**：
> There are many problems to solve within education! To say there’s only 1 aspect would be a massive disservice to the ~2 decades the average person spends going through a school system. Some studies estimate the average American is at a middle school reading level. That’s one problem (of many) we can aim to solve with something like Bloomy.

> **2arrs2ells**：
> When AI can handle the content, teachers get to focus on motivation, values and emotions.
> 
> I started my career as a teacher and spent > 8 hrs a day lesson planning, delivering content & grading. If I could have handed that off to a great program like Bloomy, I could have built far better relationships & my students would have been so much better off.

> > **bearjaws**：
> > There is already every form of content, hundreds of times over, for almost every K12 topic.
> > 
> > The problem hasn't been content for nearly a decade.

**Onavo**：
Will ChatGPT dream of Bloom's 2 Sigma problem?

https://en.wikipedia.org/wiki/Bloom%27s_2_sigma_problem

> **2arrs2ells**：
> Check out https://www.modernbloom.org/

**rhaynes**：
Congrats on the launch! I'm curious if you're familiar with ED Hirsch's work and if so how you see a "core knowledge" curriculum fitting into AI-enabled tutoring. Your landing page suggests you might be falling into traditional anti-patterns for strengthening reading skills like "finding the main idea" and "close reading" of the text (your ai tutor animation instructs a student to look closely for the answer). These patterns are commonly used in American education and have largely been discredited. They persist due to outdated learning theory taught in American educational schools and are likely responsible for our falling reading scores. I'm bringing this up because my hope is that any ed tech tool regardless of whether it uses AI would start with the right foundational theory.

**Chemio_AI**：
This strongly resonates with what we are building at ChemioAI [1], although we have deliberately started with a narrower audience: college students taking Organic Chemistry I and II.

We are also approaching Bloom’s 2-sigma challenge as the design goal. The aim is not another chatbot that gives away answers, but a patient, Socratic coach operating within a structured system of diagnosis, guided practice, feedback, productive struggle, and independent mastery.

One reason we chose college O-Chem rather than K–12 is precisely the concern raised throughout this thread about screen time and introducing conversational AI too early. Organic Chemistry is a notoriously difficult gateway course taken by older students who are already studying digitally. It gives us a more bounded, age-appropriate environment in which to test whether AI can strengthen effortful learning rather than replace thinking.

Your separation of the tutor from the underlying curriculum and mastery system is especially important. We have reached a similar conclusion: AI can ask better questions, provide patient scaffolding, and adapt how concepts are explained, but it should not independently define the curriculum, determine mastery, or become the source of truth. We therefore keep curriculum, pedagogical policy, mastery decisions, and safety controls in a deterministic orchestration layer outside the model.

Congratulations on the launch. It is encouraging to see others pursuing the same underlying educational ambition from a different starting point.

[1] chemio.ai

**ghm2199**：
First of all congrats on the launch.

I worked at an edtech startup with adaptive learning platforms in previous decades. One thing that is always difficult to surmount was that at the under K12 level were:

1. B2b it was hard to land large contracts(like getting an entire public school district to jump from large publishers like HMH or Wiley) because it turned out that the teachers themselves did not care about adaptivity when they had a thousand other things to worry about. But teachers are not the ones that make the deals. It's the school district board and The reps at large publishing just said we are also adaptive and no one would care about how you differentiated. Teachers and students really aren't the lot you have to convince in a b2b deal do you :)?

2. If you want the b2c route then the customer acquisition cost was way too high because again like to get teachers and students to actually adopt this to help them was really a hard sell, especially when the public school system has teachers that are so overburdened with other stuff.

I see that you mentioned charter schools for your pilot, which are not exactly public schools but I dunno of they come with the same set of challenges, but I wonder  are these above two challenges are Also something you have had to face while scaling your product?

> **JimsonYang**：
> OP this is it
> 
> Almost all the founders who have tried to go into education have come out with similar thoughts.
> 
> Schools are basically legacy companies with low nps products. It might do you better to vertically integrate as hard as that is

> > **alexsouthmayd**：
> > I agree that how we approach the market will be the difference between being successful and failing. At this stage, we’re focused on finding early adopters who have the autonomy to try a different curriculum and already believe mastery learning and AI tutoring are where education is headed. Based on that point, we are validating several B2B & B2C hypotheses over the next few months to truly understand where we should position ourselves in the industry.
> > 
> > As you stated, our primary focus is charter schools, but we’re also working with microschools, homeschool co-ops, and families directly. To make this as accessible as possible for families, we are an approved vendor in over 15 states, which allows homeschool families to use their ESA funds for Bloomy.
> > 
> > Our goal is to work with people who are excited to build this future with us and prove the model from there!

**vessenes**：
Alex, thanks for building this. I imagine it will help many children!

Couple comments on this being 'screen' oriented, which are as you say endemic in schools and terrible.

There's a fair amount of research that paper reading and handling and writing gets significantly higher retention than screen reading. Most especially physically writing notes, but generally comprehension is just higher for paper. Interestingly e-ink is in the middle between screens and paper.

VLMs offer the interesting possibility of 'looking over the shoulder' of students as they work examples and problems by hand through a camera. It's a harder lift, and it's more expensive, but it might find much higher buy-in to think about a combo book / workbook / AI tutor business model, not least because if you talk to almost any parent or teacher they will tell you that they are extremely worried about genz/alpha kids' abilities to focus, read with attention for longer periods of time or handwrite.

Many of the exercises can be evaluated through a VLM pretty much as easily as in a chat window -- more expensive inference, but possibly a much better world.

A middle ground here might be experimenting with something like a remarkable tablet - it's relatively easy to vibe code a responsive eink page right now, and you could do away with the camera side. I guess I'd think of pairing it with a phone app to talk that could hook up to the remarkable.

My pet theory on handwriting notes and why they're so much better than typing or just listening - if not in shorthand, they are too slow to capture lectures word for word, and thus force a first summarization/categorization step, meaning stuff has to literally go in to short term memory then get pulled out and processed; this just *has* to be better than typing in a sort of fast typing haze and trying to read them later. It's also the reason my college notebooks have things like (WTF?? <---) next to notes -- I was trying to synthesize and couldn't in the moment. In addition to all this, I understand brain scans show quite a high percentage of the brain gets involved when drawing/handwriting notes -- you have micro and macro muscle movements plus all the cognitive and visual tasks together.

At any rate, it will be a great service to learners to have a quality AI tutor, and I'd pitch you on looking seriously at e-ink or paper modalities if you want to help students learn even better and faster. The tech is SUUUPER close right now, or even could be there with a little willpower.

> **alexsouthmayd**：
> Thanks for the thoughtful comment. We’ve actually had a few school districts ask about paper workbooks, so this is already on our radar. Right now, students can move at their own pace and use a notebook alongside Bloomy, but we haven’t figured out how much paper or e-ink should be part of the product itself.
> 
> The VLM idea is especially interesting. It could let Bloomy see how a student worked through a problem, not just whether the final answer was right. We’ll definitely take a closer look at this, so I appreciate your recommendation!

> > **vessenes**：
> > I kind of nerd baited myself and have something building for remarkable right now; it's a fork of the riddle diary app for remarkable with spaced repetition and subject tracking. I'm curious how it will feel! drop me a line if you're interested and I'll let you know if I learn anything.

**JimsonYang**：
Tell us about the test scores increased? Did you find similar results on the PSAT?

If your metrics are good, increasing test scores is the thing thats 100% going yo get schools on board

> **alexsouthmayd**：
> We ran a pilot with roughly 150 students in grades 6–8. Students who used Bloomy for one hour per week averaged 1.8x their expected winter-to-spring growth on NWEA MAP.
> 
> Our team was understandably energized by these results, and we plan to run several more pilots this fall to see whether we can produce similar gains across other student populations and assessments, including the PSAT.

**F7F7F7**：
Congrats man. I've been in edtech for the last 15 years.  I was working on something similar (socratic method, 1:1 LLM <-> student, skills based) but joined a company and had to shelve it due to a non-compete.

You've picked one hell of a time to enter the K12 market.   1:1 device backlash, AI tool scrutiny hightening, teacher exhaustion, no recovery in sight for the recent funding cliff.

Your pilot model is the way to go. My favorite tools all grew out of that model.  Stay patient, listen to the early users, encourage them to spread the word. Dont' be above grinding it out at a table at some of the smaller regional educaitonal confreneces.

Sounds like you're already doing this but take IXL head on. They are ripe for the picking.

Good luck!

> **alexsouthmayd**：
> Thank you! It's an interesting time for sure. In the face of all the headwinds, there are also some interesting tailwinds and opportunities:
> 
> -Shrinking budgets forcing reevaluation of longstanding contracts, especially those that provide single-subject or limited grade band solutions
> -A general awareness that, despite the uncertainty around AI, schools need to "figure out this AI thing"
> -School choice driving demand for mastery-based curricula among alternative educational options
> 
> I love a good regional conference.

**joeguilmette**：
I want this exact thing, but I dont want the learning to take place on a screen or device. I want the AI in the background, the tool for the parent and teacher to use to drive the child’s curriculum. This seems trivially easy- printers are cheap.

**ChaitanyaSai**：
Congratulations on the launch!

How do you solve for "meaning?" Is there some implicit expectation that kids arrive with motivation to discover meaning, or some extrinsic rewards?

As AI essentially commoditizes the mechanical aspects of learning, this is the question we find ourselves asking.

I would like to share our journey running a microschool (where our kids go, along with 40 others now) and how we use AI and what we think about its role.

Some useful context, because this really has informed our approach. I am an engineer turned neuroscientist and the co-author of a popular nonfiction book on the mind (and I share this here because the hard effortful self-driven work of crafting this book taught me more about the mind than anything else in my PhD or later). This work, done during the pandemic when learning was coming online, was what pushed us into setting up the school and gave us the courage to work on it from first principles and not rely on any off-the-shelf alternative pedagogy (montessori, waldorf etc). We looked at (and continue to work on) the full-stack of philosophy, pedagogy, process, practice. So the "what should they learn" is also met with "why should they learn this" and also "how should they be learning this"

The *single biggest* learning for us, which we are now able to articulate clearly, is that schools are set up to fail because there is a well-intentioned but misguided focus on *measurement* (what are they learning). This gravitational pull results in a focus on *mechanics* (the most easily measurable thing; long division, periodic tables). This results in a narrow focus on concepts (what David Perkins terms elementitis). Most importantly, what gets left out is meaning. Why should I care about this? With a well-intentioned curriculum and an administration pipette we basically leach out agency and meaning.

So we try to solve for meaning. Our biggest worry with AI is that it focuses entirely on mechanics, with very little meaning. Adults and kids are learning to discount AI-content as automated and inauthentic. We derive meaning from connection. AI can help with the mechanics, but only when meaning has been established. Without this clear-eyed understanding and buy-in we basically have chromebooks all over again, which flattened learning to 2D screens and accomplished nothing (if you look at literacy numeracy scores)

Chatbots are great if you start with meaning and motivation. I already care about the why, so I will socratically find my way to the how and what. But if we do not care about it, which really is the biggest malaise (why should a child who has not yet explored the world or literature they like care about foreshadowing or plot mountains?) Sure, the AI could make it easier, but the kids still need to care?

Wrote about our meaning > motivation > mechanics > measurement revelation and the usual unfortunate inversion here https://blog.comini.in/p/schooling-has-a-meaning-crisis-paradoxically

We need many more people approaching education with ideas and experiments, so thank you and good luck!

> **alexsouthmayd**：
> This is a very thoughtful response! Thank you. I'd love to chat with you further, if you'd like to reach out directly to me (just use the demo form on the site). We are launching Bloomy this fall with Prenda and Apogee microschools (and in discussions with 1 other large microschool network). Your perspective would be valuable.
> 
> Quickly, on meaning: academics are a necessary but insufficient condition for a meaningful school experience. Thus Bloomy is not aiming to solve the meaning question. At the same time, meaning and purpose should (hopefully) create richer outcomes on academics, whether those are pursued using Bloomy or something else.
> 
> Meaning is also subjective. You could ask each of our schools using Bloomy what their meaning is -- I'm sure they'd all have an answer, and each answer would be at least a little different.
> 
> But I'm sure they'd all say they infuse meaning into their school days.
> 
> I'll check out your blog as well.

> > **ChaitanyaSai**：
> > Will reach out, thanks!

**gurjeet**：
I'm quite surprised by the difference in HN users' (quite positive) reaction to this product compared to quite negative reactions to Ello, posted here a few days ago. Is there a substantial difference in teaching methodology, or other factor that makes Ello unpalatable?

https://news.ycombinator.com/item?id=48852199

> **_matthew_**：
> Ello is targeted at 5 year olds whereas this is targeted at a broader range. Also the mechanisms are explained much more clearly here.

**fuddle**：
I think product demo walk through would be very helpful on the home page.

**yizhexu**：
Congradulations to the launch! When will lower grade come out? And can you speak more about how you determine what "skills" are relevant to teach?

**closetkantian**：
So, professional educator here, with fifteen years of high school teaching experience. If the sample passages and questions on the front page accurately reflect what's inside this, I would not let my kids go anywhere near it.

You've chosen to use the most generic AI-generated prose, when you could have licensed or hired writers to craft thoughtful, rich passages. I doubt you've consulted any serious standardized test item writers in the construction of what is essentially a standardized test item-based curriculum. This is the pedagogical equivalent of a Lunchable--mass produced, wrapped in plastic, and basically nutrition-free.

> **alexsouthmayd**：
> Thanks for engaging! Our passages are a mix of public domain passages and in-house authored material which are specced to a long list of requirements. This allows us to create passages spanning a rich variety of characteristics, including genres, contexts, settings, cultures, socioeconomic backgrounds, household family set-ups (e.g., single-parent households, grandparent-led households), etc. We also rigorously vet our content using AI evaluators from Learning Commons, which were created using a golden set of inputs from a panel of experienced educators.
> 
> I also have several years' experience writing standardized test preparatory materials. Ultimately the reading comprehension modules serve the end goal of teaching students discrete skills, which roll up into standards. Those standards are (as you point out) the main focus of standardized, summative tests.
> 
> We encourage students to read real books! We have an AI writing tool that integrates with schools' novel studies curricula to generate a wide variety of prompts so that students can engage in long form writing about the books they are reading.

> > **closetkantian**：
> > Okay, thanks for the extended response. I suppose I would have to look at more questions, but I'm really surprised by what you chose to include on the front page, where you'd presumably want to highlight your best work. That passage strikes me as very obviously AI generated.

> > > **alexsouthmayd**：
> > > Thanks, that's very helpful feedback! We'll improve this.

> > **docheinestages**：
> > I got the same impression looking at your website and demo video. They both came across as generic AI-made content.

> **senordevnyc**：
> *"professional educator here, with fifteen years of high school teaching experience"*
> 
> You do ACT / SAT prep and tutoring, correct? Just wanted to be clear, because the description here sure makes it sound like you're a high school teacher.

> > **closetkantian**：
> > Both. I do classroom teaching as well as SAT / ACT verbal tutoring.

> **windexh8er**：
> 100%
> 
> This looks very poorly thought out by the site alone. The quotes are all concerning as well because all three of them have emdashes. Maybe they're paraphrased, but then those aren't the actual quotes from those educators.
> 
> Parents and teachers who are willing to put middle schoolers in front of screens *more* are doing our future a disservice.  There are real studies (none that I can find on Bloomy) showcasing how this negatively impacts students [0]. I doubt you'll find a correlation that more screen / compute interaction at younger ages improves long term cognition as it's not how kids develop.
> 
> Beyond this every parent should run after a glance at the privacy policy and the sheer number of different backend services required to run this. This is a privacy nightmare, long-term, for kids who have no choice. School districts, and a lot of parents, don't understand any of this.  I don't even see how this abides by laws in some states simply because there are no protections of model training by some of the examples provided in the privacy policy. This does not abide by our state laws requiring a provider to be able to remove student data *permanently* within 90 days. In fact no LLM that doesn't have a "no train" clause abides by this simple requirement and it's unfortunate that districts will get sued over using tools like this in the near future.
> 
> My advice to this is: if you want to build a tutor then target parents. When you try to shove this down the throat of every student in a district you're making a lot of assumptions and impacting many negatively long term. This may be great for disadvantaged areas, but this is not how kids need to learn. They need to learn, explore and make mistakes on their own and not be preconditioned to the easy answer.
> 
> The iPad generation of parenting is about to get a whole lot darker as more and more of these types of companies are taking shots at easy targets, like school districts, with little to no studies behind impacts.
> 
> Finally, very expensive! I ran a simple 5 student cost calculation and it's over $2000 a year for those students. And that cost does not include math which is currently not available which would be another $1400.
> 
> [0] https://jamanetwork.com/journals/jamapediatrics/fullarticle/2722666

> > **alexsouthmayd**：
> > Thanks for engaging! Let me clear up some inaccuracies lest others misunderstand.
> > 
> > First, those are all verbatim quotes from the educators. They were taken directly from letters of reference (which I recently had to compile for a quite intense Technical Due Diligence for a district). They're real school leaders. They're listed plainly on the website. You can look them up online. Whether they used AI in the creation or editing of their letters, I do not know.
> > 
> > The platform has been designed to minimize PII required. We have a very standard third-party vendor stack. Basically just OpenAI and Anthropic as frontier labs for the models, but neither is permitted to train on our data (we have Zero Data Retention agreements with those organizations). The other vendors are standard for operating the app (e.g., Supabase, Vercel). Nothing crazy here.
> > 
> > Not only can users request deletion of their data -- it's standard for any user who cancels their relationship, within 30 days. You can read it right in our privacy policy.

> > > **windexh8er**：
> > > > First, those are all verbatim quotes from the educators. They were taken directly from letters of reference (which I recently had to compile for a quite intense Technical Due Diligence for a district). They're real school leaders. They're listed plainly on the website. You can look them up online. Whether they used AI in the creation or editing of their letters, I do not know.
> > > 
> > > This feels off to me as they don't feel like real quotes given they're all very similar.
> > > 
> > > > The platform has been designed to minimize PII required. We have a very standard third-party vendor stack. Basically just OpenAI and Anthropic as frontier labs for the models, but neither is permitted to train on our data (we have Zero Data Retention agreements with those organizations). The other vendors are standard for operating the app (e.g., Supabase, Vercel). Nothing crazy here.
> > > 
> > > There are many sections in your "Privacy Snaphot" section where you don't explicitly say there is data retention.  This to me feels like a convenient workaround to the other training callouts.  You listed 4 vendors above yet none of that stack is called out transparently in any of your publicly facing documentation.  Why?  Do kids educations not deserve for parents and staff to understand where the data actually resides and how it's processed?  That's the thing with technology in schools - there's always a loophole way for any company to collect and store data on kids.  Their behavior, their persona, their intentions, their thoughts...  We all know how egregiously Flock is being used *against* taxpayers.  I suspect these types of learning platforms will also be used *against* kids in the near future and startups like Bloomy don't actually have the improvement of kids as their goal - the goal is $$$.  And when you sell off Bloomy to Google or Meta, then what?  You state no long term goals and you make no commitments to student, staff or parents.  Those districts who trust you have no clue in how they're handing data over to you.
> > > 
> > > > Not only can users request deletion of their data -- it's standard for any user who cancels their relationship, within 30 days. You can read it right in our privacy policy.
> > > 
> > > I've read a lot of ToS and Privacy policy for companies like this.  They all fall apart when you ask for proof.  So... How do you prove the data is gone?  I'm a parent who requests my kids account do be deleted along with the data.  How do you showcase all of this?  I know that, from experience, nobody puts time or effort into this because it's not a money maker.  But, yes, I can read your policy.  Your policy actually says nothing to the extent of giving me any sort of confidence in how you handle student data. By all means please explain.
> > > 
> > > Finally, you don't address (at all) the impact study I referenced.  So where is your data coming from?  Any long term studies?  Or are these metrics one offs?  You don't share # of students, nothing.  I don't understand how you build trust with kids data that is very proximal to AI systems that have not been proven safe with respect to young children.  What is Bloomy's response?
> > > 
> > > Edit:
> > > I think it would be rather interesting for Bloomy to provide free accounts to some red-teamers to really understand if what you claim is true with respect to your pipeline of protections.  I have zero confidence an educator building something like this has actually thought through data protection, model protection or any of the base level considerations you need when building a tool that handles user data, let alone data of minors.

**makeyouragent**：
One metric I would add is mastery under decreasing assistance. A student who answers correctly after three increasingly specific hints has shown something useful, but it is not the same evidence as solving a fresh version unaided. If both outcomes update the skill score equally, the personalized path can advance the student too early.

For each attempt, I would keep the skill, item variant, number and specificity of hints, revisions, elapsed time, and whether the final reasoning came from the student. Advancement could require an unaided success on a new item plus a delayed check later in the session or on another day. The tutor's own explanation should never count as evidence that the learner mastered the step it just supplied.

This also gives teachers and families a more useful explanation than a single mastery percentage. “Can solve independently, but does not retain it after a day” and “can solve with one conceptual hint” point to different next lessons. That distinction seems especially important when the chat interface is both teaching the skill and measuring it.

> **alexsouthmayd**：
> Great points! Agreed on the distinctions. With enough data we should be able to identify lots of cool things about mastery.

**tmpz22**：
Move fast and break things.

**williamcotton**：
Article Title: Ed tech is profitable. It is also mostly useless

https://www.economist.com/united-states/2026/01/22/ed-tech-is-profitable-it-is-also-mostly-useless

**timostrating**：
Hey first of all, Congratulations on the launch. I'm a teacher at a Dutch applied university where we use mastery learning to teach students software development, the code for our learning system is open source so feel free to take a look [1].

I personally always followed traditional schooling but programs like flip the classroom or https://www.khanacademy.org/ really helped me and I now also see the same value in my own teaching and your work so thanks for working on this.

At my program we have experimented a lot with teacher bots, AI grading, using AI to generate assignments and other forms of AI but in the end we always came back to 1on1 feedback sessions and ditched the AI to be just an optional tool. In a teacher feedback session a teacher would open the work of the student and grade the work based on how much of the objective was reached. In our experience students will find the tools to not do there homework and that is more than fine as long as they understand what they are doing. We eventually settled on 1 or 2 day exams without AI. Screen recording as proof. Where you get graded on the same objectives and can use any trick you have learned. Assignments typically take 1 day to compleet. Assignments need to be redone if a student scores less than 80%. On the exam often 55% is a passing grade.

So some of the things that pointed out to me where: 90% correct sounds really high. A lot of AI access sounds like a lot of trouble shooting to find the right amount and per student this amount may be different. We for example see that some students do better with AI and others learn less. Students may also ask AI outside of bloomy and I could not find how that is precisely handled. Lastly the course sounds very independent. Are there any group projects or assignments that can be done together. We are for example currently exploring adding tags to assignments to indicate you could pair a programming assignment or that you could pair with AI.

[1]: https://sd42.nl/

> **alexsouthmayd**：
> These are really thoughtful points. Thanks for sharing them. I'd love to check out your code.
> 
> The percentage mastery threshold on Summit may indeed be quite high, but the Summit also comes after the student has proven they are ready for the it by satisfying the BKT threshold on Climb. Still, though, it is worth testing out mastery percentage thresholds to see if lowering it makes any positive difference (e.g., maybe we are not letting students progress fast enough because the bar for quasi-perfection is so high).
> 
> On students asking AI outside of Bloomy: that is always likely to be a challenge. One way we mitigate this is by protecting the clipboard so students cannot copy/paste in or out of the platform. This is especially helpful in our Writing Studio tool, where students write long form essays (although clipboard protection is optional and can be disabled by the teacher/parent if they wish -- e.g., if the student typically drafts in Google Docs or Word and wants to easily paste).

**mindsolutions**：
The focus on mastery learning via adaptive curriculum is a much-needed approach for K-12, especially since the biggest bottleneck in education is often the one-size-fits-all pace. I am curious how you plan to handle the feedback loop between the AI tutor and the student's emotional engagement with the harder subjects. I am working on something similar for adult personal growth at https://mindsolutions.ai/r/hn , where we use personality assessments to tailor the learning experience, but managing the pedagogical side for younger learners is a much more complex challenge.

**Dramatize**：
My son gets too distracted by any screen (we have had to implement a total screen ban), so screen-based learning doesn't work after a few days. Is there a way to create an analogue paper version? ie with printer and scanner.

