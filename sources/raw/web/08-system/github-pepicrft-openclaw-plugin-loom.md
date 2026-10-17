# pepicrft/openclaw-plugin-loom：md 学习图谱

- 链接：https://github.com/pepicrft/openclaw-plugin-loom
- 作者：pepicrft
- 仓库说明：
- 星数：16
- 获取方式：GitHub README + SKILL/说明文件

---

## README

# OpenClaw Loom

[![CI](https://github.com/pepicrft/openclaw-plugin-loom/actions/workflows/ci.yml/badge.svg)](https://github.com/pepicrft/openclaw-plugin-loom/actions/workflows/ci.yml)

An OpenClaw plugin that turns your learning into a **living graph** of nodes, paths, and context captures. Loom blends mastery learning, spaced repetition, and retrieval practice, and indexes everything with QMD for fast search across Markdown and QMD files.

## Features

- Learning graph with prerequisites, unlocks, and mastery states
- Spaced repetition scheduling with review ratings
- Next-node recommendations with automatic unlocks
- Context captures to inject real-life situations into your learning map
- Local-first Markdown/QMD library with clean folder structure
- QMD indexing for semantic search and embeddings
- Optional git sync to keep your library in version control

## Installation

```bash
openclaw plugins install openclaw-plugin-loom
```

Or from GitHub:

```bash
<<<<<<< HEAD
openclaw plugins install github:pepicrft/clawd-plugin-loom
=======
openclaw plugins install github:pepicrft/openclaw-plugin-loom
>>>>>>> 72e4635 (Rename from clawd-plugin-loom to openclaw-plugin-loom)
```

## Configuration

```json5
{
  plugins: {
    entries: {
      "openclaw-plugin-loom": {
        enabled: true,
        config: {
          libraryPath: "/Users/you/Loom",
          collectionName: "learn",
          gitRemote: "origin",
          gitBranch: "main",
          gitSync: true,
          gitAutoCommit: true,
          autoInstallQmd: true,
          mask: "**/*.md",
          masteryThreshold: 4,
          srsIntervals: [1, 3, 7, 14, 30, 60, 120, 240]
        }
      }
    }
  }
}
```

## Loom Framework

### Folder Convention

- paths/ -> one folder per learning path (Nix, German, etc.)
- nodes/ -> learning nodes grouped by path
- contexts/ -> quick captures from real-life situations
- sessions/ -> auto-logged review sessions
- resources/ -> PDFs, links, or datasets

Notes are plain Markdown files; reference other nodes by id using wikilinks (e.g. `[[nix/derivations]]`) or normal links.

### What Is a Node?

A node is the smallest unit of learning you want to master. It should be **narrow, testable, and self-contained**.

Good node contents:
- A short explanation in your own words
- A concrete example or mini exercise
- Links to prerequisite or follow-up nodes by `id`
- If relevant, a "check yourself" prompt (question or task)

### Node Frontmatter

Required:
- id
- title
- path
- created
- updated

Recommended:
- summary
- type: concept | practice | project | checkpoint
- status: locked | available | in-progress | mastered | paused
- prerequisites: [node_id]
- unlocks: [node_id]
- familiarity: 0-5
- srs_stage: 0+
- last_reviewed
- next_review
- tags

Example:

```md
---
id: "german/akkusativ"
title: "Akkusativ basics"
summary: "Use Akkusativ with direct objects"
path: "german"
type: "concept"
status: "available"
prerequisites:
  - "german/der-die-das"
unlocks:
  - "german/dative-intro"
familiarity: 1
srs_stage: 0
last_reviewed: null
next_review: null
created: "2026-01-03T12:00:00.000Z"
updated: "2026-01-03T12:00:00.000Z"
tags:
  - "grammar"
---

Body starts here.
```

## Usage

### CLI

```bash
# Initialize the library structure
openclaw learn init

# Create a path
openclaw learn path "Nix"

# Add a node
openclaw learn node "Nix Store Basics" \
  --path nix \
  --summary "Understand /nix/store layout" \
  --tags nix,foundations

# Capture a contextual situation
openclaw learn capture "German bakery chat" \
  --path german \
  --tags german,speaking \
  "Asked for Schrippen and got confused about plural forms"

# Unlock nodes whose prerequisites are met
openclaw learn unlock

# Suggest next node to study
openclaw learn next --start

# Review a node
openclaw learn review nix/store-basics --rating good

# Query the library
openclaw learn query "nix derivations" --mode query --limit 5
```

### Tools (for agents)

- `learn_add_node`
- `learn_capture`
- `learn_next`
- `learn_review`
- `learn_query`

### Gateway RPC

- `learn.add`
- `learn.capture`
- `learn.next`
- `learn.review`
- `learn.query`
- `learn.graph`

## Git Sync

When git sync is enabled, Loom:

1. Pulls before reading or writing
2. Auto-commits changes (when `gitAutoCommit` is true)
3. Pushes after writing

## QMD Setup

The plugin auto-installs `qmd` if missing:

- Uses `bun install -g https://github.com/tobi/qmd` when bun is available
- Falls back to `npm install -g https://github.com/tobi/qmd`

If you want to manage `qmd` manually, set `autoInstallQmd: false`.

## SRS Defaults

The default spaced-repetition intervals (days) are:

```
[1, 3, 7, 14, 30, 60, 120, 240]
```

You can override them via `srsIntervals` in the plugin config.

## Requirements

- Node 20+
- bun or npm for installing qmd (unless qmd already installed)

## Tests

```bash
npm test
npm run build
```

## Research Notes

See `RESEARCH.md` for the learning science sources used to design Loom's framework.

## Learning Framework References

The framework is informed by these cross-topic learning principles:

- **Distributed practice / spacing effect**: Cepeda et al. (2006), *Psychological Science*. DOI: https://doi.org/10.1111/j.1467-9280.2006.01684.x
- **Testing effect / retrieval practice**: Roediger & Karpicke (2006), *Science*. DOI: https://doi.org/10.1126/science.1152408
- **Interleaving vs. blocking**: Kornell & Bjork (2008), *Psychological Science*. DOI: https://doi.org/10.1111/j.1467-9280.2008.02127.x
- **Mastery learning**: Bloom (1968), *Learning for Mastery*. ERIC: https://files.eric.ed.gov/fulltext/ED053419.pdf
- **Deliberate practice**: Ericsson, Krampe, & Tesch-Romer (1993), *Psychological Review*. DOI: https://doi.org/10.1037/0033-295X.100.3.363
- **Concept mapping**: Novak & Gowin (1984), *Learning How to Learn*.


## 文件 SKILL.md

# Loom Learning Graph Skill

This skill guides agents on how to use the Loom plugin to build and expand a learning graph over time.

## Purpose
- Help users navigate learning paths (e.g., Nix, German) through graph nodes.
- Expand the graph organically as new knowledge appears.
- Keep knowledge warm with spaced repetition reviews.

## Core Model
- **Path**: a learning track (e.g., `nix`, `german`).
- **Node**: atomic learning unit with prerequisites, unlocks, and review scheduling.
- **Context**: real-world capture that should seed new nodes or enrich existing ones.

## What a Node Contains
- A short explanation in your own words
- A concrete example or mini exercise
- Links to prerequisite or follow-up nodes by `id`
- A “check yourself” prompt (question or task)

## When to Create Nodes
- When a user says “I want to learn X”, **create a path** for X and seed 1-3 starter nodes.
- When a user mentions a new concept, term, or confusion point, **create a node**.
- When a context capture reveals missing scaffolding, **add prerequisites**.
- When a node reaches mastery, **add or unlock a next node** that builds on it.
- When a session reveals gaps, **insert a bridging node**.

## How to Expand the Graph
- Prefer **small, focused nodes** over large, vague ones.
- Use `prerequisites` to gate advanced topics.
- Add `unlocks` to highlight natural next steps.
- Always link nodes by `id` in body text (wikilinks are fine).

## Workflow (Agent)
1. **Capture context** when the user mentions a real situation.
2. **Create or update nodes** from the context.
3. **Unlock nodes** when prerequisites are mastered.
4. **Recommend next** using `learn next` and prompt review with `learn review`.

## Tooling
- `learn_add_node` to add nodes.
- `learn_capture` to capture contexts.
- `learn_next` to pick the next node.
- `learn_review` to schedule repetition.
- `learn_query` to search the library.

## Defaults
- Nodes are Markdown (`.md`).
- Spaced repetition intervals default to `[1, 3, 7, 14, 30, 60, 120, 240]` days.

## Example Triggers
- “I read about Nix flakes today” → add node `nix/flakes` with prereqs.
- “I got confused ordering coffee in German” → capture context and add node `german/ordering-coffee`.

