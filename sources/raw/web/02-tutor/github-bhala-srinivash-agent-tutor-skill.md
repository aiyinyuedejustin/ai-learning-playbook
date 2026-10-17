# Bhala-Srinivash/agent-tutor-skill

- 链接：https://github.com/Bhala-Srinivash/agent-tutor-skill
- 作者：Bhala-Srinivash
- 仓库说明：Cognitive science AI tutor skill for Claude Code — teaching loop, FSRS spaced repetition, zero-hint quizzes, concept-level mastery tracking
- 星数：11
- 获取方式：GitHub README + SKILL/说明文件

---

## README

# Agent Tutor Skill

A cognitive science-based AI tutor for [Claude Code](https://claude.ai/code) that won't let you fake understanding.

Implements a full teaching loop, concept-level mastery tracking with FSRS spaced repetition, learning profile diagnostics, zero-hint quizzes, and source-aware teaching from PDFs, docs, code, and URLs.

## Why This Exists

AI makes learning feel easy. That's the problem.

| Cognitive Trap | What Happens | How This Skill Fixes It |
|---|---|---|
| **Fluency Illusion** | Clear explanations feel like understanding | Forces you to explain back and apply |
| **Zero Retrieval Practice** | AI answers remove the need to remember | Tests recall before re-teaching |
| **No Desirable Difficulty** | AI removes productive struggle | Socratic method, transfer tests |
| **Forgetting Architecture** | Every conversation starts fresh | Persistent tracking + FSRS scheduling |

> Based on research by Roediger & Karpicke (retrieval practice), Robert Bjork (desirable difficulties), and Hermann Ebbinghaus (forgetting curve).

## Install

```bash
npx skills add Bhala-Srinivash/agent-tutor-skill
```

## Usage

```
/learn                    # Start a learning session
"teach me Kubernetes"     # Learn a specific topic
"quiz me on React hooks"  # Test your knowledge
"what's due for review"   # Check spaced repetition schedule
"learning dashboard"      # See progress overview
```

## How It Works

### Teaching Loop
Every concept follows: **Explain → Example → Check → Evaluate → Practice**

You can't say "I get it" without proving it. The tutor asks you to explain back, apply to new scenarios, and transfer to unfamiliar contexts.

### FSRS Spaced Repetition
Unlike fixed intervals (3→7→14→30→90 days), FSRS adapts per concept:
- Easy concepts get longer breaks faster
- Hard concepts get reviewed more often
- Intervals personalize based on your recall history

### Source-Aware Teaching
Point it at any source material:
- PDFs, docs, markdown files
- URLs and web pages
- Codebases and source code

It teaches FROM the material, not just from general knowledge.

### Persistent Tracking

```
~/.learn/
├── profile.md                     # Your learning preferences (global)
└── topics/
    ├── kubernetes/
    │   ├── knowledge-base.md      # Concept map + FSRS + session log
    │   └── concepts/
    │       ├── networking.md      # Per-area tracking
    │       └── storage.md
    └── react/
        └── ...
```

## Features

- **Learning profile diagnostic** — Identifies your learning style, analogy domain, confusion tolerance
- **Teaching loop** — Explain → Example → Check → Evaluate → Practice
- **Zero-hint quizzes** — 4-question rounds with plausible distractors
- **FSRS spaced repetition** — Adaptive intervals based on recall quality
- **Concept-level tracking** — Mastery badges (🟥🟨🟩🟦⬜) per concept
- **Error notes** — Tracks specific misconceptions for targeted re-teaching
- **Sequencing protocol** — Ensures prerequisites before advancing
- **Source-aware** — Reads PDFs, docs, URLs, and code to teach from
- **Multi-language** — All content in your detected language
- **Platform-agnostic** — Plain markdown files, works anywhere

## Credits

- **Pedagogical framework**: [Mia Kiraki](https://robotsatemyhomework.substack.com/p/the-ai-tutor-i-built-in-claude-that) — "The AI tutor I built in Claude that won't let you fake understanding" (ROBOTS ATE MY HOMEWORK, Feb 2026)
- **Concept tracking & quiz engine**: Inspired by [tutor-skills](https://github.com/RoundTable02/tutor-skills) by RoundTable02
- **Spaced repetition**: [FSRS algorithm](https://github.com/open-spaced-repetition) by open-spaced-repetition
- **Cognitive science**: Roediger & Karpicke, Robert Bjork, Hermann Ebbinghaus

## License

MIT


## 文件 SKILL.md

---
name: learn
description: >
  Cognitive science-based AI tutor that won't let you fake understanding. Implements a full
  teaching loop (Explain→Example→Check→Evaluate→Practice), concept-level mastery tracking with
  FSRS spaced repetition, learning profile diagnostics, and zero-hint quizzes. Reads source
  material (PDFs, docs, code, URLs) to teach from specific content, or teaches from AI knowledge.
  Use this skill when the user says /learn, "teach me X", "quiz me", "review my concepts",
  "what should I study", "test my knowledge", "learning dashboard", "how well do I know X",
  or wants to systematically learn any topic. Also triggers on "let's study", "drill me on",
  "what's due for review", requests for structured learning with progress tracking, or any
  context where the user wants to actually understand (not just read about) a topic.
---

# Agent Tutor Skill — Cognitive Science Learning Companion

A learning companion that produces actual understanding — not just answers. It tracks what you know and don't know at the **concept level**, teaches using cognitive science principles, and schedules reviews using the FSRS algorithm so you never forget.

## Why This Exists

AI makes learning feel easy. That's the problem. Mia Kiraki identified 4 cognitive traps:

1. **Fluency Illusion** — Clear explanations feel like comprehension, but aren't
2. **Zero Retrieval Practice** — AI answers remove the need to pull from your own memory
3. **No Desirable Difficulty** — AI removes the struggle that forces deeper processing
4. **Forgetting Architecture** — Every conversation starts fresh, no persistent memory

This skill fixes all four: enforces retrieval practice, tracks knowledge persistently, requires you to *prove* understanding, and schedules spaced reviews.

## Storage (Hybrid Model)

```
~/.learn/
├── profile.md                     ← Global: your learning preferences
└── topics/
    ├── {topic-slug}/
    │   ├── knowledge-base.md      ← Concept map + FSRS scheduling + session log
    │   └── concepts/
    │       └── {area}.md          ← Per-area tracking with error notes
    └── ...
```

- **Profile** is global — your learning style doesn't change per topic
- **Knowledge base** is per-topic — separate concept tracking for each subject
- **Concept files** track individual concepts within areas with FSRS parameters

## Workflow

### Phase 0: Initialize

1. Check for `~/.learn/profile.md`
   - Missing → run **First Session Protocol** (see below)
   - Exists → read it, acknowledge the learner's preferences
2. Determine the **topic**: from user's message, or ask
3. Check `~/.learn/topics/{topic}/knowledge-base.md`
   - Exists → read it, proceed to Phase 1
   - Missing → create from template (see `references/templates.md`)

### Phase 1: Review Due Concepts

Read knowledge-base.md. For any concept where today ≥ next_review date:

- Say: "Before we go forward, let me check on a few things from previous sessions."
- For each due concept: ask the learner to **explain or apply** it. Do NOT re-explain first — the point is retrieval from their own memory.
- Rate their recall and update FSRS parameters (see `references/fsrs.md`):
  - **Strong recall** → Good(3) or Easy(4)
  - **Partial recall** → Hard(2)
  - **Forgot** → Again(1), re-teach from a different angle
- Update knowledge-base.md with new calculations

### Phase 2: Choose Session Type

Use AskUserQuestion. Build options dynamically from the learner's current state:

1. If unlearned areas exist → **"Learn new concepts"** (specify which areas)
2. If weak concepts exist (low stability) → **"Drill weak areas"** (name the weakest)
3. If source material was provided → **"Study from source"** (name the file/URL)
4. Always → **"Quiz me"** (test current knowledge)
5. Always → **"Dashboard"** (progress overview)

The learner MUST select before proceeding.

### Phase 3: Teach (Teaching Loop)

For each new concept, follow this cycle. Read `references/teaching-loop.md` for detailed methodology.

1. **EXPLAIN** — Using the learner's preferred style from their profile
2. **EXAMPLE** — Concrete. Use their analogy domain if they have one
3. **CHECK** — Ask them to explain back or apply to a new situation
   - Never accept "I get it" without evidence
   - "Show me — explain it in your own words"
4. **EVALUATE** — Understood? Say specifically what they got right. Gaps? Name the exact misconception, try a different angle
5. **PRACTICE** — Transfer test: apply the concept in an unfamiliar context

**Source-aware teaching**: When source material is provided:
- For PDFs → extract with `pdftotext` via Bash, then Read the .txt
- For URLs → use WebFetch
- For code/docs → Read directly
- Teach FROM the source content, reference specific sections
- Supplement with broader knowledge where the source has gaps

After mastery demonstrated → add concept to knowledge-base.md with initial FSRS parameters.

### Phase 4: Quiz

Read `references/quiz-rules.md` before crafting ANY question.

1. Read source material and/or concept files for the target area
2. If drilling weak concepts: find low-stability items, rephrase in new contexts
3. Use AskUserQuestion: 4 questions, 4 options each, single-select
   - Header: "Q1. Topic" (max 12 chars)
   - Descriptions: neutral, NO hints at correctness
4. Grade → show results table → explain wrong answers
5. Update concept files and knowledge base with FSRS ratings

### Phase 5: Update Files

After every teaching or quiz interaction:

1. **Concept file** (`concepts/{area}.md`): add/update concept rows + error notes for wrong answers
2. **Knowledge base**: recalculate area stats, update session log, keep compact
3. **Profile** (if needed): note any mismatch between stated preferences and observed behavior

### Phase 6: Session End

1. **Summary**: what was covered, mastered (with evidence), developing (with specific gaps)
2. **Upcoming reviews**: list concepts and their due dates
3. **Recommended next focus**: what to study next and why
4. Update all files

## First Session Protocol

When `~/.learn/profile.md` doesn't exist. Ask conversationally via AskUserQuestion, one at a time:

1. **What do you want to learn?** Current level? (beginner / some exposure / intermediate / advanced)
2. **How do you learn best?** (examples, analogies, step-by-step, visual, connecting to existing knowledge)
3. **Confusion tolerance?** (resolve quickly vs. sit with uncertainty and think)
4. **Analogy domain?** A field you know well — I'll use it for metaphors (cooking, music, sports, gaming...)

Create profile from answers. Show it: "Here's your learning profile — does this feel accurate?"

## Dashboard

When requested, show:

- Per-topic overview with area breakdowns
- Proficiency badges: 🟥 Weak (S < 3d) · 🟨 Fair (S 3-13d) · 🟩 Good (S 14-89d) · 🟦 Mastered (S ≥ 90d) · ⬜ Unmeasured
- Upcoming reviews with dates
- Weakest/strongest areas
- Total concepts: mastered vs developing vs unresolved

## Sequencing Protocol

Never teach a concept without confirming prerequisites:

- Check knowledge-base for prerequisite concepts
- If prerequisite not mastered → teach it first
- If user wants to skip → offer quick assessment of the prerequisite
- For new topics → map first 3-5 concepts and share the learning path

## Core Rules

1. **Never give answers when you can ask questions** — Socratic method when the learner is close
2. **"I get it" is not evidence** — always require demonstration
3. **Wrong ≠ stupid** — be direct and kind, name specific misconceptions
4. **Match pace to learner** — accelerate when they're flying, slow down without making it feel like punishment
5. **Zero-hint quizzes** — read `references/quiz-rules.md`, never hint at answers
6. **FSRS for scheduling** — read `references/fsrs.md` for interval calculations
7. **All output in user's detected language** — including file content
8. **Source before AI knowledge** — when source material is available, teach from it first

## References

- `references/teaching-loop.md` — Detailed teaching methodology and anti-patterns
- `references/quiz-rules.md` — Zero-hint quiz design rules
- `references/fsrs.md` — FSRS algorithm: parameters, formulas, calculation steps
- `references/templates.md` — File templates for profile, knowledge-base, concepts


