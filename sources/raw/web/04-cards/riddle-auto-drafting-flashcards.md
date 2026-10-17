# riddle.press：自动起草闪卡

- 链接：https://riddle.press/auto-drafting-flashcards/
- 作者：The Riddle Team
- 获取方式：网页正文（trafilatura 提取）

---

[Tools for Thought](https://riddle.press/tag/tools-for-thought/)

# Auto-drafting reading flashcards with Readwise Reader and Obsidian

Takeaways from your Readwise readings, auto-drafted into flashcards that sync to Anki through Obsidian.

*This workflow was previously featured in the Riddle Fortnightly, but seemed chunky enough to merit its own article.*

A few years ago, pre-ChatGPT, a collective called [Psionica](https://github.com/Psionica?ref=riddle.press) sought to spark an upgrade in human learning with something called [‘Autocards’](https://github.com/paulbricman/autocards?ref=riddle.press). The premise was simple. We read things every day; we remember vanishingly little. Flashcards, and particularly spaced repetition, are an unreasonably effective means of committing things to long term memory, requiring only a handful of minutes per card, spread out over years. But taking the time to write cards is a huge bottleneck. Autocards, the dream was, would create Anki-ready flashcards *for* you, providing at least a first draft to be refined.

Being pre-ChatGPT, Autocards never worked very well, and Psionica eventually dissolved. (I believe it used a GPT-2 era BERT model.) But the idea remained, and has been implemented in a few places, like RemNote, and a hodgepodge of Obsidian plugins like [“Auto Anki”](https://github.com/cadrianxyz/obsidian-auto-anki?ref=riddle.press), [“QuizCraft”](obsidian://show-plugin?id=flashcard-gen), and [“Quiz Generator”](obsidian://show-plugin?id=quiz-generator).[\[1\]](#fn1)

I recently tried to recreate this myself, using the existing AI features of two ubiquitous tools for thought: [Readwise Reader](read.readwise.io) and [Obsidian](obsidian.md). Readwise, a read-it-later tool, has an OpenAI-powered “Ghostreader” that can be prompted with context from your reading material and highlights. And Obsidian has a number of plugins for extracting and syncing flashcards between markdown and Anki. Hence the very simple idea behind this automation: ask the Ghostreader to write flashcards in a markdown format usable by Obsidian’s plugins, where they can be synced to Anki. Voila!

Were it that easy, it would hardly merit description, except to exude at how easy formerly magical technological acts have become. As it turns out, there were a few subtleties worth documenting.

First, I used the plugin [Obsidian\_to\_Anki](https://github.com/ObsidianToAnki/Obsidian_to_Anki/wiki?ref=riddle.press#current-features) with the Q: and A: format to extract flashcards from my Obsidian notes. Markdown flashcards look like this:

```
Q: How long do Riddlers live? #flashcard 
A: They are immortal.
```
After a bit of configuration described in their docs, you can sync these cards to Anki by running a command in Obsidian. I recommend changing the plugin’s default settings to automatically sync cards to Anki once daily.

I then configured Readwise's Ghostreader to create highlights in that format, by creating a custom prompt called in Reader’s settings (Go to Preferences -> Preferences -> Ghostreader Prompts). I called it ‘Draft Flashcards’.

These prompts can use the Jinja2 templating language to dynamically insert document content, your highlights from it, and details like the document title and author name. While testing this, I made a few refinements to discourage vague questions and nebulous references to ‘the document’ – but you can refine this to your needs.

```
As a teacher and mentor, you are preparing a set of flashcards for a student based off of the following text,  {{ document.title }}. To most effectively engage the student,  you are also reviewing his highlights in the document. You will then prepare a set of flashcards to help him remember the key ideas from his highlights.
Below is the full document text:
"""
{% if (document.content | num_tokens) > 25000 %}
    {{ document.html | central_paragraphs | join('\n\n') }}
    {% elif (document.content | num_tokens) > 2500 %}
    {{ document.content | central_sentences | join('\n\n') }}
    {% else %}
    {{ document.content }}
    {% endif %}
"""
And here are the student’s highlights from this document.
""" 
{% for highlight in highlights %} {{ highlight.content }} {{ "\n\n" }} {% endfor %} 
"""
Please write at least four but possibly many more sets of questions and answers that extract the key ideas and most relevant details from the document, paying special attention to the student’s highlights. Try to create roughly one question per highlight. For example, if one of the student’s highlights is a factual statement, one question-answer pair should rephrase the fact into a question and provide the answer. You may also use the context surrounding each highlight to provide the best questions possible. 
Your questions should elucidate the most unexpected and useful information from the document. There should only be one idea per question, following Andy Matushak’s advice on creating flashcards. Avoid vague questions like "what did X say about Y" -- instead, give some detail and ask for more, or for the reasoning behind it. Avoid references to 'the document', or asking about the context of something with respect to the document, as the student will use these flashcards separately from the original source. If you want to refer to the document in the question or answer, use its title, "{{ document.title }}". Similarly, always refer to the author as {{ document.author }}. Above all, make the questions and answers beautiful.
Your questions and answers should be provided in the below format, with three blank lines between question sets.
Q: Question Here #flashcard
A: Short answer here.
{% if document.note %}
Do not repeat information or questions in the student's own notes, which are below:
"""{{ document.note }}"""
{% endif %}
Again, please provide roughly one question-answer pair per highlight.
```
This works beautifully with GPT-4o, and inserts flashcard-formatted chunks of markdown in Readwise’s document note.

From here, you can sync this note (along with your highlights) into your Obsidian vault with the [Readwise Obsidian plugin](https://docs.readwise.io/readwise/docs/exporting-highlights/obsidian?ref=riddle.press). However, there are two things you’ll have to configure for that to work properly:

First, once the Readwise plugin has synced an article’s highlights to Obsidian, it will only ever *append* to that file afterwards. That means that if you lazily highlighted some document over the course of an hour, during which time a Readwise-Obsidian sync occurred — and *then* you ran Ghostreader and created our draft flashcards, they won’t sync. The document note will only sync if it’s present when the plugin first conducts the sync.

To combat this, change the plugin setting (Obsidian -> Settings -> Readwise Official -> Configure resync frequency) to 24 hrs.

The second problem is that the Readwise plugin somehow mangles the formatting of the document note when importing it to Obsidian, removing newlines. Without them, `Obsidian_to_anki` doesn't properly detect the flashcards.

To fix this, visit the plugin's formatting settings (with the Obsidian command "Readwise Official: Customize formatting"), and replace the text `{{document_note}}`, wherever it appears, with the following script, which will scan for lines beginning in `A:` and add a newline to the end.

```
{% set notes = document_note or '' %}{% for line in notes.split('\n') %}{{ line }} 
{% if 'A:' in line %}{{ '\n' }}{% endif %}{% endfor %}
```
Finally, let’s see this workflow in action! Seated with your biscuits and E-ink tablet, you peruse an article in Readwise Reader and make some highlights. After finishing the piece, you reflect that it had good quality; you’d like to remember it.

To draft a set of flashcards, [activate Ghostreader](https://docs.readwise.io/reader/guides/ghostreader/overview?ref=riddle.press), click on your custom prompt – and, after a few seconds of an animated ghost bobbing up and down, something like the following will be appended to your document note.

```
Q: What is the significance of the phrase "palace of crystal" in Dostoyevsky's philosophy? #flashcard 
A: The "palace of crystal" represents the counterfeit offerings of the world that sedate us and strip us of our humanity, contrasting the value of facing life's real struggles.
...
```
From there, it will migrate to the corresponding literature note in Obsidian. There, you can spiff up the flashcard – sharpening the question and refining the answer as appropriate – or, if it doesn’t seem worth remembering, you can just delete it.

But if it does, now you have it on an express route to your long-term memory.

1. Why not just use one of these? In Readwise Reader, you can give the LLM access to the full text content of your reading, not just your highlights, which might help it draft good questions without requiring you to obsessively highlight every relevant detail. [↩︎](#fnref1)
