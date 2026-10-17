# Brunimir/Knowledge-Factory

- 链接：https://github.com/Brunimir/Knowledge-Factory
- 作者：Brunimir
- 仓库说明：An agentic Personal Knowledge Management (PKM) system that turns raw, multi-disciplinary input into durable, interconnected, retrievable knowledge — and tells you exactly how much you can learn without falling behind.
- 星数：2
- 获取方式：GitHub README + SKILL/说明文件

---

## README

# The Knowledge Factory

**An agentic Personal Knowledge Management (PKM) system that turns raw, multi-disciplinary input into durable, interconnected, retrievable knowledge — and tells you exactly how much you can learn without falling behind.**

Most note-taking solutions are where information goes to die: you capture more than you ever revisit, connections never form, and nothing reaches long-term memory.

This system fixes that. It treats knowledge as a *production pipeline*, run by Claude Code over an Obsidian vault — where raw information is broken down into atomic concepts, woven into maps of related ideas, optionally drilled into memory as spaced-repetition flashcards, and composed into reusable solutions.

A built-in capacity model keeps the *learning* load honest. Because concepts can also be captured for reference only — without ever being studied — the vault grows at a pace you can actually retain, and you never become its bottleneck.

> This repository ships the **engine** — templates, extraction prompts, Claude Code skills, and orchestration scripts. You bring your own Obsidian vault; the system installs *over* it. The only vault content included is **one worked example** (the *Learning & Memory* MOC and its 11 concept notes under `20_Learning/`), so you can see real output.

*If you're a student, researcher, or professional trying to learn faster and retain more — the Knowledge Factory is for you.*

---

## 1. The Pipeline

### 1.1 Overall — the knowledge loop

Knowledge flows through five engines in a continuous loop:

![The five engines of the Knowledge Factory — Capture, Process, Interconnect, Retain (optional), Produce. Human verification is optional, Retain can be skipped for reference-only notes, and a gem-capture loop turns new insights from conversations into fresh input in the inbox.|697](5-engines.svg)

Raw material enters through **Capture**, is atomised into clean concept notes by **Process**, is related to the rest of the vault by **Interconnect**, is *optionally* committed to long-term memory by **Retain**, and is put to work by **Produce**. Solutions and flashcards in turn surface gaps, which feed the next capture cycle(Note to claude, to clarify)

### 1.2 The five engines

#### 🎣 Capture
Gets vault-worthy ideas out of conversations and sources and into the inbox, without polluting the vault.
- **`extract-gems`** — at the end of a substantive Claude conversation, identifies the genuinely vault-worthy "gems" and routes each one: a new candidate, a one-line refinement of an existing note, or *exclude*. Conversation-scoped, so it never runs the full pipeline by accident.
- **Extraction prompts** — `EXTRACT_PROMPT.md` (after a Claude conversation) and `EXTRACT_PROMPT_NotebookLM.md` (for books/PDFs or other soucres via NotebookLM) define a strict, machine-readable block format: a falsifiable claim, a named mechanism, a boundary condition, an application, and typed edges to other concepts.
- **Output:** raw structured notes land in `00_Inbox/` (Note Stock → Note Pipe → AI_Candidates), never directly in the vault.

#### ⚙️ Process
Turns raw inbox notes into atomic, self-contained concept notes.
- **`process-inbox`** (skill: `pkm-ingestion`) — runs a multi-phase ingestion pipeline (Phases 0–5): validates each note against a quality gate, writes one **atomic concept note** per teachable idea using the Feynman-style template, and surgically patches every relevant **Map of Content** — a concept can belong to more than one MOC (its `moc:` field is a list), so a cross-cutting idea is mapped into each domain it touches.
- Enforces hard safety rules: never overwrites a note's full content, never invents facts, and never edits a `status: final` note except for two whitelisted patches.
- **Output:** concept notes in `20_Learning/21_Concepts/`, MOC patches in `20_Learning/22_Maps of Content/`.

#### 🔗 Interconnect
Makes the vault more than the sum of its notes.
- **`weave-links`** — a retroactive pass that discovers cross-domain relationships between concepts living in *different* MOCs, recording each edge in the canonical prose-verb format using a closed 7-label vocabulary (`supports`, `contradicts`, `prerequisite-for`, `instance-of`, `mechanism-of`, `mitigates`, `related-to`).
- **`visualise-moc {stem}`** — renders a two-tier Mermaid concept map (overview + cluster detail) for a MOC, fully derived from a pre-extracted manifest and regenerated idempotently.
- **`vault-health`** (skill: `pkm-review`) — surfaces *actionable* notes (final notes still awaiting flashcards), MOC coverage, orphans, flashcard coverage, and acronym/knowledge gaps. Drafts are a valid permanent state and are never nagged — the human is deliberately not the bottleneck.

#### 🧠 Retain
Locks finalised knowledge into long-term memory through spaced repetition.
- **`generate-flashcards`** (skill: `pkm-flashcards`) — generates dense Anki cards from `status: final` concept notes: three cards per concept (WHAT / HOW / WHEN), one batch file per run for safe AnkiConnect syncing.
- **Output:** flashcards in `20_Learning/23_FlashCards/`, synced to Anki. (The Capacity Model in §2 bounds how much new material enters Retain each week so the review load stays sustainable.)
- Anki rides your brain's forgetting curve — resurfacing each card the instant before it would be cleared — so every recall signals "keep this," converting short-lived facts into durable long-term memory.

#### 🚀 Produce (Output Bridge)
Puts mapped knowledge to work as real-world deliverables. (Canonically the **Output Bridge** / **Phase 5** in `CLAUDE.md` and the `pkm-solution` skill.)
- **`pkm-solution`** — the Phase 5 "Output Bridge": drafts a **Pattern** (a reusable, abstracted playbook) or a **Solution** (a realised deliverable, optionally with a binary companion), with automatic use-count tracking on the source Patterns.
- **Output:** artefacts in `40_Solutions/`.

### 1.3 The command surface

Claude Code dispatches on the first word of your request. Seven pipeline commands, plus one cross-cutting retrieval command:

| Command | Engine | What it does |
|---|---|---|
| `extract-gems` | Capture | Pull vault-worthy gems out of the current conversation. |
| `process-inbox` | Process | Ingest raw inbox notes → atomic concept notes + MOC updates. |
| `weave-links {scope}` | Interconnect | Discover & record cross-domain links between MOCs. |
| `visualise-moc {stem}` | Interconnect | Render a Mermaid concept map for one MOC. |
| `vault-health` | Interconnect | Audit coverage, gaps, and the flashcard backlog (never nags drafts). |
| `generate-flashcards` | Retain | Generate Anki flashcards from final concept notes. |
| `pkm-solution` | Produce | Draft a Pattern or Solution from the vault. |
| `vault-query {question}` | *Retrieve* | Answer an ad-hoc question with a cited, synthesised answer drawn only from the vault (or admit it has nothing). |

> `vault-query` is a **read-only, cross-cutting retrieval command**, not a sixth pipeline engine: it spans the whole vault to *use* what the five engines have crystallised (the "Usage" job in §6), and never writes a note.

---

## 2. The Capacity Model — *how much can you actually retain?*

Capturing knowledge is easy; **retaining** it is the constraint. Spaced repetition only works if the daily review load stays sustainable — so the system models intake against a fixed, honest review budget.

The whole model reduces to one equation — the **monthly concept-retention capacity** `K`, derived directly from a sustainable daily review budget `D`:

> **K = (D · T · P) / (C · R)** — the model's monthly retention capacity.
>
> With the recommended values: **(31 × 7 × 4) / (3 × 8) = 868 / 24 ≈ 36 concepts/month**.

| Symbol | Meaning                                           | Recommended value |
| ------ | ------------------------------------------------- | ----------------- |
| **D**  | Sustainable daily review load you set (cards/day) | **31**            |
| **C**  | Cards generated per concept                       | **3**             |
| **R**  | Mean reviews per card over its lifetime           | **8**             |
| **T**  | Days per period                                   | **7** (one week)  |
| **P**  | Periods per month                                 | **4** (weeks)     |
| **K**  | Monthly concept-retention capacity *(the answer)* | **≈ 36 / month**  |

**How it's derived, in one breath.** The sustainable daily review load `D` is the real constraint. Each new concept spawns `C` cards, each reviewed `R` times over its life. So learning `X` concepts a week costs `(X · C · R) / T` reviews a day — set that equal to `D`, solve, and multiply by the `P` weeks in a month to get `K`.

The weekly lever falls out as `K / P` ≈ **9 new concepts/week**.

**This budget bounds *learning*, not crystallisation.** You can capture and crystallise far more than 36 concepts a month — reference notes need no flashcards. The budget governs only what you commit to memory.

Push *learning* past it and the daily review load climbs above budget. The model makes that trade-off explicit instead of letting the backlog grow silently — and tuning `C`, `R`, or `D` moves the capacity with it.

---

## 3. What the System Produces

### The Vault (Obsidian)

A numbered folder taxonomy keeps capture, learning, and output cleanly separated:

```
00_Inbox/            raw capture (Note Stock → Note Pipe → AI_Candidates) + generated indexes
10_Ideas/            half-formed ideas not yet atomic concepts
20_Learning/
  ├─ 21_Concepts/        atomic concept notes (the core unit of knowledge)
  ├─ 22_Maps of Content/ MOCs — clusters + typed edges + cross-domain links
  ├─ 23_FlashCards/      generated Anki decks (one file per batch)
  └─ 24_Diagrams/        rendered Mermaid concept maps
30_Sources/          source material (books, PDFs, references)
40_Solutions/        Patterns and Solutions (knowledge turned into output)
50_Admin/            vault administration
99_System/           templates, prompts, skills, and this system's scaffolding
```

### The artefacts

- **Concept note** — the atomic unit. A single teachable idea in Feynman structure: Core Idea, Mechanism (+ boundary condition), Application (when to use / when *not* to), and typed edges. Carries `status`, `reviewed`, and `flashcards` flags that gate everything downstream.
- **Map of Content (MOC)** — a living map of one domain: concept clusters, typed relationships, and a Cross-Domain Links section connecting it to other MOCs. A single concept can be mapped into several MOCs at once (its `moc:` field is a list), so cross-cutting ideas surface in every domain they touch.
  - **Flashcards (+ Anki)** — three dense cards per final concept (WHAT / HOW / WHEN), synced to Anki via the flashcards-obsidian plugin for spaced repetition.
- **Solutions** — where knowledge becomes output:
  - **Solution doc** — a realised deliverable built from vault concepts (optionally with a `.pptx`/`.docx`/`.xlsx` companion).
  - **Pattern** — a reusable, abstracted playbook with a tracked use-count.

### The artefact lifecycle

Every knowledge artefact moves through **one consistent lifecycle** — the same three
flags gate a concept, a MOC, a Pattern, and a Solution alike, so there is only one
state machine to learn:

```
draft  ──(human review pass)──▶  final  ──(generate-flashcards / opt-out)──▶  final + flashcards:true
  │                                 │
  └─ reviewed: false ──────────────▶ reviewed: true
```

- **`status: draft`** — the resting state for everything the agent writes and most of
  what you write. It is a **valid permanent state**: a reference note you never intend
  to study can live as `draft` forever. Drafts are never nagged.
- **`status: final`** — *you* promote a note to `final` in a single review pass, against
  three criteria: the core idea is statable from memory in one sentence, every wikilink
  resolves, and at least one real application is named. The agent **never** sets `final`
  on its own, and never edits a `final` note except two whitelisted patches.
- **`reviewed` / `flashcards`** — `reviewed: true` records your approval; `flashcards`
  flips to `true` when cards are generated *or* when you deliberately opt a note out of
  studying ("reviewed, no need to study"). A note is eligible for `generate-flashcards`
  only when `status: final AND reviewed: true AND flashcards: false`.

The design principle: **the human is never the bottleneck.** `draft` has no review SLA,
nothing is ever flagged as "stale," and you promote only the notes you choose — the rest
rest indefinitely. See [`docs/lifecycle.md`](docs/lifecycle.md) for the full reference.

### A worked example

To show real output — not just empty templates — the repo ships one fully-built domain: the **Learning & Memory** MOC and the 11 atomic concept notes it maps.

- **MOC** — `20_Learning/22_Maps of Content/MOC_Learning_and_Memory.md`: concept clusters, key tensions, cross-domain links, an embedded SVG concept-map, and the typed relationship graph.
- **Concepts** — `20_Learning/21_Concepts/`: Active Recall, Chunking, Spaced Repetition, Focused Mode, Diffuse Mode, Interleaving, Sleep and Learning, The Magical Number Seven, Cluster Processing, Information Overload Tax, Process vs Product.

> These are real notes in Obsidian format. On GitHub, `[[wikilinks]]` render as literal text (Obsidian resolves them; GitHub doesn't), and the cross-domain links point to MOCs outside this example.

---

## 4. Getting Started

### Requirements

- **[Obsidian](https://obsidian.md/)** — the vault host.
- **[Claude Code](https://claude.com/claude-code)** — the agent that runs the pipeline.
- **Python 3** — runs `generate_index.py` to build the vault index.
- **[Anki](https://apps.ankiweb.net/) + [AnkiConnect](https://ankiweb.net/shared/info/2055492159)** — flashcard review and sync.
- **Obsidian plugins:** `flashcards-obsidian` (card sync) and `Advanced URI` (triggering sync from the launcher).
- **[Node.js](https://nodejs.org/) + `@mermaid-js/mermaid-cli` (`mmdc`)** — only needed for `visualise-moc` diagram rendering (the launcher falls back to `npx`).

> *You can ask your Claude to walk you through this section step by step — paste this README and say "help me set up the Knowledge Factory in my Obsidian vault."*

### Install

1. **Clone** this repository.
   ```bash
   git clone https://github.com/Brunimir/knowledge-factory.git
   ```
2. **Copy the scaffolding into your vault**, preserving structure: place `CLAUDE.md` at your vault root, and the contents of `99_System/` into your vault's `99_System/`. To use the engines as Claude Code slash-commands, also copy `99_System/Claude/<skill>/` into your project's `.claude/skills/`.
3. **Configure your environment.** Copy the template and fill it in:
   ```bash
   cp .env.example .env
   ```
   ```ini
   ANTHROPIC_API_KEY=sk-ant-...
   VAULT_ROOT=C:\path\to\your\obsidian\vault
   OBSIDIAN_VAULT=YourVaultName
   ANKI_EXE=%LOCALAPPDATA%\Programs\Anki\anki.exe
   ```
   Alternatively, set `VAULT_ROOT` in your shell — every script falls back to its own directory if it's unset.

### Usage

The launchers handle pre-flight (index regeneration, validation) and post-flight (run summaries):

```powershell
# Process everything sitting in the inbox
.\launch-process-inbox.ps1

# Generate flashcards from final notes and sync them to Anki
.\launch-generate-flashcards.ps1

# Render the concept map for one MOC
.\launch-visualise-moc.ps1 MOC_Learning_and_Memory
```

A typical weekly cycle: capture during the week → `process-inbox` → review and mark notes `final` → `generate-flashcards` → periodically `weave-links` and `vault-health` to keep the graph healthy → `pkm-solution` when you need to *use* what you've learned.

---

## 5. Repo Layout

```
.
├─ CLAUDE.md                       # Command interface + safety rules (place at vault root)
├─ generate_index.py              # Builds VAULT_INDEX.json from the vault
├─ launch-process-inbox.ps1       # Capture → Process launcher
├─ launch-generate-flashcards.ps1 # Retain (flashcards) launcher + Anki sync
├─ launch-visualise-moc.ps1       # Interconnect (diagram) launcher
├─ extract_diagram_candidates.ps1  # Pre-extracts the per-MOC diagram manifest
├─ extract_flashcard_candidates.ps1# Pre-extracts the flashcard candidate manifest
├─ requirements.txt               # Python dependencies (PyYAML core; per-skill locks for the rest)
├─ .env.example                   # Environment template (copy to .env)
├─ 99_System/
│  ├─ Readme.md                   # Core PKM philosophy / global rules
│  ├─ EXTRACT_PROMPT.md           # Capture: post-conversation extraction spec
│  ├─ EXTRACT_PROMPT_NotebookLM.md# Capture: NotebookLM source-extraction spec
│  ├─ *_Template.md               # Concept, MOC, Pattern, Solution, Idea, Flashcard templates
│  ├─ Annex_3_Pattern_Generator.md, Annex_4_Flashcard_Generator.md
│  ├─ acronym_allowlist.md, CANDIDATE_TEMPLATE.md, WEEKLY_REVIEW_CHECKLIST.md
│  └─ Claude/                     # The five engines + cross-cutting retrieval (Claude Code skills)
│     ├─ gem-extraction/SKILL.md  # Capture
│     ├─ pkm-ingestion/SKILL.md   # Process
│     ├─ pkm-review/SKILL.md      # Interconnect (vault-health)
│     ├─ vault-graph/SKILL.md     # Interconnect (similarity + graph topology)
│     ├─ pkm-flashcards/SKILL.md  # Retain (flashcards)
│     ├─ pkm-solution/SKILL.md    # Produce (solutions)
│     └─ vault-retrieval/SKILL.md # Retrieve (vault-query: cited hybrid retrieval)
├─ docs/                          # Full phase specifications (read by CLAUDE.md)
│  ├─ inbox-pipeline.md           # process-inbox: Phases 0–5
│  ├─ visualisation-pipeline.md   # visualise-moc: Phases V-0 → V-6
│  └─ interconnect-pipeline.md    # weave-links: Phases IC-0 → IC-6
└─ LICENSE
```

> The engine deep-dives in §1 are the high-level summary; the complete phase-by-phase specifications live in `docs/` and are loaded on demand by `CLAUDE.md` when the matching command runs.

---

## 6. Conclusion

The Knowledge Factory treats knowledge work as an engineering problem: a pipeline with clear stages, strict quality gates, and a capacity model that matches the learning load to what a human can actually retain.

It starts by breaking every source down to its **smallest common denominator — the atomic concept**: one self-contained, reusable idea. Everything downstream works only because knowledge is atomic.

From that unit, it separates four jobs that most note-taking blurs together:

- **Crystallisation** — raw input becomes atomic, interconnected, queryable concepts.
- **Learning** — a *chosen* subset is committed to long-term memory via spaced repetition.
- **Usage** — you retrieve and recombine what you've kept, on demand.
- **Production** — knowledge is turned into real-world deliverables.

You crystallise far more than you memorise. Reference concepts live in the vault, searchable whenever you need them, while the ~36-a-month budget is spent only on what you deliberately choose to learn.

Capture without crystallisation is noise; knowledge you never use stays inert. So run all five engines over an Obsidian vault, harvest new gems with every cycle, and scattered reading compounds into a body of **atomic, interconnected** knowledge that is crystallised, selectively retained, and *applied*.

It's opinionated by design, but every piece — the templates, the prompts, the skills, the capacity constants — is yours to tune.

---

## License

Licensed under the **[Apache License 2.0](LICENSE)** — © 2026 Bruno Bodson.


## 文件 CLAUDE.md

﻿# PKM Agent — Claude Code Command Interface
# Place this file at the root of your Obsidian vault (your VAULT_ROOT).
# Claude Code reads it automatically at the start of every session.

---

## ENVIRONMENT

VAULT_ROOT : <set via $env:VAULT_ROOT or edit the launcher scripts>
PLATFORM   : Windows — use PowerShell for all file operations.
             Never use /mnt/c/ paths. Never use bash or sh.
INDEX_FILE : <VAULT_ROOT>\00_Inbox\VAULT_INDEX.json

All file reads and writes go through PowerShell tools (Read-Content,
Set-Content, New-Item, Get-ChildItem). If your vault lives on
cloud-synced storage, do not use file locking operations.

---

## COMMANDS

Claude Code is invoked with one of these subcommands.
Read the first word of the user's message to dispatch:

  process-inbox          → run the PKM ingestion pipeline (Phases 0–5)
                           reads from: 00_Inbox\Note Pipe\
                           writes to:  21_Concepts\, 22_Maps_of_Content\
                           note: a concept's `moc:` field is a LIST — a note may be
                                 mapped into several MOCs; patch every relevant one.

  generate-flashcards    → generate Anki flashcards from status:final concept notes
                           reads from: 20_Learning\21_Concepts\ (status:final AND flashcards:false)
                           writes to:  20_Learning\23_FlashCards\  (FC_{stem}.md)
                           format: flashcards-obsidian plugin (4 #card headings per note)

  pkm-solution           → draft a Phase 5 artefact (Pattern or Solution)
                           reads from: 00_Inbox\VAULT_INDEX.json → 21_Concepts\,
                                       10_Ideas\, 40_Solutions\ (selective; index-first)
                           writes to:  40_Solutions\
                           see skill: 99_System\Claude\pkm-solution\SKILL.md

  vault-health           → audit wikilinks, orphans, used_in counts,
                           vault gaps (acronyms), and MOC coverage.
                           See pkm-review skill.
                           reads from: VAULT_INDEX.json + targeted note reads
                           writes to:  00_Inbox\VAULT_HEALTH_REPORT.md
                                       00_Inbox\VAULT_GAPS_REPORT.md
                           see skill: 99_System\Claude\pkm-review\SKILL.md

  visualise-moc {stem}   → render the Mermaid concept-map for one MOC
                           (two tiers: overview + cluster detail).
                           reads from: VAULT_INDEX.json + the per-MOC
                                       manifest at 00_Inbox\DIAGRAM_CANDIDATES_{stem}.json
                                       (pre-extracted by extract_diagram_candidates.ps1)
                           writes to:  20_Learning\24_Diagrams\Diagram_{stem}.md
                                       (full overwrite, idempotent)
                                       + surgical patch to the MOC's ### Cluster Map subsection
                           see spec: docs\visualisation-pipeline.md

  weave-links {scope}    → discover and record cross-domain relationships
                           between concept notes that live in different MOCs
                           (a retroactive interconnection pass, distinct from
                           process-inbox Phase 4, which only routes new notes)
                           scope: one or more MOC stems or domain names
                           reads from: VAULT_INDEX.json + the source concept
                                       notes backing surviving candidate edges
                           writes to:  the `## Cross-Domain Links` section of
                                       the in-scope MOCs ONLY — never concept
                                       notes (status:final notes are locked)
                           see spec: docs\interconnect-pipeline.md

  extract-gems           → identify vault-worthy "gems" from THIS conversation
                           and route each: new candidate / one-line refinement /
                           exclude. Conversation-scoped (not index-first), so the
                           index staleness gate does not apply.
                           writes to:  00_Inbox\AI_Candidates\  (new candidates)
                                       or a one-line bullet on an existing concept
                           see skill: 99_System\Claude\gem-extraction\SKILL.md

  vault-query {question} → answer an ad-hoc vault question with a CITED,
                           synthesised answer, or admit the vault has nothing on
                           it. Hybrid retrieval (dense bge-micro-v2 + sparse BM25,
                           fused with RRF) over a gitignored, rebuildable shadow
                           index. READ-ONLY — never writes a vault note. Cites
                           every claim as [[stem]] and never fabricates.
                           corpus: 21_Concepts, 22_Maps_of_Content, 40_Solutions,
                                   10_Ideas (Note Pipe excluded)
                           see skill: 99_System\Claude\vault-retrieval\SKILL.md

If no subcommand is recognised, ask the user which command they meant.
Do not guess. Do not run the ingestion pipeline by default.

---

## BEFORE EVERY RUN

State briefly: which command, how many notes/files in scope, which MOCs will be affected.
If anything is ambiguous (unknown subcommand, missing files, unclear intent), ask — do not guess or proceed with defaults.

If the request has multiple plausible interpretations, NAME EACH ONE
and ask which is meant. Do not pick silently. Example: "build me a
deck on X" could mean (a) a composite Solution with a .pptx companion,
(b) a doc Solution with a markdown outline, (c) a Pattern abstracting
the slide-building approach. State all three and let the human pick.

---

## BEFORE EVERY process-inbox RUN

Confirm that VAULT_INDEX.json was generated today:
  Read the "generated" field from VAULT_INDEX.json.
  If it is not today's date, print:
    "⚠ Index is from {date}. Run generate_index.py first, then retry."
  and stop. Do not proceed with a stale index.

---

## BEFORE EVERY pkm-solution RUN

Same staleness gate as process-inbox: read the "generated" field from
VAULT_INDEX.json. If it is not today's date, print:
  "⚠ Index is from {date}. Run generate_index.py first, then retry."
and stop. Phase 5 retrieval is index-first — a stale index will surface
deleted notes and miss new ones.

Then restate the user's brief in one sentence and name the chosen artefact
type (Pattern or Solution) before any file read. If the brief
is unclear or the type ambiguous, ask — do not guess.

---

## BEFORE EVERY visualise-moc RUN

Same staleness gate: read the "generated" field from VAULT_INDEX.json.
If it is not today's date, print:
  "⚠ Index is from {date}. Run generate_index.py first, then retry."
and stop.

Then check the per-MOC diagram manifest at
00_Inbox\DIAGRAM_CANDIDATES_{stem}.json. If missing OR its `generated`
field is not today, print:
  "⚠ Manifest stale or missing. Re-run launch-visualise-moc.ps1
   (it will rebuild the manifest before invoking the agent)."
and stop.

Then check 00_Inbox\MMDC_MODE.txt — it must contain "global" or "npx".
If absent, the launcher's mmdc doctor check did not run. Print:
  "⚠ MMDC_MODE.txt missing. Run launch-visualise-moc.ps1, not the
   agent directly."
and stop. The agent uses this sentinel to know whether to call `mmdc`
or `npx -y @mermaid-js/mermaid-cli` for the V-4 validation loop.

---

## BEFORE EVERY weave-links RUN

Same staleness gate: read the "generated" field from VAULT_INDEX.json.
If it is not today's date, print:
  "⚠ Index is from {date}. Run generate_index.py first, then retry."
and stop. Cross-domain discovery is index-first — a stale index will
surface deleted notes and miss new ones.

Then restate the scope in one sentence — which MOCs (or domains) will be
woven together — before any file read beyond the index. If the scope is
missing, or a named domain maps to several MOCs, ASK; do not guess. A weave
needs at least two MOCs.

weave-links NEVER writes to a concept note. Every discovered edge lands in a
MOC's ## Cross-Domain Links section — Safety Rule #6 stands, because most
cross-domain targets are status:final concept notes.

---

## WINDOWS FILE OPERATION PATTERNS

Use these exact PowerShell patterns. Do not improvise alternatives.

READ a file:
  Get-Content "$env:VAULT_ROOT\path\to\file.md" -Raw -Encoding UTF8

LIST files in a folder:
  Get-ChildItem "$env:VAULT_ROOT\00_Inbox\Note Pipe" -Filter "*.md"

WRITE a new file (concept note):
  $content = @'
  {full file content here}
  '@
  Set-Content -Path "$env:VAULT_ROOT\21_Concepts\Stem_Name.md" `
              -Value $content -Encoding UTF8

APPEND to an existing file (MOC patch):
  $patch = @'
  {patch content here}
  '@
  Add-Content -Path "$env:VAULT_ROOT\22_Maps_of_Content\MOC_Name.md" `
              -Value $patch -Encoding UTF8

PATCH a specific section (replace a line in an existing file):
  $file = "$env:VAULT_ROOT\22_Maps_of_Content\MOC_Name.md"
  $content = Get-Content $file -Raw -Encoding UTF8
  $content = $content -replace 'note_count: \d+', 'note_count: {new_value}'
  Set-Content -Path $file -Value $content -Encoding UTF8

MOVE a file to QUARANTINE:
  Move-Item -Path "$env:VAULT_ROOT\00_Inbox\Note Pipe\file.md" `
            -Destination "$env:VAULT_ROOT\00_Inbox\QUARANTINE\file.md"

MOVE a fully processed file to Z_Note bin (after final batch):
  Move-Item -Path "$env:VAULT_ROOT\00_Inbox\Note Pipe\file.md" `
            -Destination "$env:VAULT_ROOT\00_Inbox\Z_Note bin\file.md"

CHECK if file exists:
  Test-Path "$env:VAULT_ROOT\path\to\file.md"

---

## FINAL CRITERIA GATE (used by process-inbox and generate-flashcards)

A note is eligible for status:final when the human has confirmed
all three in a single review pass:
  1. Core idea statable from memory in one sentence (retrieval test)
  2. All wikilinks resolve and make sense in context
  3. At least one real situation named in Application where it applies

The agent NEVER sets status:final automatically.
The agent leaves new notes at status:draft after successful write.
The human sets status:final after their review pass.
generate-flashcards only processes status:final notes.

CONCEPT RESTING STATES (no review SLA — the human is not a bottleneck):
  • draft        — the agent-written AND human-drafted resting state, and a
                   valid PERMANENT one: no time limit. A concept may stay draft
                   forever (a reference note, or content never chosen for study),
                   or rest as an agent-written note awaiting an OPTIONAL human
                   pass. Never treated as stale or nagged. The human promotes the
                   notes they choose; the rest rest indefinitely.
  • final + flashcards:false — approved; flashcards pending generation.
  • final + flashcards:true  — terminal. Either the cards were generated, OR
                   the human set flashcards:true by hand to opt the note out
                   of studying ("reviewed, no need to study"). Either way no
                   flashcards are (re)generated and it is never flagged.
  vault-health surfaces only actionable notes (final + flashcards:false); it
  never nags about a draft backlog. As gem-extraction grows vault volume, this
  keeps the human off the critical path. (There is no needs-review status —
  any legacy needs-review notes map to draft.)

See docs/lifecycle.md for the full artefact-lifecycle reference.

---
## PROCESS-INBOX PIPELINE — see docs/inbox-pipeline.md

The full PHASE 0–5 definitions for the `process-inbox` command live in:
  docs/inbox-pipeline.md

When the user invokes `process-inbox`, READ that file first, then
execute the phases as defined there. Do NOT load it for any other
command (process-inbox is the only consumer). The shared gates above
(BEFORE EVERY process-inbox RUN, FINAL CRITERIA GATE) still apply
and remain in this file.

## VISUALISE-MOC PIPELINE — see docs/visualisation-pipeline.md

The full PHASE V-0 → V-6 definitions for the `visualise-moc` command
live in:
  docs/visualisation-pipeline.md

When the user invokes `visualise-moc {MOC_stem}`, READ that file first,
then execute the phases as defined there. Do NOT load it for any other
command. The shared gates above (BEFORE EVERY visualise-moc RUN, SAFETY
RULES, WINDOWS FILE OPERATION PATTERNS) still apply and remain in this
file.

The diagram file at 20_Learning\24_Diagrams\Diagram_{stem}.md is the ONE
place in the system where a full-file overwrite is correct on every run
— the file is fully derivable from the manifest and is regenerated
idempotently. Concept notes and MOCs are still patched surgically;
Safety Rule #6 stands for status:final concept notes.

## PKM-SOLUTION PIPELINE — see 99_System\Claude\pkm-solution\SKILL.md

The full Phase 5 (Output Bridge) definitions for the `pkm-solution`
command live in:
  99_System\Claude\pkm-solution\SKILL.md

When the user invokes `pkm-solution` (or `/pkm-solution`), READ that
file first, then execute the phases as defined there. Do NOT load it
for any other command. The shared gates above (BEFORE EVERY
pkm-solution RUN, SAFETY RULES, WINDOWS FILE OPERATION PATTERNS) still
apply and remain in this file.

Reference for the Phase 5 process as a whole (artefact types, templates,
validation rules) is the human-readable spec at:
  40_Solutions\Personal Knowledge Management System - Solution.md

The skill file is the authoritative agent spec; the spec doc is the
human reference. (The spec doc lives in 40_Solutions/ as a Solution
because it IS the realised PKM system, not merely a hypothesis.)

## WEAVE-LINKS PIPELINE — see docs/interconnect-pipeline.md

The full PHASE IC-0 → IC-6 definitions for the `weave-links` command live
in:
  docs/interconnect-pipeline.md

When the user invokes `weave-links` (with a scope of MOC stems or domains),
READ that file first, then execute the phases as defined there. Do NOT load
it for any other command. The shared gates above (BEFORE EVERY weave-links
RUN, SAFETY RULES, WINDOWS FILE OPERATION PATTERNS) still apply and remain in
this file.

weave-links is the only command that retroactively connects notes already in
the vault. Its discovered edges live exclusively in MOC ## Cross-Domain Links
sections, in the canonical prose-verb format
([[A]] <label> [[B]] (in [[MOC_X]])) using the closed 7-label vocabulary.
Safety Rule #6 stands: concept notes are never edited by this pipeline.

════════════════════════════════════════════════════════════════
SAFETY RULES (enforced at every write operation)
════════════════════════════════════════════════════════════════
1. Never overwrite a vault file's full content. Patch only the
   specific section being changed.

2. A wikilink is valid only if the exact text exists in
   VALID_NOTES, VALID_MOCS, or VALID_EXTERNAL_MOCS.

3. When processing a batch, check each new note's title against
   all other new titles in the same batch — not just the index.
   A note written in this batch is a valid wikilink target for
   other notes in the same batch.

4. Never delete an inbox file. Move fully processed files to
   00_Inbox\Z_Note bin\ only — do not delete them.

5. Never write a note that would create a broken wikilink in an
   existing MOC. If the MOC references a title that does not yet
   exist in VALID_NOTES, add it to the MOC as plain text with
   (not yet in vault: "Title") — do not write [[Title]].

6. NEVER modify a concept note that has status:final unless the
   user explicitly asks for that specific change. The ONLY edits
   allowed to a status:final note during any pipeline are:
     a. flashcards: false → flashcards: true   (PHASE GF-3 patch)
     b. updated: <prior date> → updated: <today>   (PHASE GF-3 patch)
   No other change is permitted — not formatting, not structure,
   not "fixing" labels, not adding/removing sections, not
   prepending frontmatter, NOTHING. If a status:final note is
   structurally malformed (missing fields, legacy labels), SKIP
   it and report the issue. Do not silently auto-correct.

   When patching, use targeted regex replacements that match the
   exact line being changed. Never use file rewrites or full-file
   templating that could re-emit the file in a different shape.
   Always Test-Path the original to confirm shape before writing.

7. NEVER MAKE INFORMATION UP. ALWAYS REFER TO THE EXISTING INFO.
   When generating any derivative content from vault notes -
   flashcards, summaries, MOC entries, cross-domain links, reports
   - every factual claim, metaphor, boundary condition, example,
   and "when to use" recommendation MUST originate from the source
   note. Do not embellish, do not interpolate, do not "fill gaps"
   with plausible-sounding content. If a field is empty in the
   source, either omit the corresponding part of the output or
   skip the item entirely. Hallucinated content that ends up in a
   flashcard or MOC is worse than missing content because the user
   then learns and references something false.

8. SURGICAL CHANGES ONLY. Every changed line must trace directly to
   the user's request. Do not "fix" adjacent code, comments,
   formatting, or unrelated files while doing other work. If you
   notice something unrelated that needs fixing, mention it - do
   not silently change it. When patching an existing file, prefer
   targeted edits over full-file rewrites even if both produce the
   same end state: the diff itself is part of the audit trail, and
   a smaller diff is easier to review, revert, and trust. Also do
   not expand scope beyond what was asked - if the user said "add
   X", do not also add Y because Y "would be nice"; ask first.

════════════════════════════════════════════════════════════════
GENERATE-FLASHCARDS PIPELINE
════════════════════════════════════════════════════════════════

DESIGN
  Output is per-MOC per batch. The first run for an MOC writes
  Flashcards_{moc_stem}.md; every subsequent run writes a NEW
  file named "Flashcards_{moc_stem} - Batch {N}.md" (N = 2, 3, ...).
  Never append to, rewrite, or reorder cards in a previously
  written flashcard file. The flashcards-obsidian plugin inserts
  <!--ID:nnn--> markers after each card on first Anki sync;
  appending to a file that has already been synced (or that the
  plugin thinks it has synced) triggers the AnkiConnect silent-
  fail duplicate trap, which leaves new cards out of Anki without
  surfacing an error. One file per batch isolates each sync.
  Folder-based deck routing keeps every batch file in the same
  Anki sub-deck regardless of filename.

  Cards use the inline format with the :: separator (matches the
  plugin's inlineSeparator setting). Three dense cards per concept:
  WHAT (definition + metaphor + boundary), HOW (mechanism + key
  insight), WHEN (when to use + when NOT to use).

────────────────────────────────────────────────────────────────
PHASE GF-0 — LOAD INDEX AND IDENTIFY CANDIDATES (once per run)

  Read VAULT_INDEX.json.
  Parse VALID_NOTES as normal.

  CANDIDATES = notes where:
    status     == "final"     AND
    reviewed   == true         AND
    flashcards == false

  All three flags must be set. status:final means the note structure
  is locked; reviewed:true means the human has read it through and
  approved it for downstream use; flashcards:false means a card has
  not yet been generated. Any note missing one of the three is not
  eligible.

  If CANDIDATES is empty:
    Print: "No final reviewed notes need flashcards - nothing to process."
    Stop.

  Print: "Generating flashcards for {N} concept(s) across {M} MOCs."

────────────────────────────────────────────────────────────────
PHASE GF-1 — LOAD CANDIDATE MANIFEST (one file read, not N)

  Read the pre-extracted manifest:
    00_Inbox\FLASHCARD_CANDIDATES.json

  This file is generated by extract_flashcard_candidates.ps1 (run by
  the launch script before the agent starts). It contains every
  eligible candidate with these fields already parsed:

    stem          - filename stem (no .md)
    title         - frontmatter title
    moc_stem      - first entry in moc: list
    humanized_moc - "Learning and Memory" form (for the file header)
    description   - frontmatter description
    core          - lead prose of ## Core Idea (Summary), without the
                    **Metaphor:**/**Example:** sub-blocks
    metaphor      - extracted **Metaphor:** value, multi-line capable,
                    or null if not present (do NOT invent one)
    mechanism     - full ## Mechanism (Key details) section text
                    (includes bullets and the boundary line - the
                    boundary is also provided separately)
    boundary      - extracted **Boundary condition:** value, or null
    when_to       - extracted **When to use:** value, or null
                    (legacy fallback to **Strengths:** applied)
    when_not      - extracted **When NOT to use:** value, or null
                    (legacy fallback to **Opportunities:** /
                    **Limitations:** applied)
    is_stub       - true if the note appears to be a navigation stub
                    (core says "has been split into", description
                    matches /stub/, etc.) - the agent must ASK the
                    user before processing flagged stubs
    stub_reason   - human-readable reason the note was flagged
    has_required  - true if the minimum required fields are present:
                    title AND moc_stem AND core AND
                    (when_to OR when_not)

  DO NOT open the source .md files. Reading from the manifest is the
  entire point - it cuts ~50% of extraction-phase tokens by avoiding
  N round trips.

  If the manifest is missing or its `generated` date is not today,
  run the extraction script first:
    powershell -ExecutionPolicy Bypass -File `
      "$env:VAULT_ROOT\extract_flashcard_candidates.ps1"
  Then read the freshly written manifest.

  Eligibility recap:
    Per GF-0, a note is eligible if status:final AND reviewed:true AND
    flashcards:false. The extraction script enforces this filter.

  STUB HANDLING (interactive):
    If any candidate has is_stub == true, ASK the user before
    processing those candidates:
      "{N} note(s) flagged as navigation stubs: {list}.
       Skip these, or generate stub-cards anyway?"
    Wait for response. Default if unclear: skip.

  REQUIRED-FIELDS GATE (silent):
    For every candidate where has_required == false, log:
      "⚠ {stem}: missing {fields} - skipping."
    and skip. Do not write partial cards.

  TRUTHFULNESS RULE (applies to ALL card generation):
    NEVER make information up. NEVER add facts, examples, metaphors,
    boundaries, or claims that are not in the source manifest fields.
    If a field is null, the corresponding card content must come from
    a different field that IS populated, or the card section must be
    omitted entirely. Hallucinated content in flashcards is worse
    than missing content - it teaches the user something false.

────────────────────────────────────────────────────────────────
PHASE GF-2 — GROUP BY MOC AND WRITE BATCH FILE

  Target folder : 20_Learning\23_FlashCards\
  Target file   : a NEW file per run, named by batch number:
                    Batch 1  → Flashcards_{moc_stem}.md
                    Batch N (N≥2) → "Flashcards_{moc_stem} - Batch {N}.md"

  Determine N before writing:
    base = "Flashcards_{moc_stem}.md"
    pattern = "Flashcards_{moc_stem} - Batch *.md"
    If neither base nor any pattern match exists → N = 1, file = base
    Else N = (highest existing batch number for this MOC) + 1, where
      base counts as batch 1 and each "- Batch K.md" contributes K.
      File = "Flashcards_{moc_stem} - Batch {N}.md".
    Never overwrite an existing flashcard file. If the chosen filename
    already exists, abort with an error - do not silently bump N
    further, as that hides a prior failed run.

  Group successfully-extracted candidates by moc_stem.

  For each MOC group:

    Create the batch file fresh with this header (and a single blank
    line, no cards yet). The title carries the batch suffix only when
    N ≥ 2; for batch 1 the title is plain "Flashcards - {humanized moc_stem}".

        ---
        title: Flashcards - {humanized moc_stem}
        type: flashcard-batch
        moc: [{moc_stem}]
        created: {today}
        tags:
          - card
        ---

        # Flashcards - {humanized moc_stem}


      Where humanized moc_stem strips the leading "MOC_" and replaces
      underscores with spaces. Example: MOC_Learning_and_Memory →
      "Learning and Memory".

    For each candidate in this group, write adaptive card blocks
    after the header (in encounter order). Each card is structured as:
      `#card` on its own line, then `Question :: Answer` on the next
      line, then a blank line before the next card.

    Three cards per concept maximum. Question phrasing adapts to the
    concept's grammar (singular/plural, action verb fits the concept):

      Card 1 - WHAT (always emitted if the concept is eligible):
        #card
        What is/are {Title}? :: {dense prose definition that names what
        it is, weaves in metaphor naturally if present, names the key
        behaviour or property, and ends with the boundary condition
        woven into the prose. 3-5 sentences. Use plain prose - NO
        bold labels like **Metaphor:** or **Boundary condition:**.}

      Card 2 - HOW (emit only if mechanism is non-empty):
        #card
        How does/do {Title} work? :: {dense prose mechanism explaining
        the chain of cause and effect, with the most important insight
        woven in. May use inline "Key insight:" or "Boundary condition:"
        WITHOUT bold formatting. 3-5 sentences. No bullets.}

      Card 3 - WHEN (emit if when_to OR when_not is present; phrasing
      adapts to the concept):
        - Both when_to AND when_not present:
            #card
            When and why would you use/apply/act on {Title}{ deliberately|
            in practice | knowledge}? :: {Action recommendation in prose}.
            Do NOT {counter-action in prose}. {Goal or principle
            clarification.} 2-4 sentences.
        - Only when_to present:
            #card
            When should you use {Title}? :: {Action recommendation in
            prose - 1-2 sentences.}
        - Only when_not present:
            #card
            When should you avoid {Title}? :: Do NOT {counter-action
            in prose - 1-2 sentences.}

  Question phrasing rules:
    - Concept name appears BARE in the question - no quotes around it
    - "What is" for singular nouns, "What are" for plural (Endorphins)
    - "How does" for singular, "How do" for plural
    - Card 3 verb adapts: "use ... deliberately" for hormones/tools,
      "act on ... knowledge" for diagnostic concepts, "apply" for
      frameworks - pick the verb that reads naturally for the concept

  Card body rules:
    - Plain prose paragraphs. NO markdown bold labels like
      **When to use:** or **Metaphor:** or **Boundary condition:**.
    - Inline lowercase labels are fine when natural ("Boundary
      condition: ...", "Critical boundary condition: ...", "Key
      insight: ...") but use sparingly - prefer woven prose.
    - Use "Do NOT" in caps for the counter-case in Card 3.
    - Replace em-dashes (—) with " - " (space hyphen space).
    - No bullet points, no headings, no wikilinks inside card bodies.
    - Each card body: 3-5 dense sentences. Compress without losing
      the core mechanism, metaphor, or boundary.

  Reference example - Cortisol (Biology of Performance MOC):

    #card
    What is Cortisol? :: Cortisol is a temporary survival mechanism
    that prepares the body for fight-or-flight - it increases heart
    rate and mobilises resources for immediate threat response. It
    becomes highly destructive when chronic: it suppresses the immune
    system, completely blocks oxytocin release, and makes empathy
    biologically impossible. It is also highly contagious - a single
    panicked leader can cascade cortisol through an entire team
    within minutes.

    #card
    How does Cortisol work? :: Cortisol spreads through a team via
    visible panic - a single dysregulated leader activates the
    stress response in everyone around them. The reverse is equally
    true: a calm, grounded leader actively suppresses cortisol
    spread, making emotional self-regulation a structural team-safety
    function, not merely a personal virtue. Chronic cortisol blocks
    oxytocin and destroys team empathy. Acute cortisol - short and
    bounded - is adaptive and sharpens focus.

    #card
    When and why would you act on Cortisol knowledge? :: Recognise
    when cortisol is spreading and de-escalate: eliminate chronic,
    unnecessary stressors - your team will biologically lose the
    ability to trust one another under sustained exposure. Do NOT
    attempt to eliminate all stress - acute, short-duration cortisol
    (a deadline, a high-stakes pitch) is adaptive and healthy. The
    goal is to prevent chronic elevation, not create a zero-stress
    environment, which removes the performance benefit of
    appropriate arousal.

  Minimum 1 card per concept (the WHAT card). Maximum 3.
  If the concept yielded only the WHAT card, log:
    "ⓘ {stem}: 1 card only (no mechanism, no when_to/when_not)."
  ...even though that case shouldn't pass the GF-1 eligibility gate
  (which requires at least one of when_to/when_not).

  WRITE DISCIPLINE — critical for Anki ID stability:
    1. Always create a NEW file with Set-Content -Encoding UTF8.
       Never read, append to, or rewrite a pre-existing flashcard
       file - not even to "fix" formatting.
    2. Confirm the chosen filename does not already exist before
       writing (Test-Path). If it does, abort with an error.
    3. Once the plugin syncs the file and writes back <!--ID:nnn-->
       markers, treat that file as immutable. The next generation
       run produces a separate batch file.

  GF-2 RUN TABLE — output at the end of GF-2, before moving to GF-3.
  This is the at-a-glance audit of what was just written. The user
  scans this table to verify each concept's three cards landed in the
  expected MOC file with the expected status.

  Format:
  | MOC | Concept | What | How | When | Status & comment |

  Column rules:
    MOC      — humanized MOC name (e.g. "Learning and Memory")
    Concept  — concept stem (e.g. "Active_Recall")
    What     — ✓ written | — skipped | ⚠ flagged
    How      — ✓ written | — skipped | ⚠ flagged
                (— if mechanism manifest field was null)
    When     — ✓ written | — skipped | ⚠ flagged
                (— if both when_to and when_not were null)
    Status   — short comment per row, e.g.:
                "All 3 cards written"
                "2/3 - HOW skipped (no mechanism in source)"
                "Skipped - missing required fields: when_to_or_not"
                "Skipped - flagged stub, user declined"
                "Skipped - flagged stub, user accepted (3 stub cards)"

  One row per ELIGIBLE candidate (from GF-1), including those that
  were skipped at GF-1 or GF-2. Group rows by MOC for readability.

  After the table, also print a one-line totals summary:
    "Generated: X concepts (Y cards) | Skipped: Z | MOC files touched: M"

────────────────────────────────────────────────────────────────
PHASE GF-3 — PATCH SOURCE NOTES  (flashcards: false → true)

  For each candidate whose 3 cards were successfully appended:
    Patch 20_Learning\21_Concepts\{stem}.md:
      $content = $content -replace 'flashcards: false', 'flashcards: true'
      $content = $content -replace 'updated: \d{4}-\d{2}-\d{2}', "updated: $today"

  Patch only sources whose cards were actually written this run.
  Never patch a source that was skipped.

────────────────────────────────────────────────────────────────
PHASE GF-4 — REPORT

  Two outputs: a markdown table in the agent transcript (for log
  history) and a JSON results file the launch script renders as a
  console-aligned table (for at-a-glance terminal review).

  (a) MARKDOWN TABLE — print to the transcript using the canonical
  GF-2 columns, augmented with post-patch status:
      | MOC | Concept | What | How | When | Status & comment |

  Status & comment reflects the FINAL state after GF-3:
    "All 3 cards written, source patched"
    "2/3 cards written, source patched - HOW skipped (no mechanism)"
    "Skipped - missing required fields (source NOT patched)"
    "Skipped - stub declined by user (source NOT patched)"
    "Cards written but source patch FAILED - manual review required"

  Group rows by MOC. After the table, print one totals line:
    "Generated: X concepts (Y cards) | Sources patched: P |
     Skipped: Z | MOC files touched: M"

  (b) JSON RESULTS FILE — write to:
      00_Inbox/FLASHCARD_RUN_RESULT.json

  Schema:
    {
      "generated": "YYYY-MM-DD",
      "rows": [
        {
          "moc":     "Learning and Memory",
          "concept": "Active_Recall",
          "what":    "✓",   // ✓ written | — skipped | ⚠ flagged
          "how":     "✓",
          "when":    "✓",
          "status":  "All 3 cards written, source patched"
        },
        ...
      ],
      "totals": {
        "concepts_generated":  N,
        "cards_total":         3*N approx,
        "sources_patched":     P,
        "skipped":             Z,
        "moc_files_touched":   M
      }
    }

  Sort `rows` by moc then concept. Use UTF-8 encoding (no BOM).
  The launch script reads this and renders a console-aligned table
  after Claude returns, so the user can scan results without scrolling
  back through the transcript.

  DO NOT re-output card content - it is already in the MOC files.

────────────────────────────────────────────────────────────────
FLASHCARD FORMAT NOTES (flashcards-obsidian plugin)
  - Each card uses the two-line block format:
        #card
        Question? :: Answer text.
    The standalone "#card" line tags the next line as a flashcard;
    the plugin parses the front/back via the :: separator.
  - inlineSeparator is :: (configured in plugin data.json).
  - flashcardsTag is "card" (configured in plugin data.json).
  - folderBasedDeck is ON — files in 20_Learning/23_FlashCards/ land
    in the "20_Learning::23_FlashCards" Anki sub-deck.
  - On first sync the plugin appends ^NNNNNNNNNNNNN (13-digit Anki
    note ID) on the line below each card. On re-sync it matches by
    ID, updating Anki when the markdown changes. NEVER edit, reorder,
    or remove these IDs or their cards become orphaned.
  - SILENT-FAIL TRAP: AnkiConnect rejects "duplicates" (notes whose
    front field matches an existing card in any deck under the same
    note model). When this happens the plugin shows ONLY "Nothing to
    do, everything is up to date" - the duplicate errors appear in
    the dev console (Ctrl+Shift+I), not the UI. If sync produces no
    IDs in the file after a successful-looking run, check the
    console for "cannot create note because it is a duplicate" and
    delete the orphan Anki cards via Browse before re-syncing.


## 文件 99_System/Claude/gem-extraction/SKILL.md

﻿---
name: extract-gems
description: Identifies vault-worthy "gems" produced during a conversation with Claude and routes each to the right destination - a new AI_Candidate, a one-line refinement of an existing note, or exclude. Use when the user asks to extract or capture gems, run the gem-capture / gem-identification process, check whether a conversation produced something vault-worthy, or formalise an insight into the KZN vault; also offer it proactively at the end of a substantive conceptual conversation. Do NOT fire for coding tasks, drafting help, sanity checks, or short (<20-message) chats.
---

# extract-gems - post-conversation gem identification

Turns insight produced in a Claude conversation into vault artefacts, conservatively.
This skill supplies the *when* and the *routing* around the canonical prompt and
candidate template in `99_System/EXTRACT_PROMPT.md` - read that file; do not duplicate
its template here.

Conversation-scoped, not index-first: it reasons over THIS chat, verifies any vault
references by direct read, and writes at most one candidate file plus (optionally) one
one-line note patch. A stale VAULT_INDEX.json therefore does NOT block this skill - the
staleness gate exists to protect index-first retrieval, which this is not.

## When to run

Fire on an explicit request ("extract/capture gems", "run gem capture", "is this
vault-worthy", "formalise this insight"), or offer proactively after a substantive
conceptual conversation. Apply the heuristic honestly first: did the conversation
produce something the user could not have articulated at the start - genuinely new in
framing, mechanism, or connection - not a synthesis of what they already knew, and not a
nicely-worded version of an existing idea? Most conversations fail this bar; that is the
expected outcome.

Do NOT fire for: coding/drafting/sanity-check sessions; conversations where Claude only
restated the user's own input; chats under ~20 messages; or where the insight feels like
agreeableness rather than substance.

## How to run

**G-0 Heuristic gate.** Apply the bar above. If nothing clears it, output exactly:
`Nothing in this conversation rises to vault-worthy. Reasons: [brief]` and stop.

**G-1 Distill.** Write each surviving idea as a one/two-sentence decontextualized
statement in the user's voice.

**G-2 Vault dedup check.** For each candidate, name the closest existing concept note(s)
/ MOC and read them directly to confirm. This is the step that prevents
reworded-existing-idea pollution.

**G-3 Disposition and route.** Classify each candidate per the table in
`EXTRACT_PROMPT.md` -> Disposition and Routing:
- **New** - nothing covers it -> one sharpest candidate to `00_Inbox/AI_Candidates/`.
- **Refinement** - sharper/extended version of an existing concept -> one-line patch on
  that note (not a new candidate).
- **Already captured** - written into an artefact during this same conversation -> exclude.
- **Operational / tooling** - about the PKM machinery, not domain knowledge -> propose a
  `CLAUDE.md`/`SKILL.md` edit, not a vault note.

**G-4 Write.**
- *New*: file `00_Inbox/AI_Candidates/YYYY-MM-DD-{slug}.md` using the EXTRACT_PROMPT.md
  template (`status: proposed`, `source: claude-chat-YYYY-MM-DD`). `Test-Path` first;
  never overwrite. AI_Candidates is not scanned by generate_index.py - no index churn.
- *Refinement*: guarded literal patch on the concept note - add one bullet **before** the
  `**Boundary condition:**` line in `## Mechanism`, bump `updated`. Confirm the anchor
  matches exactly once before writing. **Only if `status: final` is NOT set**; for a final
  note add a `## Cross-Domain Links` entry on its MOC instead — and if the note is in
  multiple MOCs, add it to the MOC whose Core Question the refinement speaks to (or to
  each such MOC if it speaks to several).
- *Exclude / tooling*: report only, or draft the CLAUDE.md/SKILL.md change.

**G-5 Report and stop.** List each candidate and its disposition. New candidates wait for
the user's weekly review - never promote into `20_Learning/21_Concepts/` here (that is process-inbox's
job, after the cooling period).

## Safety
- One sharpest New candidate only; demote the rest to Refinement or Exclude.
- Precision over recall - default to Exclude when unsure.
- Never edit a `status: final` concept note (CLAUDE.md Safety Rule 6).
- PowerShell `Set-Content -Encoding UTF8`; literal guarded patches; never full-file rewrites.
- Do not run the inbox pipeline and do not set `status: final`.


## 文件 99_System/Claude/pkm-flashcards/SKILL.md

---
name: pkm-flashcards
description: Generates Anki-ready flashcard files from finalised Obsidian concept notes. Use this skill whenever the user asks to generate flashcards, create Anki cards, process final concept notes into cards, or mentions Annex 4, the flashcard pipeline, or spaced repetition export. Also trigger when the user marks a note as final and asks what happens next, or when the user provides a set of concept notes and asks for retention materials. This skill produces one consolidated .md file per MOC routed to the correct Anki deck via card-deck frontmatter.
---

# PKM Flashcard Generation Skill

Generates 3 Anki flashcards per finalised concept note (Definition, Mechanism, Application) and writes them into a single consolidated `.md` file per MOC. The file is placed in `20_Learning/23_FlashCards/` and syncs to Anki via the Flashcards plugin.

## Trigger condition

A concept note is eligible for flashcard generation when:
- `status: final` in its YAML frontmatter
- `flashcards: false` (not yet generated)

Notes with `status: draft` are skipped and logged —
it is a valid permanent resting state, not an error. A note with `status: final`
and `flashcards: true` is also skipped: `flashcards: true` means the cards
already exist OR the human opted the note out of studying (reviewed, no cards
needed). Never generate cards for it.

---

## Input

One or more concept notes. Read the following fields from each:
- `title` — used for card questions and filename
- `moc` — used to derive the Anki deck name
- Core Idea (Summary) — source for Definition card
- Mechanism (Key details) — source for Mechanism card
- Application (When to use / When NOT to use) — source for Application card

---

## Deck name derivation

Derive the Anki deck name from the note's `moc` YAML field:
1. Take the first MOC listed
2. Strip the `MOC_` prefix
3. Replace underscores with spaces

Examples:
- `MOC_Biology_of_Performance` → `Biology of Performance`
- `MOC_Learning_and_Memory` → `Learning and Memory`
- `MOC_Presentations_That_Drive_Action` → `Presentations That Drive Action`

---

## File behaviour

**If `20_Learning/23_FlashCards/{MOC name}.md` already exists:**
Append the new cards to the end of the existing file. Do not overwrite.

**If the file does not exist:**
Create it with the frontmatter block and the new cards.

---

## Output format — consolidated file per MOC

```markdown
---
card-deck: {MOC name derived above}
---

#card
{Question 1} :: {Answer 1}

#card
{Question 2} :: {Answer 2}
```

### Critical structural rules

| Rule | Why it matters |
|---|---|
| Opening `---` before `card-deck:` | Tells Obsidian this is metadata, not card content |
| Closing `---` after `card-deck:` | Closes the metadata block |
| `#card` alone on its own line | Tag is the trigger — must not be inline with the question |
| Question and answer on one continuous line | Plugin splits on `::` within a single line; hard line breaks end the card |
| One blank line between cards | Separates card blocks without breaking the parser |
| No em-dashes (—) in card content | Use regular hyphen with spaces ( - ) instead |

---

## Three card templates

### Card 1 — Definition
**Question format:** `What is {Concept Name}?`
**Answer format:** Core claim in 1-2 sentences. Bold labels for inline structure.

```
#card
What is {Concept}? :: {Core claim}. **Metaphor:** {metaphor if applicable}. **Boundary condition:** {when it breaks down}.
```

### Card 2 — Mechanism
**Question format:** `How does {Concept Name} work?`
**Answer format:** The causal chain. Must include boundary condition.

```
#card
How does {Concept} work? :: {Causal chain or key mechanics}. **Key mechanic:** {most important detail}. **Boundary condition:** {when the mechanism breaks down or reverses}.
```

### Card 3 — Application
**Question format:** `When and why would you use {Concept Name}?`
**Answer format:** When to use then When NOT to use. Both must be specific.

```
#card
When and why would you use {Concept}? :: **When to use:** {specific context}. **When NOT to use:** {specific counter-case — name the situation explicitly}.
```

---

## Answer quality rules

1. The answer must be self-contained — the reader should not need to open the concept note to understand it.
2. Boundary condition is mandatory in the Mechanism card. A card without it creates an incomplete mental model.
3. Do not copy the Core Idea verbatim as the Definition answer — paraphrase so the brain must reconstruct, not recognise.
4. `When NOT to use` must name a specific context, not a vague qualifier. Bad: "when it doesn't apply." Good: "when the environment is chronically stressful and the structural cause hasn't been addressed."
5. Every answer stays on one continuous line — no hard line breaks inside the answer.
6. No em-dashes anywhere in card content.

---

## Post-generation step

After writing the cards, update the source concept note's YAML:
```yaml
flashcards: true
updated: {today's date}
```

---

## Report

```
## Flashcards generated
| Note | Deck | Cards added | File |

## Skipped
| Note | Reason |
```


## 文件 99_System/Claude/pkm-ingestion/SKILL.md

---
name: pkm-ingestion
description: Processes raw inbox notes into atomic Obsidian concept notes and updates Maps of Content. Use this skill whenever the user asks to process inbox notes, generate concept notes, run the Sunday pipeline, ingest NotebookLM output, convert flying notes into vault notes, or mentions CLAUDE.md, the PKM pipeline, or batch processing notes. Also trigger when the user pastes raw Gist/Evidence/Debate structured text or Concept/Why it matters flying note format. This skill enforces the full validate_note() quality gate before any file is written.
---

# PKM Ingestion Skill

Processes raw inbox notes into atomic Obsidian concept notes following the Feynman template, then updates the relevant Maps of Content. Runs as a weekly Sunday batch but can be triggered manually for any set of raw notes.

---

## Authoritative phase definitions

The full Phase 0–5 pipeline rules — classification, audit (including Unflagged acronym + Domain inheritance), build, MOC update, report — live in:

    docs/inbox-pipeline.md

**READ that file first when this skill is invoked.** Do not execute any phase without the authoritative rules from that document. The phase definitions there are the single source of truth; this SKILL.md is the entry point, not the definition.

If anything in `docs/inbox-pipeline.md` appears to conflict with the safety rules in `CLAUDE.md`, CLAUDE.md wins and the conflict is flagged to the user before proceeding.

---

## Inputs required before starting

- `[RAW NOTES]` — raw text from `00_Inbox/Note Pipe/` (any format, but structurally complete)
- `[VAULT_INDEX]` — contents of `00_Inbox/VAULT_INDEX.json` (pre-generated by `generate_index.py`; must be today's date per CLAUDE.md staleness gate)
- `[ACRONYM_ALLOWLIST]` — `99_System/acronym_allowlist.md` (read for the Phase 2 Unflagged acronym audit)
- `[TEMPLATES]` — concept and MOC templates in `99_System/` (used by Phase 3 build)

**Important:** Only scan `00_Inbox/Note Pipe/`. Do not process anything in `00_Inbox/Note Stock/` — that folder is human territory for notes still being completed.

**Do not scan the vault.** Read VAULT_INDEX.json, raw notes, the acronym allowlist, and templates — nothing else.

---

## Outputs

- New concept notes in `20_Learning/21_Concepts/` (status: `draft`)
- MOC patches in `20_Learning/22_Maps of Content/` (insertions only, never rewrites)
- Run report: exceptions, quarantines, MOC candidates, vault gaps surfaced from Phase 2 audit
- Files moved between `00_Inbox/Note Pipe/` and `00_Inbox/Z_Note bin/` on successful processing, or `00_Inbox/QUARANTINE/` on validate_note() failure

All operational rules — classification criteria, audit columns, validators, safe_stem derivation, wikilink rule, MOC update logic, report shape — are in `docs/inbox-pipeline.md`. This file delegates to it intentionally to eliminate the drift that existed prior to 2026-05-20 between two parallel copies of the phase rules.

---

## Safety

CLAUDE.md safety rules 1–8 apply to every operation in every phase. They are not duplicated here for the same reason the phase rules are not: a single source of truth prevents drift.


## 文件 99_System/Claude/pkm-review/SKILL.md

---
name: pkm-review
description: Performs periodic vault health checks, surfaces notes needing review, audits MOC coverage, and manages the VAULT_INDEX.json. Use this skill whenever the user asks to review the vault, check which notes need attention, find stale or unreviewed notes, audit MOC completeness, update the vault index, check flashcard coverage, find orphaned notes, surface open questions across MOCs, or asks what needs to be done in the vault. Also trigger when the user asks for a vault summary, a progress report, or mentions the Delegation Diligence Loop in the context of their PKM system.
---

# PKM Vault Review Skill

Performs structured vault health checks and surfaces actionable items. Reads from `VAULT_INDEX.json` and targeted note files — does not scan the full vault on every run.

## Review types

Call the relevant section based on what the user requests. For a full health check, run all sections.

---

## Review 1 — Actionable notes

The vault has NO review SLA. `draft` is a valid, permanent
resting state with no time limit. A concept may stay `draft` forever — it
might be a reference note never meant to be studied, or content not yet chosen
for promotion. Volume is expected to be high (gem-extraction feeds the vault
faster than any human can attentively review), and the human is deliberately
NOT the throughput bottleneck. Unreviewed notes are therefore NEVER flagged as
"stale" or "needing attention" on age.

Surface ONLY genuinely actionable notes:
- `flashcards: false` AND `status: final` AND `concept_role: study` (or absent —
  `study` is the default) → approved and awaiting flashcards (run
  `generate-flashcards`). Not raised for notes the human has opted out of
  studying via `flashcards: true` (see Review 3). **Never raised for
  `concept_role: reference` or `concept_role: scaffold`** — those are kept for
  lookup or structure, not study, so `flashcards: false` on them is the correct
  terminal state, not a gap.

Output format:
```
## Actionable notes
| Title | Type | Status | Issue |
| Chunking | concept | final | Approved — flashcards not yet generated |
```

For visibility only — never as a to-do list — the summary may report how many
notes sit in each state (see the Summary section).

---

## Review 2 — MOC coverage audit

For each MOC in `VAULT_INDEX.json`:
1. Count how many concept notes list this MOC in their `moc` field
2. Flag any MOC with fewer than 4 notes (below minimum viable cluster)
3. Flag any concept note with `moc: []` (orphaned — not assigned to any MOC)
4. Check if any MOC has not been updated in 60+ days

Output format:
```
## MOC coverage
| MOC | Note count | Last updated | Flag |
| Biology of Performance | 15 | 2025-03-01 | — |
| Prose Momentum | 2 | 2024-11-12 | Below threshold (min 4) |

## Orphaned notes (no MOC assigned)
| Title | Domain | Suggested MOC |
```

---

## Review 3 — Flashcard coverage

For each finalised concept note (`status: final`) with `concept_role: study`
(or no `concept_role` — `study` is the default):
- Check `flashcards` field
- If `flashcards: false`, flag it (approved, cards still to be generated)

Skip `concept_role: reference` and `concept_role: scaffold` notes entirely —
they are not study material, so `flashcards: false` on them is correct and is
never a coverage gap.

`flashcards: true` on a final note is terminal and is NEVER flagged: it means
either the cards were generated OR the human deliberately opted the note out of
studying ("reviewed, no need to study"). Do not expect a flashcard file to
exist for such a note, and never treat its absence as a gap.

Also check `20_Learning/23_FlashCards/` for consolidated files:
- List which MOC decks exist
- Flag any MOC that has `status: final` + `flashcards: false` +
  `concept_role: study` notes but no flashcard file (a real coverage gap —
  opted-out `flashcards: true` notes and `reference`/`scaffold` notes do not
  count)

**Sync-reality check (loop A — closes the silent-fail gap).** A note can be
marked `flashcards: true` while its cards never reached Anki (the documented
AnkiConnect duplicate trap). A successfully synced flashcard file contains Anki
ID markers (`<!--ID:` or a `^NNNNNNNNNNNNN` line). So:
- For each file in `20_Learning/23_FlashCards/`, check for at least one Anki ID
  marker. **Flag any flashcard file that has ZERO ID markers** — its cards are
  not in Anki. (Cross-check `00_Inbox/FLASHCARD_RUN_RESULT.json` →
  `sync_verification[]` if present: any `synced: false` entry is a confirmed
  silent-fail to re-sync.)
- This is a committed-artefact gap (cards were written but not landed), so it IS
  surfaced — distinct from the never-nagged draft backlog.

Output format:
```
## Flashcard coverage
| MOC | Final notes | Flashcard file exists | Notes without cards |

## Flashcard sync gaps (loop A)
| Flashcard file | Anki IDs present? | Action |
| Flashcards_Threat_Protection - Batch 2.md | NO | Re-sync; check dev console for duplicate errors |
```

---

## Review 4 — Open questions surface

Scan each MOC file's `## Open Questions` section.
Collect all open questions across all MOCs.
Group by domain and sort by MOC.

Output format:
```
## Open questions across vault
### {MOC name}
- {Question 1}
- {Question 2}
```

Use this to identify where new source material or concept notes would have the highest impact.

---

## Review 5 — MOC candidate detection

Scan concept notes with `moc: []` or notes in `SATELLITE` status.
If 3 or more unassigned notes share a domain, flag as a MOC candidate.

Output format:
```
## MOC candidates
| Cluster | Notes | Suggested title |
| Personal Positioning | Prime Real Estate, Dialect Mirroring, The Presentation Halo Effect, AMR Framework | MOC_Personal_Positioning |
```

---

## Review 6 — Vault gap scan (acronyms + missing concepts)

Surface acronyms and technical terms used in `status:final` concept notes that have no matching vault concept and no inline expansion. Catches gaps that escaped the ingestion-time audit (e.g. acronyms in Mechanism or Application sections from older runs, or terms the agent silently treated as "general knowledge").

**Never edits any concept note** — Rule 6 makes final notes immutable except for the two GF-3 patches. This review only writes the report.

### Inputs

- `00_Inbox/VAULT_INDEX.json` — `notes[]`, `patterns[]`, `decisions[]`, `solutions[]`, `ideas[]` (for matching against vault terms; staleness gate applies)
- `99_System/acronym_allowlist.md` — the `allowlist:` YAML list (skipped from flagging)
- Concept note files at `20_Learning/21_Concepts/*.md` where `status: final`

### Procedure

1. **Build `VALID_TERMS`** — union of every `stem`, `title`, and entry from `aliases[]` across `notes`, `patterns`, `decisions`, `solutions`, `ideas`. Lowercase for comparison.

2. **Load `ALLOWLIST`** — parse the `allowlist:` field from `99_System/acronym_allowlist.md` frontmatter. Lowercase entries.

3. **For each `status: final` concept note**:
   a. Read the file. Strip frontmatter (`--- … ---`). Strip fenced code blocks (` ``` … ``` `) and inline backtick spans — they hold protocols, identifiers, etc. that are not jargon to flag.
   b. Extract every `\b[A-Z]{2,}\b` token from the remaining body prose.
   c. Classify each token:

   | Result | Condition |
   |---|---|
   | SKIP — allowlisted | lowercased token ∈ `ALLOWLIST` |
   | SKIP — in vault | lowercased token ∈ `VALID_TERMS` (including the note's own title/aliases) |
   | SKIP — expanded inline | within 80 chars before or after the acronym, a parenthetical expansion exists whose word initials spell the acronym, e.g. `Network File System (NFS)` or `NFS (Network File System)` |
   | GAP | none of the above |

4. **Aggregate**:
   - Count occurrences per gap acronym across all final notes.
   - Capture the first surrounding sentence (≤ 200 chars) as context per occurrence.
   - Compute per-note gap density.

5. **Write `00_Inbox/VAULT_GAPS_REPORT.md`** (UTF-8, no BOM):

```markdown
# Vault Gaps Report
Generated: YYYY-MM-DD
Final notes scanned: N
Distinct acronyms flagged: N
Total gap occurrences: N

## Top priority — acronyms used ≥ 3 times with no vault concept
| Acronym | Count | Best-guess expansion | Sample notes |
|---|---|---|---|
| SMB | 7 | (not found in any context) | Azure_Files_Storage, Azure_NetApp_Files, ... |

## All flagged acronyms
| Acronym | Count | First context |
|---|---|---|
| SMB | 7 | "supports both SMB and NFS protocols" (Azure_Files_Storage) |

## Notes with highest gap density
| Note | Gap count | Acronyms |
|---|---|---|
| Azure_NetApp_Files | 4 | SMB, NFS, AD, LDAP |

## Resolution menu (human decides per acronym)
- **Add concept** — write a new concept note for the term so future ingestion resolves the reference. Best for terms used ≥ 3 times.
- **Add to allowlist** — append to `99_System/acronym_allowlist.md` if the term is truly atomic and not worth its own concept.
- **Patch source note** — only valid if the note is NOT yet `status: final`. Final notes are immutable (Rule 6).
- **Accept** — acknowledge the gap; it will reappear on the next scan until one of the above is done.
```

### Safety

- Reads concept files only. Never writes to `20_Learning/21_Concepts/`.
- Code-fence and inline-backtick stripping prevents false positives on identifiers like `SELECT`, `HTTP/2`, `JSON`.
- Self-reference is excluded (a note titled "RBAC" using `RBAC` in its own body is not a gap).
- If `99_System/acronym_allowlist.md` is missing or malformed, log a warning and proceed with an empty allowlist (Review 6 still runs but flags more aggressively).
- If `VAULT_INDEX.json` is stale (`generated` ≠ today), STOP — the false-positive rate on freshly-added vault concepts would be too high.

---

## Review 7 — Cluster health

Note counts say nothing about whether the *clustering* is good. A MOC can have
plenty of notes but clusters that are oversized (concepts dropped at render),
fragmented into singletons, or incoherent (a concept's relationships pull into a
different cluster). Run the cluster-health gate:

```
powershell -ExecutionPolicy Bypass -File cluster_health.ps1
```

It parses every MOC's `## Concept Landscape` clusters and `## Concept
Relationships` edges and flags, per cluster:

- **OVERSIZED (> 9 concepts)** — the diagram silently drops the overflow; the
  cluster is doing too much. Split it: `recluster.ps1 -MocStem {stem}` drafts a
  split by token + edge similarity for the human to confirm.
- **singleton (1 concept)** — boundary too fine; merge into the nearest sibling
  (recluster.ps1 proposes the merge).
- **list-only (0 structural edges)** — no learnable backbone; run
  `connect_clusters.ps1 -MocStem {stem}` to draft structural edges.
- **orphans** — notes that claim the MOC in `moc:` but sit in no cluster (place
  them).
- **misplaced** — a concept whose typed edges mostly pull into another cluster
  (consider moving it, or the two clusters should merge).

**Structural-debt routing (loop D).** The diagram pipeline already computes rich
quality signals that otherwise die in console output — route them into this
report:
- Read the latest `00_Inbox/DIAGRAM_RENDER_PLAN.json` (written by
  `build_diagrams.ps1`). Surface any cluster where the diagram dropped concepts
  at render (`selected < total`) — these are oversized clusters actively losing
  information.
- Optionally fold in `vault-graph topology` output (orphans, dead wikilinks,
  centrality) as the graph-metric backend — same orphan/dead-link signals,
  computed over the whole wikilink graph. (See
  `99_System/Claude/vault-graph/SKILL.md`.)
Track unresolved items run-over-run so structural debt has somewhere to live
instead of being recomputed and forgotten each week.

**Never auto-fix** — re-clustering is a human judgment call. Report the flagged
MOCs and worst offenders, and point the user at `recluster.ps1` /
`connect_clusters.ps1` for the drafts. These two helpers write review worksheets
to `00_Inbox/` and never edit a MOC themselves.

Output format:
```
## Cluster health
| MOC | Oversized clusters | Singletons | List-only | Orphans | Misplaced | Render-dropped |
| MOC_Threat_Protection | Attack Landscape (20), Copilot Ops (10) | — | 7/7 | — | — | 11 concepts |
| MOC_Enterprise_Architecture | Architecture as Thinking (17), Org Dynamics (13) | — | 6/6 | 1 | 3 | 8 concepts |
```
Lead the Priority actions with the worst oversized clusters — they actively
lose information at render time.

---

## Review 8 — Quarantine surfacing (loop B)

`validate_note()` failures land in `00_Inbox/Quarantine/` and in the index's
`validation_errors[]`, but nothing recurringly surfaces them — a quarantined
note is invisible to every downstream forever. Because a quarantined note is a
*committed artefact that failed*, surfacing it does NOT violate the no-nag
principle (unlike draft).

- Read `validation_errors[]` from `VAULT_INDEX.json` (already computed — one
  read, zero extra scan). Cross-check the file list in `00_Inbox/Quarantine/`.
- Report the count and each stem with its first validation error.

Output format:
```
## Quarantine (loop B)
Quarantined notes: N
| Stem | First validation error |
| Foo_Bar | invalid domain: 'security' — must be one of [...] |
```

---

## Review 9 — AI_Candidates cooling (loop E)

`extract-gems` writes proposed candidates to `00_Inbox/AI_Candidates/` with a
cooling period before the weekly promote/merge/discard decision. This is the ONE
backlog that SHOULD be surfaced — a proposed-but-undecided artefact, distinct
from the intentionally un-nagged draft notes.

- List entries in `00_Inbox/AI_Candidates/` older than **N = 14 days** (by file
  mtime or the candidate's `extracted:` field), so nothing sits indefinitely
  without a decision.

Output format:
```
## AI_Candidates cooling (loop E)
Candidates awaiting weekly review: N (M older than 14 days)
| Candidate | Age (days) | Suggested type |
```

---

## Review 10 — Frontmatter well-formedness (loop F)

`generate_index.py` parses only the **first** `---...---` block in a file. A note
can therefore be structurally broken yet still parse "successfully" into a WRONG
record — and never raise a missing-field error — so the defect is invisible to
every other review (which all trust the index). This is exactly how a whole MOC's
notes were silently mis-indexed: a `concept_role:` mini-block had been prepended
*above* the real frontmatter, so the index read `{concept_role: study}` as the
entire frontmatter and defaulted `title`→stem, `status`→draft, `moc`→[],
`flashcards`→false for ~100 notes. Reviews 1–3 saw "valid" records and flagged
nothing.

Because the index cannot be trusted to surface this class of defect, this review
reads the note **files directly** via a deterministic script:

```
powershell -ExecutionPolicy Bypass -File frontmatter_health.ps1
```

It scans `21_Concepts`, `22_Maps of Content`, `40_Solutions`, `10_Ideas` and
flags, per file:

- **DOUBLE_FM** — more than one frontmatter block at the top (the index reads
  only the first; the real one is stranded in the body). The classic signature is
  a `concept_role:` (or any) mini-block prepended above the real frontmatter.
- **MIDFILE_BOM** — a UTF-8 BOM (U+FEFF) at any offset > 0. A *leading* BOM is
  tolerated; one mid-file means content was prepended in front of the original
  BOM (a botched batch edit) — the reliable fingerprint of DOUBLE_FM.
- **UNCLOSED_FM** — opens with `---` but the block is never closed.
- **NO_FM** — a concept note with no frontmatter at all.

This is a committed-artefact defect (a malformed file that silently corrupts the
index), so it IS surfaced — distinct from the never-nagged draft
backlog. **Never auto-fix in a routine review** — report the offenders and their
flags. A fix re-shapes the frontmatter (merging blocks, stripping the stray BOM),
which is a structural edit; on `status: final` notes it requires explicit user
authorisation (Safety Rule #6), so it is a separate, deliberate action — not part
of the read-only health pass. When fixing, back up the originals to `60_Admin/`
first, transform only files matching an exact malformation signature, then
**re-run `generate_index.py`** so the corrected frontmatter reaches the index.

Run this review **first** in a full health check: if it FAILs, note in the report
that all index-derived sections (Reviews 1–3, 6) may be based on wrong records
until the malformed files are repaired.

Output format:
```
## Frontmatter health (loop F)
Malformed files: N
| Flags | File |
| DOUBLE_FM, MIDFILE_BOM | Global_Region_Resource_Allocation.md |
```

---

## Index management — regenerate VAULT_INDEX.json

Run when the user adds notes outside the agent pipeline or requests a manual index refresh.

```python
# generate_index.py — run from vault root
import os, json
from pathlib import Path

VAULT = Path(__file__).parent
INDEX = VAULT / "00_Inbox" / "VAULT_INDEX.json"

SKIP_DIRS = {
    "00_Inbox", "30_Sources", "40_Solutions", "99_System",
    ".obsidian", ".trash", "Templates", "Assets"
}

notes, mocs = [], []
for root, dirs, files in os.walk(VAULT):
    dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]
    for fname in files:
        if not fname.endswith(".md"): continue
        title = fname[:-3]
        if fname.startswith("MOC_"): mocs.append(title)
        else: notes.append(title)

with open(INDEX, "w") as f:
    json.dump({"notes": sorted(notes), "mocs": sorted(mocs)}, f, indent=2)

print(f"Index: {len(notes)} notes, {len(mocs)} MOCs")
```

**Run sequence (any cadence):**
```powershell
.\launch-process-inbox.ps1     # regenerates the index automatically, then runs process-inbox
```
Every launcher regenerates `VAULT_INDEX.json` before the agent starts; run
`python generate_index.py` by hand only after editing notes out of band.

---

## Token budget reference

| Operation | Cost |
|---|---|
| Load VAULT_INDEX.json (100-note vault) | ~800 tokens |
| CLAUDE.md instructions | ~1,500 tokens |
| Per note processed | ~1,100 tokens |
| Report output | ~150 tokens |
| **Sustainable batch size** | **40-60 mixed notes/week** |
| Hard context limit (Sonnet) | ~160 notes |

---

## Full health check report format

Run all review sections (1–9) and output:

```
## Vault health check — {date}

### Frontmatter health (run FIRST — Review 10, loop F)
{Review 10 output. If it FAILs, prepend a banner: index-derived sections below
may reflect wrong records until the malformed files are repaired.}

### Summary
Notes total: N | Final: N | Draft: N | Needs review: N
MOCs: N | Orphaned notes: N | Open questions: N
Quarantined: N | Flashcard sync gaps: N | AI_Candidates awaiting review: N
Malformed frontmatter: N   ← if > 0, index-derived sections may be unreliable

### Priority actions (ordered by urgency)
1. {Most urgent item}
2. {Second item}
...

### Actionable notes
{Review 1 table}

### MOC coverage
{Review 2 table}

### Flashcard coverage
{Review 3 tables — incl. Flashcard sync gaps (loop A)}

### Open questions
{Review 4 output}

### MOC candidates
{Review 5 output}

### Cluster health
{Review 7 output — incl. structural-debt routing (loop D)}

### Quarantine
{Review 8 output (loop B)}

### AI_Candidates cooling
{Review 9 output (loop E)}
```

---

## Metadata fields this skill depends on

The following YAML fields must be present on concept notes for this skill to work correctly:

```yaml
type: concept | moc | pattern | idea | solution
status: draft | final
domain: learning | writing | presentations | biology | strategy | multiple | enterprise-architecture | ai-systems | data-engineering | cybersecurity
source_type: book | course | article | notebooklm | shower-thought
created: YYYY-MM-DD
updated: YYYY-MM-DD
moc: [MOC title]
reviewed: true | false
flashcards: true | false
concept_role: study | reference | scaffold   # optional; absent ⇒ study. Gates flashcard/review nagging (Reviews 1 & 3): reference/scaffold notes are never flagged for missing cards.
```

If these fields are missing from older notes, flag them in the report as `METADATA INCOMPLETE` rather than failing silently.

**Note:** missing-field detection relies on the index, which only parses the
first frontmatter block. A note with a *structurally* broken frontmatter (a
second block, a stray mid-file BOM) can parse into a wrong record without any
missing-field error — that class of defect is caught by **Review 10**, which
reads the files directly. Run Review 10 first so this section's signals are
trustworthy.


## 文件 99_System/Claude/pkm-solution/SKILL.md

---
name: pkm-solution
description: Drafts a Phase 5 artefact — Pattern or Solution — from vault knowledge into 40_Solutions/. Use this skill whenever the user asks to draft a pattern, write a solution, build a presentation/memo/strategy from the vault, abstract a recurring approach, or mentions /pkm-solution, output-bridge, or Phase 5. Always shortlist candidates from VAULT_INDEX.json before reading any concept/pattern file in full.
---

# PKM Solution Skill (Phase 5 — Output Bridge)

Drafts one of two artefact types into `40_Solutions/`:

| Type | Frontmatter `type:` | Filename suffix | What it is |
|---|---|---|---|
| Pattern  | `pattern`  | `{Title} - Pattern.md`  | Reusable approach to a recurring problem — the **how** |
| Solution | `solution` | `{Title} - Solution.md` | A delivered work product (deck, memo, plan, essay) built from vault notes |

Full Phase 5 reference: `40_Solutions/Personal Knowledge Management System - Solution.md`.
Validation rules and templates live in `99_System/` (Pattern_Template.md, Solution_Template.md).

---

## Inputs required before starting

- `[BRIEF]` — the user's request: what they want produced, for whom, by when, with what constraints. If absent or unclear, ask before proceeding.
- `[VAULT_INDEX]` — contents of `00_Inbox/VAULT_INDEX.json`. Reject and stop if `generated` ≠ today (CLAUDE.md staleness gate).
- `[TEMPLATES]` — `99_System/Pattern_Template.md`, `Solution_Template.md`. Read only the one matching the decided type.

**Do not scan the vault.** The only files this skill opens during shortlisting are `VAULT_INDEX.json` and (after human confirmation) the specific notes on the shortlist.

---

## Phase S-0 — Staleness and intent gate

1. Read `00_Inbox/VAULT_INDEX.json`. If `index["generated"]` ≠ today's date, print:
   `⚠ Index is from {date}. Run generate_index.py first, then retry.` and stop.
2. Restate the brief in one sentence. If you cannot, ask the user to sharpen it before continuing.
3. If the brief has multiple plausible readings — different artefact
   type (Pattern vs Solution), different Solution mode
   (doc vs composite), different scope (one deliverable vs a series),
   different audience — NAME EACH READING and ask which is meant.
   Do not collapse ambiguity by picking the most likely option.
   Mis-identifying the type is the most expensive failure mode of
   this skill: it loads the wrong template and routes the artefact
   to the wrong validation gate.

---

## Phase S-1 — Decide the type

Use the decision tree (matches the spec exactly):

```
Is the output something you delivered or will deliver?
  (a presentation, a memo, a strategy doc, a CV, an email)
    └─→  SOLUTION

Is the output an abstract reusable approach to a recurring problem?
  (a methodology, a framework, a workflow)
    └─→  PATTERN
```

If two types could fit, pick the one **closer to action**: a Solution that proves a Pattern beats a draft Pattern with no use record.

State the chosen type out loud. Do not load any other template.

### S-1b — If type is Solution, pick the mode

A Solution is always recorded as a `.md` file in `40_Solutions/`. What
varies is whether the `.md` is itself the deliverable or whether it is
the vault record for a binary deliverable that lives alongside it.

| Mode | `.md` content | Companion file | Example |
|---|---|---|---|
| **Doc**       | `## The Solution` IS the deliverable (essay, memo, plan, strategy doc written in markdown) | none | `How to Implement the PKM System - Solution.md` |
| **Composite** | `## The Solution` describes the deliverable + points to companion(s) | `.pptx` / `.docx` / `.xlsx` / `.xlsm` sharing the same base name | `Q3 Strategy Pitch - Solution.md` + `Q3 Strategy Pitch - Solution.pptx` |

Ask the user:
> Is this a doc Solution (.md only) or composite (.md + companion file)? If composite, name the companion filename(s) — they must share the base `{Title} - Solution` and live in `40_Solutions/`.

Record the mode and any companion filenames before proceeding. The
companion may already exist or be planned for later — either is valid,
but the filename must be agreed up front so the `.md` declares it.

**The skill never creates or modifies binary files.** Composite mode
writes only the `.md`. The user produces the `.pptx`/`.docx`/`.xlsx`
separately.

---

## Phase S-2 — Shortlist from the index (no file reads)

Parse the index into four working sets, all sourced from `VAULT_INDEX.json`:

| Set | Source | Used for |
|---|---|---|
| `CONCEPTS`     | `notes[]`              | Underlying mechanisms |
| `PATTERNS`     | `patterns[]`           | Reusable approaches the brief may apply |
| `IDEAS`        | `ideas[]`              | Pre-production hypotheses to test |
| `VALID_STEMS`  | union of these lists + `solutions[]` | Wikilink validation set |

### Scoring (deterministic, no file reads)

For each candidate in `CONCEPTS ∪ PATTERNS ∪ IDEAS`, compute:

1. **Domain hit (+3)** — `domain` matches the brief's domain. If the brief is cross-domain (`multiple`), skip this filter.
2. **Tag overlap (+2 per match)** — case-insensitive token intersection of `tags[]` with brief keywords. Tokenise the brief on whitespace and punctuation; lowercase both sides.
3. **Description / aliases / title substring hit (+1 per match)** — substring match on each.
4. **Pattern bonus (+1)** — `use_count > 0` (it has demonstrated value).

Sort each set by score descending. Cut at:
- **≤ 12 concepts**
- **≤ 5 patterns**
- **≤ 3 ideas**

If a candidate's `tags[]` is empty, **mark it `(no tags — match quality reduced)`** in the shortlist. Do not drop it, but the human should know precision is weaker on that row.

### Present the shortlist

One markdown table grouped by type. Columns: `Stem | Score | Status | Domain | One-line (description) | Notes`. Notes column carries flags: `(no tags)`, `(status: draft)`.

Then ask:
> Confirm the shortlist. Add / remove stems by name. Reply `go` to proceed with the list as-is.

**Do not read any full note yet.** Wait for the human reply.

---

## Phase S-3 — Deep read confirmed stems only

Once the human confirms, read the full content of every stem on the final shortlist — and only those. Use the dedicated PowerShell pattern from CLAUDE.md (`Get-Content … -Raw -Encoding UTF8`). Do not read anything else.

If a confirmed stem is missing from the index (typo, renamed file), stop and ask. Do not silently substitute.

---

## Phase S-4 — Load the matching template

Open exactly one file from `99_System/`:

| Decided type | Template |
|---|---|
| Pattern  | `99_System/Pattern_Template.md`  |
| Solution | `99_System/Solution_Template.md` |

If the template file is missing, stop and report. Do not freehand the structure.

---

## Phase S-5 — Draft the artefact

Fill the template strictly from the deep-read material plus the brief. No invented facts, no plausible-sounding fill. If a section has no source content, leave it blank and flag the gap in the post-draft report — do not embellish.

### Frontmatter emission contract (non-negotiable)

The indexer (`generate_index.py → parse_frontmatter`) parses with `yaml.safe_load` and **silently drops** any note whose frontmatter is malformed — a missing opening `---` returns `None` (the note never enters the index, flashcards, or health checks; it just vanishes), and any YAML error skips it the same way. Emit the block to these rules exactly:

1. **Fences.** Line 1 of the file is exactly `---` — no BOM, no blank line, no leading whitespace before it. Close the block with a line that is exactly `---`. Nothing precedes the opening fence.
2. **No blank lines inside the block.** Keys run contiguously from the opening fence to the closing fence.
3. **Key and value on one line.** Every scalar field is `key: value` with the value on the **same line** as its key and a single space after the colon. Never let a value wrap to the next line (the classic `problem:` ↵ `Writing fails…` bug — that makes `problem` null and the wrapped text an invalid bare scalar). An intentionally empty field is `key:` with nothing after the colon and **no trailing space**.
4. **Quote any value that could be misread as YAML.** Wrap the value in double quotes — escaping any interior `"` as `\"` — whenever it contains a colon-space `: `, a `#`, or begins with one of `@ \` * & ! | > % [ ] { } , ? : -` or a quote. `description` and `problem` are prose and routinely contain an interior `: ` (e.g. "one upstream choice: reveal…") — an unquoted `: ` is read as a new key/value separator and breaks the whole block, so when in doubt, quote these two.

### Type-specific drafting rules

**Pattern**
- `ingredients[]` is a list of **exact concept stems** from the deep-read concepts. 3–5 atomic concepts is the canonical shape; more is acceptable if each adds a distinct mechanism.
- `problem` is one sentence — the recurring problem this pattern solves.
- `problem_type` ∈ `{learning, communication, leadership, decision-making, productivity}`.
- `use_count` starts at `0`. The skill bumps it on subsequent Solutions that cite this pattern (see Phase S-7).

**Solution**
- `built_from[]` lists every concept, pattern, idea, or prior solution stem the work actually drew on. Must be non-empty.
- `companion[]` lists binary deliverable filenames. Empty list = doc mode (the `.md` is the deliverable). Non-empty = composite mode. Each entry must:
  - Share the base name `{Title} - Solution` with this file
  - End in a supported extension: `.pptx`, `.ppt`, `.docx`, `.doc`, `.xlsx`, `.xlsm`, `.xls`, `.pdf`
  - Live in `40_Solutions/` (existence is not required at write time — the companion may be produced after the `.md`)
- The Vault sources block at the bottom enumerates: Patterns used / Concepts applied / Ideas explored — each entry must be a real stem from the index.
- `## The Solution` section content depends on mode:
  - **Doc:** the section is the actual deliverable text (essay, memo, plan).
  - **Composite:** the section describes the companion deliverable — what it is, who it's for, key sections — and names each companion file explicitly. Do not paste binary content; do not attempt to render slide outlines as if they were the deck itself unless the brief explicitly asks for a markdown outline as the deliverable.
    - **`.pptx` companions — standing exception:** also add the deck's slide-by-slide **voiceover script** (the spoken narration, verbatim from its speaker notes — full sentences, not presenter cues) as a `## The Script` section placed immediately after `## The Solution`. This is required by the pptx skill's "Companion Solution record" rule and overrides the no-slide-outline default above for decks.

### Stems are immutable

**Never invent a stem.** Every entry in `ingredients`, `built_from`, and every `[[wikilink]]` in the body must exist in `VALID_STEMS`. If the brief names something not in the vault:
- Write it in plain prose, not as a wikilink, with `(not yet in vault: "...")`.
- Flag in the post-write report so the user can decide whether to capture it.

---

## Phase S-6 — Pre-write validation gate

Run before any file write. Hard fail → fix inline once → still failing → write to `00_Inbox/QUARANTINE/` and report.

**First, actually parse the frontmatter — do not eyeball it.** Write the candidate `$content` to a temp file and run it through the indexer's own parser. This is a real command, not a self-attested checkbox; the emission contract's faults (missing fence, wrapped value, interior `: `) are invisible to the eye and only a parser catches them:

```powershell
$VaultRoot = if ($env:VAULT_ROOT) { $env:VAULT_ROOT } else { (Get-Location).Path }
$tmp = Join-Path $env:TEMP "pkm_fm_check.md"
Set-Content -Path $tmp -Value $content -Encoding UTF8
python -c "import sys; sys.path.insert(0, sys.argv[2]); from generate_index import parse_frontmatter; c=open(sys.argv[1], encoding='utf-8').read(); f,e=parse_frontmatter(c); assert f, (e[0] if e else 'no frontmatter — note would be SILENTLY DROPPED from the index (missing opening --- ?)'); print('FM_OK')" $tmp $VaultRoot
```

`FM_OK` → proceed to the field checks below. Any traceback (`AssertionError`, `YAML parse error: …`, `frontmatter block never closed`) → fix per the emission contract and re-run this exact command before writing. Never write a file whose frontmatter has not printed `FM_OK`.

```
✓ Frontmatter printed FM_OK (parsed by generate_index.parse_frontmatter — not eyeballed)
✓ type ∈ {pattern, solution}
✓ filename ends in " - Pattern.md" / " - Solution.md"
  and the suffix matches the type field
✓ title, status, description, domain, created, updated all present and non-empty
✓ domain ∈ {learning, writing, presentations, biology, strategy, multiple, enterprise-architecture, ai-systems, data-engineering, cybersecurity}

  (Pattern)
✓ problem present (1 sentence)
✓ ingredients[] non-empty; every stem exists in VALID_STEMS
✓ problem_type ∈ {learning, communication, leadership, decision-making, productivity}
✓ use_count is an integer (default 0)

  (Solution)
✓ built_from[] non-empty; every stem exists in VALID_STEMS
✓ companion[] (if present): each entry shares the base `{Title} - Solution`
  with this file AND ends in .pptx/.ppt/.docx/.doc/.xlsx/.xlsm/.xls/.pdf.
  Existence is checked with Test-Path; missing companion → warn (not fail),
  log in the post-write report so the user knows to produce it.

  (All types)
✓ Every [[wikilink]] in the body exists in VALID_STEMS, or is written
  in plain prose with (not yet in vault: "...")
```

---

## Phase S-7 — Write and patch

### Write the file

Path: `40_Solutions/{Title} - {Type}.md`. Use `Set-Content -Path ... -Value $content -Encoding UTF8` exactly as specified in CLAUDE.md's Windows File Operation Patterns. Confirm the chosen filename does not already exist (`Test-Path`) — never overwrite an existing artefact. If it exists, stop and ask whether to bump the title.

For composite Solutions, the `.md` is the only file this skill writes. Binary companions (`.pptx`, `.docx`, `.xlsx`, `.xlsm`, `.pdf`) are produced by the user outside this skill. The `.md`'s `companion:` field and `## The Solution` section name the expected filename(s); the user is responsible for placing the binary in `40_Solutions/` under the agreed name.

### Use-count patch (Solutions only)

For every Pattern stem listed in the new Solution's `built_from[]` or `## Vault sources → Patterns used`, increment that Pattern's `use_count` by 1 using a **targeted regex patch**:

```powershell
$file = Join-Path $VaultRoot "40_Solutions\{Pattern stem}.md"
$content = Get-Content $file -Raw -Encoding UTF8
$content = $content -replace 'use_count: (\d+)', {
    "use_count: $([int]$_.Groups[1].Value + 1)"
}
Set-Content -Path $file -Value $content -Encoding UTF8
```

**Never rewrite the Pattern file.** Patch the single line only. If the regex fails to match (legacy file shape), log and skip — do not invent a `use_count:` line.

### What NOT to patch

- Concept notes — they are immutable past `status: final` except for the two GF-3 patches. The pkm-solution skill never touches a concept file.
- MOCs — Phase 4 owns those.
- Existing solutions — never overwrite.
- **Binary companion files** (`.pptx`, `.docx`, `.xlsx`, `.xlsm`, `.pdf`, etc.) — never created, opened, read, moved, renamed, or deleted by this skill. The `.md` declares them; the user owns them.

---

## Phase S-8 — Report

Two outputs.

### (a) Markdown table — transcript

| Type | Title | Path | Stems referenced | Use_count patches | Status |
|---|---|---|---|---|---|

Status values:
- `Written, validated`
- `Written, validated, 2 patterns incremented`
- `Quarantined — {reason}`
- `Not written — user declined at shortlist`

Then the gap list, if any:
```
Gaps (referenced but not in vault):
  - "Some Thing" — flagged in body as (not yet in vault: "Some Thing")
  - "Other Thing" — likewise
```

### (b) JSON results

Write `00_Inbox/PKM_SOLUTION_RUN_RESULT.json`:

```json
{
  "generated": "YYYY-MM-DD",
  "type":      "pattern | solution",
  "mode":      "doc | composite | n/a",
  "stem":      "Title - Type",
  "path":      "40_Solutions/Title - Type.md",
  "companion":          [ "Title - Solution.pptx" ],
  "companion_present":  [ true ],
  "shortlist": { "concepts": N, "patterns": N, "ideas": N, "confirmed": N },
  "built_from":        [...],
  "ingredients":       [...],
  "use_count_patched": [ "Pattern_Stem_1", ... ],
  "gaps":              [ "Thing 1", "Thing 2" ],
  "validation_errors": [],
  "status":            "written | quarantined | declined"
}
```

`mode` is `"doc"` or `"composite"` for Solutions, `"n/a"` for Pattern.
`companion[]` and `companion_present[]` are aligned arrays — the second
records whether each declared companion file exists on disk at write time.
Missing companions are a warning, not a failure.

UTF-8, no BOM, sorted keys not required.

---

## Safety rules

1. **Never invent stems.** Every cross-reference must resolve in `VALID_STEMS`. Plain-prose fallback for anything missing.
2. **Never read a concept/pattern/idea file until it has been confirmed on the shortlist.** Shortlisting runs against the index only.
3. **Never overwrite an existing Phase 5 file.** `Test-Path` before write; stop on collision.
4. **Never edit a concept note** — concept files are out of scope for this skill (see CLAUDE.md SAFETY RULE 6).
5. **Use_count is the only field this skill patches in an existing Phase 5 file.** Single regex-targeted replacement. No full-file rewrites.
6. **Stale index halts everything.** Phase S-0 stop is hard — fix the index, then re-invoke.

---

## What this skill is NOT for

- Capturing ideas → `10_Ideas/` directly, no skill needed (ideas are pre-production).
- Editing existing concept notes → out of scope; flag for review session.
- Generating flashcards → that's `pkm-flashcards`.
- Vault audits, coverage sweeps, suffix mismatches across the existing folder → that's `pkm-review`.
- Anything in `30_Sources/`, `20_Learning/22_Maps of Content/`, or `00_Inbox/` — read-only for this skill.


## 文件 99_System/Claude/vault-graph/SKILL.md

# Skill: vault-graph
**Engine:** 03 — Interconnect
**Requires:** the local module `99_System/Claude/vault-graph/vault_graph.py` over
`rapidfuzz` + `datasketch` + `networkx`. Install hash-locked:
`pip install --require-hashes -r 99_System/Claude/vault-graph/requirements.lock`

> **Dependency note.** The previous external dependency `graphifyy` (new,
> anonymous `author: None`, unreviewed, heavy) was **removed on 2026-06-20** and
> replaced by the local module `vault_graph.py`, a thin read-only backend over
> the three libraries this skill actually uses (`rapidfuzz`, `datasketch`,
> `networkx`). The dependency tree now contains no unreviewed third-party code
> and is pinned + hash-locked (`requirements.lock`), clearing the publish gate
> that graphifyy held. The phase descriptions below are implemented by
> `vault_graph.py` (functions `similarity()`, `topology()`, `shortest_path()`)
> and runnable directly: `python vault_graph.py {similarity|topology|path A B}`.

## Purpose
Analyse the vault's concept graph: detect near-duplicate concepts via fuzzy
matching (rapidfuzz + MinHash) and surface structural insights — centrality,
clustering, and path finding — from the wikilink graph (networkx). vault-graph
is the **read-only graph-metric backend for `vault-health`**: its topology
output (orphans, dead wikilinks, centrality) feeds the weekly vault-health
report (feedback loops D and E), rather than being a standalone command users
discover separately.

## Commands

| Command | What it does |
|---|---|
| `vault-graph similarity` | Find near-duplicate concept notes by title and content |
| `vault-graph topology` | Centrality, clustering, and orphan detection across the wikilink graph |
| `vault-graph path {concept-a} {concept-b}` | Shortest wikilink path between two concepts |

---

## `vault-graph similarity`

Find concept notes that are suspiciously similar but filed separately — candidates for merging, linking, or consolidating.

### Phases

**S-0 — Load**
Read all concept note titles and first paragraphs from `20_Learning/21_Concepts/`. If `VAULT_INDEX.json` exists and is fresh, use it; otherwise parse files directly.

**S-1 — Title fuzzy match**
Use `rapidfuzz.fuzz.token_sort_ratio` on all title pairs. Flag pairs scoring ≥ 80.

**S-2 — Content MinHash**
Use `datasketch.MinHash` + LSH on full note bodies (128 permutations). Flag pairs with Jaccard similarity ≥ 0.5.

**S-3 — Report**
For each flagged pair, print:
- Both note titles + their similarity score
- A recommendation: `merge` / `link` / `review`

Output: printed report only. **No vault writes.**

---

## `vault-graph topology`

Build the directed wikilink graph and compute structural metrics to surface the vault's most important, most bridging, and most isolated concepts.

### Phases

**T-0 — Build graph**
Parse all `[[wikilinks]]` from concept notes and MOCs into a directed `networkx.DiGraph`. Nodes = note stems; edges = wikilink references.

**T-1 — Centrality**
Compute and rank:
- **Degree centrality** — most linked-to (hub concepts)
- **Betweenness centrality** — bridge concepts connecting otherwise distant clusters
- **PageRank** — importance weighted by the quality of incoming links

Surface top 10 for each metric.

**T-2 — Clustering**
Find weakly connected components. Flag isolated nodes (no inbound or outbound links) as orphans for human review.

**T-3 — Report**
Print ranked tables + flag structural anomalies (orphans, dead wikilinks pointing to non-existent notes).

Output: printed report only. **No vault writes.**

---

## `vault-graph path {concept-a} {concept-b}`

Trace the shortest wikilink chain between two concepts — useful for understanding how ideas in different MOCs are connected.

### Phases

**P-0 — Build graph**
Same as T-0.

**P-1 — Path find**
Run `networkx.shortest_path(G, source=concept-a, target=concept-b)`.

**P-2 — Report**
Print the full chain of notes from source to target. If no path exists, report the closest reachable node from each end and the gap between them.

Output: printed report only. **No vault writes.**

---

## Similarity thresholds (canonical — shared with the Phase 2 overlap classifier)
The similarity thresholds are defined here, once, and reused by both dedup
paths so they agree:
- **Title fuzzy match:** `rapidfuzz.fuzz.token_sort_ratio ≥ 80`
- **Content MinHash:** Jaccard `≥ 0.5` (128 permutations)

`process-inbox` Phase 2 OVERLAP DETECTION (see `docs/inbox-pipeline.md`) uses
the SAME fuzz ≥ 80 tripwire to flag spelling-variant / near-duplicate titles
before classifying TYPE 1/2/3/MERGE. If you tune these numbers, change them
here and update the cross-reference in inbox-pipeline.md — do not let the two
dedup paths drift to different thresholds.

## Safety rules
- **Read-only.** This skill never creates, edits, or deletes vault files.
- `VAULT_INDEX.json` can seed the **node set and titles** (stems + frontmatter),
  but it stores **no body wikilinks and no edge list** — so `topology` and
  `path` MUST parse note bodies for `[[wikilinks]]` to build the graph. The
  index alone cannot supply edges. (Extending `generate_index.py` to emit a
  link list would remove that parse, but that is a larger change — not assumed
  here.)
- Never auto-merge or auto-link flagged pairs — similarity results are for human review only.
- Report missing wikilink targets as dead links, not errors; the referenced MOC may exist in the user's full vault but outside this export.


## 文件 99_System/Claude/vault-retrieval/SKILL.md

# Skill: vault-query
**Role:** Retrieve — a read-only, cross-cutting retrieval command over the whole
vault (the "Usage" job), not one of the five pipeline engines.
**Requires:** the local module `99_System/Claude/vault-retrieval/retrieval.py`
(`onnxruntime` + `tokenizers` + `numpy`). Install hash-locked:
`pip install --require-hashes -r 99_System/Claude/vault-retrieval/requirements.lock`

> **Dependency note.** Dense embeddings run `TaylorAI/bge-micro-v2` — the *same*
> model the vault's Smart Connections plugin uses — on CPU via `onnxruntime` (no
> torch). Sparse (BM25) and RRF fusion are pure numpy. The ONNX model +
> tokenizer download once into `.embeddings/` (gitignored, derived, rebuildable)
> and are not a pip dependency. Markdown stays the single source of truth; the
> shadow index is a disposable, regenerable cache.

## Purpose
Answer an ad-hoc question about the vault with a **cited, synthesised** answer —
or honestly admit the vault has nothing on it. Retrieval is **hybrid**: notes are
split into overlapping chunks, then dense semantic recall (bge-micro-v2) + sparse
keyword (BM25) score every chunk and fuse via Reciprocal Rank Fusion, with each
note taking its best chunk — so a question phrased differently from the target,
or answered deep inside a long note, still finds it. Your **Q-4 read of the top
notes is the reranker** — no separate cross-encoder model is needed, which keeps
the dependency tree lean.

## Command
`vault-query {question}` — synthesises a cited answer from the vault.
**Read-only.** Never writes a vault note. The corpus is concepts, MOCs,
40_Solutions and 10_Ideas (Note Pipe / raw inbox is excluded).

---

## Pipeline (the agent IS in this loop)

**Q-0 — Refresh the shadow index (incremental, cheap).**
Run once at the start of the command:
```
python 99_System/Claude/vault-retrieval/retrieval.py build
```
This re-chunks and re-embeds only notes whose SHA-256 changed (seconds when
nothing changed; ~85 s only on the very first build). Skip if you just built it
this session.

**Q-1 — Expand the query (opportunistic).**
Generate 2–4 alternative phrasings of the question (synonyms, the domain term,
a plain-language restatement). You are the model, so this is free. Pass them as
`--expand` flags. Each phrasing is fused in via RRF, widening recall. If you
have no good rewrites, pass none — retrieval degrades cleanly to the single
query (and to BM25-only if the embedder is ever unavailable).

**Q-2 — Retrieve.**
```
python 99_System/Claude/vault-retrieval/retrieval.py query "{question}" \
    --expand "{phrasing 1}" --expand "{phrasing 2}" --json --top 8
```
Read the JSON: `results[]` (each with `stem`, `path`, `title`, `snippet`,
`dense_cos`, `bm25`, `rrf`), `max_cos`, and `low_confidence`.

**Q-3 — Gate: admit gaps, never fabricate.**
If `low_confidence` is true, OR the top results plainly do not address the
question (read the snippets — semantic score can be a false positive), respond:
> "Nothing in the vault addresses this."
You may name the closest tangential note as a pointer, but do NOT invent an
answer. This is Safety Rule #7: every claim must originate from a source note.

**Q-4 — Synthesise with citations.**
Otherwise, read the top relevant notes from their `path`s (index + notes only —
no outside knowledge), then write a concise answer where **every factual claim
cites its source note** as a clickable `[[stem]]` wikilink. Prefer 2–5 sources;
do not pad with weakly-related notes. Close with a "Sources:" list of the
`[[stem]]`s actually used. If sources disagree, say so and cite both.

---

## Examples
- `vault-query how do I stop password-reuse attacks?`
  → cites `[[Credential_Stuffing]]`, `[[Multi-Factor_Authentication]]`,
    `[[Credential_Proliferation_Mitigation_(SSO)]]`.
- `vault-query what's the best recipe for sourdough?`
  → "Nothing in the vault addresses this." (low_confidence; no fabrication.)

## Safety rules
- **Read-only.** Never creates, edits, or deletes a vault file.
- **No fabrication.** Synthesis draws only from retrieved notes; cite every
  claim; admit gaps rather than guess (Safety Rule #7).
- The shadow index and model under `.embeddings/` are derived and gitignored;
  deleting them and re-running `build` reproduces the index and changes no note.

