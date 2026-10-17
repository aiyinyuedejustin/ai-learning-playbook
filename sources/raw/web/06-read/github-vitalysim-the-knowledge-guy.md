# vitalysim/the-knowledge-guy：把一本书变成 skill

- 链接：https://github.com/vitalysim/the-knowledge-guy
- 作者：vitalysim
- 仓库说明：Turn any PDF or EPUB into a structured Claude Code skill  - then ask your whole bookshelf a single question.
- 星数：27
- 获取方式：GitHub README + SKILL/说明文件

---

## README

# The Knowledge Guy

> Turn any PDF or EPUB into a structured Claude Code skill —
> then ask your whole bookshelf a single question.

<p align="center">
  <img src="docs/hero-pipeline.png" alt="Pipeline diagram: /book-to-skill ingests a PDF through five map-reduce stages into a two-tier Claude Code skill; /the-knowledge-guy routes any question across every installed skill and writes both a chat response and an HTML artifact." width="900">
</p>

*From a PDF on disk to a queryable knowledge skill in one command;
from a question to a cross-domain answer in another.*

---

## What this is

A long book is 400K+ tokens; you forget the middle by the end; asking
a question that spans three books is impossible. Existing tools
either stuff everything into context (expensive, forgetful) or
hand-write summaries (lossy, immediately stale).

`/book-to-skill` is a **map-reduce ingest pipeline** that turns a
PDF or EPUB into a two-tier Claude Code skill: an always-loaded
concept map (~3K tokens — thesis, 6-10 load-bearing frameworks,
chapter and topic indexes) plus on-demand chapter toolkits (~1K
tokens each — frameworks, techniques, anti-patterns, worked
examples). A 600-page book becomes a skill that costs a few thousand
tokens to consult instead of four hundred.

`/the-knowledge-guy` is the **router and interactive teacher** across
every installed skill. It auto-discovers skills from the filesystem
at every invocation, routes any question to every plausibly relevant
book in parallel, and synthesises one answer with inline citations.
It can teach a topic step by step with quizzes and resumable progress
— and it can turn a chapter into an interactive **learn-by-doing**
website: theory with manipulable SVG illustrations, auto-checked
quizzes, in-browser code labs, and open tasks it grades against a
rubric.

The architectural rule that holds it together: **plumbing in Python,
intelligence in Claude.** `extract.py` does mechanical PDF → text +
slices + image manifest, and that is *all* it does. Every act of
understanding — framework extraction, concept mapping, synthesis,
quiz authoring — is an LLM call.

Both skills follow Anthropic's `SKILL.md` open standard — consumed
natively by Claude Code, Claude Desktop, claude.ai, the Claude API,
OpenAI Codex CLI, and GitHub Copilot. See *Install on your platform*
below.

## Quick start

```bash
/book-to-skill /path/to/book.pdf                                  # ingest  (add --course → complete coverage + practice)
/the-knowledge-guy what do my books say about margin of safety?   # ask
/the-knowledge-guy walk me through Kerberos                       # tutor
/the-knowledge-guy course <skill-slug>                            # learn by doing
/the-knowledge-guy nutshell <skill-slug>                          # skim
/the-knowledge-guy resume                                         # resume
```

Every invocation also writes a self-contained HTML artifact to
`artifacts/`. Course pages are interactive — they run in the browser.

## The system, in two pieces

### `/book-to-skill` — the ingest pipeline

Map-reduce in six stages (the sixth, **Stage 3 PRACTICE**, is opt-in),
plus an opt-in per-chapter **coverage audit**. What's worth knowing:

- **Two-tier output.** `SKILL.md` is always loaded;
  `chapters/<book_number>-<slug>.md` is paged in on demand. The
  tier-1 file is front-loaded so compaction keeps the start safely.
- **`book_number` is the canonical chapter label** — `ch07`, `intro`,
  `appendix-a`, `part-1`, `fm`, `bm`. The book's own chapter numbers,
  never extraction order. The manifest also carries an internal
  `index` — never user-facing.
- **`schema_version: 2`** plus three idempotent helper scripts so
  legacy skills upgrade in place without re-extracting.
- **Resume is filesystem-driven.** Re-running on a partial run is
  always safe; chapter files in `chapters/` are the checkpoint.
- **`raw/` stays with the skill** — full text, slices, images,
  metadata, Pass-0 spine. Re-extracting one chapter never re-runs
  Stage 0.
- **Seven genre profiles** (technical / vuln-hunting / financial /
  scientific / productivity / narrative non-fiction / general) tune
  chunk boundaries, the chapter schema, and the reduce emphasis.
- **Complete-coverage mode (opt-in)** replaces the default dense, capped
  toolkits with capturing *every* load-bearing element in every chapter,
  then runs a per-chapter **coverage audit** and re-runs any chapter with
  gaps until it clears a 95% gate — so nothing is silently dropped. (CS:APP
  was ingested this way: 130 sections, every one audited to 100%.)
- **Stage 3 PRACTICE (opt-in)** turns each chapter into a practice set —
  it extracts the book's own exercises, generates new ones, and for
  cyber/technical chapters can web-research realistic labs. The output
  (`practice/<book_number>-<slug>.json`) is what `/the-knowledge-guy
  course` renders as an interactive learn-by-doing site. Best for
  technical / textbook / vuln-hunting books.
- **Options — flags or interactive.** Pass `--complete` (full coverage),
  `--practice` (Stage 3), `--course` (both → course-ready), or
  `--regenerate` (rebuild an existing skill) — or omit them and
  book-to-skill prompts for each *with a cost estimate before spending*.
  The same flags pass through the router: `/the-knowledge-guy <path>.pdf --course`.

### `/the-knowledge-guy` — the router + teacher

Auto-discovery, no registry. Reads `.claude/skills/*/SKILL.md`
frontmatter at every invocation; drop a skill in, the router picks it
up on the next call. Excludes itself and `book-to-skill` from
routing, every time.

| Mode | What it does | Trigger |
| ---- | ------------ | ------- |
| **ask** | Cross-domain synthesis essay with inline citations | open-ended question |
| **walk** | Interactive curriculum with quizzes, progress saved across sessions | `walk me through <topic>` |
| **course** | Interactive learn-by-doing site per chapter — theory + auto-checked quizzes + in-browser code labs + open tasks graded by Claude | `course <book> [<chapter>]` |
| **check** | Grade an open-ended practice answer against its rubric | `check <book> <ch> <id>` |
| **nutshell** | Whole-book per-chapter skim (~100 words/chapter) | `nutshell <book>` |
| **library** | Bookshelf overview | `library` |
| **comparison** | One concept across multiple books, tagged agree / extend / tension | `compare <topic>` |
| **cheatsheet** | Operational one-pager per book | `cheatsheet <book>` |
| **glossary** | A-Z term lookup, per-book or cross-library | `glossary [<book>]` |
| **concept-map** | Tier-1 framework graph for a book | `concept-map <book>` |
| **toolkit** | Tier-2 deep dive on one chapter | `toolkit <book> <chapter>` |
| **ingest** | Hand off a PDF/EPUB to `book-to-skill` | `add <path>.pdf` |
| **resume** | Pick up an interrupted walk | `resume` |

Ask mode never reads a domain `SKILL.md` itself — it reads only the
40-line frontmatter for routing, then fans out one parallel subagent
per matched skill. Each subagent loads exactly one book and answers
in 200-400 words with chapter citations. The orchestrator synthesises
the reports into one unified essay.

### Learn by doing — the `course` experience

For technical, textbook, and vuln-hunting books, reading is only half
of learning. `/the-knowledge-guy course <book>` renders an interactive
website per chapter (plus a syllabus index) that teaches *and* makes you
practice. The full loop, all in a self-contained HTML page that opens
from disk:

- **Theory** — the chapter taught in practitioner voice, composed from
  the design-system components, optionally with an **interactive SVG
  concept widget**: toggle a sanitizer and watch taint stop at it; drag a
  write-length past a buffer's capacity and watch it turn critical; step a
  pipeline; compare two approaches. Five widget types
  (`flow`, `toggle-state`, `stepper`, `slider`, `compare`), all built from
  the existing `.plate`/`.illus` classes so they invert in dark mode, with
  motion gated behind `prefers-reduced-motion`. The teaching subagent adds
  one only where a concept is genuinely structural — prose by default.
- **Practice** — auto-checked quizzes (multiple-choice, predict-output,
  fix-the-bug, fill-in-the-blank, reorder-steps, spot-the-anti-pattern)
  with instant feedback; **in-browser runnable code labs** (JavaScript
  natively; Python via Pyodide) that execute the learner's code in a
  sandboxed iframe and run a deterministic check; and open-ended tasks.
- **Grading + progress** — an open task's *"Check with Claude"* button
  copies a `check …` command; paste it back and Claude grades it against
  the task's rubric and records the result. Quiz/lab progress saves to the
  browser's `localStorage`; a durable `course-<slug>.md` memory file is the
  source of truth, and the index shows a mastery meter per chapter.

The practice content comes from `book-to-skill`'s opt-in **Stage 3
PRACTICE**, which extracts the book's own exercises, generates new ones,
and can web-research realistic labs (`practice/<book_number>-<slug>.json`).
Two lints guard it: `lint_practice.py` *executes* every lab to prove its
solution passes and its starter fails, and `lint_concept_widgets.py`
validates each widget's schema and rejects any bespoke SVG that hardcodes
a color (the engine itself never sets one).

## Every output is also an HTML artifact

Every invocation writes both text to chat *and* a self-contained HTML
file to `artifacts/`, using a shared design system ("Knowledge Guide
· Modern" — Bricolage Grotesque + JetBrains Mono, single cobalt
accent, light/dark + density toggle persisted in `localStorage`).
Catalog at `artifacts/index.html` is auto-updated on every write.

```
artifacts/
├── index.html                              ← auto-updated catalog
├── library.html                            ← bookshelf overview
├── nutshells/<book-slug>.html              ← cached, deterministic
├── synthesis/YYYY-MM-DD-<query-slug>.html  ← dated, never reused
├── walks/<topic>-step-<N>.html             ← overwritten per step
├── walks/<topic>-recap.html                ← durable
├── courses/<book-slug>/index.html          ← syllabus, regenerated
├── courses/<book-slug>/<book_number>.html  ← interactive lesson, cached
└── comparisons/  toolkits/  cheatsheets/
    concept-maps/  glossaries/              ← cached per slug
```

Deterministic outputs (nutshell, toolkit, cheatsheet, concept-map,
per-book glossary, library, course lessons) are cached and reused;
non-deterministic ones (synthesis, comparison, walk-recap) accumulate as
dated files. The design system lives at
[`.claude/skills/the-knowledge-guy/design-system/`](./.claude/skills/the-knowledge-guy/design-system/)
— `shell.html` (which carries the static CSS plus two guarded engines: the
practice **lab engine** and the **concept-widget engine**), `layouts.md`,
`widgets.md` (the widget schema), and a full visual contract at
`reference/full-demo-light.html`.

## Honest limitations

- Optimised for 50–500 page **technical or non-fiction prose**.
  Cookbooks, reference manuals, and dense math textbooks extract
  less cleanly.
- Stage 0 requires PyMuPDF; scanned PDFs without an OCR layer fall
  back to text-only (no figures).
- Image-heavy books cost extra at extraction time — the pipeline
  reads every kept figure with a vision call.
- **Course mode** needs a modern browser to open the generated pages.
  Quizzes and JavaScript labs run fully offline; **Python** labs fetch
  Pyodide from a CDN on first Run and fall back to "check with Claude"
  when offline. Open-ended tasks are graded back in chat, not in the
  page. Practice generation (Stage 3) is best on technical / textbook /
  vuln-hunting books; narrative and finance books get quizzes and
  reflection tasks rather than code labs.

## Design principles

1. **Auto-discovery over configuration.**
2. **Two tiers per skill — Tier 1 always loaded, Tier 2 paged in.**
3. **Plumbing in Python, intelligence in Claude.**
4. **Parallel by default** — multi-skill answers and multi-step
   teaching both fan out in a single message.
5. **Raw stays with the skill** — re-extraction never re-runs Stage 0.
6. **Filesystem-driven resume; idempotent upgrade scripts.**

## Repository layout

```
the-knowledge-guy/
├── README.md · CLAUDE.md
├── artifacts/                  ← every HTML output lands here
└── .claude/skills/
    ├── book-to-skill/
    │   ├── SKILL.md            ← pipeline runbook (Stages 0-3)
    │   ├── reference/          ← templates, genre profiles, concept-map spec,
    │   │                         practice-template.md (the Stage-3 contract)
    │   └── scripts/            ← extract.py · detect_chapters.py · lint_chapters.py
    │                             lint_practice.py · lint_concept_widgets.py
    │                             backfill_book_numbers.py · relabel_nutshell.py
    │                             upgrade_walk_memory.py · upgrade_course_memory.py
    ├── the-knowledge-guy/
    │   ├── SKILL.md            ← mode dispatch + all 13 modes (incl. course / check)
    │   ├── walk-mode.md        ← interactive curriculum + quiz + course memory
    │   └── design-system/      ← shell.html (+ lab & widget engines) · layouts.md
    │                             widgets.md · reference/
    └── <book-derived skills>/  ← one per ingested book (+ optional practice/)
```

## Install on your platform

This repo ships **two skills** — `book-to-skill` and
`the-knowledge-guy`. Both must be installed. Generated book-skills
(from running `/book-to-skill`) sit alongside them and are picked
up by the router automatically. Requires
[`uv`](https://docs.astral.sh/uv/) for the per-skill Python venv
(PyMuPDF + ebooklib + beautifulsoup4 + pypdf).

### Universal install — clone once, symlink everywhere

Covers Claude Code + Claude Desktop in one step:

```bash
git clone https://github.com/vitalysim/the-knowledge-guy.git ~/the-knowledge-guy
mkdir -p ~/.claude/skills
ln -s ~/the-knowledge-guy/.claude/skills/book-to-skill      ~/.claude/skills/
ln -s ~/the-knowledge-guy/.claude/skills/the-knowledge-guy  ~/.claude/skills/
~/the-knowledge-guy/.claude/skills/book-to-skill/scripts/setup.sh
```

Symlinking (rather than copying) means `git pull` upgrades both
skills in place. Other platforms (web, API, Codex, Copilot) add a
second link, a ZIP upload, or an API registration — see below.

### Claude Code (CLI) — `~/.claude/skills/`

The universal install above covers this. Project-scoped alternative:
drop the two skills into `<your-project>/.claude/skills/` instead.
Skills hot-reload — no restart needed.
Docs: <https://code.claude.com/docs/en/skills>

### Claude Desktop (macOS / Windows) — shared user-scope dir

The desktop app reads the same `~/.claude/skills/` as the CLI. If
you ran the universal install, the app picks the skills up on next
launch. Available on Free / Pro / Max / Team / Enterprise since
April 13, 2026.
Docs: <https://support.claude.com/en/articles/12512180-use-skills-in-claude>

### claude.ai (web) — ZIP upload via Settings

```bash
cd ~/the-knowledge-guy/.claude/skills
zip -r book-to-skill.zip      book-to-skill
zip -r the-knowledge-guy.zip  the-knowledge-guy
```

Then in claude.ai: **Settings → Customize → Skills → Create skill →
Upload .zip**. Repeat for each ZIP. Requires Code Execution + File
Creation enabled. Note: claude.ai can't write to a local
`artifacts/` folder — HTML artifacts in web sessions render inline
in the chat container instead.
Docs: <https://support.claude.com/en/articles/12512180-use-skills-in-claude>

### Anthropic API / Agent SDK — `container.skills`

Register each skill as a custom skill, then reference both in
`container.skills` with the beta header (code execution must be
enabled; up to 8 skills per request):

```python
client.messages.create(
    model="claude-opus-4-7", max_tokens=4096,
    container={"skills": [{"type": "custom", "skill_id": "<id-1>"},
                          {"type": "custom", "skill_id": "<id-2>"}]},
    extra_headers={"anthropic-beta": "skills-2025-10-02,code-execution-2025-08-25"},
    messages=[{"role": "user", "content": "/the-knowledge-guy library"}],
)
```

Docs: <https://platform.claude.com/docs/en/build-with-claude/skills-guide>

### OpenAI Codex CLI — `~/.agents/skills/`

Codex CLI (since Dec 2025) consumes `SKILL.md` as-is from
`~/.agents/skills/`:

```bash
mkdir -p ~/.agents/skills
ln -s ~/the-knowledge-guy/.claude/skills/book-to-skill      ~/.agents/skills/
ln -s ~/the-knowledge-guy/.claude/skills/the-knowledge-guy  ~/.agents/skills/
```

Codex's tool runtime differs from Claude Code's (no `Skill` tool, no
`AskUserQuestion`), so the **walk** and **ingest** modes degrade to
prompted-text fallbacks; **ask**, **nutshell**, **library**, and the
other read-only modes work directly.
Docs: <https://developers.openai.com/codex/skills>

### GitHub Copilot — `.github/skills/` per repo

Copilot's skill support (April 2026) is project-scoped. For each
repo where you want the skills available:

```bash
cd <your-repo>
mkdir -p .github/skills
cp -R ~/the-knowledge-guy/.claude/skills/book-to-skill      .github/skills/
cp -R ~/the-knowledge-guy/.claude/skills/the-knowledge-guy  .github/skills/
```

Active in Copilot's agent mode. The Python venv assumed by
`book-to-skill` won't exist in Copilot's container — ingest mode
doesn't run there; query modes do.
Docs: <https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills>
and <https://code.visualstudio.com/docs/copilot/customization/agent-skills>

### Porting to platforms without native skill support

- **Cursor IDE** — uses `.cursor/rules/*.mdc`; adaptation is
  mechanical (frontmatter conversion + per-file split).
  [Docs](https://cursor.com/docs/rules).
- **Zed Editor** — native support pending
  ([zed#49057](https://github.com/zed-industries/zed/issues/49057));
  paste `SKILL.md` content into the system prompt in the interim.
- **Cline / Roo / Aider / Continue** — no standardised skills
  mechanism as of May 2026; stopgap is to paste the runbook text
  from `book-to-skill/SKILL.md` and `the-knowledge-guy/SKILL.md`
  into the platform's system-prompt or rules file.

### Compatibility matrix (May 2026)

| Platform | Native skills? | Install location | Consumes `SKILL.md` as-is? |
| --- | --- | --- | --- |
| **Claude Code (CLI)** | ✓ | `~/.claude/skills/` or `./.claude/skills/` | yes |
| **Claude Desktop** (mac/win) | ✓ | `~/.claude/skills/` | yes |
| **claude.ai** (web) | ✓ | Settings → Customize → Skills (ZIP upload) | yes |
| **Anthropic API / Agent SDK** | ✓ | `container={"skills":[…]}` + beta header | yes |
| **OpenAI Codex CLI** (Dec 2025+) | ✓ | `~/.agents/skills/` | yes |
| **GitHub Copilot** (Apr 2026+) | ✓ | `.github/skills/` per repo | yes |
| **Cursor IDE** | needs adapt | `.cursor/rules/*.mdc` | no — manual conversion |
| **Zed Editor** | pending | — | — |
| **Cline / Roo / Aider / Continue** | no | — | — |

After install, ingest your first book with
`/book-to-skill /path/to/book.pdf` (genre prompt → cost estimate →
name). A 600-page book takes ~10-20 min wall-clock and roughly $1-3
in API costs depending on model.

## Upgrading legacy skills

Four idempotent helper scripts handle older skills:
`backfill_book_numbers.py` populates `book_number` and renames
chapter files, `relabel_nutshell.py` fixes cached nutshell headings
after backfill, `upgrade_walk_memory.py` rewrites stale
`<slug>/chNN` shorthand inside walk memory, and
`upgrade_course_memory.py` repairs `book_number` drift in any
`practice/*.json` files and `course-<slug>.md` memory after a
re-backfill. All four are no-ops on already-current skills.

## Contributing

PRs welcome. Read [`CLAUDE.md`](./CLAUDE.md) and the two `SKILL.md`
files first — together they're the canonical architecture brief; the
rest of the docs are derived from them.

**Common contributions**

- **A new mode in `the-knowledge-guy`** — add the trigger to mode
  dispatch in `the-knowledge-guy/SKILL.md`, write the mode section,
  and add the matching HTML layout in `design-system/layouts.md`.
  Every mode emits an artifact (per Step 0.5).
- **A new design-system component** — add it to
  `design-system/shell.html`, demo it in
  `design-system/reference/full-demo-light.html`, and reference it
  from any layout that uses it. Don't introduce a second accent
  colour — cobalt is load-bearing.
- **A new practice exercise type or concept-widget type** — extend the
  frozen contract (`book-to-skill/reference/practice-template.md` for
  exercises, `the-knowledge-guy/design-system/widgets.md` for widgets),
  add the renderer branch to the matching engine in
  `design-system/shell.html`, and teach the lint
  (`lint_practice.py` / `lint_concept_widgets.py`) to validate it. Widgets
  must stay theme-safe — class swaps only, never a `fill`/`stroke`.
- **A new genre profile for `book-to-skill`** — extend
  `book-to-skill/reference/genre-profiles.md`. Genres tune chunk
  boundaries, the chapter schema, and the reduce emphasis.
- **A new helper script** — drop it in `book-to-skill/scripts/`,
  make it idempotent, document the one-line invocation in
  `book-to-skill/SKILL.md`.
- **The hero diagram** — open
  `artifacts/readme-hero-pipeline.html` in a browser, flip the
  theme toggle if desired, screenshot the `.plate` block, and save
  to `docs/hero-pipeline.png`. The source HTML uses the live
  design-system tokens, so the diagram stays in sync if the
  palette changes.

**Style**

- Markdown wraps at 80 columns; commands and paths go in fenced code
  blocks; no trailing whitespace.
- Python is PEP-8 with no extra dependencies beyond what `setup.sh`
  provisions (PyMuPDF, ebooklib, beautifulsoup4, pypdf).
- Voice in docs is editorial-confident — declarative sentences, no
  marketing language, no emoji.
- Commit subjects are imperative (`Add X`, `Fix Y`); the body
  explains *why* the change exists, not *what* changed.

**Before opening a PR**

- If you touched a chapter file, run
  `book-to-skill/scripts/lint_chapters.py <skill-dir>`.
- If you touched `extract.py`, ingest a small test book and confirm
  `chapters_manifest.json` is `schema_version: 2` with every entry
  carrying `book_number`.
- If you touched a layout, regenerate one cached artifact (e.g.
  `/the-knowledge-guy nutshell <slug> --regenerate`) and open it in
  both light and dark themes.
- If you touched the practice schema, an exercise renderer, or a lab,
  run `book-to-skill/scripts/lint_practice.py <skill-dir>` — it executes
  every lab to prove its solution passes and its starter fails.
- If you touched the widget schema, the widget engine, or a course page,
  run `book-to-skill/scripts/lint_concept_widgets.py --page <course.html>`
  and open the page in both themes (and with reduced motion).

**Issues**

- Bugs: include the affected skill slug, the failing slash command,
  and the relevant `.claude/skills/<slug>/raw/metadata.json` if it
  helps the repro.
- Feature requests: describe the use case before sketching the
  implementation.

## What's next

Designed for but not shipped: voice-mode walks, spaced repetition on
the recorded fumbles, remote channels (desktop / claude.ai), and a
mastery view across overlapping walks.


## 文件 CLAUDE.md

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A **Claude Code skill library**, not an app. There is no build step, no
test runner, no entry point. Two installed entry points carry the whole
system:

- **`/book-to-skill`** (`.claude/skills/book-to-skill/`) — the **ingest
  pipeline**. Map-reduce in 6 stages (Stage 0 EXTRACT → Pass 0 SPINE →
  Stage 1 MAP → Stage 2 REDUCE → Stage 2.5 NUTSHELL → **Stage 3 PRACTICE**,
  the last opt-in) that turns a PDF/EPUB into a two-tier knowledge skill:
  ~3K-token always-loaded `SKILL.md` + on-demand
  `chapters/<book_number>-<slug>.md` toolkits, plus optional
  `practice/<book_number>-<slug>.json` exercise sets. Plumbing in Python
  (`scripts/extract.py`), intelligence in Claude (Stages 1, 2 & 3 are
  LLM-driven subagent fan-outs).
- **`/the-knowledge-guy`** (`.claude/skills/the-knowledge-guy/`) — the
  **router + interactive teacher** across every installed domain skill.
  Auto-discovers them by scanning `.claude/skills/*/SKILL.md` at every
  invocation. **Thirteen modes**: `ask` (default — parallel cross-domain
  synthesis essay), `walk` (interactive curriculum + quizzes, progress
  saved to `~/.claude/projects/<this project>/memory/walk-*.md`),
  `course` (interactive learn-by-doing site per chapter — theory + quizzes
  + in-browser code labs) and its `check` sub-mode (grades open tasks),
  `nutshell`, `library`, `comparison`, `cheatsheet`, `glossary`,
  `concept-map`, `toolkit`, `ingest`, `resume`.

**Domain skills** (one per ingested book, e.g. `forshaw-windows-security/`,
`sethi-rich-life/`) are the artifacts `book-to-skill` produces. Each is
independently invokable as `/<slug>`. They are *outputs* of the system,
not part of its surface — treat them as interchangeable demonstrations.

Read `README.md` for the user-facing narrative. Read
`.claude/skills/book-to-skill/SKILL.md` for the pipeline procedure (this
*is* the runbook). Read
`.claude/skills/the-knowledge-guy/SKILL.md` for the router behavior and
all thirteen modes.

## Canonical chapter labels — `book_number` (schema_version 2)

The single most important architectural fact, easy to get wrong:

- Every manifest entry has a `book_number` (`ch07`, `intro`, `preface`,
  `appendix-a`, `part-1`, `fm`, `fm-2`, `bm`, …). This is the **only**
  user-facing chapter label. It is the filename prefix, the heading in
  `nutshell.md`, the citation in walks and ask-mode answers.
- The manifest also has `index` — extraction order, 1..N over everything
  the extractor produced (front matter included). **`index` is internal
  only.** Using it in filenames or labels reintroduces the off-by-N
  drift bug that this codebase already fought once.
- Source of truth: `book-to-skill/scripts/extract.py:parse_book_number_kind`
  + `assign_book_numbers`. Display-side renderers (the-knowledge-guy
  nutshell mode, walk-mode.md, citations) must read `book_number` from
  `chapters_manifest.json`, never reconstruct it.

A manifest at `schema_version: 1` is **legacy**. Step 6 of book-to-skill
stops on encountering one and tells the user to run
`backfill_book_numbers.py`. Don't try to "just continue".

## Every output is an HTML artifact

Every `/the-knowledge-guy` invocation writes **both** text to chat and
a self-contained HTML artifact to `artifacts/` at the project root. The
folder is the user's catalog and the skill's cache:

```
artifacts/
├── index.html                              ← auto-updated catalog
├── library.html                            ← bookshelf overview
├── nutshells/<book-slug>.html              ← cached, deterministic
├── synthesis/YYYY-MM-DD-<slug>.html        ← dated, accumulates
├── walks/<topic>-step-<N>.html             ← overwritten per step
├── walks/<topic>-recap.html                ← durable
├── courses/<slug>/<book_number>.html       ← cached interactive chapter site
├── courses/<slug>/index.html               ← syllabus, always regenerated
└── comparisons/  toolkits/  cheatsheets/
    concept-maps/  glossaries/              ← cached per slug
```

The design system is **Knowledge Guide · Modern** at
`.claude/skills/the-knowledge-guy/design-system/` — Bricolage
Grotesque + JetBrains Mono, single cobalt accent, light/dark +
density toggle persisted in `localStorage`. Three files there:

- `shell.html` — the wrapper. Placeholders `{{TITLE}}`,
  `{{EXTRA_CSS}}`, `{{BODY}}`. Read it, substitute, write. It also
  carries two guarded engines that no-op on any page without their JSON
  island, so they ship harmlessly in every artifact: the **lab engine**
  (`#kg-exercises` → auto-checked quizzes, sandboxed-iframe code labs,
  "check with Claude" buttons, progress in `localStorage`) and the
  **concept-widget engine** (`#kg-concept-widgets` → interactive theory
  SVG illustrations built from the `.plate`/`.illus` classes; it only ever
  swaps classes, never a `fill`/`stroke`, so it is theme-safe; state is
  ephemeral). Widget motion is the system's only animation, gated behind
  `prefers-reduced-motion`. Schema: `design-system/widgets.md`.
- `layouts.md` — one section per use case (nutshell / synthesis /
  walk-session / walk-recap / comparison / toolkit / glossary /
  cheatsheet / concept-map / library / **course-chapter / course-index**).
  Each has the path under `artifacts/`, the title, EXTRA_CSS (usually
  empty — the shell already has every component), and the body template.
- `reference/full-demo-light.html` + `-dark.html` — canonical visual
  contract of every component, in both themes.

**One CDN exception.** Artifacts are otherwise fully self-contained
(CSS/JS inline; Google Fonts the only external request). Python code
labs lazy-load **Pyodide from a CDN on first Run only**, and degrade to
"check with Claude" when offline. JS labs need no network. Do not inline
Pyodide. Prefer `runtime: "js"` labs where the concept allows.

**Never invent CSS.** Pull EXTRA_CSS from `layouts.md` verbatim. If
you need a one-off tweak, use inline `style=""`. New utility classes
belong in `shell.html`, added deliberately — never per-artifact.

After writing any artifact, regenerate `artifacts/index.html` so the
catalog reflects the new file. Deterministic outputs (nutshell,
toolkit, cheatsheet, concept-map, per-book glossary, library, **course
chapter pages**) are **cached** — reuse the existing file on repeat
invocations unless the user passes `--regenerate`. Non-deterministic ones
(synthesis, comparison, walk-recap) get dated filenames and accumulate.
The **course index** is regenerated every time (cheap; reflects progress).

## Operational commands

These are real scripts in `.claude/skills/book-to-skill/scripts/`. All
are idempotent.

```bash
# Upgrade a legacy (schema_version=1) skill in place
./book-to-skill/scripts/backfill_book_numbers.py <skill-dir> [--dry-run]

# After backfill, resync labels + citations in cached nutshell.md
./book-to-skill/scripts/relabel_nutshell.py <skill-dir> [--dry-run]

# Rewrite stale `slug/chNN` shorthand inside walk memory after backfill
./book-to-skill/scripts/upgrade_walk_memory.py [memory-dir] [--dry-run]

# Quality lint a skill's chapter toolkit files (verbatim-copy detection,
# size sanity, missing headings). Uses the manifest to resolve raw paths,
# so it works for chapters named intro/appendix-a/fm as well as chNN.
./book-to-skill/.venv/bin/python ./book-to-skill/scripts/lint_chapters.py <skill-dir>

# Validate Stage-3 practice files AND execute every runnable lab to prove
# its model solution passes (and the starter fails). Hard-fails broken labs,
# bad MCQs, book_number mismatches. Run after Stage 3 / before shipping.
./book-to-skill/.venv/bin/python ./book-to-skill/scripts/lint_practice.py <skill-dir>

# Validate course-lesson concept widgets (the 5-type schema in widgets.md) and
# the theme-safety of bespoke static SVG (no hardcoded colors). --check-stdin
# gates one spec at render time; --page / <dir> audits rendered course pages.
./book-to-skill/.venv/bin/python ./book-to-skill/scripts/lint_concept_widgets.py --page <course-page.html>

# Repair book_number drift in practice/*.json + course-*.md after a re-backfill
# (sibling of upgrade_walk_memory.py; joins practice→manifest by chapter title).
./book-to-skill/scripts/upgrade_course_memory.py [memory-dir] [--dry-run]

# Provision the per-skill Python venv (one-time)
./book-to-skill/scripts/setup.sh
```

There is a **second, separate `scripts/` at the repo root** — do not
confuse it with `book-to-skill/scripts/`. It holds repo-level tooling,
not pipeline logic:

```bash
# Benchmark the real cost of one /book-to-skill ingest. Two-step:
#   1) ./scripts/measure_ingest.sh --start   (snapshots subscription usage)
#   2) run /book-to-skill <book> in a fresh window
#   3) ./scripts/measure_ingest.sh --finish [session_id]
# Reports wall-clock, quota Δ, token totals, main-vs-Stage-1 split,
# per-subagent breakdown, and an equivalent-API-cost estimate. Reads the
# session + agent-*.jsonl under ~/.claude/projects/<this project>/.
./scripts/measure_ingest.sh --start | --finish
```

The slash commands themselves (`/book-to-skill`, `/the-knowledge-guy`,
`/<book-slug>`) are how the user invokes everything — they execute via
Claude Code's skill runtime; do not try to call them from bash.

## Where to read before editing

| Editing… | Read first |
|---|---|
| Pipeline behavior, stages | `book-to-skill/SKILL.md` (the runbook) |
| Manifest schema, including `book_number` vocabulary | `book-to-skill/reference/concept-map-spec.md` |
| Per-chapter toolkit shape | `book-to-skill/reference/chapter-template.md` |
| Per-chapter nutshell shape + numbering rule | `book-to-skill/reference/nutshell-template.md` |
| Genre-specific extraction profiles | `book-to-skill/reference/genre-profiles.md` |
| Stage-3 practice file shape (the frozen contract) | `book-to-skill/reference/practice-template.md` |
| Course-lesson concept-widget schema (the 5 types) | `the-knowledge-guy/design-system/widgets.md` |
| Routing, ask synthesis, and the 13 modes (incl. `course` / `check`) | `the-knowledge-guy/SKILL.md` |
| Walk mode procedure + course/check memory grammar | `the-knowledge-guy/walk-mode.md` |
| Worked walk transcripts | `the-knowledge-guy/examples.md` |
| HTML artifact layouts (one per use case) | `the-knowledge-guy/design-system/layouts.md` |
| HTML shell + design tokens | `the-knowledge-guy/design-system/shell.html` |
| Visual contract for every component | `the-knowledge-guy/design-system/reference/full-demo-light.html` |
| Artifact catalog conventions | `artifacts/README.md` |

## Architecture details that span files

- **`extract.py` is pure plumbing.** It does PDF/EPUB → text + images +
  per-chapter raw slices + `metadata.json`. It assigns `book_number` to
  each chapter via `assign_book_numbers` (single source of truth). It
  never summarises — *every* act of understanding happens in Claude.
- **Stages 1 and 2 are LLM-driven subagent fan-outs**, not Python. Stage
  1 maps over chapters (one subagent per chapter, parallel). Stage 2
  reduces over the chapter toolkit files to produce the concept map +
  indexes. Both are driven by prompts in `book-to-skill/SKILL.md`.
- **Resume is filesystem-driven**, not log-driven. A `chapters/<…>.md`
  that exists, is > 500 bytes, and lacks "extraction failed" counts as
  done. Stage 2 only runs once all chapter files exist. `progress.json`
  is a log, not the source of truth.
- **`raw/` stays with the skill.** Every domain skill keeps the
  original `full_text.txt`, per-chapter raw `.txt` slices, images,
  `metadata.json`, and `spine.md` inside `<slug>/raw/`. Re-extracting a
  single chapter never needs to rerun Stage 0.
- **The router never reads a domain `SKILL.md`.** It reads only
  frontmatter (≤ 40 lines per skill) for routing decisions, then fans
  out subagents that each load exactly one `SKILL.md`. Adhere to this —
  reading domain `SKILL.md`s in the router will blow context budgets on
  any non-trivial library.
- **Every mode emits an HTML artifact.** Step 0.5 of
  `the-knowledge-guy/SKILL.md` documents the universal procedure: read
  `design-system/shell.html`, find the matching layout in
  `design-system/layouts.md`, substitute, write to
  `artifacts/<subfolder>/<filename>.html`, refresh
  `artifacts/index.html`. Caching rules per the artifacts section
  above; non-deterministic outputs always create a new dated file.
- **Stage 3 (PRACTICE) is opt-in and additive — like Stages 1 & 2, it's
  an LLM subagent fan-out** (one per chapter) driven by prompts in
  `book-to-skill/SKILL.md` Step 8.6. It writes
  `practice/<book_number>-<slug>.json` (frozen schema in
  `reference/practice-template.md`). It does **not** bump
  `schema_version` (stays `2`) — the `course` renderer discovers practice
  by **file presence**, never a version flag. The runbook's
  legacy-guard / `assert schema_version == 2` are unchanged.
- **`course` mode is a renderer; `check` closes the loop in chat.** A
  course page is fully self-contained — quizzes/labs check client-side.
  The only non-deterministic part, grading an *open* task, happens in chat
  via the `check` sub-mode (the page's "Check with Claude" button copies a
  `check …` command to paste back). `course-<slug>.md` memory (walk-mode
  grammar) is the durable source of truth; browser `localStorage` is a
  live cache.

## Conventions to preserve when editing

- **Cite chapters as `[skill-name <book_number>]` inline** at the point
  of each claim, never in trailing per-skill perspective blocks.
- **Nutshell mode skips entries** where `word_count < 300` **or**
  `book_number` starts with `fm` / `bm` (any front/back matter, even
  long ones). See `book-to-skill/SKILL.md` Step 8.5.
- **Filenames are `<book_number>-<slug>.md`** in `chapters/`. The slug
  is normalised lower-kebab without redundant prefixes
  (`backfill_book_numbers.py:_strip_redundant_prefix` handles cleanup).
  **Practice files mirror this exactly**: `practice/<book_number>-<slug>.json`,
  keyed off `book_number` (never `index`). `lint_practice.py` hard-fails a
  stem/`book_number` mismatch.
- **Practice answer keys never reach the browser.** When `course` mode
  inlines the `#kg-exercises` island, it must strip `rubric` and
  `model_answer` from every `open` exercise (they're consumed only by the
  `check` sub-mode). The renderer whitelists fields per family — see
  `practice-template.md` → "Field-visibility rule".
- **Drop-in extensibility is sacred** — never hardcode skill slugs in
  routing or rendering. The router rediscovers skills every invocation.
- **Design system: never invent CSS in an artifact.** Pull the
  EXTRA_CSS block from `the-knowledge-guy/design-system/layouts.md`
  verbatim. New components or utility classes go in
  `design-system/shell.html`, edited deliberately; one-off tweaks
  inside an artifact use inline `style=""`. Family coherence across
  every output is the whole point.
- **Citations in ask/synthesis** are inline `[skill-slug <book_number>]`
  in chat text, and `.source` cards (per the demo) in the HTML artifact.
  Don't trail per-skill perspective blocks at the end — the essay is
  unified.

## Walk memory

Walks save state to `~/.claude/projects/<this project>/memory/walk-<slug>.md`.
The file uses shorthand like `housel/ch04` for chapter references; this
shorthand is bound to the *current* `book_number` numbering and will
drift if a skill is re-backfilled. Run `upgrade_walk_memory.py` after
any pipeline change that renumbers chapters. **Courses** save the same
way to `course-<skill-slug>.md` (identical walk grammar — see
`walk-mode.md` → "Course memory"); after a re-backfill run
`upgrade_course_memory.py`, which repairs both the `course-*.md` files
**and** the `practice/*.json` filenames/labels.

## Things you should NOT do

- Do not run `book-to-skill/scripts/extract.py` directly to "test it" on
  a real book without coordinating — extraction is hash-cached and
  produces a `.venv` and ~hundreds of MB of cache.
- Do not delete `raw/` from a domain skill. It is part of the skill.
- Do not commit generated artifacts (chapter files, nutshells) from an
  in-progress book ingest — wait for the run to finish; Stage 2
  validation will flag failed chapters.
- Do not assume `chNN` in a filename equals book chapter N. The legacy
  bug this codebase fixed was exactly that conflation.
- Do not write HTML directly into `previews/`. That directory is the
  frozen design exploration; live outputs go to `artifacts/`.
- Do not edit `artifacts/index.html` by hand expecting it to persist —
  it's regenerated on every artifact write.
- Do not introduce a second accent color into the design system. One
  saturated accent (cobalt) is load-bearing; semantic colors
  (`--ok`, `--warn`, `--crit`, `--insight`) are for actual state, used
  sparingly.
- Do not render `rubric` or `model_answer` into a course page — they are
  the open-task grading key and must stay server-side (chat only).
- Do not ship a runnable lab without running `lint_practice.py` — it
  **executes** each lab; a model solution that can't pass its own check is
  a hard error, not a warning.
- Do not inline Pyodide into artifacts (it's ~10 MB). Lazy-load it from
  CDN on first Python Run and degrade to "check with Claude" offline.
- Do not let a concept widget (or bespoke theory SVG) set a `fill` /
  `stroke` / `style` color — only `.plate`/`.illus` classes + CSS vars, so
  themes invert. The widget engine enforces this for generated SVG;
  `lint_concept_widgets.py` enforces it for bespoke SVG. Run it before
  shipping a course page with a widget or illustration.
- Do not persist concept-widget state. Widgets are exploration, not graded
  mastery; persisting would corrupt the `kg-lab-progress-v1` mastery math
  and break page reproducibility. They reset to authored defaults on load.


## 文件 .claude/skills/book-to-skill/SKILL.md

---
name: book-to-skill
description: >-
  Converts a technical or non-fiction book (PDF or EPUB) into a structured,
  two-tier Claude Code skill — extracting the author's named frameworks,
  techniques, anti-patterns, figures, and concept relationships into a
  knowledge base that loads cheaply and deepens on demand. Handles embedded
  images and scanned pages via native image understanding. Use this whenever
  the user wants to turn a book into a skill, study a book through Claude,
  apply an author's frameworks while working, or build a reusable knowledge
  base from a PDF or EPUB — even if they don't say the word "skill".
  Optional flags make it course-ready: --complete (verified full-coverage
  extraction, every element audited), --practice (per-chapter quizzes +
  in-browser runnable code labs + open tasks), or --course (both); practice is
  what /the-knowledge-guy renders into an interactive learn-by-doing course.
when_to_use: >-
  Trigger phrases — "turn this book into a skill", "create a skill from this
  PDF", "create a skill from this EPUB", "convert PDF to skill", "convert EPUB
  to skill", "I want to study X book", "add this book to my skills", "make a
  skill out of this book", "analyze this book", "extract frameworks from this
  book", "build a knowledge base from this book". Accepts a path to a PDF or
  EPUB and an optional skill-name slug.
disable-model-invocation: false
context: fork
agent: general-purpose
allowed-tools: >-
  Bash(uv *) Bash(bash *) Bash(mkdir *) Bash(cp *) Bash(mv *)
  Bash(rm *) Bash(find *) Bash(wc *) Bash(echo *) Bash(cat *) Bash(ls *)
  Bash(test *) Bash(file *) Bash(date *) Read Write Glob Grep Task
argument-hint: <path-to-pdf-or-epub> [skill-name-slug] [--complete] [--practice] [--course]
arguments: [book_path, skill_name]
effort: high
---

# Book-to-Skill Converter

> **Empty-args guard (read first).** This guard fires **only** when the
> user invoked `/book-to-skill` with no positional argument at all
> (i.e. `$book_path` is the empty string or unset). In that one case,
> reply only with:
>
> > book-to-skill needs a PDF or EPUB path.
> > Usage: `/book-to-skill /path/to/book.pdf [skill-name]`
>
> and end the turn — do not invoke any other skill, do not resume any
> prior walk, do not load `the-knowledge-guy`.
>
> **If `$book_path` is non-empty, do NOT trigger this guard.** Whether
> the path is valid (exists, is a PDF/EPUB, etc.) is checked by Step 0
> below using `test -f` and `file`. Never decide validity from the path
> string alone — always run the actual filesystem check first.

Turn a book into a Claude Code skill that is **expert by default and deep on
demand**. The result is not a book report — it is a toolkit of the author's
crystallised frameworks, plus a concept map of how those frameworks connect.

## Philosophy

- **Extract structure, not summaries.** Capture named frameworks, exact
  techniques, anti-patterns, and figures — not chapter recaps.
- **Plumbing in Python, intelligence in Claude.** `scripts/extract.py` does
  only mechanical extraction. Every act of *understanding* — what a framework
  is, what a diagram means, how concepts relate — is Claude's work.
- **Two tiers.** The generated `SKILL.md` is the always-loaded expert (a
  concept map + topic index). The `chapters/` files are the depth, paged in
  only when needed. This is why a 600-page book becomes a skill that costs a
  few thousand tokens to consult, not 400K.
- **Raw stays with the skill.** The mechanical extraction (full text,
  per-chapter raw text, images, metadata, spine) is preserved inside the
  generated skill at `<slug>/raw/`. The chapter `.md` files are summaries;
  the raw lets the skill (and the user) re-read original passages, quote
  exactly, or re-extract a chapter without re-running Stage 0.

## Architecture — a map-reduce pipeline

```
Stage 0   EXTRACT   extract.py → text + images + per-chapter slices + offsets
Pass 0    SPINE     fast read of ToC + intros → the book's thesis & framework list
Stage 1   MAP       each chapter → one chapter file   (parallel subagents)
Step 7.5  AUDIT     each chapter → coverage verdict; re-run any gaps  (complete mode)
Stage 2   REDUCE    all chapter files → concept map + topic index → SKILL.md
Stage 2.5 NUTSHELL  each chapter file → one micro-summary block → nutshell.md
Stage 3   PRACTICE  each chapter → one practice set (quizzes/labs/tasks)  (opt-in)
```

Stage 1 maps over chapters; Stage 2 reduces over chapter *extractions*. Stage 2
never sees the full text — only the small chapter files — so book length never
breaks the context budget. The reduce step **consolidates and connects**; it
does not summarise summaries.

## Modes

Route by what the user asks:

1. **Full conversion** (default) — a PDF/EPUB path with no special request.
   Run all steps.
2. **Analyze only** — "analyze", "just extract", "let me review first". Run
   Steps 0–5, produce the extraction report, stop. Do not generate skill files.
3. **Resume** — a prior run was interrupted, or the user says "resume". See
   *Resuming* at the end; re-run is safe and skips completed work.

---

## Step 0 — Out-of-scope check

If the argument is not a path to a PDF or EPUB, stop:
> "book-to-skill needs a PDF or EPUB path. Usage:
> `/book-to-skill /path/to/book.pdf [skill-name]`"

## Step 0.5 — Resolve the book-to-skill install path

The skill can live in **either** the current project's `.claude/skills/` or
the user's `~/.claude/skills/`. Resolve which once and reuse:

```bash
BTS_DIR=""
for cand in "$(pwd)/.claude/skills/book-to-skill" "$HOME/.claude/skills/book-to-skill"; do
  if [ -f "$cand/scripts/extract.py" ]; then BTS_DIR="$cand"; break; fi
done
test -n "$BTS_DIR" || { echo "book-to-skill: install not found"; exit 1; }
```

Every reference below to `${BTS_DIR}` is this resolved path. Do not hard-code
either location.

## Step 0.6 — Flag shortcuts (optional)

The invocation may carry any of these flags alongside the path/slug. **Strip
them from the arguments before resolving `skill_name`** — a `--…` token must
never become the slug — and set the matching toggle. Each flag is exactly
equivalent to the user saying the corresponding phrase at Step 4:

| Flag | Effect |
|---|---|
| `--complete`, `--complete-coverage` | `WITH_COVERAGE=complete` — verified full coverage (every element, audited + gap-filled) |
| `--practice`, `--with-practice` | `WITH_PRACTICE=yes` — Stage 3 per-chapter quizzes + runnable labs + open tasks |
| `--course` | **both** of the above — the "I want an interactive `/the-knowledge-guy course`" shortcut |
| `--regenerate` | overwrite an existing skill's outputs (re-run stages even if files exist) |

When a flag has pre-decided a choice, still show the Step-4 cost estimate (cost
stays explicit) but **don't re-prompt that option** — only wait for the final
"proceed?" confirmation. No flags = today's fully-interactive default, unchanged.

## Step 1 — Validate input and dependencies

```bash
test -f "$0" && file "$0"
```

Confirm the extension is `.pdf`/`.epub` or the magic bytes are `%PDF`/`PK`.
Then ensure the extraction libraries are present:

```bash
bash "${BTS_DIR}/scripts/setup.sh"
```

`setup.sh` requires [`uv`](https://docs.astral.sh/uv/) — it creates a venv at
`${BTS_DIR}/.venv` and installs PyMuPDF, ebooklib,
beautifulsoup4, and pypdf into it via `uv pip install`. PyMuPDF is
the primary backend (text + images + tables + outline + page rendering in one
library). If it cannot be installed, the extractor falls back to text-only and
**images and scanned pages will be skipped** — tell the user if that happens.

## Step 2 — Identify the genre

Read `reference/genre-profiles.md`. Then ask the user:

> "What kind of book is this? It changes how I extract.
>
> ─ Preserve tables / code / exact wording ─
>  1. **Technical** — programming, engineering, architecture
>  2. **Vuln-hunting / security** — offensive security, exploitation, RE
>  3. **Financial** — investing, valuation, markets, quant
>  4. **Scientific** — academic, research methods, dense reference
>  5. **Legal / regulatory** — statutes, case law, compliance, doctrine
>  6. **Textbook** — pedagogical, sections + exercises
>  7. **Reference / cookbook** — recipe-style, self-contained primitives
>
> ─ Prose-driven ─
>  8. **Business / leadership** — org-level frameworks, decision rules
>  9. **Psychology** — biases, effects, popular cog-sci (Kahneman, Ariely)
> 10. **History** — eras, events, causes, dated actors
> 11. **Productivity** — habits, decision-making, mental models
> 12. **Biography / memoir** — life arcs, turning-point decisions
> 13. **Narrative non-fiction** — case-study or argument-driven
> 14. **Not sure** — I'll treat it as general"

Store the choice as `GENRE`. It selects the profile that governs the chunk
boundary, the chapter schema, and the reduce emphasis for the rest of the
run. If the user is unsure between two, consult the **Selector heuristics**
section at the bottom of `genre-profiles.md` before committing.

## Step 3 — Extract (Stage 0)

Best-effort sweep of stale staging dirs from previous runs (never fail
the run on this):

```bash
find /tmp -maxdepth 1 -name 'book_skill_work*' -type d -mtime +1 \
  -exec rm -rf {} \; 2>/dev/null || true
```

```bash
uv run --python "${BTS_DIR}/.venv/bin/python" \
  "${BTS_DIR}/scripts/extract.py" "$0" \
  --mode <technical|text> --genre <GENRE> --coverage <standard|complete> \
  --work-dir /tmp/book_skill_work
```

Pass `--coverage complete` when the user chose complete-coverage mode (Step 4,
`WITH_COVERAGE=complete`); otherwise `--coverage standard` (the default). In
complete mode the extractor floors the image threshold to 110px so real figures
aren't dropped before the LLM ever sees them.

(Equivalent: `"${BTS_DIR}/.venv/bin/python" "${BTS_DIR}/scripts/extract.py"
…` — the venv created by `setup.sh` is the single source of truth for the
extractor's dependencies.)

Use `--mode technical` for genres **1–7** (anything that needs tables,
code, or exact wording preserved — technical, vuln-hunting, financial,
scientific, legal, textbook, reference). Use `--mode text` for genres
**8–13** (prose-driven — business, psychology, history, productivity,
biography, narrative). For `general` (14), default to `--mode text` unless
the user overrides.

The work-dir is a staging area; Step 6 moves everything into the generated
skill at `<slug>/raw/` once the slug is known. This writes to
`/tmp/book_skill_work/`:

- `full_text.txt` — assembled reading-order text, with `[[IMAGE: ...]]` and
  `[[PAGE_SCAN: ...]]` placeholders anchored where they occur.
- `raw_chapters/chNN.txt` — each chapter pre-cut as its own file.
- `images/` — every kept figure, plus rendered pages of scanned PDFs.
- `metadata.json` — chapter offset map, image manifest, token estimates,
  granularity diagnosis, and scan-ratio fields:
  - `chapters_source` — `"raw_chapters"` initially, becomes `"chapters_split"`
    when a manual re-split is in effect.
  - `granularity_warning` — non-null when chapters look over-merged.
  - `scan_cost_warning` — true when ≥ 10% of pages are image-only.
  - `is_scanned_document` — true when ≥ 55% are image-only.

Read `metadata.json`. Surface both warnings to the user before continuing:
- `is_scanned_document: true` → chapter text will come from vision OCR;
  expect higher cost.
- `scan_cost_warning: true` (and not fully scanned) → some pages are
  image-only; vision-OCR cost will be elevated.

### Granularity check — automatic re-split (no manual opt-in)

The pipeline never ships a few merged mega-chapters or a single "Full Text"
blob. Always run the heading detector and capture its candidate count:

```bash
"${BTS_DIR}/.venv/bin/python" "${BTS_DIR}/scripts/detect_chapters.py" \
  /tmp/book_skill_work/full_text.txt --table
```

Let `A = metadata.json["chapter_count"]` and `B = detector candidate count`.
**Re-split automatically** (don't wait for the user — just surface the
before/after counts) when ANY of these holds:

- `metadata.json["granularity_warning"]` is non-null **and** `B ≥ max(5, A+2)`,
- `A == 1` **or** the sole chapter title is `"Full Text"`,
- `WITH_COVERAGE=complete` **and** `B ≥ A+2`.

Say e.g. *"Granularity: extractor found A chapters; detector found B —
auto-re-splitting into the finer set."* Otherwise keep `raw_chapters/` (and say
so). To re-split:

1. For each candidate `i` with `char_start=S_i` (and next start `S_{i+1}`,
   or end-of-file), write `/tmp/book_skill_work/chapters_split/chNN.txt`
   containing `full_text[S_i:S_{i+1}]`.
2. Overwrite `metadata.json["chapters"]` with the new list of
   `{index, title, slug, char_start, char_end, est_tokens, book_number,
   raw_text_path}` entries pointing at `chapters_split/` (run the same
   `assign_book_numbers` labelling).
3. Set `metadata.json["chapters_source"] = "chapters_split"` and refresh
   `chapter_count` / `granularity_warning` (now null).

**Worst case — the detector also returns < 2 candidates** (no outline, no
headings at all, so the extractor produced a single `"Full Text"` chapter):
do not proceed merged. Fixed-size tile instead — split `full_text.txt` into
`ceil(len/40000)` equal slices (~10K tokens each), titled `"Section 1..N"`,
written to `chapters_split/` exactly as above. (The char ranges still tile the
whole document with no gaps — `finalize_chapter_ranges`' contract.)

From this point onward, Stage 1 reads `chapters_split/` instead of
`raw_chapters/`. Step 6 moves both directories into the skill's `raw/`
so the original auto-extraction is preserved as a record.

## Step 4 — Pre-flight cost estimate

Read pricing from `${BTS_DIR}/reference/pricing.json` and inject it into
the estimate. If `pricing.as_of` is more than 90 days behind today's
date, prepend: `⚠ Reference prices are dated <as_of> — verify current
rates at the source URL before committing.`

From `metadata.json`, present an estimate **before generating anything**:

```
📖 <title> (<format>) — <page_count> pages, <chapter_count> chapters
📄 Text ~<estimated_text_tokens/1000>K tokens | Images <image_count> (~<estimated_image_tokens/1000>K vision tokens)
⚠ <scanned_pages> of <page_count> pages are image-only (~10× vision cost)   ← only if scan_cost_warning
⚠ Chapter granularity: <granularity_warning>                                 ← only if non-null

💰 Estimated token cost (full conversion):
   Input  ≈ <estimated_total_tokens × 1.4>   (chapter reads + image reads + prompts)
   Output ≈ <chapter_count × 1,100 + 9,000>  (chapter files + SKILL.md + supporting files)

   Reference API prices (per MTok, as of <pricing.as_of>):
     <for each model in pricing.models: label — $<input> in / $<output> out>

📁 Will generate: SKILL.md + <chapter_count> chapter files + glossary + patterns + cheatsheet + nutshell + chapters_manifest.json
➡  Proceed with full conversion? (or say "analyze only" to preview first)

🎓 Optional — interactive practice (Stage 3): add a per-chapter practice set
   (auto-checked quizzes + in-browser code labs + open tasks) so the book can
   be rendered as an interactive `/the-knowledge-guy course`. Best for technical
   / textbook / vuln-hunting books. Adds ~1 subagent per eligible chapter
   (≈ +<chapter_count × 1,400> output tokens). Say "with practice" to include it.

🔎 Optional — COMPLETE coverage (verified): by default I extract dense, capped
   toolkits (~800–1,400 tokens/chapter; signal over completeness). In COMPLETE
   mode I instead capture EVERY load-bearing element in every chapter (each
   framework, code example, figure, table, anti-pattern, exercise, definition),
   with no token cap, then run a per-chapter COVERAGE AUDIT and automatically
   re-run any chapter with gaps until every chapter passes. Materially more
   expensive — roughly 2.5–4× standard:
     Toolkits ≈ <chapter_count × 3,000> output (no cap)
     Audit    ≈ <chapter_count × 700> output × ~1.6 rounds (reads RAW + toolkit)
     Gap-fill ≈ re-runs the thinnest ~<round(chapter_count × 0.6)> chapters once
   Say "complete coverage" for verified-complete extraction; otherwise I use
   standard mode.
```

Wait for confirmation. If the user says "analyze only", switch to Mode 2. If
the user opts in with "with practice" (or passed `--practice`/`--course` per
Step 0.6, or the genre is technical / textbook /
vuln-hunting and they accept the suggestion), set `WITH_PRACTICE=yes` and run
**Step 8.6** after the nutshell. If the user says "complete coverage" (or passed
`--complete`/`--course` per Step 0.6; phrases:
"complete coverage", "cover everything", "don't skip anything"), set
`WITH_COVERAGE=complete` — this passes `--coverage complete` to extract.py
(Step 3), makes the auto-re-split mandatory, injects the complete-mode mandate in
Step 7, and runs the **Step 7.5** audit + gap-fill loop with the Step-10 coverage
gate. `WITH_COVERAGE` is independent of `WITH_PRACTICE` (both can be on). Default
is `standard` — today's cheap path, unchanged. Otherwise skip Stage 3 — it is
purely additive and can be run later by re-invoking with `--regenerate` once
practice support
is wanted.

## Step 5 — Pass 0: build the spine

A chapter extractor that hasn't seen the whole book cannot tell what is central
versus incidental. Fix that cheaply first.

Build the spine **mechanically**, not impressionistically — every chapter
extractor reads it, so weak input here propagates everywhere.

1. Read `full_text.txt` chars `0–8,000` (front matter + ToC region).
2. For each chapter listed in `metadata.json["chapters"]`, read the first
   1,000 characters of its raw file (whichever directory
   `metadata.json["chapters_source"]` points at).
3. Synthesise the three sections below from those fragments only. Do not
   pull from the full chapter bodies — that's Stage 1's job.

Write to `/tmp/book_skill_work/spine.md`:

```markdown
# Spine — <Title> by <Author>
## Thesis
<2–3 sentences: what the whole book argues.>
## Framework Inventory
- <Framework name> — <one line> (≈ ch<N>)
## Domain & Vocabulary
<the subject area and 5–10 distinctive terms the book uses.>
```

The spine is passed to **every** chapter extractor in Stage 1 so each one
extracts in light of where the book is going.

**If Mode 2 (analyze only):** produce the extraction report now from the spine
plus a skim of the chapter files — frameworks, principles, techniques,
anti-patterns, a suggested skill name, and a detected-chapters table — then
stop.

## Step 6 — Purpose, skill name, scaffolding

Ask the purpose (weights what the Core section foregrounds):
> "What should this skill help you do? (1) apply the author's frameworks while
> working (2) think with the author's mental models (3) reference specific
> chapters (4) all of the above"

Determine the skill slug: use argument `$1` if given; otherwise propose
`{author-lastname}-{core-concept}` and `{book-title-hyphenated}` and let the
user pick.

**Output destination — project-local.** The generated skill is written to the
**current working directory's** `.claude/skills/<slug>/` — i.e. the project
the user invoked `/book-to-skill` from. Resolve once and reuse:

```bash
SKILLS_ROOT="$(pwd)/.claude/skills"
SKILL_DIR="${SKILLS_ROOT}/<slug>"
mkdir -p "${SKILL_DIR}/chapters" "${SKILL_DIR}/raw" || {
  echo "FATAL: cannot create ${SKILL_DIR} — check permissions on $(pwd)/.claude/" >&2
  exit 1
}
```

`mkdir -p` will also create `$(pwd)/.claude/` if missing — the user has
explicitly asked for project-local skills. If the hard error fires, stop;
do not silently fall back to `~/.claude/skills/`. Confirm `${SKILL_DIR}/`
does not already exist with content; if it does, append `-2` or ask.

**Legacy-skill check.** If `${SKILL_DIR}/chapters_manifest.json`
already exists from a prior run, inspect it:

```bash
sv=$(python3 -c "import json,sys;print(json.load(open('${SKILL_DIR}/chapters_manifest.json')).get('schema_version',1))" 2>/dev/null)
if [ "$sv" != "2" ]; then
  echo "⚠  Existing manifest is schema_version=$sv (legacy chapter numbering)."
  echo "   Run: ${BTS_DIR}/scripts/backfill_book_numbers.py ${SKILL_DIR}"
  echo "   Or delete the manifest to start fresh, then re-run /book-to-skill."
  exit 1
fi
```

This stops Stage 1 before it would overwrite chapter files with the
wrong numbering, which would silently corrupt SKILL.md links and
nutshell citations. The user can resolve by either running
`backfill_book_numbers.py` (preferred — preserves any existing chapter
content) or deleting the manifest (preferred only for a full re-extract).

**Move the raw extraction into the skill.** The work-dir from Step 3 is
staging; the raw extraction is part of the skill from now on. Move it in and
write `progress.json` inside it:

```bash
mv /tmp/book_skill_work/full_text.txt    "${SKILL_DIR}/raw/"
mv /tmp/book_skill_work/raw_chapters     "${SKILL_DIR}/raw/"
mv /tmp/book_skill_work/chapters_split   "${SKILL_DIR}/raw/" 2>/dev/null || true
mv /tmp/book_skill_work/images           "${SKILL_DIR}/raw/" 2>/dev/null || true
mv /tmp/book_skill_work/metadata.json    "${SKILL_DIR}/raw/"
mv /tmp/book_skill_work/spine.md         "${SKILL_DIR}/raw/"
echo '{"stage1_done": [], "stage2_done": false}' > "${SKILL_DIR}/raw/progress.json"
```

`chapters_split/` only exists if a manual re-split was performed in Step 3.
When present, it takes precedence in Stage 1.

From this point onward, **every path that used to point into
`/tmp/book_skill_work/` now points into `${SKILL_DIR}/raw/`** (chapter raw
text, spine, metadata, images, progress).

## Step 7 — Stage 1: MAP (chapter extraction)

Read `reference/chapter-template.md`. Then, for each chapter in
`metadata.json`, generate
`${SKILLS_ROOT}/<slug>/chapters/<book_number>-<slug>.md` (the
project-local skills root resolved in Step 6).

**Filename prefix uses `book_number`, not the manifest `index`.**
`metadata.json["chapters"][*].book_number` is the book-native label
that `extract.py` assigns: `ch07` for "Chapter 7 — …", `intro` for
the Introduction, `preface`, `appendix-a`, `fm` / `fm-2` for front
matter, `bm` for back matter, `part-1` for "Part I". The `index`
field is still present but is extraction order only — never use it
in filenames or in user-facing labels. If `book_number` is missing
(extremely old skills), fall back to `ch{index:02d}` and log it.

**Choose the chapter source directory once, up front:**

```
if metadata.json["chapters_source"] == "chapters_split":
    CHAPTERS_DIR = "${SKILL_DIR}/raw/chapters_split"
else:
    CHAPTERS_DIR = "${SKILL_DIR}/raw/raw_chapters"
```

Pass `CHAPTERS_DIR` into every subagent task. Don't hardcode `raw_chapters/`
— a manual re-split won't take effect otherwise.

**Resume = filesystem is ground truth.** Before spawning subagents, list
existing files in `${SKILL_DIR}/chapters/`. For every
`<book_number>-*.md` that already exists and is `> 500 bytes` and does
not contain "extraction failed", that chapter is done — skip it.
`progress.json` is a running log only; do not use it to drive resume
decisions.

**Parallelise.** Spawn the chapters as parallel subagents with the `Task` tool
— independent contexts keep each extraction sharp and the run survives length.
Batch them (e.g. 5–8 at a time) for a long book. Give each subagent this task:

```
Extract one chapter into a Claude Code skill chapter file.

Inputs (substitute <SKILL_DIR> with the absolute project-local path from
Step 6 and <CHAPTERS_DIR> with the source chosen above):

  - Chapter raw text:  <CHAPTERS_DIR>/<book_number>.txt
  - Book spine:        <SKILL_DIR>/raw/spine.md   (read for context)
  - Genre profile:     <paste the relevant profile from genre-profiles.md>
  - Chapter template:  <BTS_DIR>/reference/chapter-template.md
                       (substitute the path resolved in Step 0.5)

Steps:
  1. Read the spine, then the chapter raw text.
  2. If the raw text is < 300 chars or obviously garbled (e.g. < 50% real
     words), do NOT invent content. Write a stub:
       # <Book number> — extraction failed
       Raw source is <X> chars / appears corrupted. Inspect
       <CHAPTERS_DIR>/<book_number>.txt and re-extract if needed.
     Save to <SKILL_DIR>/chapters/<book_number>-extraction-failed.md and
     report "CHAPTER FAILED: <book_number>" to the orchestrator. Do not
     proceed.
  3. For every [[IMAGE: images/..]] or [[PAGE_SCAN: images/..]] placeholder,
     Read <SKILL_DIR>/raw/<that path> and fold its meaning into the chapter
     file as text (per the template's image-handling section — including
     its rules for failed reads).
  4. Write the chapter summary file to:
     <SKILL_DIR>/chapters/<book_number>-<chapter-slug>.md
     following the chapter template, adapted to the genre profile. The raw
     source remains at <CHAPTERS_DIR>/<book_number>.txt — do not delete or
     modify it.

Extract structure, not summary. Preserve exact framework names. 800–1,400
tokens. Report the chapter title and key frameworks when done.
```

**Complete-coverage mode (`WITH_COVERAGE=complete`).** Replace that final
paragraph of the subagent prompt with the complete-mode mandate:

```
Extract structure, not summary. Preserve exact framework names. COMPLETE-COVERAGE
MODE: no token cap — produce a toolkit containing EVERY load-bearing element
present in this chapter (every named framework, code example, figure, reference
table, anti-pattern, exercise, key definition). Condense prose/narration; never
drop a load-bearing element. Omit a template section only if that element is
genuinely absent from THIS chapter — the genre profile's de-emphasis is NOT a
reason to drop a present element. For every fenced code block, [[IMAGE]] /
[[PAGE_SCAN]] placeholder, and table in the raw text, ensure a corresponding
entry exists in the toolkit (or a one-line "decorative" / "could not be read"
note). Report the chapter title, key frameworks, and a one-line element tally
(frameworks/code/figures/tables/anti-patterns/exercises/definitions) when done.
```

(A Step-7.5 audit verifies this and re-runs any chapter that skipped something,
so completeness here avoids a re-run.)

After each batch, append completed chapter numbers to
`${SKILL_DIR}/raw/progress.json`. If a subagent fails, retry that one
chapter — do not restart the run.

## Step 7.5 — COVERAGE AUDIT + gap-fill (complete mode only)

**Run this only if `WITH_COVERAGE=complete`** (Step 4). Skip it entirely in
standard mode (zero cost there). It *proves* every chapter toolkit captured every
load-bearing element in its raw chapter, and re-runs any chapter that didn't —
ingest will not reach "done" with a known gap. Read the frozen contract first:
`${BTS_DIR}/reference/coverage-audit-template.md` (schema, the
load-bearing/decorative/needs-manual-review rules, `THRESHOLD=0.95`,
`N_ROUNDS=3`). Like Stage 1, this is a parallel per-chapter fan-out.

`mkdir -p "${SKILL_DIR}/raw/coverage"`. Eligible chapters = the same set Stage 1
extracted (skip `fm`/`bm` and `word_count < 300`).

**The loop** (`THRESHOLD = 0.95`, `N_ROUNDS = 3`):

```
for round in 1..3:
  1. MECHANICAL pre-check (cheap, all chapters):
        "${BTS_DIR}/.venv/bin/python" "${BTS_DIR}/scripts/lint_chapters.py" \
          "${SKILL_DIR}" --coverage --json   →  {book_number: [figure deficits]}
  2. AUDIT (LLM, parallel, batched 5–8) every chapter NOT already passing on disk
     (a chapter is passing iff raw/coverage/<bn>.json exists, parses, and
     verdict=="complete"). Each audit subagent uses the prompt in
     coverage-audit-template.md, reads the raw slice + the toolkit, and writes its
     JSON verdict to ${SKILL_DIR}/raw/coverage/<book_number>.json. Spawn them with
     a recognizable label (coverage-audit-<bn>) so measure_ingest.sh attributes them.
  3. failing = chapters where audit.verdict=="gaps" OR audit.coverage < 0.95
               OR audit.missing is nonempty OR the mechanical pre-check found a deficit.
  4. if failing is empty: break — every chapter is covered.
  5. if round == 3: stop looping; record residuals (below).
  6. GAP-FILL: re-run the Stage-1 subagent (complete-mode mandate) for each failing
     chapter, appending the gap-fill addendum from coverage-audit-template.md —
     "keep everything already present and ADD: <missing[].name + raw_evidence>,
      <mechanical deficits>". Overwrite chapters/<bn>-<slug>.md. DELETE that
     chapter's raw/coverage/<bn>.json so it is re-audited next round. Label these
     gapfill-<bn>.
```

**Residuals.** After the loop, any chapter that never reached `verdict=="complete"`
is written to `${SKILL_DIR}/raw/coverage/RESIDUALS.json`
(`{book_number: {coverage, missing, needs_manual_review}}`) and **surfaced loudly**
— it is carried to the Step-10 gate. `needs_manual_review` figures (genuinely
unreadable) are reported for inspection but are **not** gaps.

**Resume** is filesystem-driven and idempotent: a chapter with a passing
`raw/coverage/<bn>.json` is skipped on re-run; gap-fill deletes the JSON so only
re-extracted chapters are re-audited. `progress.json` stays a log only.

## Step 8 — Stage 2: REDUCE (concept map)

**Lint first.** Run the quality check on the chapter files before reduce
reads them — surfaces runaway word counts, missing structural headings,
and verbatim-quote copy-pastes:

```bash
"${BTS_DIR}/.venv/bin/python" "${BTS_DIR}/scripts/lint_chapters.py" \
  "${SKILL_DIR}"
```

Lint warnings are advisory: show them to the user. Re-run any chapter
that fails badly before reading on (a chapter with "extraction failed"
or 6,000 words will degrade the concept map). Do not block — the user
decides.

Read `reference/concept-map-spec.md`. Then:

1. Read **every** generated `chapters/ch*.md` file and `spine.md`.
2. **Consolidate** — dedupe recurring frameworks into single nodes, resolve
   refinements, pick the 6–10 load-bearing frameworks. (For financial/
   scientific genres, do not over-merge terms that differ subtly.)
3. Build the **concept map** (node list + typed edges).
4. Build the **topic index** — map the vocabulary a user would actually ask
   in, with synonyms and multi-chapter pointers. This is the bridge between
   the two tiers; a weak index makes "go to the chapter" fail.
5. Generate `glossary.md`, `patterns.md`, `cheatsheet.md`, sizing/sharding
   them to the book per the spec's scaling table.
6. If the topic index exceeds ~2,000 tokens (cap in `concept-map-spec.md`),
   keep the highest-frequency ~60 terms inline in `SKILL.md` and write the
   full version to `${SKILL_DIR}/topic-index-full.md`, linked from `SKILL.md`.
7. Write `${SKILL_DIR}/chapters_manifest.json` (schema in
   `concept-map-spec.md`).
   - Set `schema_version: 2` at the top.
   - Read `${SKILL_DIR}/raw/metadata.json` once. For each manifest
     entry, **copy `book_number` verbatim** from the matching
     metadata chapter (matched by `index`). `book_number` is the
     canonical label — never reconstruct it from `index` or from
     filenames; the source of truth is `extract.py:assign_book_numbers`
     and its output already lives in `metadata.json`.
   - `file` must equal `chapters/<book_number>-<slug>.md` (the
     filename Stage 1 actually wrote).
   - `status` is `extracted` | `failed`, derived from whether the
     file contains an "extraction failed" stub.
   - Refuse to write the manifest if any chapter is missing
     `book_number` in metadata — print the failing entries and stop;
     a missing `book_number` indicates extract.py did not run with
     `assign_book_numbers`, and proceeding would corrupt downstream
     renderers.

Set `stage2_done: true` in `${SKILL_DIR}/raw/progress.json` (log only).

## Step 8.5 — Stage 2.5: NUTSHELL (per-chapter micro-summaries)

Produce `${SKILL_DIR}/nutshell.md` — a per-chapter micro-summary skim
of the whole book, one ~100-word block per chapter, that the user can
scroll in a single response via `/the-knowledge-guy nutshell <slug>`.

This stage maps over the **chapter toolkit files**, not the raw text,
so cost scales with chapter count, not book size.

1. Read `${BTS_DIR}/reference/nutshell-template.md` (the schema and
   voice rules).
2. Read `${SKILL_DIR}/chapters_manifest.json`. **Skip** an entry if
   *any* of the following holds:
   - `word_count < 300` (front matter, acknowledgments, dedications,
     stubs).
   - `book_number` equals `fm` / `bm` or starts with `fm-` / `bm-`
     (any front- or back-matter slot, even if it happens to exceed the
     word threshold — the user wants chapters in a nutshell skim,
     not indexes or copyright pages).
3. For every remaining entry, spawn a parallel subagent (single
   message, N `Task` calls). Each subagent gets:
   - The template (inline).
   - The chapter's toolkit file path (`${SKILL_DIR}/<file>`).
   - The chapter index, title, and skill slug.
   - The one-line thesis from `${SKILL_DIR}/raw/spine.md` for tone.

   Each subagent returns exactly one nutshell block (80-120 words,
   3-5 bullets) following the template's "Required shape" section.
   No preamble, no closing remarks — just the block.

4. Concatenate the returned blocks in manifest order. Prepend:

   ```
   # <Book title> — in a nutshell

   > <one-line thesis pulled from spine.md>
   ```

5. Write to `${SKILL_DIR}/nutshell.md`. Target total length: ~2-3K
   tokens for a typical 15-25 chapter book.

If a subagent fails or returns a malformed block (no
`## <book_number>` heading, or >180 words), retry once. If it fails
twice, write a single-line stub for that chapter
(`## <book_number> — <title>\n\n*Nutshell generation failed.*`) and
continue — do not block the whole stage.

## Step 8.6 — Stage 3: PRACTICE (per-chapter exercises) — opt-in

**Run this only if `WITH_PRACTICE=yes`** (Step 4). It is purely additive:
it produces a per-chapter practice set that `/the-knowledge-guy course`
renders as an interactive learn-by-doing site (auto-checked quizzes,
in-browser runnable code labs, open tasks). Skipping it changes nothing
else; it can be added later by re-running with `--regenerate`.

Like Stage 1, this is a **parallel per-chapter subagent fan-out**; like the
nutshell, it maps over the **chapter toolkit files** (plus the raw slice),
so cost scales with chapter count. The frozen output contract is
`${BTS_DIR}/reference/practice-template.md` — read it first.

### Prep (orchestrator, once)

1. Read `${BTS_DIR}/reference/practice-template.md` (schema, the three
   exercise families, the extract/generate/research decision tree, the lab
   safety rails).
2. Resolve the genre from `metadata.json` (normalize a stored menu-number
   to a slug — `lint_practice.py:resolve_genre` has the mapping). Compute
   `is_codey = genre in {technical, vuln-hunting, textbook, scientific, reference}`
   and `is_cyber = genre == vuln-hunting` (or the spine vocabulary is
   security-heavy). Stage 3 targets technical / textbook / vuln-hunting
   first; other genres degrade to `auto` + `open` only.
3. Resolve `<CHAPTERS_DIR>` exactly as Step 7 does (the dir named by
   `metadata.json["chapters_source"]` — `chapters_split/` if a re-split
   happened, else `raw_chapters/`). **Do not hardcode `raw_chapters/`.**
4. `mkdir -p "${SKILL_DIR}/practice" "${SKILL_DIR}/raw/research"`.
5. Eligible chapters = manifest entries **excluding** `book_number` starting
   `fm`/`bm` and `word_count < 300` (same skip rule as the nutshell).
6. **Resume (filesystem-driven):** a chapter is done iff
   `practice/<book_number>-<slug>.json` exists, parses, and has ≥ 1
   exercise. Skip those. (An empty/failed stub does **not** count — retry it.)

### Fan-out (one subagent per remaining chapter, batched 5–8)

Each subagent reads: the chapter toolkit `chapters/<book_number>-<slug>.md`
(primary), the raw slice `<CHAPTERS_DIR>/<book_number>.txt`, `raw/spine.md`,
the genre's profile block, `reference/practice-template.md`, and
`raw/research/<book_number>.md` **if it already exists**. Its task prompt:

```
Generate a PRACTICE set for ONE chapter, following the frozen schema in
practice-template.md (read it). Inputs (absolute paths substituted):
  - Chapter toolkit:  <SKILL_DIR>/chapters/<book_number>-<slug>.md
  - Raw chapter text: <CHAPTERS_DIR>/<book_number>.txt
  - Spine:            <SKILL_DIR>/raw/spine.md
  - Schema + genre profile: practice-template.md + the <genre> block (inline)
  - Research cache (READ if it exists): <SKILL_DIR>/raw/research/<book_number>.md
  - Web tools (ONLY if is_cyber/is_codey AND a realistic lab needs current
    external detail AND no cache exists yet): WebSearch, WebFetch

Steps:
  1. Read the toolkit, then the raw slice. Decide extract-vs-generate
     (does the raw text contain exercises? signals: "Exercise", "Problems",
     "Lab", "Challenge", "Q1"…). Extract & complete the book's own where
     present; otherwise generate from the toolkit's Frameworks / Anti-patterns
     / Code Examples — every exercise's tests.framework MUST name a real one.
  2. If web research is warranted and no cache exists: WebSearch/WebFetch,
     then distil findings to <SKILL_DIR>/raw/research/<book_number>.md with
     source URLs + today's date (one `date +%Y-%m-%d` call). If a cache
     exists, READ it — do not search again.
  3. Produce 4–8 exercises: ≥2 auto, ≥1 runnable (ONLY if a code example
     exists; prefer runtime "js" so it runs offline), ≥1 open.
     - For every runnable lab: write solution_code AND a deterministic
       assert/stdout check, and TRACE the solution through the check to
       confirm it passes and the starter fails. Pure functions only — no
       I/O, network, clock, randomness (the lint will EXECUTE it).
     - For every MCQ-shaped item: exactly ONE correct option; distractors
       are plausible misconceptions, not nonsense.
     - For every open task: include rubric + model_answer (server-side only).
  4. Write <SKILL_DIR>/practice/<book_number>-<slug>.json (canonical) and a
     <book_number>-<slug>.md mirror. Cite by book_number; preserve exact
     framework names. A faithful 4-exercise set beats a padded 8.
```

A subagent that fails writes a stub `{"exercises": []}` (which resume will
retry); never block the whole stage on one chapter.

### Validate (orchestrator)

Run the lint — it **executes** every runnable lab and hard-fails any whose
model solution doesn't pass its own check:

```bash
${BTS_DIR}/.venv/bin/python ${BTS_DIR}/scripts/lint_practice.py "${SKILL_DIR}"
```

**Re-run any chapter the lint flags with a hard ERROR** (broken lab, bad
MCQ, bad book_number) before declaring Stage 3 done. Warnings are advisory.
Set `stage3_done: true` in `raw/progress.json` (log only). Stage 3 does
**not** bump `chapters_manifest.json` — practice is discovered by file
presence, and `schema_version` stays `2`.

## Step 9 — Write the master SKILL.md

Using the template in `concept-map-spec.md`, write
`${SKILLS_ROOT}/<slug>/SKILL.md`. Keep the body under ~4,000 tokens and
front-load it (truncation eats the end). It must contain: the book thesis, the
concept map, the Core Frameworks section, the chapter index (linked), the
topic index, and the supporting-files links.

## Step 10 — Validate, clean up, report

Validate before declaring done:

```bash
test -f "${SKILLS_ROOT}/<slug>/SKILL.md"
test -f "${SKILLS_ROOT}/<slug>/chapters_manifest.json"
test -f "${SKILLS_ROOT}/<slug>/nutshell.md"
ls "${SKILLS_ROOT}/<slug>/chapters/" | wc -l   # == chapter_count
# Surface any chapters that bailed out during Stage 1:
grep -l "extraction failed" "${SKILLS_ROOT}/<slug>/chapters/"*.md || true
# Surface any nutshell blocks that failed:
grep -l "Nutshell generation failed" "${SKILLS_ROOT}/<slug>/nutshell.md" || true
# schema_version + book_number presence — every entry must have one,
# and every `file` field must reference a chapter that actually exists.
python3 - <<'PYEOF'
import json, os, sys
p = "${SKILLS_ROOT}/<slug>/chapters_manifest.json"
m = json.load(open(p))
assert m.get("schema_version") == 2, f"manifest schema_version != 2 ({m.get('schema_version')!r}); see Step 8."
bad = [c for c in m["chapters"] if not c.get("book_number")]
assert not bad, f"{len(bad)} chapter(s) missing book_

（文件较长，此处截取前 40000 字符）

## 文件 .claude/skills/the-knowledge-guy/SKILL.md

---
name: the-knowledge-guy
description: >-
  Knowledge router AND interactive teacher across every book-derived skill in
  this project. Two modes — (1) **ask**: auto-discovers all domain skills
  (finance, vuln hunting, AI security, red-teaming, personal growth, ...),
  picks the relevant ones, invokes them in parallel as focused subagents,
  and synthesises one comprehensive cross-domain answer; (2) **walk**:
  proposes a curriculum and walks the user through it interactively — one
  concept at a time, taught from the source chapters, then quizzed via
  forced-choice questions, with progress saved across sessions; (3)
  **course**: renders interactive learn-by-doing websites per chapter —
  theory plus auto-checked quizzes, in-browser runnable code labs, and
  open-ended tasks graded by Claude.
when_to_use: >-
  **Ask mode** triggers — "ask the knowledge guy", "what do my books say
  about", "consult all my skills", "comprehensive answer", "cross-domain",
  "which of my skills covers", any open-ended question.
  **Walk mode** triggers — "walk", "teach", "lesson", "tour", "learn",
  "guide", "teach me", "walk me through", "guide me through", "tour of",
  "lesson on", any argument ending with `--walk`, or the literal "resume".
  **Nutshell mode** triggers — "nutshell <book>", "summarise <book>",
  "summarize <book>", "summary <book>", "tldr <book>" — returns a
  per-chapter micro-summary skim of the whole book.
  **Course / lab mode** triggers — "course <book>", "lab <book> [<chapter>]",
  "practice <book>", "hands-on <book>", "drills <book>", "exercises <book>",
  "learn by doing" — builds an interactive learn-by-doing site per chapter
  (theory + auto-checked quizzes + in-browser code labs + open tasks).
  **Check sub-mode** triggers — "check <book> <chapter> <exercise-id>",
  "grade", "submit" — grades an open-ended practice answer against its rubric.
  **Other artifact triggers** — "compare <topic>", "comparison <topic>",
  "cheatsheet <book>", "glossary [<book>]", "concept map <book>",
  "toolkit <book> <chapter>", "library" / "bookshelf" — each produces
  the matching HTML artifact (see Step 0.5 below for the full list).
allowed-tools: >-
  Bash(ls *) Bash(find *) Bash(cat *) Bash(test *) Bash(pwd)
  Bash(mkdir *) Bash(date *) Bash(grep *)
  Read Write Edit Glob Grep Agent Skill AskUserQuestion
argument-hint: <question>  |  walk <topic>  |  course <book> [<ch>]  |  check <book> <ch> <id>  |  resume  |  nutshell <book>  |  compare <topic>  |  cheatsheet <book>  |  glossary  |  concept-map <book>  |  toolkit <book> <ch>  |  library  |  add <path-to-pdf-or-epub>
---

# the-knowledge-guy — knowledge router + interactive teacher

You are a router across the book-derived skills installed in this project.
Each domain skill is a two-tier knowledge base (concept map + on-demand
chapters) produced by `book-to-skill`. You have **several modes** —
all of them produce both a text response in chat AND an HTML artifact
in `artifacts/` using the shared design system:

- **Ask mode (default)** — fan out parallel subagents and synthesise one
  comprehensive cross-domain essay.
- **Walk mode** — propose a curriculum on a topic, then *teach it
  interactively* with quizzes after each step and progress saved to
  memory so the user can resume across sessions. Procedure in
  [walk-mode.md](walk-mode.md); worked transcripts in
  [examples.md](examples.md).
- **Course mode** — render an interactive *learn-by-doing* website per
  chapter: theory from the chapter toolkit, then a practice section with
  auto-checked quizzes, in-browser runnable code labs, and open tasks.
  Driven by the per-chapter `practice/<book_number>-<slug>.json` that
  book-to-skill's Stage 3 produces. The **check** sub-mode grades
  open-ended answers against their rubric and records progress.
- **Nutshell mode** — per-chapter micro-summary skim of a whole book.
- **Library mode** — render the bookshelf overview.
- **Comparison mode** — one concept across multiple books, side by side.
- **Cheatsheet mode** — operational one-pager for a book.
- **Glossary mode** — A-Z term lookup, per book or cross-library.
- **Concept-map mode** — Tier-1 framework graph for a book.
- **Toolkit mode** — Tier-2 deep-dive on a specific chapter.
- **Ingest mode** — hand off a PDF/EPUB to `book-to-skill`.

The user's argument is `$QUERY`. Treat the entire argument string as one
value.

---

## Step 0 — Artifacts awareness (do this first, every invocation)

Every output you produce gets written to `artifacts/` at the project
root, using the design system in
`.claude/skills/the-knowledge-guy/design-system/`. The folder is the
user's catalog and your cache. Before doing anything else:

```bash
ARTIFACTS="$(pwd)/artifacts"
test -d "$ARTIFACTS" || mkdir -p "$ARTIFACTS"
ls "$ARTIFACTS" 2>/dev/null
ls "$ARTIFACTS"/nutshells "$ARTIFACTS"/cheatsheets "$ARTIFACTS"/toolkits \
   "$ARTIFACTS"/concept-maps "$ARTIFACTS"/glossaries "$ARTIFACTS"/walks \
   "$ARTIFACTS"/comparisons "$ARTIFACTS"/synthesis "$ARTIFACTS"/courses 2>/dev/null
```

Use this listing to:

- **Reuse cached artifacts.** Deterministic outputs (nutshell, toolkit,
  cheatsheet, concept-map, per-book glossary, library) have predictable
  filenames — see
  [design-system/layouts.md](design-system/layouts.md) "Filename rules"
  for the full table. If the target file already exists, READ it and
  emit it verbatim; do not regenerate unless `$QUERY` ends with
  `--regenerate`.
- **Surface related artifacts.** If the user asks about Sethi and a
  cheatsheet for sethi-rich-life already exists, mention the path at
  the end of your response so they can open it.
- **Update the index.** After writing any new artifact, regenerate
  `artifacts/index.html` so the catalog stays current. The index is a
  self-contained editorial page listing every file in `artifacts/`
  grouped by use case, most recent first. Use the same design system.

---

## Mode dispatch (after Step 0)

Inspect `$QUERY`, checking in this order:

1. **Resume** — if `$QUERY` is the literal `resume`, **walk mode** (resume
   an existing walk — see walk-mode.md Step 1).
2. **Check** — starts with `check`, `grade`, or `submit` (typically
   `check <skill> <book_number> <exercise-id>`, often pasted from a course
   page's "Check with Claude" button) → **check sub-mode** below.
3. **Course** — starts with `course`, `lab`, `practice`, `hands-on`,
   `drill`, `drills`, or `exercises`; OR starts with "learn by doing" /
   "learn-by-doing"; OR ends with `--course` / `--lab` (strip the flag,
   keep the target) → **course mode** below. Checked before Walk so
   "learn by doing X" builds a course rather than walking; bare `learn`
   still routes to Walk.
4. **Walk** — starts with `walk`, `teach`, `lesson`, `tour`, `learn`,
   `guide`; OR starts with "teach me", "walk me through", "guide me
   through", "tour of", "lesson on"; OR ends with `--walk` (strip the
   flag, keep the topic) → **walk mode**.
5. **Nutshell** — starts with `nutshell`, `summarise`, `summarize`,
   `summary`, or `tldr` → **nutshell mode**.
6. **Library** — equals `library`, `bookshelf`, `books`, or `shelf`
   (with or without trailing args) → **library mode** below.
7. **Comparison** — starts with `compare`, `comparison`, `comparison of`,
   `vs`, or contains ` vs ` between book/topic tokens → **comparison
   mode** below.
8. **Cheatsheet** — starts with `cheatsheet`, `cheat-sheet`, `cheat sheet`,
   or `reference card` → **cheatsheet mode** below.
9. **Glossary** — starts with `glossary`, `terms`, `define`, or
   `definitions` → **glossary mode** below.
10. **Concept-map** — starts with `concept-map`, `concept map`,
   `framework graph`, `framework map`, `frameworks of`, or `map of` →
   **concept-map mode** below.
11. **Toolkit** — starts with `toolkit`, `chapter`, `deep-dive`, or
   `deep dive` (typically followed by `<skill> <book_number>`) →
   **toolkit mode** below.
12. **Ingest** — `$QUERY` matches any of:
    - contains a token of the form `\S+\.(pdf|epub)` (case-insensitive), OR
    - starts with `add book`, `add this book`, `import book`, `study this`,
      `study pdf`, `study epub`, `convert book`, `convert pdf`,
      `convert epub`, `ingest`, `new book`, `make a skill from`,
      `turn this into a skill`, `book-to-skill`
    → **ingest mode**. Order matters: walk triggers are checked first,
    so "walk me through ~/foo.pdf" still walks an existing skill rather
    than re-importing.
13. **Default** — **ask mode**, continue with this file.

**Walk mode hands off to `walk-mode.md` from its Step 1. Course / check /
nutshell / library / comparison / cheatsheet / glossary / concept-map /
toolkit / ingest jump to their named section below. Otherwise continue
with the ask-mode procedure.**

---

## Step 0.5 — HTML emission (applies to every mode)

Every mode below ends with the same final step: **emit an HTML
artifact** to `artifacts/` using the shared design system. The
procedure is identical regardless of mode:

1. Read `.claude/skills/the-knowledge-guy/design-system/shell.html`.
2. Open `design-system/layouts.md` and find the section matching this
   mode. Note the **path**, **title**, **EXTRA_CSS**, and **body
   template**.
3. Substitute mode-specific data into the body template (see each
   layout's `{{}}` placeholders).
4. Substitute `{{TITLE}}` + `{{EXTRA_CSS}}` + `{{BODY}}` into the
   shell.
5. Write the result to `artifacts/<subfolder>/<filename>.html` per
   the layout's path rule.
6. Regenerate `artifacts/index.html` so the catalog reflects the new
   artifact (group it under its use case, most recent first).
7. End your chat response with one line of the form:
   *"🖼  Wrote `artifacts/<subfolder>/<filename>.html` — open it for
   the rich rendering."*

**Cache rule.** Before generating, check whether the target file
already exists. For **deterministic** artifacts (nutshell, toolkit,
cheatsheet, concept-map, per-book glossary, library, **course chapter
pages**), reuse the cached file unless the user passed `--regenerate`. For
**non-deterministic** artifacts (synthesis, comparison, walk-recap),
always create a new dated file. The **course index** (`courses/<slug>/index.html`)
is cheap and reflects progress, so it is **always regenerated**. Course
chapter pages are fully self-contained: their quizzes and labs are checked
client-side in the browser; the only non-deterministic part — grading an
open-ended task — happens **in chat** via the `check` sub-mode, never in
the artifact.

**Never invent CSS.** Pull the EXTRA_CSS block from `layouts.md`
verbatim. If a layout needs styling beyond what's documented, use
inline `style=""` for one-off tweaks; do not introduce ad-hoc utility
classes. New layouts belong in `layouts.md`, not in arbitrary
artifacts.

---

## Nutshell mode (per-chapter micro-summary skim)

Used when the user wants a whole-book skim — one short block per
chapter, ~100 words each, the whole book in one scrollable response.
The artifact lives at `<skill>/nutshell.md` and is pre-generated at
ingest time by `book-to-skill` (Stage 2.5). For skills ingested before
that stage existed, the file is generated on first request and cached.

### Step N1 — Resolve the target skill

Strip the trigger verb from `$QUERY` (`nutshell`, `summarise`,
`summarize`, `summary`, or `tldr`). The remainder is `$TARGET`.

If `$TARGET` is empty:

> "Which book? Run `/the-knowledge-guy nutshell <skill-slug>` — e.g.
> `nutshell bogle-common-sense-investing`. Installed skills:
> `<list from filesystem>`."

Then stop.

Discover installed skills the same way as Step 1 below:

```bash
SKILLS_ROOT="$(pwd)/.claude/skills"
find "$SKILLS_ROOT" -maxdepth 2 -name SKILL.md
```

Exclude `the-knowledge-guy` and `book-to-skill`. For each remaining
skill, read frontmatter (`Read` with `limit: 40`) and parse `name` +
`description`.

Match `$TARGET` against each skill's slug and the book title that
appears in its description (case-insensitive substring + token overlap):

- **1 match** → use it.
- **0 matches** → tell the user, list installed skills, stop.
- **2+ matches** → use `AskUserQuestion` to disambiguate (up to 4
  options, each option's label is the slug, description is the
  one-line book title).

### Step N2 — Read the cached nutshell (fast path)

```bash
test -f "${SKILL_DIR}/nutshell.md" && cat "${SKILL_DIR}/nutshell.md" > /dev/null && echo EXISTS || echo MISSING
```

If `EXISTS`, `Read` `${SKILL_DIR}/nutshell.md` and emit it verbatim as
the chat response. Then follow **Step 0.5** to render the HTML artifact
at `artifacts/nutshells/<skill-slug>.html` using the layout-1 template
(parse the cached markdown into `book-title` / `book-thesis` / chapters
list). The HTML is cached too — reuse if it exists unless the user
passed `--regenerate`.

### Step N3 — Self-heal (slow path, first request only)

If `nutshell.md` is `MISSING` (skill was ingested before Stage 2.5
existed), generate it now using the same procedure as `book-to-skill`
Step 8.5:

1. Read `${SKILL_DIR}/chapters_manifest.json`.
2. Resolve the book-to-skill install path so you can read the template:

   ```bash
   BTS_DIR="$(find "$SKILLS_ROOT" -maxdepth 2 -type d -name book-to-skill | head -1)"
   test -f "${BTS_DIR}/reference/nutshell-template.md" || { echo "Template missing — cannot generate nutshell"; exit 1; }
   ```

3. Read the template once into memory. Read the one-line thesis from
   `${SKILL_DIR}/raw/spine.md` (the line under `## Thesis`).
4. **Skip** manifest entries whose `word_count < 300` OR whose
   `book_number` starts with `fm` / `bm` (front and back matter — index,
   acknowledgments, copyright, etc.). Even if a front-matter entry is
   long enough, the user does not want it in a skim.
5. Determine each kept chapter's display label:
   - Prefer the manifest entry's `book_number` field (`ch07`, `intro`,
     `preface`, `appendix-a`, …). This is the canonical label —
     `book-to-skill` Stage 2.5 and the backfill script both populate
     it.
   - **Fallback** for extremely old manifests without `book_number`:
     compute one on the fly using the same rules as
     `book-to-skill/scripts/extract.py:assign_book_numbers` (parses
     "Chapter 7 — …", "7. …", "Introduction", "Appendix A", etc.).
     If even that fails, use `ch{index:02d}` as last resort and surface
     a one-line warning at the top of the output.
6. Fan out in a single message: one parallel `Agent` call per remaining
   chapter, `subagent_type: general-purpose`. Each subagent prompt:

   ```
   You are generating one per-chapter nutshell block for a skill skim.

   Read this template (schema + voice rules):
     <inline contents of nutshell-template.md>

   Read this single chapter toolkit file and base your block on it
   ONLY — do not read other chapters, do not invent content:
     <SKILL_DIR>/<chapter file from manifest>

   Context for tone (the book's whole-book thesis):
     <one-line thesis>

   Output exactly one nutshell block following the template's
   "Required shape" — starts with `## <book_number> — <title>`,
   80-120 words, 3-5 bullets. No preamble, no closing remarks, no
   markdown fences.

   Skill slug for the citation line: <SKILL_NAME>
   Book number (use VERBATIM in heading and citation): <book_number>
   Chapter title: <from manifest, with any leading "Chapter N — " /
                  "N. " stripped>
   ```

7. Concatenate returned blocks in manifest order. Prepend:

   ```
   # <Book title> — in a nutshell

   > <one-line thesis from spine.md>
   ```

8. Write the result to `${SKILL_DIR}/nutshell.md` with `Write`.
9. Emit the file contents as the response. Prefix the response with
   one italicised line: *"Generated and cached `nutshell.md` for
   `<skill-slug>` (first request — future calls will be instant)."*

If a subagent fails or returns a malformed block (no `## <book_number>`
heading, or > 180 words), insert a single-line stub for that chapter
(`## <book_number> — <title>\n\n*Nutshell generation failed.*`) and
continue.

Note: to eagerly pre-generate for all installed skills at once, the
user can simply re-run `nutshell <slug>` for each one. No backfill
script is provided.

---

## Library mode (bookshelf overview)

Triggered by `library`, `bookshelf`, `books`, `shelf`.

1. Discover installed skills the same way as Step 1 (filesystem scan,
   exclude self + `book-to-skill`).
2. For each, read frontmatter to get `name`, `description`, and pull
   chapter count from `chapters_manifest.json` if present.
3. Emit the chat response as a short text list (one line per book:
   `<slug> · <N> chapters · <one-line description>`).
4. **Render `artifacts/library.html`** using the layout-10 template in
   `design-system/layouts.md`. Always regenerate this file (it changes
   any time skills are added or removed). Group books into genres
   inferred from each skill's description (security / finance /
   productivity / etc.). Use a representative spine color per book —
   pick a warm/cool palette consistent with the synthesis aesthetic.

---

## Comparison mode (one concept across multiple books)

Triggered by `compare`, `comparison`, `<topic> vs <topic>`.

1. Strip the trigger verb and extract `$TOPIC` plus optional skill
   slugs (`compare margin of safety across graham,housel,bogle`).
2. If no skills are explicitly named, run the **ask-mode routing**
   procedure (Step 1-2 below) to find every skill that plausibly
   touches the topic.
3. Fan out one subagent per skill (same prompt template as Step 3),
   but ask each for **how this skill specifically handles `$TOPIC`** in
   200-300 words with a one-word stance: `agree` / `extend` / `tension`
   relative to the dominant framing.
4. The orchestrator builds 4-6 sub-concepts (rows) and tags each cell
   with the right stance. Render as the layout-5 comparison table.
5. **Render `artifacts/comparisons/YYYY-MM-DD-<topic-slug>.html`**
   using the layout-5 template. Always create a new dated file — every
   comparison is unique.
6. Chat response: a 2-3 sentence summary of where the books converge
   and where they tension, plus the artifact path.

---

## Cheatsheet mode (operational one-pager for a book)

Triggered by `cheatsheet <book>` or `cheat-sheet <book>`.

1. Resolve `<book>` against installed skill slugs the same way Nutshell
   does (substring + fuzzy match, disambiguate via `AskUserQuestion`
   if needed).
2. Check `<skill-dir>/cheatsheet.md` — every book-to-skill output
   includes one. Read it.
3. Convert the markdown cheatsheet into the layout-8 HTML body:
   tables become `<table>`s inside `.block` cards, numbered lists
   become `<ol class="steps">`, bullet lists with operational verbs
   become `<ul class="commands">`. Group 2 columns of cards.
4. **Render `artifacts/cheatsheets/<skill-slug>.html`** using the
   layout-8 template. **Cached** — reuse if it exists unless
   `--regenerate`.
5. Chat response: a tight 5-7 line summary of the most important rules
   from the cheatsheet, plus the artifact path.

---

## Glossary mode (A-Z term lookup)

Triggered by `glossary`, `terms`, `define`, `definitions`.

- **No book argument** → cross-library mode. Walk every installed
  skill's `glossary.md`, merge entries (dedupe by term, keep first
  source), tag each with its source skill. Write to
  `artifacts/glossaries/full-library.html`.
- **Book argument** (`glossary <book>`) → per-book glossary. Read just
  that skill's `glossary.md`. Write to
  `artifacts/glossaries/<skill-slug>.html`.

Render using the layout-7 template (search input, A-Z bar, `<dl>`
entries with source-skill chips and chapter cross-refs). **Cached** —
reuse unless `--regenerate`.

Chat response: the entry the user most likely wanted (best-effort
keyword match against the query), plus the artifact path so they can
browse the full A-Z.

---

## Concept-map mode (Tier-1 framework graph for a book)

Triggered by `concept-map <book>`, `concept map <book>`,
`framework graph <book>`, `frameworks of <book>`.

1. Resolve `<book>` against installed skill slugs.
2. Read the skill's `SKILL.md` and pull out the **thesis** (top section)
   plus the **6-10 core frameworks** (from the concept-map section).
   Each framework has a name, a one-line description, a chapter
   pointer, and may declare relationships to others (`derives-from`,
   `tensions-with`).
3. Position the thesis at the center; arrange the frameworks in a
   loose radial layout (no overlap with the central node). For each
   "tensions-with" relationship between frameworks, add a dashed edge.
4. **Render `artifacts/concept-maps/<skill-slug>.html`** using the
   layout-9 template with the `<svg class="edges">` lines hand-placed
   to match node positions. **Cached** — reuse unless `--regenerate`.
5. Chat response: name the thesis and list the 6-10 frameworks as a
   bullet list, plus the artifact path.

---

## Toolkit mode (Tier-2 deep-dive on one chapter)

Triggered by `toolkit <book> <chapter>`, `chapter <book> <chapter>`,
`deep-dive <book> <chapter>`.

1. Resolve `<book>` to a skill slug.
2. Resolve `<chapter>` to a `book_number` from the skill's
   `chapters_manifest.json` (matches by book_number directly, or by
   chapter title substring).
3. Read `<skill-dir>/chapters/<book_number>-<slug>.md` (the existing
   per-chapter toolkit file produced by Stage 1 of book-to-skill).
4. Convert its sections to the layout-6 HTML body:
   - "Core Idea" → drop-cap lede.
   - "Frameworks Introduced" → one `.frame` block per framework.
   - "Encryption keys" / tables / code → `.ascii` blocks.
   - "Anti-patterns" → `.callout.warn` cards.
   - "Defender's playbook" / good practices → `.callout.good` cards.
5. **Render `artifacts/toolkits/<skill-slug>-<book_number>.html`**
   using the layout-6 template. **Cached** — reuse unless
   `--regenerate`.
6. Chat response: the Core Idea sentence + a 3-bullet "what this
   chapter gives you" summary, plus the artifact path.

---

## Course mode (interactive learn-by-doing site)

Builds an interactive website per chapter — **theory** taught from the
chapter toolkit, then a **practice** section with auto-checked quizzes,
in-browser runnable code labs, and open-ended tasks. The practice content
comes from `<skill>/practice/<book_number>-<slug>.json` (produced by
book-to-skill Stage 3). Course mode is a **renderer** — it never invents
exercises; a chapter with no practice file renders theory-only.

Triggered by `course <book>`, `lab <book> [<chapter>]`, `practice <book>`,
`hands-on <book>`, `drills <book>`, `exercises <book>`, `learn by doing …`.

### Step C1 — Resolve the target

Strip the trigger verb and any `--regenerate` / `--course` / `--lab` flag
from `$QUERY`. Resolve the first token to a skill slug the same way
Nutshell mode does (substring + fuzzy; `AskUserQuestion` to disambiguate
2+). If a second token is present, resolve it to a `book_number` against
`<skill>/chapters_manifest.json` (by `book_number` directly or chapter-title
substring) → **single-chapter** build. No second token → **whole-book**
build. Read `chapters_manifest.json` into memory.

```bash
COURSES="$(pwd)/artifacts/courses/<skill-slug>"; mkdir -p "$COURSES"
ls "$(pwd)/.claude/skills/<skill-slug>/practice" 2>/dev/null   # which chapters have practice
```

### Step C2 — Sequence the chapters (whole-book build)

Spawn **one** planner subagent (the walk-mode Step-3 pattern). It reads
**only** `<skill>/SKILL.md` (the concept-map DAG + topic index) and
`chapters_manifest.json`, then returns a prerequisite-ordered chapter list
as one line of JSON:

```json
[{"book_number":"ch01","title":"…","prereqs":[],"order":1}, …]
```

It topologically sorts the `A → builds on / requires → B` edges so
prerequisites precede dependents. **Fallbacks:** if the DAG is absent or
cyclic, use manifest `index` order. Always **skip** chapters whose
`book_number` starts with `fm`/`bm` or whose `word_count < 300` (same rule
as nutshell). For a single-chapter build, skip this step.

### Step C3 — Per chapter: cache, theory, practice

For each chapter in the sequence (or the one requested):

1. **Cache check** — if `artifacts/courses/<slug>/<book_number>.html`
   exists and `--regenerate` was not passed, reuse it; skip to the next
   chapter (do **not** re-run the teaching subagent).
2. **Practice** — read `<skill>/practice/<book_number>-<slug>.json` if it
   exists. If missing, this chapter renders theory-only with a
   `.callout.caution` ("No practice set yet — run `/book-to-skill <book>
   --regenerate` to build one.").
3. **Theory** — spawn a teaching subagent using the **walk-mode Step-6b
   teaching prompt** (depth = intermediate), pointed at
   `<skill>/SKILL.md` (orientation) + `<skill>/chapters/<book_number>-<slug>.md`
   (the source). It returns the theory section composed from existing
   components (`.def`, `.worked`, `.code-block`, `.callout`, `.capsule`,
   `.source`). Fan these out in parallel across uncached chapters (batch ~6).

   **Append this concept-visual clause to the teaching prompt** (course mode
   only — chat walks never get it):

   > *Only where it genuinely earns its place — the same bar as deciding a
   > chapter gets a runnable lab — you MAY additionally return up to ONE
   > interactive widget and/or ONE static illustration. Default to prose; never
   > illustrate a definition a sentence already nails.*
   > - **Widget**: a fenced ` ```json ` block tagged `widget` containing ONE
   >   object that validates against `design-system/widgets.md` — `type` ∈
   >   `flow | toggle-state | stepper | slider | compare`, fixed
   >   `viewBox 0 0 640 280`, coordinates in range, edges referencing real node
   >   ids, `surface:"plate"` for neutral structure or `"illus"` for anything
   >   showing ok/warn/crit state. **JSON only — do not draw SVG for a widget;
   >   the engine draws it.**
   > - **Static SVG**: a fenced ` ```html ` block tagged `illus` — an inline
   >   `<svg class="illus" viewBox="…">` or `<div class="plate">…</div>`, for a
   >   structural diagram no widget covers. Use **only** design-system classes
   >   (`il-*` / `node-*` / `edge-*` / `arrow*`) — never `fill="#…"`,
   >   `stroke="#…"`, `style` color, `<script>`, or animation.

4. **Collect + gate the visuals.** From each chapter's teaching output, take at
   most one `widget` block and one `illus` block (discard extras). Pipe each
   through the lint and **drop anything that fails** — never ship a malformed
   widget or a hardcoded-color SVG:

   ```bash
   echo "$WIDGET_JSON" | ${BTS_DIR}/.venv/bin/python ${BTS_DIR}/scripts/lint_concept_widgets.py --check-stdin
   echo "$STATIC_SVG"  | ${BTS_DIR}/.venv/bin/python ${BTS_DIR}/scripts/lint_concept_widgets.py --check-stdin
   ```

### Step C4 — Render each chapter page (layout 11)

Follow **Step 0.5** with `design-system/layouts.md` **§11 · Course chapter**:
- Compose the body: chrome → theory section → practice section + the
  `#kg-practice` mount + the `#kg-exercises` JSON island.
- **Theory visuals (if Step C3.4 kept any):** drop the static `illus`/`plate`
  SVG verbatim into a `<div id="theory-illustration">` inside the theory
  section (after the worked example). For the widget, emit an **empty**
  `<figure class="widget" data-widget-id="<widget.id>"></figure>` mount where it
  belongs in the flow, and add the widget object to a single
  `<script type="application/json" id="kg-concept-widgets">[…]</script>` island
  at the end of the body — escaped exactly like `#kg-exercises` below (replace
  `<` with `<`). The shell's widget engine hydrates the mount; you do
  **not** hand-author the SVG. Widget state is intentionally ephemeral (not
  saved). Omit the island entirely when the page has no widget.
- **Sanitize the island** (the one security-critical step): inline the
  practice file's `exercises` array, but for every exercise with
  `"family": "open"`, **remove `rubric` and `model_answer`** — they are the
  grading key and must never reach the browser. Whitelist per the
  field-visibility rule in `book-to-skill/reference/practice-template.md`.
  Also replace every `<` with the JSON unicode escape `<` in the
  island text (still valid JSON; `JSON.parse` decodes it back) so chapter
  content can never break out of the `<script>` tag with a stray
  `</script>`.
- Both the `.mastery` meter and the `#kg-practice` mount carry
  `data-scope="<skill-slug>/<book_number>"` — they must match (the engine
  keys localStorage on it).
- Write `artifacts/courses/<skill-slug>/<book_number>.html`.

The shell's lab engine renders every exercise family, checks answers
client-side, runs labs in a sandboxed iframe, and saves progress to
localStorage. You do **not** hand-author exercise cards.

### Step C5 — Render the course index (layout 12) + memory

- Render `artifacts/courses/<skill-slug>/index.html` from **§12 · Course
  index** — the syllabus in DAG order, prereq chips, and per-chapter
  progress meters (`data-total` = each chapter's exercise count; the shell
  paints them from localStorage). **Always regenerate** this file.
- Write/update the course memory file (Step CM, below).
- Regenerate `artifacts/index.html` with a new **Courses** group.

### Step C6 — Chat response

2–3 lines: book, N chapters built (+ how many were cached), the first
chapter to open, and the index path. Tell the user the open-ended tasks
have a **"Check with Claude"** button that pastes a `check …` command back
into this chat for grading.

### Step CM — Course memory (shared with walk)

Write `~/.claude/projects/-Users-vitaly-MyPlace-projects-the-knowledge-guy/memory/course-<skill-slug>.md`,
reusing the walk-memory frontmatter + `✅ / ⚠ / ▶ / ⏳` grammar (see
walk-mode.md Step 7). One `## Practice` line per chapter listing its
exercise `id`s and state. This markdown is the **durable source of truth**
the `check` sub-mode updates; the browser's localStorage is the live cache.
Add a `- [Course: <book>](course-<slug>.md) — <M> exercises, last touched <date>`
line to `MEMORY.md`.

---

## Check sub-mode (grade an open-ended practice answer)

Closes the open-task loop. A course page's **"Check with Claude"** button
copies a command of the form:

```
/the-knowledge-guy check <skill-slug> <book_number> <exercise-id>
--- my attempt ---
<the user's written answer>
```

### Step K1 — Parse

Read the skill slug, `book_number`, and `exercise-id` from the three
tokens after `check`. Everything after the `--- my attempt ---` marker is
the user's attempt (may be empty — handle gracefully).

### Step K2 — Load the rubric (server-side fields)

Read `<skill>/practice/<book_number>-<slug>.json`, find the exercise by
`id`, and take its `rubric` (criteria + weights) and `model_answer` — the
**server-side-only** fields the browser never saw. Also read
`<skill>/chapters/<book_number>-<slug>.md` for ground truth on framework
names. If the file or id is missing, say so and stop.

### Step K3 — Grade

Spawn **one** focused subagent (the ask-mode fan-out pattern, single
skill). Give it the rubric, the `model_answer`, the chapter file, and the
user's attempt. It returns: a verdict per rubric criterion (met / partial /
missed), an overall **pass / revisit**, and the single most important thing
to fix. Cite `[<skill-slug> <book_number>]` inline like every other mode.

### Step K4 — Record + respond

- Update `course-<skill-slug>.md`: flip that exercise's marker to
  `✅ graded: pass` or `⚠ graded: revisit`, and append the fumble to
  `## Notes`. Update the `Last updated:` date and the `MEMORY.md` line.
- Emit a small result artifact per Step 0.5 (reuse the **§11** layout's
  feedback components, or a compact synthesis-style card) at
  `artifacts/courses/<skill-slug>/<book_number>-check-<exercise-id>.html`,
  and refresh `artifacts/index.html`.
- Chat: the overall verdict + the one thing to fix + the citation, and a
  pointer back to the course page to continue.

---

## Ingest mode (handoff to `book-to-skill`)

Used when the user wants to add a new book to their skills mid-conversation.

### Step I1 — Extract the path

Parse `$QUERY` and find the first token matching `\S+\.(pdf|epub)`
(case-insensitive). Strip surrounding quotes. Expand `~/` to `$HOME/`.
If a second token of the form `[a-z0-9-]+` (not starting with `--`) follows the
path, treat it as the optional skill slug.

**Flags (pass-through).** Also scan `$QUERY` for any of `--complete` /
`--complete-coverage`, `--practice` / `--with-practice`, `--course`, and
`--regenerate` (book-to-skill's Step-0.6 flags). Collect the ones present into
`$FLAGS`, and exclude every `--…` token from slug matching (a flag must never
become the slug). `--course` = complete coverage **+** practice — the "make it an
interactive course" shortcut.

If no path is found, print:

> "I detected a book-ingest request, but couldn't find a `.pdf` or
> `.epub` path in your message. Run `/book-to-skill <path>` directly, or
> re-ask me with the path included."

Then stop. Do **not** call `Skill` with a guessed path.

### Step I2 — Validate the path

```bash
test -f "$PATH_VALUE" || { echo "Path not found: $PATH_VALUE"; exit 1; }
```

If the file does not exist, tell the user and stop.

### Step I3 — Mid-walk confirmation (only if a walk is in progress)

Check `$HOME/.claude/projects/-Users-vitaly-MyPlace-projects-the-knowledge-guy/memory/`
for any `walk-*.md` with `Status: in_progress`. If at least one exists,
use `AskUserQuestion` to confirm:

- "Pause the current walk and ingest this book now" (recommended)
- "Cancel — I'll resume the walk first"

If the user picks pause, update the walk memory's `Last updated:` line
to today's date (no other state change — resume logic picks back up).

### Step I4 — Hand off via the Skill tool

Call:

```
Skill(skill="book-to-skill", args="<path> [<slug>] [<flags>]")
```

Append any `$FLAGS` parsed in Step I1 (e.g. `--course`) so the ingest runs in
complete-coverage / practice mode without re-prompting those choices.

`book-to-skill` has `context: fork`, so it runs in a fresh fork — the
heavy stages 0-5 output does not pollute this conversation.

### Step I5 — Post-ingest report

When the Skill call returns, summarise the result in 2-3 lines (skill
name created, chapter count if surfaced). Then suggest a next step:

- If a walk was paused: "Run `/the-knowledge-guy resume` to continue the
  paused walk, or `/the-knowledge-guy walk <topic>` to start a walk on
  the newly added skill."
- Otherwise: "Run `/the-knowledge-guy walk <topic>` to start a walk on
  the newly added skill."

---

## Step 1 — Discover installed domain skills

Run this once to enumerate skills:

```bash
SKILLS_ROOT="$(pwd)/.claude/skills"
test -d "$SKILLS_ROOT" || { echo "No .claude/skills dir at $(pwd)"; exit 1; }
find "$SKILLS_ROOT" -maxdepth 2 -name SKILL.md
```

For each `SKILL.md` returned, use `Read` with `limit: 40` to load only the
YAML frontmatter. Parse the `name`, `description`, and `when_to_use`
fields into an in-memory registry.

**Exclude from the registry:**

- `the-knowledge-guy` itself (you are the router; do not recurse).
- `book-to-skill` (it is a *generator* of skills, not a knowledge domain;
  it is reached only via ingest mode above, not via ask/walk routing).
- Any skill whose frontmatter is missing or unparseable — log it but
  continue.

If the registry is empty after exclusions, stop and tell the user:

> "No domain skills are installed yet. Run `/book-to-skill /path/to/book.pdf`
> on a PDF or EPUB to add one, then ask me again."

---

## Step 2 — Route

Match `$QUERY` against each registered skill's combined
`description + when_to_use` text. Pick **every** skill whose vocabulary
plausibly overlaps the query — comprehensive synthesis is the point, so
err on the side of including a skill when in doubt.

Routing rules:

- **Clear single-domain query** (e.g. "how do I bypass AMSI?") → route to
  that one skill only. State the routing decision in one line before
  fanning out.
- **Multi-domain query** (e.g. "how do I find vulnerabilities in an ML
  serving stack?") → route to every plausibly relevant skill.
- **No matches** → route to **all** registered domain skills and tell the
  user no skill was an obvious fit, so you're broadcasting.
- **Meta queries** ("what skills do I have?", "list my books") → answer
  directly from the registry without fanning out.

Before Step 3, print a one-line plan:

> Routing to: `skill-a`, `skill-b` — spawning N parallel subagents.

---

## Step 3 — Fan out (single message, N parallel Agent calls)

In **one message**, emit one `Agent` tool call per matched skill. They run
in parallel; do not call them sequentially. Each subagent:

- `subagent_type`: `general-purpose`
- `description`: `Consult <skill-name>`
- `prompt`: (template below)

Prompt template for each subagent — substitute `<SKILL_NAME>`,
`<SKILL_DIR>` (absolute path), and `<QUERY>`:

```
You are a focused domain expert acting as a single book-skill consultant.

Load ONLY this skill:
  <SKILL_DIR>/SKILL.md

Read its concept map and topic index. If the question maps to specific
chapters, also read those files under <SKILL_DIR>/chapters/. Do not load
any other skill.

Answer this question using ONLY this skill's knowledge:
  <QUERY>

Rules:
- 200-400 words.
- Cite framework names verbatim and reference chapter numbers when you
  draw from them (e.g. "ch07-kerberoasting").
- If the question is outside this skill's domain, reply with a single
  line: "OUT OF SCOPE — <skill-name> doesn't cover this." Do not invent.
- Do not hedge, do not summarise the whole book — answer the question.

Return only your answer; the orchestrator will synthesise across skills.
```

If a subagent fails, note the failure but continue with the others.

---

## Step 4 — Synthesise

Collect every subagent report. Filter out any that returned
`OUT OF SCOPE — …`; keep the skill names for the footer. Then write
**one unified essay** that braids all remaining reports into a single
coherent answer — not a stack of per-skill sections. Shape:

```
## <Title that names the question's core>

<Opening paragraph — the direct answer in 3-5 sentences, already braided
 across skills with inline citations like [bogle-common-sense-investing
 ch3] or [forshaw-windows-security ch14].>

<Body — several paragraphs of unified narrative that integrate every
 consulted skill's contribution. Cite inline at the point of each claim,
 not in trailing per-skill blocks. Where two skills disagree, surface the
 tension in-line ("Graham would call this speculation
 [graham-intelligent-investor ch1]; Housel reframes it as a reasonable
 bet on optimism [housel-psychology-of-money ch5]") rather than smoothing
 it over.>

<Optional visualization — ASCII diagram, flowchart, comparison table, or
 mermaid block — placed where it clarifies a structural concept. See
 visualization rules below.>

<Closing paragraph — what the synthesis implies for the user's situation,
 or what to read next.>

---
**Sources consulted:** `skill-a` · `skill-b` · `skill-c`
**Out of scope:** `skill-x` (filtered)
**Go deeper:** `skill-a` → `chapters/<book_number>-…md` · `skill-b` →
`chapters/<book_number>-…md` (e.g. `ch07-taxes-are-costs-too.md`,
`intro-day-zero.md`, `appendix-a-common-ports.md`)
```

Length scales with the question. Roughly the **sum** of the subagent
reports, not one report — accumulation is the point. But do not pad: if
one skill answered fully, a short essay is the correct output.

### Step 5 — Emit the synthesis HTML artifact

After the chat response, follow **Step 0.5** to render the synthesis
as HTML using the layout-2 template. Path:
`artifacts/synthesis/YYYY-MM-DD-<query-slug>.html`. Always create a
new file (every ask is unique). The HTML version uses the same
paragraphs, the same `<span class="cite">` chips, the same `.pull`
quote, the same `.ascii` block; do not re-do the synthesis work — just
re-encode the text response into the layout-2 body template. End your
response with the artifact path so the user can open it.

### Visualization rules

- Add a visualization *

（文件较长，此处截取前 40000 字符）
