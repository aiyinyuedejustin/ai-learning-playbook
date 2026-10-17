# adityak74/learn-anything-24h

- 链接：https://github.com/adityak74/learn-anything-24h
- 作者：adityak74
- 仓库说明：A Claude Code / Codex skill that turns any complex topic into a 24-hour active-learning sprint.
- 星数：3
- 获取方式：GitHub README + SKILL/说明文件

---

## README

<h1 align="center">Learn Anything 24h</h1>

<p align="center">
  <img src="./logo.svg" alt="Learn Anything 24h logo" width="860">
</p>

<p align="center">
  <a href="https://adityakarnam.com">
    <img src="https://img.shields.io/badge/Checkout-adityakarnam.com-111827?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Checkout adityakarnam.com">
  </a>
</p>

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/Skill-Learn%20Anything%2024h-0f172a" alt="Skill"></a>
  <a href="#claude-code"><img src="https://img.shields.io/badge/Claude%20Code-supported-d97706" alt="Claude Code"></a>
  <a href="#codex"><img src="https://img.shields.io/badge/Codex-supported-2563eb" alt="Codex"></a>
  <a href="#hermes"><img src="https://img.shields.io/badge/Hermes-supported-16a34a" alt="Hermes"></a>
  <a href="#openclaw"><img src="https://img.shields.io/badge/OpenClaw-supported-0f766e" alt="OpenClaw"></a>
  <a href="#opencode"><img src="https://img.shields.io/badge/OpenCode-supported-7c2d12" alt="OpenCode"></a>
  <a href="#what-it-does"><img src="https://img.shields.io/badge/Mode-active%20learning-059669" alt="Mode"></a>
  <a href="#what-you-get"><img src="https://img.shields.io/badge/Output-final%20artifact-7c3aed" alt="Output"></a>
  <a href="https://github.com/adityak74/learn-anything-24h/stargazers"><img src="https://img.shields.io/github/stars/adityak74/learn-anything-24h?style=social" alt="GitHub stars"></a>
  <a href="https://github.com/adityak74/learn-anything-24h/blob/main/LICENSE"><img src="https://img.shields.io/github/license/adityak74/learn-anything-24h" alt="License"></a>
</p>

> Turn any hard topic into a focused 24-hour learning sprint.
>
> This is not a reading-list generator. It is a forced-output learning skill for Claude Code, Codex, Hermes, OpenClaw, and OpenCode that compresses a complex topic into an active-learning plan with exercises, teach-back prompts, and a required final artifact.
>
> **Promise:** operational fluency in one day, not fake mastery.

## Quick Start

1. Install the skill for your platform from the [Install](#install) section below.
2. Invoke it with a concrete outcome, for example:

```text
/learn-anything-24h Learn distributed systems for Staff Engineer interviews
```

3. Get a time-boxed sprint with concepts, exercises, traps, and a final artifact.

## What's Inside

Skill Description
`learn-anything-24h` Turns any hard topic into a focused 24-hour active-learning sprint with concrete exercises and a required proof-of-learning artifact.

## Why People Use It

- You need to get useful on a hard topic fast.
- You want output, not a giant reading list.
- You need interview-level, builder-level, or staff-level clarity quickly.
- You want a proof-of-learning artifact at the end, not vague confidence.

## Why This Exists

Most AI learning prompts fail in predictable ways:

- they generate huge reading lists
- they confuse breadth with usefulness
- they avoid retrieval practice
- they end with no proof of learning

`learn-anything-24h` fixes that by forcing:

- 80/20 concept mapping
- prerequisite compression
- active recall
- build / solve / derive work
- misconception checks
- a final artifact you can actually show

## What It Does

Given a topic, the skill produces a structured sprint with:

- a concrete target outcome
- the 5-9 concepts that matter most
- what to ignore for now
- a time-boxed learning schedule
- warm-up, applied, and hard questions
- teach-back prompts
- misconception traps
- a small resource strategy
- a final proof-of-learning artifact
- a 7-day continuation plan

It works especially well for:

- AI and ML systems
- software engineering domains
- research papers
- interview preparation
- architecture and staff-level topics
- learning-by-building projects

## What Changes When Active

- It prioritizes the few concepts that actually move the topic.
- It forces retrieval practice instead of passive reading.
- It gives you applied exercises that expose fake understanding quickly.
- It ends with a concrete artifact you can show, ship, or teach from.

## What You Get

Every run follows this structure:

```markdown
# 24-Hour Learning Sprint: <Topic>

## 0. Target Outcome
## 1. The 80/20 Map
## 2. Prerequisite Compression
## 3. 24-Hour Schedule
## 4. Exercises
## 5. Misconception Traps
## 6. Resource Strategy
## 7. Final Artifact
## 8. Mastery Rubric
## 9. Next 7 Days
```

## Example Prompts

```text
/learn-anything-24h Learn vLLM internals deeply enough to build one
/learn-anything-24h Learn distributed systems for Staff Engineer interviews
/learn-anything-24h Learn compilers by building a tiny interpreter
/learn-anything-24h Learn the Transformer architecture from first principles
/learn-anything-24h Learn MCP server architecture in 6 hours
```

## Best Use Cases

- `Interview prep`
  Ask for tradeoffs, likely questions, whiteboard explanations, and answer drills.
- `Learn by building`
  Ask for an implementation-focused sprint ending in working code.
- `Research understanding`
  Ask for a paper breakdown with equations, assumptions, and critique.
- `Staff-level systems`
  Ask for architecture, scaling, tradeoffs, and failure-mode thinking.
- `Crash-course fluency`
  Give a smaller time budget and force the same output structure.

## Install

Pick your platform below. Each section stays collapsed to keep the README compact.

<details>
<summary><strong>Claude Code</strong></summary>

```bash
claude marketplace add .
```

Or, from inside Claude Code:

```text
/plugin add
```

Files used:

```text
skills/claude/learn-anything-24h/SKILL.md
.claude-plugin/plugin.json
.claude-plugin/marketplace.json
```
</details>

<details>
<summary><strong>Codex</strong></summary>

```bash
codex marketplace add .
```

Or, from inside Codex:

```text
/plugin add
```

Files used:

```text
skills/codex/learn-anything-24h/SKILL.md
skills/codex/learn-anything-24h/agents/openai.yaml
.codex/skills/learn-anything-24h/SKILL.md
.codex/skills/learn-anything-24h/agents/openai.yaml
```
</details>

<details>
<summary><strong>Hermes</strong></summary>

```bash
mkdir -p ~/.hermes/skills/learn-anything-24h
cp skills/hermes/learn-anything-24h/SKILL.md ~/.hermes/skills/learn-anything-24h/SKILL.md
```

Then invoke it as:

```text
/learn-anything-24h Learn distributed systems for Staff Engineer interviews
```

Files used:

```text
skills/hermes/learn-anything-24h/SKILL.md
```
</details>

<details>
<summary><strong>OpenClaw</strong></summary>

Install into the current workspace:

```bash
openclaw skills install ./skills/openclaw/learn-anything-24h
```

Install globally for local agents:

```bash
openclaw skills install ./skills/openclaw/learn-anything-24h --global
```

Manual global install also works:

```bash
mkdir -p ~/.openclaw/skills/learn-anything-24h
cp skills/openclaw/learn-anything-24h/SKILL.md ~/.openclaw/skills/learn-anything-24h/SKILL.md
```

Files used:

```text
skills/openclaw/learn-anything-24h/SKILL.md
.agents/skills/learn-anything-24h/SKILL.md
```
</details>

<details>
<summary><strong>OpenCode</strong></summary>

Global install:

```bash
mkdir -p ~/.config/opencode/skills/learn-anything-24h
cp skills/opencode/learn-anything-24h/SKILL.md ~/.config/opencode/skills/learn-anything-24h/SKILL.md
```

This repo also ships a project-local OpenCode skill in:

```text
.opencode/skills/learn-anything-24h/SKILL.md
```

Files used:

```text
skills/opencode/learn-anything-24h/SKILL.md
.opencode/skills/learn-anything-24h/SKILL.md
.agents/skills/learn-anything-24h/SKILL.md
```
</details>

`install.sh` is still available for direct local skill installation across all supported platforms.

## Design Principles

- output over passive consumption
- practical usefulness over breadth
- honest scope over fake mastery
- resource minimalism over link spam
- artifact-based proof over vague understanding

## Good Fit

Use this skill when you want:

- a serious crash course on a difficult topic
- interview-focused preparation
- a learn-by-building sprint
- a paper-to-practice understanding loop
- a structured way to become useful fast

## Not For

This project does not try to:

- replace long-term deliberate practice
- guarantee full mastery in a day
- generate giant course catalogs
- act like a passive study assistant

## Share It

If you publish examples, demos, or forks, good showcase topics include:

- `Learn LLM inference engines deeply enough to build one`
- `Learn Kubernetes from first principles in 24 hours`
- `Learn distributed systems for senior/staff interviews`
- `Learn retrieval systems by building one`
- `Learn MCP by implementing a local server`

Best share format:

- the original prompt
- one screenshot of the generated sprint
- the final artifact produced from it

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=adityak74/learn-anything-24h&type=Date)](https://star-history.com/#adityak74/learn-anything-24h&Date)

## License

MIT


## 文件 .agents/skills/learn-anything-24h/SKILL.md

---
name: learn-anything-24h
description: Turn any complex topic into a 24-hour active-learning sprint with 80/20 concept mapping, prerequisite compression, active recall, hands-on exercises, teach-back prompts, and a final artifact.
license: MIT
compatibility: opencode
metadata:
  audience: engineers
  workflow: active-learning
---

# Learn Anything 24h

Use this skill when the user wants to learn a hard topic quickly and needs a serious plan rather than passive resources.

This skill produces operational fluency plans, not fake mastery claims.

Ask at most two clarifying questions, and only if the topic or intended outcome is materially unclear:

1. What is your current level: beginner, intermediate, or advanced?
2. What is your target outcome: interview, project, research, implementation, writing, or teaching?

Always produce this structure:

```markdown
# 24-Hour Learning Sprint: <Topic>

## 0. Target Outcome
## 1. The 80/20 Map
## 2. Prerequisite Compression
## 3. 24-Hour Schedule
## 4. Exercises
## 5. Misconception Traps
## 6. Resource Strategy
## 7. Final Artifact
## 8. Mastery Rubric
## 9. Next 7 Days
```

Bias toward output over passive consumption, and always end with a concrete artifact that proves applied understanding.


## 文件 .codex/skills/learn-anything-24h/SKILL.md

---
name: learn-anything-24h
description: Turn any complex topic into a 24-hour active-learning sprint with 80/20 concept mapping, prerequisite compression, active recall, hands-on exercises, teach-back prompts, and a final artifact. Use when the user wants to learn, understand, crash-course, prepare for, or become operationally fluent in a difficult topic quickly.
metadata:
  short-description: Turn any hard topic into a 24-hour active-learning sprint.
---

# Learn Anything 24h

Use this skill when the user wants to learn a hard topic quickly and needs a serious plan rather than passive resources.

This skill produces operational fluency plans, not fake mastery claims.

## Invocation

- This skill is invoked by mentioning `$learn-anything-24h`.
- Treat the remaining user text as the learning request.
- If the request is already specific enough, do not ask clarifying questions.

## Default Assumptions

If the user does not specify otherwise, assume:

- learner level: strong software engineer
- time budget: 24 hours
- learning style: active recall, implementation, and teach-back
- outcome: explain + apply + build
- output quality: professional and concrete

Ask at most two clarifying questions, and only if the topic or intended outcome is materially unclear:

1. What is your current level: beginner, intermediate, or advanced?
2. What is your target outcome: interview, project, research, implementation, writing, or teaching?

## Core Behavior

Build a compressed learning sprint around:

1. ruthless 80/20 prioritization
2. prerequisite compression
3. active recall
4. applied work
5. a required final artifact

Bias toward output. The user should leave with tasks, exercises, and a proof-of-learning artifact.

Avoid:

- giant reading lists
- vague study advice
- generic motivational language
- long link dumps
- passive "watch these videos" plans
- claims of guaranteed mastery

## Mode Detection

Infer the mode from the request. If multiple modes fit, choose the one closest to the user's stated goal.

- `default`: general learning sprint
- `interview`: prioritize tradeoffs, whiteboarding, explanation, and likely questions
- `builder`: prioritize implementation, debugging, and hands-on milestones
- `research`: prioritize papers, assumptions, equations, experiments, and critique
- `staff-engineer`: prioritize architecture, scaling, tradeoffs, failure modes, and decision quality
- `paper`: convert a specific paper into an understanding sprint
- `crash`: use the same structure compressed to the stated time budget

Mode cues:

- "for interviews", "interview prep" -> `interview`
- "by building", "implement", "project" -> `builder`
- "paper", "from the paper", "research" -> `paper` or `research`
- "staff engineer", "architecture", "scaling" -> `staff-engineer`
- explicit sub-24-hour deadline -> `crash`

## Output Contract

Always produce this structure:

```markdown
# 24-Hour Learning Sprint: <Topic>

## 0. Target Outcome
## 1. The 80/20 Map
## 2. Prerequisite Compression
## 3. 24-Hour Schedule
## 4. Exercises
## 5. Misconception Traps
## 6. Resource Strategy
## 7. Final Artifact
## 8. Mastery Rubric
## 9. Next 7 Days
```

If the user gives a different time budget, keep the same section structure and rename the title to match the stated duration.

## Section Requirements

### 0. Target Outcome

Define a concrete end state. Use "By the end of this sprint, you should be able to..." and make it observable.

### 1. The 80/20 Map

List 5-9 concepts.

For each concept, include:

- why it matters
- what confusion it removes
- a simple analogy
- a practical example

### 2. Prerequisite Compression

Split prerequisites into:

- `Must know`
- `Can ignore for now`
- `Learn only if blocked`

Aggressively reduce prerequisite sprawl.

### 3. Schedule

Default 24-hour schedule:

```markdown
### Hour 0-1: Orientation
### Hour 1-3: Foundations
### Hour 3-6: Mechanisms
### Hour 6-9: Guided Examples
### Hour 9-12: Build / Solve / Derive
### Hour 12-16: Advanced Concepts
### Hour 16-20: Independent Challenge
### Hour 20-22: Retrieval and Feynman Test
### Hour 22-24: Final Artifact
```

Each time block must include:

- goal
- what to learn
- what to do
- output
- self-check question

For `crash` mode, compress proportionally while preserving orientation, foundations, applied work, retrieval, and final artifact.

### 4. Exercises

Always include:

- 5 warm-up questions
- 5 applied questions
- 5 hard questions
- 3 teach-back prompts
- 1 final boss challenge

Questions must be topic-specific and should expose shallow understanding quickly.

### 5. Misconception Traps

List common wrong mental models using this pattern:

```markdown
Wrong model: ...
Correct model: ...
```

Favor misconceptions that would cause bad design choices or wrong explanations.

### 6. Resource Strategy

Recommend categories, not a dump of links.

Default structure:

1. one canonical doc, book, or paper
2. one implementation or repository
3. one high-quality lecture or video
4. one hands-on exercise

If the user explicitly asks for current links, recommendations, or latest sources, gather them. Otherwise stay focused and minimal.

### 7. Final Artifact

Every sprint must end with a required artifact selected from the user's goal:

- `interview` -> answer bank + system design explanation
- `project` or `builder` -> working implementation
- `research` or `paper` -> paper memo + derivation notes
- `writing` -> technical blog post
- `teaching` -> lesson plan + explain-back script
- `staff-engineer` or `architecture` -> design doc + diagram
- `debugging` -> checklist + failure-mode guide

If no clear mapping exists, choose the artifact that best proves applied understanding.

### 8. Mastery Rubric

Define four levels:

- Beginner
- Useful
- Strong
- Expert

Keep the rubric concrete and measurable. "Useful" should mean the learner can actually do something with the topic.

### 9. Next 7 Days

Provide a lightweight continuation plan to avoid false confidence after the sprint.

## Style

Write with these qualities:

- intense
- practical


## 文件 .opencode/skills/learn-anything-24h/SKILL.md

---
name: learn-anything-24h
description: Turn any complex topic into a 24-hour active-learning sprint with 80/20 concept mapping, prerequisite compression, active recall, hands-on exercises, teach-back prompts, and a final artifact.
license: MIT
compatibility: opencode
metadata:
  audience: engineers
  workflow: active-learning
---

## What I do

- Turn a hard topic into a time-boxed active-learning sprint.
- Prioritize the 5-9 concepts that matter most.
- Force exercises, teach-back, and a final proof-of-learning artifact.

## When to use me

Use this when you want a serious crash course on a difficult topic and need output rather than passive study advice.

If the request is already specific enough, do not ask clarifying questions.

Ask at most two clarifying questions only when needed:

1. What is your current level: beginner, intermediate, or advanced?
2. What is your target outcome: interview, project, research, implementation, writing, or teaching?

Always produce this structure:

```markdown
# 24-Hour Learning Sprint: <Topic>

## 0. Target Outcome
## 1. The 80/20 Map
## 2. Prerequisite Compression
## 3. 24-Hour Schedule
## 4. Exercises
## 5. Misconception Traps
## 6. Resource Strategy
## 7. Final Artifact
## 8. Mastery Rubric
## 9. Next 7 Days
```

Avoid giant reading lists, vague study advice, and fake mastery claims.


## 文件 skills/claude/learn-anything-24h/SKILL.md

---
name: learn-anything-24h
description: Turn any complex topic into a 24-hour active-learning sprint with 80/20 concept mapping, prerequisite compression, active recall, hands-on exercises, teach-back prompts, and a final artifact. Use when the user wants to learn, understand, crash-course, prepare for, or become operationally fluent in a difficult topic quickly.
---

# Learn Anything 24h

Use this skill when the user wants to learn a hard topic quickly and needs a serious plan rather than passive resources.

This skill produces operational fluency plans, not fake mastery claims.

## Default Assumptions

If the user does not specify otherwise, assume:

- learner level: strong software engineer
- time budget: 24 hours
- learning style: active recall, implementation, and teach-back
- outcome: explain + apply + build
- output quality: professional and concrete

Ask at most two clarifying questions, and only if the topic or intended outcome is materially unclear:

1. What is your current level: beginner, intermediate, or advanced?
2. What is your target outcome: interview, project, research, implementation, writing, or teaching?

If the prompt is already specific enough, do not ask and proceed.

## Core Behavior

Build a compressed learning sprint around:

1. ruthless 80/20 prioritization
2. prerequisite compression
3. active recall
4. applied work
5. a required final artifact

Bias toward output. The user should leave with tasks, exercises, and a proof-of-learning artifact.

Avoid:

- giant reading lists
- vague study advice
- generic motivational language
- long link dumps
- passive "watch these videos" plans
- claims of guaranteed mastery

## Mode Detection

Infer the mode from the request. If multiple modes fit, choose the one closest to the user's stated goal.

- `default`: general learning sprint
- `interview`: prioritize tradeoffs, whiteboarding, explanation, and likely questions
- `builder`: prioritize implementation, debugging, and hands-on milestones
- `research`: prioritize papers, assumptions, equations, experiments, and critique
- `staff-engineer`: prioritize architecture, scaling, tradeoffs, failure modes, and decision quality
- `paper`: convert a specific paper into an understanding sprint
- `crash`: use the same structure compressed to the stated time budget

Mode cues:

- "for interviews", "interview prep" -> `interview`
- "by building", "implement", "project" -> `builder`
- "paper", "from the paper", "research" -> `paper` or `research`
- "staff engineer", "architecture", "scaling" -> `staff-engineer`
- explicit sub-24-hour deadline -> `crash`

## Output Contract

Always produce this structure:

```markdown
# 24-Hour Learning Sprint: <Topic>

## 0. Target Outcome
## 1. The 80/20 Map
## 2. Prerequisite Compression
## 3. 24-Hour Schedule
## 4. Exercises
## 5. Misconception Traps
## 6. Resource Strategy
## 7. Final Artifact
## 8. Mastery Rubric
## 9. Next 7 Days
```

If the user gives a different time budget, keep the same section structure and rename the title to match the stated duration.

## Section Requirements

### 0. Target Outcome

Define a concrete end state. Use "By the end of this sprint, you should be able to..." and make it observable.

### 1. The 80/20 Map

List 5-9 concepts.

For each concept, include:

- why it matters
- what confusion it removes
- a simple analogy
- a practical example

### 2. Prerequisite Compression

Split prerequisites into:

- `Must know`
- `Can ignore for now`
- `Learn only if blocked`

Aggressively reduce prerequisite sprawl.

### 3. Schedule

Default 24-hour schedule:

```markdown
### Hour 0-1: Orientation
### Hour 1-3: Foundations
### Hour 3-6: Mechanisms
### Hour 6-9: Guided Examples
### Hour 9-12: Build / Solve / Derive
### Hour 12-16: Advanced Concepts
### Hour 16-20: Independent Challenge
### Hour 20-22: Retrieval and Feynman Test
### Hour 22-24: Final Artifact
```

Each time block must include:

- goal
- what to learn
- what to do
- output
- self-check question

For `crash` mode, compress proportionally while preserving orientation, foundations, applied work, retrieval, and final artifact.

### 4. Exercises

Always include:

- 5 warm-up questions
- 5 applied questions
- 5 hard questions
- 3 teach-back prompts
- 1 final boss challenge

Questions must be topic-specific and should expose shallow understanding quickly.

### 5. Misconception Traps

List common wrong mental models using this pattern:

```markdown
Wrong model: ...
Correct model: ...
```

Favor misconceptions that would cause bad design choices or wrong explanations.

### 6. Resource Strategy

Recommend categories, not a dump of links.

Default structure:

1. one canonical doc, book, or paper
2. one implementation or repository
3. one high-quality lecture or video
4. one hands-on exercise

If the user explicitly asks for current links, recommendations, or latest sources, gather them. Otherwise stay focused and minimal.

### 7. Final Artifact

Every sprint must end with a required artifact selected from the user's goal:

- `interview` -> answer bank + system design explanation
- `project` or `builder` -> working implementation
- `research` or `paper` -> paper memo + derivation notes
- `writing` -> technical blog post
- `teaching` -> lesson plan + explain-back script
- `staff-engineer` or `architecture` -> design doc + diagram
- `debugging` -> checklist + failure-mode guide

If no clear mapping exists, choose the artifact that best proves applied understanding.

### 8. Mastery Rubric

Define four levels:

- Beginner
- Useful
- Strong
- Expert

Keep the rubric concrete and measurable. "Useful" should mean the learner can actually do something with the topic.

### 9. Next 7 Days

Provide a lightweight continuation plan to avoid false confidence after the sprint.

## Style

Write with these qualities:

- intense
- practical
- concise
- structured
- high-signal
- honest about limits
- biased toward action

The user should feel:

- I know exactly what to do next.
- I know what matters and what I can ignore.
- I have exercises that will reveal whether I actually understand this.
- I will end with something I can show or use.

## Anti-Patterns

Do not:

- output a generic study plan with weak verbs like "explore" or "review"
- list more than a few core resources unless the user explicitly asks
- confuse breadth with usefulness
- hide the final artifact until the end
- over-explain easy background instead of prioritizing the topic's core mechanisms
- claim the user will completely master the topic in one day

Preferred framing:

`Operational fluency in one day, not fake mastery.`

## Examples

User:

```text
Learn vLLM internals deeply enough to build one
```

Behavior:

- choose `builder` mode
- emphasize inference lifecycle, batching, KV cache, scheduling, and memory constraints
- require a toy inference engine design or implementation artifact

User:

```text
Learn distributed systems for Staff Engineer interviews
```

Behavior:

- choose `staff-engineer` + `interview` priority
- emphasize tradeoffs, failure modes, replication, partitioning, consistency, and system design explanations
- require an answer bank and architecture walkthrough artifact

User:

```text
Learn the Transformer architecture from first principles in 6 hours
```

Behavior:

- choose `crash` mode
- keep the full structure
- compress the schedule and exercises while preserving active recall and a final artifact

## Safety

For dangerous, illegal, or harmful topics, redirect toward safe, defensive, educational, or policy-compliant learning paths.


## 文件 skills/codex/learn-anything-24h/SKILL.md

---
name: learn-anything-24h
description: Turn any complex topic into a 24-hour active-learning sprint with 80/20 concept mapping, prerequisite compression, active recall, hands-on exercises, teach-back prompts, and a final artifact. Use when the user wants to learn, understand, crash-course, prepare for, or become operationally fluent in a difficult topic quickly.
metadata:
  short-description: Turn any hard topic into a 24-hour active-learning sprint.
---

# Learn Anything 24h

Use this skill when the user wants to learn a hard topic quickly and needs a serious plan rather than passive resources.

This skill produces operational fluency plans, not fake mastery claims.

## Invocation

- This skill is invoked by mentioning `$learn-anything-24h`.
- Treat the remaining user text as the learning request.
- If the request is already specific enough, do not ask clarifying questions.

## Default Assumptions

If the user does not specify otherwise, assume:

- learner level: strong software engineer
- time budget: 24 hours
- learning style: active recall, implementation, and teach-back
- outcome: explain + apply + build
- output quality: professional and concrete

Ask at most two clarifying questions, and only if the topic or intended outcome is materially unclear:

1. What is your current level: beginner, intermediate, or advanced?
2. What is your target outcome: interview, project, research, implementation, writing, or teaching?

## Core Behavior

Build a compressed learning sprint around:

1. ruthless 80/20 prioritization
2. prerequisite compression
3. active recall
4. applied work
5. a required final artifact

Bias toward output. The user should leave with tasks, exercises, and a proof-of-learning artifact.

Avoid:

- giant reading lists
- vague study advice
- generic motivational language
- long link dumps
- passive "watch these videos" plans
- claims of guaranteed mastery

## Mode Detection

Infer the mode from the request. If multiple modes fit, choose the one closest to the user's stated goal.

- `default`: general learning sprint
- `interview`: prioritize tradeoffs, whiteboarding, explanation, and likely questions
- `builder`: prioritize implementation, debugging, and hands-on milestones
- `research`: prioritize papers, assumptions, equations, experiments, and critique
- `staff-engineer`: prioritize architecture, scaling, tradeoffs, failure modes, and decision quality
- `paper`: convert a specific paper into an understanding sprint
- `crash`: use the same structure compressed to the stated time budget

Mode cues:

- "for interviews", "interview prep" -> `interview`
- "by building", "implement", "project" -> `builder`
- "paper", "from the paper", "research" -> `paper` or `research`
- "staff engineer", "architecture", "scaling" -> `staff-engineer`
- explicit sub-24-hour deadline -> `crash`

## Output Contract

Always produce this structure:

```markdown
# 24-Hour Learning Sprint: <Topic>

## 0. Target Outcome
## 1. The 80/20 Map
## 2. Prerequisite Compression
## 3. 24-Hour Schedule
## 4. Exercises
## 5. Misconception Traps
## 6. Resource Strategy
## 7. Final Artifact
## 8. Mastery Rubric
## 9. Next 7 Days
```

If the user gives a different time budget, keep the same section structure and rename the title to match the stated duration.

## Section Requirements

### 0. Target Outcome

Define a concrete end state. Use "By the end of this sprint, you should be able to..." and make it observable.

### 1. The 80/20 Map

List 5-9 concepts.

For each concept, include:

- why it matters
- what confusion it removes
- a simple analogy
- a practical example

### 2. Prerequisite Compression

Split prerequisites into:

- `Must know`
- `Can ignore for now`
- `Learn only if blocked`

Aggressively reduce prerequisite sprawl.

### 3. Schedule

Default 24-hour schedule:

```markdown
### Hour 0-1: Orientation
### Hour 1-3: Foundations
### Hour 3-6: Mechanisms
### Hour 6-9: Guided Examples
### Hour 9-12: Build / Solve / Derive
### Hour 12-16: Advanced Concepts
### Hour 16-20: Independent Challenge
### Hour 20-22: Retrieval and Feynman Test
### Hour 22-24: Final Artifact
```

Each time block must include:

- goal
- what to learn
- what to do
- output
- self-check question

For `crash` mode, compress proportionally while preserving orientation, foundations, applied work, retrieval, and final artifact.

### 4. Exercises

Always include:

- 5 warm-up questions
- 5 applied questions
- 5 hard questions
- 3 teach-back prompts
- 1 final boss challenge

Questions must be topic-specific and should expose shallow understanding quickly.

### 5. Misconception Traps

List common wrong mental models using this pattern:

```markdown
Wrong model: ...
Correct model: ...
```

Favor misconceptions that would cause bad design choices or wrong explanations.

### 6. Resource Strategy

Recommend categories, not a dump of links.

Default structure:

1. one canonical doc, book, or paper
2. one implementation or repository
3. one high-quality lecture or video
4. one hands-on exercise

If the user explicitly asks for current links, recommendations, or latest sources, gather them. Otherwise stay focused and minimal.

### 7. Final Artifact

Every sprint must end with a required artifact selected from the user's goal:

- `interview` -> answer bank + system design explanation
- `project` or `builder` -> working implementation
- `research` or `paper` -> paper memo + derivation notes
- `writing` -> technical blog post
- `teaching` -> lesson plan + explain-back script
- `staff-engineer` or `architecture` -> design doc + diagram
- `debugging` -> checklist + failure-mode guide

If no clear mapping exists, choose the artifact that best proves applied understanding.

### 8. Mastery Rubric

Define four levels:

- Beginner
- Useful
- Strong
- Expert

Keep the rubric concrete and measurable. "Useful" should mean the learner can actually do something with the topic.

### 9. Next 7 Days

Provide a lightweight continuation plan to avoid false confidence after the sprint.

## Style

Write with these qualities:

- intense
- practical
- concise
- structured
- high-signal
- honest about limits
- biased toward action

The user should feel:

- I know exactly what to do next.
- I know what matters and what I can ignore.
- I have exercises that will reveal whether I actually understand this.
- I will end with something I can show or use.

## Anti-Patterns

Do not:

- output a generic study plan with weak verbs like "explore" or "review"
- list more than a few core resources unless the user explicitly asks
- confuse breadth with usefulness
- hide the final artifact until the end
- over-explain easy background instead of prioritizing the topic's core mechanisms
- claim the user will completely master the topic in one day

Preferred framing:

`Operational fluency in one day, not fake mastery.`

## Examples

User:

```text
Learn vLLM internals deeply enough to build one
```

Behavior:

- choose `builder` mode
- emphasize inference lifecycle, batching, KV cache, scheduling, and memory constraints
- require a toy inference engine design or implementation artifact

User:

```text
Learn distributed systems for Staff Engineer interviews
```

Behavior:

- choose `staff-engineer` + `interview` priority
- emphasize tradeoffs, failure modes, replication, partitioning, consistency, and system design explanations
- require an answer bank and architecture walkthrough artifact

User:

```text
Learn the Transformer architecture from first principles in 6 hours
```

Behavior:

- choose `crash` mode
- keep the full structure
- compress the schedule and exercises while preserving active recall and a final artifact

## Safety

For dangerous, illegal, or harmful topics, redirect toward safe, defensive, educational, or policy-compliant learning paths.


## 文件 skills/hermes/learn-anything-24h/SKILL.md

---
name: learn-anything-24h
description: Turn any complex topic into a 24-hour active-learning sprint with 80/20 concept mapping, prerequisite compression, active recall, hands-on exercises, teach-back prompts, and a final artifact.
version: 1.0.0
metadata:
  hermes:
    tags: [learning, education, study-system, active-recall]
    category: education
---

# Learn Anything 24h

## When to Use

Use this skill when the user wants to learn a hard topic quickly and needs a serious plan rather than passive resources.

This skill produces operational fluency plans, not fake mastery claims.

## Invocation

- Hermes exposes installed skills as slash commands, so this skill should be available as `/learn-anything-24h`.
- Treat the remaining user text as the learning request.
- If the request is already specific enough, do not ask clarifying questions.

## Default Assumptions

If the user does not specify otherwise, assume:

- learner level: strong software engineer
- time budget: 24 hours
- learning style: active recall, implementation, and teach-back
- outcome: explain + apply + build
- output quality: professional and concrete

Ask at most two clarifying questions, and only if the topic or intended outcome is materially unclear:

1. What is your current level: beginner, intermediate, or advanced?
2. What is your target outcome: interview, project, research, implementation, writing, or teaching?

## Procedure

Build a compressed learning sprint around:

1. ruthless 80/20 prioritization
2. prerequisite compression
3. active recall
4. applied work
5. a required final artifact

Bias toward output. The user should leave with tasks, exercises, and a proof-of-learning artifact.

Infer the mode from the request. If multiple modes fit, choose the one closest to the user's stated goal.

- `default`: general learning sprint
- `interview`: prioritize tradeoffs, whiteboarding, explanation, and likely questions
- `builder`: prioritize implementation, debugging, and hands-on milestones
- `research`: prioritize papers, assumptions, equations, experiments, and critique
- `staff-engineer`: prioritize architecture, scaling, tradeoffs, failure modes, and decision quality
- `paper`: convert a specific paper into an understanding sprint
- `crash`: use the same structure compressed to the stated time budget

Mode cues:

- "for interviews", "interview prep" -> `interview`
- "by building", "implement", "project" -> `builder`
- "paper", "from the paper", "research" -> `paper` or `research`
- "staff engineer", "architecture", "scaling" -> `staff-engineer`
- explicit sub-24-hour deadline -> `crash`

Always produce this structure:

```markdown
# 24-Hour Learning Sprint: <Topic>

## 0. Target Outcome
## 1. The 80/20 Map
## 2. Prerequisite Compression
## 3. 24-Hour Schedule
## 4. Exercises
## 5. Misconception Traps
## 6. Resource Strategy
## 7. Final Artifact
## 8. Mastery Rubric
## 9. Next 7 Days
```

If the user gives a different time budget, keep the same section structure and rename the title to match the stated duration.

Section requirements:

- `0. Target Outcome`: define a concrete observable end state using "By the end of this sprint, you should be able to..."
- `1. The 80/20 Map`: list 5-9 concepts, and for each include why it matters, what confusion it removes, a simple analogy, and a practical example
- `2. Prerequisite Compression`: split into `Must know`, `Can ignore for now`, and `Learn only if blocked`
- `3. 24-Hour Schedule`: include goal, what to learn, what to do, output, and a self-check question for each time block
- `4. Exercises`: include 5 warm-up, 5 applied, 5 hard questions, 3 teach-back prompts, and 1 final boss challenge
- `5. Misconception Traps`: use `Wrong model:` and `Correct model:` pairs
- `6. Resource Strategy`: recommend categories rather than dumping links unless the user explicitly asks for current links or latest sources
- `7. Final Artifact`: choose an artifact that proves applied understanding and matches the user goal
- `8. Mastery Rubric`: define `Beginner`, `Useful`, `Strong`, and `Expert` concretely
- `9. Next 7 Days`: provide a lightweight continuation plan

Default 24-hour schedule:

```markdown
### Hour 0-1: Orientation
### Hour 1-3: Foundations
### Hour 3-6: Mechanisms
### Hour 6-9: Guided Examples
### Hour 9-12: Build / Solve / Derive
### Hour 12-16: Advanced Concepts
### Hour 16-20: Independent Challenge
### Hour 20-22: Retrieval and Feynman Test
### Hour 22-24: Final Artifact
```

For `crash` mode, compress proportionally while preserving orientation, foundations, applied work, retrieval, and final artifact.

## Pitfalls

Do not:

- output a generic study plan with weak verbs like "explore" or "review"
- list more than a few core resources unless the user explicitly asks
- confuse breadth with usefulness
- hide the final artifact until the end
- over-explain easy background instead of prioritizing the topic's core mechanisms
- claim the user will completely master the topic in one day
- generate giant reading lists, vague study advice, generic motivational language, or long link dumps

Preferred framing:

`Operational fluency in one day, not fake mastery.`

## Verification

The response should make the user feel:

- I know exactly what to do next.
- I know what matters and what I can ignore.
- I have exercises that will reveal whether I actually understand this.
- I will end with something I can show or use.


## 文件 skills/openclaw/learn-anything-24h/SKILL.md

---
name: learn-anything-24h
description: Turn any complex topic into a 24-hour active-learning sprint with 80/20 concept mapping, prerequisite compression, active recall, hands-on exercises, teach-back prompts, and a final artifact.
license: MIT
homepage: https://github.com/adityak74/learn-anything-24h
metadata:
  openclaw:
    homepage: https://github.com/adityak74/learn-anything-24h
---

# Learn Anything 24h

## When to use

Use this skill when the user wants to learn a hard topic quickly and needs a serious plan rather than passive resources.

This skill produces operational fluency plans, not fake mastery claims.

## Invocation

- OpenClaw exposes user-invocable skills as slash commands, so this skill should be available as `/learn-anything-24h`.
- Treat the remaining user text as the learning request.
- If the request is already specific enough, do not ask clarifying questions.

## Procedure

Assume the learner is a strong software engineer unless the user says otherwise.

Ask at most two clarifying questions, and only if the topic or intended outcome is materially unclear:

1. What is your current level: beginner, intermediate, or advanced?
2. What is your target outcome: interview, project, research, implementation, writing, or teaching?

Build a compressed learning sprint around:

1. ruthless 80/20 prioritization
2. prerequisite compression
3. active recall
4. applied work
5. a required final artifact

Infer the mode from the request:

- `default`
- `interview`
- `builder`
- `research`
- `staff-engineer`
- `paper`
- `crash`

Always produce this structure:

```markdown
# 24-Hour Learning Sprint: <Topic>

## 0. Target Outcome
## 1. The 80/20 Map
## 2. Prerequisite Compression
## 3. 24-Hour Schedule
## 4. Exercises
## 5. Misconception Traps
## 6. Resource Strategy
## 7. Final Artifact
## 8. Mastery Rubric
## 9. Next 7 Days
```

Requirements:

- list 5-9 core concepts in the 80/20 map
- compress prerequisites into `Must know`, `Can ignore for now`, and `Learn only if blocked`
- include a time-boxed schedule with goal, learning task, action, output, and self-check
- include 5 warm-up, 5 applied, and 5 hard questions
- include 3 teach-back prompts and 1 final boss challenge
- choose a final artifact that proves applied understanding
- keep resources minimal unless the user explicitly asks for current links or latest recommendations

## Pitfalls

Do not:

- output giant reading lists
- give vague study advice
- confuse breadth with usefulness
- hide the final artifact until the end
- claim the user will fully master the topic in one day

Preferred framing:

`Operational fluency in one day, not fake mastery.`

## Verification

The response should leave the user with a concrete plan, concrete exercises, and a clear artifact to produce.


## 文件 skills/opencode/learn-anything-24h/SKILL.md

---
name: learn-anything-24h
description: Turn any complex topic into a 24-hour active-learning sprint with 80/20 concept mapping, prerequisite compression, active recall, hands-on exercises, teach-back prompts, and a final artifact.
license: MIT
compatibility: opencode
metadata:
  audience: engineers
  workflow: active-learning
---

## What I do

- Turn a hard topic into a time-boxed active-learning sprint.
- Prioritize the 5-9 concepts that matter most.
- Force exercises, teach-back, and a final proof-of-learning artifact.

## When to use me

Use this when you want a serious crash course on a difficult topic and need output rather than passive study advice.

If the request is already specific enough, do not ask clarifying questions.

Ask at most two clarifying questions only when needed:

1. What is your current level: beginner, intermediate, or advanced?
2. What is your target outcome: interview, project, research, implementation, writing, or teaching?

Always produce this structure:

```markdown
# 24-Hour Learning Sprint: <Topic>

## 0. Target Outcome
## 1. The 80/20 Map
## 2. Prerequisite Compression
## 3. 24-Hour Schedule
## 4. Exercises
## 5. Misconception Traps
## 6. Resource Strategy
## 7. Final Artifact
## 8. Mastery Rubric
## 9. Next 7 Days
```

Bias toward action:

- ruthless 80/20 prioritization
- prerequisite compression
- active recall
- applied work
- a required final artifact

Avoid giant reading lists, vague study advice, and fake mastery claims.

