# Dafi：用 ChatGPT 和 Claude 学习

- 链接：https://www.dafi-ai.com/en/blog/how-to-use-chatgpt-and-claude-to-study
- 作者：Evan Sende
- 获取方式：网页正文（trafilatura 提取）

---

AI assistants can explain, quiz you and find the gaps in your understanding, or they can quietly do your thinking for you. Here is how to use ChatGPT and Claude as a study partner grounded in your own course material.

ChatGPT and Claude can make you a much better student or a much weaker one. The difference is not the tool; it is whether the AI does the thinking or makes you do it.

**Short answer:** to study with an AI assistant, give it your actual course material, ask it to explain, question you and find your gaps rather than produce answers, and always check what it says against your notes. Used that way, it is a patient tutor available at 2 a.m. Used as an answer machine, it gives you the feeling of understanding without the understanding.

## Problem 1: generic answers that don't match your course

A general assistant answers from general knowledge. Your exam, however, is based on what your professor said: their definitions, their examples, the authors they chose, the method they expect. A textbook-correct answer can still lose points if it ignores the framework seen in class.

The fix is grounding: give the assistant your material before asking. Paste a section of your notes, upload the slides, or connect it to your notes directly (more on that below). Then say it explicitly: "Answer only from this material. If something is not in it, tell me."

## Problem 2: fluency is not learning

Reading a clear AI explanation feels like understanding. It is not the same as being able to explain it yourself on an exam. Research on learning consistently favours retrieval, meaning pulling information out of your memory, over rereading. So the best prompts make *you* produce something.

## Prompts that make you think

**Explain, then check me**

Explain \[concept\] from my notes in simple terms, with one example from the course. Then ask me to explain it back in my own words and tell me what I got wrong or left out.

**Quiz me, one question at a time**

Using only my notes on \[chapter\], ask me 10 questions, one at a time. Wait for my answer before the next one. Mix definitions, applications and "why" questions. At the end, list the topics I struggled with.

**Find my gaps**

Here is my summary of \[topic\]. Compared to the lecture notes, what is missing, wrong or too vague?

**Past exam practice**

Here is a past exam question. Don't answer it. Give me a hint about the approach, then grade my answer against the notes.

**Make it concrete**

Give me three situations where \[principle\] applies and one where it doesn't, and explain the difference.

For more on building quizzes from your notes, see [how to turn your course notes into practice exams](/en/blog/turn-course-notes-into-practice-exams-ai).

## Academic integrity: where the line is

Rules vary by university and by course, so read your course outline, and ask your professor when it is unclear. A safe principle: using AI to understand, practise and get feedback is studying; submitting AI-generated work as your own is not. In practice:

- Using AI to explain a concept or quiz you before an exam is generally fine.
- Using AI to write an essay, a lab report or a take-home exam you submit is generally not, unless explicitly allowed.
- When AI use is allowed in an assignment, many courses require you to say how you used it.
- AI can be confidently wrong. Check facts, citations and formulas against your course material.

## Connect your DAFi notes to ChatGPT or Claude

Copy-pasting notes into every conversation gets old fast. **DAFi** has an MCP connector (MCP, the Model Context Protocol, is the standard these assistants use to connect to external tools) so that the assistant you already use can work from your DAFi courses and notes.

How it works:

1. In DAFi on the web, open the AI connection page (from the Chat section or your account) and copy the DAFi MCP address.
2. **Claude:** on claude.ai, go to Settings › Connectors, choose "Add custom connector", name it DAFi and paste the address.
3. **ChatGPT:** on chatgpt.com, go to Settings › Apps › Advanced settings, turn on developer mode, then create an app named DAFi with the address. Availability depends on your ChatGPT plan.
4. Select "Connect" and sign in with your DAFi account to allow access.

Once connected, the assistant can use your courses and notes to answer. You can ask things like "Explain what my professor said about civil liability", "Make a quiz on this week's lectures" or "Sum up my week". You can see your connections in DAFi and disconnect an assistant at any time. The access is focused on reading: your courses, notes, upcoming exam dates and quiz results. DAFi also works on its own: your lectures become notes, summaries, flashcards and quizzes.

## A study session with an AI assistant, step by step

1. **Retrieve first (10 min):** without any help, write what you remember about the topic.
2. **Compare (5 min):** ask the assistant to compare your recall with your notes and list what you missed.
3. **Understand (15 min):** ask for explanations only on the gaps, grounded in your notes.
4. **Test (15 min):** get quizzed one question at a time.
5. **Log (5 min):** write the two or three points still weak and review them in two days.

The assistant never replaces steps 1 and 4. They are where the learning happens. Everything else, AI can speed up.

Lead front-end engineer and mobile contributor at Dafi. Building tools that make studying less painful and more effective.
