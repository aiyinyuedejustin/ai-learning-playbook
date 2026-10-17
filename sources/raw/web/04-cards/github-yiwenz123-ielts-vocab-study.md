# YiwenZ123/ielts-vocab-study：雅思托福词汇 skill

- 链接：https://github.com/YiwenZ123/ielts-vocab-study
- 作者：YiwenZ123
- 仓库说明：IELTS/TOEFL vocab study skill (Claude Code) - SQLite CLI, spaced repetition
- 星数：0
- 获取方式：GitHub README + SKILL/说明文件

---

## README

# ielts-vocab-study

IELTS/TOEFL academic vocabulary study skill for Claude Code / Cursor.

- SQLite-backed spaced repetition CLI (`scripts/vocab.py`)
- 1000-word seed list (`assets/ielts_vocab_seed.csv`)
- JSON + terminal text reports (progress maps, daily summary, wrong-words notebook, CSV export)
- Beijing time (UTC+8) for sessions and timestamps

## Quick start

```powershell
$env:PYTHONIOENCODING='utf-8'
py scripts/vocab.py --format text stats
py tests/test_vocab_cli.py
```

See `SKILL.md` for agent workflows and `INSTALL.md` for Cursor junction setup.

## Layout

| Path | Purpose |
|------|---------|
| `SKILL.md` | Agent skill instructions |
| `scripts/vocab.py` | CLI |
| `assets/ielts_vocab_seed.csv` | Word seed data |
| `tests/test_vocab_cli.py` | CLI tests |

Default database (not in repo): `%USERPROFILE%\.codex\data\ielts-vocab-study\study.sqlite`


## 文件 SKILL.md

---
name: ielts-vocab-study
description: Use when the user wants to learn new English vocabulary (IELTS/TOEFL academic words), review learned words, check study progress, look up a specific word, view wrong words, export progress, or check today's study summary. Triggers on phrases like "learn new words", "review vocabulary", "study progress", "wrong words", "export progress", "today's progress", "vocab", "ielts words", "toefl words", "academic vocabulary", or any similar request about IELTS/TOEFL vocabulary study.
---

# IELTS Vocabulary Study Skill

Use the bundled CLI for all study operations. The CLI auto-initializes the database when it is empty, so normal study flows should not run `init` first.

Claude Code Bash tool, Bash, or zsh:
```bash
PYTHONIOENCODING=utf-8 uv run --python 3.13 python <SKILL_DIR>/scripts/vocab.py [global-options] <command> [args]
```

PowerShell only:
```powershell
$env:PYTHONIOENCODING='utf-8'; uv run --python 3.13 python <SKILL_DIR>/scripts/vocab.py [global-options] <command> [args]
```

Resolve `<SKILL_DIR>` to the directory containing this `SKILL.md`. Put global options such as `--db` and `--format text` before the subcommand. The default database is `~/.codex/data/ielts-vocab-study/study.sqlite`, shared with the Codex copy of this skill so progress survives skill updates.

Use JSON for internal parsing and conversation flow. Use `--format text` when the user asks for a report, summary, dashboard, wrong-words notebook, or export confirmation; text output is a terminal-friendly character dashboard with progress bars, grid maps, sparklines, and ranked bars.

## Initialization

Do not run `init` at the start of each conversation. The CLI automatically imports the bundled 1000-word seed data the first time a normal command opens an empty database.

Use `init` only when the user explicitly asks to initialize, repair, migrate, or refresh the bundled word list:

```bash
PYTHONIOENCODING=utf-8 uv run --python 3.13 python <SKILL_DIR>/scripts/vocab.py init
```

`init` imports 1000 academic words and is idempotent. It also migrates older databases, including known seed spelling corrections.

## Commands

### Learn New Words
```bash
... vocab.py select --mode learn --limit 10
```
Returns up to 10 new words. `--limit` must be 1-100. If an unfinished learn session exists today, the command resumes it and returns only the remaining words.

### Review Learned Words
```bash
... vocab.py select --mode review --limit 20
```
Returns due words from `learning`, `reviewing`, and due `mastered` words. Selection uses a lightweight spaced-repetition schedule (`next_review_at`, `interval_days`, `ease_factor`). If an unfinished review session exists today, the command resumes it.

Each returned word includes `days_overdue` (integer ≥ 0; 0 = "due today" or freshly scheduled). In text mode each entry is suffixed with `(due today)` or `(N days overdue)` so the agent can prioritize the most stale words first.

### Record A Result
```bash
... vocab.py record --word <WORD> --mode learn --result remembered|partial|forgot
... vocab.py record --word <WORD> --mode review --result remembered|partial|forgot
```

- `remembered`: user recalled the meaning correctly
- `partial`: user partly remembered or needed a hint
- `forgot`: user could not recall the meaning

Word lookup is case-insensitive and trims extra whitespace. Recording marks the word completed in any active session; a session auto-closes when all its words are recorded.

### Statistics
```bash
... vocab.py stats
... vocab.py stats --word <WORD>
```

Overall stats include total words, status counts, `learned_words` / `mastered_words` with matching `learned_pct` / `mastered_pct` ratios, due review count, average accuracy, most recent review, and review result distribution. Per-word stats include definition, Chinese translation, phonetic, difficulty (1–5), status, accuracy, schedule fields, and recent reviews.

### Daily Summary
```bash
... vocab.py daily
```

Shows today's summary using the Beijing (UTC+8) calendar date: sessions, learned/reviewed counts, result distribution, accuracy, and current streak.

For a human-readable report:
```bash
... vocab.py --format text daily
```

### Wrong Words Notebook
```bash
... vocab.py wrong --limit 50 --offset 0
... vocab.py wrong --limit 20 --detail
```

Lists words with `wrong_count > 0`, ordered by wrong count and most recent forgotten attempt. `--detail` includes the last five forgotten attempts per word. `--limit` must be 1-500.

For a styled wrong-words report:
```bash
... vocab.py --format text wrong --limit 20 --detail
```

### Export Progress
```bash
... vocab.py export --path <PATH>
```

Exports all words and progress to CSV. Default path is `~/ielts_vocab_report_YYYYMMDD.csv`. The CSV uses UTF-8 BOM for Windows Excel and includes stable columns such as `accuracy_rate`, `total_reviews`, `remembered_count`, `partial_count`, and `forgot_count`.

For a styled export confirmation:
```bash
... vocab.py --format text export --path <PATH>
```

## Opening (Greeting when skill is invoked)

When the skill is invoked (user types `/ielts-vocab-study` or a trigger phrase), follow this **exact** sequence. Do NOT improvise the layout — use the CLI's text output verbatim and the fixed menu template below.

### Step 1 — Fetch data

Run **both** commands in parallel:

```bash
... vocab.py --format text stats
... vocab.py --format text daily
```

### Step 2 — Render the greeting

Output the two text reports **as-is** (they already contain progress bars, sparklines, maps, etc.), separated by a blank line. Do NOT wrap them in markdown tables or reformat them.

Then append this **fixed menu** verbatim (replace `<N>` with the actual due-review count from the stats JSON — run `vocab.py stats` in JSON mode if you need the number, or parse it from the text output):

```
---

**What would you like to do?**

1. Learn New Words — Study a batch of new IELTS/TOEFL core vocabulary
2. Review Words — <N> words are due for review
3. Check Progress — Detailed study statistics
4. Wrong Words — View frequently forgotten words
5. Export Progress — Export a CSV study report

Please choose a number, or tell me what you'd like to do!
```

### Rules for the opening

- Never build the dashboard manually with markdown tables or emoji grids. Always delegate to `--format text`.
- If the database is brand-new (all 1000 words are `new`), the text output already handles this gracefully — just show it.
- If an active session exists, the daily report's `[Next Step]` section will mention it. Do not add extra reminders.
- Keep the opening concise: two text blocks + the menu. No extra commentary before or between them.

## Conversation Flow

### Learning
1. Run `select --mode learn --limit N`.
2. For each word, show the English word, phonetic transcription, and part of speech first.
3. Prompt the user with exactly two options and wait for their reply:
   - Type their own understanding of the word (Chinese or English, free-form).
   - Reply "I don't know".
4. After the user replies, reveal `definition_en`, `definition_zh`, `example_en`, and `theme`.
5. **Auto-evaluate** the user's answer against the revealed definition and choose a result silently (do not ask the user to self-assess):
   - `remembered`: the user's answer captures the core meaning correctly.
   - `partial`: the user's answer is partly correct (right general area but missing key detail, or mixing in a wrong sense).
   - `forgot`: the user's answer is clearly wrong, unrelated, or they said "I don't know".
6. Run `record --word <WORD> --mode learn --result <RESULT>` and briefly tell the user which result was chosen and why (one short sentence).
7. Continue to the next word automatically. After the last word, summarize results.

### Reviewing
1. Run `select --mode review --limit N`.
2. If no due words are returned, tell the user nothing is due and suggest learning new words or checking progress.
3. Present only the English word (with phonetic and part of speech) as a recall prompt, with the same two options:
   - Type their own understanding of the word.
   - Reply "I don't know".
4. After the user replies, reveal the definition, translation, and example.
5. **Auto-evaluate** the answer as in the Learning flow (remembered / partial / forgot), then run `record --word <WORD> --mode review --result <RESULT>` with a one-sentence explanation.
6. Continue to the next word automatically. After the last word, summarize remembered / partial / forgot counts.

### Auto-evaluation rules
- Judge meaning, not exact wording. A colloquial Chinese paraphrase that captures the core sense counts as `remembered`.
- If the user mentions one valid sense of a polysemous word but misses others, treat it as `remembered` (the example sentence disambiguates).
- If the user confuses the word with a clearly different word (e.g., "prone" → "俯卧的" when the example is about tendency), treat it as `partial`, not `forgot`, unless nothing overlaps.
- Never ask the user to pick remembered / partial / forgot themselves; always decide and explain the decision.

### Progress, Lookup, Daily, Wrong Words, Export
- For overall progress, run `stats` and summarize learned/mastered/due counts and accuracy.
- For one word, run `stats --word <WORD>` and show the entry plus recent review history.
- For today's report, run `daily` and mention active incomplete sessions.
- For wrong words, run `wrong --limit 20`; optionally re-test those words using the review flow.
- For export, run `export --path PATH` or the default path and report the generated file path and row count.

## Important Notes

- Use `PYTHONIOENCODING=utf-8` in command examples; the script also reconfigures stdout/stderr to UTF-8 defensively.
- Default output is JSON. Use `--format text` for terminal-visual user-facing reports.
- `review_count` increments only in `review` mode.
- Status transitions: `new` -> `learning` -> `reviewing` -> `mastered`.
- A word becomes `mastered` after 5+ review attempts and at least 80% decisive accuracy.
- `accuracy_rate = correct_count / (correct_count + wrong_count)` and excludes `partial`.
- `mastered` words remain eligible when their `next_review_at` is due.
- A `forgot` result (in either `learn` or `review` mode) sets `interval_days = 0`, so the word becomes due immediately and reappears in the very next `select --mode review` batch instead of waiting until tomorrow.
- If all words are learned, congratulate the user and suggest review.
- The CLI uses only the Python standard library.

## Language

Present guidance, prompts, and summaries in English. Show vocabulary definitions and examples in English with Chinese translations.

