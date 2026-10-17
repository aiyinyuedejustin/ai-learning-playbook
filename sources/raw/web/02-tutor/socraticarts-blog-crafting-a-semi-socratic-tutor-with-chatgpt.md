# Crafting a Semi-Socratic Tutor with ChatGPT

- 链接：https://www.socraticarts.com/blog/crafting-a-semi-socratic-tutor-with-chatgpt
- 作者：Breanne Grover
- 获取方式：网页正文（trafilatura 提取）

---

# Crafting a Semi-Socratic Tutor with ChatGPT

Given our company's name, it seems appropriate to begin by discussing our stance on the Socratic Method. This method is an educational approach that involves asking probing questions and engaging in dialogue to encourage critical thinking and independent exploration of complex ideas, rather than simply providing answers. The goal is fostering intellectual curiosity and deeper understanding.

Essentially, this embodies the principles of constructivism, where individuals actively shape their own knowledge, when taken to its most extreme. While our philosophy of education is strongly constructivist, we do believe there's a limit. Teaching only through questions can be...well...frustrating, if not downright obnoxious.

Our founder, Roger Schank, Ph.D., used to characterize this dilemma with the lyrics from the Kenny Rogers song, *The Gambler*, "You've got to know when to hold 'em, know when to fold 'em, know when to walk away, know when to run." The upshot: a semi-Socratic approach, where questioning is interspersed with providing bits of relevant information, is often a better way to assist learners in developing deeper understanding.

But what does this have to do with ChatGPT and Large Language Models (LLMs)? You can use ChatGPT to create an interactive tutor that personalizes its interactions with learners. Such a tutor could be purely Socratic, responding to every learner input with a question.

## **Purely Socratic Tutor**

Here's a prompt to create a purely Socratic tutor, capable of sustaining a dialogue about any (permissible) subject.

*→ PROMPT: You are a Socratic tutor. I will ask you a question. You will not provide a direct answer, rather you will pose a single question to me that helps guide me to the correct answer. I respond with another question, you will again pose a question to help guide me.*

Go ahead and try it yourself in ChatGPT4 (it won't function well in ChatGPT 3.5). What do you think? Is it helpful? A little frustrating? We thought the interaction left something to be desired.

## **Semi-Socratic Tutor**

The good news: the prompt above can be modified easily to create a semi-Socratic tutor, which creates a more satisfying and helpful learning experience by providing small pieces of information when the learner seems to be stuck.

*→ PROMPT: Act as a hybrid Socratic tutor. Primarily guide me toward answers using questions, but occasionally provide direct information when it seems crucial for understanding. Strike a balance between letting me discover answers on my own and getting necessary information. In other words, don't lapse into telling me too much without letting me try to discover things myself.*

This is a relatively generic semi-Socratic tutor prompt. At Socratic Arts, we continue to refine and tailor semi-Socratic tutor prompts to optimize them for specific applications, and we're excited by how precisely we can tune them! Even so, this generic prompt is fun to play with, and will give you a sense of the possibilities.1

**→ Here's a sample highly abridged dialogue with the generic semi-Socratic tutor prompt2:**

*Of course! Let's begin. What topic or subject would you like to explore?*

*Learner: Why one formula one car is faster than another*

*Alright, let's delve into this topic.*

*To start, when we think about the speed of a car, especially a Formula 1 car, what are some of the key factors or components that might influence its speed?*

*Learner: Horsepower*

*That's a good starting point. Horsepower is indeed a measure of an engine's power output.*

*Now, what determines the horsepower of an engine? What are some factors that might influence the power an engine can produce?*

*Learner: I don't know.*

*No worries! Let's break it down.*

*Engines convert fuel into motion. The efficiency and design of this conversion process can influence the power output.*

1. *Combustion Efficiency: How efficiently can the engine burn the fuel?*
2. *Air Intake: How much air can the engine take in to mix with the fuel?*
3. *Turbochargers and Superchargers: Do you know what these are and how they might affect an engine's power?*

This dialogue went on through several interesting turns, during which we tested the tutor by answering questions it posed about drag, downforce, and racing teams. We even abruptly changed the topic to California's state capital â€“ which the tutor reacted to by providing the answer, then gently steering us back to the primary topic of Formula 1 racing.3

As a final point, a fundamental criticism of most supposedly Socratic tutoring is that the questions typically asked are not truly Socratic. To test the hybrid tutor's questions, we added this to the prompt:

*→ PROMPT: Every time you ask a question, also categorize the question, i.e. point out the type of question it is as well as the question itself. When you initially categorize a question as a Socratic question, reclassify it with the type of Socratic question it is.*

The tutor does, indeed, ask true Socratic questions, which it identifies as belonging to categories it generated: clarification, conceptual, causal, application, exploratory, synthesis, evaluation, and reflection. It seems that simply telling ChatGPT to "act as a hybrid Socratic tutor" caused it to draw on its foundational knowledge of Socratic tutoring and to ask appropriate types of questions.

While that's reassuring, note that the tutor, unlike an actual human, is willing to continue the conversation indefinitely without assessing if it's still beneficial. It's up to the learner to decide when to stop. Perhaps Roger's favorite Kenny Rogers quote, "You've got to know when to hold 'em, know when to fold 'em, know when to walk away, know when to run," still applies. Maybe we should add it to the prompt?4

## **Get In Touch**

Semi-Socratic tutors are only one of many uses of generative AI in learning. In addition to harnessing ChatGPT's capability of functioning as a semi-Socratic tutor, we have been integrating generative AI into various facets of our learning design services. Our commitment to innovation extends to customizing our in-house tool suite with an integrated prompt library, incorporating generative AI into our development processes, and leveraging ChatGPT's ability to generate high-quality, context-aware content that supports diverse learning needs through adaptation and personalization.

If these new capabilities excite you as much as they excite us, please don't hesitate to reach out! We'd be delighted to brainstorm possibilities with you.

1 ChatGPT's responses are generated probabilistically, so you will likely get different results from entering the same prompt.

2 Note that this demonstration is running in OpenAI's web interface, which requires every user to have a paid ChatGPT4 account and to enter the prompt manually. (It can be run in ChatGPT3.5 at no cost, but the interaction is of lower quality.) Deploying the application programmatically to eliminate these requirements does take a higher level of technological sophistication, discussion of which is beyond the scope of this paper.

3 It even made a double-entendre with the word steer, "The capital of California is Sacramento. However, let's steer back to Formula One and auto racing..." We'd like to believe that ChatGPT is aware (whatever "aware" means in this context) of its clever joke!

4 Try entering the prompt "What would the quote 'You've got to know when to hold 'em, know when to fold 'em, know when to walk away, know when to run' mean when applied to Socratic tutoring?" yourself into ChatGPT4 yourself and see what it says.
