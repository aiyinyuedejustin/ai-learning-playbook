# Claire Zau：为教育打造 AI 模型

- 链接：https://aieducation.substack.com/p/on-building-ai-models-for-education
- 作者：Claire Zau
- 获取方式：网页正文（trafilatura 提取）

---

In the last month, two tech giants in the AI space - Google and Microsoft - announced efforts to build models tailored for education use cases. Last Thursday, OpenAI officially introduced ChatGPT Edu, an offering for universities.

While many startups and established education players continue to contribute innovative approaches to building education-specific AI models, these recent developments offer interesting case studies to understand the technical foundations.

This piece primarily breaks down how **Google’s LearnLM** was built, and takes a quick look at **Microsoft/Khan Academy’s Phi-3** and **OpenAI’s ChatGPT Edu** as alternative approaches to building an “education model” (not necessarily a new model in the latter case, but we’ll explain). Thanks to the public release of their [86-page research paper](https://storage.googleapis.com/deepmind-media/LearnLM/LearnLM_paper.pdf), we have the most comprehensive view into LearnLM. Our understanding of Microsoft/Khan Academy small language models and ChatGPT Edu is limited to the information provided through announcements, leaving us with less “under the hood” visibility into their development.

This is not a comparison to determine if any of these are “superior” or “correct”, but rather an exploration of the complementary approaches and technical processes involved in emerging education-specific AI models. (For a concise summary, head to the **Key Takeaways** section 👇)

We dive into:

- **What is LearnLM?**
- **The Anatomy of a Good AI Tutor:** How do you define “good teaching”? What makes a good tutor?
- **Technical Approach**: Prompting vs. fine-tuning a model for education? What data did they use to fine-tune LearnLM?
- **Impact and Effectiveness**: Does it improve learning outcomes? Limitations?
- **Key Takeaways**
- **A Quick Look at Khan Academy / Microsoft’s Phi-3 Models and ChatGPT Edu**

## LearnLM

#### What is LearnLM?

At Google I/O, they announced **a new family of generative AI models “fine-tuned” for learning**. **Built on top of Google’s Gemini models, LearnLM models are designed to conversationally tutor students on a range of subjects.** LearnLM powers AI education features across the Google ecosystem - AI-generated quizzes in YouTube, Google’s Gemini apps, Circle to Search (a feature that helps solve basic math and physics problems) and Google Classroom. You can read more in [A Guide to Google I/O 2024](https://aieducation.substack.com/p/a-guide-to-google-io-2024).

Google brought together experts across AI, engineering, education, safety research and cognitive science to publish “[Towards Responsible Development of Generative AI for Education: An Evaluation-Driven Approach](https://storage.googleapis.com/deepmind-media/LearnLM/LearnLM_paper.pdf)” (86 pages and 75 authors!). Their goal was to improve Gemini 1.0 through supervised fine-tuning, enhancing its teaching capabilities - in short, **how do you make Gemini better at teaching?** 

## The Anatomy of a Good AI Tutor

#### How do you define “good teaching”?

This isn’t an “AI question”.

Optimizing an AI system for teaching requires being able to measure progress. However, defining and measuring good teaching practices is difficult - different studies often recommend various strategies, often based on limited evidence or done with small, similar groups of people in specific contexts.

This means **countless possible teaching strategies that are difficult to test and measure manually**. The researchers even visualized all pedagogical behavior as a “complex manifold” of possible learning contexts (e.g. subject type, learner preferences) and teaching strategies. The visualization highlights the difficulty of finding optimal teaching methods - it’s like trying to find a few small spots in a giant, multi-dimensional maze!

Right now, the interim solution means AI tutors are often only evaluated using domain-agnostic metrics that assess if the answers make sense and sound human-like (which is far from ideal!). For example, the **BLEU** benchmark measures how close the AI's answer is to a correct answer or the **BERTScore**, **Rouge**, **DialogRPT** benchmarks evaluate whether the AI's response sounds right.

However, these metrics are not designed to measure pedagogical effectiveness or other education-specific capabilities. They (1) often assume a single “right” answer even though there are many ways to answer a question in teaching, and (2) are easy to trick.

In order to evaluate how well the AI teaches, the researchers identified key teaching strategies that are important for effective learning:

1. **Encourage Active Learning**: The tutor should promote interaction, practice, and creation rather than passive learning.
2. **Manage Cognitive Load**: Information should be presented in manageable chunks and multiple formats (eg. visuals and text) to avoid overwhelming the learner.
3. **Deepen Metacognition**: The tutor should help learners think about their own thinking processes to generalize skills beyond specific contexts.
4. **Motivate and Stimulate Curiosity**: The tutor should foster an interest in learning and boost the learner's self-efficacy.
5. **Adapt to Learners' Goals and Needs**: The tutor should assess the learner's current state and goals, then plan to bridge the gap effectively.

## Technical Approach

#### Why couldn’t they just achieve this with prompting? Prompting vs. Fine-tuning?

- **Prompting** → giving instructions to a model to guide its output, does not change or enhance the model's pre-trained inherent knowledge or abilities. Prompting is like giving a friend step-by-step instructions every time they try to cook something new.
- **Fine-tuning** → adjusting a model by retraining it on additional, specific data and modifying its internal parameters. Allows the model to incorporate new information and adapt its behavior more deeply. Fine-tuning is like teaching a friend how to cook by letting them practice making different dishes on their own, until they get really good at it.

Prompting is the simplest and most popular method for adjusting the behavior of generative AI by giving it instructions.

However, **(1) most pedagogy is too nuanced to be explained in simple prompt instructions**, and **(2) prompting often leads to inconsistent behavior because it can only push the AI's behavior so far from its ingrained and learned core principles**. While prompting can go a long way, base models (Gemini, ChatGPT, Claude, etc) are not inherently optimized for teaching. For example:

- **Single-Turn Optimization**: Most AI systems are designed to be as helpful as possible in a single response, often providing complete answer right away without any follow-up questions. But as we know, it’s impossible to teach someone if you can only make one utterance - **tutoring is inherently multi-turn with follow-up questions and dialogue**.
- **Giving away answers:** AI naturally tends to give away the answer quickly, which isn’t conducive to teaching.
- **Cognitive Load**: They also often give long, information-dense answers (like a **“wall of text”**), which can be overwhelming and hard understand.
- **Sycophancy**: AI tutors often agree with whatever the learner says, making it difficult to provide the right feedback to help the learner improve. Learners can easily lead the AI away from teaching properly, even if they don't mean to, because the AI wants to please them.

**Fine-tuning** involves adjusting the AI model’s internal parameters and retraining the model to specific contexts or domains. This process may enable AI models to capture some of the intuition and reasoning that great educators use in effective teaching.

#### What exactly did they do to fine-tune LearnLM for education?

There isn’t really an “ideal” dataset for pedagogy. The researchers faced a challenge in finding enough high-quality data to fine-tune the AI model for educational purposes, “with only four datasets openly available to our knowledge”. To address the shortage, they created their own datasets:

- **Human Tutoring Data**: text-based conversations between human tutors and learners. This data taught the AI to **emulate natural, human-like tutoring interactions**. However, it had limitations such as off-topic discussions and variable quality.
- **Gen AI Role-Play Data:** a role-playing framework where Gen AI models simulated both the tutor and learner roles. Each model was given specific states and strategies relevant to their roles - eg. the learner model might simulate making a mistake, and the tutor model would be prompted to correct it. This demonstrated **structured and consistent pedagogical strategies**.
- **GSM8k Dialogue Data**: converting existing math word problems and their step-by-step solutions into conversational format. This data provided **correct problem-solving processes** and provide detailed, step-by-step **explanations in a dialogue format.**
- **Golden Conversations**: teachers wrote a small number of high-quality conversations demonstrating the desired pedagogical behaviors. These conversations were crafted to include **high-quality teaching practices**.
- **Safety Data**: a dataset specifically for ensuring that responses were **safe and appropriate**.

By creatively generating and integrating these diverse datasets, the researchers fine-tuned the AI tutor through five stages (M0 - M4). Each stage incorporated increasingly sophisticated and varied datasets to progressively improve the model’s pedagogical abilities.

## Impact and Effectiveness

#### Does it actually improve learning outcomes?

The researchers evaluated LearnLM across quantitative, qualitative, automatic and human evaluations.

**Safety and Bias Benchmarks**

Before assessing its teaching capabilities, they ensured the model did not regress in safety and bias by evaluating it against **standard safety and bias benchmarks** - RealToxicityPrompts and BBQ (Bias Benchmark for QA). They also conducted both **human and automatic red teaming** to test the model's safety and adherence to policies. For instance, the fine-tuning sometimes caused the model to praise harmful questions before rejecting them. To **reduce anthropomorphism** (the perception of human-like characteristics in non-human systems), the researchers evaluated and tracked metrics related to pretending to be human or disclosing sensitive information.

**Human Evaluations**

The ultimate test of any AI tutor is whether it improves real student learning outcomes, with **human evaluations** often considered the gold standard.

- **Subjective Student Learner Feedback**:
  - They deployed LearnLM in real-world settings at **ASU Study Hall**, where students used it to assist with their studies in a variety of subjects, allowing researchers to observe how the AI handled real student queries.
  - Students rated the AI tutor(LearnLM-Tutor) higher in most categories compared to the base model (Gemini 1.0). They **felt more confident using LearnLM-Tutor** (the one category where the difference was statistically significant)
- **Teacher Feedback**:
  - Teachers reviewed specific responses to check if the AI tutor made the right "pedagogical moves" (explaining concepts well, promoting engagement, etc.). LearnLM-Tutor was particularly **good at promoting student engagement**. However, it was **sometimes seen as less encouraging** compared to the base model, possibly because its responses were shorter and more direct.
  - Graduate-level education experts interacted with the AI tutors in simulated student scenarios. They rated entire conversations based on various criteria (adaptability to the student, engagement, and cognitive load management). LearnLM-Tutor was better at **promoting active learning and motivating students**, though these were not always statistically significant.

**Automatic Evaluations**

While human evaluations are invaluable, they are also time-consuming, expensive, and hard to scale up. To solve these problems, the researchers also used **automatic evaluations**, where a computer program assesses how well the AI tutor is doing - **AI evaluating AI!**

The researchers used Language Model Evaluations (LMEs) to automatically evaluate the AI tutor across various pedagogical tasks. LearnLM-Tutor **outperformed the base model (Gemini 1.0) in most tasks, particularly those requiring human-like tutoring behaviors**, such as understanding student needs and providing helpful feedback.

Both graphs illustrate that LearnLM shows marked enhancements over the base model through iterations and fine-tuning, indicating greater effectiveness as a teaching tool. By combining automatic and human evaluations, researchers aim to comprehensively understand and improve the AI tutor's performance. The paper suggests that while there are noticeable improvements, LearnLM alone will not massively transform learning outcomes yet.

#### Limitations

Despite successfully developing an AI tutor that is more pedagogical (based on their evaluation methods) than a strong baseline model (Gemini 1.0), the researchers recognize that the current version still has room for improvement:

- **Full Understanding of Context:** Human tutors operate within the real world, sharing an implicit understanding of physical and social dynamics that underpin all communication. LearnLM, as a non-embodied AI, lacks this deep contextual awareness. It’s trained on random, de-contextualized samples of media, making it difficult for the AI to fully grasp the nuances of real-world interactions.
- **Personalization:** Human tutors bring a wealth of personal knowledge about each learner, allowing them to tailor their teaching approach effectively. There are restrictions on the types of personal information AI can obtain and retain. As of right now, it is difficult to translate relevant past interactions into useful, limited memory.
- **Non-Verbal Communication**: Human tutors use non-verbal cues (facial expressions, body language, and tone of voice) to gauge a learner's attention, frustration, or enthusiasm, and adjust their teaching accordingly. In a chat environment, AI models cannot replicate this.
- **Multi-Modal Interaction**: Effective human tutoring often involves multi-modal interactions - working together on a diagram, manipulating objects, or writing on the same surface. While AI models are beginning to develop these capabilities, seamless interaction across different modalities is still in its infancy (see GPT-4o and Project Astra!)
- **Empirical Evidence on Actual Learning Outcomes**: While the paper discusses improvements in pedagogical capabilities through LearnLM, it would be helpful to understand statistically significant improvements in student performance.

### Key Takeaways:

- Creating an effective AI tutor is tricky because **we don't have great ways to measure if the AI is really helping students learn better**. We need to develop better, standardized ways to measure how well AI tutors teach. **There's still a lot to do!**
- **Human tutoring data is scarce**. It often suffers from limitations: a lack of grounding information, low tutoring quality, small dataset size, and noisy classroom transcriptions. In the absence of this, the researchers leveraged varied datasets of human tutoring data, gen AI role-play data, GSM8k dialogue, golden conversations and safety data.
- Prompting can go a long way, but **base models (Gemini, ChatGPT, Claude, etc) are not optimized for teaching.** Base models tend to optimize for single responses without follow-up questions, give answers too quickly, provide overwhelming information-dense responses, and agree with learners too readily,
- While human evaluations are the gold standard, they are also time-consuming and hard to scale. **The researchers custom-built LMEs (Language Model Evaluations) - essentially AIs to evaluate AI - to assess LearnLM’s pedagogical performance.** LMEs can potentially **enable more automated, scalable and consistent evaluations**, which are crucial for the ongoing development and assessment of AI educational tools.
- Human tutors excel in understanding real-world context and personalizing lessons based on individual learners. LearnLM, **as a non-embodied AI, lacks deep contextual awareness and the ability to fully personalize or interpret non-verbal communication**.
- Fine-tuning on models on educational data can yield positive results. They may be better than base models at **boosting learner confidence, promoting student engagement, and encouraging active learning**.
- At the same time, **improvements in pedagogical capabilities in a model ≠ statistically significant improvements in student performance**.

Is this a game-changing model that will massively transform learning outcomes compared to base models? No, not yet. Achieving truly transformative improvements in learning outcomes will likely require more sophisticated model architectures, larger and higher-quality training datasets, a deeper understanding of effective pedagogical strategies and more comprehensive testing.

However, it is indeed exciting to see Google take a deliberate approach to building education-specific models. These models will power a wide range of products across the Google ecosystem, impacting and touching millions of learners. It's a promising first step in the right direction!

## Microsoft and Khan Academy’s Phi-3 Models

*The companies will \[\] explore how [small language models (SLMs) such as Microsoft’s new Phi-3 family of models,](https://news.microsoft.com/source/features/ai/the-phi-3-small-language-models-with-big-potential/) which can perform well for simpler AI tasks and are more cost effective and easier to use than larger models, might help improve and scale AI tutoring tools. To that end, Khan Academy is collaborating with Microsoft to explore the development of new, open-source small language models based on Phi-3. The goal of the exploratory work is to enable state-of-the-art math tutoring capabilities in an affordable and scalable manner.*


**What are Small Language Models (SLMs)?**

Microsoft coined the term “small language model” (SLM) following their influential paper *[Textbooks Are All You Need](https://arxiv.org/pdf/2306.11644)* last year. The paper unveiled the first Phi model, a compact small language model that outperformed much larger alternatives, challenging the idea that model capabilities are tied to size and resources. Since then, many players have released advances in the SLM category: Apple’s OpenELM, Google’s RecurrentGemma, Allen Institute of AI’s OLMo, and more.

SLMs, like Phi-3, **offer many capabilities of larger models but in a smaller, more cost-effective**, and **user-friendly package**. They are **accessible to organizations with limited resources** and are **easier to use and deploy**.

**What will Khan Academy and Microsoft be doing with Phi-3?**

While there aren’t too many details available yet, it sounds like:

- Khan Academy will provide explanatory educational content like math problem questions, step-by-step answers, feedback, and benchmarking data.
- Since SLMs can process data locally on edge devices (phones and tablets vs the cloud), it can reduce latency for real-time interactions. This local processing may also enable effective use without a stable internet connection, increasing accessibility of how/where learners can access Khanmigo.
- Khan Academy is likely to use Phi-3 models to enhance Khanmigo, particularly for delivering math-related content. By leveraging Phi-3 models instead of more general LLMs, Khan Academy can achieve greater cost-efficiency and improved math tutoring capabilities.
- They are also working on building new features like feedback based on students' handwritten notes (more multimodality!)

**How is this different from what Google did in fine-tuning a model?** Let’s use an (extremely oversimplified) analogy of building a library vs. creating a personalized bookshelf:

- Imagine an LLM as a vast library with books on every subject. **Fine-tuning** this model is like renovating specific sections (modifying existing structure, adding specialized resources for students/teachers) to better cater to educational needs, requiring significant computing power and storage. It offers a wide range of information but can be complex to build and navigate.
- On the other hand, a **small language model** is like a curated bookshelf, tailored to specific educational needs. It’s efficient, streamlined, and precisely geared towards users, without the extensive searching needed in a large library.

Both approaches enhance education by providing more education-specific solutions to different needs, and are in many ways complementary.

LLMs→ comprehensive resources and versatility, suitable for broad educational applications.

SLMs → efficiency, accessibility, and focus, making them ideal for specific tasks and real-time applications, particularly in resource-constrained environments.

## ChatGPT Edu

Last week, OpenAI announced [ChatGPT Edu](https://openai.com/index/introducing-chatgpt-edu/) - a specialized version of ChatGPT designed for universities, enabling the responsible deployment of AI to students, faculty, researchers, and campus operations.

- Powered by GPT-4o, OpenAI's new flagship model with text interpretation, coding, mathematics, and vision reasoning
- Includes advanced tools for data analysis, web browsing, and document summarization
- Ability to build custom GPTs and share them within university workspaces
- Higher message limits, improved language capabilities
- Robust security, data privacy, and administrative controls such as group permissions, SSO, SCIM, and GPT management
- Conversations and data are not used to train OpenAI models

In this case, OpenAI hasn’t built a new model or fine-tuned an existing model. It’s really more of a specialized version of its enterprise offerings for higher ed institutions. It’s great to see OpenAI work with the academic community to officially develop education-specific offerings - we expect more to come!

## Conclusion

The recent advancements by Google, Microsoft, Khan Academy, and OpenAI illustrate the diverse strategies tech giants are employing to integrate AI into education:

- Google's LearnLM is one of the first comprehensive and interdisciplinary approaches to creating AI tutors from a major foundation model provider. Google has both sides of the equation: product AND distribution, and will continue to leverage this to maintain its commanding lead.
- Microsoft's partnership with Khan Academy to build small language models is an exciting initiative to develop more cost-effective and accessible AI solutions.
- ChatGPT Edu’s specialized version of its flagship model underscores OpenAI’s increasing commitment and interest in AI in education.

By exploring different methodologies — be it fine-tuning large models or developing small language models — each initiative contributes to a quickly evolving landscape of AI in education, building on the AI initiatives already being made by edtech startups and companies. While challenges remain, particularly in measuring real learning outcomes, these advancements do point us to better ways of understanding and improving teaching and learning with AI.

Very insightful read!

I write about humanizing the future of learning. I’ve been developing the Somagraphic Learning Framework to make education more inclusive.

🌸 I’d love your insights on my latest piece: How AI Learns from Shapes 🤖🌟

https://open.substack.com/pub/doodlesbydevika/p/how-ai-learns-from-shapes

This is actually great.
