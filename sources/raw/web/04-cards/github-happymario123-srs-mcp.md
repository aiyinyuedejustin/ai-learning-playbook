# happymario123/srs-mcp

- 链接：https://github.com/happymario123/srs-mcp
- 作者：happymario123
- 仓库说明：Spaced-repetition MCP server for Claude — study any topic, right inside your coding sessions
- 星数：0
- 获取方式：GitHub README

---

## README

# srs-mcp — spaced repetition, as an MCP server

Give any MCP-capable agent (Claude Code, Claude Desktop, or any other
MCP host) real, correctly-scheduled spaced-repetition memory instead of
re-deriving "what's due today" from a markdown table by hand every
session. Implements SM-2 (the algorithm behind Anki/SuperMemo) as four
callable tools, backed by a local SQLite file. No account, no network
calls, no telemetry — everything runs on your machine.

**Status: prototype, not yet published anywhere.** Built and verified
locally (see "How it's been verified" below); not yet installed by
anyone outside this project. Treat version 0.2.0 as pre-release.

## Why this exists

Markdown checklists and vocab tables are common ways people (and the
agents helping them) track what to review, but nothing computes an
actual schedule from them — "due today" ends up being a guess, re-read
by eye every time. srs-mcp is the missing piece: a small, real
scheduling algorithm exposed as tools, so an agent can track review
state for anything — flashcards, interview questions, vocab, onboarding
quizzes — without re-implementing SM-2 in a prompt.

## The four core tools (free, unlimited, forever)

| Tool | What it does |
|---|---|
| `add_item(topic, question, answer)` | Add a review item under a topic. New items are due immediately. |
| `get_due_items(topic="", limit=10)` | List items due today or overdue. Answer withheld until graded, like a real flashcard review. |
| `grade_item(item_id, quality)` | Grade recall 0–5 (5 = perfect, <3 = fail/reset). Returns the next due date via SM-2 and the correct answer. |
| `get_stats(topic="")` | Totals, due-today count, average ease factor. |

## Get Pro

Two additional tools are gated behind a Pro license — this is the
free/paid split srs-mcp uses instead of subscriptions or a hosted
backend:

| Tool | What it does |
|---|---|
| `export_items(topic="", format="json"\|"csv")` | Bulk export/backup all your review data. |
| `get_forecast(topic="", days=30)` | Review-load forecast — how many items come due each of the next N days, so a pile-up is visible before it happens. |

**How licensing works, concretely:** srs-mcp signs license keys with an
Ed25519 private key that never leaves the maintainer's machine; this
repo ships only the matching public key (`license.py`), which can
verify a signature but can't forge one. Buy a key, set it as
`SRS_LICENSE_KEY` (env var) or save it to `~/.srs-mcp/license.key`, and
the Pro tools unlock — no account, no phone-home check, works offline.
See `license.py` for the full mechanism and its stated limitations
(short version: this deters casual copying, it isn't DRM — nothing
stops someone from patching out the check in their own local copy of
an open-source Python file; see the module docstring for the honest
version of this tradeoff).

**No live purchase link exists yet.** This section describes the
mechanism, which is built and tested (see `test_license_gate.py`), not
a working store. When a purchase flow exists, it goes here.

## Install

Requires Python 3.11+.

```bash
git clone <repo-url>   # not yet public — see status note above
cd srs-mcp
python3 -m venv .venv
.venv/bin/pip install -e .
.venv/bin/srs-mcp       # runs the server on stdio
```

To use it as a Claude Code plugin, point Claude Code at this directory
(or, once published, at its marketplace listing) — `.claude-plugin/plugin.json`
and `.mcp.json` are already set up; the server reads `SRS_DB_PATH` so a
plugin install's data survives updates (`${CLAUDE_PLUGIN_DATA}/srs.db`
under Claude Code, or a co-located `srs.db` for a direct/manual run).

## How it's been verified

Not just "it imports" — actually run, over the real MCP protocol:

- `test_client.py` spawns `server.py` as a subprocess (the same way a
  real MCP host does), drives a full add/list/grade/list session, and
  independently re-checks the resulting SQLite rows outside the test
  harness.
- `test_license_gate.py` spawns the server three ways (no license,
  valid license, tampered license) and confirms `export_items` /
  `get_forecast` refuse in cases 1 and 3 and return real data in case 2
  — proving the license check is a real gate, not a no-op.
- `examples/bulk_import.py` is a working, idempotent example script that
  loads a generic CSV or JSON file of items into srs-mcp via real
  `add_item` MCP calls (not direct SQLite writes) — a starting point for
  bulk-loading your own tracker (vocab, interview prep, onboarding
  checklists, anything else) instead of adding items one at a time.

## Honest gap to "ready to launch" — not rounded up

1. **No public repo.** Every real distribution path (Claude Code's
   community plugin marketplace, a GitHub release, an MCP directory
   listing) needs this reachable at a public git URL. This project is
   local-only. Creating that (a GitHub repo, possibly an account) is
   outside this project's current autonomy without an explicit
   go-ahead — everything above is prepared to make that a
   copy-and-push action, not a build task, once given.
2. **Can't self-validate against `claude plugin validate`.** No `claude`
   CLI or Node/npx available in this dev environment. The plugin
   manifest is schema-conformant as far as careful reading of
   Anthropic's docs and cross-referencing their own production
   `marketplace.json` can confirm, not machine-validated.
3. **No live purchase flow.** The license mechanism is real and tested;
   turning it into an actual sale needs a storefront (Ko-fi, Gumroad,
   or similar) that doesn't exist yet — that's an account-creation step,
   outside this project's autonomy without a go-ahead.
4. **License enforcement is honesty-based, not tamper-proof**, by
   design and by the nature of shipping readable Python — see the
   "Get Pro" section above and `license.py`'s docstring.
5. **No auth/multi-tenant story.** Single local SQLite file, single
   user. Fine for the current "runs on your machine" model; would need
   real design work to become a hosted/team product.
6. **Zero external validation.** Nobody outside this project has
   installed or used this. Every claim above is "this works as built
   and tested," not "people want this."

## License

MIT — see `LICENSE`. (The Pro-tier *license key mechanism* is separate
from the code's own MIT license — see "Get Pro" above.)

