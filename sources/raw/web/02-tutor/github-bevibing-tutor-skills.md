# bevibing/tutor-skills

- 链接：https://github.com/bevibing/tutor-skills
- 作者：bevibing
- 仓库说明：A Claude Code skill that turns PDFs, docs, and codebases into Obsidian study vaults
- 星数：1352
- 获取方式：GitHub README + SKILL/说明文件

---

## README

# tutor-skill

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude_Code-skill-blue)](https://docs.anthropic.com/en/docs/claude-code)
[![Install with npx skills](https://img.shields.io/badge/npx_skills-add-green)](https://github.com/vercel-labs/skills)

Two [Claude Code](https://docs.anthropic.com/en/docs/claude-code) skills that turn any knowledge source into an **Obsidian StudyVault** and then quiz you on it — closing the loop from content to comprehension.

## How It Works

```
  Documents / Code                    Obsidian                    Quiz Session
 ┌──────────────────┐           ┌──────────────────┐          ┌──────────────────┐
 │  PDF, MD, HTML,  │  /tutor   │   StudyVault/    │  /tutor  │  4 questions per  │
 │  EPUB, source    │──setup──▶ │   structured     │────────▶ │  round, graded,   │
 │  code projects   │           │   interlinked    │          │  concept tracking  │
 └──────────────────┘           │   notes + MOC    │          └────────┬─────────┘
                                └──────────────────┘                   │
                                         ▲                             │
                                         └─────── progress updates ────┘
```

## Skills Overview

| Skill | Command | Purpose | Input | Output |
|-------|---------|---------|-------|--------|
| **tutor-setup** | `/tutor-setup` | Generate a StudyVault | Documents or source code | Obsidian vault with notes, dashboards, practice questions |
| **tutor** | `/tutor` | Interactive quiz tutor | An existing StudyVault | Quiz sessions with concept-level progress tracking |

## Quick Start

### One-line install (recommended)

```bash
npx skills add RoundTable02/tutor-skills
```

> Requires [npx skills](https://github.com/vercel-labs/skills) — works with Claude Code, Cursor, Windsurf, and more.

### Manual install

```bash
git clone https://github.com/RoundTable02/tutor-skills.git
cd tutor-skills
./install.sh
```

### Step 1: Generate a StudyVault

```bash
cd ~/study-materials/          # or any source code project
claude
> /tutor-setup
```

### Step 2: Start Quizzing

```bash
claude
> /tutor
```

---

## tutor-setup

Transforms knowledge sources into a structured Obsidian StudyVault. Mode is auto-detected:

| Marker Found | Mode |
|---|---|
| `package.json`, `pom.xml`, `build.gradle`, `Cargo.toml`, `go.mod`, etc. | Codebase Mode |
| No project markers | Document Mode |

### Document Mode

Turns PDFs, text files, web pages, and other sources into comprehensive study notes.

- Auto-scans working directory for source files (PDF, TXT, MD, HTML, EPUB)
- Extracts and analyzes content with verified source mapping
- Generates concept notes with comparison tables, ASCII diagrams, and exam patterns
- Creates practice questions with hidden answers (active recall via fold callouts)
- Builds a dashboard with Map of Content (MOC), Quick Reference, and Exam Traps
- Full interlinking with `[[wiki-links]]` across all notes

**Phases**

| Phase | Name | Description |
|-------|------|-------------|
| D1 | Source Discovery | Scan, extract, and verify source content mapping |
| D2 | Content Analysis | Build topic hierarchy and dependency map |
| D3 | Tag Standard | Define English kebab-case tag registry |
| D4 | Vault Structure | Create numbered folders per topic |
| D5 | Dashboard | MOC, Quick Reference, Exam Traps |
| D6 | Concept Notes | Structured notes with tables, diagrams, callouts |
| D7 | Practice Questions | Active recall with fold callouts (8+ per topic) |
| D8 | Interlinking | Cross-reference all notes with wiki-links |
| D9 | Self-Review | Verify against quality checklist |

**Generated structure**

```
StudyVault/
  00-Dashboard/          # MOC + Quick Reference + Exam Traps
  01-<Topic1>/           # Concept notes + practice questions
  02-<Topic2>/
  ...
```

### Codebase Mode

Generates a new-developer onboarding vault from a source code project.

- Auto-detects tech stack, architecture patterns, and module boundaries
- Traces request flows and data flows end-to-end
- Creates per-module notes with key files, public interfaces, and dependency maps
- Generates onboarding exercises (code reading, configuration, debugging, extension)
- Builds a dashboard with architecture overview, module map, API surface, and getting started guide

**Phases**

| Phase | Name | Description |
|-------|------|-------------|
| C1 | Project Exploration | Scan files, detect tech stack, map layout |
| C2 | Architecture Analysis | Identify patterns, trace flows, map modules |
| C3 | Tag Standard | Define `#arch-*`, `#module-*`, `#pattern-*` registry |
| C4 | Vault Structure | Create dashboard + per-module folders |
| C5 | Dashboard | MOC with module map, API surface, getting started |
| C6 | Module Notes | Purpose, key files, interface, flow, dependencies |
| C7 | Exercises | Code reading, config, debugging, extension tasks |
| C8 | Interlinking | Cross-link all modules and exercises |
| C9 | Self-Review | Verify against quality checklist |

**Generated structure**

```
StudyVault/
  00-Dashboard/          # MOC + Quick Reference + Getting Started
  01-Architecture/       # System overview, request flow, data flow
  02-<Module1>/          # Per-module notes
  03-<Module2>/
  ...
  NN-DevOps/             # Build, deploy, CI/CD
  NN+1-Exercises/        # Onboarding exercises
```

---

## tutor

Interactive quiz tutor that tracks what you know and don't know at the **concept level**. Works with any StudyVault generated by `tutor-setup`.

### Session Types

| Type | When Available | Focus |
|------|----------------|-------|
| Diagnostic | Unmeasured areas (⬜) exist | Broad assessment of new areas |
| Drill weak areas | Weak areas (🟥/🟨) exist | Targeted practice on struggles |
| Choose a section | Always | Study any area on demand |
| Hard-mode review | All areas 🟩/🟦 | Challenge mastered material |

### Quiz Flow

1. Detects your StudyVault and reads the learning dashboard
2. Presents session options based on your current proficiency
3. Delivers 4 questions per round (4 options each, zero hints)
4. Grades answers and explains mistakes
5. Updates concept files and dashboard automatically

### Progress Tracking

Proficiency is tracked per area with emoji badges:

| Badge | Level | Rate |
|-------|-------|------|
| 🟥 | Weak | 0–39% |
| 🟨 | Fair | 40–69% |
| 🟩 | Good | 70–89% |
| 🟦 | Mastered | 90–100% |
| ⬜ | Unmeasured | No data |

Concept-level tracking stores attempts, correct count, last tested date, and error notes for wrong answers — so drill sessions rephrase missed concepts in new contexts.

---

## The Learning Cycle

```
           ┌────────────────────────────┐
           │   /tutor-setup             │
           │   Generate StudyVault      │
           └──────────┬─────────────────┘
                      │
                      ▼
           ┌────────────────────────────┐
           │   Read & review notes      │
           │   in Obsidian              │
           └──────────┬─────────────────┘
                      │
                      ▼
           ┌────────────────────────────┐
           │   /tutor                   │
           │   Take diagnostic quiz     │◀──────────┐
           └──────────┬─────────────────┘           │
                      │                              │
                      ▼                              │
           ┌────────────────────────────┐           │
           │   Review weak areas        │           │
           │   in Obsidian              │           │
           └──────────┬─────────────────┘           │
                      │                              │
                      ▼                              │
           ┌────────────────────────────┐           │
           │   /tutor                   │           │
           │   Drill weak concepts      │───────────┘
           └────────────────────────────┘
```

## Requirements

- [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code) installed and configured
- [Obsidian](https://obsidian.md/) (recommended) to open and navigate the generated vault

## Repository Structure

```
tutor-skill/
├── skills/
│   ├── tutor-setup/              # Vault generation skill
│   │   ├── SKILL.md
│   │   └── references/
│   │       ├── templates.md
│   │       ├── codebase-workflow.md
│   │       ├── quality-checklist.md
│   │       └── codebase-templates.md
│   └── tutor/                    # Interactive quiz skill
│       ├── SKILL.md
│       └── references/
│           └── quiz-rules.md
├── examples/
├── install.sh
├── uninstall.sh
├── README.md
└── LICENSE
```

## Uninstall

```bash
./uninstall.sh
```

Or manually:

```bash
rm -rf ~/.claude/skills/tutor-setup
rm -rf ~/.claude/skills/tutor
```

## License

[MIT](LICENSE)


## 文件 skills/tutor-setup/SKILL.md

---
name: tutor-setup
description: >
  Transforms knowledge sources into an Obsidian StudyVault. Two modes:
  (1) Document Mode — PDF/text/web sources → study notes with practice questions.
  (2) Codebase Mode — source code project → onboarding vault for new developers.
  Mode is auto-detected based on project markers in CWD.
argument-hint: "[source-path-or-url]"
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, WebFetch
---

# Tutor Setup — Knowledge to Obsidian StudyVault

## CWD Boundary Rule (ALL MODES)

> **NEVER access files outside the current working directory (CWD).**
> All source scanning, reading, and vault output MUST stay within CWD and its subdirectories.
> If the user provides an external path, ask them to copy the files into CWD first.

## Mode Detection

On invocation, detect mode automatically:

1. **Check for project markers** in CWD:
   - `package.json`, `pom.xml`, `build.gradle`, `Cargo.toml`, `go.mod`, `Makefile`,
     `*.sln`, `pyproject.toml`, `setup.py`, `Gemfile`
2. **If any marker found** → **Codebase Mode**
3. **If no marker found** → **Document Mode**
4. **Tie-break**: If `.git/` is the sole indicator and no source code files (`*.ts`, `*.py`, `*.java`, `*.go`, `*.rs`, etc.) exist, default to Document Mode.
5. Announce detected mode and ask user to confirm or override.

---

## Document Mode

> Transforms knowledge sources (PDF, text, web, epub) into study notes.
> Templates: [templates.md](references/templates.md)

### Phase D1: Source Discovery & Extraction

1. **Auto-scan CWD** for `**/*.pdf`, `**/*.txt`, `**/*.md`, `**/*.html`, `**/*.epub` (exclude `node_modules/`, `.git/`, `dist/`, `build/`, `StudyVault/`). Present for user confirmation.
2. **Extract text (MANDATORY tools)**:
   - **PDF → `pdftotext` CLI ONLY** (run via Bash tool). NEVER use the Read tool directly on PDF files — it renders pages as images and wastes 10-50x more tokens. Convert to `.txt` first, then Read the `.txt` file.
     ```bash
     pdftotext "source.pdf" "/tmp/source.txt"
     ```
   - If `pdftotext` is not installed, install it first: `brew install poppler` (macOS) or `apt-get install poppler-utils` (Linux).
   - URL → WebFetch
   - Other formats (`.md`, `.txt`, `.html`) → Read directly.
3. **Read extracted `.txt` files** — understand scope, structure, depth. Work exclusively from the converted text, never from the raw PDF.
4. **Source Content Mapping (MANDATORY for multi-file sources)**:
   - Read **cover page + TOC + 3+ sample pages from middle/end** for EVERY source file
   - **NEVER assume content from filename** — file numbering often ≠ chapter numbering
   - Build verified mapping: `{ source_file → actual_topics → page_ranges }`
   - Flag non-academic files and missing sources
   - Present mapping to user for verification before proceeding

### Phase D2: Content Analysis

1. Identify topic hierarchy — sections, chapters, domain divisions.
2. Separate concept content vs practice questions.
3. Map dependencies between topics.
4. Identify key patterns — comparisons, decision trees, formulas.
5. **Full topic checklist (MANDATORY)** — every topic/subtopic listed. Drives all subsequent phases.

> **Equal Depth Rule**: Even a briefly mentioned subtopic MUST get a full dedicated note supplemented with textbook-level knowledge.

6. **Classification completeness**: When source enumerates categories ("3 types of X"), every member gets a dedicated note. Scan for: "types of", "N가지", "categories", "there are N".
7. **Source-to-note cross-verification (MANDATORY)**: Record which source file(s) and page range(s) cover each topic. Flag untraceable topics as "source not available".

### Phase D3: Tag Standard

Define tag vocabulary before creating notes:
- **Format**: English, lowercase, kebab-case (e.g., `#data-hazard`)
- **Hierarchy**: top-level → domain → detail → technique → note-type
- **Registry**: Only registered tags allowed. Detail tags co-attach parent domain tag.

### Phase D4: Vault Structure

Create `StudyVault/` with numbered folders per [templates.md](references/templates.md). Group 3-5 related concepts per file.

### Phase D5: Dashboard Creation

Create `00-Dashboard/`: MOC, Quick Reference, Exam Traps. See [templates.md](references/templates.md).

- **MOC**: Topic Map + Practice Notes + Study Tools + Tag Index (with rules) + Weak Areas (with links) + Non-core Topic Policy
- **Quick Reference**: every heading includes `→ [[Concept Note]]` link; all key formulas
- **Exam Traps**: per-topic trap points in fold callouts, linked to concept notes

### Phase D6: Concept Notes

Per [templates.md](references/templates.md). Key rules:
- YAML frontmatter: `source_pdf`, `part`, `keywords` (MANDATORY)
- **source_pdf MUST match verified Phase D1 mapping** — never guess from filename
- If unavailable: `source_pdf: 원문 미보유`
- `[[wiki-links]]`, callouts (`[!tip]`, `[!important]`, `[!warning]`), comparison tables > prose
- ASCII diagrams for processes/flows/sequences
- **Simplification-with-exceptions**: general statements must note edge cases

### Phase D7: Practice Questions

Per [templates.md](references/templates.md). Key rules:
- Every topic folder MUST have a practice file (8+ questions)
- **Active recall**: answers use `> [!answer]- 정답 보기` fold callout
- Patterns use `> [!hint]-` / `> [!summary]-` fold callouts
- **Question type diversity**: ≥60% recall, ≥20% application, ≥2 analysis per file
- `## Related Concepts` with `[[wiki-links]]`

### Phase D8: Interlinking

1. `## Related Notes` on every concept note
2. MOC links to every concept + practice note
3. Cross-link concept ↔ practice; siblings reference each other
4. Quick Reference sections → `[[Concept Note]]` links
5. Weak Areas → relevant note + Exam Traps; Exam Traps → concept notes

### Phase D9: Self-Review (MANDATORY)

Verify against [quality-checklist.md](references/quality-checklist.md) **Document Mode** section. Fix and re-verify until all checks pass.

---

## Codebase Mode

> Generates a new-developer onboarding StudyVault from a source code project.
> Full workflow: [codebase-workflow.md](references/codebase-workflow.md)
> Templates: [codebase-templates.md](references/codebase-templates.md)

### Phase Summary

| Phase | Name | Key Action |
|-------|------|------------|
| C1 | Project Exploration | Scan files, detect tech stack, read entry points, map directory layout |
| C2 | Architecture Analysis | Identify patterns, trace request flow, map module boundaries and data flow |
| C3 | Tag Standard | Define `#arch-*`, `#module-*`, `#pattern-*`, `#api-*` tag registry |
| C4 | Vault Structure | Create `StudyVault/` with Dashboard, Architecture, per-module, DevOps, Exercises folders |
| C5 | Dashboard | MOC (Module Map + API Surface + Getting Started + Onboarding Path) + Quick Reference |
| C6 | Module Notes | Per-module notes: Purpose, Key Files, Public Interface, Internal Flow, Dependencies |
| C7 | Onboarding Exercises | Code reading, configuration, debugging, extension exercises (5+ per major module) |
| C8 | Interlinking | Cross-link modules, architecture ↔ implementations, exercises ↔ modules |
| C9 | Self-Review | Verify against [quality-checklist.md](references/quality-checklist.md) **Codebase Mode** section |

See [codebase-workflow.md](references/codebase-workflow.md) for detailed per-phase instructions.

---

## Language

- Match source material language (Korean → Korean notes, etc.)
- **Tags/keywords**: ALWAYS English


## 文件 skills/tutor/SKILL.md

---
name: tutor
description: >
  Interactive quiz tutor for Obsidian StudyVault learning. Use when the user wants to:
  (1) Take a diagnostic assessment of their knowledge,
  (2) Study or review specific sections/topics,
  (3) Drill weak areas identified in previous sessions,
  (4) Check their learning progress or dashboard,
  or says things like "quiz me", "test me", "let's study", "/tutor", "학습", "퀴즈", "평가".
---

# Tutor Skill

Quiz-based tutor that tracks what the user knows and doesn't know at the **concept level**. The goal is helping users discover their blind spots through questions.

## File Structure

```
StudyVault/
├── *dashboard*              ← Compact overview: proficiency table + stats
└── concepts/
    ├── {area-name}.md       ← Per-area concept tracking (attempts, status, error notes)
    └── ...
```

- **Dashboard**: Only aggregated numbers. Links to concept files. Stays small forever.
- **Concept files**: One per area. Tracks each concept with attempts, correct count, date, status, and error notes. Grows proportionally to unique concepts tested (bounded).

## Workflow

### Phase 0: Detect Language

Detect user's language from their message → `{LANG}`. All output and file content in `{LANG}`.

### Phase 1: Discover Vault

1. Glob `**/StudyVault/` in project
2. List section directories
3. Glob `**/StudyVault/*dashboard*` to find dashboard
4. If found, read it. Preserve existing file path regardless of language.
5. If not found, create from template (see Dashboard Template below)

If no StudyVault exists, inform user and stop.

### Phase 2: Ask Session Type

**MANDATORY**: Use AskUserQuestion to let the user choose what to do. Analyze the dashboard to build context-aware options, then present them.

Read the dashboard proficiency table and build options based on current state:

1. If unmeasured areas (⬜) exist → include "Diagnostic" option targeting those areas
2. If weak areas (🟥/🟨) exist → include "Drill weak areas" option naming the weakest area(s)
3. Always include "Choose a section" option so the user can pick any area
4. If all areas are 🟩/🟦 → include "Hard-mode review" option

Present these as an AskUserQuestion with header "Session" and concise descriptions showing which areas each option targets. The user MUST select before proceeding.

### Phase 3: Build Questions

1. Read markdown files in target section(s)
2. If drilling weak area: also read `concepts/{area}.md` to find 🔴 unresolved concepts — rephrase these in new contexts (don't repeat the same question)
3. Craft exactly 4 questions following `references/quiz-rules.md`

**CRITICAL**: Read `references/quiz-rules.md` before crafting ANY question. Zero hints allowed.

### Phase 4: Present Quiz

Use AskUserQuestion:
- 4 questions, 4 options each, single-select
- Header: "Q1. Topic" (max 12 chars)
- Descriptions: neutral, no hints

### Phase 5: Grade & Explain

1. Show results table (question / correct answer / user answer / result)
2. Wrong answers: concise explanation
3. Map each question to its area

### Phase 6: Update Files

#### 1. Update concept file (`concepts/{area}.md`)

For each question answered:
- **New concept**: Add row to table + if wrong, add error note under `### 오답 메모` (or localized equivalent)
- **Existing 🔴 concept answered correctly**: Increment attempts & correct, change status to 🟢, keep error note (learning history)
- **Existing 🟢 concept answered wrong again**: Increment attempts, change status back to 🔴, update error note

Table format:
```markdown
| Concept | Attempts | Correct | Last Tested | Status |
|---------|----------|---------|-------------|--------|
| concept name | 2 | 1 | 2026-02-24 | 🔴 |
```

Error notes format (only for wrong answers):
```markdown
### Error Notes

**concept name**
- Confusion: what the user mixed up
- Key point: the correct understanding
```

#### 2. Update dashboard

- Recalculate per-area stats from concept files (sum attempts/correct across all concepts in that area)
- Update proficiency badges: 🟥 0-39% · 🟨 40-69% · 🟩 70-89% · 🟦 90-100% · ⬜ no data
- Update stats: total questions, cumulative rate, unresolved/resolved counts, weakest/strongest

Dashboard stays compact — no session logs, no per-question details.

## Dashboard Template

Create when no dashboard exists. Filename localized to `{LANG}`. Example in English:

```markdown
# Learning Dashboard

> Concept-based metacognition tracking. See linked files for details.

---

## Proficiency by Area

| Area | Correct | Wrong | Rate | Level | Details |
|------|---------|-------|------|-------|---------|
(one row per section, last column = [[concepts/{area}]] link)
| **Total** | **0** | **0** | **-** | ⬜ Unmeasured | |

> 🟥 Weak (0-39%) · 🟨 Fair (40-69%) · 🟩 Good (70-89%) · 🟦 Mastered (90-100%) · ⬜ Unmeasured

---

## Stats

- **Total Questions**: 0
- **Cumulative Rate**: -
- **Unresolved Concepts**: 0
- **Resolved Concepts**: 0
- **Weakest Area**: -
- **Strongest Area**: -
```

## Concept File Template

Create per area when first question is asked. Example:

```markdown
# {Area Name} — Concept Tracker

| Concept | Attempts | Correct | Last Tested | Status |
|---------|----------|---------|-------------|--------|

### Error Notes

(added as concepts are missed)
```

## Important Reminders

- ALWAYS read `references/quiz-rules.md` before creating questions
- NEVER include hints in option labels or descriptions
- NEVER use "(Recommended)" on any option
- Randomize correct answer position
- After grading, ALWAYS update both concept file AND dashboard
- Communicate in user's language

