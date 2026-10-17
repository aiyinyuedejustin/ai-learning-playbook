# HN：Ask HN，学编程时用 LLM 有益还是有害

- 链接：https://news.ycombinator.com/item?id=43953226
- 作者：dominicq
- 获取方式：Hacker News 帖子与评论全文

---

## Ask HN: Are LLMs useful or harmful when learning to program?（dominicq，11 分）

（讨论共收录 20 条评论，缩进表示回复层级）

Is there any consensus on whether it makes you a good programmer to study using LLMs? Or should you perhaps do it the old fashioned way, by reading manuals and banging your head against the problem?

**calrain**：
I think they are useful as long as you use them the right way.

Dig into problems, try to understand why it was solved a specific way, ask what are the con's of doing it another way, and let it know you are a learning and want to understand more of the fundamentals.

LLMs are just a tool, so try and use them to help you learn the fundamentals of the language.

It could also be argued that using StackOverflow to solve a problem doesn't help you understand a problem, and equally, just asking an LLM for answers doesn't help you understand the language.

**benoau**：
I have seen people learn programming incrementally for decades by googling a problem and finding some code and trying to adapt it to their requirements.  LLMs certainly make this more efficient.

**flessner**：
Absolute beginners usually don't even know how to ask proper questions. LLMs can help you in that regard... they'll answer your questions and provide you an answer no matter how trivial.

However, over reliance on it - like with all technologies - doesn't end well.

**Zambyte**：
In my opinion, the most useful way to use LLMs for learning (anything, but including programming) is to have it explain things in terms of what you are familiar with. You can give the model context of things you know are relevant that you do understand (or at least have a functional understanding of), and ask it to explain things that you don't yet understand, building on what you know. For example, asking things like "I am familiar with object encapsulation and mutating state over time in object oriented programming. If pure functional programming does not allow for mutation, how to you manage the state of objects over time?" or "Help me learn about Kubernetes. I am familiar with using docker, docker compose, and virtual machines for deploying my applications."

The problem is when you're learning something completely foreign like learning to program in your first language, you don't really have enough context to ask meaningful questions. In that case, it is simply better to do things like read manuals and bang your head against the problem.

**codingdave**：
If you read what they produce, learn to debug it, and make it an active learning experience, then yes, they are useful. If you just copy/paste code and errors back and forth, then no, they are harmful.

No matter what purpose you are trying to achieve, the success of a tool comes from applying the correct tool, to the correct problem, in the correct way. LLMs are kinda cool that they are flexible enough to be a viable tool for many things, but those other two criteria are up to you.

**aristofun**：
It depends on how you use it a lot.

The more you rely on it as a source of truth and as your mentor or executor of your hi level intentions - the more harmful. Obviously.

When you’re beginner you can’t possibly know good vs bad, right vs wrong decisions.

Whatever mental model and thinking flaws you start with is going to be amplified. And hidden behind false sense of progress (the more you rely on llm the more you trust it with whatever terrible code it spits out).

If you treat and use it just as a sophisticated algorithm to save some time on typing, or exposing alternatives, edge cases - then it’s very useful in speeding up your learning.

**fzwang**：
From my personal experiences, working with small engineering teams and running an comp sci education program[1].

TL;DR: There are some benefits, but mostly not worth it or actively harmful for students/junior engineers.

1) Students using LLMs to code or getting answers generally learn much slower than those who do it old fashioned way (we call it "natty coding"). A very important of the learning experience is the effort to grok the problem/concept in your own mind, and finding resources to support/challenge your own thinking. Certainly an answer from a chatbot can be one of those resources, but empirically students tend to just accept the "quickest" answer and move on (bad habbit from schooling). But eventually it hurts them down the road, since their "fuzzy" understanding compounds over time. It's similar to the old copy-from-StackOverflow phenomenon, but on steroids. If the students are using these new tools as the new search, then they still need to learn to read from primary sources (ie. the code or at least the docs).

2) I think one of the problems right now is that we're very used to measure learning via productivity. Ie. the ability of a student to produce a thing is a measurement of their learning. The new generation of LLM assistants breaks this model of assessment. And I think a lot of students feel the need to get on the bandwagon because they produce very immediate benefits (like doing better on homework) while incurring long-term costs. What we're trying to do is to actually teach them about learning and education first, so they at least understand the tradeoffs they are making using these new AI tools.

3) Where we've found better uses for these new tools are in situations where the student/engineer understand that it's an adversarial relationship. Ie. there's a 20% chance of bullshit. This positioning puts the accountability in the human operators (can't say the AI "told me so") and also helps them train their critical analysis skills. But it's not how most tools are positioned/designed from a product perspective.

Overall, we've mostly prohibited junior staff/students from using AI coding tools, and they need a sort of "permit" to use it in specific situations. They all have to disclose if they're using AI assistants. There are less restrictions on senior/more experienced engineers, but most of them are using LLMs less due to the uncertainties and complexities introduced. The "fuzzy understanding" problem seems to affect senior folks to a lesser degree, but it's still there and compounds over time.

Personally, I've seen myself be more mindful of the effects of automation from these experiences. So much so that I've turned off things like auto-correct, spellcheck, etc. And it seems like the passing of the torch from senior to junior folks is really strained. I'm not sure how it'll play out. A senior engineer who can properly architect things objectively have less use for junior folks, from a productivity perspective, because they can prompt LLMs to do the manual code generation. Meanwhile, junior folks all have high powered footgun which can slow down their learning. So one is pulling up the ladder behind them, while the other is shooting their feet.

[1] https://www.divepod.to

**cylinderthought**：
they are really good for learning quick. but don't fall in the trap of copypasting, take your time, don't rush and ask repeatedly to the ai what the hell this does until you understand it and you can write it by yourself completely.

**wafadaar**：
Like any tool, really depends on how you approach using them.

Giving it a problem statement and just blindly asking it for an answer will always yield the worst result, but I find this is often our first instinct.

Working with it to solve the problem in a "step-by-step" manner obviously yields a much better result as you tend to understand how it got to the answer.

I look at it as similar to rote-memorization vs. learning/understanding.

Most often I now use it to help find the "right question" for me to ask when starting with a new topic or domain or synthesize docs that were difficult for me to understand into simpler or more digestible terms.

**alecsm**：
¿Is a calculator useful or harmful when learning maths?

**mattbrewsbytes**：
Someone new to woodworking might not realize a tape measure has a couple modes of operation and if you use it wrong can be off by 1/8". So AI is like a tape measure that could be wrong 50% of the time, depending. You'll need to ask AI to explain itself and validate its own answers. Then if you're new to programming you should independently also be learning things.

**CM30**：
They can be useful, though you have to use them carefully.

For instance, one of the best ways I've found to learn a new language or framework or technique is to find a working example of something, then take it apart piece by piece to see how it all fits together. LLMs can work really well here. They can give you a super basic example of how something works, as well as an explanation you can use as a jumping off point for further research.

And those basic examples can be surprisingly hard to find elsewhere. A lot of open source systems are designed for people with no programming knowledge whatsoever, and in a way that they can handle 52 million possible use cases with all the caveats that brings along. So when you're trying to learn from them, you end up having to untangle hundreds of conditions and feature flags and config options and other things designed for use cases you simply don't have. LLMs can provide a simple, customised example that avoids that.

That said, you have to be willing to try things yourself, and put in the effort needed to figure out why the code the LLM returned does what it does, and how it works on a technical level. If you're just throwing problems at the tool and letting them do all the work (like many vibe coders now), you're not really learning anything.

**huevosabio**：
LLMs are fantastic for learning anything.

But the learning happens when you bang your head. It has to hurt the same way going to the gym hurts. If it doesn't, you're not training and probably you're not really learning.

**DantesKite**：
Yes. It's basically a custom StackOverflow human available to you at all hours of the day.

**babyent**：
LLMs will give you what you ask.

Case in point I asked LLM to generate some code for me. It didn’t use generics (a language feature) and gave me some shit code.

I had to prompt it several more times to give me generic code with better typings.

I think it would be helpful for a total nooblet to get a hang of the basics but I think if they rely on the LLM too much beyond a certain point they will face diminishing returns.

Think about it. There is so much knowledge in the world. Anyone can do anything to a satisfactory degree pretty quickly. But to really understand something takes experience and self-discovery. And I’m not speaking about master. Just expertise.

**TowerTall**：
i would say depends. If you use it for *writing* the code, I will say yes. If you instead use it to discus how to aproach the problem I would say "no/not sure". One of the best ways to become a good developer is to learn from the code we write. On the other hand we also often need someone to speak with about the code we write or plan on writing. I think the best cause of action is that you write the code and then use LLM as a reviewer and someone to talk about writing code with.

**mkbkn**：
Don't use LLM while you're learning. Don't outsource your thinking to a third party. Period.

> **gus_massa**：
> I agree. This is similar to our recommendation while learning math. You *must* do some[1] calculations and problem solving by hand alone, with some minimal help when you are stuck. And only then, use coworkers, wolfram alpha or AI to handle part of the job.
> 
> [1] Both extremes are bad. Two integrals are too few. A million are too many.

**hiAndrewQuinn**：
It is undeniably useful, and people who are denying this have no recollection of what it was like to learn to program for the first time. Anything that helps you surmount the brick wall difficulty curve of that first programming language is a godsend, and I can tell you this from having seen real motivated undergraduates in action during their CS degrees.

**muzani**：
My rule of thumb: If the LLM is more junior than you, then go ahead and let it full autopilot. Check the results like you would check the result from a junior.

If the LLM is more senior than you, learn from it – treat it like a tutor and ask a lot of questions. Things like why we'd use MVP architecture instead of MVC. Ask until you have no dumb questions left. The hardest part of RTFM is often knowing which part of the manual to read and going through the what before the why. Ask the LLM to explain, then verify by searching it yourself.

LLMs will often pull the wrong language if you're not careful. Like contains() may function differently in different languages. This is where it's vital to RTFM.

