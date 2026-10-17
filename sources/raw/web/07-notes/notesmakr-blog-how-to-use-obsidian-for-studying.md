# Notesmakr：用 Obsidian 学习

- 链接：https://notesmakr.com/blog/how-to-use-obsidian-for-studying
- 获取方式：网页正文（trafilatura 提取）

---

Here's the uncomfortable truth: most students who learn **how to use Obsidian for studying** end up with a stunning graph of interconnected notes and a mediocre exam grade. Hundreds of linked notes. A glowing constellation in graph view. A vault that looks like a second brain. It feels like deep studying. It mostly isn't.

Obsidian is one of the most powerful note-taking tools ever made for students. It stores every lecture, reading, and idea as plain-text files on your own computer, and it lets you link them together into a web of understanding no other app matches. But building a web of notes and *remembering* what's in them are two completely different jobs. Obsidian is brilliant at the first one. On its own, it does almost nothing for the second.

So this is the honest guide. You'll get a student Obsidian setup that actually works, the linking system that makes ideas stick, the one plugin that turns your vault into a self-quiz, and a clear-eyed list of what Obsidian cannot do for your memory. You'll also see how to bolt on the missing piece, spaced repetition, so the hours you pour into your vault show up on the test. If you want to see how Obsidian stacks up against the other big option first, read our guide to [how to use Notion for studying](/blog/how-to-use-notion-for-studying).

## What Does "Using Obsidian for Studying" Actually Mean?

**Using Obsidian for studying means turning a folder of plain-text Markdown notes into a linked knowledge base: lecture notes, readings, and your own ideas, all connected with `[[wikilinks]]` and viewable as a graph, stored locally and searchable in seconds.** Obsidian is a free notes maker that treats each note as an atomic idea you can wire to every related idea.

That is genuinely powerful. The problem is what most students *do* with it. They spend weeks perfecting the folder structure, installing themes, and admiring the graph, then call it studying.

Here's the split that matters.

**What Obsidian is great at:**

- Capturing notes from every class as plain-text files you own forever
- Linking ideas across subjects so connections become visible
- Building a personal wiki you can search instantly, even offline
- Handling Markdown, LaTeX math, code blocks, and diagrams natively
- Growing with you, from first-year notes to a thesis, in one vault

**What Obsidian does not do out of the box:**

- Schedule your reviews so you revisit material right before you forget it
- Force you to retrieve answers from memory instead of re-reading them
- Generate flashcards or quizzes from your notes automatically
- Tell you which topics you actually know versus which ones just *look* familiar

That second list is the whole game. Obsidian is an outstanding **knowledge base**. It is not, by default, a **memory system**. Mistake one for the other and you'll walk into the exam having "studied" in Obsidian for weeks with very little locked in.

## The Science: Why a Beautiful Vault Won't Save You

There's a reason building the perfect second brain feels so good and works so poorly.

In their landmark review of learning techniques, **Dunlosky et al. (2013)** ranked ten common study strategies by how well they actually work. The two winners were **practice testing** and **distributed practice** (spacing your study over time). Both earned "high utility." The losers? **Summarising** and **highlighting**, rated "low utility." Linking and rewriting notes in Obsidian is a form of elaboration, which helps. But if you never test yourself, you're skipping the single most powerful technique in the review.

This connects to the **testing effect**, documented by **Roediger and Karpicke (2006)**: students who retrieved information from memory remembered roughly 50% more a week later than students who simply re-read it. Scrolling your tidy linked notes is exactly the re-reading trap.

There's also good news for Obsidian users. Writing notes in your own words, connecting them to what you already know, is called **elaborative encoding**, and it works. **Slamecka and Graf (1978)** named this the **generation effect**: information you generate yourself is remembered better than information you passively copy. Every time you write an atomic note in plain language and link it to three others, you're generating, not transcribing. That's real learning. It just isn't enough on its own.

The gap is **spacing**. **Cepeda et al. (2006)** reviewed 254 studies and found that reviews spread over time produce dramatically stronger long-term memory than the same amount of study crammed together. Obsidian has no built-in system to space your reviews. Close the vault, and the [forgetting curve](/blog/spaced-repetition-guide) starts erasing everything you linked so carefully.

**A note you never revisit is a note you'll forget.** Obsidian is superb at building connections. It does nothing, by default, to schedule the reviews that turn those connections into durable memory.

## How to Set Up Obsidian for Studying (Step by Step)

You don't need 40 plugins. You need a vault, a folder logic, and a linking habit. Here's the setup that works for real coursework.

Download Obsidian from obsidian.md (free for personal use) and create a **vault**. A vault is just a folder on your computer where every note lives as a `.md` file. Name it something boring and permanent like "Studies." One vault for all your subjects is usually better than one per class, because the whole point is linking across subjects.

Resist the urge to over-engineer. Start with three folders: `Sources` (readings, lecture slides, PDFs you didn't write), `Notes` (atomic notes in your own words), and `Maps` (index notes that link to everything on a topic). That's it. You can add more later, but most students never need to.

An **atomic note** holds one idea, titled as a clear statement: "Myelin speeds up nerve signal transmission," not "Lecture 4." Write it in plain language, as if explaining it to a friend. This is where the generation effect kicks in. If you can't write the idea simply, you haven't understood it yet.

Type `[[` and Obsidian suggests existing notes. Link each new note to related ones: causes, contrasts, examples. These links are the reason Obsidian beats a plain folder of documents. Over a semester, the connections reveal how your subject actually fits together, and open the graph view to see it.

For each big topic, make one index note (a "map of content") that links out to every atomic note underneath it. This becomes your revision hub. Instead of hunting through folders, you open one map and see the whole topic laid out as links.

## Turn Your Obsidian Notes Into Active Recall

Here's where most Obsidian tutorials stop and most exam grades suffer. Linking notes builds understanding. It does not build recall. To fix that, you have to make Obsidian test you.

There are two levels to this.

**Level 1: Question notes.** Rewrite your atomic notes as questions. Instead of a note titled "The sodium-potassium pump," title it "How does the sodium-potassium pump maintain the resting membrane potential?" and put the answer below a fold or in a linked note. To review, read the question, answer out loud from memory, then check. You've just turned passive notes into a self-quiz.

**Level 2: The Spaced Repetition plugin.** Obsidian has no native flashcard system, but the community [Spaced Repetition plugin](https://github.com/st3v3nmw/obsidian-spaced-repetition) (by st3v3nmw) adds one. You mark inline flashcards with a separator like `Question::Answer`, and the plugin schedules reviews using an SM-2 or FSRS algorithm, the same science behind Anki. Reviews happen inside your vault, and the scheduling data stays in plain text.

This is the honest catch. That plugin requires setup: installing it, learning the card syntax, and configuring the algorithm. On desktop it's manageable. On mobile it's fiddly, and syncing your vault across devices means paying for Obsidian Sync or wiring up iCloud, Git, or another service yourself. Obsidian gives you total control, but it makes you assemble the retention layer by hand.

## Best Obsidian Plugins for Students (2026)

Obsidian's power comes from **community plugins**, but installing 30 of them is a classic time-sink. Start with the few that earn their place.

| Plugin | What it does | Worth it for students? | 
|---|---|---|
| **Spaced Repetition** | Flashcards and note-level review with SM-2/FSRS inside your vault | Yes, if you'll maintain it | 
| **Dataview** | Turns your vault into a queryable database (auto lists, tables) | Great for tracking readings and tasks | 
| **Templater** | Reusable note templates (lecture note, book note, etc.) | Saves setup time every day | 
| **Excalidraw** | Hand-drawn diagrams and visual notes inside Obsidian | Useful for STEM and concept maps | 
| **Readwise Official** | Auto-syncs highlights from Kindle, articles, and PDFs | Only if you already use Readwise | 

*Start with one plugin that solves your biggest problem. Add others only when you feel the pain they fix. Plugin sprawl is procrastination in disguise.*

## Watch: Obsidian for Studying in Action

Sometimes seeing the setup on screen beats reading about it. Here are two clear walkthroughs.

### Obsidian Tutorial: How to Use Obsidian Notes for Beginners

This walkthrough covers the absolute basics: creating a vault, writing your first notes, and linking them together. Key insight: **the links between notes, not the notes themselves, are where Obsidian's value lives.**

### My Effective Note-Taking System | Obsidian for Uni Students

This one shows a working student system rather than a theoretical one. Key insight: **a simple, repeatable capture-and-link routine beats an elaborate vault you abandon by midterms.**

## A Practical Example: Passive Vault vs Active Vault

The same Obsidian setup can be studying or busywork. The difference is whether you ever retrieve.

**You copy the lecture slides into Obsidian, tidy the formatting, link a few notes, and admire the graph. Before the exam, you scroll through your notes twice.**

It feels productive. Every note is neat and connected. But you never once answered a question from memory. On exam day the material feels familiar and you still can't produce the answers. That's recognition, not recall.

**You rewrite each concept as a question note in your own words, link it to related ideas, then tag the key facts as spaced-repetition cards. Each day you run a short review and answer from memory before checking.**

Now the vault forces retrieval. You know exactly which cards you keep missing (that's your study list) and which are locked in. Same app, same hours, completely different exam result.

## Quick Reference: When to Use Obsidian (and What to Add)

| Your goal | Use in Obsidian | Add for memory | 
|---|---|---|
| Capture lecture notes | Atomic notes + wikilinks | Question-format titles | 
| Connect ideas across classes | Graph view + maps of content | Elaborate as you link | 
| Understand a hard concept | Write it in plain words | Explain it aloud from memory | 
| Memorise facts and formulas | (Not Obsidian's strength) | Spaced-repetition flashcards | 
| Review before an exam | Open the topic's map of content | Spaced review, not re-reading | 

## Obsidian vs Notion vs Notesmakr: Which Does What?

These tools are not rivals so much as different jobs. Here's the honest breakdown.

| Job | Obsidian | Notion | Notesmakr | 
|---|---|---|---|
| Linked, offline, plain-text notes | **Best** | Limited | No | 
| All-in-one planner and databases | Limited | **Best** | No | 
| Built-in spaced repetition | Plugin only | No | **Yes (free, SM-2)** | 
| Cloze fill-in-the-blank cards | Plugin only | No | **Yes (free)** | 
| AI flashcards from a PDF | No | No | **Yes (free within limits)** | 
| Works with no setup on mobile | Fiddly | Yes | Yes | 

*Obsidian owns your knowledge base. Notesmakr owns your memory. Many students use a note tool for capture and a dedicated retention tool for review.*

Obsidian's own [documentation and community](https://help.obsidian.md/) are upfront that spaced repetition is not a native feature; it lives in third-party plugins you install and maintain yourself. If you want that memory layer without the assembly, that's exactly the gap Notesmakr fills.

## How Notesmakr Complements Your Obsidian Vault

Obsidian is your knowledge base. **Notesmakr** is a notes maker built to be the retention layer Obsidian leaves to plugins, so the ideas you link so carefully actually survive to exam day.

Here's the honest split of what's free and where the limits are:

- **Free:** manual flashcards, cloze (fill-in-the-blank) cards with progressive letter hints, **SM-2 spaced repetition** that schedules your reviews automatically, and **Anki `.apkg` import** so you can bring existing decks in. No plugin setup, and it works on mobile from the first minute.
- **Free within limits:** AI flashcards and quizzes generated from your notes or a PDF, AI note simplification, mind maps, and Pippy, the AI tutor. The free plan gives you 5 AI notes and 40 AI generations; Scholar raises the limits.

A realistic workflow: keep writing and linking your atomic notes in Obsidian, then pull the five most test-critical facts from each topic and turn them into spaced-repetition cards in Notesmakr. Or, when you're short on time, drop a lecture PDF into the [PDF to flashcards tool](/tools/pdf-to-flashcards) and let it draft the cards, then refine them. Facing a dense chapter you never linked? The [note summarizer](/tools/note-summarizer) pulls the key points into a study-ready summary. For the full picture on generating cards from your material, see our [AI flashcards guide](/blog/ai-flashcards-guide).

## Common Mistakes (And How to Avoid Them)

### Mistake 1: Building the vault instead of using it

Weeks of tweaking folders, themes, and plugins is procrastination wearing a productivity costume. **The fix:** cap all "setup" at 30 minutes, then start writing real notes today with whatever you've got.

### Mistake 2: Collecting notes you never revisit

A vault of 500 untouched notes is a graveyard, not a [second brain](/blog/second-brain-for-students). **The fix:** every note you keep should be linked to at least one other and revisited on a schedule.

### Mistake 3: Copying slides verbatim

Pasting lecture content into Obsidian skips the generation effect that builds memory. **The fix:** rewrite every concept in your own words as a clear, atomic statement.

### Mistake 4: Expecting Obsidian to remember for you

Obsidian stores and links; it does not schedule reviews. Without spacing, the forgetting curve wins. **The fix:** add the Spaced Repetition plugin or move key facts into a tool that schedules reviews automatically.

### Mistake 5: Drowning in plugins

Thirty plugins you half-configured slow you down and break on updates. **The fix:** start with one, add another only when you feel the specific pain it solves.

## The Research Behind It

Using Obsidian well is grounded in decades of learning science:

- **Practice testing and distributed practice top the rankings** (Dunlosky et al., 2013): A review of ten study techniques rated practice testing and spacing as "high utility" and summarising and highlighting as "low utility."
- **The testing effect** (Roediger & Karpicke, 2006): Students who retrieved information remembered about 50% more after a week than students who re-read it.
- **The generation effect** (Slamecka & Graf, 1978): Information you generate in your own words is remembered better than information you passively copy.
- **The spacing effect** (Cepeda et al., 2006): A review of 254 studies found reviews spread over time produce far stronger long-term retention than massed study.
- **Desirable difficulties** (Bjork & Bjork, 2011): Making retrieval effortful, not easy recognition, is what builds durable memory.

## Frequently Asked Questions

### Is Obsidian good for studying?

Obsidian is excellent for studying as a knowledge base. It links notes across subjects, stores everything as fast, offline plain-text files, and grows with you for years. Its weakness is memory: it has no built-in spaced repetition, so pair it with a retention tool or the Spaced Repetition plugin to actually memorise material.

### Is Obsidian free for students?

Yes. Obsidian is free for personal use, including all core note-taking, linking, graph view, and community plugins. Paid add-ons are optional: Obsidian Sync for cross-device syncing and Obsidian Publish for publishing notes online. Students can build a complete study vault without paying anything.

### Can you make flashcards in Obsidian?

Not natively. Obsidian has no built-in flashcard feature, but the community Spaced Repetition plugin adds inline flashcards and note-level review using SM-2 or FSRS scheduling. It requires installation and learning the card syntax. For zero-setup flashcards with spaced repetition, use a dedicated app alongside Obsidian.

### Obsidian vs Notion for students: which is better?

Choose Obsidian if you study alone, value fast offline plain-text notes, and love linking ideas into a graph. Choose Notion if you want templates, task tracking, and easy collaboration in study groups. Neither has strong built-in spaced repetition, so add a dedicated retention tool to either.

### How do I add spaced repetition to Obsidian?

Install the community Spaced Repetition plugin, then mark flashcards inline with a separator like `Question::Answer` or review whole notes on a schedule. The plugin uses an SM-2 or FSRS algorithm to time your reviews. For an easier path, move key facts into a flashcard app that includes spaced repetition by default.

## Start Today

You don't need a perfect vault. You need a working one plus a memory layer. Do this now:

1. Download Obsidian and create one vault called "Studies."
2. Add three folders: Sources, Notes, Maps.
3. Write today's hardest concept as one atomic note in your own words.
4. Link it to two related notes with `[[wikilinks]]`.
5. Install the Spaced Repetition plugin, or pull that concept into a spaced-repetition app.
6. Run one review session before you close your laptop.

Obsidian will build you a knowledge base no other app can match. Just don't confuse a beautiful graph with a trained memory. Link the ideas, then close the vault and recall them.

"The palest ink is better than the best memory."

— Chinese proverb
