# Reddit r/PKMS：在 Obsidian 里用 GPT 真正学进去

- 链接：https://www.reddit.com/r/PKMS/comments/1nj4b22/how_ive_been_using_gpt_in_obsidian_to_actually/
- 作者：u/No-Trick5569（r/PKMS，14 分，4 条评论）
- 获取方式：Reddit 帖子与评论全文（取自 Arctic Shift 公开存档）

---

## 帖子：How I’ve Been Using GPT in Obsidian to Actually Learn, Not Just Collect Notes

I’ve been experimenting with combining GPT and Obsidian in my PKM setup, and it’s grown into something I haven’t really seen described anywhere else. Most of what I come across about AI in PKM is focused on plugins or auto-summaries. What I ended up building turned into more of a reflective learning system, so I figured I’d share.

# From questions to notes

Most of my notes don’t just capture information — they capture the process of learning. I write down the question I had, the confusion I went through, and how I eventually made sense of it.

Often this starts as a Q&A dialogue with GPT, where I get pushed, challenged, and sometimes corrected. The final note shows the wrong turns and the breakthrough moment, not just the polished answer. From there, I pull out evergreen notes and create flashcards, but only after curating so I don’t end up with piles of junk.

# From coach to study note

The step from Q&A dialogue to study note is where the system really shines. When a study note gets created, it doesn’t just sit there. GPT automatically looks inside a “note compendium” — a structured index of all my existing notes — to identify practical links and tags.

But these aren’t just blindly added. There are rules in place to avoid what I’d call “flimsy links” (connections that are technically possible but meaningless) and irrelevant tags that bloat the system. The linking and tagging only happens when it strengthens the knowledge graph and keeps everything coherent.

That means each new study note arrives not just with the content of my learning process, but also with curated connections to related ideas, all woven into the vault in a way that supports retrieval later on.

# Reflection loops

I also keep daily journals. GPT helps clean them up and summarize them, but the real value comes from what I call temporal reflection. It looks back over past entries and points out open loops or recurring themes. That’s been useful for spotting patterns I wouldn’t have noticed.

On top of that, I do 30-day reflections to get a broader perspective on where my focus has been and how it’s shifting.

# Vault access for GPT

The thing that really changed how this works is giving GPT access to my notes. Every time I open Obsidian, a script generates two files: one is a compiled version of all my notes in a format GPT can read easily, and the other is just a list of all note titles. Uploading them takes about half a minute.

This gives GPT a near up-to-date snapshot of my whole vault. It can remind me where I solved a problem, connect topics together, and reflect on themes across my writing. It feels less like asking a chatbot questions and more like talking to an assistant that actually knows my notes.

# Keeping GPT consistent (and within limits)

I ran into two separate issues and solved them in different ways:

* **Character/complexity limits:** I use a kernel–library setup to deal with the constraint of inline instructions. The kernel is a compact inline set with only the essential rules. The library is a larger, expanded file with modules for different contexts, and the kernel has anchors that point to those modules. This solves the practicality/length problem and lets the system scale without stuffing everything into the inline prompt.
* **Drift and inconsistency:** I reduced drift by writing the instructions themselves in a contract/programming-style way — explicit MUST/BAN rules, definitions, and modular sections that read more like an API spec than an essay. That shift in style (not the kernel–library structure) is what made the biggest difference in keeping GPT on-task and consistent.

# Coaching modules

On top of the core structure, I’ve set up different coaching modules that plug into the kernel–library system. Each one is designed for a different kind of learning or reflection:

* **Programming coach** – Guides me as a beginner in programming, asking Socratic questions, helping me debug, and making sure I learn actively instead of just getting answers.
* **Psychology coach** – Focused on reflection and discussing psychological topics, tying them back into personal habits, thought patterns, and self-understanding.
* **Project coach** – Walks me step by step through projects, using interactive prompts to help me learn the process of building something, not just the final result.

Because these modules are anchored in the library, I can switch contexts without losing consistency. GPT knows which “mode” it’s in, and the style of coaching adjusts to fit the situation.

# The whole engine

Right now the system works in layers:

* Q&A dialogues that become study notes
* Study notes that link and tag themselves through the compendium
* Evergreens distilled from those notes
* Curated flashcards for review
* Daily and monthly reflections
* GPT grounded in my vault for retrieval and connections
* Kernel–library for scale + contract/code style for consistency
* Coaching modules for different domains of learning and reflection

It’s not just a way to save more notes. It’s a way to actually learn from them, reflect on them, and reuse them over time.

# Why I’m sharing

I haven’t seen much in PKM spaces that goes beyond surface-level AI integrations. This ended up being something different, so I wanted to put it out there in case it sparks ideas. If anyone’s interested, I’m happy to go into more detail about the instruction system and the vault export.

## 评论（共收录 14 条，缩进表示回复层级）

**u/jezarnold**（2 分）：
This is great. Quick question 

> Every time I open Obsidian, a script generates two files: one is a compiled version of all my notes in a format GPT can read easily, and the other is just a list of all note titles. Uploading them takes about half a minute

**Any chance you can share your workflow here, and the script?** Are you using desktop ChatGPT, or linking via API to a local LLM? Have you simply enabled ChatGPT MD , vault chat or Smart Connect? 

Saved to digest more later.

> **u/No-Trick5569**（0 分）：
> I can it might take me a while to fully describe the workflow.  I'm using desktop chat gpt.  I upload the daily compendium and index in the custom GPT creator, I usually upload the extended\_instructions.md too because they are all in the same folder and it's easy.  I iterate a lot so it's usually worth it to make sure everything is up to date.  
> 
> There are 3 scripts for the creation of the index and compendium.   One makes sure the other 2 run every time I open my vault.  The other 2 actually create and format the files for easy GPT consumption.  They are naturally tailored to my own folder and note structure, so YMMV.
> 
> The kernel points to the extended instructions and the extended instructions has various modules that dictate how the GPT is supposed to interact with the index and compendium files.

> **u/No-Trick5569**（1 分）：
> The whole thing is built with Obsidian’s Templater plugin, not any external connector or live GPT access.
> 
> Here’s how it works. Every time I open Obsidian, Templater runs two commands. The first one builds the note compendium. That file is just all of my notes stitched together into a single document, with each note separated and marked by its title. The second command builds the note index, which is nothing more than a flat list of all note titles in the vault.
> 
> The compendium is what gives GPT the content of the vault. The index is what keeps the linking strict. GPT has to match a title exactly from that list in order to create a link, which keeps out “flimsy links” or guesses.
> 
> Once those two files are created, I upload them into ChatGPT along with my extended instruction file. The kernel is embedded in the inline instructions already, and I rarely change it. The extended instructions are modular and I update them frequently, so they get re-uploaded. Dropping all three files in at once is the easiest way to start a session.
> 
> I don’t use a local LLM, desktop ChatGPT, or Smart Connect. Just plain ChatGPT in the browser with Obsidian and Templater handling the exports.
> 
> I'd love to post a big detailed explanation but my larger posts are being denied.

**u/bluemyria**（1 分）：
What you just shared looks quite exciting to me. I was trying to invent/setup a similar workflow. 

It is really encouraging when someone has already been successful with such a learning workflow.

Could you give us some more insights on your technical setup? Thanks so much in advance!

> **u/No-Trick5569**（1 分）：
> I'd love to, but I'm pulling my hair out trying to get reddit to allow me to post the instruction sets.  I don't know if it thinks it's malicious code or what, but it just gives me a generic error with no explanation.

> **u/No-Trick5569**（1 分）：
> The way the kernel and instruction set are written is closer to a **rulebook or API spec** than to an essay. Instead of narrative explanations, it lays down hard requirements and bans, like a contract that the GPT has to follow. Each section is modular, with precise triggers, outputs, and fail conditions. The goal is to strip out ambiguity so the model behaves consistently, no matter the context.
> 
> Example snippet:
> 
>     pitfalls_and_gotchas:
>       rule: "List common mistakes or traps learners may fall into."
>       ban: ["vague phrasing", "handwaving"]
>       validation:
>         - "If no pitfalls listed → Conformance = fail."
>     
> 
> That’s the tone throughout: dry, binding, almost legalistic — but it works because the GPT treats it like a checklist rather than a suggestion.
> 
> I wrote the kernel and instruction set in a contract-style format, more like a programming spec than prose. Everything is modular, with strict rules, bans, and validation checks, so the GPT has no ambiguity in how to behave.

**u/Fluid-Difference-804**（1 分）：
Yup, I'm trying to mark what I want to ask, just write it in Obsidian, the answer to the question, then reverse link to the topic, let's say ADHD... ✍️🤔 #Obsidian #Questions #ADHD #NoteTaking

> **u/No-Trick5569**（1 分）：
> That’s a solid starting habit. The way I’ve set mine up takes that idea and stretches it into a bigger loop. I don’t just keep the question and answer — I log the whole dialogue of how I struggled, what I guessed wrong, and what eventually clicked. That dialogue later becomes the “Interactive Prompts” section of a study note.
> 
> From there the study note isn’t just a Q and A. It gets expanded with a summary of the core idea, why it matters, pitfalls to avoid, analogies, counterexamples, transfer tests, and a final integration section that stitches the whole arc together. Then, right at the end, the system applies strict rules to add links and tags, so the note slots into the vault without bloating it.
> 
> Once I’ve got a study note, I can distill out evergreens — atomic insights that stand alone and connect outward. And if it’s a topic I really want to remember, I’ll spin flashcards off those evergreens until I get a set that feels valuable.
> 
> So in your ADHD example, you’d start exactly how you describe: write the question, think it through, jot the answer, and link to ADHD. But if you run it through a process like this, you’d also capture the wrong turns, surface related concepts, and end up with notes and flashcards that reflect *how* you learned it, not just the final answer.

**u/nearlynarik**（2 分）：
This is very interesting. You've shared the what and the results for you, but you haven't quite described the 'how'.

are you approaching it through VS Code, or giving it GPT folder access?

How do you approach creating summaries of the conversations you've had with LLMs.

It obviously looks like you've put considerable reflection into developing your system. Would you share examples of the set up to guide people in this journey too? As you mentioned, it's not commonly described.

> **u/No-Trick5569**（1 分）：
> GPT does not have live folder access. Instead, I generate two export files from Obsidian. One is the note compendium, which stitches all notes together into a single file GPT can read. The other is the note index, which is just a flat list of every note title in the vault. These exports are created by simple scripts that run when I open Obsidian. The compendium gives GPT the raw content of my vault. The index enforces strict linking by requiring exact title matches instead of fuzzy guesses.
> 
> When I start a session, I upload three files: the compendium, the index, and the extended instructions. The kernel itself is embedded in the inline instructions and almost never changes — updating it is rare and deliberate. The extended instructions are modular and evolve daily, so they get refreshed often. For convenience I just drop all three files in together when I begin.
> 
> Conversation summarization is built into the workflow. Each turn in the coaching dialogue is logged as an Idea Record. When I promote the session into a study note, those turns appear under Interactive Prompts. The rest of the study note — the summary, why it matters, pitfalls, historical backdrop, analogies, counterexample, transfer test, resonance echoes, and the integration — is generated automatically by the rules. Linking and tagging are handled last, after integration, so the note embeds itself properly in the graph.
> 
> Daily journals follow the same pattern. I write freely, then the reflection module produces a summary and runs a temporal reflection pass to spot recurring themes and open loops. Every thirty days I run a larger reflection that surfaces broader shifts in attention and focus. These reflection notes are also linked and tagged by the same modules, so they stay woven into the system instead of floating separately.
> 
> Outcome.
> 
> The setup is minimal to copy. You need:
> 
> 1. Obsidian for writing.
> 2. Two export scripts that build note\_compendium.md and note\_index.md.
> 3. A kernel written into the inline instructions.
> 4. An extended instructions file that you update and upload with the exports at the start of a session.
> 
> This snapshot method avoids live folder access, but GPT still sees your whole vault in context. It is slower than direct integration, but it is predictable, auditable, and refreshable on your schedule.

**u/No-Trick5569**（1 分）：
My notifications weren't working properly so I just now see all these replies.  I'll get to all of you, just have to hold on a while!

**u/No-Trick5569**（1 分）：
I'm having a lot of trouble posting replies here, reddit is just giving me an "unable to post" error with no explanation

**u/No-Trick5569**（1 分）：
Alright well I messaged the mods, hopefully I can get things fixed and actually reply to you guys.

**u/Even-Step-7989**（1 分）：
any chance this can now work better with obsidian mcp on chatgpt developer mode ?

