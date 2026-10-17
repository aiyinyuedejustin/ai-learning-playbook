# lowwwbank/anything-to-course

- 链接：https://github.com/lowwwbank/anything-to-course
- 作者：lowwwbank
- 仓库说明：Universal AI agent skill that turns any material into learning-science-based self-study courses with retrieval practice, spaced repetition, and tutor mode.
- 星数：24
- 获取方式：GitHub README + SKILL/说明文件

---

## README

# anything-to-course

**Turn any material into a course that actually teaches. Built on learning science, not content dumps.**

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg) ![Agent Skills](https://img.shields.io/badge/Agent%20Skills-compatible-blue.svg) ![Works with](https://img.shields.io/badge/works%20with-Claude%20Code%20%C2%B7%20Claude.ai%20%C2%B7%20Codex%20%C2%B7%20any%20Agent%20Skills%20tool-8A2BE2.svg)

<p align="center">
  <img src="assets/social-preview.jpg" alt="anything-to-course: turn source material into a self-study course workflow" width="900">
</p>

A universal AI agent skill that turns documents, notes, books, transcripts, slides, codebases — or just a topic — into a complete self-study course, then runs your study sessions as a tutor. Built and tested on Claude Code; designed for Claude.ai, OpenAI Codex, Gemini CLI, Cursor, and any agent that can read a `SKILL.md` folder.

---

## What this is

`anything-to-course` is a portable course-design workflow for AI agents. It does not just summarize source material. It turns material into observable capabilities, lessons, practice, feedback, checkpoints, and a spaced review plan.

```
Source material       Capability map       Course build          Study mode
      |                    |                    |                    |
      v                    v                    v                    v
Docs, notes,  -->  outcomes, gaps  -->  lessons, tasks,  -->  retrieval,
slides, code       prerequisites        hidden answers        calibration,
or a topic          module order         review schedule       tutoring
```

## Quick demo

Ask your agent:

```text
Use the anything-to-course skill.
Turn ./docs/sql-handbook into a 3-week self-study course for analysts
who know Excel but have never written SQL.
Make learners practice before reading answers.
```

You get a course package with a syllabus, modules, lessons, hidden answer files, checkpoints, and a review schedule:

```text
sql-for-analysts/
├── 00-syllabus.md
├── modules/
│   ├── 01-filtering-rows/
│   └── 02-aggregation/
├── answers/
└── review-schedule.md
```

See the generated example in [`examples/example-course/sql-for-analysts/`](examples/example-course/sql-for-analysts/).

## The problem

Ask an AI to "make a course from this" and you get a **content dump**: well-formatted explanations, a cheerful summary, and a recognition quiz at the end. It reads smoothly. It feels clear. And it evaporates within a week — because *feeling of understanding* and *ability to act* are different outcomes, and rereading fluent text only produces the first one.

Decades of cognitive science are unambiguous about what produces durable capability: **effortful retrieval, spaced re-encounters, interleaved discrimination practice, feedback after (never before) an attempt, and support that fades**. Almost no AI-generated course uses any of it.

This skill hard-wires all of it into every course it builds.

## What you get

Give it source material and an audience. It produces a structured course:

```
your-course/
├── 00-syllabus.md            # observable capabilities, module map, how to study
├── modules/
│   ├── 01-foundations/
│   │   ├── 00-overview.md    # outcomes, prerequisites, entry diagnostic
│   │   ├── 01-....md         # lessons: attempt → principle → worked example
│   │   │                     #   → contrast → practice with fading support
│   │   └── 99-checkpoint.md  # mixed practice, methods not named
│   └── ...
├── answers/                  # feedback & explanations — physically separate,
│                             #   so answers can't be seen before the attempt
└── review-schedule.md        # spaced repetition plan (+1d, +7d, +30d)
```

Every lesson follows an 11-step canonical flow where the learner **attempts before reading the explanation**, retrieves from memory before seeing options, rates confidence before checking, and gets feedback that explains the *cause* of the error and demands a retry.

## See it before you run it

**[`examples/example-course/sql-for-analysts/`](examples/example-course/sql-for-analysts/)** is a complete, unedited course produced by this skill — syllabus, two modules, checkpoints, separated answer files, and a review schedule. Open any lesson and compare it with what "make me a course on SQL" gives you in a raw chat: the difference *is* the skill. A one-file taste: [`examples/sample-lesson.md`](examples/sample-lesson.md).

The skill also shows you a **sample lesson first** on every run — one representative lesson in ~5 minutes for your sign-off on depth and tone — before building the full course.

## Prerequisites

- An AI agent that can read local files: Claude Code, Claude.ai / Claude Desktop, OpenAI Codex, Gemini CLI, Cursor, or a similar tool.
- Git, if you want to clone the repository.
- Source material: docs, notes, PDFs, transcripts, slides, code, links you paste in, or just a topic brief.

No package manager, database, API key, or network access is required by the skill itself.

## Install

### Claude Code

```bash
git clone https://github.com/lowwwbank/anything-to-course.git ~/.claude/skills/anything-to-course
```

Then just ask:

> Turn ~/docs/sql-handbook/ into a 3-week course for analysts who know Excel but not SQL.

### Claude.ai / Claude Desktop

Zip this folder and upload it under **Settings → Capabilities → Skills**, then ask Claude to build a course from your material.

### OpenAI Codex CLI

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/lowwwbank/anything-to-course.git ~/.agents/skills/anything-to-course
```

### Repo-scoped install

If you want a project-local skill, vendor it inside the current repo:

```bash
mkdir -p .agents/skills
git clone https://github.com/lowwwbank/anything-to-course.git .agents/skills/anything-to-course
```

### Cursor, Gemini CLI, or any other agent

Place this folder wherever your agent can read it, then tell the agent to use `SKILL.md`. The skill is plain markdown: no scripts, no dependencies, no network access required.

### Copy-paste only

If your agent does not support local skill folders, copy the contents of [`SKILL.md`](SKILL.md) into the agent's custom instructions or prompt window, then attach or paste your source material.

## Run your first course

```text
Use the anything-to-course skill.
Turn <your source material> into a self-study course for <audience>.
Target outcome: learners should be able to <observable capability>.
Time budget: <duration>.
```

## How it works

1. **Intake** — audience, prior knowledge, target capabilities, time budget, stakes.
2. **Capabilities, not topics** — the material becomes 3–8 observable outcomes ("given X, the learner can Y to standard Z"). Content that serves no capability is cut.
3. **Dependency mapping** — modules ordered by what-builds-on-what, not by the source's table of contents. One lesson = one capability.
4. **Sample lesson first** — one representative lesson for your sign-off before the full build; style mismatches cost one lesson to fix, not a course.
5. **Lessons via the canonical flow** — real problem → learner attempt → principle → worked example (with the *why* of each step) → contrasting case → self-explanation → completion task → independent task → feedback → retry → exit ticket.
6. **Retention engineering** — exit tickets reach back to earlier lessons, cumulative checkpoints interleave modules, and `review-schedule.md` schedules retrieval at +1 day, +7 days, +21–30 days.
7. **Quality gate** — the finished course is audited against a 40-item author checklist and an anti-pattern list before delivery.
8. **Study mode** — afterwards, the same skill runs your sessions as a tutor: retrieval-first quizzing, confidence calibration, spaced reviews from the schedule, and a study log ([`references/study-mode.md`](references/study-mode.md)).

## The science

Every design rule traces to published research — mostly meta-analyses:

| Design rule | Evidence |
|---|---|
| Practice by retrieval, not rereading | [Rowland 2014](https://pubmed.ncbi.nlm.nih.gov/25150680/) · [Adesope et al. 2017](https://doi.org/10.3102/0034654316689306) · [Yang et al. 2021](https://doi.org/10.1037/bul0000309) |
| Attempt before explanation | [Sinha & Kapur 2021 (productive failure)](https://doi.org/10.3102/00346543211019105) · [Pan & Carpenter 2023 (pretesting)](https://doi.org/10.1007/s10648-023-09814-5) |
| Spaced reviews, relearning to criterion | [Dunlosky et al. 2013](https://doi.org/10.1177/1529100612453266) · [Rawson & Dunlosky 2013](https://doi.org/10.1007/s10648-013-9240-4) |
| Worked examples that fade with expertise | [van Gog, Paas & Sweller 2010](https://doi.org/10.1007/s10648-010-9145-4) · [expertise reversal meta-analysis 2025](https://doi.org/10.1016/j.learninstruc.2025.102142) |
| Directed self-explanation prompts | [Bisra et al. 2018](https://eric.ed.gov/?id=EJ1186664) · [Chi & Wylie 2014 (ICAP)](https://doi.org/10.1080/00461520.2014.965823) |
| Interleaving for tool selection | [Brunmair & Richter 2019](https://pubmed.ncbi.nlm.nih.gov/31556629/) |
| Feedback after the attempt, cause-level, with retry | [Wisniewski, Zierer & Hattie 2020](https://doi.org/10.3389/fpsyg.2019.03087) · [Shute 2008](https://doi.org/10.3102/0034654307313795) |
| Confidence calibration against the fluency illusion | [Koriat & Bjork 2005](https://doi.org/10.1037/0278-7393.31.2.187) |
| Terms defined before first use | [Mayer 2017 (pre-training)](https://doi.org/10.1111/jcal.12197) · [Shatz 2023 (curse of knowledge)](https://doi.org/10.1111/test.12320) |
| Concrete example → abstract principle | [Fyfe et al. 2014 (concreteness fading)](https://doi.org/10.1007/s10648-014-9249-3) |
| Goals ↔ practice ↔ assessment alignment | [Biggs 1996 (constructive alignment)](https://doi.org/10.1007/BF00138871) |
| Debriefed MCQ distractors | [Roediger & Marsh 2005](https://pubmed.ncbi.nlm.nih.gov/16248758/) |
| AI grading only with rubrics | [Jukiewicz & Wyrwa 2026](https://doi.org/10.3390/app16020680) |

The full principle set with conflict-resolution rules lives in [`references/learning-science.md`](references/learning-science.md).

## What this skill refuses to do

Honest constraints, by design:

- ❌ No walls of explanation with a quiz bolted on the end
- ❌ No answers visible before the learner's attempt
- ❌ No recognition-only testing ("which of these is the definition of...")
- ❌ No new jargon used before it's defined for *this* audience
- ❌ No single example without a contrast or counterexample
- ❌ No topic ordering copied from the source's table of contents
- ❌ No "reread and highlight" as a study strategy
- ❌ No optimizing for completion speed and satisfaction over delayed performance
- ❌ No invented facts to pad thin source material — gaps get flagged instead

The full anti-pattern list is in [`references/quality-rubrics.md`](references/quality-rubrics.md).

## Repository structure

```
anything-to-course/
├── SKILL.md                        # the skill: workflow the agent follows
├── references/
│   ├── learning-science.md         # 18 principles + research citations
│   ├── course-blueprint.md         # canonical course/module/lesson templates
│   ├── practice-design.md          # practice matrix, question & feedback design
│   ├── quality-rubrics.md          # author checklist, case rubric, anti-patterns
│   └── study-mode.md               # tutor protocol: sessions, calibration log
├── examples/
│   ├── example-course/             # complete generated course (SQL for analysts)
│   └── sample-lesson.md            # one-file lesson excerpt
└── README.md
```

The skill uses [progressive disclosure](https://agentskills.io/specification): agents load ~100 tokens of metadata at startup, the workflow when triggered, and reference files only when needed.

## FAQ

**What inputs work?** Anything the agent can read: markdown/docs, PDFs, meeting or lecture transcripts, slide decks, blog post collections, codebases, or a plain topic description ("make me a course on X for Y"). Thin material gets flagged, not padded.

**What about non-English source material?** Fine. The skill's instructions are English; the generated course follows the language you ask for.

**Can it run the course too, not just write it?** Yes — say "run my study session" and the skill turns tutor: retrieval-first quizzing, confidence calibration, spaced reviews, and a study log, with hard rules like "no answers before an attempt" ([protocol](references/study-mode.md)).

**How long a course can it build?** From a 1-hour primer to a multi-week program. Light requests keep the core invariants (attempt-first, retrieval practice, hidden answers) and drop the heavy apparatus (cumulative checkpoints, long review schedules).

## License

[MIT](LICENSE). Skills can direct an agent's behavior — always review a skill's contents before installing, including this one.


## 文件 SKILL.md

---
name: anything-to-course
description: Turn any source material — documents, notes, books, articles, transcripts, slides, codebases, or just a topic — into a complete self-study course built on evidence-based learning science (retrieval practice, spaced repetition, interleaving, faded scaffolding, confidence calibration). Use whenever the user wants to create a course, curriculum, tutorial, training program, study guide, workshop, onboarding track, or learning path from existing content or expertise, even if they only say "help me teach X", "make learning materials from this", or "I need to explain this to my team".
license: MIT
metadata:
  author: lowwwbank
  version: "1.0"
---

# Anything to Course

Build courses that change what the learner **can do**, not what they recognize.

The failure mode to avoid: a "content dump" — well-organized explanations followed by a
few recognition quizzes. It reads smoothly, feels clear, and evaporates within a week.
Fluency is not learning. Every design decision in this skill exists to force effortful
retrieval, spaced re-encounters, and transfer to new contexts, because those are the
mechanisms that produce durable capability (see `references/learning-science.md` for the
principles and the research behind them).

## The one rule that governs everything

> The unit of course design is not a topic or a page. It is a **new capability of the
> learner** — something they can do after the course that they could not do before.

Content that does not serve a capability gets cut. A capability without practice is a
promise without a mechanism. A check that doesn't match the capability measures the
wrong thing.

## Workflow

### Step 0 — Intake

Collect the source material and establish context. Ask the user (or infer and state
assumptions explicitly if working autonomously):

1. **Audience** — who is the learner? What do they already know? What jargon is safe?
2. **Target capabilities** — what should the learner be able to DO afterwards?
3. **Scope and time budget** — a 2-hour primer and a 6-week course are different designs.
4. **Delivery format** — markdown for self-study (default), slides, LMS-ready text, etc.
5. **Stakes** — hobby curiosity vs. job-critical skill changes how much retention
   engineering (reviews, checkpoints) the course needs.

If the source material is thin in places, say so and either research the gap or mark it
as an explicit assumption. Never invent facts to fill a chapter.

### Step 1 — Define capabilities, not topics

Convert the material into 3–8 observable capabilities. Each must answer four questions:

1. What will the learner be able to do?
2. In what situation?
3. To what standard?
4. How will we see that it formed?

Weak: *"Understand product metrics."*
Strong: *"Given a product description and a set of metrics, the learner can choose the
primary metric, justify the choice, reject plausible alternatives, and name one risk of
misinterpreting it."*

Weak objectives produce weak courses — you cannot design practice for "understand".

### Step 2 — Map prerequisites and structure

- Build a dependency graph: which capabilities rest on which concepts and procedures.
- Slice into modules and lessons. **One lesson = one coherent capability**, a limited
  set of new concepts, one connected mental model. If a task needs several not-yet-taught
  operations, split the lesson or add stepping stones.
- Order by dependencies, not by the source material's table of contents.
- Plan a short diagnostic at each module start — its job is to choose the right level of
  support, not to grade.

Read `references/course-blueprint.md` before writing any lesson — it defines the
canonical chapter flow this skill follows.

### Step 3 — Prove the format with one sample lesson

Before building the whole course, write ONE representative lesson (pick the most
central capability, not the easiest) and show it to the user with a one-line note:
"this is the format every lesson will follow — happy with the depth, tone, and
practice style?". Why this step exists: it moves the user's first payoff from
"30+ minutes in" to "5 minutes in", and it catches style/depth mismatches when
fixing them costs one lesson, not a whole course. Adjust on feedback, then proceed.
Skip only when the user explicitly asked for a fully autonomous run — and say so.

### Step 4 — Write lessons using the canonical flow

Every lesson follows the attempt-first sequence (full detail and rationale in
`references/course-blueprint.md`):

1. Real problem or question the lesson answers
2. Learner's short attempt or prediction **before** the explanation
3. Clear statement of the principle
4. Fully worked example — showing *why* each step, not just *what*
5. Contrasting example or counterexample
6. Self-explanation prompts
7. Partially completed task
8. Independent task, notes closed
9. Feedback (in a separate answer file — never visible before the attempt)
10. Corrected retry or new variation
11. Exit ticket mixing current and previous lessons

Two writing rules are non-negotiable:

- **First-use rule**: never use a term the target learner doesn't know without defining
  it in plain words at first substantive use. Pattern: *"**Term** — what it is in plain
  words; what distinguishes it from neighbors; why it matters here."* Judge novelty by
  the audience's vocabulary, not the author's.
- **Example → principle**: every story or case ends with the transferable principle and
  at least one contrast (different context, or a look-alike case where the principle
  does NOT apply). One vivid example without contrast teaches surface details.

### Step 5 — Design practice and assessment

Read `references/practice-design.md` for the practice format matrix, question design,
distractor rules, and feedback structure. Core constraints:

- Practice format must match the capability (recall → free recall, not multiple choice;
  tool selection → mixed tasks that don't name the method; judgment → open case with a
  rubric).
- Recall before recognition: the learner formulates an answer from memory first, rates
  confidence, and only then sees options or the answer key.
- Support fades: worked example → completion task → independent task → new context.
- Some tasks must NOT name the method — in real work, problems don't arrive labeled with
  the chapter title.

### Step 6 — Engineer retention

- Schedule spaced reviews: same day → +1 day → +7 days → +21–30 days, scaled to course
  length. Every review requires retrieval, not rereading.
- Each lesson's exit ticket pulls one or two items from earlier lessons.
- Every 2–3 modules: a cumulative checkpoint with interleaved tasks from all previous
  modules, including at least one integration task where the method is not named.
- Emit a `review-schedule.md` so the learner knows when to return and to what.

### Step 7 — Quality gate

Before delivering, audit the whole course against the author checklist in
`references/quality-rubrics.md`. Fix every violation — the checklist items are cheap to
fix at this stage and expensive to discover as a learner. Also verify none of the
anti-patterns (same file) survived: recognition-only quizzes, answers visible before
attempts, terms used before definition, single examples without contrast, practice only
at the end.

### Step 8 — Deliver

Default output structure (adapt if the user asked for a different format):

```
<course-name>/
├── 00-syllabus.md            # capabilities, prerequisites, module map, how to study
├── modules/
│   ├── 01-<module-name>/
│   │   ├── 00-overview.md    # outcomes, why it matters, diagnostic
│   │   ├── 01-<lesson>.md    # lessons per canonical flow
│   │   └── 99-checkpoint.md  # end-of-module mixed practice
│   └── ...
├── answers/                  # feedback + explanations, one file per lesson,
│   └── ...                   # kept separate so answers aren't visible during attempts
└── review-schedule.md        # spaced repetition plan with dates/offsets
```

In `00-syllabus.md`, tell the learner *how* to use the course: attempt before peeking,
rate confidence, follow the review schedule, treat errors as material. Learners default
to rereading — the course must teach them not to.

## Study mode — running a course as the tutor

This skill also RUNS courses, not only writes them. When the user says "help me study
this course", "quiz me", "run my review session", or points at a course produced by this
skill (or any structured material), switch to tutor mode and follow the session protocol
in `references/study-mode.md`: retrieval first, confidence before checking, feedback
after the attempt, calibration log, and the spaced schedule as the source of what's due.
After delivering a new course (Step 8), offer this explicitly: "Want me to run your
first study session now?" — the course only works if somebody studies it.

When the course will be graded by an AI (open cases, variations), embed the guardrails
from `references/practice-design.md` § "AI as coach": give the AI the goal, context,
rubric, and quality-level examples; require it to cite specific fragments of the
learner's answer; and treat its feedback as a hypothesis, not a verdict. AI feedback
without a rubric drifts toward generic praise.

## Scaling to the request

Not every request needs the full apparatus. A "quick 1-hour intro" still gets
capability-first objectives, attempt-before-explanation, and retrieval practice — but
fewer modules, a lighter review schedule, and no cumulative checkpoints. State what was
cut and why. What never gets cut: practice with feedback, and answers hidden until after
the attempt.

