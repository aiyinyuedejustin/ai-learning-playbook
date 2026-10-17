# Scott Young：用 AI 学得更好的 22 条想法

- 链接：https://www.scotthyoung.com/blog/2025/05/13/22-thoughts-on-using-ai-to-learn-better/
- 作者：Scott Young
- 获取方式：网页正文（trafilatura 提取）

---

I’ve been thinking about (and tinkering with) AI a lot lately. Specifically, I’m focused on how the new tools can be used to learn better.

[Ultralearning](https://www.scotthyoung.com/blog/ultralearning/) was premised, in part, on the idea that new technologies can help autodidacts accelerate their learning. Open courseware enabled, for the first time, someone like myself to [study from actual MIT classes](https://www.scotthyoung.com/blog/myprojects/mit-challenge-2/). Machine translation, Skype tutoring and spaced repetition software transformed the possibilities for [learning languages](https://www.scotthyoung.com/blog/myprojects/the-year-without-english-2/). Even learning to [draw by hand](https://www.scotthyoung.com/blog/myprojects/portrait-challenge/) can be accelerated if you are able to superimpose your reference images to easily diagnose mistakes.

But those technological leaps pale in comparison to the advances in AI we’ve experienced in the last couple of years. The possibilities for using technology to assist with principles I identified in [my 2019 book](https://www.scotthyoung.com/blog/ultralearning/) are vast—meta-learning, on-demand explanations, limitless practice problems, corrective feedback and more.

Given the size of the topic, I’ve been a little reluctant to write about it, as I feel it deserves much more in-depth effort than a single blog post could ever provide. However, as that will take me some time to arrive at, I figured I’d share some tentative thoughts:

## Necessary and Unnecessary Difficulty

1\. AI can make learning easier. This is a double-edged sword. While it can reduce some of the unnecessary pain of learning by making explanations, examples and guidance more available, it also has the obvious potential to undercut the necessary effort required for learning.

2\. [Necessary effort](https://www.scotthyoung.com/blog/2022/01/04/cognitive-load-theory/) includes things like attending to facts, forming a mental model of the situation, practice, retrieval, and noticing gaps in your own abilities and understanding**.**

3\. Unnecessary effort includes things like difficulties due to poor explanations, insufficient practice materials, materials that are too hard/easy, trial-and-error problem solving, lack of feedback, etc.

4\. This dual nature means that, like most other tech changes, AI will have ambiguous effects on learning, broadly speaking. Some people will use it to learn more effectively; others will simply use it to cheat on their homework.

5\. Furthermore, what constitutes “necessary” effort is both [theoretically contentious](https://www.scotthyoung.com/blog/2022/05/25/do-you-learn-more-by-struggling-on-hard-problems/) and [poorly understood](https://www.tandfonline.com/doi/abs/10.1080/00461528209529247) by learners. Therefore, the risk that even well-meaning students undercut their learning by skipping over the “necessary” parts is non-trivial.

## The Value of Learning Skills

6\. At the same time AI makes learning easier, it also changes the value of what is learned. Many skills that can be performed well by AI are going to rapidly lose their economic value. Basic illustration, translation, and coding skills are going to be devalued as a near-costless competitor emerges.

7\. But this does not mean learning, itself, is a waste of time. In the near-term, many AI-adjacent skills may even increase in value as “centaurs,” or human/AI collaborative pairs, are more productive than either on their own. <sup>1</sup>

8\. Nor is it the case that, just because an LLM can do a skill, learning it as a human being is a waste of time. To think efficiently, much knowledge and skill needs to be in your brain, not on silicon. Thus, just as teaching children to add numbers has remained a core aspect of mathematics education despite decades of cheap calculators, so too will it remain important to learn a lot of skills that AI can already perform at superhuman levels.

9\. This means using AI to accelerate your learning in the skills it is already proficient in is the most obvious use case for AI-assisted learning. Despite the precarious position of professional translation, for instance, this is one of the best times to study a new language.

## Verifying AI Output

10\. Much is made of hallucinations, but nearly all sources have a degree of fallibility. I remember the moral panic about Wikipedia when it first arrived, but today, Wikipedia is more accurate than pretty much every non-academic source (and even then you’d be alarmed at how often citations are misleading).

11\. The easiest way to sidestep hallucinations wholesale is to use AI in a verifiable way. Verifiable prompts produce answers that may have been difficult to generate, but are easy to check. Since [P!=NP](https://en.wikipedia.org/wiki/P_versus_NP_problem)[<sup>2</sup>](#easy-footnote-bottom-2-17281) this is enormously useful. For instance, asking AI to give the primary sources used means you can easily check whether the research says what the AI claims.

12\. Analogies, metaphors, visual mnemonics and other “help me remember this” types of prompting are also an example of verifiable AI output—here hallucinations are irrelevant because the answer isn’t factual; AI generating dozens of examples of creative “sounds like” imagery for a keyword mnemonic isn’t an issue of accuracy beyond whether the words actually do sound alike. <sup>3</sup>

## AI May Not Be a Good Teacher, but It Might Be a Great Tutor

13\. Currently, a major bottleneck in AI usefulness is the clarity and precision of the prompt it is given. Responses can be vastly more helpful if you’re really clear on what you want. Many disappointments of AI use come from expecting a good one-shot response, though it may take a few iterations on your prompt before you can articulate exactly what you need.

14\. This prompt-dependency means that AI can be a great tutor, even though it is a mediocre teacher. For most people, a traditional course/textbook/curriculum will be better than “going blind” into AI and expecting it to teach you in an effective way. But, if you already know your sticking point, then AI is great for filling in the gaps.

15\. For example, a key step in the [Feynman Technique](https://www.scotthyoung.com/blog/2024/03/26/5-keys-feynman-technique/) is to map your understanding of a topic so you can identify a precise question. In the original formulation, that then turned to close reading to try to resolve your confusion, but now it is the perfect time to ask an AI.<sup>4</sup>

## How I Am Using AI for Learning: AI’s Strengths and Weaknesses (So Far…)

16\. I now do a lot of my reading “AI assisted,” meaning that when I read a textbook or paper, I query a reasoning model like o3 to ask follow-up questions like if there are updates based on more recent research, the empirical status of claims the author is making and do robustness checks to see if an author’s viewpoint is mainstream or unorthodox.

17\. But I haven’t given up on real books yet. Deep Research and other tools can do a decent literature review if you have a niche question, but it’s undoubtedly worse than a book or review paper written by an actual expert.

18\. In addition to knowledge and explanations, AI can also help with cognitive skills. It can be hard to find good practice problems and questions, but AI can generate them.

19\. I’ve used AI a lot to help practice Macedonian grammar, something that’s difficult to do with flashcards (because you’re learning a rule, not a fact), and which doesn’t have the ample resources that major world languages offer.

20\. Still, fine-tuning to get useful output can also be hard. Repetitive practice quickly devolves into loops of highly similar questions/answers upon repeat prompting. Getting an API key and prompting the AI through software is probably more reliable than using the chat interface.

21\. Coding agents are getting good enough now that bespoke learning software for specific tasks is approaching the threshold of feasibility from a cost-benefit standpoint. I recently made a script to help my Chinese listening skills by downloading a YouTube video, making a transcript, summarizing it in English and providing a table of key words to help with watching. Something like this would have been incredibly helpful in my [intensive language learning](https://www.scotthyoung.com/blog/myprojects/the-year-without-english-2/) periods, but coding it myself from scratch would have taken so long that it would have eaten up most of the benefits.

## My Final Thoughts

22\. Ultimately, in spite of the new wonders (and worrisome dangers) of AI, it’s important to underline that learning itself hasn’t changed. You still have the same brain, and the [rules for how learning works](https://www.scotthyoung.com/blog/getbetter/) still apply.

In all this, I’ve entirely side-stepped the question of whether AI is “good” as a whole. As someone whose livelihood depends on many of the skills that AI now performs, I’m as uncertain as anyone about the answer to that question.

Still, I take the invention of LLMs and their likely continued progress to be brute facts of reality. As the world changes, the most valuable skill will be learning to adapt.

#### Footnotes

1. Tyler Cowen’s [Average is Over](https://www.amazon.com/average-over-powering-america-stagnation/dp/0525953736), written before the recent LLM boom, is the best description of this emerging reality I’ve seen.2. Obviously true. Lack of proof notwithstanding.3. Hat tip to [Benny Lewis](https://www.fluentin3months.com/about/) for this suggestion.4. While AI explanations are not verifiable in the way that mnemonics or citations are, they do seem to be reasonably reliable (or at least better than a typical Internet search, which is the most likely alternative).
