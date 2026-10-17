# How to Use AI to Learn Coding SO fast it feels impossible

- URL: https://www.youtube.com/watch?v=JDIXhJX6kdE
- Channel: Manware
- Published: 2026-09-06
- Duration: 05:28
- Transcript: 平台自动字幕 / auto captions, lang=en-orig
- Cite as: [mm:ss](timestamp link) — each line below starts with one

## Chapters

- [00:00](https://www.youtube.com/watch?v=JDIXhJX6kdE&t=0s) Peak Intro
- [00:29](https://www.youtube.com/watch?v=JDIXhJX6kdE&t=29s) First attempts...
- [01:43](https://www.youtube.com/watch?v=JDIXhJX6kdE&t=103s) Awakening
- [02:12](https://www.youtube.com/watch?v=JDIXhJX6kdE&t=132s) Example Agents (Tutor Mode)
- [02:51](https://www.youtube.com/watch?v=JDIXhJX6kdE&t=171s) Examiner Mode
- [03:08](https://www.youtube.com/watch?v=JDIXhJX6kdE&t=188s) Review Mode
- [03:56](https://www.youtube.com/watch?v=JDIXhJX6kdE&t=236s) How to use this effectively
- [04:40](https://www.youtube.com/watch?v=JDIXhJX6kdE&t=280s) Video Explainers

## Transcript

[00:00](https://www.youtube.com/watch?v=JDIXhJX6kdE&t=0s) When I was a kid, I used to think I would be so much smarter if only I had a brain chip that answers any question I had. Fast forward to 2026, it's actually here and it made me even dumber than I was before. So, I went down the rabbit hole of how to actually learn programming with AI and ended up creating an entire AI workflow toolkit designed to make me reason more and reduce unproductive struggle so I can learn programming faster and deeper at the same time. There's also one hidden gem I found online that I'll share at the end of this video. by disabling

[00:30](https://www.youtube.com/watch?v=JDIXhJX6kdE&t=30s) inline suggestions and using only ask mode instead of agent mode because they are the biggest sources of laziness for me. Next, I created a markdown file that explicitly instructs the AI agent to act like a teacher, encourage me to think, give me hints, and other instructions I found online. This forces the agent into tutoring mode rather than a code wrapping machine. But I soon realized just saying give me hints is not enough. Like, yeah, bro, that's not a hint. To fix this, I came up with a hint ladder. Now, whenever I ask AI for a hint, it starts with level zero where it asks me

[01:01](https://www.youtube.com/watch?v=JDIXhJX6kdE&t=61s) questions and encourages me to form a hypothesis before proceeding on to level one where it only directs me to a concept, a file, or a function to investigate. On level two, it explains a relevant concept. On level three, it tells me an approach but not the strategy and so on till level six where it just gives up and hands me the code. This way I can also track the level of assistance I needed for a problem, but more on that in a bit. But now I had a new problem. I had to copy-paste the same prompt repeatedly and it became very annoying. in another use case where I asked AI to explain a code snippet to

[01:32](https://www.youtube.com/watch?v=JDIXhJX6kdE&t=92s) me, it actually explained the code snippet to me, you dumbass. You're supposed to make me think and figure it out myself. So, I came up with this prompt, but again I had to copy-paste it repeatedly. And that's when I stepped out of my chair, said nah, I'd win, and built an AI learning toolkit with predefined agents and skills, which is just a fancy way of saying markdown files. But now I can just type {slash} hint with the problem I'm stuck at and the hint ladder begins. I can just say slash read with the code snippet I found online. The AI will lead me to discover

[02:03](https://www.youtube.com/watch?v=JDIXhJX6kdE&t=123s) what every single token is doing here. This workflow works in three modes: tutor, examiner, and reviewer, and dynamically switches between them. Let's go over some examples. Tutor mode. Now, when I'm building a project by myself and encounter a bug that I'm not able to fix, I can use the debug command and instead of AI telling me how to fix it, it asks me question to solve it myself. Like what I expected, what actually happened, what the error log said, how to find more clues, reproduce it, and trace it to the root cause. But wait, man, wait. Doesn't this make me slower? Going slower here on purpose is exactly

[02:34](https://www.youtube.com/watch?v=JDIXhJX6kdE&t=154s) how you get there faster. This thinking pattern saves me time by reducing unnecessary effort spent thinking elsewhere and increases the time I'm thinking in the correct direction, where the actual learning happens. And over time, this will reprogram my brain to habitually think like a senior engineer. Examiner mode. Now, when I'm planning and designing a new project or a new feature, I can use the R command which challenges my current design and takes me from a vague idea to solid constraints on requirements, states, interfaces, failure modes, etc., which are the exact type of problems you want

[03:05](https://www.youtube.com/watch?v=JDIXhJX6kdE&t=185s) to excel at in this era of AI coding. Review mode. And another such skill set is code review. Now, you know it's boring when you finally finish writing code, it's running, and you just want to move on to the next step instead of optimizing it. But you are still locked in your own way of thinking. By using this command, AI finds the weakest parts of you, labels issues by severity, and asks you discovery questions instead of rewriting your code. This is how Goku evolves as well. A very different kind of feature I've included is this folder. I receive the concepts I learned, mistakes I made, and questions left

[03:36](https://www.youtube.com/watch?v=JDIXhJX6kdE&t=216s) unanswered at the end of each coding session. You know, the act of recalling while you're writing this stuff down hard codes these concepts in your hippocampus. And then later I can invoke the retrieve command to quickly warm up and reinforce what I learned in the the session. If you remember this video, yes, I actually took that and many other habits from there into this workflow. There are 12 commands in total, but if you don't know which one to call, you can directly just use the loan command and AI will automatically fetch the right prompt for you under the hood. There's still one massive caveat in this

[04:07](https://www.youtube.com/watch?v=JDIXhJX6kdE&t=247s) workflow. Since this is still AI, I get very comfortable using it. So, ideally, we want to use it in a Pomodoro style. Like 30 minutes building and learning yourself and then a 5-minute AI session. A very practical learning system you can adopt right now is this one. I currently made it compatible with Copilot, Cloud Code, Cursor, Open Code. And fun fact, my agent actually refused to make this for anti-gravity and even roasted it. But I eventually included it as well because I know most of you are still using it. And the price for using this product is only

[04:39](https://www.youtube.com/watch?v=JDIXhJX6kdE&t=279s) one subscribe. Okay, so remember the hidden gem I mentioned earlier? So, currently, we have this tiny text box that can magically answer anything you ask back in plain text. But what if it answered with a video instead? Well, actually, now you can with Scrimba's Explain plugin for ChatGPT, which is totally sponsored for completely free right now. You ask it anything and it replies with a full video explanation with fancy visuals as fast as a ChatGPT response. Wait, even my job is in danger now. It also quizzes you about what you just learned. And you can even create a

[05:09](https://www.youtube.com/watch?v=JDIXhJX6kdE&t=309s) playlist of bigger explainers. Links in the description and thanks to Scrimba for making this video possible. And thanks to you for watching. I'm there.
