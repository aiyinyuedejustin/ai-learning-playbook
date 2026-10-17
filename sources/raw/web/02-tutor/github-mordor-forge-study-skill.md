# mordor-forge/study-skill

- 链接：https://github.com/mordor-forge/study-skill
- 作者：mordor-forge
- 仓库说明：Claude Code skill for interactive learning with FSRS-6 spaced repetition, research agents, book catalog, ADHD-aware sessions, and domain-specific visualization
- 星数：47
- 获取方式：GitHub README + SKILL/说明文件

---

## README

# study

> **Lamplight v2 is in development** on the [`v2`](https://github.com/mordor-forge/study-skill/tree/v2) branch. See the [design doc](https://github.com/mordor-forge/study-skill/blob/v2/docs/design/lamplight-v2.md) and the [tracking issue](https://github.com/mordor-forge/study-skill/issues/37).
> `main` stays v1 until v2.0 ships. v1 is also preserved at the [`v1.0.0`](https://github.com/mordor-forge/study-skill/tree/v1.0.0) tag.

An Agent Skills-compatible study tutor for structured, interactive learning with spaced repetition.

The active agent teaches concepts through notes and guides you through exercises you implement yourself, with FSRS-based review scheduling, optional research integrations, PDF source material support, and restart-safe session state.

## Quick Start

1. Install the full skill folder for your agent:

   Claude Code:
   ```bash
   mkdir -p ~/.claude/skills
   cp -R study/ ~/.claude/skills/study/
   ```

   Codex:
   ```bash
   mkdir -p ~/.agents/skills
   cp -R study/ ~/.agents/skills/study/
   ```

   Hermes:
   ```bash
   mkdir -p ~/.hermes/skills
   cp -R study/ ~/.hermes/skills/study/
   ```

2. Build the FSRS scheduler:
   ```bash
   cd <installed-study-skill>/scripts/fsrs
   go build -o fsrs ./cmd/fsrs/
   ```

3. Start learning:
   ```text
   /study init "Go concurrency"
   /study start
   ```

   In Codex, explicitly mention the skill if needed:
   ```text
   $study study init "Go concurrency"
   ```

## Prerequisites

### Required

- **An Agent Skills-compatible client** such as Claude Code, Codex, Hermes, Cline, or OpenCode
- **Go 1.22+** — to build the FSRS spaced repetition binary
- **Python 3.11+** and **uv** — for the book catalog builder (only needed if you use `study catalog`)

### Recommended

These enhance the experience but aren't required:

| Plugin/Skill | What it enables | Install |
|---|---|---|
| [SciAgent-Skills](https://github.com/jaechang-hits/SciAgent-Skills) | Curated bioinformatics and life science skills — domain-aware lessons, parameter tables, troubleshooting, exercise verification for scientific topics | Install from that project's current agent-specific instructions |
| context7 | Live framework/library documentation in lessons | Install through your agent's MCP/plugin mechanism |
| Playwright | Browser preview for visual diagrams | Install through your agent's MCP/plugin mechanism |
| [visual-explainer](https://github.com/nicobailon/visual-explainer) | Self-contained HTML diagrams and visualizations for lesson content | Install from that project's current agent-specific instructions |

### Optional

| Plugin/MCP | What it enables |
|---|---|
| LSP plugins (gopls, pyright, etc.) | Real-time code validation during exercise review |
| calibre or pandoc | Ebook format conversion (epub/mobi → PDF for ingestion) |

#### NotebookLM is no longer supported

Earlier versions of this README recommended a community NotebookLM MCP server for source
material. That path is unsupported now, and Lamplight v2 removes it
([ADR-0011](https://github.com/mordor-forge/study-skill/blob/v2/docs/adr/0011-lamplight-does-not-use-notebooklm.md)).

NotebookLM has no official API for personal Google accounts. The community server reaches it
through undocumented endpoints, signed in with your browser's Google session cookies. That is
unofficial access, which Google neither documents nor supports, and it may not be allowed by
Google's terms. If it goes wrong, the account at risk is yours, so this project no longer
recommends installing it.

v1 still uses a NotebookLM MCP server when it finds one in your agent. To keep v1 away from
it, remove the server from your agent's configuration. If you installed the tool only for
this skill, uninstall it too (`uv tool uninstall notebooklm-mcp-cli`) and delete the Google
sign-in it saved, as that project's documentation describes. Without the server, v1 falls
back to searching extracted text, as [Source Material](#source-material) describes.

## Graceful Degradation

The skill adapts to what's available. Nothing crashes if a plugin is missing:

| Feature | With plugin | Without plugin |
|---|---|---|
| Scientific domains | Curated workflows, parameter tables, troubleshooting via SciAgent-Skills | Falls through to web search |
| Lesson research | Live docs via context7 | Model's built-in knowledge |
| Source material | Semantic search via a NotebookLM MCP server ([unsupported](#notebooklm-is-no-longer-supported)) | Grep over extracted text, or skipped |
| Concept diagrams | HTML via visual-explainer | ASCII diagrams in lesson notes |
| Code validation | LSP real-time checking | User runs tests manually |
| Book catalog | Fuzzy search across library | Manual `--source` path |

## Commands

```
study init <topic> [--template=<name>] [--source <path>]
    Initialize a study workspace for a topic.
    Auto-detects language template from topic.

study start
    Start or resume a learning session.
    Checks energy, presents due reviews, enters lesson loop.

study status
    Show progress, difficulty level, review queue.

study review
    Standalone review session for all due FSRS items.

study add-source <path>
    Add a PDF/ebook as source material.

study catalog build <library-path>
    Index a directory of books for topic matching.

study catalog search <query>
    Search the catalog for books matching a topic.

study break
    Save session state and exit cleanly.
```

## Agent Support

The skill is intentionally portable: `SKILL.md` contains the workflow, `references/`
contains deeper protocols, `templates/` contains workspace scaffolds, and `scripts/`
contains deterministic support tools.

| Client | Install/use |
|---|---|
| Claude Code | Copy to `~/.claude/skills/study`; use `/study ...` if exposed as a command |
| Codex CLI/IDE/App | Copy to `.agents/skills/study` or `~/.agents/skills/study`; invoke with `$study` or rely on implicit skill matching |
| Hermes Agent | Copy to `~/.hermes/skills/study`; run from the study workspace and resume via Hermes session flags plus `.study-config.json` |
| Cline | Copy to `.cline/skills/study` or `~/.cline/skills/study` |
| OpenCode | Use built-in Agent Skills support when available; older setups may use `opencode-agent-skills` |

For details, read `references/agent-adapters.md`.

## Stop And Resume

Stop/resume is workspace-driven, not agent-memory-driven. The authoritative state
lives in `.study-config.json`, `lessons/`, `practice/`, `notes/`, and
`.fsrs/cards.json`. Any agent can resume a workspace by reading
`references/workspace-lifecycle.md`, then following `session_state.phase`,
`pending_action`, and `context`.

This is especially important for Hermes and other agents with their own memory or
session resume systems: those systems help recover chat context, but the study
workspace remains the source of truth.

## Usage

Use the skill after installation:

```text
/study init "Quantum Mechanics"
/study start
/study status
/study review
```

For catalog-backed source discovery:

```bash
cd <installed-study-skill>/scripts/catalog
uv sync
uv run study-catalog build /path/to/books --output ~/.config/study/book-catalog.json
uv run study-catalog search "quantum mechanics"
```

## Learning Approaches

Choose at init:

- **Concept** (default) — focused lessons with standalone exercises
- **Project** — build toward a working end product, lesson by lesson
- **Challenge** — progressive difficulty, minimal notes, maximum practice

## Book Catalog

If you have a collection of PDF books or ebooks, build the catalog before
`study init` if you want automatic book suggestions. The skill looks for the
default catalog at:

```text
~/.config/study/book-catalog.json
```

Build it once, then rebuild whenever your library changes:

```bash
# Build the catalog (one-time)
cd <installed-study-skill>/scripts/catalog
uv sync
uv run study-catalog build /path/to/your/books/ --output ~/.config/study/book-catalog.json

# The skill auto-suggests relevant books when you init a workspace
/study init "Quantum Mechanics"
# → "Found 3 matching books in your library. Add as source?"
```

For a local library, replace the source path with the directory that contains
your books:

```bash
cd <installed-study-skill>/scripts/catalog
uv sync
uv run study-catalog build /path/to/your/books --output ~/.config/study/book-catalog.json
```

## Source Material

Add a textbook as source material and the skill queries it during lessons:

```
/study init "Operating Systems" --source ~/Books/tanenbaum-os.pdf
```

The skill extracts the text, saves it as searchable markdown files under `sources/`, and
searches those during lessons.

A NotebookLM MCP server, when one is installed in your agent, is used instead in v1. That
path is unsupported: see [NotebookLM is no longer supported](#notebooklm-is-no-longer-supported).

## SciAgent-Skills Integration

When the [SciAgent-Skills](https://github.com/jaechang-hits/SciAgent-Skills) plugin is installed (built by [Jaechang Hits](https://github.com/jaechang-hits)), the study skill becomes domain-aware across bioinformatics, cheminformatics, biostatistics, proteomics, drug discovery, scientific computing, and more.

**What it enables:**

- **Automatic domain detection** — `study init "scRNA-seq analysis"` detects the genomics domain and attaches the `scanpy-scrna-seq` skill. Multi-tool pipelines (e.g., STAR → featureCounts → DESeq2) attach multiple skills in execution order.
- **Curated lesson content** — lessons are enriched with validated workflows, key parameter tables, and common recipes from the matched skill instead of relying on generic web search.
- **Parameter-based difficulty scaling** — beginner exercises use default parameters, intermediate exercises require tuning, advanced exercises demand justification, and expert exercises give datasets where defaults deliberately fail.
- **Exercise verification** — during review, the skill cross-references your implementation against sciagent's Common Recipes as a private structural check (never shown to you).
- **Troubleshooting as hints** — when stuck, the skill checks the matched sciagent skill's troubleshooting table before spawning a research agent.

Install SciAgent-Skills from its current instructions. For Claude Code, the
plugin commands are:

```bash
/plugin marketplace add jaechang-hits/SciAgent-Skills
/plugin install sciagent-skills
```

The skill works without SciAgent-Skills installed — scientific topics fall back to web search.

## Spaced Repetition (FSRS)

Completed lessons become review cards tracked by the [FSRS-6 algorithm](https://github.com/open-spaced-repetition/free-spaced-repetition-scheduler). The system uses a hybrid review model:

- **Integrated** — due items surface automatically as a warm-up at session start (max 3, capped at 5 min)
- **Standalone** — `study review` for dedicated review sessions

No streak counters, no guilt for missed reviews. The algorithm silently reschedules.

## Difficulty Adaptation

The skill tracks exercise performance (hints requested, review rounds, recall ratings) and adjusts lesson depth across four levels:

```
beginner → intermediate → advanced → expert
```

Adjustments are automatic with periodic calibration checks where you can override.

## Templates

| Template | Use case |
|---|---|
| `go-idiomatic` | Learning Go — cmd/, internal/, Makefile |
| `go-flat` | Using Go for physics/math — flat main.go |
| `python` | Python topics or Python as tool |
| `typescript` | TypeScript/JS topics |
| `rust` | Rust or systems programming |
| `c` | C or low-level programming |
| `plain` | Non-code topics (theory, math, science) |

Custom templates: create at `~/.config/study/templates/<name>/`.

## ADHD-Aware Design

- **Energy gating** — asks battery level before suggesting tasks
- **Capped review warm-ups** — max 3 items, no marathon review sessions
- **Detailed break state** — captures exactly where you stopped for seamless resumption
- **No guilt mechanisms** — no streaks, no "you missed N days", no judgment
- **Time budget awareness** — optional session length, paces lessons accordingly

## Project Structure

```
study/
├── README.md
├── SKILL.md                    # Core orchestrator (~345 lines)
├── references/
│   ├── fsrs-spaced-repetition.md
│   ├── research-agents.md
│   ├── difficulty-adaptation.md
│   ├── template-resolution.md
│   └── visual-libraries.md
├── templates/
│   ├── go-idiomatic/
│   ├── go-flat/
│   ├── python/
│   ├── typescript/
│   ├── rust/
│   ├── c/
│   └── plain/
└── scripts/
    ├── fsrs/                   # Go — FSRS-6 scheduler
    └── catalog/                # Python — book catalog builder
```

## Development

Run checks from the repository root:

```bash
make setup
make test
make lint
make typecheck
make coverage
```

The Python catalog is a nested uv project with its lockfile at
`scripts/catalog/uv.lock`. The Go FSRS scheduler is a nested Go module at
`scripts/fsrs`.

The deterministic lifecycle smoke test creates a temporary study workspace,
writes a lesson, adds an FSRS card, records a break state, and verifies another
agent could resume from `.study-config.json`:

```bash
scripts/e2e/study-lifecycle-smoke.sh
```

## License

MIT


## 文件 AGENTS.md

# Agent Guide

## Project Overview

This repository contains the `study` Agent Skills-compatible tutor. It defines an
interactive learning workflow in `SKILL.md`, reusable reference instructions in
`references/`, starter workspaces in `templates/`, a Go FSRS scheduler in
`scripts/fsrs`, and a Python book catalog tool in `scripts/catalog`.

## Development Commands

Use the root `Makefile` as the stable entrypoint:

```bash
make setup        # install Python catalog dev dependencies
make test         # run Python catalog and Go FSRS tests
make lint         # run ruff and gofmt verification
make typecheck    # run Python type checks
make coverage     # run tests with coverage output
make build        # build scripts/fsrs/fsrs
```

Single-file or narrow checks:

```bash
cd scripts/catalog && uv run ruff check src/catalog/scanner.py
cd scripts/catalog && uv run pyright src/catalog/scanner.py
cd scripts/catalog && uv run pytest tests/test_scanner.py
cd scripts/fsrs && go test ./internal
cd scripts/fsrs && go test ./cmd/fsrs -run TestCLIAddCard
```

## Code Conventions

- Keep skill behavior in Markdown instructions unless executable code is needed.
- Keep generated study workspaces independent from the installed skill directory.
- Python catalog code targets Python 3.11+, uses Pydantic models, and is linted by
  Ruff.
- Go FSRS code targets Go 1.22+ and should remain deterministic and JSON-oriented.
- Add focused regression tests for scanner, converter, matcher, CLI, and scheduler
  changes.
- Prefer typed public function signatures in `scripts/catalog/src`.
- Use conventional commit prefixes such as `fix:`, `feat:`, `docs:`, `test:`,
  and `ci:`.
- Do not commit generated binaries, local study workspaces, or agent assessment
  reports.

## Important Paths

- `SKILL.md`: command orchestration and user-facing study workflow.
- `references/fsrs-spaced-repetition.md`: FSRS invocation and review protocol.
- `references/agent-adapters.md`: Claude Code, Codex, Hermes, Cline, OpenCode,
  and generic client setup.
- `references/workspace-lifecycle.md`: init/start/break/resume state contract.
- `scripts/fsrs`: Go scheduler, store, and CLI.
- `scripts/catalog`: Python catalog scanner, matcher, converter, and CLI.
- `templates`: files copied into newly initialized study workspaces.

## Patterns

- Scanner changes: update `scripts/catalog/src/catalog/scanner.py` and add
  focused cases in `scripts/catalog/tests/test_scanner.py`.
- Catalog CLI changes: exercise `main()` through argv in
  `scripts/catalog/tests/test_cli.py`.
- FSRS changes: keep CLI behavior JSON-compatible and add Go tests under
  `scripts/fsrs/internal` or `scripts/fsrs/cmd/fsrs`.
- Skill workflow changes: update `SKILL.md` and any deeper protocol file under
  `references/` together.


## 文件 CLAUDE.md

@AGENTS.md


## 文件 SKILL.md

---
name: study
description: "Interactive learning tutor with spaced repetition, research helpers, and restart-safe study workspaces. Use when the user wants to learn something new: teach me, I want to study, help me learn, study X, create a course on, tutorial for, walk me through learning. Also use for commands like study init, study start, study status, study review, study break, and book catalog setup/search. Works across Claude Code, Codex, Hermes, Cline, OpenCode, and other Agent Skills-compatible clients for programming, math, physics, science, engineering, and other structured learning."
---

# Study Workspace - Interactive Tutor

A structured learning environment where **you write the code**, and the agent teaches, guides, and supervises. Every lesson has notes and exercises you implement yourself, with spaced repetition for long-term retention.

## Philosophy

- **You do the work** - The agent teaches and supervises, you implement
- **Structured lessons** - each lesson = notes + exercise + review
- **Spaced repetition** - FSRS algorithm resurfaces concepts before you forget
- **Research-backed content** - lessons enriched by live docs, notebooks, web research, and sciagent-skills domain expertise
- **ADHD-aware** - energy gating, capped reviews, no guilt, detailed break state
- **Git-tracked progress** - all attempts saved, safe to experiment

## Agent Compatibility

This skill follows the open Agent Skills folder shape: `SKILL.md` plus optional
`references/`, `templates/`, and `scripts/`. The durable behavior is the study
workspace contract, not any single agent client's slash-command implementation.

Before running a workflow in a new client, read:
- `references/agent-adapters.md` for Claude Code, Codex, Hermes, Cline, OpenCode,
  and generic agent setup.
- `references/workspace-lifecycle.md` for the init/start/break/resume state
  contract shared by all agents.

## Commands

### `study init <topic> [--template=<name>] [--source <path>]`

Initialize a new study workspace.

**Steps:**

0. Read `references/workspace-lifecycle.md` for the shared workspace contract.
1. Sanitize topic to directory name, create workspace, `git init`
2. **Template resolution** — read `references/template-resolution.md`:
   - Auto-detect language from topic → select template + mode (code-as-subject or code-as-tool)
   - Detect scientific domain → attach matching sciagent-skills if plugin is installed
   - Copy template files, create `lessons/`, `practice/`, `notes/`, `.fsrs/`
3. **Ask learning approach**:
   ```
   How would you like to learn?
   1. Project-based — build something real, lesson by lesson (I'll ask what you want to build)
   2. Concept-based — focused lessons with standalone exercises (default)
   3. Challenge-based — progressive difficulty, minimal hand-holding
   ```
   If **project**: ask what to build → store as `end_goal`, create `lessons/plan.md` outline
   If **project** and `sciagent_skills` are attached: use the primary skill's Workflow steps as a lesson plan backbone. Each workflow step maps to a lesson — read `references/research-agents.md` for how to extract skill content.
   - In clients without a dedicated question UI, ask in plain text and wait for
     the user's answer. Do not silently choose the default unless the user asked
     for non-interactive setup.
4. **Source material** — if `--source` provided:
   - Read `references/research-agents.md` for backend selection
   - NotebookLM available → create notebook, add PDF as source
   - Fallback → extract text via pdfplumber, save to `sources/`
   - Store source info in config
5. **Book catalog** — if `~/.config/study/book-catalog.json` exists:
   - Search catalog for topic matches
   - Show the top relevant books with title, format, and path
   - Ask: "Add any of these as source material? Reply with numbers, paths, or skip."
   - Wait for the user's answer. Do not skip this prompt unless there are no
     matches or the user asked for non-interactive setup.
6. Create `.study-config.json` (see Config Schema below), commit, show welcome

### `study start`

Start or resume a learning session.

**Resumption — always check first:**

Read `references/workspace-lifecycle.md` before mutating `.study-config.json`.

1. Read `.study-config.json`
2. If `session_state.phase` is NOT `idle`:
   - Resumed session. Read current lesson file.
   - Tell user: "Resuming — you were [doing X] on Lesson N: [title]"
   - Check `session_state.energy`: "You were at [half] battery. How are you feeling now?"
   - Pick up from saved phase
3. If `idle`: fresh session, increment `session_count`

**Fresh session flow:**

1. **Energy check**: "Before we start — full battery, half, or fumes?"
2. **Energy gating**:
   - Full → new lesson + review warm-up
   - Half → continue existing exercise or review only
   - Fumes → review only (lightweight) or suggest coming back later
3. **Optional time budget**: "How long do you have? (or skip for open-ended)"
4. **FSRS review warm-up** — read `references/fsrs-spaced-repetition.md`:
   - Resolve `<skill-dir>` to the directory containing this `SKILL.md`
   - Run: `FSRS_STORE=.fsrs/cards.json <skill-dir>/scripts/fsrs/fsrs schedule`
   - If items due: present max 3 as recall exercises (cap at 5 minutes)
   - If nothing due: skip to lesson
5. **Main lesson loop** (see below)

**Main Loop:**

```
LOOP:
  1. Agent's Turn: Teach
     - Create lesson notes (with proactive research — read references/research-agents.md)
     - Assign exercise
     - Commit notes: [agent] lesson N: topic
     - Update session_state.phase = "teaching"

  2. User's Turn: Implement
     - User works in practice/lesson-NN/
     - User can ask questions, request hints, or say "done"
     - Update session_state.phase = "practicing"

  3. Review & Feedback
     - Check git diff to see user's work
     - If sciagent skill attached: read references/difficulty-adaptation.md for verification protocol
     - Provide specific feedback (quote their code, explain why)
     - Track metrics: review_rounds, hints_requested
     - Update session_state.phase = "reviewing"

  4. Completion
     - When exercise passes review:
       - Add FSRS card: FSRS_STORE=.fsrs/cards.json <skill-dir>/scripts/fsrs/fsrs add "lesson-NN" "topic" N
       - Update lesson status to "completed"
       - Check difficulty adaptation (read references/difficulty-adaptation.md)
       - Ask: next lesson, review, or break?

  REPEAT
```

### `study status`

Show progress overview. Read `.study-config.json` and use
`references/workspace-lifecycle.md` to interpret `session_state`. If
visual-explainer is available, generate an HTML dashboard. Otherwise text:

```
Study: [topic] ([approach])
Difficulty: [level]
Progress: [N] lessons completed, [M] in review queue

Lessons:
  1. [title] ✓
  2. [title] ✓
  3. [title] ← current
  4. [title] (planned)

Review: [N] items due | Next review: [date]
Sources: [N] books attached
```

### `study review`

Standalone review session. Read `references/fsrs-spaced-repetition.md` for the full protocol. No lesson, just recall exercises for all due items.

### `study add-source <path>`

Add a PDF/ebook to the current workspace. Read `references/research-agents.md` for backend selection and ingestion.

### `study catalog build <library-path>`

Build book catalog:
```bash
cd <skill-dir>/scripts/catalog && uv run study-catalog build <library-path>
```

### `study catalog search <query>`

Search the catalog:
```bash
cd <skill-dir>/scripts/catalog && uv run study-catalog search "<query>"
```

### `study break`

Save session state and exit cleanly:
Read `references/workspace-lifecycle.md` first.
1. Commit any uncommitted changes
2. Update `.study-config.json`:
   - `session_state.phase` = current phase (NOT `idle` — that loses context)
   - `session_state.pending_action` = specific next step
   - `session_state.context` = brief note about where things stand
   - `session_state.energy` = current energy level
3. Write session summary to `notes/session-YYYY-MM-DD.md`
4. Commit: `[session] end session N`

## Lesson Structure

Each lesson file in `lessons/NN-topic.md`:

```markdown
# Lesson N: Topic

## Concept
[Clear explanation — enriched by research agent findings]

## Key Points
- Point 1
- Point 2

## Reference Example (Don't Copy!)
[Small example illustrating the concept, if helpful]

## Common Pitfalls
- Pitfall and how to avoid it

## Exercise

### What to Build
[Clear description]

### Requirements
1. Requirement 1
2. Requirement 2

### Success Criteria
- [ ] Criterion 1
- [ ] Criterion 2

### Where to Work
Create your implementation in: `practice/lesson-NN/`
```

## Teaching Rules

1. **NEVER write implementation code for the user.** Small reference examples in notes (2-5 lines) are OK. Exercises must be implemented by the user entirely.
2. **Guide, don't solve.** Hints not answers. Point to concepts, not code. Ask questions to guide thinking.
3. **Feedback is specific.** Quote their code. Explain why something is wrong/good. Suggest approach, not exact fix.
4. **Encourage experimentation.** Breaking things is learning. Git keeps everything safe.

## User Interaction

**After presenting a new lesson:**
```
What would you like to do?
1. Read the lesson and start the exercise
2. I have questions about the concept first
3. Take a break
```

**After providing feedback:**
```
What's next?
1. I'll revise my implementation
2. Questions about the feedback
3. I think it's done — final review?
4. Move to next lesson
5. Take a break
```

**When user is stuck:**
- Ask what specifically is confusing
- Provide hints, not solutions
- Spawn on-demand research agent if needed (read `references/research-agents.md`)
- Point to relevant section of lesson notes or source material

## Visual Enrichment

When teaching concepts that benefit from visual representation, read `references/visual-libraries.md` to select the right rendering approach:

- **Equations** → KaTeX (web-native, CDN)
- **Function plots, phase portraits** → JSXGraph (web-native, CDN)
- **3D surfaces** → Plotly.js (web-native, CDN)
- **Physics simulations** → p5.js + Matter.js (web-native, CDN)
- **Circuit diagrams** → SchemDraw (Python SVG generation)
- **Molecular structures** → Kekule.js (web-native) or RDKit (SVG generation)
- **Star charts** → Starplot (Python SVG generation)
- **Music notation** → LilyPond (CLI SVG generation)

If subagents or background tasks are available, ask visual-explainer with the
library choice in the prompt:

```
Agent(subagent_type="general-purpose", prompt="
  Using the visual-explainer skill, create an HTML page showing [concept].
  Use KaTeX for equations and JSXGraph for the function plot.
  Save to practice/lesson-NN/diagrams/
")
```

For SVG generation (circuits, molecules, etc.), generate a Python script, run it via Bash, and embed the SVG in the HTML.

For scientific topics with sciagent-skills attached, the plugin's visualization skills (`matplotlib-scientific-plotting`, `plotly-interactive-visualization`, `seaborn-statistical-visualization`) provide domain-appropriate plotting patterns (volcano plots, UMAP embeddings, heatmaps, survival curves). Pass the relevant sciagent visualization skill name to the visual-explainer agent for domain-specific output.

If visual-explainer is unavailable, use ASCII diagrams in the lesson notes. Visuals are enrichment, never a dependency.

## Config Schema (v3)

`.study-config.json`:

```json
{
  "version": 3,
  "topic": "Go Concurrency",
  "template": "go-idiomatic",
  "template_mode": "code-as-subject",
  "approach": "concept",
  "end_goal": null,
  "difficulty": "beginner",
  "difficulty_override": null,
  "next_calibration_at_lesson": 4,
  "mode": "tutorial",
  "created": "2026-04-04T10:00:00Z",
  "sciagent_skills": [],
  "sciagent_primary": null,
  "progress": {
    "current_lesson": 0,
    "lessons_completed": 0,
    "session_count": 0,
    "last_session": null
  },
  "lessons": [],
  "session_state": {
    "phase": "idle",
    "pending_action": null,
    "context": null,
    "energy": null,
    "time_budget_minutes": null
  },
  "sources": [],
  "review": {
    "fsrs_data_path": ".fsrs/cards.json",
    "items_due": 0,
    "last_review": null
  },
  "catalog_path": "~/.config/study/book-catalog.json"
}
```

## Git Conventions

- `[agent]` - lesson notes, feedback, guidance written by the active agent
- `[user]` - user's implementation work
- `[session]` - session start/end markers

Always commit before switching turns between the agent and user. This keeps the
git history clean and makes `git diff HEAD` reliable for reviewing user work.

## Workspace Layout

```
workspace/
├── .study-config.json
├── .fsrs/cards.json
├── lessons/
│   ├── plan.md              (project approach only)
│   ├── 01-intro.md
│   └── 02-next-topic.md
├── practice/
│   ├── lesson-01/
│   └── lesson-02/
├── notes/
│   ├── feedback-2026-04-04.md
│   └── session-2026-04-04.md
├── sources/                  (chunked text from PDFs, if no NLM)
└── [template files]          (go.mod, Makefile, etc.)
```

## Learning Approaches

- **concept** (default) — focused lessons with standalone exercises, no overarching project
- **project** — build toward a working end product; each lesson advances the build
- **challenge** — progressive difficulty, minimal notes, maximum practice

Store in `.study-config.json` → `approach`. Shapes how exercises are generated.

## Modes

Per-session modes that can change within an approach:

- **tutorial** (default) — structured lessons with concepts + exercises
- **practice** — work on exercises without new concepts
- **exploration** — user-driven, the agent assists and answers questions
- **review** — revisit previous lessons via FSRS, fill gaps

