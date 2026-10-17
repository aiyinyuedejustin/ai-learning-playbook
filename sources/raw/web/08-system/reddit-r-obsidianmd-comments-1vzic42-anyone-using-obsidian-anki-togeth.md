# Reddit r/ObsidianMD：Obsidian 和 Anki 一起做间隔复习

- 链接：https://www.reddit.com/r/ObsidianMD/comments/1vzic42/anyone_using_obsidian_anki_together_for_spaced/
- 作者：u/Illustrious-Pay-7516（r/ObsidianMD，26 分，4 条评论）
- 获取方式：Reddit 帖子与评论全文（取自 Arctic Shift 公开存档）

---

## 帖子：Anyone using Obsidian + Anki together for spaced repetition?

I've been using the Spaced Repetition plugin in Obsidian for a while, but I'm finding it a bit clunky as my number of flashcards grows. I'm thinking about moving the actual spaced repetition part to Anki, while still keeping Obsidian as my main knowledge base.

I'm curious if anyone here uses Obsidian and Anki together.

Ideally, I'd like Obsidian/Markdown to remain the source of truth, and have selected flashcards automatically synced to Anki. **My main concern is avoiding a situation where I have to manually maintain the same card in two places**.

For people who have this setup:

* How do you sync cards between Obsidian and Anki?
* Do you use an Obsidian plugin, AnkiConnect, or your own scripts?
* Which side do you treat as the source of truth?
* How do you handle editing/deleting cards without creating duplicates or losing Anki review history?
* Has this setup been reliable long term?

I'd also be interested in hearing whether you tried this and eventually decided it was simpler to just stay with either Obsidian or Anki.

## 评论（共收录 3 条，缩进表示回复层级）

**u/Saaajeel**（3 分）：
I made the [Echo Recall](https://community.obsidian.md/plugins/echo-recall) plugin for this exact purpose.

Each heading becomes a card in Anki. (Dont go by the screenshots on the community website, the Deep Recall mode isnt included there. Those screenshots are from the first version, which was based on a different idea of keeping everything inside Obsidian. and i am currently too pressed rn to update the new screenshots) but anyway,

If you turn on Deep Recall mode in the settings, connect Obsidian and Anki using the AnkiConnect add-on, and click on the flashcard icon on the ribbon, each heading gets converted into an Anki card with ALL the context maintained. Obsidian remains the source of truth.

Theres also an Update button on the ribbon, so if you make any changes inside Anki, those changes will be overwritten. Changes have to be made only in Obsidian.

This is the Obsidian → Anki workflow.

As for Anki → Obsidian, I made this Anki add-on:

[https://ankiweb.net/shared/info/1162061440](https://ankiweb.net/shared/info/1162061440)

This is the exact opposite. It syncs Anki cards to Obsidian AS IT IS, but the source of truth is Anki. So any changes you make inside Obsidian will be overwritten by the next sync from the Anki app.

The idea behind this add-on was to link my relevant Anki cards, which contain isolated facts, to my comprehensive notes, questions, or analytical notes wherever needed, instead of copy pasting or retyping everything.  


**My overall workflow is basically**:   
Creating new notes, reviewing new notes, analysis, and pretty much all creative tasks on my computer in Obsidian → synced to Anki with Echo Recall → then I use my iPad to review everything inside Anki :)

> **u/Saaajeel**（1 分）：
> Writing this made me realise i need to work on articulating my thoughts better and having a more logical flow in how i express them lol If anybody has any good resources or tips on how I can improve this, please lmk!

**u/Vaveili1**（7 分）：
Anki's review engine is worth it, but true bidirectional sync between markdown and .apkg files is the part nobody has solved without losing review history. The realistic setups people run long-term: obsidian-to-anki using AnkiConnect, where you write cards in your notes with a specific syntax and it pushes new/edited cards to Anki on a sync command, matching by a stored note ID so edits update in place instead of duplicating. Obsidian stays the source of truth for content, Anki keeps its own review history separate. Deletions are the one thing you handle manually.

Keep your card syntax dead simple in the markdown and treat Anki as a one-way export target.

