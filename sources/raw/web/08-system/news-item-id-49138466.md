# HN：Ask HN，你们怎么用 AI 学习

- 链接：https://news.ycombinator.com/item?id=49138466
- 作者：mfalcon
- 获取方式：Hacker News 帖子与评论全文

---

## Ask HN: How are you using AI to learn?（mfalcon，9 分）

（讨论共收录 23 条评论，缩进表示回复层级）

It's time to start learning advanced topics again and I thought it'd be at least interesting to take advantage of LLM's to help me learn better or faster.

I've read here that some of you are using "socratic skills" where you give the LLM some content and then you get a series of questions in order to learn but I don't think it's the only approach to this.

I'll start tackling the "Attention is all you need" paper and then I want to go deeper.

What's your approach?

**idontwantthis**：
I’ve had claude code create a practice project for me to learn SQL. I had it create 12 projects of graded difficulty with automated tests. It was super helpful. I had to revise the lessons as I was completing them, but overall it worked fantastically.

> **mfalcon**：
> SQL seems to be a great fit because of how easy is to verify the output.

**7nolikov**：
AI is effective when combined with traditional approaches. I usually ask users to provide existing trusted educational resources with user reviews, create a roadmap for learning skills, and then provide examples for specific cases.
Even when I am taking a course on learning portal, I often ask AI about alternatives

> **mfalcon**：
> Are you building something in this space? Or are you giving the resources directly to a llm chat interface along with some prompt?

> > **7nolikov**：
> > No, I am requesting resources for my learning. E.g., I want to learn a new skill - compare several alternatives by pricing and effectiveness. If I already have some candidates, I can request llm to search for reviews

**acron0**：
I had Claude research and synthesize as much as it could from published curriculums and then design its own undergrad Philosophy degree. Then I asked it to split it into lessons, and I am consuming these lessons, delivered dialogically, at the rate of about 1 a week at the moment. It's fun, it's engaging, and I really feel like I am learning and making progress. Could all be an illusion.

> **mfalcon**：
> Do you trust everything you read or how do you verify that the LLM is not hallucinating and giving you erroneus content?

> > **paulcole**：
> > How do you verify that books and websites and videos are not giving you erroneous content?
> > 
> > You trust some and distrust others at face value based on prior experience and what you want to believe. Sometimes you check after the fact and sometimes you don’t.
> > 
> > It’s the same exact thing with LLMs.

**codingdave**：
I absolutely don't learn content from AI. LLMs still are at the point where they sound plausible to non-experts, but are just wrong about things you know well. So if you feel you are learning successfully with an LLM teacher, guess which side of that line you are on?

That being said, they absolutely can spin out a topic list and help you find gaps in your knowledge in order to create a self-study plan. As a over-engineered librarian, they are terrific.

**while_true_**：
AI, when used in an organized and structured way, is excellent for learning a language. For example:

1. Ask AI for the 10 most commonly used verbs in ordinary daily speech in language X.

2. Prompt AI: generate 4 short sentences for each of the 10 verbs at the A1 (beginner) level.  Provide the sentences in .csv format compatible with the Anki flash card program.

3. Import .csv into Anki.  Study your 40 cards.

As you advance you can do much more like having conversations with AI avatars, transcribing videos, translating text, generating audio clips, and so on.

Dr Taylor Jones, a PhD linguist, goes into greater detail here: https://youtu.be/xQXiSGDXknA?

> **rsanek**：
> If you want to skip the clunky csv step, you can utilize https://github.com/jasperket/clanki and push directly from AI to Anki.

> **nicbou**：
> You can also use it to write and see the corrected version of your sentences. This got me to practice a lot more.

**brudgers**：
Googling.

Watching Youtube.

Same as before.

**sieve**：
I often produce have LLMs extract the text from a book scan and then translate it into English or some other language I know. Then I load it into my interlinear reader for side-by-side reading. Convenient when you are starting out with a language

**jamesdwilson**：
I told my system prompt to randomly inject contextually appropriate words and idioms of languages i want to learn into its responses.

**NishanStepak**：
I am building a vibe coding project.  As part of the project, I am reading books on each step of the process.  This means first reading on how artificial intelligence works, then reading about how to vibe code, then about how prompting works, how context engineering works, how AI project management works, how basic machine language works.  Then project advances, I am learning about how to market SAAS, learning how SEO and GEO work.  Before this I took classes from the Verizon Skill Forward program which is free to anyone older than 17 in the United States, https://www.verizon.com/about/responsibility/human-prosperity/workforce-development  It covers many classes and certifications in EdX which is an online training program.  I am using AI to apply what I am reading.  Things like joining Github, and joining other places related to what I am reading or taking classes on.  Through my library I also have access to LinkedIn training, so I am applying what I am learning through AI.  This includes things like using AI for basic investing and other things.  You can test anything you learn about AI with AI.  There are a ton of new books on AI.  I like the ones from O'Reilly Media, and the For Dummies books by Wiley give just enough content to learn a little bit.

**gokuljs**：
Just take a tough project, an ambitious one. Then do system design first. Use AI and you, and figure out failure modes, all that where it can fail. Then start building piece by piece and start reading that code and publish thats it

**sagunbuilds**：
I learned by building instead of studying. I'm a mechanical engineer working in finance, zero software background, and over the last couple of months I shipped a browser extension with an AI assistant writing the code while I made the product decisions.

The surprise was a) it has been much harder than I expected b) I ended up learning a lot. I thought it would may be pick up a bit of programming. But it was mostly everything around programming: how OAuth works, why my sign in kept expiring after an hour (a code deletion took out the token refresh route with it), how Stripe webhooks fail silently, why emails land in the Promotions tab, how Google decides what to crawl. Each broken thing forced me to understand a system I didn't know existed the week before. Learning to work with the AI model has also been a huge lesson on its own:)

**npras1**：
Nothing has changed wrt learning new things since LLM. We are the ones who still have to do the learning.

And the speed of learning is still limited by the individual's constraints: ability to focus for an extended time and chance to apply the new knowledge so the learning is reinforced.

Even before LLM's there was no shortage of knowledge and also the organization of them.

So I resort to same method I've been using ever since: reading books, writing code by hand, and sometimes, writing a blog post so I could refer things later.

Actually, I've added a further constraint on myself once I realised the above: to never learn anything from videos. Youtube is simply too distracting. Books are great, and coding by hand the stuff I'm trying to learn... I feel I need that experience to imprint things in my brain.

**nicbou**：
I use it like a pokedex. Yesterday I was using it to know if I see swifts or swallows in the evening, and learned a bit more about them. For low-stakes questions that blogs cover well, it’s great. The stakes are low and it gives me a better starting point than shallow content.

It’s also good as a fuzzy dictionary/thesaurus/expression finder. It’s good for refining my writing skills.

I use it to learn German by writing the texts myself then comparing it with the AI’s version. It highlights subtle mistakes I make.

**taosx**：
I really want an AI tutor (ai learning harness) that I can give it a topic, it can synthesize information from sources, gauge my level, create lessons that I can read, give me exercises, track repetition optimal timings and track my progress.

I've noticed that for me it's much faster to learn by doing exercises targeting the exact thing you need than just trying to apply that to a much bigger chunk of work directly, especially for someone that's a bit of a failing perfectionist.

I was just looking for that and I saw https://github.com/THU-MAIC/OpenMAIC. I haven't tried it as I'm trying a few small experiments to see if I can create a curriculum for a framework with no docs.

The first naive one failed for multiple reasons but mostly because many guardrails are needed and we need a proper process that tracks too many things.

> **comment0r**：
> Maybe the new company from Andrew Ng is for you, though it doesn’t operate publicly yet: https://learnvector.ai/

**watchdog408**：
At work, I have to maintain legacy systems, and that’s taught me that the best way to understand something you’re unfamiliar with is to use diagrams. Specifically, I have a Claude license and use Draw.io skills to have the AI analyze a project’s code and/or documents and create high- and low-level diagrams so I can understand everything. From there, I ask the AI to integrate them into an MD with all the necessary explanations to make it easier for me.

