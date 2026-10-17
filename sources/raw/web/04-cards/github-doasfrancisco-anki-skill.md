# doasfrancisco/anki-skill

- 链接：https://github.com/doasfrancisco/anki-skill
- 作者：doasfrancisco
- 仓库说明：
- 星数：57
- 获取方式：GitHub README + SKILL/说明文件

---

## README

# Anki Skill

A Claude Code skill that creates and browses Anki flashcards during coding sessions. When you're learning something new — a concept, gotcha, or mental model — Claude proposes a card, you approve it, and it's in your deck.

## Demo

https://www.loom.com/share/0248912742334161936f4aabba55105b

## Why

I have 500+ Anki cards and 226 leeches. Bad cards are the problem. This skill enforces quality rules so every card Claude creates is atomic, minimal, and worth remembering long-term.

## How it works

1. You're coding with Claude Code and learn something new
2. Claude notices and proposes a flashcard (or you invoke `/anki`)
3. You review the front, back, deck, and tags
4. On approval, the card is created in Anki via AnkiConnect

No external dependencies — just Python's stdlib (`urllib.request`).

## Prerequisites

- **Anki desktop** running on your machine
- **AnkiConnect addon** installed — open Anki, go to Tools > Add-ons > Get Add-ons, paste code `2055492159`, restart Anki. This exposes a local API on port 8765 that the skill talks to.

## Setup

1. Copy this folder to `~/.claude/skills/anki/`
2. (Optional) Add a SessionStart hook to remind Claude about card creation:

```json
{
  "type": "command",
  "command": "echo \"Reminder: You can create Anki flashcards with /anki. If you notice the user learning something new, proactively suggest a card.\""
}
```

## Usage

### Create a card

```bash
python ./scripts/create_card.py \
  --deck "7. computer science" \
  --front "What does __slots__ do in Python?" \
  --back "Restricts instance attributes to a fixed set, saving memory by skipping __dict__." \
  --tags "python,memory"
```

### List cards

```bash
python ./scripts/list_cards.py --query "tag:python added:7"
python ./scripts/list_cards.py --deck "7. computer science" --added 30
```

### List decks

```bash
python -c "import sys; sys.path.insert(0, './scripts'); from anki_connect import list_decks; print(list_decks())"
```

## Card quality rules

1. **Atomic** — one fact per card
2. **Short, specific front** — few words, one unambiguous answer
3. **Minimal back** — no unnecessary text
4. **Visual over prose** — file trees and code blocks over sentences
5. **No trivia** — only things worth remembering long-term
6. **Tag consistently** — lowercase, comma-separated

## Project structure

```
anki-skill/
├── SKILL.md          # Claude Code skill definition
├── README.md
└── scripts/
    ├── anki_connect.py   # AnkiConnect client (stdlib only)
    ├── create_card.py    # CLI: create a card
    └── list_cards.py     # CLI: list/filter cards
```


## 文件 SKILL.md

---
name: anki
description: Create and browse Anki flashcards during coding sessions. Use when the user invokes /anki, asks to create a flashcard, or when you notice the user learning something new and worth remembering (a concept, trick, gotcha, or mental model).
---

# Anki Card Creator

Create flashcards from Claude Code. Scripts are bundled in `./scripts/`.

## Available operations

### Create a card

```bash
python ./scripts/create_card.py \
  --deck "7. computer science" \
  --front "What does __slots__ do in Python?" \
  --back "Restricts instance attributes to a fixed set, saving memory by skipping the per-instance __dict__." \
  --tags "python,memory"
```

### List cards (check for duplicates before creating)

```bash
python ./scripts/list_cards.py --query "tag:python added:7"
python ./scripts/list_cards.py --deck "7. computer science" --added 30
```

### List decks (discover deck names)

```bash
python -c "import sys; sys.path.insert(0, './scripts'); from anki_connect import list_decks; print(list_decks())"
```

## Card quality rules

The user has 226 leeches. Quality over quantity.

1. **Atomic** — one fact per card. If the answer has "and", split it.
2. **Short, specific front** — few words, one unambiguous answer. Not open-ended.
3. **Minimal back** — no unnecessary text. If a structure speaks for itself, don't add explanation below it.
4. **Visual over prose** — prefer file trees, code blocks, or diagrams over sentences when the answer is structural.
5. **No trivia** — only things worth remembering long-term (concepts, gotchas, mental models).
6. **Tag consistently** — use lowercase, comma-separated (e.g. `python,decorators`).

### Good card

- Front: "What's the file structure of a Claude Code skill?"
- Back:
```
<skill>/
├── SKILL.md
└── scripts/
    ├── main.py
    └── helpers.py
```

### Bad card

- Front: "Explain Python's memory model, GIL, and garbage collection"
- Back: (three paragraphs) — too many facts, split into separate cards.

## Workflow

1. **Propose** the card: show front, back, deck, and tags in a formatted block.
2. **Wait** for user approval. Never create without explicit confirmation.
3. **Check duplicates** with `list_cards.py --query "<relevant keywords>"` before creating.
4. **Create** the card only after approval.
5. **Confirm** with the note ID from the output.

## Troubleshooting

If the connection fails, Anki desktop must be running with the AnkiConnect addon installed (addon code: 2055492159).

