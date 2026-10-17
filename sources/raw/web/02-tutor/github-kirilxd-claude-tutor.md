# kirilxd/claude-tutor

- 链接：https://github.com/kirilxd/claude-tutor
- 作者：kirilxd
- 仓库说明：Turn Claude Code into your personal tutor — personalized learning plans, adaptive quizzes, SM-2 spaced repetition, and a web dashboard. Works with any topic.
- 星数：141
- 获取方式：GitHub README + SKILL/说明文件

---

## README

<p align="center">
  <img src="assets/logo.png" alt="claude-tutor logo" width="180">
</p>
<h1 align="center">claude-tutor</h1>
<p align="center">Turn Claude Code into your personal tutor — with spaced repetition.</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License"></a>
  <a href="https://github.com/kirilxd/claude-tutor"><img src="https://img.shields.io/badge/Claude_Code-2.0+-7C3AED.svg" alt="Claude Code 2.0+"></a>
  <a href="https://github.com/kirilxd/claude-tutor"><img src="https://img.shields.io/badge/node-18+-339933.svg?logo=node.js&logoColor=white" alt="Node.js 18+"></a>
</p>

<br>

<p align="center">
  <img src="assets/screenshot-overview.png" alt="Dashboard overview" width="720">
</p>

<br>

## Get started in 10 seconds

```
/plugin marketplace add kirilxd/claude-tutor
/plugin install claude-tutor@kirilxd-plugins
```

Then just say:

```
teach me about Kubernetes
```

---

## What it does

Claude Tutor creates personalized learning plans, quizzes you with adaptive difficulty, and schedules reviews using SM-2 spaced repetition — all inside Claude Code. Works with any topic: programming, system design, DevOps, languages, science, history, music theory.

**No slash commands needed.** Just talk naturally:

| Say this | Claude does this |
|---|---|
| "teach me about recursion" | Creates a learning plan with curated resources |
| "quiz me on networking" | Adaptive quiz targeting your weak areas |
| "how well do I know Python" | Progress report with study recommendations |
| "find me resources on Rust" | Curated materials grouped by module |
| "open dashboard" | Launches web UI at localhost:3847 |

## The learning cycle

```
plan → study → quiz → review → repeat
```

1. **Plan** — `/learn` researches your topic and builds a structured plan with modules, concepts, and curated resources
2. **Study** — Claude teaches each module interactively with analogies, examples, and comprehension checks
3. **Quiz** — `/quiz` tests you with mixed formats (MCQ, true/false, short answer, fill-in-blank) that adapt to your level
4. **Review** — SM-2 spaced repetition schedules concept reviews at optimal intervals (1d → 6d → 15d → ...)
5. **Repeat** — `/review` shows progress and recommends what to study next

## Key features

| | Feature | Details |
|---|---|---|
| 🧠 | **SM-2 spaced repetition** | Industry-standard algorithm schedules reviews right before you forget |
| 📊 | **Adaptive difficulty** | Questions get harder as you improve, easier when you struggle |
| 🎯 | **Weak area targeting** | Quizzes prioritize concepts you've gotten wrong before |
| 👤 | **Learner profiles** | Remembers your style (hands-on, visual, theory-first) across all topics |
| 🔍 | **Diagnostic assessment** | Calibrates your actual level so you skip what you already know |
| 🔔 | **Session-start reminders** | Shows overdue reviews every time you open Claude Code |
| 🛡️ | **Schema enforcement** | PreToolUse hooks prevent data corruption automatically |
| 🌐 | **Web dashboard** | Full visual interface — create plans, take quizzes, view calendar |

## Web dashboard

A local web UI at `http://localhost:3847` with everything you need:

| View | What it does |
|---|---|
| **Overview** | All topics, stats, overdue alerts, study recommendations |
| **Create Topic** | Build a learning plan via form — Claude researches and generates it |
| **Take Quiz** | Interactive MCQ/True-False quiz with instant feedback |
| **Plan Viewer** | Browse modules, reorder them, view resources |
| **Progress** | Score trend chart, quiz history, spaced repetition schedule |
| **Calendar** | Monthly view of upcoming and overdue reviews |
| **Profile** | Edit learning style and background preferences |

The dashboard and CLI share the same data. Switch between them freely.

<details>
<summary>Learning plan</summary>
<br>
<img src="assets/screenshot-plan.png" alt="Learning plan view" width="720">
</details>

<details>
<summary>Progress tracking</summary>
<br>
<img src="assets/screenshot-progress.png" alt="Progress tracking view" width="720">
</details>

<details>
<summary>Review calendar</summary>
<br>
<img src="assets/screenshot-calendar.png" alt="Review calendar view" width="720">
</details>

## Commands

| Command | Description | Example |
|---|---|---|
| `/learn <topic>` | Create a learning plan with web research | `/learn Kubernetes` |
| `/quiz [topic]` | Take an adaptive quiz | `/quiz` or `/quiz DNS` |
| `/review [topic]` | View progress and recommendations | `/review` |
| `/resources <topic>` | Get curated learning resources | `/resources system design` |
| `/dashboard` | Launch the web dashboard | `/dashboard` |

## Your data stays local

All data is stored on your machine. Nothing is sent to external services.

```
~/.claude/learning/
├── index.json              # topic registry
├── profile.json            # learner preferences
├── plans/
│   └── <topic>-<date>.json # learning plans
└── progress/
    └── <topic>.json        # quiz results, spaced repetition schedules
```

## Development

```
claude-tutor/
├── .claude-plugin/
│   ├── plugin.json         # plugin manifest
│   └── marketplace.json    # marketplace definition
├── commands/               # slash command definitions
├── skills/                 # skill instructions (SKILL.md files)
│   ├── learn/
│   ├── quiz/
│   ├── review/
│   ├── resources/
│   └── dashboard/server/   # Express server + vanilla JS frontend
├── hooks/                  # PreToolUse + SessionStart hooks
├── tests/                  # hook unit tests
└── evals/                  # trigger + functional evaluations
```

### Running tests

```bash
node tests/test-hooks.js                              # hook unit tests (27 tests)
./evals/run-trigger-eval.sh                           # trigger evals (17 prompts)
./evals/run-functional-eval.sh                        # end-to-end evals (21 checks)
node skills/dashboard/server/tests/dashboard.test.js  # dashboard tests (30 scenarios)
```

## Known limitations

| Limitation | Details |
|---|---|
| **Quiz formats** | Dashboard supports MCQ and True/False only. Short answer and fill-in-blank are CLI-only. |
| **AskUserQuestion** | CLI may fall back to plain text depending on Claude Code version. |
| **CLI schema drift** | Claude occasionally invents field names. Dashboard normalizes on read; hook blocks common errors. |

## Uninstalling

```
/plugin uninstall claude-tutor@kirilxd-plugins
/plugin marketplace remove kirilxd-plugins
```

To remove learning data: `rm -rf ~/.claude/learning/`

## License

MIT


## 文件 CLAUDE.md

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

A Claude Code plugin that turns Claude into a personal tutor with spaced repetition. Users install it via the plugin marketplace and interact through slash commands (`/learn`, `/quiz`, `/review`, `/resources`, `/dashboard`) or natural language.

## Testing

```bash
node tests/test-hooks.js                              # Hook unit tests (27 tests, instant)
./evals/run-trigger-eval.sh                           # Natural language trigger routing (17 prompts)
./evals/run-functional-eval.sh                        # End-to-end workflows (21 checks)
node skills/dashboard/server/tests/dashboard.test.js  # Dashboard tests (30 scenarios)
```

Run hook tests after any change to `hooks/enforce-paths.js` or data schemas.

## Architecture

The plugin has three layers that work independently:

**Skills** (`skills/*/SKILL.md`) — Markdown instructions that Claude follows. Not code. Each skill defines a multi-phase workflow (e.g., learn: clarify scope → research → generate plan → save). Skills reference data paths and schemas but don't enforce them.

**Hooks** (`hooks/`) — Node.js scripts that enforce data integrity at write time:
- `enforce-paths.js` — PreToolUse hook on Write/Edit. Blocks wrong paths, schema leakage between plan/progress files, unknown fields, and score format errors. This is the safety net for when Claude invents field names.
- `session-start.js` — SessionStart hook. Reads spaced repetition data and prints overdue review reminders.

**Dashboard** (`skills/dashboard/server/`) — Express server at localhost:3847. Reads/writes the same JSON files as the CLI. Has its own validation (`validate.js`) that mirrors the hook logic plus SM-2 algorithm implementation.

## Data Layout

All user data lives in `~/.claude/learning/` (absolute path, never relative):

| Path | Purpose | Allowed top-level fields |
|---|---|---|
| `~/.claude/learning/index.json` | Topic registry | `topics` (map of slug → metadata) |
| `~/.claude/learning/profile.json` | Learner preferences | `learningStyle`, `background`, `createdTopics` |
| `~/.claude/learning/plans/<slug>-<date>.json` | Learning plans | `topic`, `slug`, `created`, `level`, `goal`, `depth`, `timeCommitment`, `modules`, `totalEstimatedTime`, `diagnostic` |
| `~/.claude/learning/progress/<slug>.json` | Quiz progress | `topic`, `quizzes`, `weakAreas`, `strongAreas`, `overallScore`, `spacedRepetition` |

**The critical rule:** Plan fields and progress fields must never cross directories. The hook blocks this, but skills must also get the paths right. `overallScore` is a percentage (0-100), not a fraction (0-1).

## Command → Skill → Tool Chain

Each command (`commands/*.md`) defines `allowed-tools` that restrict what Claude can do:
- `/learn` — AskUserQuestion, WebSearch, WebFetch, Read, Write, Bash(mkdir)
- `/quiz` — AskUserQuestion, Read, Write, Bash(mkdir)
- `/review` — Read only
- `/resources` — WebSearch, WebFetch, Read
- `/dashboard` — Bash(node/npm/cd)

When modifying a skill, check the matching command's `allowed-tools` — the skill can't use tools the command doesn't allow.

## Dashboard Server

The server (`skills/dashboard/server/`) shares data with the CLI via the same JSON files. Key modules:
- `api.js` — REST routes (`/api/stats`, `/api/topics`, `/api/plans/:slug`, `/api/progress/:slug`, etc.)
- `validate.js` — Schema validation + SM-2 algorithm (`updateSM2`, `computeWeakStrong`, `getModuleScores`)
- `sse.js` — Server-sent events for streaming Claude responses to the browser
- `public/app.js` — Vanilla JS SPA (no framework, hash-based routing)

Dashboard runs on port 3847. To run manually: `cd skills/dashboard/server && npm install && node index.js`

## Common Pitfalls

- Claude invents field names like `quiz_history`, `results`, `history` instead of `quizzes` — the hook catches this but skills should use correct names
- Writing to `./learning/` (relative) instead of `~/.claude/learning/` (absolute) — hook blocks this
- Putting quiz data in plan files or vice versa — hook blocks this
- `overallScore: 0.85` instead of `overallScore: 85` — hook blocks this
- Skills reference `AskUserQuestion` tool — each skill has a line enforcing its use, but the model may still fall back to plain text in some Claude Code versions


## 文件 skills/dashboard/SKILL.md

---
name: dashboard
description: Use only when user explicitly asks to "open dashboard", "show dashboard", "launch dashboard", or "learning UI". Opens a local web interface for viewing and editing learning plans, quiz progress, and spaced repetition data.
---

# Dashboard — Learning Data Web UI

**ALWAYS** use the `AskUserQuestion` tool when asking the user questions, in any context. If you have too many questions for the tool, split them up into multiple calls.

The dashboard is a local web server that provides a visual interface for the learning data stored in `~/.claude/learning/`.

To launch: run `/dashboard` or tell the user to run `/dashboard`.

The dashboard runs at `http://localhost:3847` and supports:
- Viewing all topics, plans, and progress
- Editing module order and resources
- Viewing and overriding spaced repetition schedules
- Calendar view of upcoming reviews
- Resetting progress or deleting topics
- Launching quiz/learn sessions in Claude Code


## 文件 skills/learn/SKILL.md

---
name: learn
description: Use when user wants to learn a topic or create a study plan. Triggers on "teach me", "I want to learn", "explain X to me", "study", "help me understand", "where do I start with", "how do I get into", or any request to understand a subject in depth. Covers both technical topics (programming, system design, DevOps) and general knowledge (history, science, languages, music theory). Also use when someone asks for a "learning path", "roadmap", or "curriculum" for a topic — even if they don't explicitly say "learn".
---

# Learn — Topic Research & Learning Plan Generator

## Overview

Guide the user from a vague "I want to learn X" into a structured, researched learning plan with curated resources. Ask clarifying questions, research the topic, and produce a module-by-module plan saved to disk.

## File Storage Rules — EXACT PATHS (no deviation)

The learning system uses three separate directories. Each directory has ONE purpose:

| Directory | Stores | Allowed fields |
|---|---|---|
| `~/.claude/learning/plans/` | Learning plans ONLY | topic, slug, created, level, goal, depth, timeCommitment, modules, totalEstimatedTime, diagnostic |
| `~/.claude/learning/progress/` | Quiz progress ONLY | topic, quizzes, weakAreas, strongAreas, overallScore, spacedRepetition |
| `~/.claude/learning/` (root) | index.json + profile.json ONLY | topics (index), learningStyle/background/createdTopics (profile) |

CORRECT — saving a learning plan:    `~/.claude/learning/plans/dns-2026-03-29.json`
WRONG — saving a learning plan:      `~/.claude/learning/progress/dns.json`

CORRECT — saving quiz progress:      `~/.claude/learning/progress/dns.json`
WRONG — saving quiz progress:        `~/.claude/learning/plans/dns-2026-03-29.json`

CORRECT — saving any learning data: `~/.claude/learning/plans/dns-2026-03-29.json`
WRONG — saving to project directory: `./learning/plans/dns-2026-03-29.json`

Always use the ABSOLUTE path `~/.claude/learning/` — never a relative path like `./learning/`.
Never add quiz fields (quizzes, weakAreas, strongAreas, spacedRepetition, overallScore) to plan files.
Never add plan fields (modules, resources, goal, depth, timeCommitment) to progress files.
Verify the path is correct BEFORE writing.

## Process

### Check for Existing Topic

Before starting a new plan, check if this topic already exists.

Read `~/.claude/learning/index.json` and look for a matching topic (fuzzy match same as quiz skill: "k8s" → "kubernetes").

**If the topic exists:**
1. Read the plan file and progress file
2. Show a brief status:

```
── Resuming: [Topic] ────────────────────
Level: [level] | Modules: [completed]/[total] | Score: [score]%
Last activity: [date]
──────────────────────────────────────────
```

3. Determine the next action:
   - If no quizzes taken on any module: "Ready to start learning? I'll teach you Module 1: [title]"
   - If some modules quizzed: "You left off at Module [N]: [title]. Continue?"
   - If all modules quizzed with score >80%: "You've completed this topic! Want to retake quizzes on weak areas, or adjust the plan?"
4. If user wants to continue, teach the next incomplete module interactively (see Phase 5: Teach)
5. If user wants to adjust, load the existing plan and let them modify it

**If the topic is new:** proceed to Phase 0 (profile) and Phase 1 (scope).

### Phase 0: Load or Create Learner Profile

Read `~/.claude/learning/profile.json` if it exists.

**If profile exists:**
- Greet the user by acknowledging their learning style and background
- Skip questions about learning style and background in Phase 1 — you already know
- Still ask topic-specific questions (level, goal, focus areas)

**If no profile exists (first time):**
- During Phase 1, include the learning style question (see Phase 1 examples)
- After Phase 1, save the profile as JSON to `~/.claude/learning/profile.json` (create directory if needed):
  - `learningStyle`: the user's choice (e.g., "hands-on")
  - `background`: extracted from level + goal answers
  - `createdTopics`: array with the current topic slug

**If profile exists and this is a new topic:**
- Append the topic slug to `createdTopics` array

### Phase 1: Clarify Scope

**ALWAYS** use the `AskUserQuestion` tool when asking the user questions, in any context. If you have too many questions for the tool, split them up into multiple calls.

Ask 2-5 clarifying questions, skipping any already answered by the user's initial message.

**Rules:**
- Ask ONE question per message — wait for the answer before asking the next
- Use multiple choice with clear options and descriptions for every question
- Only one question per message — never combine questions
- Ask at least 2 (level + goal) — cap at 5
- If a learner profile exists, skip the learning style question

**Question 1 — Current level:**

Ask "What's your current experience with [topic]?" with options:
- No experience — Complete beginner, starting from scratch
- Some basics — Familiar with core ideas but not hands-on
- Intermediate — Working knowledge, want to go deeper
- Advanced — Strong foundation, want expert-level depth

**Question 2 — Learning goal:**

Ask "What do you want to be able to do after learning [topic]?" with 3 topic-specific goal options. Each option needs a label and a description.

**Question 3 — Depth** (optional):

Ask "How deep do you want to go?" with options:
- High-level overview — Understand the big picture and key concepts
- Working knowledge — Enough to use it confidently day-to-day
- Deep expertise — Thorough understanding including edge cases

**Question 4 — Focus areas** (optional):

Ask which areas to focus on. Allow selecting multiple from 2-4 topic-specific subtopics, each with a label and description.

**Question 5 — Time commitment** (optional):

Ask "How much time do you want to invest?" with options:
- A few hours — Quick introduction to the basics
- A weekend — Solid foundation with practice
- A week — In-depth study with projects
- Ongoing study — Long-term learning commitment

**If no learner profile exists**, also ask "How do you prefer to learn?" with options:
- Reading docs & articles — Text-based, self-paced learning
- Watching videos — Visual explanations and walkthroughs
- Hands-on projects — Learn by building and experimenting
- Theory first — Understand principles, then apply them

### Phase 1.5: Diagnostic Assessment (non-beginners only)

Skip this phase if the user said they have "no experience" or are a "complete beginner."

For users with some background, generate a 5-question diagnostic quiz to calibrate their actual level. This prevents wasting time on material they already know.

**How to run the diagnostic:**

Generate 5 multiple choice questions testing foundational concepts at increasing difficulty. Ask ONE question per message — wait for the answer before the next.

- Questions 1-2: Basic terminology and concepts (should be easy for anyone with "some basics")
- Questions 3-4: Intermediate understanding (application of concepts)
- Question 5: Advanced concept (only experts get this right)

Each question should have 4 options with descriptions. Label them "Diagnostic Q1/5" through "Q5/5".

After the diagnostic, note which level the user actually tested at:
- 0-1 correct: Suggest starting from beginner despite their self-assessment
- 2-3 correct: Confirmed intermediate — can skip introductory modules
- 4-5 correct: Confirmed advanced — compress fundamentals, focus on depth

Store the diagnostic results in the plan JSON by adding a `diagnostic` field:

```json
{
  "diagnostic": {
    "taken": true,
    "score": 3,
    "total": 5,
    "calibratedLevel": "intermediate",
    "skipModules": []
  }
}
```

Use these results in Phase 3 (Generate Learning Plan) to mark introductory modules as "skippable" or compress them into a quick review.

### Phase 2: Research

Perform **3-5 web searches** with varied queries:

1. `"[topic] learning roadmap [year]"` — find structured learning paths
2. `"best [topic] tutorial for [level]"` — find recommended resources
3. `"[topic] official documentation"` — find authoritative sources
4. `"[topic] [specific subtopic] guide"` — drill into focus areas
5. `"[topic] common mistakes beginners"` — anticipate pitfalls

For each search:
- Use the WebSearch tool
- Fetch the top 2-3 results with WebFetch
- Extract: key concepts, recommended order, good resources, common learning paths

**Synthesize** the research into a coherent structure. Don't just list links — understand what the community recommends and why.

### Phase 3: Generate Learning Plan

Create a structured plan with modules. Present it to the user in readable markdown:

```
## Learning Plan: [Topic]

**Level:** [beginner/intermediate/advanced]
**Goal:** [user's goal]
**Estimated time:** [total]

### Module 1: [Title]
**Time:** [estimate]
**Objectives:**
- [what the user will understand/be able to do]

**Key concepts:** [list]

**Resources:**
- [resource with link and type]

### Module 2: [Title]
...
```

**Rules:**
- 3-8 modules depending on topic depth
- Each module should be completable in one sitting
- Order modules from foundational to advanced
- Include a mix of resource types per module (docs, videos, tutorials, books)
- Note free vs paid resources
- Every module MUST have `keyConcepts` with at least 2 concept strings — the quiz system uses these to generate questions. A module with empty keyConcepts is broken.
- If a diagnostic was taken, mark modules covering concepts the user already knows as "Review (optional)" instead of required

Ask the user: "Does this plan look good? Want to adjust anything — add, remove, or reorder modules?"

### Phase 4: Save

After user approves the plan:

1. **Construct path**: `~/.claude/learning/plans/{topic-slug}-{YYYY-MM-DD}.json`
2. **Verify path** contains `/plans/` — NOT `/progress/`
3. **Create directory** `~/.claude/learning/plans/` if it doesn't exist (use Bash: `mkdir -p`)
4. **Save plan** as JSON to that path — use ONLY the fields listed below:

The JSON format:

```json
{
  "topic": "Topic Name",
  "slug": "topic-name",
  "created": "YYYY-MM-DD",
  "level": "beginner|intermediate|advanced",
  "goal": "user's stated goal",
  "depth": "overview|working-knowledge|deep",
  "timeCommitment": "a few hours|a weekend|a week|ongoing",
  "modules": [
    {
      "id": 1,
      "title": "Module Title",
      "objectives": ["objective 1", "objective 2"],
      "keyConcepts": ["concept1", "concept2"],
      "estimatedTime": "2 hours",
      "resources": [
        {
          "title": "Resource Name",
          "url": "https://...",
          "type": "docs|video|tutorial|book|course",
          "free": true
        }
      ]
    }
  ],
  "totalEstimatedTime": "15 hours"
}
```

3. **Update index** at `~/.claude/learning/index.json`:
   - **Read the existing file first** — do not overwrite other topics
   - If the file doesn't exist, create `{"topics":{}}`
   - Add/update ONLY this topic's entry (preserve all other topics):

```json
{
  "displayName": "Topic Name",
  "planFile": "plans/topic-name-2026-03-01.json",
  "progressFile": "progress/topic-name.json",
  "created": "2026-03-01",
  "lastActivity": "2026-03-01",
  "level": "beginner",
  "modulesCompleted": 0,
  "modulesTotal": 5,
  "quizzesTaken": 0,
  "overallScore": null
}
```

4. **Update profile** at `~/.claude/learning/profile.json`:
   - Read existing profile (or create `{}` if missing)
   - Set `learningStyle` if determined in Phase 1
   - Set `background` from the level
   - Append the topic slug to `createdTopics` array (if not already present)

5. **Confirm** to the user: "Learning plan saved! You can now use `/quiz [topic]` to test your knowledge, or `/resources [topic]` to see all resources."

### Phase 5: Teach (optional)

After saving the plan (or when resuming an existing topic), offer to teach the next incomplete module.

Ask: "Ready to start Module [N]: [title]? I can walk you through it now, or you can study on your own and come back for a quiz."

**If the user wants to be taught:**

Teach the module interactively. The goal is genuine understanding, not information dumping.

**Teaching structure for each module:**

1. **Connect to prior knowledge** — "In the last module you learned [X]. [Topic] builds on that by..." If this is Module 1 or you don't know the user's background, connect to general knowledge or the user's stated goals.

2. **Explain core concepts** — Cover each key concept from the module's `keyConcepts` list. For each concept:
   - Give a clear, concise explanation (2-3 paragraphs max)
   - Use an analogy that connects to something the user likely knows
   - Provide a concrete example
   - If the learner profile says "hands-on", emphasize examples and exercises
   - If "theory-first", lead with principles before examples

3. **Check understanding** — After every 2-3 concepts, ask a quick multiple choice comprehension question. This isn't a quiz — it's a "does this make sense?" check. If the user gets it wrong, re-explain differently before moving on.

4. **Reference resources** — Point to specific resources from the module: "For a deeper dive on this, check out [Resource Title] — it covers [specific aspect]."

5. **Summarize** — At the end of the module, recap the 3-5 key takeaways.

6. **Bridge to next** — "Next up is Module [N+1]: [title], which builds on [concept] you just learned."

7. **Suggest quiz** — "Want to test what you've learned? Run `/quiz [topic]` (and mention the module you just covered) to check your understanding."

**Teaching guidelines:**
- Keep explanations conversational, not textbook-like
- Never go more than 3-4 paragraphs without an interaction point
- If the user seems to be struggling (wrong answers on comprehension checks), slow down and add more examples
- If the user is breezing through, pick up the pace and add depth
- Use the learner profile's learning style to adapt your approach

**If the user declines teaching:**
- Suggest: "No problem! Study at your own pace using the resources in the plan. When you're ready, run `/quiz [topic]` to test your knowledge."

## Topic Slug Convention

Convert topic to kebab-case for filenames: "Kubernetes Networking" → "kubernetes-networking", "Spanish Grammar" → "spanish-grammar". Use lowercase, replace spaces with hyphens, remove special characters.


## 文件 skills/quiz/SKILL.md

---
name: quiz
description: Use when user wants to be tested or quizzed on any topic. Triggers on "quiz me", "test me", "test my knowledge", "practice questions", "check my understanding", or when asking for a quiz on something they've been learning. Also use when user finishes a learning module and wants to check understanding. Works with or without a prior learning plan.
---

# Quiz — Interactive Knowledge Testing

**ALWAYS** use the `AskUserQuestion` tool when asking the user questions, in any context. If you have too many questions for the tool, split them up into multiple calls.

Generate and deliver mixed-format quiz questions based on the user's learning plan. Ask one question at a time, give immediate feedback, track scores, and adapt difficulty based on prior performance.

## File Storage Rules — EXACT PATHS (no deviation)

Quiz progress is saved to ONE specific directory:

    ~/.claude/learning/progress/{topic-slug}.json

CORRECT path for quiz progress: `~/.claude/learning/progress/dns.json`
WRONG path for quiz progress:   `~/.claude/learning/plans/dns-2026-03-29.json`

CORRECT — saving any learning data: `~/.claude/learning/progress/dns.json`
WRONG — saving to project directory: `./learning/progress/dns.json`

Always use the ABSOLUTE path `~/.claude/learning/` — never a relative path like `./learning/`.
Never write quiz data (quizzes, weakAreas, strongAreas, spacedRepetition, overallScore) to plan files.
Never add extra fields beyond those defined in Step 6's schema.
Verify the path contains `/progress/` before writing.

## Process

### Step 1: Determine Topic & Module

**If the user specified a topic** (e.g., `/quiz kubernetes`):
- Read `~/.claude/learning/index.json`
- Find matching topic (fuzzy match: "k8s" → "kubernetes", "Spanish" → "spanish-grammar")
- If ambiguous, ask the user to clarify

**If no topic specified** (just `/quiz`):
- Read index.json, find topic with most recent `lastActivity`
- Confirm with user: "Quiz you on [topic]?"

**If no learning plans exist:**
- Tell the user: "No learning plans found. Use /learn <topic> to create one first, or tell me a topic and I'll quiz you on general knowledge."
- If user provides a topic without a plan, generate questions from Claude's knowledge (no plan file needed)

**Module targeting:**
- If user says "test me on module 2" or "quiz me on deployments", target that specific module
- Otherwise, quiz across all modules, weighting toward weak areas if prior quiz data exists

### Step 2: Load Prior Performance

You MUST read `~/.claude/learning/progress/[topic-slug].json` before generating questions. This file contains quiz history, weak/strong areas, and spaced repetition schedules. If you skip this step, the quiz won't adapt to the user's level.

**Adaptive difficulty — mention your adjustments to the user:**
- No prior data → generate questions at the plan's level
- Prior overall score > 80% → tell the user "Your score is high, so I'm asking harder, more conceptual questions" and increase difficulty
- Prior overall score < 50% → tell the user "Let's focus on the fundamentals" and decrease difficulty
- Weight questions toward `weakAreas` from prior quizzes
- If `spacedRepetition` data exists, check for concepts where `nextReview` is today or in the past. These are overdue for review — tell the user "You have N concepts due for review" and include them in the quiz

### Step 3: Generate Questions

Generate a set of questions (default: 5, user can request more/fewer).

**Mix of formats:**

| Format | Use for | Proportion |
|---|---|---|
| **Multiple choice** (4 options, one correct) | Factual recall, terminology, definitions | ~40% |
| **True/False** | Common misconceptions, nuanced distinctions | ~20% |
| **Short answer** (1-3 sentences) | Conceptual understanding, explanations | ~25% |
| **Fill-in-the-blank** | Syntax, commands, formulas, key terms | ~15% |

**Question quality rules:**
- Questions should test understanding, not trick the user
- Wrong MCQ options should be plausible (common misconceptions), not obviously wrong
- Short answer questions should have clear evaluation criteria (key concepts to look for)
- Each question should map to a specific concept from the learning plan

### Step 4: Deliver Interactively

Ask ONE question per message. Use multiple choice with clear options and descriptions for every question. Wait for the user's answer before proceeding to the next.

**Question format examples:**

Multiple choice — "Q1/5 (Multiple Choice) — Which Kubernetes object ensures a specified number of pod replicas are running?" with 4 options, each with a short description.

True/False — "Q2/5 (True or False) — In TCP, the receiver sends acknowledgments for every individual packet." with True/False options, each with a clarifying description.

Fill-in-the-blank — "Q3/5 (Fill in the Blank) — The kubectl command to view all running pods is: kubectl _____ pods -n <namespace>" with 4 options.

Short answer — "Q4/5 (Short Answer) — Explain the difference between a Pod and a Deployment. Pick the closest answer." with 2-3 options plus "Other (None of these match my understanding)".

**After the user answers, give feedback:**

If correct:
> Correct! [1-2 sentence explanation reinforcing the concept]

If incorrect:
> Not quite. The answer is [correct answer]. [2-3 sentence explanation helping the user understand]

For short answers, evaluate for key concepts, not exact wording. If partially correct, say what they got right and what's missing. Be encouraging but honest.

Then immediately ask the next question — no extra text between feedback and the next question.

### Step 5: Show Results

After all questions, present a summary:

```
── Results: [Topic] ──────────────────────
Score: [correct]/[total] ([percentage]%)

[For each question:]
[✓/✗] Q[n]: [brief concept label]

[If there are wrong answers:]
Weak areas: [list concepts that need review]
Suggestion: [specific actionable advice]
──────────────────────────────────────────
```

### Step 6: Save Progress

The progress file at `~/.claude/learning/progress/{topic-slug}.json` is the **single source of truth** for quiz data. The web dashboard also reads and writes this file. Always read the existing file first, then append/update — never overwrite from scratch.

1. **Construct path**: `~/.claude/learning/progress/{topic-slug}.json`
2. **Verify path** contains `/progress/` — NOT `/plans/`
3. **Create directory** `~/.claude/learning/progress/` if it doesn't exist
4. **Read the existing file** — if it exists, load its current data and append to it. If it doesn't exist, create a new object
5. **Append** the new quiz to the `quizzes` array (do not replace existing quizzes)
6. **Recompute** `weakAreas`, `strongAreas`, and `overallScore` from ALL quizzes (not just the latest)
7. **Update** `spacedRepetition` for each concept tested
8. **Write** the file using ONLY the fields listed below — no extra fields:

```json
{
  "topic": "topic-slug",
  "quizzes": [
    {
      "date": "YYYY-MM-DD",
      "module": null,
      "score": 4,
      "total": 5,
      "difficulty": "beginner",
      "questions": [
        {
          "format": "mcq",
          "concept": "concept-label",
          "correct": true
        }
      ]
    }
  ],
  "weakAreas": ["concept-a", "concept-b"],
  "strongAreas": ["concept-c", "concept-d"],
  "overallScore": 80
}
```

**CRITICAL format rules — the web dashboard reads these files, so the format must be exact:**

- `overallScore` is a percentage (0-100), NOT a fraction. `80` not `0.8`.
- `weakAreas` and `strongAreas` are arrays of **strings** (concept names), NOT objects.
  - CORRECT: `"weakAreas": ["DNS resolution", "CNAME records"]`
  - WRONG: `"weakAreas": [{"concept": "DNS resolution", "moduleId": 1}]`
- `spacedRepetition` keys must be **concept names** (matching the `concept` field in questions), NOT module IDs.
  - CORRECT: `"spacedRepetition": {"DNS resolution": {...}}`
  - WRONG: `"spacedRepetition": {"1": {...}, "2": {...}}`
- All `spacedRepetition` values must have `easeFactor` (number), `intervalDays` (integer), `nextReview` (YYYY-MM-DD string), `repetitions` (integer). None can be null.

**Compute weak/strong areas (aggregate across ALL quizzes):**
- For each concept that has ever appeared in any quiz question, count total attempts and correct answers
- Concepts correct in <50% of attempts → `weakAreas` (as plain strings)
- Concepts correct in >=80% of attempts → `strongAreas` (as plain strings)
- `overallScore` = round(total correct across all quizzes / total questions across all quizzes × 100)

**Update spaced repetition schedule:**

For each concept tested in this quiz, update the `spacedRepetition` field in the progress file using the SM-2 algorithm:

**For each concept:**
1. Determine quality score (0-5): correct on first try = 5, correct after hesitation = 4, incorrect but close = 2, incorrect = 0
2. If quality >= 3 (correct):
   - If first review (`repetitions` was 0): `intervalDays` = 1
   - If second review (`repetitions` was 1): `intervalDays` = 6
   - Subsequent: `intervalDays` = round(previous interval × `easeFactor`)
   - `repetitions` += 1
3. If quality < 3 (incorrect):
   - Reset: `intervalDays` = 1, `repetitions` = 0
4. Update ease factor: `easeFactor` = max(1.3, easeFactor + 0.1 - (5 - quality) × (0.08 + (5 - quality) × 0.02))
5. Compute `nextReview` = today + `intervalDays` (format: YYYY-MM-DD)

For new concepts (not yet in `spacedRepetition`), initialize with `easeFactor: 2.5`, `intervalDays: 1`, `repetitions: 0`, `nextReview: today + 1 day`.

**Validation before writing:** Every SR entry must have all 4 fields set to non-null values. If any field would be null, use the default: `easeFactor: 2.5`, `intervalDays: 1`, `repetitions: 0`, `nextReview: tomorrow`.

**Updated progress JSON structure:**

```json
{
  "topic": "topic-slug",
  "quizzes": [...],
  "weakAreas": [...],
  "strongAreas": [...],
  "overallScore": 80,
  "spacedRepetition": {
    "concept-label": {
      "easeFactor": 2.5,
      "intervalDays": 6,
      "nextReview": "2026-03-26",
      "repetitions": 2
    }
  }
}
```

This is backwards-compatible — if `spacedRepetition` is missing, treat all concepts as unscheduled.

9. **Update index.json** at `~/.claude/learning/index.json`:
   - Read existing index first
   - Set `topics[slug].quizzesTaken` = total number of quizzes in the progress file
   - Set `topics[slug].overallScore` = the computed overallScore (percentage, 0-100)
   - Set `topics[slug].lastActivity` = today's date (YYYY-MM-DD)

## No-Plan Quiz Mode

If a user asks to be quizzed on a topic with no existing learning plan:
- Generate questions from Claude's own knowledge
- Still deliver interactively with feedback
- Still save progress to enable tracking
- Suggest: "Want me to create a full learning plan for this topic? Use /learn [topic]"


## 文件 skills/resources/SKILL.md

---
name: resources
description: Use when user asks for learning resources, recommendations, or materials on any topic. Triggers on "find me resources", "what should I read about", "best tutorials for", "recommend a book on", "good courses for", "where can I learn more about", "any videos on", or any request for curated study materials. Also use when user wants to browse what's available before committing to a full learning plan — this skill works with or without an existing plan.
---

# Resources — Curated Learning Materials

**ALWAYS** use the `AskUserQuestion` tool when asking the user questions, in any context. If you have too many questions for the tool, split them up into multiple calls.

## Overview

Provide curated external resources for a topic, either from an existing learning plan or via fresh web research. Group by type, note free vs paid, and organize by module when a plan exists.

## Data Schemas

The resources skill reads data written by the learn skill. Here are the formats:

**index.json** (`~/.claude/learning/index.json`) — look up `topics[slug].planFile` to find the plan path.

**Plan files** (`~/.claude/learning/plans/<slug>-<date>.json`) — contain `modules[]`, each with `resources[]` where each resource has `title`, `url`, `type` (docs|video|tutorial|book|course), and `free` (boolean).

## Process

### Step 1: Check for Existing Plan

Read `~/.claude/learning/index.json` and look for the requested topic.

**If a plan exists:**
- Read the plan JSON from `~/.claude/learning/plans/[file]`
- Extract all resources organized by module
- Present them grouped by type within each module

**If no plan exists:**
- Perform fresh web research (3-5 searches, same as the learn skill's research phase)
- Curate and present results

### Step 2: Present Resources

**With existing plan — organize by module:**

```
── Resources: [Topic] ────────────────────────────

### Module 1: [Title]

📖 Documentation
  • [Title] — [url]
    [one-line description if helpful]

🎥 Videos & Courses
  • [Title] — [url] (free|$paid)

📝 Tutorials
  • [Title] — [url]

📚 Books
  • [Title] — [author] (free|$paid)

### Module 2: [Title]
...
──────────────────────────────────────────────────
```

**Without plan — organize by type:**

```
── Resources: [Topic] ────────────────────────────

📖 Official Documentation
  • ...

🎥 Video Courses
  • ...

📝 Tutorials & Articles
  • ...

📚 Books
  • ...

💡 Tip: Use /learn [topic] to create a structured learning
   plan that organizes these resources into modules.
──────────────────────────────────────────────────
```

### Resource Quality Rules

- Prefer official documentation and well-known sources
- Always note free vs paid
- Include a mix of formats (not all videos, not all text)
- For subtopic-specific requests, focus resources narrowly
- If resources from the plan are stale or broken, supplement with fresh search


## 文件 skills/review/SKILL.md

---
name: review
description: Use when user asks about their learning progress or wants study guidance. Triggers on "how am I doing", "my progress", "what should I study next", "show my scores", "what are my weak areas", "review my learning", "how well do I know X", or any request to see quiz results, track improvement, or decide what to focus on next. Also use when the user seems unsure what to study — this skill provides data-driven recommendations.
---

# Review — Learning Progress Dashboard

**ALWAYS** use the `AskUserQuestion` tool when asking the user questions, in any context. If you have too many questions for the tool, split them up into multiple calls.

## Overview

Show the user their learning progress across all topics or for a specific topic. Display quiz scores, module completion, weak areas, score trends, and actionable next steps.

## Data Schemas

The review skill reads data written by the learn and quiz skills. Here are the formats you'll encounter:

**index.json** (`~/.claude/learning/index.json`) — master registry:
```json
{
  "topics": {
    "topic-slug": {
      "displayName": "Topic Name",
      "planFile": "plans/topic-slug-2026-03-01.json",
      "progressFile": "progress/topic-slug.json",
      "created": "2026-03-01",
      "lastActivity": "2026-03-01",
      "level": "beginner",
      "modulesCompleted": 0,
      "modulesTotal": 5,
      "quizzesTaken": 1,
      "overallScore": 0.8
    }
  }
}
```

**Plan files** (`~/.claude/learning/plans/<slug>-<date>.json`) — contain `modules[]` with `id`, `title`, `objectives`, `keyConcepts`, `estimatedTime`, `resources[]`.

**Progress files** (`~/.claude/learning/progress/<slug>.json`) — contain `quizzes[]` (each with `date`, `module`, `score`, `total`, `questions[]`), `weakAreas[]`, `strongAreas[]`, `overallScore` (percentage 0-100, not fraction).

Progress files now also contain `spacedRepetition` — a map of concept labels to SM-2 scheduling data (`easeFactor`, `intervalDays`, `nextReview`, `repetitions`). Concepts with `nextReview` at or before today are due for review.

## Process

### Step 1: Load Data

Read `~/.claude/learning/index.json`.

**If file doesn't exist or is empty:**
- Tell the user: "No learning data found yet. Use /learn <topic> to start your first topic!"
- Stop here.

**If user specified a topic** (e.g., `/review kubernetes`):
- Load that topic's plan and progress files
- Show detailed single-topic view

**If no topic specified:**
- Load all topics from index
- Show overview of all topics

### Step 2: Display Progress

**All-topics overview format:**

```
── Learning Progress ─────────────────────────────

[Topic Name] (started [date])
  Module 1: [Title]    [progress bar] [score]%  ([N] quizzes)
  Module 2: [Title]    [progress bar] not started
  ...
  Weak areas: [list]
  Next step: [actionable suggestion]

[Topic Name 2] ...

── Due for Review ────────────────────────────────
  [Topic]: [N] concepts due ([list top 3 concept names])
  [Topic 2]: [N] concepts due ([list top 3])

  Run /quiz [topic] to review these concepts.
──────────────────────────────────────────────────

── Summary ───────────────────────────────────────
  Active topics: [N]
  Total quizzes taken: [N]
  Average score: [N]%
  Suggested focus: [topic — reason]
──────────────────────────────────────────────────
```

**Due for review section:**

If any concepts have `nextReview` at or before today across any topic, show the "Due for Review" block between the per-topic details and the Summary (as shown above). If no concepts are due, omit this block entirely.

**Progress bar rendering:**
- Use Unicode block characters: `█` for filled, `░` for empty
- 10 characters wide
- Based on quiz scores for that module (no quizzes = all empty)

**Single-topic detailed format:**
- Show all modules with per-module quiz history
- Show score trend if multiple quizzes (e.g., "Module 1: 60% → 75% → 90%")
- List all weak and strong areas
- Show total time estimated vs modules completed
- Suggest specific module to focus on next

### Step 3: Recommend Next Action

Always end with one clear, actionable suggestion:

- If concepts are due for review (nextReview <= today): "You have [N] concepts due for review in [topic]. Run `/quiz [topic]` to keep them fresh — spaced repetition works best when you review on schedule."
- If a topic has weak areas: "Retake the quiz on [topic] focusing on [weak area]. Use `/quiz [topic]`"
- If a module is unstarted: "Start Module [N]: [title]. Check `/resources [topic]` for study materials"
- If all modules are strong: "Great work on [topic]! Consider exploring a related topic or increasing the difficulty"
- If multiple topics exist: prioritize the one with lowest score or most staleness

