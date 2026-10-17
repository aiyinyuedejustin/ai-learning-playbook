# r/Anki：用 AI 做卡的人能分享吗

- 链接：https://www.reddit.com/r/Anki/comments/1nbwwm3/for_those_who_use_ai_to_create_flashcards_could
- 作者：u/senivim（r/Anki，3 分，7 条评论）
- 获取方式：Reddit 帖子与评论全文（取自 Arctic Shift 公开存档）

---

## 帖子：For those who use AI to create flashcards, could you share a good prompt?

(i know that making my own flashcards may be more effective but I'm finding it faster for now using ai made flashcards, and then modify as i go). At times i get a good deck with well made flashcards but at times I feel the flashcards aren't of good quality. Any prompt that gave you good flashcards every time? 

## 评论（共收录 19 条，缩进表示回复层级）

**u/Danika_Dakika**（2 分）：
r/AnkiAi

**u/funbike**（2 分）：
General AI prompting advice:  Have AI generate the prompt for you.

In a prompt, supply 5 examples of your idea of good flashcards.  Then issue a prompt for more clarity such as:

```
The above are examples of good vocabulary flashcards.
Generate a list of questions you can ask me to determine why I consider that true.
```

Then give it your answers.  Then generate the final prompt:

```
Based on the above examples and Q&A, generate an LLM GPT prompt that will create good flashcards.  Include the examples in the prompt as few-shots.
```

You can use that prompt to create your cards.  This technique is how I write many of my prompts.

**u/Academic-Fox8128**（2 分）：
This one's an example of my go to.

Let S={w1,w2,...,wN}={}, where N is a finite positive integer and n in {1, 2, ..., N}. Construct a table as a CSV file (in plain text format with comma delimiters, quoted fields where necessary, and a header row), every row of which will correspond to wn from S. Make sure the words are in their plain form (singular, masculine, infinitive, unconjugated where applicable), followed by the one they are listed in written in parentheses if it's a variant (the plain form of the word becomes the base form of wn). The first column should be devoted to the proper wn; the second, should contain its Oxford dictionary definition in Czech; the third, phonetic pronunciation; the fourth, one contextual sentence in Czech (no longer than 15 words); the fifth, its etymology described in less than 30 words; the sixth, its translation into Lithuanian; the seventh, a contextual sentence in Lithuanian (not longer than 15 words); the eighth, pronunciation of the Lithuanian translation; the ninth, translation into French; the tenth, into Russian; the eleventh, a contextual sentence in Russian (not longer than 15 words); the twelfth, into English; the thirteenth, the name of the part of speech of wn (including grammatical gender and case where applicable).

**u/some-person-into-psy**（6 分）：
Here's one I've been using with good results (using GPT-5):

You are an expert at creating high-quality, durable, and efficient spaced-repetition flashcards. Your task is to take any provided content and convert it into Anki flashcards that maximize long-term retention and understanding.

Your flashcards must follow these principles:

1. Follow SuperMemo’s “20 Rules of Formulating Knowledge”
	•	Keep questions and answers simple, clear, and concise — one fact per card.
	•	Break down complex information into atomic facts.
	•	Use active recall and avoid recognition-only questions unless necessary.
	•	Avoid cloze deletions unless they make the card simpler and unambiguous.
	•	Use minimum information principle: include only as much as needed to answer.
	•	Make cards unambiguous — ensure the question has only one correct answer.
	•	Use context when needed so the meaning remains clear outside the original text.
	•	Avoid unnecessary or vague words; use precise, concrete language.
	•	Avoid “enumerations” — split lists into multiple cards.
	•	Use visuals only when they meaningfully support recall.

2. Apply Andy Matuschak’s principles
	•	Frame questions to prompt deep thinking and connection, not just rote recall.
	•	Where relevant, use “Why…?” or “How…?” questions to promote understanding.
	•	Avoid trivia in isolation — cards should connect to a bigger mental model.
	•	Make the answer mentally satisfying to recall — aim for an “aha” moment.
	•	For abstract concepts, use examples and contrasts.

3. Apply Control-Alt-Backspace’s “Precise” guidance
	•	Avoid overly broad or fuzzy prompts; make them specific and targeted.
	•	Ensure questions test only one thing at a time.
	•	Anticipate common wrong answers and adjust wording to avoid ambiguity.
	•	Optimize for recall speed — the card should be answerable in 5–10 seconds.
	•	For concepts that are similar or confusable, differentiate explicitly in the question.

4. Formatting
	•	Output as a list of cards in this format:
Q: [Question]
A: [Answer]

•	No numbering unless the user requests it.
	•	Keep the language simple and clear — aim for someone with no prior context being able to answer with study.

5. Your Process
	1.	Parse the content to identify the core facts, relationships, and principles.
	2.	Break down into atomic, precise recall prompts.
	3.	Eliminate redundancy and merge overlapping cards.
	4.	Rewrite in clear, specific, unambiguous language.
	5.	Test yourself: Would the question still make sense in isolation? Does it have exactly one correct answer?

⸻

Example

Content: “In classical conditioning, extinction occurs when a conditioned stimulus is presented repeatedly without the unconditioned stimulus, leading to a decrease in the conditioned response.”

Q: In classical conditioning, what happens during extinction?
A: The conditioned stimulus is presented repeatedly without the unconditioned stimulus, leading to a decrease in the conditioned response.

Q: What causes the conditioned response to decrease during extinction in classical conditioning?
A: Repeated presentation of the conditioned stimulus without the unconditioned stimulus.

Now, take the provided content and generate the highest-quality Anki flashcards possible, following the rules above.

> **u/Shot-Respond-8904**（-1 分）：
> Hey, this is a super common problem with using general AI for flashcards. Getting the prompt just right is a huge hassle, and the quality can be really inconsistent, just like you said.
> 
> I'm the developer of a web app called NoteDeck, which I built to solve this exact issue.
> 
> The whole idea is that instead of you needing to perfect a prompt, the app has a pre-optimized system for analyzing your notes (PDFs, text, etc.) and generating high-quality cards automatically. It handles all the complex prompting in the background so you can get consistent results without the trial and error.
> 
> There's a free tier so you can see if the quality works for your needs. You can check it out here:
> [NoteDeck](https://note-deck.vercel.app)
> 
> Hope this helps!

> **u/DoodlePope**（2 分）：
> Damn, I'm using this from now on. Thanks

> **u/studymaxxer**（2 分）：
> I LOVE YOU

> **u/Dependent_Nebula_417**（2 分）：
> I dont usually comment but I just came back to let you know this is by far the best prompt I've come across. I've been trying to prompt engineer for anki for a couple days and haven't been able to get the desired outcome so you are a life saver!!

> **u/BreadfruitNo1731**（1 分）：
> Thank you

> **u/Vast-Cod2606**（1 分）：
> Gasss

**u/BetoMatt**（1 分）：
I like it simple. 

1. Make concise and easy to study notes from this document/text. (Then active recall)

2. Please create short answer questions with answers based on this content.

3. Please create multiple choice questions, best of 5 answers, on the same content

**u/DangerousDementus**（1 分）：
You are an expert, skilled and superlative English Language Teaching (ELT) specialist with exceptional and effective written communication skills. Your methodology focuses on teaching vocabulary within a rich, meaningful context. You are specifically tasked with creating a detailed vocabulary lesson for an intermediate (B1) English student from Brazil.
Provide the meaning and definition of the word “{{word}}” within the context of the sentence: “{{sentence}}”. 
Carefully analyze the given sentence so that you correctly identify the context in which the word is being used. Analyze the provided word within the context of the sentence and generate a detailed vocabulary guide. Provide a comprehensive, context-aware, and didactic analysis of the English word, based on its usage in the provided sentence. The entire output must be in English. If the word has more than one definition or has more than one meaning in different contexts, be specific and provide only the meaning and definition related to the provided sentence and context. 
Provide 7 high-quality sentences and usage examples of the word. These sentences must all use the word in the same context you identified. Ensure the sentences demonstrate a natural use of the word. Prioritize and use the following online dictionaries, sources, and resources: Oxford English Dictionary (OED): [https://www.oed.com]; Oxford Learner's Dictionaries: [https://www.oxfordlearnersdictionaries.com]; Cambridge Dictionary: [https://dictionary.cambridge.org]; Collins Dictionary: [https://www.collinsdictionary.com]; Merriam-Webster: [https://www.merriam-webster.com]; Longman Dictionary of Contemporary English (LDOCE): [https://www.ldoceonline.com]; Macmillan Dictionary: [https://www.macmillanenglish.com]; Dictionary.com: [https://www.dictionary.com]; Sentence Stack: [https://sentencestack.com]. 
Output: Write the word in its basic form, using the original root word (e.g., “Undermine”, not “Undermining” or “Undermined”) with a “[]” beside which will contain inside what part of speech the word is (e.g., noun, verb, adjective, adverb, conjunction, etc.). In the next lines, write the sentences and usage examples. Next, write the meaning and definition of the word provided by all the dictionaries, sources, and resources. Next, summarize and explain the meaning and definition of the word in a didactical way for a foreign English student from Brazil using English only, without Portuguese words. Finally, write the best and most commonly used 3-5 synonyms of the word that are appropriate for the specific context.
{{word}}:
{{sentence}}:

**u/DoodlePope**（1 分）：
"create as many as you deem fit basic anki flashcards which i can directly paste in a text document to import into Anki. Make sure to include all formulas shown in the text as cards"

**u/valvze**（1 分）：
[Neobloc](https://neobloc.org) should take care of you :) Really simple to use and pretty powerful.

> **u/Strange-Research6662**（1 分）：
> yeah ! And only a coffee's price a month ! 

**u/SpinelessLinus**（1 分）：
I'm developing [https://studycardsai.com/](https://studycardsai.com/) \- you can try it for free (no credit card) and I would really appreciate any feedback.

Upload a PDF, wait for flashcards, import directly into Anki. You can review directly on the platform as well!

**u/green-hairs**（1 分）：
That's why CardSnap flashcards generator exists, so you don't loose time with the prompts and formating.

**u/Ok_Gain4340**（1 分）：
If you want speed, rather than making them using AI, a flashcard generator app would be better. saves you the import/export hassle as well as the prompt engineering hassle. I use one called [clozemd.com](http://clozemd.com) which is made specifically for med. saves loads of time.

**u/Hour-Chest8654**（1 分）：
I have been using claudefree for anki card generation and it is giving me great results but due to usage limits the speed is dramatically slow is there a way to solve this 

