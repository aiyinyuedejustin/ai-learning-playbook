# mkrech/anki-course-tutor-mcp-server

- 链接：https://github.com/mkrech/anki-course-tutor-mcp-server
- 作者：mkrech
- 仓库说明：
- 星数：1
- 获取方式：GitHub README + SKILL/说明文件

---

## README

# Anki Course Tutor MCP Server

AI-powered learning system that combines Anki's spaced repetition with AI-driven tutoring via chat interface.

[![Tests](https://img.shields.io/badge/tests-102%20passing-brightgreen)](tests/)
[![Coverage](https://img.shields.io/badge/coverage-74%25-green)](htmlcov/)
[![Python](https://img.shields.io/badge/python-3.13+-blue)](pyproject.toml)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue)](LICENSE)

## ✨ Features

- 🎓 **Chat-based Learning** - Natural conversation interface via MCP
- 🤖 **AI Explanations** - Contextual explanations for incorrect answers
- ✅ **User Review System** - Confirm or override automatic answer evaluation
- 📊 **Progress Tracking** - Detailed statistics and learning analytics
- 🔄 **Anki Scheduler Integration** - Submit reviews directly to Anki's spaced repetition system
- 🎯 **Flexible Modes** - Explain mode (with AI explanations) or Test mode (assessment only)
- 🔌 **11 MCP Tools** - Complete learning workflow via chat interface
- 📝 **Multiple Card Types** - Basic, Cloze, Multiple Choice (MC), Single Choice (SC), and KPRIM
- 🎨 **Flexible Answer Formats** - Accept R/F, T/F, Y/N, or 1/0 for KPRIM questions

## Prerequisites

1. [Anki](https://apps.ankiweb.net/) installed and running
2. [AnkiConnect](https://ankiweb.net/shared/info/2055492159) add-on installed
3. Python 3.13+
4. [uv](https://github.com/astral-sh/uv) for package management

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd anki-course-tutor-mcp-server

# Install with uv (recommended)
uv sync

# Or with pip
pip install -e ".[dev]"
```

## Anki Setup

1. Install [Anki](https://apps.ankiweb.net/)
2. Install [AnkiConnect addon](https://ankiweb.net/shared/info/2055492159):
   - Open Anki → Tools → Add-ons → Get Add-ons
   - Enter code: `2055492159`
   - Restart Anki
3. Keep Anki running in the background when using the tutor

## Configuration

Edit `config.yaml` to customize:

### Anki Connection & Scheduler

```yaml
anki:
  connect_url: "http://localhost:8765"  # AnkiConnect URL
  connect_timeout: 30                    # Connection timeout (seconds)
  retry_attempts: 3                      # Number of retry attempts
  use_anki_scheduler: true               # Enable Anki scheduler integration
```

**Scheduler Integration:**
- When `use_anki_scheduler: true`, reviews are submitted to Anki's native spaced repetition scheduler
- Cards will appear in Anki with updated due dates based on your answers
- **Ease mapping**: Correct = 4 (Easy), Incorrect = 1 (Again)
- Requires Anki Desktop running with AnkiConnect
- Set to `false` for local-only mode (no Anki scheduler updates)

**Requirements:**
- Anki Desktop must be running
- AnkiConnect addon installed and enabled
- Cards must have numeric IDs from Anki

### Other Settings

- **Tutor personalities and weights** - Control Normal/Pirate rotation
- **Learning modes** - EXPLAIN (with AI) or TEST (assessment only)
- **Evaluation behavior** - Case sensitivity, whitespace handling
- **Storage paths** - Session and progress data locations

## Usage with Claude Desktop

Add to your `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS):

```json
{
  "mcpServers": {
    "anki-course-tutor": {
      "command": "uv",
      "args": [
        "--directory",
        "/full/path/to/anki-course-tutor-mcp-server",
        "run",
        "anki-course-tutor"
      ]
    }
  }
}
```

Restart Claude Desktop to load the MCP server.

## 💬 Usage Examples

### Starting a Session

```
You: List my Anki decks
AI: I found these decks:
    1. Spanish Vocabulary (150 cards)
    2. Python Programming (87 cards)

You: Start a learning session with Spanish Vocabulary in EXPLAIN mode
AI: ✓ Created session abc-123 with 150 cards
    Ready to begin! Type "next card" to start.
```

### Learning with Review

```
You: Next card
AI: 📝 Card 1/150
    Question: ¿Cómo estás?

You: How are you?
AI: 🤔 I think this is CORRECT!
    Expected: "How are you?" or "How do you do?"
    
    Do you agree? (yes/no)

You: yes
AI: ✅ Correct! Progress: 1/150 cards completed
```

### Getting Explanations (EXPLAIN Mode)

```
You: What hour is it?
AI: 🤔 I think this is INCORRECT.
    Expected: "What time is it?"
    
    Do you agree? (yes/no)

You: yes
AI: Let me explain:
    
    "¿Qué hora es?" translates to "What time is it?" in English. 
    While "hour" and "time" are related, we use "What time" as the 
    standard expression. Think of "time" as the specific point on 
    the clock, while "hour" is more about duration.
```

### KPRIM Questions with Flexible Formats

```
You: Next card
AI: 📝 Card 5/150
    Question: Welche Aussagen über Conditional Parameterization sind korrekt?
    
    Options:
    Q_1: Sie ist die graphische Darstellung von P(G|I)
    Q_2: Sie verwendet bedingte Wahrscheinlichkeitstabellen
    Q_3: Sie ist nur für diskrete Variablen definiert
    Q_4: Sie ermöglicht effiziente Inferenz in Bayesianischen Netzen
    Q_5: Sie ersetzt die Chain Rule vollständig
    
    Hint: Sources: Folie 5 | Extra: Conditional Parameterization ist 
          die graphische Darstellung von P(G|I)

You: RRFRF
AI: You answered: 'RRFRF'
    Correct answer: '1 1 0 1 0'
    
    Was your answer correct? (yes/no)

You: yes
AI: ✅ Correct! Progress: 5/150 cards completed
```

**Supported KPRIM answer formats:**
- **R/F** (German): `RRFRF`, `R,R,F,R,F`, `R R F R F`
- **T/F** (English): `TTFTT`, `T,T,F,T,T`, `T T F T T`
- **Y/N**: `YYNYN`, `Y,Y,N,Y,N`, `Y Y N Y N`
- **1/0** (Numeric): `11010`, `1,1,0,1,0`, `1 1 0 1 0`

All formats are case-insensitive and separator-agnostic.
```

## 🏗️ Architecture

### State Machine

```
NOT_STARTED → PRESENTING_CARD → AWAITING_ANSWER
                                      ↓
                               EVALUATING
                                      ↓
                              AWAITING_REVIEW
                                   ↙    ↘
                         (correct)        (incorrect)
                              ↓                ↓
                   AWAITING_ANSWER ← EXPLAINING
                              ↓
                   SESSION_COMPLETE
```

### MCP Tools

| Tool | Description |
|------|-------------|
| `list_decks` | List all available Anki decks |
| `start_session` | Create new learning session |
| `resume_session` | Resume paused session |
| `get_next_card` | Present next card question |
| `submit_answer` | Submit answer for evaluation |
| `confirm_evaluation` | Confirm/override evaluation |
| `get_explanation` | Get AI explanation (EXPLAIN mode) |
| `get_session_stats` | Get session statistics |
| `end_session` | Complete and save session |

## Configuration

Edit `config.yaml` to customize settings:

```yaml
anki:
  connect_url: "http://localhost:8765"
  connect_timeout: 10

tutor:
  personalities:
    - name: "normal"
      ratio: 3
    - name: "pirate"
      ratio: 1
  modes:
    explain:
      max_sentences: 5

learning:
  simple_srs:
    retry_incorrect: true
  evaluation:
    case_sensitive: false
```

## Development

```bash
# Run tests (102 tests, 74% coverage)
uv run pytest

# Run with coverage report
uv run pytest --cov=src --cov-report=html

# Lint and format
ruff check src/ tests/
ruff format src/ tests/

# Type checking
ruff check --select=F,I,B,C4,UP
```

### Project Structure

```
anki-course-tutor-mcp-server/
├── src/anki_course_tutor/
│   ├── mcp_server.py         # FastMCP tools and resources
│   ├── learning_engine.py    # State machine and evaluation
│   ├── session_manager.py    # Session CRUD
│   ├── progress_tracker.py   # Statistics and persistence
│   ├── scheduler.py          # Card scheduling
│   ├── ai_tutor.py           # AI explanations
│   └── anki_client.py        # Anki integration
├── tests/                    # 100 tests
├── docs/                     # Documentation
│   └── MANUAL_TESTING.md     # Testing guide
└── data/                     # Sessions and progress (gitignored)
```

## 🐛 Troubleshooting

### AnkiConnect Issues

**"AnkiConnect not available"**
- Ensure Anki Desktop is running
- Verify AnkiConnect addon is installed (Tools → Add-ons)
- Test connection: `curl http://localhost:8765`
- Check AnkiConnect configuration allows local connections

**"Failed to submit review to Anki"**
- Anki Desktop must be running during learning sessions
- Check `use_anki_scheduler: true` in `config.yaml`
- Verify card IDs are numeric (imported from Anki)
- Review AnkiConnect logs in Anki (Tools → Add-ons → AnkiConnect → View Files)

### Deck and Card Issues

**"Deck not found"**
- Check deck name is exact (case-sensitive)
- Verify deck contains cards in Anki
- Refresh Anki deck list
- Try listing decks first to see available names

**"Invalid card ID"**
- Cards must be imported from Anki with numeric IDs
- Cannot use manually created cards with string IDs for scheduler integration
- Set `use_anki_scheduler: false` for local-only mode without Anki updates

See [docs/MANUAL_TESTING.md](docs/MANUAL_TESTING.md) for detailed troubleshooting.

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development guidelines.

Key points:
- Follow ruff formatting
- Add tests for new features (target: 80% coverage)
- Update OpenSpec proposals for significant changes
- Use type hints everywhere

## License

Apache License 2.0 - see [LICENSE](LICENSE) file for details.

Copyright 2025 Michael Krech

## Status

✅ **MVP Complete** - All core features implemented with 102 passing tests (74% coverage)


## 文件 AGENTS.md

<!-- OPENSPEC:START -->
# OpenSpec Instructions

These instructions are for AI assistants working in this project.

Always open `@/openspec/AGENTS.md` when the request:
- Mentions planning or proposals (words like proposal, spec, change, plan)
- Introduces new capabilities, breaking changes, architecture shifts, or big performance/security work
- Sounds ambiguous and you need the authoritative spec before coding

Use `@/openspec/AGENTS.md` to learn:
- How to create and apply change proposals
- Spec format and conventions
- Project structure and guidelines

Keep this managed block so 'openspec update' can refresh the instructions.

<!-- OPENSPEC:END -->

## 文件 openspec/AGENTS.md

# OpenSpec Instructions

Instructions for AI coding assistants using OpenSpec for spec-driven development.

## TL;DR Quick Checklist

- Search existing work: `openspec spec list --long`, `openspec list` (use `rg` only for full-text search)
- Decide scope: new capability vs modify existing capability
- Pick a unique `change-id`: kebab-case, verb-led (`add-`, `update-`, `remove-`, `refactor-`)
- Scaffold: `proposal.md`, `tasks.md`, `design.md` (only if needed), and delta specs per affected capability
- Write deltas: use `## ADDED|MODIFIED|REMOVED|RENAMED Requirements`; include at least one `#### Scenario:` per requirement
- Validate: `openspec validate [change-id] --strict` and fix issues
- Request approval: Do not start implementation until proposal is approved

## Three-Stage Workflow

### Stage 1: Creating Changes
Create proposal when you need to:
- Add features or functionality
- Make breaking changes (API, schema)
- Change architecture or patterns  
- Optimize performance (changes behavior)
- Update security patterns

Triggers (examples):
- "Help me create a change proposal"
- "Help me plan a change"
- "Help me create a proposal"
- "I want to create a spec proposal"
- "I want to create a spec"

Loose matching guidance:
- Contains one of: `proposal`, `change`, `spec`
- With one of: `create`, `plan`, `make`, `start`, `help`

Skip proposal for:
- Bug fixes (restore intended behavior)
- Typos, formatting, comments
- Dependency updates (non-breaking)
- Configuration changes
- Tests for existing behavior

**Workflow**
1. Review `openspec/project.md`, `openspec list`, and `openspec list --specs` to understand current context.
2. Choose a unique verb-led `change-id` and scaffold `proposal.md`, `tasks.md`, optional `design.md`, and spec deltas under `openspec/changes/<id>/`.
3. Draft spec deltas using `## ADDED|MODIFIED|REMOVED Requirements` with at least one `#### Scenario:` per requirement.
4. Run `openspec validate <id> --strict` and resolve any issues before sharing the proposal.

### Stage 2: Implementing Changes
Track these steps as TODOs and complete them one by one.
1. **Read proposal.md** - Understand what's being built
2. **Read design.md** (if exists) - Review technical decisions
3. **Read tasks.md** - Get implementation checklist
4. **Implement tasks sequentially** - Complete in order
5. **Confirm completion** - Ensure every item in `tasks.md` is finished before updating statuses
6. **Update checklist** - After all work is done, set every task to `- [x]` so the list reflects reality
7. **Approval gate** - Do not start implementation until the proposal is reviewed and approved

### Stage 3: Archiving Changes
After deployment, create separate PR to:
- Move `changes/[name]/` → `changes/archive/YYYY-MM-DD-[name]/`
- Update `specs/` if capabilities changed
- Use `openspec archive <change-id> --skip-specs --yes` for tooling-only changes (always pass the change ID explicitly)
- Run `openspec validate --strict` to confirm the archived change passes checks

## Before Any Task

**Context Checklist:**
- [ ] Read relevant specs in `specs/[capability]/spec.md`
- [ ] Check pending changes in `changes/` for conflicts
- [ ] Read `openspec/project.md` for conventions
- [ ] Run `openspec list` to see active changes
- [ ] Run `openspec list --specs` to see existing capabilities

**Before Creating Specs:**
- Always check if capability already exists
- Prefer modifying existing specs over creating duplicates
- Use `openspec show [spec]` to review current state
- If request is ambiguous, ask 1–2 clarifying questions before scaffolding

### Search Guidance
- Enumerate specs: `openspec spec list --long` (or `--json` for scripts)
- Enumerate changes: `openspec list` (or `openspec change list --json` - deprecated but available)
- Show details:
  - Spec: `openspec show <spec-id> --type spec` (use `--json` for filters)
  - Change: `openspec show <change-id> --json --deltas-only`
- Full-text search (use ripgrep): `rg -n "Requirement:|Scenario:" openspec/specs`

## Quick Start

### CLI Commands

```bash
# Essential commands
openspec list                  # List active changes
openspec list --specs          # List specifications
openspec show [item]           # Display change or spec
openspec validate [item]       # Validate changes or specs
openspec archive <change-id> [--yes|-y]   # Archive after deployment (add --yes for non-interactive runs)

# Project management
openspec init [path]           # Initialize OpenSpec
openspec update [path]         # Update instruction files

# Interactive mode
openspec show                  # Prompts for selection
openspec validate              # Bulk validation mode

# Debugging
openspec show [change] --json --deltas-only
openspec validate [change] --strict
```

### Command Flags

- `--json` - Machine-readable output
- `--type change|spec` - Disambiguate items
- `--strict` - Comprehensive validation
- `--no-interactive` - Disable prompts
- `--skip-specs` - Archive without spec updates
- `--yes`/`-y` - Skip confirmation prompts (non-interactive archive)

## Directory Structure

```
openspec/
├── project.md              # Project conventions
├── specs/                  # Current truth - what IS built
│   └── [capability]/       # Single focused capability
│       ├── spec.md         # Requirements and scenarios
│       └── design.md       # Technical patterns
├── changes/                # Proposals - what SHOULD change
│   ├── [change-name]/
│   │   ├── proposal.md     # Why, what, impact
│   │   ├── tasks.md        # Implementation checklist
│   │   ├── design.md       # Technical decisions (optional; see criteria)
│   │   └── specs/          # Delta changes
│   │       └── [capability]/
│   │           └── spec.md # ADDED/MODIFIED/REMOVED
│   └── archive/            # Completed changes
```

## Creating Change Proposals

### Decision Tree

```
New request?
├─ Bug fix restoring spec behavior? → Fix directly
├─ Typo/format/comment? → Fix directly  
├─ New feature/capability? → Create proposal
├─ Breaking change? → Create proposal
├─ Architecture change? → Create proposal
└─ Unclear? → Create proposal (safer)
```

### Proposal Structure

1. **Create directory:** `changes/[change-id]/` (kebab-case, verb-led, unique)

2. **Write proposal.md:**
```markdown
## Why
[1-2 sentences on problem/opportunity]

## What Changes
- [Bullet list of changes]
- [Mark breaking changes with **BREAKING**]

## Impact
- Affected specs: [list capabilities]
- Affected code: [key files/systems]
```

3. **Create spec deltas:** `specs/[capability]/spec.md`
```markdown
## ADDED Requirements
### Requirement: New Feature
The system SHALL provide...

#### Scenario: Success case
- **WHEN** user performs action
- **THEN** expected result

## MODIFIED Requirements
### Requirement: Existing Feature
[Complete modified requirement]

## REMOVED Requirements
### Requirement: Old Feature
**Reason**: [Why removing]
**Migration**: [How to handle]
```
If multiple capabilities are affected, create multiple delta files under `changes/[change-id]/specs/<capability>/spec.md`—one per capability.

4. **Create tasks.md:**
```markdown
## 1. Implementation
- [ ] 1.1 Create database schema
- [ ] 1.2 Implement API endpoint
- [ ] 1.3 Add frontend component
- [ ] 1.4 Write tests
```

5. **Create design.md when needed:**
Create `design.md` if any of the following apply; otherwise omit it:
- Cross-cutting change (multiple services/modules) or a new architectural pattern
- New external dependency or significant data model changes
- Security, performance, or migration complexity
- Ambiguity that benefits from technical decisions before coding

Minimal `design.md` skeleton:
```markdown
## Context
[Background, constraints, stakeholders]

## Goals / Non-Goals
- Goals: [...]
- Non-Goals: [...]

## Decisions
- Decision: [What and why]
- Alternatives considered: [Options + rationale]

## Risks / Trade-offs
- [Risk] → Mitigation

## Migration Plan
[Steps, rollback]

## Open Questions
- [...]
```

## Spec File Format

### Critical: Scenario Formatting

**CORRECT** (use #### headers):
```markdown
#### Scenario: User login success
- **WHEN** valid credentials provided
- **THEN** return JWT token
```

**WRONG** (don't use bullets or bold):
```markdown
- **Scenario: User login**  ❌
**Scenario**: User login     ❌
### Scenario: User login      ❌
```

Every requirement MUST have at least one scenario.

### Requirement Wording
- Use SHALL/MUST for normative requirements (avoid should/may unless intentionally non-normative)

### Delta Operations

- `## ADDED Requirements` - New capabilities
- `## MODIFIED Requirements` - Changed behavior
- `## REMOVED Requirements` - Deprecated features
- `## RENAMED Requirements` - Name changes

Headers matched with `trim(header)` - whitespace ignored.

#### When to use ADDED vs MODIFIED
- ADDED: Introduces a new capability or sub-capability that can stand alone as a requirement. Prefer ADDED when the change is orthogonal (e.g., adding "Slash Command Configuration") rather than altering the semantics of an existing requirement.
- MODIFIED: Changes the behavior, scope, or acceptance criteria of an existing requirement. Always paste the full, updated requirement content (header + all scenarios). The archiver will replace the entire requirement with what you provide here; partial deltas will drop previous details.
- RENAMED: Use when only the name changes. If you also change behavior, use RENAMED (name) plus MODIFIED (content) referencing the new name.

Common pitfall: Using MODIFIED to add a new concern without including the previous text. This causes loss of detail at archive time. If you aren’t explicitly changing the existing requirement, add a new requirement under ADDED instead.

Authoring a MODIFIED requirement correctly:
1) Locate the existing requirement in `openspec/specs/<capability>/spec.md`.
2) Copy the entire requirement block (from `### Requirement: ...` through its scenarios).
3) Paste it under `## MODIFIED Requirements` and edit to reflect the new behavior.
4) Ensure the header text matches exactly (whitespace-insensitive) and keep at least one `#### Scenario:`.

Example for RENAMED:
```markdown
## RENAMED Requirements
- FROM: `### Requirement: Login`
- TO: `### Requirement: User Authentication`
```

## Troubleshooting

### Common Errors

**"Change must have at least one delta"**
- Check `changes/[name]/specs/` exists with .md files
- Verify files have operation prefixes (## ADDED Requirements)

**"Requirement must have at least one scenario"**
- Check scenarios use `#### Scenario:` format (4 hashtags)
- Don't use bullet points or bold for scenario headers

**Silent scenario parsing failures**
- Exact format required: `#### Scenario: Name`
- Debug with: `openspec show [change] --json --deltas-only`

### Validation Tips

```bash
# Always use strict mode for comprehensive checks
openspec validate [change] --strict

# Debug delta parsing
openspec show [change] --json | jq '.deltas'

# Check specific requirement
openspec show [spec] --json -r 1
```

## Happy Path Script

```bash
# 1) Explore current state
openspec spec list --long
openspec list
# Optional full-text search:
# rg -n "Requirement:|Scenario:" openspec/specs
# rg -n "^#|Requirement:" openspec/changes

# 2) Choose change id and scaffold
CHANGE=add-two-factor-auth
mkdir -p openspec/changes/$CHANGE/{specs/auth}
printf "## Why\n...\n\n## What Changes\n- ...\n\n## Impact\n- ...\n" > openspec/changes/$CHANGE/proposal.md
printf "## 1. Implementation\n- [ ] 1.1 ...\n" > openspec/changes/$CHANGE/tasks.md

# 3) Add deltas (example)
cat > openspec/changes/$CHANGE/specs/auth/spec.md << 'EOF'
## ADDED Requirements
### Requirement: Two-Factor Authentication
Users MUST provide a second factor during login.

#### Scenario: OTP required
- **WHEN** valid credentials are provided
- **THEN** an OTP challenge is required
EOF

# 4) Validate
openspec validate $CHANGE --strict
```

## Multi-Capability Example

```
openspec/changes/add-2fa-notify/
├── proposal.md
├── tasks.md
└── specs/
    ├── auth/
    │   └── spec.md   # ADDED: Two-Factor Authentication
    └── notifications/
        └── spec.md   # ADDED: OTP email notification
```

auth/spec.md
```markdown
## ADDED Requirements
### Requirement: Two-Factor Authentication
...
```

notifications/spec.md
```markdown
## ADDED Requirements
### Requirement: OTP Email Notification
...
```

## Best Practices

### Simplicity First
- Default to <100 lines of new code
- Single-file implementations until proven insufficient
- Avoid frameworks without clear justification
- Choose boring, proven patterns

### Complexity Triggers
Only add complexity with:
- Performance data showing current solution too slow
- Concrete scale requirements (>1000 users, >100MB data)
- Multiple proven use cases requiring abstraction

### Clear References
- Use `file.ts:42` format for code locations
- Reference specs as `specs/auth/spec.md`
- Link related changes and PRs

### Capability Naming
- Use verb-noun: `user-auth`, `payment-capture`
- Single purpose per capability
- 10-minute understandability rule
- Split if description needs "AND"

### Change ID Naming
- Use kebab-case, short and descriptive: `add-two-factor-auth`
- Prefer verb-led prefixes: `add-`, `update-`, `remove-`, `refactor-`
- Ensure uniqueness; if taken, append `-2`, `-3`, etc.

## Tool Selection Guide

| Task | Tool | Why |
|------|------|-----|
| Find files by pattern | Glob | Fast pattern matching |
| Search code content | Grep | Optimized regex search |
| Read specific files | Read | Direct file access |
| Explore unknown scope | Task | Multi-step investigation |

## Error Recovery

### Change Conflicts
1. Run `openspec list` to see active changes
2. Check for overlapping specs
3. Coordinate with change owners
4. Consider combining proposals

### Validation Failures
1. Run with `--strict` flag
2. Check JSON output for details
3. Verify spec file format
4. Ensure scenarios properly formatted

### Missing Context
1. Read project.md first
2. Check related specs
3. Review recent archives
4. Ask for clarification

## Quick Reference

### Stage Indicators
- `changes/` - Proposed, not yet built
- `specs/` - Built and deployed
- `archive/` - Completed changes

### File Purposes
- `proposal.md` - Why and what
- `tasks.md` - Implementation steps
- `design.md` - Technical decisions
- `spec.md` - Requirements and behavior

### CLI Essentials
```bash
openspec list              # What's in progress?
openspec show [item]       # View details
openspec validate --strict # Is it correct?
openspec archive <change-id> [--yes|-y]  # Mark complete (add --yes for automation)
```

Remember: Specs are truth. Changes are proposals. Keep them in sync.

