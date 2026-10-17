# jnalewajk：AI as a learning coach

- 链接：https://jnalewajk.me/en/blog/ai-as-a-learning-coach/
- 作者：Jakub Nalewajk
- 获取方式：网页正文（trafilatura 提取）

---

# How I set up Claude Code as a backend learning coach

Jakub Nalewajk · March 26, 2026

## On this page

[Back to blog](/en/blog/)

For months I used AI to learn code. I’d read the generated solutions, feel like I understood them, and move on. Then I sat down to build something without AI and realized I couldn’t write basic things I supposedly “knew” for weeks.

## The illusion of learning

I came across a video by Marcin Czarkowski about the illusion of learning and it hit close. He described exactly what I’d been doing - you read AI-generated code, you feel like you get it, but your brain processes it on the surface. There’s no struggle, so there’s no effort. And without effort, nothing sticks.

Recognizing the pattern was one thing. Admitting that this had been my learning for months was harder. I wrote about a related problem in my post about [refactoring AI code](/en/blog/refactoring-ai-code/) - there, the issue was delegating too much to agents without understanding the output. Here, the problem went deeper. The AI wasn’t writing bad code. I just wasn’t learning anything from it, even though I was convinced I was.

## A system, not willpower

I could have told myself “from now on I write everything myself” and lasted maybe a week. Instead, I built a system that doesn’t give me a way out. I’m going through NestJS and I configured Claude Code as a coach that refuses to write code for me.

What it can do:

- Explain concepts when I ask
- Review code I wrote
- Quiz me on material
- Generate Anki flashcards from sessions

What it can’t do:

- Write implementation code
- Give me ready solutions
- Hint at how to implement something (unless I’m stuck for over 15 minutes)

Sounds simple. In practice, it’s annoying. You’re stuck on something, you know the AI has the answer, and it won’t give it to you. It asks “what are your options?”, “what does the docs say?”, “why would you pick that approach?”. You want a solution, you get questions.

## What a session looks like

Every session starts with a quiz on material from previous sessions. Not the last one - from 3-5 sessions back. The idea is to let the brain forget a little so it has to work harder to recall. That’s when things actually stick.

Then I plan what I’m building. Not “start coding” - first an architecture discussion. The coach asks why this structure, what dependencies, what if requirements change. Only when I have a plan do I write code.

During coding, the coach throws random questions from past topics. “What’s the difference between middleware and a guard in NestJS?” - 15 seconds to answer, then back to code. It’s a bit distracting, but that’s the point - old stuff shouldn’t just fade away.

At the end of every session, two mandatory parts. First - I have to explain what I built and why. Not “I made a CRUD” but in detail - what decisions I made, why a repository pattern instead of direct database access, where the pattern comes from. The coach scores it 1-5. Second - an interview-style question. One question, I answer like I’m in a job interview, I get a score and feedback.

The session generates Anki flashcards. Not just standard question-answer pairs, but also cards that connect concepts - “How does Dependency Injection in NestJS relate to the Dependency Inversion Principle from SOLID?”. 5-10 minutes of daily review outside sessions.

## Tracking between sessions

The system logs what I struggled with. If I score 2/5 on database transactions during a quiz, that topic comes back. Not as “let’s review transactions” - more like I’ll get a task that requires using transactions in the context of something new. Topics I stumble on don’t disappear until I actually get them.

Every session ends with a log - what I did, how it went, where I got stuck, what’s next. The coach plans the next session based on these logs, not a rigid curriculum.

## What came out of it

Two weeks in, too early for any hard conclusions. But I built two full NestJS modules from scratch. Database, relations, error handling, repository pattern, DTOs. Things I previously “knew” from reading AI-generated code, I can now actually write and - more importantly - explain every line.

The difference is this: before, I’d open generated code and think “yeah, I get it”. Now I write the code myself and I know exactly where I don’t understand, because I get stuck there. Not understanding stopped being invisible.

## Not quitting AI

This isn’t about ditching AI. It’s the opposite. When I actually understand what I’m reading, I get way more out of AI than I ever did before. I can judge whether generated code makes sense. I can fix it. I can ask a good question instead of accepting the first answer.

The whole system - prompts, skills, session logs, roadmap - is open on [GitHub](https://github.com/jaqubowsky/iron-log). If you’re trying something similar or have ideas on how to improve it, let me know.
