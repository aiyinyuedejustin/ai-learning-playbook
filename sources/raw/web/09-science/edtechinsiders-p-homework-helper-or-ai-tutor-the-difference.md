# Edtech Insiders：作业助手还是 AI 导师

- 链接：https://edtechinsiders.substack.com/p/homework-helper-or-ai-tutor-the-difference
- 作者：Sarah; Alex Sarlin; Ben Kornell; Jen Lapaz; Lin Ler
- 获取方式：网页正文（trafilatura 提取）

---

[Get 10% of your EdTech Week Ticket now with code EDTECHINSIDER10](https://www.edtechweek.com/)

# Homework Helper or AI Tutor? The Difference Determines What Students Learn.

[Sponsored by Overdeck Family Foundation](https://overdeck.org/)

#### By: [Lin Ler](https://www.linkedin.com/in/lin-ler/)

*Lin Ler is a Stanford MBA and MA in Education candidate working at the intersection of business strategy, learning science, and frontier AI. With a background spanning management consulting, EdTech startups, and the social sector, Lin translates complex AI capabilities into practical insight for the future of learning.*

Of all the topics raised since Generative AI hit education, the concept of “AI tutoring” may be what has most thoroughly grabbed the public imagination. It’s also one of the hardest to define. The “AI tutoring” label can plausibly be applied to a very diverse set of learning experiences:

- **Dedicated edtech “AI tutoring” products** (e.g., Synthesis Tutor, SigIQ, Thinkverse, Tutor.ai)
- **“AI tutoring” features within larger learning suites** (e.g., Ace by Numerade, Khanmigo by Khan Academy, StudyFetch’s AI Tutor)
- **Mobile applications designed for on-demand homework help** (e.g., Gauth, Photomath, Brainly Homework Helper, Zuoyebang, QANDA)
- **“AI companions” designed for learning conversations, often in language learning** (e.g., TalkPal, Superhuman, Tutor Lily, Praktika, ELSA Speak)
- **AI systems designed to improve human tutoring and/or match students to tutors** (e.g., Hilink, Sidekick from Step Up Tutoring, TutorOcean)
- **Frontier large language models placed in “study mode”** (e.g., Google Guided Learning, ChatGPT Study Mode, Claude’s Learning Mode)

When the industry asks whether “AI tutoring” works, it assumes researchers are talking about one thing when referring to “AI tutoring.” When Edtech Insiders spoke with Susanna Loeb, the Kissick Family Professor and faculty director of Stanford’s SCALE Initiative, about the potential impact of AI tutoring, she clarified an important distinction: *“Are we talking about homework help, or a high-impact tutor?”*

That difference matters. A LOT. Homework helpers (and off-the-shelf LLMs) are designed to resolve the task a user brings in real time: to get to an answer. Great tutors *don’t* provide answers. They build trusted relationships, decide what each learner needs, preserve the student’s responsibility to think and practice, and help learners make progress over time through a larger course of learning.

## AI Tutoring Is Not a Monolith

A new SCALE brief from Stanford offers a useful route through this definitional problem. Instead of sorting tutoring models by how sophisticated their AI appears, *[AI Tutoring Is Not a Monolith](https://scale.stanford.edu/research-in-action/ai-tutoring-not-monolith)* places them on a spectrum of **relational intensity**: the depth and consistency of the human connection surrounding the student.

At the high-intensity end, a human tutor leads the instruction and holds the relationship, while AI may assist with lesson preparation, data analysis, or suggestions. In the middle, the student works directly with an AI tutor while a person oversees the process and intervenes. At the lowest-intensity, the student works with an AI-only tutor without direct human oversight.

This framework does not assume that more human contact always makes a tool better (ex: A well-designed hybrid can use AI to remove administrative work and give a human tutor more time for the relationship). It also doesn’t assume that every student needs the same degree of support.

It *does* show where the evidence is strongest: **High-impact tutoring is still defined by live, human-led instruction.** The evidence becomes thinner as direct human involvement decreases. At present, SCALE concludes that AI-led tutors may offer valuable supplemental practice, but do not yet inherit the definition or evidence base of high-impact tutoring simply because they provide one-to-one responses.

That evidence base is unusually deep. In a 2026 synthesis, [Loeb and Carly Robinson](https://scale.stanford.edu/publications/tutoring) report that meta-analyses estimate average effects of 0.29 to 0.37 standard deviations on student achievement, making tutoring one of the most effective interventions in education research. The strongest programs also tend to share a recognizable architecture:

1. Students and tutors meet frequently, 1:1 or in small groups
2. Tutoring connects to classroom curriculum
3. Tutors use evidence of student understanding to adjust instruction
4. The same tutor works with the student over time
5. Tutors receive training, materials, and ongoing support

These features could conceivably be applied to AI-enhanced tutoring, and many of the edtech companies designing tutoring products already use several of these principles. Human tutors improve through training and coaching. AI tutors need their own form of pedagogical preparation: structured instructional goals, curriculum grounding, examples of productive tutor moves, constraints against answer-giving, and continuous evaluation of how they respond to actual student thinking. The foundation model is only one component of the tutor, and often one that must be overridden to get to deeper learning-oriented behavior.

These features explain *why* tutoring works, not merely that it works. They also give us a better test for any AI tutor: Which conditions does the product reproduce, which does it change, and which does it drop?

Consider consistency: an AI system is technically available at any hour and can respond with the same patience each time. But availability is not the same as learners actually showing up, persisting through difficulty, or trusting the person asking them to try again.

“Most of that kind of engagement is going to come from the context and from the humans that \[students\] interact with,” Loeb told us. “It’s that human connection that really inspires people to do things that are difficult.”

A new SCALE study makes the point starkly. Across [two randomized trials involving 355 elementary students](https://scale.stanford.edu/ai/repository/access-not-enough-human-support-improves-engagement-ai-tutoring), researchers gave students scheduled access to an AI literacy platform, either independently or with an in-person tutor focused on engagement rather than instruction. In the independent group, nearly half never used the platform. Those who did averaged only two to five minutes a week. Human support increased engagement by 71% to 80%, but use remained low and reading achievement did not improve. The human helped make the learning routine more real, and even that was not enough to create the dosage associated with gains.

## The Homework Helper Test

Relational intensity is likely only one part of the answer. Most educators and edtech designers agree that any student-facing system still needs to behave like a tutor in some key ways to be effective. But the exact definition of what makes tutoring effective, what the [National Tutoring Observatory](https://nationaltutoringobservatory.org/) calls effective “tutor moves”, are still very much being defined.

In a [randomized field experiment with nearly 1,000 high-school mathematics students](https://doi.org/10.1073/pnas.2422633122), access to a general GPT-4 interface increased students’ practice performance by 48%. A guardrailed “GPT Tutor,” supplied with teacher-written solutions and instructed to give hints, increased it by 127%.

Then, the AI was removed. Students who had used the general chatbot scored 17% lower than the control group on an unaided test. Students who had used the guardrailed tutor performed about the same as the control group—not worse, but not better.

This is the cognitive-debt problem described in [the first article in this series](https://edtechinsiders.substack.com/p/the-cognitive-debt-problem): a system can improve what a student produces now without building the capacity they need later. This is the *opposite* of the role of a true tutor. The guardrails prevented the harm seen with unrestricted help, but they did not automatically create a learning gain.

Loeb adds another difference. Homework help is reactive: the student must know what to ask. A tutor needs a view of the curriculum and the learner’s position within it. “Students don’t always know what they don’t know,” she said. They may also not know “what’s next in the curriculum.” A high-impact tutor therefore does not only answer the incoming question. It helps determine the next problem, explanation, or practice the student needs.

A useful working definition follows:

A student-facing AI tutor pursues a defined learning objective, elicits evidence of the student’s understanding, adapts its next move, and keeps the student responsible for the thinking.


That is a much higher bar than generating a fluent explanation. It’s also a bar that the wider AI-in-education ecosystem is beginning to make measurable.

## Building the Ecosystem for Better AI Tutors

SCALE’s role is increasingly to help guide this ecosystem: translating the established evidence on tutoring into design principles, testing new implementations, and maintaining a [repository](https://scale.stanford.edu/ai/repository) where emerging AI studies can be compared. The field is not converging on a single winning product. It is building several layers of research, infrastructure, and evaluation at once.

**Products Are Changing the Interaction**

Edtech developers are experimenting with structured, curriculum-aligned tutors rather than open chat boxes. Rori, a WhatsApp mathematics tutor, produced an estimated 0.36-standard-deviation gain in an experiment across 11 Ghanaian schools, although the small number of schools and student attrition make the estimate less certain. In the United Kingdom, Eedi and Google tested LearnLM inside a constrained mathematics platform with human tutors supervising AI-drafted messages. Meanwhile, frontier labs have introduced [ChatGPT Study Mode](https://openai.com/index/chatgpt-study-mode/), [Claude Learning Mode](https://www.anthropic.com/news/introducing-claude-for-education), and [Gemini Guided Learning](https://blog.google/products-and-platforms/products/education/guided-learning/), each designed to ask questions, scaffold steps, and delay the immediate answer. These are meaningful design shifts, although a product’s stated pedagogy is not yet evidence of durable learning.

**Benchmarks as Definitions of Effective Tutor Behavior…**

Research labs all over the world have been working on a variety of tutoring and education benchmarks to evaluate AI models, all with their own specific theories about what makes tutoring effective.

- [TutorBench](https://arxiv.org/abs/2510.02663) gives a model 1,490 difficult high-school and AP STEM scenarios and tests three practical capabilities: can it adapt an explanation to a student’s confusion, give actionable feedback on the work shown, and offer a hint that keeps the learner active? The best of 16 frontier models scored about ***56 out of 100***. By TutorBench’s definition, frontier models have lots of room for improvement, which is exactly where Edtech can take the baton and run with it.
- [MRBench](https://arxiv.org/pdf/2412.09416) is another benchmark that evaluates tutor responses across 8 pedagogical dimensions such as ‘coherence’, ‘tutor tone’, ‘mistake identification’ and of course, ‘revealing of the answer’.
- One interesting approach is to define effective tutor behavior by subject, like [MathTutorBench](https://arxiv.org/abs/2502.18940?utm_source=chatgpt.com) and [CSTutorBench](https://arxiv.org/abs/2607.05571?utm_source=chatgpt.com) for math and computer science, respectively.
- Newer benchmarks are already pushing beyond one response. [EduClaw-Bench](https://arxiv.org/abs/2608.03206) places tutor agents in a simulated 30-day learning relationship and finds that almost no model-and-agent combination sustains strong tutoring over the full period.
- In an interesting benchmark-like test by development firm [Comprendo](https://comprendo.dev/insights/can-ai-tutors-teach), six frontier models were asked to hold multi-turn conversations with *simulated* eighth-graders who were designed to hold common algebra misconceptions. When the LLMs were given generic instructions to be helpful, the models gave away ***the answer in 97% of conversations***. A “tutoring” prompt improved performance substantially, but even then, no model was consistently strong at both identifying misconceptions and withholding enough of the reasoning for the student to do the work. This was a simulation, not evidence that 97% of classroom interactions fail. Its value is diagnostic: it shows that a model trained to be helpful will usually optimize for resolving the problem. Tutoring requires a different objective.

**… and Shared Infrastructure Can Make Those Standards Reusable**

- [Learning Commons](https://docs.learningcommons.org/) is building open knowledge graphs and evaluators that connect AI outputs to curriculum, standards, and learning-science rubrics.
- Digital Promise’s [$26 million K–12 AI Infrastructure Program](https://digitalpromise.org/2026/06/29/digital-promise-announces-first-grantees-of-the-k-12-ai-infrastructure-program/) is funding open datasets, benchmarks, and models. Its first grants include a benchmark for identifying science misconceptions, simulated student models, a [National Tutoring Observatory](https://nationaltutoringobservatory.org/) project on educational speech recognition, and KB-TutorBench for multimodal formative assessment.

These layers serve different purposes. A benchmark can show whether a model makes a plausible tutoring move. It *cannot* show that a child learned. A randomized trial can estimate learning under one implementation, but it may be obsolete when the model or interface changes. Shared infrastructure allows many developers to test for the same educational properties, while repeated classroom research establishes whether those properties matter in practice.

## The Future of AI Tutoring

The near-term case for AI tutoring is not necessarily that an AI chatbot will reproduce or surpass a great human tutor. It is that the field is truly beginning to specify what the label *tutor* requires.

AI tutors should know what a student is meant to learn, identify why they are stuck, choose an appropriate next move, and most importantly, organize the student’s behavior to optimize for learning, not performance. The surrounding system must also create the consistency, trust, and motivation that get students to return. Sometimes AI may deliver the practice directly. Sometimes its highest-value role will be helping a human tutor support learners more consistently.

Loeb’s optimism rests on that wider possibility: “We’re so far from the ideal that there are lots of opportunities to do this better,” she said. AI can theoretically help schools differentiate instruction, give students more room to explore their curiosity, and support greater autonomy — but education tools and products will need to focus on “the process of learning instead of the ultimate production.”

“We know something’s not working right,” Loeb concluded, “but we’re optimistic that it could work a lot better.”

## Bibliography

###### Anthropic. (2025, April 2). Introducing Claude for Education. [https://www.anthropic.com/news/introducing-claude-for-education](https://www.anthropic.com/news/introducing-claude-for-education)

###### Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Mariman, R. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. *Proceedings of the National Academy of Sciences, 122*(26). [https://doi.org/10.1073/pnas.2422633122](https://doi.org/10.1073/pnas.2422633122)

###### Comprendo. (2026, August 10). Can AI tutors actually teach? We measured it. [https://comprendo.dev/insights/can-ai-tutors-teach](https://comprendo.dev/insights/can-ai-tutors-teach)

###### Digital Promise. (2026, June 29). Digital Promise announces first grantees of the K–12 AI Infrastructure Program. [https://digitalpromise.org/2026/06/29/digital-promise-announces-first-grantees-of-the-k-12-ai-infrastructure-program/](https://digitalpromise.org/2026/06/29/digital-promise-announces-first-grantees-of-the-k-12-ai-infrastructure-program/)

###### Google. (2025, August 6). Guided Learning in Gemini: From answers to understanding. [https://blog.google/products-and-platforms/products/education/guided-learning/](https://blog.google/products-and-platforms/products/education/guided-learning/)

###### Hashmi, S. F. A., & Rebello, N. S. (2026). A bottom-up taxonomy of student discourse with a Socratic AI physics tutor. *arXiv*. [https://arxiv.org/abs/2608.07373](https://arxiv.org/abs/2608.07373)

###### Henkel, O., Horne-Robinson, H., Kozhakhmetova, N., & Lee, A. (2024). Effective and scalable math support: Experimental evidence on the impact of an AI-math tutor in Ghana. *arXiv*. [https://arxiv.org/abs/2402.09809](https://arxiv.org/abs/2402.09809)

###### Lane, H. C., & Kageler, B. (2026). CSTutorBench: Benchmarking small language models as tutors for block-based programming. *arXiv*. [https://arxiv.org/abs/2607.05571](https://arxiv.org/abs/2607.05571)

###### LearnLM Team & Eedi. (2025). AI tutoring can safely and effectively support students: An exploratory RCT in UK classrooms. *arXiv*. [https://arxiv.org/abs/2512.23633](https://arxiv.org/abs/2512.23633)

###### Learning Commons. (2026). AI developer tools for education.

###### https://docs.learningcommons.org/

###### Lee, U., Lee, S., Jeong, Y., Lee, E., Shin, M., & Kwon, H. (2026). EduClaw-Bench: A long-horizon benchmark for pedagogical LLM agents with simulated learners. *arXiv*. [https://arxiv.org/abs/2608.03206](https://arxiv.org/abs/2608.03206)

###### Ler, R. L. (2026, May 8). The cognitive debt problem. *EdTech Insiders*.

###### Loeb, S. (2026, August 14). Interview with EdTech Insiders on AI tutoring \[Unpublished transcript\].

###### Loeb, S., & Robinson, C. D. (2026). Tutoring. *AEFP Live Handbook*. [https://scale.stanford.edu/publications/tutoring](https://scale.stanford.edu/publications/tutoring)

###### Macina, J., Daheim, N., Hakimi, I., Kapur, M., Gurevych, I., & Sachan, M. (2025). MathTutorBench: A benchmark for measuring open-ended pedagogical capabilities of LLM tutors. *arXiv*. [https://arxiv.org/abs/2502.18940](https://arxiv.org/abs/2502.18940)

###### Maurya, K. K., Srivatsa, K. V. A., Petukhova, K., & Kochmar, E. (2024). Unifying AI tutor evaluation: An evaluation taxonomy for pedagogical ability assessment of LLM-powered AI tutors. *arXiv*. [https://arxiv.org/abs/2412.09416](https://arxiv.org/abs/2412.09416)

###### National Tutoring Observatory. (n.d.). National Tutoring Observatory.

###### https://nationaltutoringobservatory.org/

###### OpenAI. (2025, July 29). Introducing study mode. [https://openai.com/index/chatgpt-study-mode/](https://openai.com/index/chatgpt-study-mode/)

###### Robinson, C. D., Gormley, D., Ribeiro, A. T., & Loeb, S. (2026). Access is not enough: Human support improves engagement with AI tutoring. *EdWorkingPapers*. [https://doi.org/10.26300/pz7p-p388](https://doi.org/10.26300/pz7p-p388)

###### SCALE Initiative. (2026). Research study repository. [https://scale.stanford.edu/ai/repository](https://scale.stanford.edu/ai/repository)

###### Srinivasa, R. S., Che, Z., Zhang, C. B. C., et al. (2025). TutorBench: A benchmark to assess tutoring capabilities of large language models. *arXiv*. [https://arxiv.org/abs/2510.02663](https://arxiv.org/abs/2510.02663)

###### Turano, C., Pihl, V., Agnew, C., Ziegler, L., & Loeb, S. (2026). AI tutoring is not a monolith: What we actually know. *SCALE Initiative at Stanford University*. [https://scale.stanford.edu/research-in-action/ai-tutoring-not-monolith](https://scale.stanford.edu/research-in-action/ai-tutoring-not-monolith)

Special thanks to [Overdeck Family Foundation](https://overdeck.org/) for sponsoring this FINAL article in our AI & Efficacy Editorial Research Series diving into key research findings from [Stanford’s AI Hub for Education Research Repository](https://scale.stanford.edu/ai/repository) (a project by Stanford’s SCALE Initiative).

You can support our work by becoming a paid subscriber, or email info@edtechinsiders.org to learn more about partnerships and sponsorships.

# Insider Announcements

Hey Insiders! We’ve partnered with the team at StartEd to offer you all 10% off your ticket to EdTech Week 2026! We’ll be there, and we know lot’s of you will be too.

This code is active for all ticket types, including 10% off the already discounted earlybird pricing through August 31. Grab your ticket now before the price goes up!

# Upcoming Events

## What Is the Future of Higher Education in America?

Friday, August 28

9:00-10:00 AM PT / Noon-1:00 PM ET

Webinar on Zoom


AI is reshaping learning, employers are rethinking credentials, and universities are facing unprecedented change. Join us for a live conversation with an incredible panel of experts exploring how higher education must evolve to remain relevant, accessible, and valuable in the decade ahead.

Join us live or register to receive the recording the following Wednesday.

# Top Edtech Headlines

### 1.  U.S. Department of Education Releases Guidance on Responsible Use of Education Technology in the Classroom

The U.S. Department of Education has released new guidance urging states, districts, educators, and edtech providers to prioritize instructional value, evidence, educator judgment, transparency, and student outcomes when selecting and using technology in classrooms. The guidance specifically calls on schools to evaluate what learning problem a tool solves, who should use it, for how long, and what evidence demonstrates that it improves learning, while encouraging districts to remove technologies that repeatedly fail to deliver results.

### 2. Does AI Stop Children From Learning?

A new analysis from The Economist examines research tracking 27,000 students ages 12–18 in China and finds a striking tradeoff in how students use AI for schoolwork. Students using AI saw homework scores increase by 18% and spent less time completing assignments, but performed 20% worse on exams than students who did not use AI—raising questions about whether AI can improve short-term performance while undermining deeper learning when students rely on it to complete work rather than understand it.

### 3. Introducing ChatGPT for Teens: Built for Learning, Backed by Protections

OpenAI has launched ChatGPT for Teens, a version of ChatGPT designed specifically for users ages 13–17 with stronger safety protections and features aimed at supporting learning rather than simply completing assignments. The experience includes Study Mode, responsible homework reminders, quizzes, learning visualizations, and Study Hours, while parents can manage selected settings and receive notifications in certain high-risk situations. OpenAI is also partnering with CodeAI to help students and educators build AI literacy and learn to question, direct, and create with AI.

### 4. Reach Capital Raises $265M Fund V to Back AI Founders Building to ‘Expand Human Potential’

Reach Capital has raised a $265 million fifth fund to invest in roughly 50 early-stage companies working across learning, health, and work. Their new thesis is focused on AI applications that “expand human potential,” with investments ranging from $1 million to $10 million from pre-seed through Series A. [Listen to our interview with Reach Partner Jomayra Herrera](https://edtechinsiders.buzzsprout.com/1877869/episodes/19664178-inside-reach-capital-s-265m-fund-v-with-jomayra-herrera) for more!

### 5. The Prohibition Fallacy: Why Banning Tech Won’t Protect Our Kids

A new Forbes Council essay by Erin Mote argues that banning technology outright is unlikely to protect children from its risks, and instead calls for a more nuanced approach to how young people engage with digital tools. This comes at a moment when schools and policymakers are weighing restrictions on phones, social media, and AI, raising the question of whether effective technology policy should focus less on prohibition and more on teaching young people how to use technology safely and responsibly.

# Inside Reach Capital’s $265M Fund V

**[Jomayra Herrera](https://www.linkedin.com/in/jomayraherrera/)** is a Partner at **[Reach Capital](https://www.reachcapital.com/)**, an early-stage venture fund investing across learning, health, and work. Previously, she worked at Emerson Collective and Cowboy Ventures, investing in companies including Handshake, Guild, Contra, and Career Karma.

### 5 Things You’ll Learn in This Episode

1. Why Reach Capital is doubling down on pre-seed and early-stage investing with its new $265M Fund V.
2. How learning, health, and work intersect to create new opportunities for innovation.
3. What Jomayra looks for in exceptional founders, especially in the age of AI.
4. Why the strongest AI companies go beyond AI as a feature to create new capabilities and durable advantages.
5. How B2C-to-B2B models and school choice are creating new opportunities across education.

Thanks for reading! Support our work by becoming a paid subscriber, or email info@edtechinsiders.org to learn more about partnerships and sponsorships.

The clause I keep coming back to is "elicits evidence of the student's understanding." Last weekend I ran a one-problem version of the homework helper test: 2/3 + 3/4, then the classic wrong answer, 5/7, into seven tools from your list (ChatGPT and Gemini default and in study mode, Guided Learning, Khanmigo). None gave away the answer. None asked how I got 5/7 either. Every one went verdict-first or rule-first and as a teacher myself I can tell you that sometimes students may seem to be thinking one way but then provide a completely unexpected answer.

I looked at MRBench's eight dimensions after reading your benchmarks section. A tutor scores for identifying the mistake, locating it, and providing guidance, and loses points for revealing the answer. Nothing scores asking the student to explain first. So the rubric, as a definition, ranks 'you added the numerators and denominators directly, but' above 'how did you get 5/7?' If benchmarks are definitions, that's the one I'd want changed.

It matters past the student. A teacher with thirty kids can't ask thirty of them how they got it every night. The kid's explanation is the only output worth passing to a teacher or a parent; 'not quite' passes nothing. Loeb's 'process of learning instead of the ultimate production' is this exactly. The process lives in the teacher–student and parent–student bond, and a tool's job is to feed it, not stand in for it.

Have you evaluated the AI tutoring apps that the Alpha Schools use? On your continuum, they appear to be a hybrid model.
