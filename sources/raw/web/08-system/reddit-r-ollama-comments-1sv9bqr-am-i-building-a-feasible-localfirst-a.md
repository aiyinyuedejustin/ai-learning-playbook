# Reddit r/ollama：本地 AI 学习系统是否可行

- 链接：https://www.reddit.com/r/ollama/comments/1sv9bqr/am_i_building_a_feasible_localfirst_ai_study/
- 作者：u/Joei160（r/ollama，3 分，17 条评论）
- 获取方式：Reddit 帖子与评论全文（取自 Arctic Shift 公开存档）

---

## 帖子：Am I building a feasible local-first AI study system, or am I fooling myself?

TL;DR: I am building a local-first AI study system for a demanding exam. The stack is Obsidian + Anki/AnkiConnect + Open WebUI in Docker + Ollama + nomic-embed-text + local Markdown vault mounted into the container. The vault is readable/writable from the container, and Anki card creation already works. My machine is an i7-12650H laptop with 32 GB RAM and an RTX 4050 Laptop GPU with 6 GB VRAM. I moved from qwen3.5:4b to qwen3:8b, but I am unsure whether this is enough for a reliable local agent that can explain content, create/edit Obsidian notes, generate Anki cards, and eventually audit gaps against an official syllabus. Is this architecture feasible, or am I being fooled by tooling complexity?

I am trying to build a local-first AI study ecosystem for a very demanding public exam. The goal is not just to “chat” with PDFs: I want a semi-operational knowledge system that can read and manipulate my Obsidian vault, generate Anki flashcards, and eventually audit gaps between my notes and the official syllabus.

I would appreciate a reality check from people who understand local LLMs, Open WebUI, Ollama, Obsidian, Anki, RAG, and agent tooling.

What I am trying to build:

The project is a local-first study platform based on:

\- Obsidian as the source of truth for Markdown notes.

\- Anki as the spaced-repetition layer.

\- AnkiConnect for programmatic card creation.

\- Open WebUI running in Docker as the interface.

\- Ollama as the local inference engine.

\- nomic-embed-text for embeddings.

\- A custom “biomechanical arm” / tool in Open WebUI that can create notes in Obsidian and create flashcards in Anki.

\- Eventually: a filesystem tool that can list, read, create, edit, move, and quarantine .md files inside the Obsidian vault.

The long-term goal is to have a system that can do things like:

\> “Explain the Questão Christie at CACD level.”  

\> “Now create an Obsidian note about it in the right folder, using my template.”  

\> “Generate 5 CEBRASPE-style true/false Anki cards from that note.”  

\> “Compare this section of my vault with the official CACD syllabus and identify gaps.”  

\> “Find weak, duplicated, missing, or underdeveloped notes.”

I do not expect perfect autonomy. I expect a human-in-the-loop system. But I do want the workflow to become fairly seamless.

Current machine specs

I am running this on a Windows 11 laptop:

\- OS: Windows 11 Home Single Language

\- CPU: Intel Core i7-12650H

\- RAM: 32 GB

\- GPU: NVIDIA GeForce RTX 4050 Laptop GPU

\- Dedicated VRAM: 6 GB GDDR6

\- CUDA cores: 2560

\- Max graphics power: 140 W

\- Storage: 1 TB SSD

\- Display: 1080p external monitor

So this is not a workstation, but it is not a weak machine either.

Current local model situation

I initially used:

\- qwen3.5:4b

That felt too weak for reliable agentic behavior.

I have now downloaded:

\- qwen3:8b

I accidentally started downloading qwen3:14b, but stopped because with only 6 GB VRAM it seems unrealistic for comfortable use. My current assumption is:

\- qwen3:8b may be viable for the operational agent.

\- qwen3:14b may be possible but slow/offloaded.

\- 30B+ local models are unrealistic on my hardware.

Is this assessment fair?

What is already working

Some parts are actually working:

1. AnkiConnect is working.  

   I successfully created Anki cards programmatically.

2. Open WebUI + Ollama are running locally.

3. Docker volume mount is working.  

   My Obsidian vault is located at:

   C:\\Obsidian

   I mounted it into the Open WebUI container at:

   /vault/obsidian

   using a Docker bind mount.

4. The container can read the vault.  

   I tested from inside the container and it listed real .md files.

5. The container can write to the vault.  

   I created a test Markdown file inside /vault/obsidian/00\_Sistema/, and it appeared in C:\\Obsidian.

6. My vault structure is being cleaned up.  

   Current top-level folders are roughly:

   \- 000\_Inbox

   \- 00\_Sistema

   \- 01\_História\_do\_Brasil

   \- 02\_História\_Mundial

   \- 03\_Política\_Internacional

   \- 04\_Geografia

   \- 05\_Economia

   \- 06\_Direito

   \- 07\_Idiomas

   \- 90\_Fontes

   \- 99\_Templates

   \- .obsidian

7. I have a master syllabus index.  

   I created an “Índice Mestre” mapping the CACD syllabus to recommended Obsidian notes. I also loaded the official CACD 2026 edital into a Knowledge Base.

Where I got stuck / frustrated

The part that broke my confidence was trying to make Open WebUI behave as a seamless agent.

I created a model preset called something like Arquivista, intended to be the single agent for the project. The system prompt included explicit rules such as:

\- The vault is at /vault/obsidian.

\- Política Internacional notes should go to /vault/obsidian/03\_Política\_Internacional.

\- História do Brasil goes to /vault/obsidian/01\_História\_do\_Brasil.

\- Never delete files permanently; move them to quarantine.

\- Before editing an existing note, read it first.

\- Use filesystem tools for real file operations.

\- Use the syllabus/edital Knowledge Base only as a normative map, not as the source of truth for live files.

However, when I tested the preset by asking:

\> “What is the internal path of the vault and where should I create a new note on Política Internacional?”

The model ignored the system prompt and answered generically, as if it had no idea about my setup:

\> “If you are using Obsidian, Notion, or another system...”

This was incredibly frustrating because the system prompt explicitly contained the answer.

Possible explanations I am considering:

1. I misconfigured Open WebUI’s model preset.

2. The preset system prompt is not actually being applied.

3. A chat/session/cache issue is causing the base model to be used instead of the preset.

4. qwen3:8b is just too weak or too instruction-unreliable.

5. I should create a custom Ollama model with a Modelfile and embed the system prompt directly into the model using SYSTEM """...""".

6. I should stop expecting a small local model to do this and use a stronger remote model/API for the agentic part.

Architectural question

Is the following architecture reasonable?

\- Use local Open WebUI + Docker + Obsidian + AnkiConnect as the operational layer.

\- Use the local model for simple operations, file manipulation, and maybe basic note generation.

\- Use Knowledge Bases only for stable reference material, such as the official syllabus and master index.

\- Use filesystem tools, not RAG, for live vault operations.

\- Use a stronger remote model when I need higher-quality reasoning, gap audits, or sophisticated content generation.

Or am I overengineering this?

What I want to know

1. Is this project feasible on my hardware?

2. Is qwen3:8b enough for this kind of local agent, or am I expecting too much?

3. Should I create a custom Ollama Modelfile model with the system prompt embedded, instead of relying on Open WebUI presets?

4. Should the “vault map” live in the system prompt rather than in a Knowledge Base?

5. Is Open WebUI a good tool for this, or should I use something else for the agent/filesystem layer?

6. Is RAG the wrong abstraction for the live Obsidian vault?

7. Would you recommend a hybrid setup where the filesystem and privacy-sensitive parts are local, but higher-level reasoning uses a remote model?

8. What is the simplest robust architecture for this?

I am not asking whether a fully autonomous AI tutor can magically manage my studies. I know that is unrealistic. I am asking whether a human-supervised, local-first, Obsidian/Anki/LLM workflow like this is technically sound, or whether I am being seduced by tooling complexity and should simplify dramatically.

Any blunt second opinions would be appreciated.

## 评论（共收录 23 条，缩进表示回复层级）

**u/David_AnkiDroid**（18 分）：
> Any blunt second opinions would be appreciated.

You're drawn to this idea as a distraction from an unpleasant task.

You're going to spend most of your time making this system, and not enough time studying. 

> **u/Joei160**（3 分）：
> I'm on vacation for three weeks. I have time (:

> > **u/123vovochen**（5 分）：
> > wrong

> **u/Grisward**（6 分）：
> This is an amazingly insightful comment. ^^
> 
> OP you’re making the choice to study Local LLM’s instead of whatever it is you’re supposed to be studying. It’s fine, many a career path is decided by this type of thing. Just remember eventually you need to study the original subject. And good luck!

> > **u/overand**（2 分）：
> > In case anyone piles on you assuming you're either using an LLM or are a bot:
> > 
> > HEY PEOPLE: I took a look at their posting history; much like me, they just write like that, and have for years, and this is a reddit account with a **10 year long** history.  Being affirming wasn't invented by LLMs - in fact, it turns out *they were trained on people writing on Reddit* (among other places, obviously.)

> > > **u/Grisward**（1 分）：
> > > Yeah I skimmed the post, wondered if it’s LLM formatted — also I don’t mind when people use LLM to write a post anyway. Your comment resonates.
> > > 
> > > I mostly skimmed the OP post and the sheer volume of it alone is what made me recognize it’s a procrastination tool. Ask me how I know, haha. Tbf to OP I have years of such procrastination.
> > > 
> > > And also, sometimes that procrastination strikes gold, and becomes something very valuable to me. Sometimes it doesn’t, and that’s all I meant in my comment to OP. If you want to take a chance that this experience turns into a skillset, do it. No guarantees, but take a shot and see. If you’re not doing it for that, prioritize accordingly.

> **u/Space__Whiskey**（1 分）：
> You sound like you are speaking from experience. I do this too. 

> **u/overand**（1 分）：
> My parent commenter is the AnkiDroid Developer, and he says-
> 
> *Everyone in the thread turns around to face Overand.*
> 
> Narrator: "When a..."
> 
> I was going to try to make a "When a dermatologist's daughter talks, you should listen" reference to a skincare product ad from the 90s, but I think that might be both too deep of a cut, and also, I have no idea how I'd do "dermatologist's daughter" in this case. Like. "When a redditor who notices their parent commentor is the developer of some great software..."
> 
> Ehh. Either way, thanks for the work!

**u/NewRooster1123**（1 分）：
The architecture is feasible, but only if you split it into three separate jobs: source of truth, retrieval, and card generation. Let Obsidian own the notes, treat embeddings/indexes as disposable, and make flashcard generation auditable against a small test set before you automate anything that writes back into the vault. If the local model has to reason over the whole system and mutate files reliably, complexity will outrun the study benefit fast. I would start with read/query/summarize only, measure error rates on 20-30 real syllabus questions, and add write actions later. I will always compare it with changing oss/closed or paid solutions like notebooklm or nouswise.

**u/guesdo**（1 分）：
RAG is just a term, there are a lot of ways to implement it. Think of RAG as giving the LLM tool calling and the ability to search your docs (Agentic RAG), or you doing the search and pushing into context (classic RAG), you can either run semantic search (embeddings) or just keyword BM25 scored search (inverted index).

The best of course IMO is hybrid (semantic+bm25) agentic RAG, but the time you will be stuck implementing that in 3 weeks is not worth the hassle. Specially around strategic chunking of docs and generation. 

That said, even with perfect tool calling and RAG, the 8B model will fill up the context FAST, and with only 6GB of VRAM you will run into a ton of issues.

Project feasible? yes, maybe, with the hardware you got, I doubt it...

I would just use a cloud model to get everything our of the way (generating the knowledge base, anki model cards, verification, etc...), once all the setup is done, maybe just a simple index based RAG with references, maybe skills with progressive discovery.

That said... OpenWebUI is a chat, that it, it can do some tool calling but its not a full fledged agent like the one you want. You might get more mileage out of your setup with a coding agent (even if you aren't coding), like OpenCode or Hermes, those are designed to look at stuff and instruction following, but the 8B model seems to weak to drive them correctly, specially if you want "thinking" on top of it like in your examples: "Explain the Questão Christie at CACD level.” then instruct following: "Now create an Obsidian note about it in the right folder, using my template."

All that is more suited for a larger model, so use that, and maybe once everything is generated, the 8B model can drive discovery and studying practices, but IMO the setup you want is not going to work, specially around large context, it will crawl to a halt and crash.





> **u/Joei160**（1 分）：
> That is exactly what I was looking for. Thank you very much!

> **u/First-Paint-3114**（1 分）：
> local rag setups are a rabbit hole fr. spent way too long messing with chunking strategies and watching my gpu melt. i ended up just going with Reseek for my actual notes and docs, it handles the hybrid search stuff without me babysitting vram usage. cloud models for generation, managed platform for retrieval, way less headache.

> > **u/Joei160**（1 分）：
> > Your comment has proven prophetic. How do you integrate cloud models with your Obsidian? The best I could come up with as of now is sharing the latest version of my vault's master index (base) with ChatGPT and asking it to contrast that with the architecture we have set up for what a "complete" vault would likely be. It can only compare the headings of my notes, though.

**u/robogame_dev**（2 分）：
I have a similar setup.

I made this Dropbox tool for file/Obsidian access, and wrote instructions on how to use it and my vault etc.

You will struggle with the more advanced asks you have, and it will be fairly slow - the model will often need to stop and list the files in a directory, then it will start reading them, then it will stop and list more files, read more, etc - context grows as it explores the notes data.

I often start a new chat with "read my latest 2 weeks of notes on topic X and get up to date on where we're at" - then go do something else for a couple minutes while it explores and reads.

After that, you've got whatever size context window you have to interact before you gotta start a new chat. In Open WebUI it's really easy to branch the convo though, so this isn't a big deal in practice, you just end up branching.

I don't think your video card has enough local mem to run a capable enough model with enough context to read your notes - assuming the exam is very demanding, it's going to need what, 32-64k of background info just to answer each question you have right? Easiest move is to start with using cheap AI, get an openrouter account and use the free models for example - since this is exam prep there's not a privacy concern so you can take advantage of all the free "we train on your inputs" inference out there.

> **u/Joei160**（2 分）：
> I really — REALLY — appreciate your input. Thank you very much.

**u/Dudmaster**（1 分）：
This space is about to blow up. I'm building a SaaS around it, but I know competitors are starting to appear too. If you're interested, check out ideagenesis.ai :)

> **u/Joei160**（1 分）：
> What do you mean by “this space is about to blow up”?

> > **u/Dudmaster**（2 分）：
> > Educational institutions haven't yet fully embraced AI for learning in a way that's genuinely productive. A lot of times cheating is an "open secret". Building conventional structured learning processes around the assistant itself is where I'm trying to take it. I definitely see others going this direction soon. For example, OpenMAIC

**u/Deep_Ad1959**（2 分）：
my read is the architecture is fine, the bottleneck is write path reliability on an 8b with 6gb of vram. reads work. writes compound errors fast: one wrong frontmatter key, one ankiconnect arg off, one heading at the wrong nesting depth, and the next three turns are the agent trying to undo what it just did. the syllabus gap audit specifically wants to be a chunked deterministic pipeline that calls the model per chunk and produces a diff, not one big agentic loop holding everything in context. local is great for explain and propose. writes want a dry-run diff with an explicit accept step, otherwise you and the agent are debugging the same vault in parallel.

> **u/Joei160**（1 分）：
> Thank you very much for this! What alternatives are there for me? The local-based thing is absolutely negotiable 😳👍

> > **u/Deep_Ad1959**（2 分）：
> > my swap would be: keep the local stack for retrieval and summarize, push every write path through a frontier model via api with a structured diff output, apply locally with a dry-run gate. claude or gemini at the api level handles the multi-turn write reasoning your 6gb card can't, and you only pay tokens on audit/write jobs, not on every read. for the syllabus gap audit, batch it: chunk the syllabus, chunk your vault by tag, compare per-chunk in a deterministic loop, output a coverage matrix. that's a cron job, not a chat. the anki side stays a last-mile script that consumes the diff and calls ankiconnect, no agent in that step.

**u/Right_Adeptness6095**（1 分）：
Concurrency locks and OOM issues? Try Veil-Piercer for a free diagnostic script. Local-first agents avoid cloud SDK bottlenecks with KV caching and reduced latency. Check it out!

  


**u/Special_Permit_5546**（1 分）：
I think the architecture is feasible, but the hard part is not the model - it is the write boundary.

  
I would avoid making the live vault the agent's playground at first. Treat the vault like a repo: read/search freely, but every create/edit/move should become a proposed patch with a human approval step. For studying, that approval step is not just safety; it forces you to actually process the material instead of outsourcing the learning.

  
My suggested split:

  
1. Obsidian/Markdown vault = source of truth

2. disposable index = embeddings/BM25/graph, rebuildable any time

3. agent workspace = draft notes + Anki candidates + gap reports

4. apply layer = explicit diff/patch into the vault

  
For 6GB VRAM, I would not expect an 8B model to reliably do long-horizon planning plus file mutation plus syllabus auditing. It can handle narrow local operations, but I would use a stronger model for the reasoning-heavy audit/write steps and keep the filesystem local.

  
Tiny disclosure because it is relevant: I'm building an open-source local-first Markdown app called Kuku around this exact pattern - AI can search/read/create/edit notes, but edits are reviewable diffs instead of silent mutations. It is macOS-first, so maybe not directly useful for your Windows setup, but the repo might be useful as a reference for the product shape: [https://github.com/kuku-mom/kuku](https://github.com/kuku-mom/kuku)

  
Your instinct that RAG is the wrong abstraction for the live vault is right IMO. RAG is fine for retrieval. For changing notes, you want file tools + deterministic policies + patches.

