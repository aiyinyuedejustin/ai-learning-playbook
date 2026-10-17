# DieselZhang/repo-mastery

- 链接：https://github.com/DieselZhang/repo-mastery
- 作者：DieselZhang
- 仓库说明：Turn any open-source repository into a developer-focused mastery course.
- 星数：2
- 获取方式：GitHub README + SKILL/说明文件

---

## README

<div align="center">

# 📚 Repo-Mastery

**Turn any open-source repository into a developer-focused mastery course.**

Learn a project's **usage → architecture → key implementations** the way you'd learn a real course — with confirmed course maps, deterministic mastery gates, spaced repetition, and dual-format (Markdown + HTML) course output.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-skill-0A84FF.svg)](#)
![Version](https://img.shields.io/badge/version-3.2.0-blue.svg)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)

[简体中文](./README.zh-CN.md) · [Documentation](./docs/ARCHITECTURE.md) · [Contributing](./CONTRIBUTING.md)

</div>

<p align="center">
  <img src="assets/repo-mastery-flow.png" alt="Repo-Mastery workflow: input repo → P0 assess → P1 course map → P2 mission & confirm → P3 interactive mastery learning → complete course" width="92%">
</p>

---

## Table of Contents

- [What is Repo-Mastery?](#what-is-repo-mastery)
- [Why](#why)
- [Features](#features)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)
- [Commands](#commands)
- [Data Model](#data-model)
- [Project Structure](#project-structure)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## What is Repo-Mastery?

Repo-Mastery is an **Agent skill** that converts any open-source repository into a structured, developer-focused mastery course. Given a local repo path or a GitHub URL, it:

1. **Pre-scans** the codebase objectively and proposes a **course map** (modules + knowledge points).
2. Has **you confirm and customize** the map — aligned with your Mission (why you want to master this repo).
3. Drives **interactive mastery learning** — diagnose → explain → Feynman check → practice → error diagnosis → spaced review.
4. Persists progress, notes, and **learning records** for cross-session continuity.
5. Synthesizes a **complete course document** in Markdown and HTML (shareable).

It is the "learn the codebase deeply" counterpart to `docs-to-course` (which teaches end-users how to *use* a tool from its docs). Repo-Mastery teaches developers how a project is *built*.

## Why

As a developer, reading an open-source project's code rarely equals "mastering" it. Repo-Mastery closes that gap with a judgeable learning mechanism:

- Every knowledge point has a **deterministic mastery gate** — not the LLM's impression.
- **Spaced repetition** fights forgetting; **learning records** capture how your understanding evolves.
- Notes and progress **persist across sessions**, so you resume exactly where you left off.

## Features

- 🗺️ **Evidence-based course maps** — every module/knowledge point points to real files, directories, and call chains.
- 🧭 **Mission-driven** — grounded in *why* you want to master the repo, not generic coverage.
- ⚖️ **Dual mastery gates** — quantitative (recency-weighted accuracy ≥ 0.9) for usage/procedure; qualitative (Feynman recital) for concepts/architecture.
- ⏳ **Spaced repetition** — per-type interval schedules with error-priority escalation.
- 🔧 **Hands-on verification** — commands run with your approval; a procedure point only counts as mastered with real evidence.
- 📝 **Persistent notes + ADR-style learning records** — auto-accumulated and user-appended; records track understanding evolution with supersession.
- 🌍 **Adaptive ingest** — small/medium repos read directly; large repos get a lightweight Python index (`code-map.json`).
- 📦 **Dual-format output** — full Markdown course (`COVERAGE.md`) + shareable interactive HTML course.
- 🌐 **Bilingual** — teaching language follows your input; code and identifiers stay original.
- 🧰 **Multi-CLI** — the same skill runs natively on **Claude Code, OpenAI Codex, Gemini CLI**, and AGENTS.md-based tools. The deterministic gate is real code (`scripts/learning_engine.py`) shared by every tool, so mastery math never drifts.

## How It Works

```
Phase 0  Complexity assessment  →  decide ingest (pure read / Python index)
Phase 1  Objective pre-scan     →  course-map candidates
Phase 2  Mission + map confirm  →  you approve/customize (mandatory)
Phase 3  Interactive mastery learning (diagnose → explain → Feynman → practice → error-diagnosis → spaced review)
Phase 4  Synthesize COVERAGE.md + optional shareable HTML course
```

Core design axiom: **intelligence at the exit, advancement at the gate** — the tutor decides what to teach, but whether the learner may advance is always a deterministic engine decision.

## Installation

The repo itself **is** the skill, following the open **Agent Skills** standard
(agentskills.io) — the same `SKILL.md` runs natively on Claude Code, OpenAI
Codex, and Gemini CLI. **Five ways to install, pick one:**

### 1. npm — one command

```bash
npx @dieselzhang/repo-mastery install            # any tool, from anywhere
# or install the CLI globally:
npm i -g @dieselzhang/repo-mastery && repo-mastery install
# options: repo-mastery install --only codex / --skip gemini / --dry-run
```

### 2. curl — one line, no npm needed

```bash
curl -fsSL https://raw.githubusercontent.com/DieselZhang/repo-mastery/main/scripts/install.sh | bash
```

Installs to Claude Code + Codex + Gemini. Add `--only codex` (etc.) after the pipe.

### 3. Claude Code — native plugin install

```bash
claude plugin marketplace add DieselZhang/repo-mastery
claude plugin install repo-mastery@repo-mastery
```

(In-session equivalents: `/plugin marketplace add …` then `/plugin install …`.)

### 4. Conversation-driven — tell the CLI to install it

| Tool | Say this |
|---|---|
| **Claude Code** | "Install the repo-mastery skill from github:DieselZhang/repo-mastery into ~/.claude/skills" (Claude clones + places it), or use the `/plugin` route above |
| **OpenAI Codex** | In Codex, use its built-in installer: `$skill-installer install https://github.com/DieselZhang/repo-mastery` |
| **Gemini CLI** | "Clone the repo-mastery skill from github:DieselZhang/repo-mastery into your skills directory" |

### 5. Manual — clone

```bash
git clone https://github.com/DieselZhang/repo-mastery ~/.claude/skills/repo-mastery
cd repo-mastery && ./scripts/install.sh    # from the checkout, install to other tools too
```

### Where each tool looks

| Tool | Skill directory | Entry point |
|---|---|---|
| **Claude Code** | `~/.claude/skills/` | `SKILL.md` — `/repo-mastery start <repo>` |
| **OpenAI Codex** | `~/.codex/skills/` (or `~/.agents/skills/`) | `SKILL.md` + `agents/openai.yaml` |
| **Gemini CLI** | its skills dir (`GEMINI_SKILLS_DIR` overridable) | `activate_skill` / `GEMINI.md` |
| **opencode / Cursor** (AGENTS.md tools) | project dir | `cp AGENTS.md <project>/AGENTS.md` |

> **Codex note**: Codex reads only its own directories — it does not read
> `~/.claude/`. Install to `~/.codex/skills/` so it is discovered. Restart the
> CLI after installing.
>
> **Plugin note**: installing as a plugin caches the skill in
> `~/.claude/plugins/cache/` and invokes it namespaced (`/repo-mastery:repo-mastery`).

**Requirements**

- A target repository: a local path or a reachable `github:owner/repo` (the skill auto-runs `git clone --depth 1`).
- Python 3.8+ — needed by the deterministic engine (`scripts/learning_engine.py`) and the large-repo index (`scripts/index_repo.py`), both pure stdlib.

## Usage

```bash
/repo-mastery start <local-path | github:owner/repo> [--language zh|en] [--fresh]
```

Example — learn a project from a GitHub URL:

```bash
/repo-mastery start github:DieselZhang/repo-mastery
```

The skill walks you through the four phases. The teaching language follows your input by default; pass `--language zh` / `--language en` to force one.

## Commands

| Command | Purpose |
|---|---|
| `/repo-mastery preview <path\|url>` | Recon — macro brief only (what / architecture / differentiation / key highlights / deep-dive candidates); zero side effects, no `.learning/` created; say "深学" to hand off into start |
| `/repo-mastery start <path\|url>` | Main flow: value brief → map → confirm → overview → learn (textbook-mode chapter by default per module); `--fresh` restarts an existing course |
| `/repo-mastery continue` | Resume — smart route: no `.learning/`? guide to start; incomplete? session preamble, due review (signposted), then new content; complete? report done. A bare `/repo-mastery` is this command. |
| `/repo-mastery review` | Spaced-review only — drains due reviews, never opens new content |
| `/repo-mastery note ["<text>"]` | Consolidate the discussion since the last note into the module note (categorized); optional text appended verbatim |
| `/repo-mastery status` | Refresh the one-page status dashboard `MASTERY.md` (progress / mastery % / review due / next objective) |

## Data Model

```text
<target-repo>/.learning/          ← travels with the repo; auto-gitignored
  ├── MISSION.md                  learning mission (why you want to master it)
  ├── course-map.json             confirmed course map
  ├── progress.json               mastery / spaced review / blockers
  ├── MASTERY.md                  one-page status dashboard (progress / mastery % / review due / next objective)
  ├── records/NNNN-slug.md        ADR-style learning records (understanding evolution)
  ├── notes/<module>.md           structured notes (auto + manual /note interval consolidation)
  ├── notes/.boundary.json        /note interval boundary (module_id + timestamp)
  ├── chapters/<module>.md        textbook-mode chapter material (default path; one per module)
  ├── briefs/<module>.md          module briefs (large repos, token-saving)
  ├── export/                     HTML course output (index.html + modules/0N-slug.html; see Phase 4)
  └── code-map.json               large-repo index (optional)
~/.repo-mastery/                  global lightweight memory
  ├── profile.md                  cross-repo preferences / level / blockers
  └── index.json                  repos studied + resume state
```

## Project Structure

```text
repo-mastery/
├── SKILL.md                        skill definition (English; Agent Skills standard)
├── README.md                       this file
├── README.zh-CN.md                 Chinese mirror
├── ADOPTION.md                     attribution: DeepTutor / docs-to-course / teach
├── CONTRIBUTING.md                 contributor guide
├── AGENTS.md                       protocol for AGENTS.md tools (Codex, opencode, Cursor)
├── GEMINI.md                       protocol for Gemini CLI
├── LICENSE                         MIT
├── package.json                    npm packaging (`repo-mastery install` one-command CLI)
├── .claude-plugin/                 Claude Code plugin marketplace + plugin manifests
│   ├── marketplace.json
│   └── plugin.json
├── agents/
│   └── openai.yaml                 Codex / Agent-Skills UI metadata
├── bin/
│   └── repo-mastery.js             npm one-command installer
├── scripts/
│   ├── learning_engine.py          the deterministic gate (mastery/schedule/record/next/validate/init)
│   ├── index_repo.py               large-repo code index (pure stdlib)
│   └── install.sh                  install to Claude Code + Codex + Gemini (also curl-pipeable)
├── references/                     skill internals (read by the skill per phase)
│   ├── curriculum-design.md        course map design from source
│   ├── mastery-policy.md           mastery / gates / spaced review / error diagnosis
│   ├── session-flow.md             interactive learning protocol (Mission + ZPD)
│   ├── quiz-design.md              quiz design (test application, not memory)
│   ├── module-brief-template.md    module briefs (pre-extracted snippets)
│   ├── note-template.md            note format
│   ├── learning-records-template.md ADR-style learning records
│   ├── gotchas.md                  failure-point checklist
│   ├── index-script-spec.md        index script docs
│   └── html-shell/                 HTML course shell (copied verbatim from docs-to-course)
└── docs/
    ├── ARCHITECTURE.md             design & architecture (English)
    ├── USAGE.md                    usage guide (English)
    └── zh-CN/                      Chinese mirrors
```

## Documentation

- [Architecture](./docs/ARCHITECTURE.md) — design, mastery engine, phases, data model.
- [Usage](./docs/USAGE.md) — detailed command reference and learning walkthrough.
- [Changelog](./CHANGELOG.md) — per-version notable changes (v1.0.0 → v3.2.0).
- [Adoption & attribution](./ADOPTION.md) — what this skill absorbs from DeepTutor, docs-to-course, and the teach skill.

## Contributing

Contributions are welcome. See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

## License

[MIT](./LICENSE) © 2026 DieselZhang.

## Acknowledgments

- **Mastery engine** adapted from [DeepTutor](https://github.com/HKUDS/DeepTutor) (HKUDS, MIT) — deterministic gates, spaced repetition, error diagnosis, `explore_context` pre-scan.
- **Curriculum design & HTML shell** absorbed from `docs-to-course` (codebase-to-course).
- **Learning mechanisms** (Mission, ZPD, learning records, fluency vs storage) absorbed from [mattpocock-skills](https://github.com/mattpocock)'s `teach` skill.

Full per-item attribution: [ADOPTION.md](./ADOPTION.md).


## 文件 AGENTS.md

# Repo-Mastery — Agent Instructions (AGENTS.md)

> This file makes Repo-Mastery usable from any agent that reads `AGENTS.md`
> (OpenAI Codex, opencode, Cursor, and compatible CLIs). Claude Code loads the
> skill natively via `SKILL.md`; Gemini CLI via `GEMINI.md`. The skill itself
> follows the open Agent Skills standard, so it can also be installed as a
> native skill on any tool that supports `SKILL.md`.

## What this is

Repo-Mastery turns any open-source repository into a **developer-focused
mastery course**: a value brief + confirmed course map, then overview-first
mastery learning (global overview → module overview → key-node discussion →
lightweight verification → spaced review) so the user fully masters a
project's **usage → architecture → key implementations**. The whole picture
comes before the nodes — **engine-enforced** via `flow_phase`: `next-objective`
refuses points until the overviews are presented and `set-phase` advances.

## When to act as the Repo-Mastery tutor

Activate this behavior when the user says any of:

- "learn / master / fully understand / deep-dive into" a repository or codebase
- "turn X repo into a course", "master this codebase", "learn X from source"
- They point at a local repo path or `github:owner/repo`

## The deterministic engine — always call it, never re-derive it

The **gate** (does the learner advance?) is computed by the engine script, not
interpreted from prose. Before/after any judgment, call:

```bash
python3 <skill_root>/scripts/learning_engine.py <subcommand> ...
```

| Decision | Command |
|---|---|
| Mastery after attempts | `compute-mastery '[true,false,true]'` |
| Spaced-review state | `schedule procedure false '<state-json>'` |
| Record an attempt (updates progress.json) | `record-attempt <path>/.learning/progress.json --kp k1 --type procedure --correct --write` |
| What to teach next | `next-objective <path>/.learning/progress.json [--mode review]` |
| Advance the overview flow | `set-phase <path>/.learning/progress.json module_overview --module m01` |
| Begin a textbook-mode chapter | `chapter-start <path>/.learning/progress.json --module m01 --sections N` |
| Advance a chapter (section/status) | `chapter-advance <path>/.learning/progress.json --section 2 --status qna` |
| Close the module-level gate | `chapter-complete <path>/.learning/progress.json` |
| Record a qualitative judgment | `set-qualitative <path>/.learning/progress.json --kp k1 --type concept --pass` |
| Validate a course map | `validate-map <path>/.learning/course-map.json` |
| Create `.learning/` scaffolding | `init <repo_path> [--force]` |

The engine is pure stdlib Python, JSON in/out. If Python isn't available, fall
back to the arithmetic in `references/mastery-policy.md` — but prefer the script.

## The workflow (follow this order)

1. **Phase 0 — assess complexity.** Small/medium repo → read source directly.
   Large (≥100k lines / ≥20 top modules) → run `scripts/index_repo.py` to build
   `code-map.json`, locate source on demand. **Optional recon prefix**: if the
   user opened with `/repo-mastery preview <repo>` (macro brief only, no
   `.learning/`), its five-section brief feeds Phase 2's value brief — on
   "深学", skip re-scanning and hand off into the course flow (see
   `references/preview-brief.md`).
2. **Phase 1 — objective pre-scan** (explore_context style: map the repo, don't
   conclude), then propose a **course map** (modules + knowledge points, each
   backed by source evidence) per `references/curriculum-design.md`.
3. **Phase 2 — value brief + Mission + confirmation (mandatory).** First
   present what this repo can teach and what makes it stand out vs peers, then
   clarify "why do you want to master this repo?" (one-at-a-time Mission tree)
   → write `.learning/MISSION.md`
   (incl. value positioning). Present the full map at once (each module with a
   recommended keep/adjust/drop); the user replies with all adjustments in one
   go, thresholds default to 0.7, and follow-up lands only on adjusted modules;
   the user approves/customizes before any learning. Never skip this. **External
   ecosystem retrieval happens
   only in Phase 2** (never Phase 1): peer/ecosystem facts go into
   `.learning/positioning.md` (see `references/positioning-brief.md`) as
   `[web]` + access date (repo facts stay `[src]` + `file:line`); unsourced
   tutor-memory claims are `[unv]` — search seeds only, never gated. No search
   tool available → build the brief from repo evidence and mark peer rows
   `[unv]` / 「需验证」; never fabricate a source. Immediately generate the first-draft
   course note COVERAGE.md, **ask whether to also build the shareable HTML
   course** (Phase 4; if yes, build it from the draft), and set
   `flow_phase: "overview"` in
   `progress.json` so the course opens engine-forced at the global overview.
4. **Phase 3 — overview-first mastery learning** per
   `references/session-flow.md`. Global overview → `set-phase module_overview
   --module m01` → per-module overview → `set-phase learning` → key-node
   discussion: explain (from source, discussion-first) → **give the reference
   answer, the user reacts to the proposal** (grill-me style; restate in their
   own words) → lightweight verification (Feynman restatement for
   concept/design; light question + self-check for procedure; none for memory —
   reference cheatsheet). **Every gate decision goes through the engine
   script**, including the `flow_phase` gate. This discussion loop is shared by
   textbook mode's section walk and after-class checking; the standalone
   per-point loop is a **supplement** (test-out / single-point deep-dive /
   post-review reteach), not a parallel learning path.
5. **Textbook mode (chapter) — the default on entering each module.** After the
   module overview, auto-start the flipped-classroom chapter flow (one line of
   notice first — an awareness statement, not a confirmation gate); switch to
   the interactive per-point mode only when the learner asks for it, for that
   module: (a) generate `chapters/<module>.md` (complete material; the
   module's HTML page rides the HTML course build — decided once at start,
   refreshed at completion, see Phase 4) → `chapter-start`; (b) walk it
   **section by section**, **pausing after each section** for the user's
   confirmation before `chapter-advance` — never chain sections in one turn;
   (c) `--status qna` after-class Q&A (same pause before advancing out of
   teaching); (d) `--status verifying` — 1–2 deep questions on the
   module's **key nodes** through the engine (`set-qualitative` for
   concept/design, `record-attempt` for procedure); (e) `chapter-complete` —
   the **module-level gate** (see Hard rules). The chapter's 课后思考题 must
   carry course-map `kp_id`s or checking can't go through the engine.
6. **Phase 4 — continuously-updated course note.** Update `COVERAGE.md`
   module-by-module as learning progresses. The HTML course is **decided once
   at Phase 2 confirmation** (ask the user; if yes, build from the first draft
   via `references/html-shell/`, copy verbatim) and **refreshed at course
   completion** (on request, from the final COVERAGE.md). It is built into
   `<repo>/.learning/export/` (`index.html` + `modules/0N-slug.html`).

## Hard rules

- **Never** replace the gate with "do you feel you've got it?" — call the engine.
- **Learning interaction is reference-answer-first** (grill-me style): after
  explaining, give the reference answer and let the user react to the proposal
  — never a blank-prompt exam.
- **Never** show a graded procedure question's expected answer *before* the
  user answers; store it in `progress.json.pending_question` server-side, and
  show it right *after* for self-check.
- **Course-map approval is mandatory** (opposite of docs-to-course).
- Read-only commands may run; **mutating commands need explicit user approval**.
- Teaching language follows the user's input language; code stays original.
- **Resuming always opens with the Session Preamble** — cross-session resumes
  replay the full preamble (value replay + MASTERY status); same-session
  continue uses a slim one-liner (last position + next objective + due count),
  display-only, before any node.
- **Advance `flow_phase` with `set-phase`** after presenting each overview;
  otherwise `next-objective` keeps refusing new points.
- **`--mode review` bypasses the overview gate** — never block a scattered-time
  review on an unfinished overview.
- **The tutor always pauses for confirmation between sections** — after each
  section (and before advancing out of teaching into Q&A) it hands control back
  with a natural confirmation point and only calls `chapter-advance` on an
  explicit user reply. Never chain sections in one turn — the engine can't see
  the conversation, so the pause is the tutor's responsibility.
- **The module-level gate is still an engine decision** — `chapter-complete`
  covers a module but never fakes mastery: key nodes keep their real engine
  records, and every unverified point gets initialised spaced review whose real
  mastery is built only by later review attempts. Never write a mastery score
  for a point the learner never actually answered.
- **New modules default to textbook-mode chapter** — after the module overview,
  auto-start the chapter flow (`chapter-start`); don't silently offer per-point
  nodes. The interactive per-point mode is an explicit, conversational per-module
  switch ("切交互式"), preceded by one line of notice — an awareness statement,
  not a confirmation gate.
- **`--mode review` also bypasses the chapter gate** — an in-progress chapter
  never blocks scattered-time review.
- **Layered wrap-up** — substantive turns (explanation / judgment / error
  diagnosis / new conclusion) close with full wrap-up: write-back +
  auto-consolidate + index.json + MASTERY.md refresh + one-line progress
  report. Mechanical turns (review drain, simple confirmation, Q&A digesting)
  **skip auto-consolidate and the MASTERY refresh** — the next substantive
  turn's consolidation covers the stretch (see `session-flow.md` §7).
- **MASTERY.md is the status dashboard** — `/repo-mastery status` regenerates
  it from `progress.json` + `course-map.json` (progress / mastery % / review
  due / next objective); substantive wrap-up refreshes it; the Session Preamble
  reads it, display-only. COVERAGE.md stays content-only (see `session-flow.md`
  §8).

## Where the details live

Read the relevant reference only when you reach that phase (keep context lean):

- Ecosystem positioning & differentiation (Phase 2): `references/positioning-brief.md`
- Course map design: `references/curriculum-design.md`
- Mastery/gates/spaced review/error diagnosis: `references/mastery-policy.md`
- Session protocol: `references/session-flow.md`
- Quiz design: `references/quiz-design.md`
- Notes / learning records: `references/note-template.md`,
  `references/learning-records-template.md`
- Failure checklist: `references/gotchas.md`

## Install hints per tool

One-command installs (published package):

```bash
npx @dieselzhang/repo-mastery install            # all tools
curl -fsSL https://raw.githubusercontent.com/DieselZhang/repo-mastery/main/scripts/install.sh | bash
```

- **Claude Code**: `~/.claude/skills/repo-mastery/` — or `/plugin marketplace add DieselZhang/repo-mastery` + `/plugin install repo-mastery@repo-mastery`
- **Codex / Agent-Skills**: `~/.codex/skills/repo-mastery/` or `~/.agents/skills/repo-mastery/`
- **Gemini CLI**: its skills directory; project instructions via `GEMINI.md`
- Or run `scripts/install.sh` to install everywhere at once.


## 文件 SKILL.md

---
name: repo-mastery
description: "Turn any open-source repository into a developer-focused mastery course. Given a local repo path or GitHub URL, build a confirmed course map and drive overview-first learning (architecture picture, then key-node discussion, then spaced review) with hands-on tasks and a continuously-updated course note (Markdown + HTML). Triggers: 'learn this repo', 'master this codebase', 'turn X into a course', 'deep-dive into X project'."
origin: personal
version: 3.2.0
tags: [learning, education, codebase, mastery, spaced-repetition]
---

# Repo-Mastery — Master an Open-Source Project from Source

## When to Activate
- user wants to learn/master/deep-dive an open-source repo or codebase
- user got new project source and wants systematic learning
- user wants architecture + key implementations from source (not usage docs)
- user wants progress to persist across sessions (spaced review + notes)
- triggers: "learn this repo", "master this codebase", "turn X into a course"

Do NOT activate for doc/README summaries, one-off code Q&A, or end-user tutorials — that is docs-to-course.

## Setup
- Target: local path or github:owner/repo (auto git clone --depth 1)
- Python 3: only for the large-repo index (scripts/index_repo.py, pure stdlib)
- Creates .learning/ in the target (auto-gitignored). ~/.repo-mastery/ (profile + index) is an OPT-IN profile — not read automatically; consulted only when the user explicitly asks for saved preferences. The current directory's .learning/ is the sole automatic state source.
- Teaching language follows the user's input (--language zh|en to force); code, paths, identifiers keep original form
- Runs on Claude Code / Codex / Gemini CLI / AGENTS.md tools (agentskills.io)

## Commands
(6 commands — each: signature + one imperative line)
/repo-mastery preview <path|url>    # zero-side-effect recon: macro brief in chat, no .learning/, no engine. Say "deep-dive" (or the user's language for "go deeper") to hand off into start.
/repo-mastery start [path|url] [--language zh|en] [--fresh]   # value brief → map confirm → overview-first learning (textbook-mode chapter per module by default); path defaults to the current directory; --fresh restarts an existing course.
/repo-mastery continue              # resume the current directory's .learning/ (session preamble first, then next-objective). If none, say so and guide to start on the current dir — never jump to a project from global memory.
/repo-mastery review                # spaced review only: drain due reviews, bypass overview gate, never open new content.
/repo-mastery note ["<text>"]       # consolidate discussion since last note into notes/<module>.md (categorized); <text> appended verbatim.
/repo-mastery status                # refresh MASTERY.md one-page dashboard from progress.json + course-map.json.

(Bare /repo-mastery routes by the current directory: has .learning/ → continue; no .learning/ → start a course on the current directory. The shared due-review pool: continue runs next-objective end-to-end and signposts due reviews; review drains them alone and bypasses the flow_phase overview gate. Preview is zero-side-effect: brief in chat, handoff on "deep-dive". Both continue and review loop next-objective, act on the returned action (overview | module_overview | chapter | answer_pending | review | complete), and stop on a non-review action.)

(Gate invariant — always hold: advancement is a deterministic engine decision, never an LLM self-assessment; mastery is built from real attempts, never faked.)

## Session Preamble (mandatory on every resume)
- New course (current dir has no .learning/ / fresh start): start clean — do NOT read ~/.repo-mastery/ preferences or index.json; teaching language follows the user's current input.
- Resume (current dir has .learning/): read the current dir's MISSION.md + positioning.md (value replay) → MASTERY.md (map + progress) → due review/chapter first. Display-only, no questions. Global memory (profile.md) is referenced only if the user explicitly asks ("use my saved preferences" / 「用我之前的偏好」).
- Same-session: one line — "Last learned X, next objective Y, N reviews due" (Chinese example: 「上次学到 X，下一步 Y，due N 条复习」).
- Then advance per next-objective. While flow_phase is overview/module_overview, next-objective refuses knowledge points (engine-enforced).

## Main Flow (/repo-mastery start)
Phase 0 — Complexity: <100k lines small/medium (read directly); ≥100k or ≥20 top-level modules large (run scripts/index_repo.py → code-map.json). See references/index-script-spec.md; measure with find + wc -l when unsure.
Phase 1 — Pre-scan → course-map candidates: objective map (README, entry, structure, build, core modules); generate candidates per references/curriculum-design.md. Repo-internal only (no ecosystem scan yet).
Phase 2 — Value brief + Mission + map confirm: deliver the value brief (what this repo can teach + differentiation) per references/clarification-interview.md §0 + references/positioning-brief.md (external retrieval for peer facts; [src]/[web]/[unv] discipline); clarify Mission one question at a time with recommended answers; present the full module list at once, user replies all adjustments in one batch, follow-up only on adjusted modules; pass_threshold defaults 0.7. Learning starts only after approval. Then write .learning/ (MISSION.md, positioning.md, course-map.json), set-phase overview, generate first-draft COVERAGE.md.
Phase 3 — Overview-first learning: next-objective is gated by flow_phase — present global overview (Phase 3.0) → set-phase module_overview --module m01 → present module overview → set-phase learning → per-point learning. In each module: textbook-mode chapter by default (see Textbook Mode); per-point interactive mode is a supplement (test-out / single-point deep-dive / post-review reteach), switched conversationally. Learning loop: explain from source → give reference answer → user reacts → judge (Feynman recital for concept/design; lightweight scenario question + self-check for procedure) → error diagnosis → spaced review. Reference answer first, never a blank prompt; expected answer shown after for graded procedure questions. Hands-on on demand (read-only commands run; mutating requires approval). Auto-consolidate substantive turns into notes/<module>.md. See references/session-flow.md, mastery-policy.md, quiz-design.md.
Phase 4 — Continuously-generated course note: COVERAGE.md generated at Phase 2, updated per module; HTML course decided once at start (reuse references/html-shell/, copy verbatim), refreshed at completion. MASTERY.md is the status dashboard (regenerated by status).

## Textbook Mode (chapter) — default on entering each module
Five steps (engine-gated):
1. Generate chapters/<module>.md (intro → sections [each = one knowledge point: explain + source walk file:line + recap + review questions aligned to knowledge_point_ids] → chapter summary → cheatsheet) → chapter-start.
   Each section's source walk pastes the relevant source (file:line locator + inline key fragment + collapsible `<details>` full source) — see `note-template.md`.
2. Walk section by section; after each section STOP and wait for explicit user reply before chapter-advance --section N.
3. Q&A (status=qna): user asks freely.
4. Verification (status=verifying): 1-2 deep questions on key nodes → set-qualitative / record-attempt.
5. Complete (chapter-complete): module-level gate — covered points get initialized spaced review (not fake mastery); module joins chapter_covered_modules; points still enter review queue. Status shows three states: 未掌握 / 已覆盖 · 待复习验证 / 已掌握 (not-yet-learned / Covered · awaiting review verification / mastered) — covered ≠ mastered.

## Data Structures
<target-repo>/.learning/: MISSION.md, positioning.md, course-map.json, progress.json, MASTERY.md, records/, notes/ (incl .boundary.json), chapters/, briefs/, code-map.json, export/, .gitignore
~/.repo-mastery/: profile.md, index.json   (opt-in profile — not read automatically; consulted only on explicit request)

Expected answers of pending questions live server-side in progress.json — never round-trip to the user before grading.

## Reference Files (read per phase)
- curriculum-design.md (P1), positioning-brief.md (P2), preview-brief.md (preview), clarification-interview.md (P2), mastery-policy.md (P3), session-flow.md (P3), quiz-design.md (P3), module-brief-template.md (P3 large), note-template.md (P3), learning-records-template.md (all), gotchas.md (all), index-script-spec.md (P0 large), example-walkthrough.md (any), html-shell/ (P4)

## Scripts
- scripts/learning_engine.py — the deterministic gate. Call for compute-mastery / schedule / record-attempt / next-objective / set-phase / chapter-* / validate-map / init. Never re-derive the math.
- scripts/index_repo.py — large-repo index (pure stdlib).
- scripts/install.sh — install to Claude Code + Codex + Gemini CLI.

## Related Skills
- docs-to-course: docs → end-user usage course (source of methodology).
- understand-anything: knowledge-graph of a codebase (pair for architecture deep dives).

## Verification
Self-check with references/gotchas.md; confirm: .learning/ gitignored; course-map.json confirmed; progress.json atomic; notes on substantive turns + ~/.repo-mastery/index.json updated; no expected-answer leakage; no unapproved mutating commands.

