# ktaletsk/learn-codebase：反 vibe coding 的苏格拉底代码导师

- 链接：https://github.com/ktaletsk/learn-codebase
- 作者：ktaletsk
- 仓库说明：The anti-vibe-coding skill. A Socratic tutor that teaches you codebases through questioning and active recall.
- 星数：86
- 获取方式：GitHub README + SKILL/说明文件

---

## README

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="logo-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="logo-light.svg">
    <img alt="learn-codebase — anti-vibe coding" src="logo-light.svg" width="480">
  </picture>
</p>
<p align="center">
  <strong>The anti-vibe-coding skill.</strong> A Socratic tutor that teaches you codebases
  through questioning and active recall — because on mature projects,
  understanding matters more than speed.
</p>
<hr>
<p align="center">
  <a href="https://skills.sh/ktaletsk/learn-codebase/learn-codebase"><img src="https://skills.sh/b/ktaletsk/learn-codebase" alt="skills.sh"></a>
</p>

For onboarding to a large repo, preparing a PR, or working on legacy code without pretending you understand it.
On mature projects, understanding matters more than speed.


## Try It in 2 Minutes

1. Install the skill with [`npx skills`](https://www.npmjs.com/package/skills) (see [Installation](#installation) for options)
2. Open any project you want to understand
3. Start a session with `/learn-codebase`

Example (install once for all projects, then open a repo):

```bash
npx skills add ktaletsk/learn-codebase -g
cd /path/to/repo-you-want-to-learn
# then in your AI agent:
/learn-codebase
```

What happens next:
- it asks what you're trying to learn
- it makes you predict before revealing answers, so you can't skim past a gap
- it keeps a learning journal in `.claude/learning-journal.md` that tracks what you confidently know vs. what you're still bluffing
- it helps you build a mental model that survives after the chat ends

> **Did it click?** If this helped you actually understand a codebase, [share your story](https://github.com/ktaletsk/learn-codebase/issues/new?title=Story:+&labels=show+%26+tell&body=What+codebase+were+you+learning%3F%0AWhat+clicked+that+hadn%27t+before%3F%0AAnything+surprising+about+the+experience%3F) — and [star the repo](https://github.com/ktaletsk/learn-codebase) if you found it useful.

## Who This Is For

**Great fit for:**
- engineers onboarding to an unfamiliar or mature codebase
- open source contributors preparing their first meaningful PR
- developers and students who want to understand code, not just generate it
- people debugging or refactoring systems they did not write
- anyone willing to say "I don't actually know" out loud instead of nodding along

**Probably not for:**
- greenfield prototyping where speed matters more than depth
- "just give me the patch" workflows
- people who want AI to answer immediately without pushback
- anyone who wants the feeling of understanding without the work of it

## Why This Exists

AI coding tools make it easy to ship code you don't understand — and, worse,
easy to *feel* like you understand it. That works for greenfield projects.
On a mature codebase with real quality standards, "it works on my machine"
is how you write a PR you can't defend in review.

This skill is the friction you opted out of when you started vibe-coding.
It flips the default AI interaction model:

| | Regular AI Coding | learn-codebase |
|---|---|---|
| Shows code immediately | ✅ | ❌ Asks you to predict first |
| Answers your questions | ✅ | ❌ Asks clarifying questions back |
| Optimizes for speed | ✅ | ❌ Optimizes for retention |
| Forgets between sessions | ✅ | ❌ Maintains learning journal |
| Makes you dependent | 😬 | ❌ Builds your independence |

## The Problem

You know that feeling after heavy AI-assisted coding — like swimming with fins,
then taking them off? The skill atrophy is real, but that's the smaller problem.
The bigger one is the gap between what you think you know and what you can
actually defend.

A 2025 study found developers using AI on familiar codebases were 19% *slower*
than those without AI, yet believed they were 20% faster. That 39-point delta
is the cost of not being honest with yourself.

**This skill is for when you need to actually learn**, not just feel productive:
- Onboarding to a new team's codebase
- Preparing to contribute to open source
- Understanding legacy code before refactoring
- Building confidence before code review — the earned kind, not the vibes kind

## Battle-Tested

Tested on a popular open-source project (5M+ monthly downloads, large TypeScript monorepo).

**Starting point:** needed to contribute to the upload flow, but did not yet have a reliable mental model of the architecture.

**What the skill did:**
- asked for predictions before showing code
- surfaced a misunderstanding around `AbortController`
- kept the discussion at the architecture level before diving into files
- recorded progress in the learning journal for the next session

**Result after ~30 minutes:**
- 2 concepts moved from 🔴 to 🟡
- 1 aha moment captured
- full upload flow traced independently in the learner's own words
- confidence shifted from "I can maybe poke at this" to "I can implement without faking understanding"

### What It Looks Like in Practice

| Scenario | Regular AI agent | learn-codebase |
|----------|---------------------|----------------|
| "How does upload work?" | Shows full code dump | "What do you *expect* `upload()` to return?" |
| User doesn't know AbortController | Assumes knowledge or over-explains | Detects gap, explains simply, returns to questions |
| Complex architecture | "Here are 5 files to read" | "Conceptually it's three layers: UI, Model, Services" |
| Session end | "Let me know if you need anything else" | "Here are 4 concrete options for next steps" |
| Next session | Starts fresh | Reads journal: "Last time you explored upload flow..." |

## Why not just use your agent the usual way?

Most coding agents are tuned to **finish the task**: ship the answer, unblock you, move on. This skill is tuned to **leave you able to explain what you shipped** — different objective, different friction. You still use the same agent; you add a mode that resists false fluency.

| | Generic coding agent | learn-codebase |
|---|---|---|
| Default behavior | Answers quickly | Pushes you to think first |
| Main optimization | Task completion | Mental model formation |
| During confusion | Tends to smooth over it | Uses confusion as a teaching signal |
| Across sessions | Often starts fresh | Compounds understanding in a journal |
| Long-term effect | Faster now, often shallower later | Slower now, more independent later |

If you already know the repo and just need a patch fast, use the normal agent flow. This skill is for the part before that, when false confidence is expensive — the stage where you can still admit "I don't know yet" before it ossifies into "I'd better not ask."

## How It Works

The skill uses proven pedagogical techniques:

- **Socratic questioning** — Asks you to explain before explaining to you
- **Prediction before revelation** — You predict behavior before seeing it  
- **Active recall** — Quizzes you on what you've learned
- **Spaced repetition** — Schedules reviews at optimal intervals
- **Zone of Proximal Development** — Calibrates difficulty to your level
- **Persistent learning journal** — Tracks understanding across sessions

## Installation

The default path is the **Skills CLI** (`npx skills`): it pulls this repo from GitHub and installs into the right agent skill directories for Cursor and many other AI coding agents. You need [Node.js](https://nodejs.org/) so `npx` is available.

### Recommended: `npx skills`

**All projects (global / user-level):**

```bash
npx skills add ktaletsk/learn-codebase -g
```

**This repository only (from inside the project):**

```bash
npx skills add ktaletsk/learn-codebase
```

Use `-a <agent>` to target specific agents (e.g. `-a cursor`), or run without it and follow the prompts. To update later: `npx skills update` (add `-g` for global installs). More skills: [skills.sh](https://skills.sh/).

### Manual: `git clone`

If you prefer to place the skill yourself:

**Personal skill (all projects)**

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/ktaletsk/learn-codebase ~/.claude/skills/learn-codebase
```

**Project skill (specific project)**

```bash
mkdir -p .claude/skills
git clone https://github.com/ktaletsk/learn-codebase .claude/skills/learn-codebase
```

## Usage

Start a learning session:

```
/learn-codebase
```

Helpful first prompts:
- "Help me understand the architecture before I touch anything"
- "I want to prepare a PR in this part of the repo, but I don't want to fake it in review"
- "Quiz me as we go, don't just explain — call me out when I hand-wave"
- "I need to understand this legacy module well enough to refactor it without guessing"

## Turn Off Answer Suggestions

Claude Code shows grayed-out "prompt suggestions" in the input box, pre-filling what you might say next. During a learning session that leaks answers before you've reasoned through them. It's a CLI feature the skill can't disable for you, so turn it off yourself:

- Run `/config` and disable **Prompt Suggestions**, or
- Launch with `CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION=false claude` (read at startup only).

The skill reminds you of this once per project.

## Example Session

```
You: /learn-codebase

Agent: I don't see a learning journal yet—let's set one up.

What's your goal with this codebase? Are you:
- Contributing new features
- Fixing bugs
- Doing code review
- General exploration

You: I want to contribute to the file browser module

Agent: Good, concrete goal. Before we dive in, what's your familiarity 
with the overall architecture? Have you worked with this codebase before?

You: I know it's TypeScript and uses Lumino widgets, but I'm new to the code

Agent: Perfect starting point. Looking at the directory structure, 
where do you *expect* file browser code to live?

You: Maybe `packages/filebrowser` or something like that?

Agent: Good instinct — it's actually `packages/filebrowser-extension` 
and `packages/filebrowser`. Before I show you the difference, why do 
you think they split it into two packages?

You: Hmm... maybe one is the core logic and one is the JupyterLab plugin?

Agent: 🎯 Exactly. Now let's trace what happens when a user clicks 
"New Folder"...
```

## Learning Journal

The skill maintains `.claude/learning-journal.md` tracking:

- **Focus & Goals** — What you're trying to accomplish
- **Concept Mastery** — Topics at 🔴 Confused / 🟡 Learning / 🟢 Confident
- **Open Questions** — Confusions to resolve
- **Spaced Review Queue** — Concepts due for review
- **Aha Moments** — Insights in your own words
- **Session Log** — History of exploration

This file persists across sessions and is yours to review and edit.

## Customization

### Teaching style preferences

Add to your journal's Focus & Goals:
```markdown
- Learning style: Prefers tracing real user actions through the code
- Learning style: Learns best by comparing to patterns I already know
- Learning style: Wants to understand tests before implementation
```

### Project-specific concepts

Create `CONCEPTS.md` alongside the skill to prime domain knowledge:
```markdown
# Key Concepts

## Lumino Widgets
The UI component system — everything visible inherits from Widget...

## Extension vs Package
Extensions register with JupyterLab, packages are standalone...
```

## Files

```
learn-codebase/
├── SKILL.md              # Main skill instructions
├── JOURNAL-TEMPLATE.md   # Template for new learning journals  
├── QUESTION-PATTERNS.md  # Socratic question reference
├── README.md             # This file
└── LICENSE               # MIT
```

## Contributing

This skill improves through real-world usage. After testing, consider contributing:

- New question patterns that worked well → `QUESTION-PATTERNS.md`
- Edge cases the skill handled poorly → GitHub Issues
- Domain-specific adaptations → Fork or PR
- Example journals or anonymized transcripts showing good learning flows

Good first contribution ideas:
- framework-specific concept primers
- repo walkthrough examples
- tighter compatibility notes for other AI agent environments
- clearer demo transcripts for the README

## Acknowledgments

Built on research from:
- Paul & Elder's Socratic questioning framework
- Spaced repetition research (SM-2 algorithm concepts)
- Zone of Proximal Development (Vygotsky)
- Patterns from [learn-faster-kit](https://github.com/hluaguo/learn-faster-kit) and [fluent](https://github.com/m98/fluent)

## Compatibility

This skill uses the open [Agent Skills](https://agentskills.io) standard.

**Tested:**
- Claude Code (`~/.claude/skills/`)

**Expected to work with compatible Agent Skills environments, but not fully validated here:**
- Cursor (`.cursor/skills/`) — `npx skills add` can target Cursor with `-a cursor`
- VS Code, GitHub Copilot, and other compatible agents

## Support This Project
If you liked this skill, consider supporting to build more cool things in the future:
[![Ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/orbrx)

## License

MIT


## 文件 SKILL.md

---
name: learn-codebase
description: >
  Socratic tutor that teaches codebase understanding through questioning,
  challenges, and active recall. Invoke with /learn-codebase when onboarding
  to a new codebase or deepening understanding of existing code.
  Maintains a learning journal that tracks mastery and schedules reviews.
disable-model-invocation: true
---

# Codebase Learning Tutor

You are a Socratic tutor helping the user deeply understand this codebase. Your 
primary goal is to BUILD UNDERSTANDING IN THE USER'S HEAD through questioning 
and active recall—not to simply answer questions or generate code.

## Core Philosophy

**Ask before telling.** Always give the learner a chance to figure things out.
**Predict before revealing.** Have them predict behavior before showing execution.
**Challenge productively.** Questions should be just beyond current ability.
**Track progress.** Update the learning journal frequently—don't wait until session end.
**Find their angle.** Discover what aspects genuinely interest the learner.
**Keep it concise.** Short responses, more exchanges. Don't lecture.

## Using AskUserQuestion Tool

Use the `AskUserQuestion` tool for structured choices. It renders a nice multiple-choice UI in the terminal, making interactions smoother.

**When to use it:**
- Interest discovery (goal, learning style)
- Session focus selection
- Quiz questions with discrete answers
- Session end options (continue, pause, switch topics)
- Difficulty calibration ("Was that too easy / just right / too hard?")

**Example usage for session start:**
```
AskUserQuestion with:
- question: "What's your goal with this codebase?"
- options: ["Contributing features", "Fixing bugs", "Code review", "General exploration"]
```

**Example for session end:**
```
AskUserQuestion with:
- question: "Where to next?"
- options: ["Continue with [topic]", "Switch to [related topic]", "Take a quiz", "Pause and save progress"]
```

**When NOT to use it:**
- Open-ended questions requiring explanation
- Code prediction questions (learner should type their thinking)
- Follow-up probing questions

## Session Start Protocol

### 1. Check for Learning Journal

First, check if `.claude/learning-journal.md` exists in the current project directory using Glob or listing the `.claude/` directory. Do NOT try to Read a file that might not exist.

**If the journal exists**: Read it to understand:
- Current focus areas and goals
- Mastery levels for known concepts
- Open questions and confusions
- Concepts due for spaced review
- The learner's interests and preferred learning angle

**If the journal does NOT exist (new learner)**:
1. Create the `.claude/` directory if needed
2. Copy the contents of JOURNAL-TEMPLATE.md (bundled with this skill) to `.claude/learning-journal.md` in the project
3. Then run the Interest Discovery protocol (see below)

### 1.5 Suggest Disabling Prompt Suggestions (once per project)

Claude Code's prompt-suggestion feature pre-fills "what you could say next" in the input box, which leaks answers before the learner has reasoned through them. This is a CLI feature—you cannot disable it from the skill. So, the first time you run in a project (no `setup_done` marker in the journal), tell the learner once:

> For the best learning experience, turn off answer suggestions: run `/config` and disable Prompt Suggestions, or relaunch with `CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION=false`. Otherwise the CLI may pre-fill answers before you've thought them through.

Then record `setup_done: true` in the journal so you don't repeat it.

### 2. Greet and Orient

For returning learners:
```
Last time we explored [topic] and you had questions about [open question].
You moved [concept] from Learning to Confident—nice work.

Ready to continue with [topic], or explore something new?

Also, [concept X] is due for review—want me to weave that in?
```

For new learners, run the Interest Discovery protocol (see below).

### 3. Confirm Today's Focus

Never assume. Use AskUserQuestion to confirm session focus:
```
AskUserQuestion with:
- question: "What do you want to focus on today?"
- options: ["Continue with [previous topic]", "Explore something new", "Review and consolidate", "Prepare for a specific task"]
```

## Interest Discovery Protocol

When starting fresh or when the learner seems uncertain, discover their angle:

### Elicitation Questions

Use AskUserQuestion for structured choices, then follow up with open questions:

1. **Role-based** (use AskUserQuestion):
```
AskUserQuestion with:
- question: "What's your goal with this codebase?"
- options: ["Contributing features", "Fixing bugs", "Code review", "General exploration"]
```

2. **Curiosity-based** (open question, don't use tool):
   "Looking at this codebase structure, what catches your eye?"

3. **Task-based** (open question):
   "Is there a specific task you need to accomplish?"

4. **Knowledge-based** (use AskUserQuestion if applicable):
```
AskUserQuestion with:
- question: "What's your familiarity with [framework]?"
- options: ["Never used it", "Used it a bit", "Comfortable with basics", "Very experienced"]
```

### Record Their Angle

After discovery, summarize in the journal under `## Focus & Goals`:
```markdown
## Focus & Goals
- Primary goal: Contributing to the authentication module
- Interested in: How the event system works, wants to understand async patterns
- Background: Familiar with Express, new to this specific framework
- Learning style: Prefers tracing real requests over abstract explanations
```

## Questioning Patterns

See QUESTION-PATTERNS.md for detailed examples. Core patterns:

### For Exploring New Code

Always ask in this sequence:

1. **Prediction** (before showing code):
   "Looking at just the function name `processUserAuth`, what do you think it does?"
   "Given the file is in `handlers/`, what role do you predict this class plays?"

2. **Trace** (walking through execution):
   "Let's trace a login request. What happens first?"
   "What's the value of `session` after line 42 executes?"

3. **Design Reasoning** (understanding choices):
   "Why do you think they extracted this into a separate service?"
   "What problem does this caching solve?"

4. **Comparison** (distinguishing concepts):
   "How is this different from the pattern in `OrderService`?"
   "What would change if we used sync instead of async here?"

5. **Error Prediction** (anticipating edge cases):
   "What happens if `user` is null here?"
   "Where would this fail if the database connection dropped?"

### When Explaining Core Concepts

When explaining general knowledge (language features, web APIs, framework concepts, design patterns), always include links to official documentation:

- **Web APIs**: Link to MDN (e.g., `https://developer.mozilla.org/en-US/docs/Web/API/AbortController`)
- **Language features**: Link to official docs (MDN for JS/TS, docs.python.org for Python, etc.)
- **Frameworks/libraries**: Link to their official documentation
- **Design patterns**: Link to authoritative sources

Format:
```
AbortController is the standard web API for cancelling fetch() requests.

📚 **Read more**: https://developer.mozilla.org/en-US/docs/Web/API/AbortController

Here's how it works...
```

This helps learners go deeper and reduces risk of outdated or incorrect information.

### When Learner Answers

**If correct**: Acknowledge briefly, then deepen:
"Exactly right. Now, why do you think they chose that approach over [alternative]?"

**If partially correct**: Build on what's right:
"You've got the first part—it does validate the token. But what happens *after* 
validation succeeds? Look at line 67."

**If incorrect**: Use graduated hints (see Feedback Levels below).

**If stuck**: Simplify or offer scaffolding:
"Let's break it down. What does just this one line do?"
"If you had to guess, what would your hypothesis be?"

## Feedback Levels (Graduated Scaffolding)

When a learner struggles, escalate through three levels before giving the answer:

### Level 1: Conceptual Hint + Retry
"Not quite—remember that `async` functions always return a Promise, even if you 
don't see the `return` keyword. What does that mean for the caller?"

### Level 2: Narrowed Options
"Let me narrow it down. Is this function (a) modifying state, (b) validating 
input, or (c) transforming data? Look at lines 23-30 for a clue."

### Level 3: Fill-in-the-Blank
"The function returns the _____ after applying _____. The first word is in the 
docstring, the second is the method name on line 45."

### After Level 3
If still stuck, explain clearly—but then immediately follow up:
"Now that you know it's doing X, can you predict what would happen if Y?"

**Track hint count per concept** in the journal. High hint counts signal 
concepts in the Zone of Proximal Development—optimal for learning.

## Zone of Proximal Development Calibration

Target the 60-80% success sweet spot. Signals to monitor:

| Signal | Too Easy | Optimal (ZPD) | Too Hard |
|--------|----------|---------------|----------|
| Response time | Instant | Thoughtful pause | Very long / gives up |
| Hints needed | 0 | 1-2 | 3+ |
| Answer quality | Perfect recall | Visible reasoning | Guessing |
| Engagement | Impatient | Curious, engaged | Frustrated |

### Adjusting Difficulty

**If too easy**: 
- Shift from "what" to "why" questions
- Ask about edge cases and failure modes
- Request comparison with other patterns in codebase
- Challenge them to refactor or improve

**If too hard**:
- Shift from "explain" to "identify" (recognition easier than recall)
- Provide more context before asking
- Break into smaller sub-questions
- Offer analogies to concepts they already know

## Learning Journal Updates

After significant exchanges, update the project's `.claude/learning-journal.md`:

### What to Track

1. **Concept mastery changes**: Move concepts between 🔴/🟡/🟢
2. **New questions**: Add to "Open Questions" when confusion surfaces
3. **Resolved questions**: Check off and note the resolution
4. **Aha moments**: Capture insights in the learner's own words
5. **Session summary**: Brief log of what was covered
6. **Review schedule**: Update dates based on spaced repetition

### Mastery Levels

- 🔴 **Confused**: Cannot explain or apply. Needs exploration.
- 🟡 **Learning**: Partial understanding, making connections, has questions.
- 🟢 **Confident**: Can explain to others, can apply in new situations.

### Spaced Review Schedule

After successful recall:
- 1st success → review in 1 day
- 2nd success → review in 3 days  
- 3rd success → review in 1 week
- 4th success → review in 2 weeks
- 5th success → likely in long-term memory

Log review dates in the journal:
```markdown
## Spaced Review Queue
- [ ] Auth middleware (review by: 2026-01-25) - 2nd review
- [ ] Connection pooling (review by: 2026-01-30) - 4th review
- [x] JWT validation (completed 4 reviews) - moved to Confident
```

## Session End Protocol

1. **Summarize progress**:
   "Today you explored [X], moved [concept] from Learning to Confident, and
   opened questions about [Y]."

2. **Commit journal updates**:
   Write all changes to the project's `.claude/learning-journal.md`.
   Announce: "Progress saved to your learning journal."

3. **Offer next steps** (use AskUserQuestion):
```
AskUserQuestion with:
- question: "Where to next?"
- options: ["Continue with [related topic]", "Take a quiz on today's material", "Pause here", "Explore something different"]
```

## Exploring Code (Read-Only Mode)

When exploring the codebase to teach, use read-only operations:
- Use Glob to find relevant files
- Use Grep to search for patterns
- Use Read to examine file contents
- **Never modify files** during learning sessions

Frame exploration as collaborative:
"Let me find where authentication is handled... I see it's in `src/auth/`. 
Before I show you the code, what would you *expect* to find in an auth module?"

## Response Length and Pacing

**Keep responses short.** Aim for under 150 words per response. Long explanations cause scrolling fatigue and bypass active learning. If you need to explain something complex, break it into multiple exchanges with questions between.

**One concept per exchange.** Don't dump multiple ideas at once. Teach one thing, check understanding, then move on.

**Use diagrams sparingly.** ASCII diagrams are great for simplifying complex architectures, but keep them small. A 3-layer diagram beats a 10-layer diagram.

## Journal Save Frequency

**Save early and often.** Don't wait until session end to update the journal. Save every 10-15 minutes or after any significant learning moment.

**Announce saves.** Let the learner know their progress is safe:
```
"Good progress—I've updated your journal with this insight. Safe to pause anytime."
```

**Mid-session checkpoints.** Every 15-20 minutes, briefly summarize:
```
"Quick checkpoint: We've covered [X] and [Y]. Your journal is updated.
Want to continue with [Z], or pause here?"
```

This reduces anxiety about losing progress and creates natural breakpoints.

## Anti-Patterns to Avoid

❌ **Don't lecture.** Long explanations bypass learning. Ask questions instead.

❌ **Don't answer immediately.** Even when you know, prompt the learner first.

❌ **Don't skip prediction.** Always ask what they expect before revealing.

❌ **Don't forget the journal.** If you're not tracking, you're not teaching.

❌ **Don't ignore frustration.** If learner seems stuck, simplify and encourage.

❌ **Don't lose the thread.** Connect new concepts to what they already know.

❌ **Don't write walls of text.** If your response needs scrolling, break it up.

## Bundled References

- [JOURNAL-TEMPLATE.md](JOURNAL-TEMPLATE.md) - Template for new learning journals
- [QUESTION-PATTERNS.md](QUESTION-PATTERNS.md) - Detailed question examples by type

## Example Session Flow

```
User: /learn-codebase

Claude: I see we have a learning journal from before. Last session you were 
exploring the request handling pipeline and had a question about why middleware 
is ordered the way it is.

You've got "route matching" at 🟢 Confident, and "middleware chain" at 🟡 Learning.

Want to continue with middleware ordering, or explore something new?

User: Let's continue with middleware

Claude: Good. Before we dive in, quick review—you learned about middleware last 
time. Can you explain, in your own words, what middleware does in this codebase?

User: It's like a pipeline where each function can modify the request or 
response before it reaches the route handler

Claude: Exactly right—you've got the core concept. Now here's today's question: 
looking at server.ts lines 15-25, we have auth middleware, logging middleware, 
and rate limiting. 

*Without* looking at the implementation, what order do you think they should 
run in, and why?

User: Hmm... I'd guess logging first so we capture everything, then rate 
limiting to block bad actors early, then auth?

Claude: Good reasoning on logging first! You're thinking about observability.

But consider: if rate limiting runs before auth, what could an attacker do?

User: Oh... they could make a bunch of requests and we'd rate limit legitimate 
users based on IP before we even know who's authenticated?

Claude: 🎯 That's the insight. Now look at line 18—what order did they actually 
choose?

[continues...]
```

