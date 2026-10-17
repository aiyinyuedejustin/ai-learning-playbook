# distinctgrey：/learn skill（gist）

- 链接：https://gist.github.com/distinctgrey/68334b52802164ec2e673f5365e3e5ff
- 作者：distinctgrey
- 获取方式：GitHub Gist 全文

---

## 文件 SKILL.md

# Learn Skill

## Purpose

Structured self-directed learning using a 6-phase, 14-step methodology grounded in evidence-based learning science: spaced retrieval (Roediger & Karpicke, 2006), the generation effect (Slamecka & Graf, 1978), deliberate practice (Ericsson et al., 1993), interleaving (Rohrer & Taylor, 2007), elaborative interrogation (Pressley et al., 1987), and the expertise reversal effect (Kalyuga et al., 2003). Adaptive scope calibration matches study intensity to available time and motivation.

## File Structure

Each learning track lives in `personal/learning/{topic-slug}/`:

```
personal/learning/{topic-slug}/
  progress.md       # Always present. Phase status, session log, metadata.
  sources.md        # Step 2. Curated source list.
  guidebook.md      # Step 5. Synthesized reference.
  concept-map.md    # Step 8. Core concepts and debates.
  builds/           # Step 9g. Build projects and prototypes.
  artifacts/        # Step 11. Output files.
```

Only `progress.md` is created at track start. Other files appear as the track progresses.

## Session Protocol

Every `/learn` session follows this sequence:

1. **Load progress**: Read `progress.md`. Report current phase, step, last session date, and days since last session.
2. **Spaced review** (Phase 4+): Ask 2-3 retrieval questions from previous sessions before moving to new material. No notes allowed. Correct wrong answers with explanation.
3. **Work on current step**: Follow the methodology for the active step.
4. **Update progress**: Append session log entry to `progress.md`. Update step status. Note any artifacts created.
5. **Suggest timing**: Based on spacing principles, recommend when to return. Early phases: next day is fine. Phase 4: increasing intervals (1 day, 3 days, 1 week).

## Methodology: 6 Phases, 14 Steps

### Phase 0: Scope and Investment

Before creating any files, calibrate scope with the user.

| Step | Action |
|------|--------|
| 0a: Motivation | Ask WHY. What does knowing this serve? Writing? Professional use? Teaching? Curiosity? The answer shapes everything downstream. |
| 0b: Time budget | How much time available? Hours per week, total weeks. |
| 0c: Calibrate scope | Propose scope given motivation + time. User confirms or adjusts. |

**Adaptive scope classes:**

| Budget | Class | Adaptation |
|--------|-------|-----------|
| Under 5h | Quick study | Skip NotebookLM. Claude reads sources directly. Compress to essentials. Fewer sources (3-8). |
| 5-20h | Standard | Full workflow. NotebookLM optional. 3-5 deep sessions. |
| 20h+ | Deep mastery | Full workflow with NotebookLM. Extended Phase 4. Multiple artifacts. |

**Expertise reversal effect**: Beginners get direct instruction and structured overviews, not expert-level workflows. Intermediate+ learners get primary sources, contrarian takes, and more open-ended exploration.

After scope calibration, create the topic subfolder and `progress.md`.

### Phase 1: Define and Plan

| Step | Action | Learning science |
|------|--------|-----------------|
| 1: Define domain | Set topic boundaries, assess current level, define what "expert" means for this scope. Start with **historical context**: trace the subject's origin, key turning points, why it exists. Causal narratives make abstract ideas stick. | Elaborative interrogation |
| 2: Identify sources | Curate 5-20 sources in batches ordered by difficulty. Beginners: overviews, explainers, history. Intermediate+: primary sources, contrarian takes. Save to `sources.md`. | Sequencing (foundational before specialized) |

### Phase 2: Aggregate and Synthesize

| Step | Action |
|------|--------|
| 3: Build source collection | Prepare sources for NotebookLM (standard/deep mastery) or for Claude to read directly (quick study). Fetch web sources. Batch by category. |
| 4: Extract guidebook | NotebookLM for standard/deep mastery: use section-specific prompts (not one monolithic prompt). For quick study: Claude reads sources and synthesizes directly. Key lesson from agentic-ai track: section-specific prompts beat monolithic prompts. |
| 5: Restructure | Quality-check the guidebook output. Separate fact from opinion. Flag gaps. Use three registers: factual (what sources say), attributed (what specific authors argue), editorial (your own synthesis). Save as `guidebook.md`. |

### Phase 3: Build Learning Environment

| Step | Action |
|------|--------|
| 6: Set up context | For Claude.ai projects: create project with instructions. For Claude Code tracks: progress file + guidebook serve as persistent context. |
| 7: Load knowledge | Upload guidebook and supporting materials to the learning environment. |
| 8: Map territory | Identify 5-7 core concepts, 3-4 open debates, weakest areas. Save as `concept-map.md`. |

### Phase 4: Deep Learning

Iterative across multiple sessions. CC picks the right mix of theory and applied steps based on where the user is. Early sessions lean toward teach-back and retrieval. As understanding grows, the balance shifts toward applied practice, builds, and sparring.

**Rule: never let theory sessions run more than two in a row without proposing an application exercise.**

#### Theory loop

| Step | Action | Learning science |
|------|--------|-----------------|
| 9a: Teach-back | Pick a concept. User explains it as if teaching someone who knows nothing about it. CC finds gaps, pushes on vague parts, asks follow-up questions that probe understanding (not just recall). | Feynman technique + generation effect |
| 9b: Retrieval practice | CC asks questions about previous material. No notes. Wrong answers get corrected with explanation. Increasing difficulty over sessions. | Testing effect |
| 9c: Interleaved practice | Mix topics within a session. Alternate between concepts rather than blocking on one topic. | Interleaving + desirable difficulty |
| 9d: Spaced review | Each new session starts with review of previous material at increasing intervals. | Spacing effect + spaced repetition |
| 9e: Deliberate practice | CC identifies weak spots from teach-backs and retrieval. Designs targeted exercises for those specific weaknesses. | Deliberate practice (Ericsson) |

#### Applied practice loop

| Step | Action | Learning science |
|------|--------|-----------------|
| 9f: Connect to current work | CC scans writing-os folders (`/professional/`, `/voxdale-projects/`, `/writing-projects/`, `/personal/`) and `/meetings/` to find what the user is working on. CC suggests concrete exercises that apply the learning topic to real projects. Example: learning game theory? "Apply Nash equilibrium analysis to the Voxdale pricing negotiation from last week's meeting." | Transfer learning: applying knowledge to authentic contexts cements understanding |
| 9g: Build a thing | When the topic and time investment allow, CC proposes a build project: a prototype, tool, document, system, or physical artifact. CC coaches through the build as a sparring partner. Asks "what would happen if...", challenges design choices, suggests alternatives. Save artifacts to `{topic-slug}/builds/`. | Constructionism (Papert): building produces deeper learning than studying. Automaticity: hands-on repetition makes low-level skills effortless. |
| 9h: Sparring rounds | CC poses scenarios, plays devil's advocate, simulates stakeholder objections, or role-plays situations where the user must apply knowledge under pressure. CC adapts difficulty based on responses. | Desirable difficulty + deliberate practice: realistic pressure exposes gaps |

#### Summative assessment

| Step | Action | Learning science |
|------|--------|-----------------|
| 10: Feynman test | User explains the entire domain coherently. CC scores on clarity, completeness, accuracy. Identifies remaining gaps. This is the gate to Phase 5. | Bloom's two-sigma: Phase 4 simulates 1:1 tutoring via corrective feedback, guided questioning, behavioral regulation |

### Phase 5: Output and Maintain

| Step | Action |
|------|--------|
| 11: Build artifacts | Produce output matching original motivation (newsletter draft, architecture doc, presentation outline, tool). Save to `artifacts/`. |
| 12: Maintenance | Set review intervals: 1 week, 1 month, 3 months. Review sessions run quick retrieval practice. Update guidebook with new sources and insights. |

## Progress Template

When creating a new track, use this template for `progress.md`:

```markdown
# {Topic Name} - Learning Track

**Created**: {date}
**Motivation**: {from step 0a}
**Time budget**: {from step 0b}
**Scope class**: {quick-study | standard | deep-mastery}
**Target**: {what "knowing this" means for this scope}

---

## Progress

| Phase | Step | Status | Notes |
|-------|------|--------|-------|
| 0 | 0a: Motivation | Done | {brief note} |
| 0 | 0b: Time budget | Done | {hours/week x weeks} |
| 0 | 0c: Calibrate scope | Done | {scope class} |
| 1 | 1: Define domain | Pending | |
| 1 | 2: Identify sources | Pending | |
| 2 | 3: Build source collection | Pending | |
| 2 | 4: Extract guidebook | Pending | |
| 2 | 5: Restructure | Pending | |
| 3 | 6: Set up context | Pending | |
| 3 | 7: Load knowledge | Pending | |
| 3 | 8: Map territory | Pending | |
| 4 | 9: Deep learning loop | Pending | |
| 4 | 10: Feynman test | Pending | |
| 5 | 11: Build artifacts | Pending | |
| 5 | 12: Maintenance | Pending | |

---

## Session Log

### Session 1: {date}

**Phase**: 0 (Scope and Investment)
**Duration**: ~{n} min
**Steps completed**: 0a, 0b, 0c

{What happened. Decisions made. Key observations.}

**Next**: Phase 1, Step 1 (Define domain)
```

## Bloom's Two-Sigma: How This Skill Approximates 1:1 Tutoring

Bloom claimed tutored students performed 2 standard deviations above classroom students. Ricón's systematic review (nintil.com) found the real effect is ~0.79 sigma. But high-quality software tutoring can approach higher gains through three mechanisms Phase 4 implements:

1. **Corrective feedback**: CC identifies gaps in teach-backs and wrong answers in retrieval practice, then explains the correct understanding.
2. **Guided questioning**: CC asks follow-up questions that probe understanding rather than testing recall. "Why does that happen?" rather than "What is X?"
3. **Behavioral regulation**: Progress tracking tells the user what to study next. Spaced review prevents cramming. The system enforces good study habits even when motivation dips.

## Anti-Patterns to Flag

- **Passive consumption**: Reading sources without teach-back or retrieval. Push toward active engagement.
- **Comfort zone looping**: Revisiting mastered material while avoiding weak spots. Steer toward deliberate practice.
- **Theory-only sessions**: More than two theory steps without application. Propose an applied exercise.
- **Skipping spaced review**: If more than 7 days since last session, insist on retrieval practice before new material.
- **Scope creep**: Expanding beyond the original motivation/time budget without explicit recalibration.
- **Perfectionism in early phases**: Spending too long on source curation or guidebook polish. Good enough is good enough for Phase 2.


## 文件 learn.md

---
description: "Start, resume, or list learning tracks"
argument-hint: "<topic-slug> or leave blank to list all tracks"
---

Manage structured learning tracks using the methodology in `/.claude/skills/learn/SKILL.md`.

Load the skill file first: read `/.claude/skills/learn/SKILL.md` for the full methodology, session protocol, and progress template.

## Routing

### No argument provided ($ARGUMENTS is empty): LIST mode

1. Scan `personal/learning/` for:
   - **Subdirectories** containing `progress.md` (new-format tracks)
   - **Flat `.md` files** directly in the directory (legacy tracks)
2. For each new-format track:
   - Read `progress.md`
   - Extract: topic name, current phase/step, scope class, last session date
   - Count steps with status "Done" vs total steps to calculate completion %
3. For each legacy flat file:
   - Count `[x]` (completed) and `[ ]` (open) items
   - Extract topic from filename (strip `.md`, replace hyphens with spaces)
   - Mark as "legacy format"
4. Display a summary table:
   ```
   ## Learning Tracks

   | # | Track | Phase | Progress | Last Session | Format |
   |---|-------|-------|----------|-------------|--------|
   | 1 | Topic Name | Phase 4: Deep Learning | 8/14 (57%) | 2026-02-10 | new |
   | 2 | Claude Code Mastery | Week 2 | 5/16 (31%) | - | legacy |
   ```
5. Ask the user: "Resume a track (enter number), or name a new topic to start learning."

### Argument matches existing track slug: RESUME mode

1. Read `personal/learning/{slug}/progress.md`
2. Load `guidebook.md` and `concept-map.md` if they exist (for Phase 4+ context)
3. Report current position: phase, step, last session date, days since last session
4. Follow the **session protocol** from SKILL.md:
   - If Phase 4+: start with 2-3 spaced review questions
   - Work on the current step
   - Update progress.md with session log when done
   - Suggest next session timing

### Argument is a new topic: NEW mode

1. Confirm with the user: "No existing track for '{topic}'. Start a new learning track?"
2. If confirmed, begin **Phase 0: Scope and Investment** from SKILL.md:
   - Step 0a: Ask about motivation
   - Step 0b: Ask about time budget
   - Step 0c: Propose scope class, get confirmation
3. Create the directory: `personal/learning/{topic-slug}/`
4. Create `progress.md` using the template from SKILL.md, with Phase 0 steps marked Done
5. Continue to Phase 1 if the user wants to keep going, or suggest they return later

## Disambiguation

If $ARGUMENTS could match either an existing slug or a new topic:
- Check if `personal/learning/{slug}/progress.md` exists
- Check if `personal/learning/{slug}.md` exists (legacy)
- If either exists: RESUME mode
- If neither: NEW mode

## Language

Respond in the language the user used when invoking the command. Learning tracks themselves default to English unless the user specifies otherwise.

