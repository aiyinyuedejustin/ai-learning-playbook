# r/Anki：最高效的制卡方式

- 链接：https://www.reddit.com/r/Anki/comments/1hov0v9/what_is_the_most_efficient_and_fast_way_to_make/
- 作者：u/alixyazdan（r/Anki，3 分，18 条评论）
- 获取方式：Reddit 帖子与评论全文（取自 Arctic Shift 公开存档）

---

## 帖子：What is the most efficient and fast way to make anki flashcards using ChatGPT?

Hi! Im making flashcards and i need to make them quick. for my syllabus, I have plenty of docs and I need to turn them into flashcards. Ive been using chatgpt to speed up the process but its more like me copy pasting section from the document and then pasting into an excel file and then importing it. And one thing I have to note is that I don't know if chatgpt is making the relevant and efficient flashcards or not.

i was wondering if anyone had a better suggestion, can I upload a file into chatgpt and it automatically make flashcards without skipping or duplicating the material? is there a better option?

  
thanks!

## 评论（共收录 24 条，缩进表示回复层级）

**u/Primary-Concern-1550**（3 分）：
try asking chat gpt to make flashcards in csv file which can directly be imported in anki

> **u/rainbowcarpincho**（1 分）：
> Commas aren't great delimiters, honestly, because you can't have any commas in your cards (?). You can pick any character going out of Chatgpt and again going into Anki.I think I used pipe | last time.

> > **u/lebrumar**（1 分）：
> > Asking it to use quotes to enclose text makes this kind of issues less prevalent

> > **u/Danika_Dakika**（3 分）：
> > Not quite just "any character" -- but there is a good selection of field separators available. [https://docs.ankiweb.net/importing/text-files.html#file-headers](https://docs.ankiweb.net/importing/text-files.html#file-headers)

**u/rainbowcarpincho**（13 分）：
You'll have to throw out a bunch manually; chatgpt can't tell a good card from a bad card, so you'll have to know the source material well enough to judge that. Learn the material FIRST, then quiz it with Anki.

**u/j3llyfinch**（0 分）：
it depends on what ur needs are, but w the free version of chatgpt, you can't rely on it to read your document accurately. seems like you've already experienced this, but it generally skip parts—and, if u try to circumvent this by saying, like, "make 75 cards," it'll just start duplicating content. 

i've found it MOST useful for things like refining my flashcards or breaking them into smaller details if i’m struggling with that. it’s also great for generating a large number of simple flashcards that follow the same format, like: “what is the name of cranial nerve \_\_\_\_\_?” / “what is the sensory innervation of cranial nerve \_\_\_\_\_?” i do need to provide the format to start with, though. and you CAN give it some creative freedom within reason. for example: when making cards about muscles, i'd say something like: when possible, make grouped cards for connected concepts instead of individual cards, like this: "all the muscles of the \[compartment\] of the \[region\] are innervated by \_\_\_\_\_, except for \_\_\_\_\_\_\_ (innervation: \_\_\_\_\_\_)" since that grouping works well for developing a big picture understanding of the concepts. so it doesn't hurt to use it to automate things once you've figured out your card approach, but be clear about how you want the cards formatted. 

and, ofc, if you have the time, writing the cards urself IS better

> **u/alixyazdan**（1 分）：
> thank you so much! will try that.   
> I was gonna write but just for one course I have around 6-8 PDFs with an average of 10 pages lol

**u/chillzaza**（0 分）：
I made an app for this! Try it out and let me know what you think: https://generateflashcards.vercel.app/

> **u/jeboteuusta**（2 分）：
> Can we add pdfs?

> > **u/chillzaza**（1 分）：
> > Working on PDF and image support! In the meantime, try copying and pasting from a PDF to see how it performs.

> > > **u/alixyazdan**（1 分）：
> > > how good is this? i see youre the developer, I would appreciate honest input regarding this :)

**u/Shige-yuki**（2 分）：
Basically AI add-ons and tools are paid for and each tool has different usage, so I think there is not much useful advice for creating cards with AI. (There are few users and many are just advertisements.)

**u/SCro_1**（5 分）：
For many months I tried to craft a prompt that could do this. I found out that chatgpt was not following exactly the instructions I would give it. This before o1 came out (yes I have the plus plan). Thanks to CoT now it does what i want. o1 does not have the possibility to upload pdfs yet so I usually convert the pdf into txt and then copy it and then put it into the following prompt: 

Role: You are an expert psychology tutor specializing in explaining concepts clearly and thoroughly, adhering to the 20 Rules of Knowledge Formulation.
Context:
Degree: Psychology
Course/Topic: [Specify the course name or topic, e.g., “Abnormal Psychology,” “Cognitive Development,” “Behavioral Neuroscience”]
Level: [Undergraduate, Graduate, etc.]
Task Part 1: Extended Summary
Provide a comprehensive summary of the following text, covering all major concepts and themes related to the specified course/topic.
Target Length: [Specify word range based on extract length; e.g., 500–800 words]
Guidelines:
Ensure clarity and logical structure
Use language appropriate to the specified academic level
Highlight connections to broader course objectives or themes
Task Part 2: Flashcards
Number of Flashcards: [Determine based on extract length and complexity; e.g., 30–50 for dense texts]
Content Requirements:
Each flashcard must focus on a single concept, definition, or application
Include examples or real-world applications relevant to the course/topic
Use clear and direct language
Ensure each flashcard is self-contained
Avoid combining multiple ideas in one flashcard
Instructions:
Summarize the entire text comprehensively and coherently
Create flashcards that encapsulate definitions, key theories, examples, and practical implications
Adhere strictly to the 20 Rules of Knowledge Formulation
Ensure alignment with the specified course/topic and academic level
Input Text (Extract):
[Paste or attach the relevant text here]
Output Requirements:
Clearly separate the extended summary from the flashcards
Ensure both components are tailored to the specified course/topic and academic level
Maintain adherence to the 20 Rules of Knowledge Formulation

This prompt creates also a summary about the content that you paste and focuses on the famous 20 rules of formulation which I find very useful as rules of thumb. I study psychology but you can change it based on preference. As you can see, you have to specificy the length of the summary and the numer of flashcards. This is because YOU STILL HAVE TO HAVE UNDERSTOOD THE TOPIC BEFORE MAKING FLASHCARDS. By then you know how much the content is dense and you can use this tool tweaking the parameters.

> **u/SCro_1**（1 分）：
> As for putting the flashcards to Anki, once you are satified with the flashcards (for me, I rarely have to change something) you can just ask to rewrite the flashcards in a manner importable to anki like it was a .txt file. Not difficult at all.

> **u/Latter-Plant-7324**（1 分）：
> what is CoT

> > **u/SCro_1**（1 分）：
> > It’s how o1 reasons, “Chain Of Thought”: Chain of thought prompting is an approach in artificial intelligence that simulates human-like reasoning processes by delineating complex tasks into a sequence of logical steps towards a final resolution (formulated by people much more expert than me). It’s like a much more complex “do it step by step”

**u/ThrillHouseofMirth**（1 分）：
Ask chatgpt what the best way to do it is.

**u/EgertonYorrickDavis**（1 分）：
I found a way that worked for me and had the opportunity to document it for some colleagues. Here’s what I’ve been doing:

Use a text as the basis for creating flashcards. The text can come from any reliable source, such as books, articles, or guidelines. Carefully reading the text will also aid in personal study, making this step valuable for learning and revision.

Use the ChatGPT tool to create flashcards based on your text:

1. Break the text into small sections containing a few paragraphs. This makes it easier for GPT to create specific flashcards.
2. Once the flashcards are generated, review them, discarding unnecessary or repeated ones, and editing as needed.
3. Continue sending the remaining text so the flashcards cover the entire content. This process takes time, but I see it as a positive: it’s still faster than creating cards from scratch, and it makes the creation process another opportunity to study and review the material you want to recall later.

Here’s my suggested prompt for ChatGPT:
'Based on the text I will send, and only after I send it, I want you to create concise flashcards. The purpose of these flashcards is to assist with [specify your purpose, e.g., personal study, teaching, certification exams]. Create 20-30 flashcards per text provided. Follow these instructions for the flashcards:

1. Write the content for the "front," followed by the "back."
2. If the card is true or false, write "V ou F."
3. If the card involves a fill-in-the-blank, hide the content with "(...)" and reveal it on the back.
4. The flashcards should follow this format:

Front:
Front content
Back:
Back content
(optional, a concise comment explaining the flashcard)'

Have a great success in your studies!

> **u/alixyazdan**（2 分）：
> Thank you so much! Really appreciate this!

**u/mgamal96**（1 分）：
The common generators that export to anki are

Dekki.ai
Pdf2Anki
Paperclips

Ps. I made dekki

> **u/alixyazdan**（1 分）：
> ill try it out, thanks!

**u/Bilz_**（1 分）：
this prompt:

Review Text: ""



Task: Your task is to convert this text into Basic Note Type (front/back) Anki flashcards. Prioritize information regarding the imaging features of diseases, unique imaging findings, and methods of differentiating similar disease entities. Ensure that each flashcard is clearly written, and adheres to the specified formatting and reference criteria.



Formatting Criteria:



\- Construct a table with three columns: "Front", “Back”, "Number".

\- Each row of the "Front" column should contain a single question testing the imaging features of disease, unique imaging findings, and methods of differentiating similar disease entities.

\- The “Back” column should contain the succinct answer to the question in the corresponding row of the “Front” column.

\- The "Number" column will serve to number each row, facilitating feedback.



Reference Criteria for each "Statement":



\- Each flashcard should test a single concept

\- Limit the word count of each question to less than 40 words.

\- Each flashcard MUST be able to stand alone. Include the subject of the flashcard somewhere in the text.

\- Keep ONLY simple, direct questions in the "Front" column.



Example:

| Front | Back | Number |

| --- | --- | --- |

Ill-formulated knowledge – Complex and wordy(you should not do cards like them)

|  What are the characteristics of the Dead Sea?| Salt lake located on the border between Israel and Jordan. Its shoreline is the lowest point on the Earth’s surface, averaging 396 m below sea level. It is 74 km long. It is seven times as salty (30% by volume) as the ocean. Its density keeps swimmers afloat. Only simple organisms can live in its saline waters | 1 |

Well-formulated knowledge – Simple and specific(you should do cards like them)

|Where is the Dead Sea located?? |on the border between Israel and Jordan | 1 |

| What is the lowest point on the Earth’s surface?| The Dead Sea shoreline| 2 |

| What is the average level on which the Dead Sea is located?| 400 meters (below sea level). | 3 |

| How long is the Dead Sea?? | 70 km| 4 |

| How much saltier is the Dead Sea than the oceans? | 7 times | 5 |

| What is the volume content of salt in the Dead Sea?| 30% | 6 |

| Why can the Dead Sea keep swimmers afloat? due to high salt content | 7 |

| Why is the Dead Sea called Dead? | because only simple organisms can live in it. | 8 |

| Why only simple organisms can live in the Dead Sea? | because of high salt content| 9 |

 

> **u/Bilz_**（1 分）：
> you can paste the result into  excel then save the file as csv and thats it.

**u/yTKONOSINA**（1 分）：
Stumbled on this app called FlashMind ([https://flashmind.fly.dev](https://flashmind.fly.dev)) and I’ve actually been enjoying it a lot. You just upload a file or even a photo of your notes, and it uses AI to turn everything into flashcards. It’s been super helpful for getting info to stick without spending hours making cards. Thought I’d share in case it helps someone else too!

