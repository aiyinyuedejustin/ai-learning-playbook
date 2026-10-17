# Nitzan94/claude-code-skills：AI tutor 等

- 链接：https://github.com/Nitzan94/claude-code-skills
- 作者：Nitzan94
- 仓库说明：Collection of Claude Code skills - AI tutor, prompt optimizer, AWS AgentCore, Chrome extensions
- 星数：11
- 获取方式：GitHub README + SKILL/说明文件

---

## README

# Claude Code Skills

A collection of skills for Claude Code - specialized knowledge modules that turn Claude into an expert at specific tasks.

## What are Skills?

Skills are markdown files that give Claude Code domain expertise. Instead of explaining what you want every time, you invoke a skill and Claude knows exactly what to do.

## Available Skills

| Skill | Description |
|-------|-------------|
| [sync-context](skills/sync-context/) | End-of-session context sync. Reviews what was learned and persists it into project context files so the next session starts up to date. |
| [skillify](skills/skillify/) | Turns the session you just finished into a reusable skill. Reads the JSONL, interviews you in four structured rounds, writes a clean SKILL.md with per-step success criteria. |
| [skill-tutor](skills/skill-tutor/) | Personal AI tutor with spaced repetition. Creates tutorials using YOUR projects, tracks learning progress, quizzes you at optimal intervals. |
| [optimize-prompt](skills/optimize-prompt/) | Evolves prompts using genetic algorithms. Give it test cases, it finds the prompt that works. |
| [deploy-agentcore](skills/deploy-agentcore/) | Deploy Python agents to AWS Bedrock AgentCore. Serverless hosting with memory, auth, and observability. |
| [chrome-extension](skills/chrome-extension/) | Build Chrome extensions with Manifest V3. Scaffolding, patterns, debugging. |
| [model-audit](skills/model-audit/) | Reads the dispatch log written by the `model-routing` hook and shows whether subagents are running on the model tiers you intended. Pairs with `hooks/model-routing`. |

## Hooks

Mechanical guardrails that run in the Claude Code harness — not skills, but artifacts you wire into `~/.claude/settings.json`.

| Hook | Description |
|------|-------------|
| [model-routing](hooks/model-routing/) | PreToolUse hook that blocks `Agent`/`Task` dispatches without an explicit `model` parameter. Kills the silent default where subagents inherit the parent's model (almost always Opus). Ships with the rule, the hook script, an audit script, and a settings snippet. Pairs with the `model-audit` skill. |

## Installation

Copy any skill folder to your Claude Code skills directory:

```bash
# Clone the repo
git clone https://github.com/Nitzan94/claude-code-skills.git

# Copy a skill (example: skill-tutor)
cp -r claude-code-skills/skills/skill-tutor ~/.claude/skills/
```

Or copy all skills:
```bash
cp -r claude-code-skills/skills/* ~/.claude/skills/
```

## Usage

In Claude Code, either:
- Invoke directly: `/skill-tutor`, `/optimize-prompt`, etc.
- Use trigger phrases: "teach me", "optimize this prompt", "deploy to agentcore"

## Creating Your Own Skills

Each skill is a folder with:
```
skill-name/
├── SKILL.md          # Main skill definition (required)
├── README.md         # Documentation
├── references/       # Domain knowledge files
├── workflows/        # Step-by-step guides
├── templates/        # Code templates
└── scripts/          # Helper scripts
```

See any skill folder for examples.

## License

MIT


## 文件 skills/init-context/SKILL.md

---
name: init-context
description: "Bootstrap progressive disclosure context architecture in any project. Turns CLAUDE.md into a router with a task-based routing table, consolidates context into a single knowledge directory, and cleans MEMORY.md into a pure index. Use when starting a new project, when CLAUDE.md has 'always read' directives, when context feels bloated, or when the user says /init-context."
---

# /init-context

Turn CLAUDE.md into a router, not a database.

The core problem: inline domain knowledge in CLAUDE.md loads tokens before the model knows the task. This isn't just wasteful — irrelevant context actively degrades reasoning quality. The fix is a routing table: load nothing by default, route to the right file based on the task.

**Arguments:** "$ARGUMENTS"

## Audit

Read the project root and report what exists with line counts:

- `CLAUDE.md` — classify: **router** (mostly pointers/structure) or **database** (inline domain knowledge, architecture details, conventions beyond the essential)
- `MEMORY.md` or auto-memory files — classify: **pure index** (one-liner pointers) or **hybrid** (mix of pointers and inline content)
- Context directories (`knowledge/`, `context/`, `docs/`) — what exists, any duplication
- Subdirectory `CLAUDE.md` files — any per-module instructions
- `README.md` — project description if no CLAUDE.md

Look for these red flags:
- "Always read" or "Before any task, read" directives
- Inline paragraphs of domain knowledge in CLAUDE.md or MEMORY.md
- Multiple context directories (`docs/` AND `context/` AND `knowledge/`)
- Context files that are always loaded but only relevant to specific task types

Report findings to the user before changing anything.

## Understand the Project

Extract the project's purpose from existing files. If nothing exists, ask:
1. What does this project do?
2. What are the main modules or areas of work?
3. What context do you find yourself repeatedly explaining to Claude in this repo?

That third question identifies exactly what should become routed context files — if you keep explaining it, it should be written down and loaded on demand.

## Classify Context: Cross-Cutting vs Task-Specific

Before designing the routing table, sort every piece of context into two buckets:

**Cross-cutting** (stays in CLAUDE.md) — information needed by most task types. Examples: template variable names used across the codebase, shared terminology, project-wide conventions, commands, deploy essentials. The test: if more than half the routing table rows would need it, it's cross-cutting.

**Task-specific** (goes in a knowledge file) — information only relevant to one or two task types. Examples: matching algorithm details, GCP IAM roles, deploy troubleshooting steps, feature specs.

Getting this wrong is the #1 source of problems. If you bury a cross-cutting concern in a task-specific file, the routing table actively blocks access to it for other tasks.

## Design the Routing Table

Build a task-based routing table that maps natural task descriptions to context files. Present it for confirmation before proceeding.

```markdown
## Context Loading

Do NOT read knowledge/ files upfront. Load only what the task requires:

| Task type | Load these files |
|---|---|
| [natural task description] | [1-2 specific file paths] |
```

Routing table principles:
- Every file load is conditional on the task — no "always read"
- Each row maps to 1-2 files maximum, not a whole directory
- The task descriptions in the left column should be specific enough that the model can match its current task without ambiguity
- If subdirectories have their own CLAUDE.md (auto-loaded when working there), note that in the table so context isn't double-loaded

## Scaffold

Apply the routing table to the project. The goal for each file:

**CLAUDE.md** — a router. Contains: project description, routing table, repo structure map, essential commands, deploy essentials, and cross-cutting context identified above. Does not contain: task-specific domain knowledge, architecture deep-dives, lengthy conventions. The test: if a section is only relevant to some tasks, it belongs in a knowledge file referenced from the routing table, not inline.

### One directory, not two

All context files go in ONE directory. Choose a descriptive name — `knowledge/` is a good default because it signals "on-demand context for the model" vs generic `docs/` which could mean anything.

**If a context directory already exists** (`docs/`, `context/`, etc.): rename it to `knowledge/` (or whatever name fits the project) and consolidate. Do NOT create a parallel directory. Use `git mv` to preserve history.

**If no context directory exists**: create `knowledge/` and extract task-specific content from CLAUDE.md into it.

### Deduplication

Before writing any new knowledge file, check for content overlap with existing files in the same directory. If two files cover the same topic:
- Keep the more detailed version
- Remove the duplicate content from the other
- Never have the same information in two places

### MEMORY.md

If auto-memory exists: MEMORY.md should be a pure index of one-liner pointers to individual memory files. Any inline content (paragraphs, technical details, gotchas) gets extracted into its own memory file. The index entry for each file should be descriptive enough that the model can decide relevance without opening it.

## Verify

After scaffolding, check:
- CLAUDE.md is a router — no inline domain knowledge, no "always read" directives
- Cross-cutting context is in CLAUDE.md, not buried in a knowledge file
- All knowledge files are in one directory (no parallel `docs/` + `knowledge/`)
- MEMORY.md (if exists) is a pure index — no inline paragraphs, just one-liner pointers
- Every knowledge/ file is reachable from the routing table
- No orphaned context (files that exist but aren't referenced from any routing entry)
- No duplicate content across knowledge files
- Subdirectory CLAUDE.md files are lean (stack, commands, gotchas — not domain knowledge)

Report the final structure and what changed.


## 文件 skills/model-audit/SKILL.md

---
name: model-audit
description: "Audit Agent/Task model routing — reads the dispatch log written by the model-routing PreToolUse hook and breaks down spend by model, subagent type, and project. Use when the user asks 'how's the model routing', 'audit my model usage', 'check the dispatch log', 'is the routing hook working', '/model-audit', or before drafting any public-facing post about Claude Code usage. Requires the model-routing hook to be installed first (see hooks/model-routing in this repo)."
---

# /model-audit — Routing Discipline Reader

Reads `~/.claude/agent_model_log.jsonl` (written by the `agent-model-check.py` PreToolUse hook) and shows whether your subagent dispatches are actually using the model tiers you intended.

**Arguments:** "$ARGUMENTS" — either a number of days (`7`, `30`) or the literal word `all`. Default: `7`.

## Step 1: Verify prerequisites

Check that the audit script and log file both exist:

```bash
test -f ~/.claude/scripts/model_audit.py && echo "script: ok" || echo "script: MISSING — install hooks/model-routing from this repo first"
test -f ~/.claude/agent_model_log.jsonl && echo "log: ok" || echo "log: MISSING — hook hasn't fired yet, dispatch any Agent in a fresh session first"
```

If either is missing, tell the user to install `hooks/model-routing/` from the same repo (https://github.com/Nitzan94/claude-code-skills/tree/master/hooks/model-routing) — the skill is the reader; the hook is what writes the data it reads.

## Step 2: Run the audit

Parse the user's arguments. If they said a number, pass it; if they said "all", pass `all`; if they said nothing, default to `7`:

```bash
python3 ~/.claude/scripts/model_audit.py "${ARGS:-7}"
```

## Step 3: Interpret the output

The script's output already includes a drift signal at the bottom. Read it and tell the user in one sentence what it means for their routing discipline:

- **Many `(unset)` entries** → the hook is catching frequent drift attempts. Good — that's the hook earning its keep.
- **Opus/Sonnet ratio above ~20%** → routing has slipped. Suggest scanning the `By subagent_type x model` section for which subagent types are running Opus when they shouldn't.
- **Zero dispatches in window** → either a quiet week, or check whether the hook is still wired (`grep agent-model-check ~/.claude/settings.json`).

Don't add new analysis the script didn't produce. The script is the source of truth; the skill's job is to surface it and frame the interpretation.


## 文件 skills/optimize-prompt/SKILL.md

---
name: optimize-prompt-gepa
description: Optimizes prompts using full GEPA methodology (Genetic-Pareto Evolution). Use when user wants to improve a prompt's accuracy on test cases, mentions "optimize prompt", "improve prompt", or has examples of desired input/output pairs. Implements Pareto frontier selection, trace-based reflection, and crossover mutations.
---

<objective>
GEPA (Genetic-Pareto Evolution for AI) optimizes prompts through:
1. **Pareto frontier** - Maintain pool of prompts that excel on different test cases
2. **Trace-based reflection** - Analyze full reasoning chains, not just outputs
3. **Crossover mutations** - Merge insights from multiple successful prompts
4. **Diversity pressure** - Prevent premature convergence

You (Claude) are the optimizer. You run prompts, capture traces, reflect on failures, and evolve improvements.
</objective>

<quick_start>
User provides:
1. A seed prompt to optimize
2. Test cases (input + expected output pairs)

You run the full GEPA loop and return the optimized prompt.

Example:
```
Seed: "Extract action items"
Test case:
  Input: "Meeting notes: John will prepare the report by Friday. Sarah to review."
  Expected: "- John: Prepare report (Due: Friday)\n- Sarah: Review (Due: unspecified)"

After GEPA optimization:
"Extract action items from text. Think step by step:
1. Identify each person mentioned
2. Find what they committed to do
3. Extract any deadline mentioned

Format each item as:
- [Person]: [Task] (Due: [deadline or 'unspecified'])

Rules:
- Skip items without clear ownership
- If deadline is vague (e.g., 'soon', 'later'), mark as 'unspecified'
- One line per action item"
```
</quick_start>

<intake>
To optimize a prompt, I need:

1. **Seed prompt** - What prompt do you want to optimize?
2. **Test cases** - Examples of input and expected output
   - Minimum: 1 example (I'll generate more synthetically)
   - Recommended: 5-10 examples for robust optimization

Optional:
- Target score (default: 90%)
- Max iterations (default: 10)
- Diversity weight (default: 0.3) - How much to favor diverse solutions

Please provide your prompt and test cases.
</intake>

<data_structures>
```
# Prompt Candidate
Candidate = {
  id: string,
  prompt: string,
  scores: {test_case_id: float},  # Score per test case
  avg_score: float,
  parent_ids: [string],  # For tracking lineage
  mutation_type: "reflection" | "crossover" | "seed"
}

# Pareto Frontier
ParetoFrontier = [Candidate]  # Candidates not dominated by any other

# Test Case with Trace
EvaluatedCase = {
  input: string,
  expected: string,
  actual: string,
  trace: string,  # Full reasoning chain
  score: float,
  feedback: string
}
```
</data_structures>

<process>
<step name="1_parse_input">
Parse user's input to extract:
- `seed_prompt`: The prompt to optimize
- `test_cases`: Array of {id, input, expected} pairs
- `target_score`: Default 0.9 (90%)
- `max_iterations`: Default 10
- `diversity_weight`: Default 0.3

Assign unique IDs to test cases (tc_1, tc_2, etc.)
</step>

<step name="2_synthetic_generation">
If fewer than 5 test cases, generate synthetic examples:

```
Given these examples:
{for each test_case: input -> expected}

Generate 5 more examples that:
- Follow the EXACT same output format
- Cover edge cases:
  * Empty/null inputs
  * Multiple items
  * Missing information
  * Ambiguous cases
- Use different names, numbers, contexts

Return as JSON array: [{"input": "...", "expected": "..."}, ...]
```

Add generated examples to test_cases with IDs.
</step>

<step name="3_baseline_evaluation">
Create seed candidate and evaluate with TRACES:

```
seed_candidate = {
  id: "c_0",
  prompt: seed_prompt,
  scores: {},
  parent_ids: [],
  mutation_type: "seed"
}
```

For each test_case:
  1. Run with trace capture:
     ```
     {seed_prompt}
     
     Input: {test_case.input}
     
     Think through this step by step, then provide your final answer.
     
     ## Reasoning:
     [Your step-by-step thinking]
     
     ## Answer:
     [Your final output]
     ```
  
  2. Parse trace (reasoning) and answer separately
  3. Score answer against expected (0-10)
  4. Store: seed_candidate.scores[test_case.id] = score/10

Calculate avg_score = mean(all scores)

Initialize:
- `pareto_frontier = [seed_candidate]`
- `all_candidates = [seed_candidate]`
- `best_avg_score = avg_score`

Report: "Baseline score: {avg_score:.0%}"
</step>

<step name="4_gepa_loop">
FOR iteration 1 to max_iterations:

  **4a. Pareto Selection**
  Select parent candidate using tournament selection with diversity bonus:
  
  ```
  For 3 random candidates from pareto_frontier:
    Calculate selection_score = avg_score + diversity_weight * uniqueness
    (uniqueness = how different this candidate's strengths are from others)
  
  Select candidate with highest selection_score
  ```
  
  selected_parent = winner

  **4b. Mini-batch Evaluation**
  Select mini-batch of 3 test cases, prioritizing:
  - Cases where selected_parent scored lowest (exploitation)
  - 1 random case (exploration)

  Run selected_parent.prompt on mini-batch WITH TRACES
  Collect: [{input, expected, actual, trace, score, feedback}, ...]

  mini_batch_score = average score
  Report: "Iteration {i}: Testing '{selected_parent.id}' on mini-batch: {mini_batch_score:.0%}"

  **4c. Early Success Check**
  IF mini_batch_score >= target_score:
    Run full validation on ALL test cases
    IF full_avg >= target_score:
      Report: "✓ Target reached: {full_avg:.0%}"
      GOTO step 5 (output)

  **4d. Trace-Based Reflection**
  Collect failures (score < 0.8) with their TRACES:

  ```
  ## Reflection Task
  
  Current prompt:
  {selected_parent.prompt}
  
  ## Failed Cases Analysis
  
  {for each failure:}
  ### Case {id}
  **Input:** {input}
  **Expected:** {expected}
  **Actual:** {actual}
  **ReasoningTrace:** {trace}
  **Score:** {score}/10
  **Feedback:** {feedback}
  
  ---
  
  ## Analysis Questions
  
  1. **Trace Analysis**: Where in the reasoning did the model go wrong?
     - Did it misunderstand the task?
     - Did it miss information in the input?
     - Did it apply wrong formatting?
  
  2. **Pattern Recognition**: What patterns do you see across failures?
     - Common misunderstandings
     - Systematic format errors
     - Missing edge case handling
  
  3. **Root Cause**: What's the SINGLE most impactful fix?
  
  4. **Specific Rules**: List 3-5 explicit rules to add to the prompt.
  
  Provide your analysis:
  ```


  Save reflection_analysis

  **4e. Generate Mutations**
  Create 2 new candidates:

  **Mutation 1: Reflection-based**
  ```
  Current prompt:
  {selected_parent.prompt}
  
  Analysis of failures:
  {reflection_analysis}
  
  Create an improved prompt that:
  - Addresses ALL identified issues
  - Includes explicit rules from analysis
  - Adds step-by-step reasoning instructions if helpful
  - Specifies exact output format with examples
  
  Write ONLY the new prompt (no explanation):
  ```

  **Mutation 2: Crossover (if pareto_frontier has 2+ candidates)**
  ```
  You have two successful prompts with different strengths:
  
  Prompt A (excels on: {cases where A > B}):
  {candidate_a.prompt}
  
  Prompt B (excels on: {cases where B > A}):
  {candidate_b.prompt}
  
  Create a NEW prompt that combines the best elements of both.
  Merge their rules, keep the most specific instructions from each.
  
  Write ONLY the merged prompt:
  ```

  Create new candidates:
  - mutation_1 = {id: "c_{n}", prompt: reflection_result, parent_ids: [selected_parent.id], mutation_type: "reflection"}
  - mutation_2 = {id: "c_{n+1}", prompt: crossover_result, parent_ids: [a.id, b.id], mutation_type: "crossover"}

  **4f. Full Evaluation of New Candidates**
  For each new candidate:
    Run on ALL test cases with traces
    Calculate scores per test case and avg_score

  **4g. Update Pareto Frontier**
  For each new candidate:
    Add to all_candidates
    
    Check Pareto dominance:
    - Candidate A dominates B if A scores >= B on ALL test cases AND > on at least one
    
    Update pareto_frontier:
    - Add new candidate if not dominated by any existing
    - Remove any existing candidates now dominated by new one

  **4h. Track Best**
  IF any new candidate has avg_score > best_avg_score:
    best_avg_score = new avg_score
    Report: "✓ New best: {best_avg_score:.0%} (candidate {id})"
  ELSE:
    Report: "No improvement. Pareto frontier size: {len(pareto_frontier)}"

  **4i. Diversity Check**
  IF all candidates in pareto_frontier have similar prompts (>80% overlap):
    Report: "⚠ Low diversity. Injecting random mutation."
    Create random_mutation with aggressive changes
    Add to next iteration's candidates

END FOR
</step>

<step name="5_output_results">
Select best_candidate = candidate with highest avg_score from pareto_frontier

Present final results:

```
## GEPA Optimization Results

### Performance
| Metric | Value |
|--------|-------|
| Baseline Score | {seed_candidate.avg_score:.0%} |
| Final Score | {best_candidate.avg_score:.0%} |
| Improvement | +{improvement:.0%} |
| Iterations | {iterations_run} |
| Candidates Evaluated | {len(all_candidates)} |
| Pareto Frontier Size | {len(pareto_frontier)} |

### Original Prompt
```
{seed_prompt}
```

### Optimized Prompt
```
{best_candidate.prompt}
```

### Per-Case Performance
| Test Case | Before | After | Δ |
|-----------|--------|-------|---|
{for each test_case:}
| {id} | {seed_scores[id]:.0%} | {best_scores[id]:.0%} | {delta} |

### Key Discoveries
{Summarize main patterns found during reflection:}
1. {discovery_1}
2. {discovery_2}
3. {discovery_3}

### Alternative Prompts (Pareto Frontier)
{If pareto_frontier has multiple candidates with different strengths:}
- **{candidate.id}**: Best for {cases where it excels} ({avg:.0%} avg)
```
</step>
</process>

<scoring_guide>
## Scoring Outputs (0-10)

| Score | Criteria |
|-------|----------|
| 10 | Perfect match: correct content AND exact format |
| 9 | Correct content, trivial format difference (whitespace, punctuation) |
| 7-8 | Correct content, minor format difference (ordering, capitalization) |
| 5-6 | Mostly correct content, wrong format structure |
| 3-4 | Partial content, significant omissions |
| 1-2 | Minimal correct content |
| 0 | Completely wrong or empty |

## Feedback Template
```
Score: X/10
✓ Correct: [what's right]
✗ Wrong: [what's wrong]
→ Fix: [specific instruction that would fix it]
```

Be STRICT about format matching. Format errors indicate missing instructions in the prompt.
</scoring_guide>

<trace_analysis_guide>
## How to Analyze Reasoning Traces

When examining a trace, look for:

1. **Task Understanding**
   - Did the model correctly interpret what to do?
   - Did it miss any requirements?

2. **Information Extraction**
   - Did it find all relevant info in the input?
   - Did it hallucinate information not present?

3. **Logic Errors**
   - Where did the reasoning go wrong?
   - What assumption was incorrect?

4. **Format Application**
   - Did it know the expected format?
   - Did it apply it correctly?

## Red Flags in Traces
- "I assume..." → Missing explicit instruction
- "I'm not sure if..." → Ambiguous requirement
- Skipping steps → Need more structured guidance
- Wrong interpretation → Need examples in prompt
</trace_analysis_guide>

<pareto_frontier_guide>
## Pareto Dominance

Candidate A dominates Candidate B if:
- A.scores[tc] >= B.scores[tc] for ALL test cases
- A.scores[tc] > B.scores[tc] for AT LEAST ONE test case

## Why Pareto Matters

Different prompts may excel on different cases:
- Prompt A: Great at edge cases, weak on simple cases
- Prompt B: Great at simple cases, weak on edge cases

Both belong in the Pareto frontier. Crossover can combine their strengths.

## Frontier Maintenance
- Max size: 5 candidates (prevent explosion)
- If over limit, keep most diverse set using k-medoids
</pareto_frontier_guide>

<edge_cases>
**Only 1 test case**: Generate 5+ synthetic examples covering edge cases before starting.

**Perfect baseline (100%)**: Report success, no optimization needed. Suggest additional edge cases to test robustness.

**No improvement after 5 iterations**: 
- Increase diversity_weight to 0.5
- Try aggressive mutations (rewrite from scratch based on learnings)
- Check if test cases have conflicting requirements

**Pareto frontier explodes (>5 candidates)**:
- Keep only the 5 most diverse candidates
- Prioritize candidates with unique strengths

**Crossover produces worse results**:
- Reduce crossover frequency
- Focus on reflection-based mutations

**Oscillating scores (up/down/up)**:
- Indicates conflicting requirements in test cases
- Review test cases for consistency
- Consider splitting into sub-tasks
</edge_cases>

<success_criteria>
Optimization completes when:
1. ✓ Full dataset score >= target_score (default 90%), OR
2. ✓ Max iterations reached, OR
3. ✓ No improvement for 3 consecutive iterations (early stopping)

Always return:
1. Best prompt from Pareto frontier
2. Score improvement trajectory
3. Key discoveries from trace analysis
4. Alternative prompts if Pareto frontier has multiple strong candidates
</success_criteria>

<example_session>
## Example: Action Item Extraction

**User Input:**
```
Seed prompt: "Extract action items from meeting notes"

Test cases:
1. Input: "John will send the report by Friday"
   Expected: "- John: Send report (Due: Friday)"

2. Input: "We should discuss the budget sometime"
   Expected: ""

3. Input: "Sarah and Mike to review the proposal by EOD"
   Expected: "- Sarah: Review proposal (Due: EOD)\n- Mike: Review proposal (Due: EOD)"
```

**GEPA Execution:**

Iteration 1: Baseline 40%
- tc_1: 8/10 (format slightly off)
- tc_2: 0/10 (returned items when should be empty)
- tc_3: 4/10 (missed second person)

Reflection: "Model doesn't know to skip vague items or split multiple people"

Mutation 1 (reflection): Added rules for ownership and multiple people

Iteration 2: 70%
- tc_2 now correct (empty)
- tc_3 still failing (format)

Crossover with seed: Merged format examples

Iteration 3: 90% ✓ Target reached

**Final Optimized Prompt:**
```
Extract action items from meeting notes.

Step-by-step:
1. Find each person with a specific commitment
2. Identify their task and any deadline
3. Format as: "- [Person]: [Task] (Due: [deadline])"

Rules:
- SKIP vague items without clear ownership ("we should...", "someone needs to...")
- If multiple people share a task, create separate lines for each
- If no deadline mentioned, use "Due: unspecified"
- If NO valid action items exist, return empty string

Example:
Input: "John and Mary will review docs by Monday. We should improve process."
Output:
- John: Review docs (Due: Monday)
- Mary: Review docs (Due: Monday)
```
</example_session>

## 文件 skills/skill-tutor/SKILL.md

---
name: skill-tutor
description: Personal tutor that teaches any topic. Use when user says "teach me", "learn about", "quiz me", "/skill-tutor", or wants to understand a new concept deeply. Creates personalized tutorials using user's actual projects, tracks learning progress, uses spaced repetition.
---

<teaching_philosophy>
## How Expert Teachers Think

Effective teaching transfers mental models, not steps. The difference:

**Weak teaching:**
"Step 1: Do X. Step 2: Do Y. Step 3: Do Z."

**Strong teaching:**
"Here's the problem you're trying to solve. Here's why naive approaches fail. Here's the insight that changes everything. Now let's apply it to YOUR project."

### The Four Principles

1. **Mental Models, Not Procedures** - Teach HOW to think, not WHAT to do
2. **Real Examples, Not Abstract** - Use the learner's actual work, not hypotheticals
3. **Show the Journey** - "Here's what you'd try... why it fails... the insight"
4. **One Deep > Ten Shallow** - Master one concept before moving on

### What Makes Teaching Fail

- Too abstract (no connection to learner's reality)
- Too procedural (steps without understanding)
- No failure modes (learner doesn't know what to avoid)
- No practice (learning without doing)
</teaching_philosophy>

<persistent_learning>
## Learning System

All tutorials and progress live in `~/skill-tutor-tutorials/`:

```
~/skill-tutor-tutorials/
├── learner_profile.md      # Background, goals, learning style
├── tutorials/              # Personalized tutorials by topic
│   ├── rag-architectures.md
│   ├── typescript-generics.md
│   ├── system-design-caching.md
│   └── ...
└── topics/                 # Topic-specific analysis
    └── knowledge_map.md    # What's been learned, connections
```

This knowledge compounds across sessions. Every tutorial references YOUR projects.
</persistent_learning>

<intake>
What would you like to do?

1. **Teach me [topic]** - Create personalized tutorial on a topic
2. **Quiz me** - Spaced repetition on concepts you've learned
3. **Continue** - See what's next based on your learning path
4. **Review progress** - See what you've learned, suggest next steps

**Wait for response.**
</intake>

<routing>
| Response | Action |
|----------|--------|
| "teach me X", specific topic | Create tutorial on that topic |
| "quiz", "quiz me" | Run quiz_priority.py, quiz on highest priority concept |
| "continue", "what's next" | Load profile, check tutorials, propose next topics |
| "progress", "review" | Show learning summary, knowledge gaps, recommendations |
</routing>

<onboarding_interview>
## For New Learners

When no `~/skill-tutor-tutorials/learner_profile.md` exists, conduct brief onboarding:

"I'm your personal tutor. I'll create tutorials using YOUR actual projects as examples, track what you learn, and quiz you for retention.

Quick intro - I need to understand how you learn best."

### Questions (ask together, keep it light)

1. **Background**: "What's your technical background? (e.g., frontend dev, backend, data science, etc.)"

2. **Current focus**: "What are you working on right now? What projects?"

3. **Learning style**: "Do you prefer: (a) theory first, (b) hands-on immediately, (c) learn by debugging mistakes?"

### Create Profile

After interview, create `~/skill-tutor-tutorials/learner_profile.md`:

```markdown
# Learner Profile

## Background
[Technical background, experience level]

## Current Projects
[What they're working on - source for examples]

## Learning Style
[How they prefer to learn]

## My Teaching Notes
[Calibration observations for future tutorials]

## Topics Learned
[Will be updated as we go]
```
</onboarding_interview>

<tutorial_creation>
## Writing Tutorials

When user requests "teach me [topic]":

### 1. Understand Context

- Read learner_profile.md
- Ask: "What specifically about [topic] interests you? What are you trying to build?"
- Find relevant project of theirs to use as example

### 2. Research if Needed

If topic requires current info (new APIs, recent changes), use WebSearch/WebFetch.
Always verify facts before teaching.

### 3. Create Tutorial File

```markdown
---
topic: [topic name]
concepts: [key concepts covered]
source_project: [which of their projects this references]
prerequisites: [max 3 prior tutorials]
understanding_score: null
last_quizzed: null
created: DD-MM-YYYY
last_updated: DD-MM-YYYY
---

# [Topic Name]

## Why This Matters
[Connect to their goals, show the problem this solves]

## The Problem
[What challenge does this address? Why do naive approaches fail?]

## The Insight
[Core mental model - what experts understand that beginners don't]

## In Your Project
[Concrete examples from THEIR actual code/projects]
[Show how this applies to what they're building]

## The Pattern
[How to apply this - with before/after examples]

## Common Mistakes
[What to avoid, failure modes]

## Practice
[Exercise using their own project]

## Q&A
[Append all questions here - living document]
```

### Quality Standards

- Start with WHY, not mechanics
- Use THEIR projects as examples
- Show the journey: "You might try X... it fails because Y... the insight is Z"
- One concept deeply > ten concepts shallow
- Predict confusion points
- End with practice on their own work
</tutorial_creation>

<quiz_mode>
## Spaced Repetition Quizzes

### Triggering Quiz

- Explicit: "Quiz me on RAG architectures"
- Open: "Quiz me" - use quiz_priority.py for spaced repetition

### Priority Logic (Fibonacci intervals)

```
score 1-2: review in 2 days
score 3-4: review in 5 days
score 5-6: review in 13 days
score 7-8: review in 34 days
score 9-10: review in 89 days
```

Priority order:
1. Never-quizzed tutorials
2. Overdue low-scoring concepts
3. Mastered concepts whose interval elapsed

### Quiz Philosophy

Quizzes reveal understanding, not recall. Ask ONE question, wait for answer.

Question types:
- **Conceptual**: "Explain [concept] in your own words"
- **Applied**: "How would you use [concept] in your [project]?"
- **Debugging**: "This code has [problem]. What's wrong?"
- **Design**: "How would you design [system] given [constraints]?"

Use THEIR projects when possible.

### Scoring (1-10)

- 1-3: Cannot recall, needs re-teaching
- 4-5: Vague memory, partial answer
- 6-7: Solid understanding, minor gaps
- 8-9: Strong grasp, handles edge cases
- 10: Could teach others

Update frontmatter: `understanding_score` and `last_quizzed: DD-MM-YYYY`

Record in `## Quiz History` section.
</quiz_mode>

<living_tutorials>
## Tutorials Evolve

- **Append all questions** to Q&A section (mandatory)
- Update when learner discovers new aspects
- Refresh `last_updated` timestamp
- Link related tutorials as knowledge grows

`understanding_score` only updates through quizzes, not teaching.
</living_tutorials>

<calibration>
## Teaching Calibration

**Early tutorials**: More scaffolding, explicit connections, slower pace
**Later tutorials**: Move faster, reference shared history, expect pattern recognition

**Do**:
- Meet learner at their level
- Use their vocabulary
- Reference their projects
- Connect to what they already know
- Be honest but encouraging

**Don't**:
- Assume unstated knowledge
- Use generic examples when their projects exist
- Overwhelm with edge cases
- Condescend about gaps
</calibration>

<knowledge_connections>
## Building Knowledge Map

As tutorials accumulate, maintain `~/skill-tutor-tutorials/topics/knowledge_map.md`:

```markdown
# Knowledge Map

## Topics Mastered (score 8+)
- [topic]: [one-line summary]

## Topics Learning (score 4-7)
- [topic]: [what needs reinforcement]

## Topics to Explore
- [topic]: [why relevant to their goals]

## Connections
- [topic A] -> [topic B]: [how they relate]
```

Use this to suggest next topics and show how concepts connect.
</knowledge_connections>

<scripts_reference>
## Scripts

### setup_tutor.py
Initialize `~/skill-tutor-tutorials/` structure.
Run before first use.

### quiz_priority.py
Calculate which tutorial to quiz based on spaced repetition.
Returns prioritized list.
</scripts_reference>


## 文件 skills/skillify/SKILL.md

---
name: skillify
description: Capture this session's repeatable process into a reusable skill. Call at end of the process you want to capture.
when_to_use: "Use when the user wants to turn a session into a skill, capture a workflow, save a process as reusable, or says 'skillify this', 'make this a skill', 'save this workflow'. Must be user-invoked -- do not auto-trigger."
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash
  - AskUserQuestion
argument-hint: "[description of the process you want to capture]"
---

# Skillify

You are capturing this session's repeatable process as a reusable skill.

## Your Session Context

The script below extracts session memory and user messages from the current session's JSONL — the same data Anthropic's bundled skillify injects via `{{sessionMemory}}` and `{{userMessages}}`:

<session_context>
!`python3 ~/.claude/skills/skillify/extract_session.py 2>/dev/null || echo "Session extraction unavailable — analyze the conversation directly."`
</session_context>

## Your Task

### Step 1: Analyze the Session

Before asking any questions, analyze the session context above. Pay special attention to the user's messages — their corrections and steering reveal preferences that should become hard rules in the skill. Also note:
- Tool calls made (these become the skill's allowed-tools)
- Agent spawns (these inform execution strategy)
- Where the user pushed back or corrected course

Identify:
- What repeatable process was performed
- What the inputs/parameters were
- The distinct steps (in order)
- The success artifacts/criteria (e.g. not just "writing code," but "an open PR with CI fully passing") for each step
- Where the user corrected or steered you
- What tools and permissions were needed
- What agents were used
- What the goals and success artifacts were

### Step 2: Interview the User

Use AskUserQuestion for ALL questions. Never ask questions via plain text. For each round, iterate as much as needed until the user is happy. The user always has a freeform "Other" option -- do NOT add your own "Needs tweaking" option.

**Round 1: High level confirmation**
- Suggest a name and description for the skill based on your analysis. Ask the user to confirm or rename.
- Suggest high-level goal(s) and specific success criteria for the skill.

**Round 2: More details**
- Present the high-level steps you identified as a numbered list. Tell the user you will dig into the detail in the next round.
- If you think the skill will require arguments, suggest arguments based on what you observed.
- If it's not clear, ask if this skill should run inline (in the current conversation) or forked (as a sub-agent with its own context). Forked is better for self-contained tasks that don't need mid-process user input; inline is better when the user wants to steer mid-process.
- Ask where the skill should be saved. Suggest a default based on context (repo-specific workflows -> repo, cross-repo personal workflows -> user). Options:
  - **This repo** (`.claude/skills/<name>/SKILL.md`) -- for workflows specific to this project
  - **Personal** (`~/.claude/skills/<name>/SKILL.md`) -- follows you across all repos

**Round 3: Breaking down each step**
For each major step, if it's not glaringly obvious, ask:
- What does this step produce that later steps need? (data, artifacts, IDs)
- What proves that this step succeeded, and that we can move on?
- Should the user be asked to confirm before proceeding? (especially for irreversible actions like merging, sending messages, or destructive operations)
- Are any steps independent and could run in parallel?
- How should the skill be executed? (e.g. always use a Task agent to conduct code review, or invoke an agent team for a set of concurrent steps)
- What are the hard constraints or hard preferences? Things that must or must not happen?

You may do multiple rounds of AskUserQuestion here, one round per step, especially if there are more than 3 steps or many clarification questions.

IMPORTANT: Pay special attention to places where the user corrected you during the session, to help inform your design.

**Round 4: Final questions**
- Confirm when this skill should be invoked, and suggest/confirm trigger phrases too.
- Ask for any other gotchas or things to watch out for.

Stop interviewing once you have enough information. IMPORTANT: Don't over-ask for simple processes!

### Step 3: Write the SKILL.md

Create the skill directory and file at the location the user chose in Round 2.

Use this format:

```markdown
---
name: {{skill-name}}
description: {{one-line description}}
allowed-tools:
  {{list of tool permission patterns observed during session}}
when_to_use: {{detailed description of when Claude should automatically invoke this skill, including trigger phrases and example user messages}}
argument-hint: "{{hint showing argument placeholders}}"
arguments:
  {{list of argument names}}
context: {{inline or fork -- omit for inline}}
---

# {{Skill Title}}
Description of skill

## Inputs
- `$arg_name`: Description of this input

## Goal
Clearly stated goal for this workflow. Best if you have clearly defined artifacts or criteria for completion.

## Steps

### 1. Step Name
What to do in this step. Be specific and actionable. Include commands when appropriate.

**Success criteria**: ALWAYS include this! This shows that the step is done and we can move on.
```

**Per-step annotations** (include where relevant):
- **Success criteria** is REQUIRED on every step
- **Execution**: `Direct` (default), `Task agent`, `Teammate`, or `[human]`. Only specify if not Direct.
- **Artifacts**: Data this step produces that later steps need (e.g., PR number, commit SHA)
- **Human checkpoint**: When to pause and ask before proceeding (irreversible actions)
- **Rules**: Hard constraints. User corrections during the reference session are especially useful here.

**Step structure tips:**
- Steps that can run concurrently use sub-numbers: 3a, 3b
- Steps requiring the user to act get `[human]` in the title
- Keep simple skills simple -- a 2-step skill doesn't need annotations on every step

**Frontmatter rules:**
- `allowed-tools`: Minimum permissions needed (use patterns like `Bash(gh:*)` not `Bash`)
- `context`: Only set `context: fork` for self-contained skills that don't need mid-process user input
- `when_to_use` is CRITICAL -- tells the model when to auto-invoke. Start with "Use when..." and include trigger phrases
- `arguments` and `argument-hint`: Only include if the skill takes parameters. Use `$name` in the body for substitution.

### Step 4: Confirm and Save

Before writing the file, output the complete SKILL.md content as a yaml code block so the user can review it with proper syntax highlighting. Then ask for confirmation using AskUserQuestion with a simple question like "Does this SKILL.md look good to save?"

After writing, tell the user:
- Where the skill was saved
- How to invoke it: `/{{skill-name}} [arguments]`
- That they can edit the SKILL.md directly to refine it


## 文件 skills/sync-context/SKILL.md

---
name: sync-context
description: "End-of-session context sync. Reviews what was learned in the conversation and proposes updates to knowledge/, people/, and projects/ files. Use when the user says /sync-context, 'sync context', 'update context', or at the end of a session in a project that uses the compounding-context structure."
---

# /sync-context — Compound Project Context

Sync what was learned this session into the project's context files so the next session starts smarter.

**Arguments:** "$ARGUMENTS"

## Step 1: Detect or set up context structure

Check which context directories exist at the project root:

```bash
ls knowledge/ people/ projects/ 2>/dev/null
```

If none exist, ask the user if they want to set up the compounding-context structure. Default: create `knowledge/`, `people/`, and `projects/` directories. The user may want a subset (e.g., only `knowledge/` for a solo project without stakeholders) or different folder names to match existing project conventions — adapt accordingly.

If a subset already exists, use what's there. Don't create missing folders unless the user asks.

Once the structure exists (or has been created), proceed to Step 2.

## Step 2: Read current context

Read all existing context files to understand what's already captured:

```bash
# List all context files
find knowledge/ people/ projects/ -name "*.md" -type f 2>/dev/null
```

Read each file to understand the current state of captured knowledge.

## Step 3: Review the session

Analyze this conversation for new information that should persist. Look for:

**Knowledge updates** (knowledge/):
- Business decisions or constraints learned
- Technical decisions made
- New requirements or scope changes
- Platform, tool, or vendor evaluations
- Domain knowledge that was clarified

**People updates** (people/):
- Stakeholder preferences revealed ("she wants it simple", "he pushed back on X")
- Communication style observations
- Decisions a person made and why
- New open questions for a stakeholder
- Answers to previously open questions (close them)

**Project updates** (projects/):
- New workstreams identified → create a folder with a README.md
- Research or analysis done → save as an artifact in the relevant project folder
- Decisions made within a workstream
- Status changes or blockers

## Step 4: Propose updates

Present ALL proposed changes to the user in a clear format:

```
## Context Updates

### knowledge/business.md
- ADD: [what to add and why]

### people/stakeholder.md
- UPDATE preferences: [what was learned]
- CLOSE question: [question that was answered]
- ADD decision: [decision made and date]

### projects/platform-selection/
- CREATE: research-notes.md with [summary of what was discussed]
```

Group by file. Show what changes and why. Be specific — quote the conversation where relevant.

## Step 5: Apply approved updates

After the user approves (they may modify or reject some), apply the changes using the Edit tool. For new files, use Write.

Rules:
- Never remove existing content unless it's clearly wrong or superseded
- Add to existing sections rather than rewriting them
- Date-stamp decisions: `- [YYYY-MM-DD] Decided to use vendor X for Phase 1`
- Keep files scannable — use headers, short bullets, tables where appropriate
- If a people/ file has placeholder fields (like "Communication style:"), fill them in rather than adding a new section

## Step 6: Commit context updates

```bash
git add knowledge/ people/ projects/
git diff --cached --stat
```

If there are changes, commit them:

```bash
git commit -m "sync-context: update [list of files changed]"
```

## Notes

- This skill is about **persistent context**, not session notes. Don't save ephemeral details (what commands were run, debugging steps tried). Save what matters for the next session.
- Bias toward updating existing files over creating new ones.
- If nothing meaningful was learned this session, say so. Don't force updates.
- Works in any project with a knowledge/, people/, projects/ structure — or any subset that fits the project.

