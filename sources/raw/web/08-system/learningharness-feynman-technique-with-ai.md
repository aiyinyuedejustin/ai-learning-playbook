# Learning Harness：费曼学习法加 AI（次日讲回）

- 链接：https://learningharness.org/feynman-technique-with-ai
- 作者：Ojasvi Yadav
- 获取方式：网页正文（trafilatura 提取）

---

# The Feynman technique with AI: explain it back the next day

The Feynman technique becomes a measurement when an AI grader holds the lesson you read and marks the explanation you give a day later.

The Feynman technique asks you to explain a concept in plain words, find the point where your explanation breaks, go back to the source, and say it again more simply. With AI it becomes an explain-back. You give the explanation, and a grader marks it against the lesson you read.

Two things decide whether it works. The explanation belongs on the day after the lesson, because retrieval beats rereading only once time has passed. A night of sleep consolidates the material first. The grader needs the lesson text and a rubric, so it marks the mechanism rather than your fluency.

## The Feynman technique with AI grades your next-day explain-back against the lesson

With AI, the Feynman technique runs as an explain-back. You read a lesson and you sleep. The next day you explain the concept in your own words, and a grader marks that explanation against the lesson it holds. Grading is the part AI adds. Someone running the technique alone has to notice their own gaps, which is the hardest step in it. A grader holding the source text names the step you left out of the mechanism, quotes the sentence you contradicted, and marks the concept as failed.

Timing is the second change. Most descriptions have you explain the material minutes after reading, while the sentences are still available to you. [Roediger and Karpicke (2006)](https://doi.org/10.1111/j.1467-9280.2006.01693.x) compared recall tests against restudying at 5 minutes, 2 days and 1 week. Restudying won at 5 minutes and lost at both later points. An explanation you give the next morning reports on what you kept, rather than on what still feels available. The rest of that argument is in [how to learn with AI](/learn-with-ai).

## What the Feynman technique is

The Feynman technique is a four-step loop for testing an explanation. First, you pick one concept and write its name at the top of a page. Second, you explain it in plain words, as though to someone who has never studied the field, using no term you cannot define. Third, you mark every place where the explanation goes vague, stalls, or falls back on the field's vocabulary. Then you go to the source and repair those places. Fourth, you simplify the repaired explanation and give it again.

The method is named after Richard Feynman because he was known for explaining physics in ordinary language. Feynman never published these four steps. Writers on study skills set them out later and attached his name to them, so treat the name as a label rather than a citation. The steps still work. Producing an explanation from memory forces you to find the parts you cannot produce. The technique locates the gap. Filling the gap needs the source material.

## Does the Feynman technique work?

The evidence supports the two operations inside the Feynman technique, and the technique under that name has not been trialed on its own. Explaining material to yourself is self-explanation, which [Dunlosky and colleagues (2013)](https://doi.org/10.1177/1529100612453266) rated moderate utility in their review of ten study techniques. Producing the explanation from memory is retrieval practice, which the same review rated high utility, alongside distributed practice.

[Karpicke and Blunt (2011)](https://doi.org/10.1126/science.1199327) had students study science texts and then either build concept maps or practice retrieval by writing down what they could recall. On a test one week later, the retrieval group scored 0.67 against 0.45 for concept mapping, about 50 percent better. Of the 120 students, 101 did better after retrieval practice. Three quarters of them had predicted that concept mapping would do at least as well. An explain-back runs both operations in one pass: you retrieve the concept, then you explain it.

The technique does not teach you anything. You cannot explain a mechanism nobody has shown you. The explain-back needs a lesson in front of it, and it measures what that lesson left behind.

## Why you should wait until the next day

An explanation you give minutes after reading measures what is still in short-term memory, so the same-session version of the technique scores you higher than a later test would. [Roediger and Karpicke (2006)](https://doi.org/10.1111/j.1467-9280.2006.01693.x) gave students prose passages, then had them either restudy the passage or take a recall test on it. The final test came after 5 minutes, 2 days or 1 week. At 5 minutes the restudy group won. At 2 days and at 1 week the tested group retained substantially more. The ranking of the two methods reverses somewhere between five minutes and two days. Restudying also raised the students' confidence, so the weaker method felt stronger while they used it. Judging a method on the day and judging it at the retest give opposite answers, which is the argument in [how to learn fast and remember it](/how-to-learn-fast).

Sleep is the second reason for the delay. [Diekelmann and Born (2010)](https://doi.org/10.1038/nrn2762) describe how declarative memories are reactivated and stabilized during slow-wave sleep. [Murre and Dros (2015)](https://doi.org/10.1371/journal.pone.0120644) replicated Ebbinghaus and found most forgetting inside the first hours and the first day. The curve probably shows a small upward step at 24 hours, which several authors attribute to sleep. The next-day explanation therefore reports on consolidated memory. The same-day quiz reports on something narrower and still worth knowing: whether the lesson landed at all.

The three checks in a study day measure different things.

| Check | Same-day quiz | Next-day explain-back | Spaced card review | 
|---|---|---|---|
| What it measures | Whether the lesson landed: the definitions, the numbers and the steps as written | Whether the mechanism survived a night, in your own words and in order | Whether one fact is still retrievable after a growing gap | 
| When it runs | Minutes after you read the lesson | The next day, before you reread anything | Days to months later, on a schedule set by your last answer | 
| What a fail triggers | The concept is taught again and tested again the next day | The concept is taught again from a different angle, then explained again the next day | The card comes back sooner, and a card that keeps failing points at a concept you never understood | 
| What a pass allows | The explain-back the next day | Cards for that concept enter the review queue | A longer gap before the next review | 

## What the grader needs to mark your explanation

The grader needs the lesson text, the list of concepts that lesson taught, and a rubric. Without them it marks fluency. A general chat model with no lesson in front of it can only judge whether your explanation sounds coherent. A confident wrong answer passes that test.

Give it four things to check on every concept. You have to state the mechanism, with the causal steps in the right order. You have to say where the concept stops applying. You have to carry the lesson's worked example through with the right numbers. You have to use the field's own terms the way the field uses them. Tell it to weigh mechanism above vocabulary, so plain words describing the right steps pass and a fluent recital of the right words fails. Tell it to withhold praise and to return one verdict per concept, pass or fail, with the missing step named.

Tell it to refuse to supply the answer while you are explaining. [Bastani and colleagues (2025)](https://doi.org/10.1073/pnas.2422633122) ran nearly 1,000 high-school students through a ChatGPT-like interface during math practice. Practice scores rose 48 percent, and scores on the later unassisted exam fell 17 percent against students who had no AI. A version prompted to give teacher-designed hints instead of answers raised practice scores 127 percent and left exam scores level with the control group. A grader that finishes your explanation for you produces the first result. The full set of requirements is in [what an AI tutor must do](/ai-tutor).

## A Feynman technique AI prompt you can paste

A workable prompt makes the model hold the lesson, wait a day, ask for your explanation, grade it against a rubric, and refuse to hand you the answer. Paste this into a new chat, then paste the lesson under it.

```
You are grading my understanding of a lesson, not teaching me.
Step 1, today. I will paste a lesson below. Read it and reply
only with a numbered list of the concepts it teaches, then
stop.
Step 2, tomorrow. I will send the word EXPLAIN. Ask me to
explain concept 1 in my own words, as if to someone who has
not read the lesson. One concept at a time. Do not show me the
lesson, do not hint, and do not finish a sentence I leave
unfinished.
Step 3. Grade each explanation against the lesson on four points.
  1 Mechanism: are the causal steps present, in the right order
  2 Limits: do I say where the concept stops applying
  3 Example: do I carry the lesson's worked example through
  4 Terms: do I use the field's terms correctly
Weigh mechanism above wording. Plain words with the right
steps pass. Correct jargon with a missing step fails.
Return, per concept: PASS or FAIL, the exact sentence where my
explanation first broke, and the one line from the lesson I
missed. Do not add praise, a summary, or encouragement. If I
ask for the answer, repeat the question.
```
Paste today's lesson, article or documentation page under the prompt, and close the window. Send EXPLAIN tomorrow, before you reread anything. If the model forgets between sessions, paste the lesson again above the word EXPLAIN without reading it first.

## What to do with a failed explanation

A failed explanation sends the concept back to teaching, and to a second explain-back the next day. Before you look anything up, write down the exact sentence where your explanation broke, in your own words. That sentence is the specification for the repair, because it names the step you cannot produce.

Then have the concept taught again from a different angle: a new worked example, a diagram of the same mechanism, smaller steps through the part that failed. Rereading the original text is the weakest option. Dunlosky and colleagues rated rereading and highlighting low utility, in the same review that rated practice testing high. That text has already failed once with you.

Test the repaired concept the next day with a fresh explain-back, and treat the second attempt as the result. Build [review cards](/spaced-repetition-with-ai) only after a concept passes. A card written on a misunderstanding rehearses the misunderstanding on a schedule.

The Learning Harness runs this loop after every lesson: a multiple-choice quiz on the day you read, an explain-back graded against the lesson the next day, and a concept that fails the explain-back re-taught on the spot and explained again the next day. See [the method](/method) for the rules in the order a learner meets them.

## Common questions

### How do I use the Feynman technique with AI?

Paste the lesson into a model and have it list the concepts the lesson teaches. Wait a day. Then have it ask you to explain each concept in your own words, with the lesson hidden from you. It grades what you say against the lesson on mechanism, limits, the worked example and terminology. Repair what fails, and explain it again the next day.

### Is the Feynman technique effective?

Its two components are effective. Producing an explanation from memory is retrieval practice, which Dunlosky and colleagues rated high utility in 2013. Explaining material to yourself is self-explanation, which the same review rated moderate. The technique under that name has not been trialed on its own. What decides the result is when you explain and who checks the explanation.

### What is a good Feynman technique AI prompt?

A good prompt does four things. It gives the model the lesson text to grade against. It delays your explanation to the following day. It fixes a rubric of mechanism, limits, worked example and terminology. It forbids hints, answers and praise. The prompt on this page does all four. A prompt without the lesson text grades your fluency.

### Feynman technique or active recall: which is better?

They overlap. Active recall, also called retrieval practice, means producing an answer from memory. The Feynman technique is retrieval practice with a constraint on the output: plain words, aimed at a listener who has not read the source. That constraint exposes gaps a one-line flashcard answer hides. Use cards for facts and the explain-back for mechanisms.

### How long should an explain-back be?

Long enough to state the mechanism as ordered steps, say where the concept stops applying, and carry the lesson's worked example through with the right numbers. For most concepts that runs to a couple of paragraphs. An explanation that runs longer than the part of the lesson it covers is usually narration of the text you read.

## Sources

1. Roediger, H. L., & Karpicke, J. D. (2006). *Test-Enhanced Learning: Taking Memory Tests Improves Long-Term Retention*. Psychological Science, 17(3), 249–255. [https://doi.org/10.1111/j.1467-9280.2006.01693.x](https://doi.org/10.1111/j.1467-9280.2006.01693.x)
2. Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). *Improving Students' Learning With Effective Learning Techniques*. Psychological Science in the Public Interest, 14(1), 4–58. [https://doi.org/10.1177/1529100612453266](https://doi.org/10.1177/1529100612453266)
3. Karpicke, J. D., & Blunt, J. R. (2011). *Retrieval Practice Produces More Learning than Elaborative Studying with Concept Mapping*. Science, 331(6018), 772–775. [https://doi.org/10.1126/science.1199327](https://doi.org/10.1126/science.1199327)
4. Diekelmann, S., & Born, J. (2010). *The memory function of sleep*. Nature Reviews Neuroscience, 11, 114–126. [https://doi.org/10.1038/nrn2762](https://doi.org/10.1038/nrn2762)
5. Murre, J. M. J., & Dros, J. (2015). *Replication and Analysis of Ebbinghaus' Forgetting Curve*. PLoS ONE, 10(7), e0120644. [https://doi.org/10.1371/journal.pone.0120644](https://doi.org/10.1371/journal.pone.0120644)
6. Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Mariman, R. (2025). *Generative AI without guardrails can harm learning*. Proceedings of the National Academy of Sciences. [https://doi.org/10.1073/pnas.2422633122](https://doi.org/10.1073/pnas.2422633122)

The Learning Harness is in a closed beta and not yet available.
