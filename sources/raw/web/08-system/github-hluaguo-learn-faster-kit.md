# hluaguo/learn-faster-kit

- 链接：https://github.com/hluaguo/learn-faster-kit
- 作者：hluaguo
- 仓库说明：AI-powered learning coach with spaced repetition with Claude Code - master any knowledge faster with personalized syllabi and progress tracking
- 星数：387
- 获取方式：GitHub README + SKILL/说明文件

---

## README

# Learn FASTER

[![Python Version](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)

> AI-powered learning coach that accelerates mastery through spaced repetition, personalized syllabi, and active practice.

**Built for [Claude Code](https://claude.com/claude-code)** - Integrates AI coaching directly into your development environment.
Also supports [Codex](https://developers.openai.com/codex) with agent-specific `AGENTS.md` instructions and shared learning tools. Codex support is less strict than Claude Code because Codex does not currently expose a CLI flag for replacing the system prompt; Learn FASTER can only inject coaching behavior through `AGENTS.md`, startup prompts, or future skill-style instructions. Codex also only exposes its structured user-input tool in Plan mode, so in Default mode it cannot present guided choice prompts the same way Claude Code can.

## Why Learn FASTER?

Master any technical skill with science-backed learning principles:

-   **Personalized syllabi** generated for your skill level and learning goals
-   **Spaced repetition** system that schedules reviews at optimal intervals
-   **Four learning modes** - choose Balanced, Exam-Prep, Theory-Focused, or Practical
-   **Active practice** with auto-generated exercises and projects
-   **Progress tracking** to visualize your learning journey

## The FASTER Framework

-   **F**orget: Beginner's mindset - approach topics with fresh perspective
-   **A**ct: Learn by doing - hands-on practice over passive reading
-   **S**tate: Optimize focus - create ideal learning conditions
-   **T**each: Explain to retain - teaching reinforces understanding
-   **E**nter: Consistent sessions - regular practice builds momentum
-   **R**eview: Spaced repetition - review at intervals for long-term retention

## Installation

**Prerequisites:** [uv](https://docs.astral.sh/uv/) package manager

```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Option 1: Persistent Installation (Recommended)

Install once and use across all projects:

```bash
uv tool install learn-faster --from git+https://github.com/cheukyin175/learn-faster-kit.git
```

Then in any project directory, simply run:

```bash
learn-faster
```

This will auto-initialize on first run and launch Claude Code with FASTER coaching mode.

### Option 2: One-Time Use

Run directly without installation:

```bash
uvx --from git+https://github.com/cheukyin175/learn-faster-kit.git learn-faster
```

### What Gets Installed

On first run, learn-faster creates shared learning tools plus agent-specific instructions.

For Claude Code:

```
your-project/
├── .claude/
│   ├── agents/practice-creator.md
│   ├── commands/
│   │   ├── learn.md
│   │   ├── review.md
│   │   └── progress.md
│   └── settings.local.json
├── .learning/
│   ├── config.json (tracks initialization)
│   ├── scripts/
│   │   ├── init_learning.py
│   │   ├── log_progress.py
│   │   ├── review_scheduler.py
│   │   └── generate_syllabus.py
│   └── references/faster_framework.md
└── CLAUDE.md
```

For Codex, run `learn-faster init --agent codex`. It creates the same `.learning/` shared tools and writes Codex instructions to `AGENTS.md`. Because Codex does not provide a system-prompt replacement flag, adherence depends on Codex reading those project instructions and the launch prompt. Codex guided-choice interactions are also limited: the user-input tool is available only in Plan mode, so Default mode falls back to plain conversational questions.

## Quick Start

1. **Install the tool**

    ```bash
    uv tool install learn-faster --from git+https://github.com/cheukyin175/learn-faster-kit.git
    ```

2. **Launch in any project directory**

    ```bash
    cd your-learning-project
    learn-faster
    ```

    First run will:

    - Prompt you to select a learning mode
    - Initialize the project structure
    - Launch your configured agent with FASTER coaching enabled

3. **Start learning**

    ```bash
    /learn "Golang fundamentals"
    ```

    The AI coach will generate a personalized syllabus and guide your learning session.

## Demo: Teach-Back in Action

The "T" in FASTER—teaching to retain—is the key differentiator. Here's how it works:

```bash
mkdir learn-go && cd learn-go
learn-faster                    # Select "Balanced" mode
/learn "Go error handling"      # In Claude Code
```

```
Coach: You've just learned about error wrapping. Ready to teach it back?
       ┌ Teach Back
       │ ● Yes, let me explain
       │ ○ Need review first
       │ ○ Not sure yet
       └

You:   So when you wrap an error with fmt.Errorf and %w, you're adding
       context like "failed to open config" while keeping the original
       error inside. Then errors.Is can still match the root cause.

Coach: ✅ Great explanation! You nailed the key insight—wrapped errors
       preserve the chain for inspection. Adding "error wrapping" to
       your review schedule. First review tomorrow.
```

**Why this works:** Explaining concepts in your own words forces active recall—proven to boost retention 2-3x vs passive reading. The coach won't just tell you answers; it guides you to construct understanding yourself.

## Usage

### CLI Commands

-   `learn-faster` - Launch Claude Code with FASTER coaching (auto-initializes on first run)
-   `learn-faster init` - Force re-initialization or switch learning modes
-   `learn-faster init --agent codex` - Initialize the project for Codex instead of Claude Code
-   `learn-faster resume [<id>] [--pick] [--fork]` - Resume a previous coaching session (`--pick` to choose interactively; `--fork` to branch into a new session id)
-   `learn-faster version` - Show current version

### Claude Code Slash Commands

Once Claude Code is running, use these commands:

-   `/learn [topic]` - Start or continue learning a topic with personalized syllabus
-   `/review` - Spaced repetition review session for topics you've learned
-   `/progress` - View detailed progress report and learning statistics

## Learning Modes

Choose the mode that fits your learning style:

-   **Balanced** - Mix of theory, practice, and real-world application (recommended for most learners)
-   **Exam-Prep** - Focused on recall, practice tests, and certification preparation
-   **Theory-Focused** - Deep conceptual understanding with mental models and first principles
-   **Practical** - Project-based learning with immediate application

Each mode provides a tailored coaching experience with mode-specific syllabi and exercises.

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/cheukyin175/learn-faster-kit.git
cd learn-faster-kit

# Install uv if needed
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv sync
```

## Use Cases

Learn FASTER is ideal for:

-   Learning new programming languages (Go, Rust, Python, TypeScript, etc.)
-   Preparing for technical certifications and exams
-   Mastering frameworks and libraries (React, Next.js, Django, etc.)
-   Building structured self-study programs
-   Onboarding to new codebases or technologies

## Requirements

-   Python 3.12+
-   [Claude Code](https://claude.com/claude-code)
-   [uv](https://docs.astral.sh/uv/) package manager

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

MIT License - See LICENSE file for details


## 文件 AGENTS.md

# Repository Guidelines

## Project Structure & Module Organization

This is a Python 3.12 package using a `src/` layout. Runtime code lives in `src/learn_faster/`, with the CLI entry point in `src/learn_faster/cli/main.py`. Agent profiles are defined in `src/learn_faster/cli/agents.py`. Packaged learning assets live under `src/learn_faster/templates/`: shared scripts and references are in `templates/shared/`, while agent-specialized assets are in `templates/agents/<agent-name>/modes/<mode>/`. Keep user-facing documentation in `README.md`, release notes in `CHANGELOG.md`, and contributor process notes in `.github/CONTRIBUTING.md`.

There is currently no committed test suite. Add tests under `tests/` when changing behavior, mirroring the package structure where practical.

## Build, Test, and Development Commands

- `uv sync` installs project dependencies from `pyproject.toml` and `uv.lock`.
- `uv run learn-faster --help` runs the CLI locally through the project environment.
- `uv run learn-faster init --agent claude-code` initializes the current directory for the Claude Code profile.
- `uv run learn-faster init --agent codex` initializes the current directory for the Codex profile.
- `uv run learn-faster version` verifies the installed package metadata and console script.
- `uv build` builds source and wheel distributions using Hatchling.
- `uv run pytest` should be used once tests are added.

Avoid committing generated local install targets in consumer projects, such as `.learning/`, `.claude/`, `.codex/`, `CLAUDE.md`, or generated `AGENTS.md`. This repository's root `AGENTS.md` is the contributor guide and should stay tracked.

## Coding Style & Naming Conventions

Use standard Python style with 4-space indentation, type hints for new public helpers, and `pathlib.Path` for filesystem work. Prefer small, direct functions that match the current CLI style. Use `snake_case` for functions, variables, and module names; use `PascalCase` for classes. Agent names and user-facing command filenames should stay lowercase and hyphenated, for example `claude-code`, `codex`, and `generate-exam.md`.

Keep JSON output formatted with two-space indentation when matching existing generated files. Preserve Markdown frontmatter in template files when editing mode prompts or commands.

## Testing Guidelines

For CLI behavior, add focused tests that exercise argument handling, initialization decisions, and file generation. Mock subprocess calls to `claude` and avoid writing outside temporary directories. Name test files `test_<module>.py` and test functions `test_<behavior>()`. If a change updates templates, include assertions for copied filenames or rendered content where possible.

## Commit & Pull Request Guidelines

Use Conventional Commits, as documented in `.github/CONTRIBUTING.md`: `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `build:`, `ci:`, or `chore:`. Recent history follows this pattern, for example `feat: add printable exam generator for exam mode`.

Pull requests should include a short description, motivation or linked issue, test results, and screenshots or terminal output when CLI behavior changes. Note any template changes explicitly because they affect files generated in downstream projects.

