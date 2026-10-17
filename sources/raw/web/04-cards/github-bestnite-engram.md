# bestnite/engram

- 链接：https://github.com/bestnite/engram
- 作者：bestnite
- 仓库说明：Self-hosted, multi-user spaced-repetition (SRS) service: FSRS v6 scheduling, 10 card types, Markdown/TeX, REST API and built-in MCP server. Written in Go.
- 星数：11
- 获取方式：GitHub README + SKILL/说明文件

---

## README

# Engram

[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL--3.0-blue.svg)](LICENSE)
[![Go Version](https://img.shields.io/badge/Go-1.26+-00ADD8?logo=go&logoColor=white)](go.mod)
[![Docker Image](https://img.shields.io/badge/Docker-nite07%2Fengram-2496ED?logo=docker&logoColor=white)](https://hub.docker.com/r/nite07/engram)
[![Algorithm](https://img.shields.io/badge/Algorithm-FSRS%20v6-brightgreen)](https://github.com/open-spaced-repetition/go-fsrs)

**English** | [中文](README.zh.md)

Engram is an open-source, self-hosted spaced repetition flashcard service. Built with a modern Svelte 5 SPA frontend and a Go backend, it pairs the state-of-the-art **FSRS v6** scheduling algorithm with a native **Model Context Protocol (MCP)** server for AI-assisted card creation and workflow automation.

Live demo: <https://engram.nite07.com/> (registration is closed; sign in with the test account `test` / `testdemo`)

---

## Screenshots

| Deck Management | Card Review (Question) |
| :---: | :---: |
| ![Deck Management](screenshots/1.png) | ![Card Review Question](screenshots/2.png) |
| **Answer Revealed** | **Instant Feedback** |
| ![Answer Revealed](screenshots/3.png) | ![Answer Feedback](screenshots/4.png) |
| **Study Statistics & Insights** | **Card Creation & Editor** |
| ![Study Statistics](screenshots/5.png) | ![Card Creation](screenshots/6.png) |

---

## Features

- **FSRS v6 Scheduling**: Adaptive scheduling based on the open-source FSRS v6 algorithm, optimizing review intervals and reducing workload compared to legacy SM-2 algorithms. Supports custom parameter optimization.
- **Rich Card Types**: Multiple question types built in — cloze, typed answer, numeric with tolerance, single-choice, multiple-choice, and true/false. Card bodies support Markdown, MathJax formulas, and media uploads.
- **Multi-user & Deck Sharing**: Multi-tenant architecture with OIDC / Single Sign-On (SSO) support. Decks can be shared across users while keeping each user's review scheduling and progress strictly isolated.
- **AI & MCP Native**: Built-in Model Context Protocol server exposing dedicated tools for LLMs and agents to search, create, update, review, and export flashcards.
- **Modern Interface & PWA**: Clean single-page application built with Svelte 5 and Tailwind CSS, featuring dark/light themes, keyboard navigation shortcuts, internationalization (`zh-CN` and `en`), and PWA support.
- **Email Reminders & Digest**: Automated daily review alerts and weekly summaries via SMTP.
- **In-depth Analytics**: Visual insights including retention rates by interval, forecast queues, review volume heatmaps, and difficulty distributions.

---

## Deck Library

Ready-to-import `.edeck` packages live in [`decks/`](./decks/). Pick one, then import it from the **Import** page (upload the file, or paste the file's public direct link), the CLI (`engram import`), or the MCP `import_deck` tool. See [`decks/README.md`](./decks/README.md) for the deck list and the step-by-step instructions.

---

## AI & MCP Integration

Engram exposes a built-in Streamable HTTP MCP server at `/mcp` authenticated by user API keys. Any MCP-compatible client or agent (such as Claude Desktop, Cursor, or Hermes) can interact with your flashcards directly.

### Configuration

Create an API key in the **Settings** panel, then add Engram to your MCP client configuration:

```json
{
  "mcpServers": {
    "engram": {
      "url": "http://localhost:8080/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY"
      }
    }
  }
}
```

### Available Tools

Engram provides 17 dedicated MCP tools:

- `list_decks` / `create_deck` / `update_deck`: Inspect accessible decks, create new ones with custom scheduling presets, or rename and describe them.
- `list_card_types`: List the supported card types with each type's fields and a validated example note, so an agent can write notes without guessing field names or syntax.
- `search_notes` / `get_note` / `list_deck_tags`: Query notes with tag and keyword filters, read a single note, and list the tags used in a deck.
- `create_notes` / `update_note` / `delete_note` / `bulk_notes`: Create, update and delete notes across all supported card types, with dry-run validation, bulk insertion and bulk tag or delete actions.
- `get_due_cards` / `submit_review`: Fetch cards due for review and record reviews. Self-assessed cards take a rating (`Again`, `Hard`, `Good`, `Easy`), and a short-answer card may also carry the answer the learner wrote, stored with the review; answer-type cards (cloze, list, typed, numeric, choice, true/false) take the answer instead, and the server grades it.
- `get_stats`: Retrieve learning summaries, queue counts, and retention rates.
- `export_deck` / `import_deck`: Export and import portable deck packages (`.edeck`).
- `create_import_upload`: Get a single-use upload URL for a deck package. The agent sends the file to it with an HTTP client such as `curl`, so a large package never passes through the model and the API key never leaves the MCP client.

---

## Deployment

### Quick Start (Docker Run)

Uses an embedded SQLite database suitable for personal use or testing:

```bash
docker run -d --name engram -p 8080:8080 \
  -e SESSION_SECRET="${SESSION_SECRET:-$(openssl rand -base64 32)}" \
  -e ENCRYPTION_KEY="${ENCRYPTION_KEY:-$(openssl rand -base64 32)}" \
  -v engram-data:/data \
  docker.io/nite07/engram:latest
```

Open `http://localhost:8080/`. On a fresh instance, navigate to `/setup` to create the initial administrator account.

### Production (Docker Compose)

For multi-user deployments, PostgreSQL is recommended.

Save the following as `docker-compose.yaml` (or use the repository's [docker-compose.yaml](./docker-compose.yaml)):

```yaml
services:
  db:
    image: postgres:18
    restart: unless-stopped
    environment:
      POSTGRES_USER: engram
      POSTGRES_PASSWORD: engram_password
      POSTGRES_DB: engram
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U engram -d engram"]
      interval: 5s
      timeout: 3s
      retries: 20
    volumes:
      - pg-data:/var/lib/postgresql

  engram:
    image: nite07/engram:latest
    restart: unless-stopped
    depends_on:
      db:
        condition: service_healthy
    ports:
      - "8080:8080"
    environment:
      DB_DRIVER: postgres
      DB_DSN: "postgres://engram:engram_password@db:5432/engram?sslmode=disable"
      SESSION_SECRET: "${SESSION_SECRET:?run: openssl rand -base64 32}"
      ENCRYPTION_KEY: "${ENCRYPTION_KEY:?run: openssl rand -base64 32}"
      BASE_URL: "https://engram.example.com"
    volumes:
      - engram-media:/data/media

volumes:
  pg-data:
  engram-media:
```

Start the stack:

```bash
SESSION_SECRET="$(openssl rand -base64 32)" \
ENCRYPTION_KEY="$(openssl rand -base64 32)" \
docker compose up -d
```

### Reverse Proxy & HTTPS

When placing Engram behind a reverse proxy (such as Caddy, Nginx, or Traefik):

1. Set `BASE_URL` to your public URL (e.g., `https://engram.example.com`).
2. Set `TRUSTED_PROXIES` to the address your proxy connects **from**, as Engram sees it (comma-separated IPs or CIDRs). Login rate limiting, audit logs and new-device alerts use the client IP; until this is set, every request appears to come from the proxy.

`TRUSTED_PROXIES` is empty by default, so `X-Forwarded-For` and `X-Real-IP` are ignored. This is deliberate: a header is only as trustworthy as the hop that set it. List the proxies you run, never client networks or `0.0.0.0/0`.

The right value depends on how the proxy reaches Engram:

| Topology | Address Engram sees |
| :--- | :--- |
| Proxy and Engram on the same host, no containers | Loopback: `127.0.0.1/32,::1/128` |
| Engram in a container, port published to the host, proxy on the host | Usually the container network's **gateway**, not `127.0.0.1`: published ports are forwarded through the bridge. Find it with `docker network inspect <network>` (`Gateway`). |
| Proxy and Engram in the same container network | The proxy container's address in that network, or the whole network's subnet |
| CDN or load balancer → proxy → Engram | Every hop that appends to `X-Forwarded-For` must be listed, or the proxy must overwrite the header with the real client IP before forwarding |

To find the address without guessing, start Engram behind your proxy with `TRUSTED_PROXIES` unset and send one request. If the request carried a forwarded header from a loopback or private address that is not trusted, Engram logs one warning, `forwarded client ip header ignored ...`, and its `remote_ip` field is the address to add. At startup Engram also logs which proxies it trusts.

---

## Configuration

Core environment variables required for startup:

| Variable | Description | Example / Default |
| :--- | :--- | :--- |
| `HTTP_ADDR` | Listening address and port | `127.0.0.1:8080` (or `0.0.0.0:8080` in Docker) |
| `BASE_URL` | Public base URL used for links and OIDC callbacks | `https://engram.example.com` |
| `DB_DRIVER` | Database driver (`sqlite` or `postgres`) | `postgres` (or `sqlite`) |
| `DB_DSN` | Database connection string or SQLite file path | `postgres://user:pass@localhost:5432/engram?sslmode=disable` |
| `SESSION_SECRET` | 32-byte Base64 key for session cookies | Generated via `openssl rand -base64 32` |
| `ENCRYPTION_KEY` | 32-byte Base64 key for database encryption | Generated via `openssl rand -base64 32` |
| `AUTO_MIGRATE` | Automatically sync schema on startup (`1` or `0`) | `1` |
| `MEDIA_DIR` | Directory for uploaded media files | `data/media` |

Additional settings (SMTP email, registration policy, OIDC provider, upload quotas) can be configured directly in the **Admin Panel** without restarting the service. See [.env.example](./.env.example) for the complete list of overrides.

---

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for local development setup, build instructions, and testing requirements.

---

## Acknowledgements

Engram builds on these projects:

- [go-fsrs](https://github.com/open-spaced-repetition/go-fsrs) — FSRS v6 scheduling and parameter optimisation.
- [fsrs-rs](https://github.com/open-spaced-repetition/fsrs-rs) — the training implementation behind the optimiser adapter.
- [Gin](https://github.com/gin-gonic/gin) and [GORM](https://gorm.io) — HTTP and database layers.
- [Svelte](https://svelte.dev/) — the single-page front end.
- [goldmark](https://github.com/yuin/goldmark) and [bluemonday](https://github.com/microcosm-cc/bluemonday) — Markdown rendering and HTML allowlisting.
- [modelcontextprotocol/go-sdk](https://github.com/modelcontextprotocol/go-sdk) — the MCP server.
- [zitadel/oidc](https://github.com/zitadel/oidc) and [go-i18n](https://github.com/nicksnyder/go-i18n) — OIDC sign-in and translation catalogs.
- [MathJax](https://www.mathjax.org/) — formula rendering.
- [Tailwind CSS](https://tailwindcss.com/) — styling.

Friend link: [LINUX DO](https://linux.do) — a Chinese-language tech community.


## 文件 AGENTS.md

# AGENTS.md — Development Guide

Read this file before making any change to this repository. It records the rules that are
not obvious from the code and the definition of "done". The task backlog with stable IDs lives in
`ROADMAP.md`.

---

## 1. Source of truth

- The code and its tests are the only statement of behaviour, data model, and scope. Nothing
  outside this repository is authoritative, and there is no separate specification to consult
  before making a change. If code and a document disagree, the code decides; if a comment and
  the code disagree, one of them is a bug — fix the code and report the disagreement.
- Anything the code does not decide must be asked, not invented. A decision that has to outlive
  the change carrying it belongs in a committed file, or the next reader cannot find it.
- **Code comments must be self-contained.** A comment states the rule and its reason in its
  own words. It never cites a document that is not committed, or a bare section number such as
  `§4.5`: a public reader has neither the file nor the numbering, so a citation there is a
  dangling pointer that carries no reason. The rule content stays, the pointer goes. References
  to committed files (`AGENTS.md`, `ROADMAP.md`, `schema/*.json`, RFCs) remain allowed, because
  those resolve for every reader.

---

## 2. Non-negotiable rules

Each rule exists because breaking it is expensive to undo. Follow them literally.

### 2.1 Text language

| Kind of text | Language | Notes |
|---|---|---|
| Logs (`slog` messages and fields, job and subprocess output, CLI diagnostics, `panic` text, internal error strings) | **English** | Never localised, never taken from a translation catalog. |
| Code comments (package/function docs and inline explanations) | **Chinese** | Explain *why*, not *what*. |
| User-facing text (UI labels, form validation, API/MCP `message`) | **Translation catalog** (`zh-CN`, `en`) | Never hardcode. |
| Identifiers (log messages, catalog keys, error `code` values) | **English** | Keeps catalogs and logs searchable and avoids mixed-language keys. |

Decision rule: machine and developer facing → English; reader of the source → Chinese;
end user → translation catalog.

### 2.2 Repository sanitisation (open-source repo)

- No real domain names, host names, private IP ranges, personal email addresses, tokens,
  passwords, or descriptions of private infrastructure in **any** committed file —
  including examples, fixtures, comments, and documentation.
- Use placeholders: `example.com`, `localhost`, `CHANGE_ME`.
- The Go module path is the one deliberate exception: it is the project's publication
  address rather than private infrastructure, so it carries the real code-host domain in
  `go.mod`, in imports, and in any documented `go get` command. Every other real domain
  stays out of the repository (see `.gitignore`). Run `git status` before every commit and
  check nothing unintended is staged.
- **This rule has no automated check any more** (the check scripts were removed on
  2026-10-06, and the source-text test guards on 2026-10-08): review it by eye on every
  commit and re-read the staged diff before merging. A subagent's "the checks pass" is not
  evidence on its own — nothing automated covers this rule.
- A test fixture needs a placeholder domain too: emails in fixtures must use `example.com`,
  `example.org`, `example.net`, or `localhost`.

### 2.3 Domain invariants (do not break these)

1. **Content and progress are separate.** `notes`/`cards` hold content only; per-user
   scheduling lives in `card_states`, keyed `(card_id, user_id)`. Sharing a deck must
   never mix two users' progress.
2. **`reviews` is append-only, with one exception: undoing a review.** Every column of
   the review log is written from the first commit — it is the only fuel for parameter
   optimisation and cannot be reconstructed later. The single permitted deletion is the row
   that a review-undo removes: undo is the user saying "that rating was a mistake", so the
   row must not be fed to the optimiser. The undo writes an audit row (`review.undo`)
   recording the removed review, so the fact and its details survive the deletion.
3. **Ratings and states are integers**: `rating` 1–4 (Again/Hard/Good/Easy),
   `state_before` 0–3 (New/Learning/Review/Relearning). This matches the FSRS ecosystem
   log format and keeps optimiser export trivial.
4. **Both databases must work**: PostgreSQL (default deployment) and SQLite (single-node
   and development). No PG-only types (`jsonb`, `serial`, `array`), JSON stored as `TEXT`,
   `clause.OnConflict` for upserts, `LIMIT/OFFSET` for paging.
5. **AutoMigrate is additive only.** Column type changes, drops, and new non-null
   constraints require an explicit, versioned migration function.
6. **One business layer, two transports.** REST handlers and MCP tools call the same
   service methods. Never duplicate validation or scheduling logic per transport.
7. **Card types are registered, not hardcoded.** Adding a type means adding one file and
   registering it; core code must not change.
8. **Review submission is idempotent.** Enforce the `expected_version` check and return
   `409` on mismatch; write the state update and the review row in one transaction.
9. **A boolean column with a database default must be a pointer in the model.** GORM omits
   a zero-valued field when the column carries a `default` tag, so the database default
   silently overwrites an explicit `false` (measured on `presets.enable_fuzz`). Use `*bool`
   for such columns; never work around it at the call site more than once.

### 2.4 Go style in this repo

- Plain monolith, organised by business package; concrete types over interfaces;
  dependencies wired explicitly in `cmd/engram`.
- **One model serves business, GORM, and JSON/CSV.** No entity/DTO mapping layers.
- Introduce an interface only when there are multiple implementations or a concrete
  replacement need; define the minimal interface **at the consumer**.
- Concrete `Store` types wrap GORM access. Add a `Service` only for genuinely complex
  flows.
- Blocking operations take `context.Context` as the first parameter.
- Errors: wrap with `%w`; API/MCP errors carry a stable English `code` plus a localised
  `message`.
- No new dependency without a reason that survives the selection principle (low complexity,
  prefer mature libraries over invented ones).

### 2.5 Tests and commits

- Table-driven tests; use a real SQLite database (in-memory or temp file) — do not mock
  the database. Core coverage targets: `internal/schedule` and `internal/cardtype`.
- **The default test database is SQLite, locally and in CI.** Neither runs a database
  service: `go test ./...` without `TEST_PG_DSN` makes the PostgreSQL cases gated by
  `internal/pgtest` skip themselves. Set `TEST_PG_DSN` to run them, and do that by hand
  whenever you touch driver-sensitive code (transactions, `clause.OnConflict` upserts,
  concurrency on `card_states`).
- Handler tests use `httptest`. Negative cases are required, not optional: permission
  denials, CSRF failures, expired keys, scope violations.
- Commits are signed (`user.signingkey` is set per repository), use Conventional Commits
  prefixes (`feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`), and are written in
  **English** — subject and body.
- One logical change per commit; message body explains why, not what.

### 2.6 Writing requirements in this repository

Every written requirement, instruction, or document line must have exactly **one**
possible reading. After writing, re-read each line; if a second reading is possible,
split it into explicit statements. This applies to code comments, task descriptions in
this file, and commit messages.

---

## 3. Layout

```
engram/
├── AGENTS.md                 # this file: the rules
├── ROADMAP.md                # the task backlog and progress conventions
├── README.md / README.zh.md  # English is the primary document; Chinese is parallel
├── LICENSE
├── go.mod                    # module git.nite07.com/nite/engram
├── cmd/engram/main.go     # subcommand entry point
├── internal/
│   ├── config/               # env vars + settings-table overlay and precedence
│   ├── store/                # GORM models and business stores
│   ├── schedule/             # go-fsrs wrapper: state machine, queue, review submit
│   ├── cardtype/             # card type registry and type implementations
│   ├── auth/                 # local accounts, sessions, CSRF, OIDC, API keys, roles
│   ├── media/                # local file storage: dedupe, write, proxy read
│   ├── api/                  # /api/v1 handlers
│   ├── mcp/                  # MCP server: tool definitions that call the services
│   ├── i18n/                 # locales/{zh-CN,en}.yaml plus loader and translator
│   └── web/                  # gin routes, JSON handlers, SPA shell serving, static assets
```

There is no top-level `test/` directory: integration coverage lives beside the code as
`internal/<package>/*_test.go`, using `httptest` for handlers and a real SQLite database (file
or in-memory) for storage.

---

## 4. Build and verify

```bash
# full-module check — the parent's merge gate only, never a per-task step
go build ./... && go vet ./... && gofmt -l . && go test ./...

# the embedded frontend build output is gitignored, so build it before the Go build
npm --prefix frontend ci
npm --prefix frontend run build

# run locally (SQLite is fine for development)
DB_DRIVER=sqlite DB_DSN=data/engram.db AUTO_MIGRATE=1 go run ./cmd/engram serve
```

Run the frontend build **before** the code checks whenever the change touches `frontend/`:
`go build ./...` embeds `frontend/dist`, which is gitignored, so a stale build is invisible in
`git status`.

### Scoped test runs

Verify a change with the packages it touches, not the whole module:

```bash
go test ./internal/schedule/... && go vet ./internal/schedule/...
```

`go build ./...` and `go test ./...` compile and test every package in the module. Parallel
writers share one machine, so each full run adds another complete compile and test pass to
the same CPU and memory; concurrent full runs compete for both and can exhaust memory. The
full-module command is the parent's merge gate, run once per integration, not once per task.

Never build the executable (`go build ./cmd/engram`, `go build -o ...`) to verify a change:
`go test` compiles the packages it needs and `go vet` type-checks them. Building the binary
is a release step, not a verification step.

### Definition of done

A task is done only when all of the following hold:

1. The acceptance criteria written next to the task in `ROADMAP.md` pass, and the evidence
   is a command output or a captured response — not a claim.
2. The packages the change touches pass `go vet` and `go test` (see "Scoped test runs"); the
   parent runs the full-module `go build ./... && go vet ./... && gofmt -l . && go test ./...`
   once at the merge gate.
3. New behaviour has tests, including the negative cases named in the task.
4. Logs are English, comments are Chinese, user-facing strings come from the catalog.
5. The change is committed with a signed, conventional commit; `git status` is clean.
6. If the change alters behaviour or decisions, report it in your final message: the
   maintainer decides which committed file records it.
7. No comment, document or commit message cites a file that is not in the repository.
   Every reference resolves for a public reader: `AGENTS.md`, `ROADMAP.md`, `README*`,
   `schema/*.json`, RFCs, or code paths inside the repository.

---

## 5. Dispatching tasks to subagents

- **Subagents must never edit `AGENTS.md` or `ROADMAP.md`** (or any project-context file such as
  `CLAUDE.md` or `.hermes.md`). Writing them requires user approval, which a leaf subagent cannot obtain: the
  attempt is auto-denied or it interrupts the user mid-workflow. The parent records verified
  progress in the gitignored `PROGRESS.local.md` and deletes the finished entries from
  `ROADMAP.md` in batches, with the user present.


- One task per subagent. Pass the task's ID, its full text from `ROADMAP.md`, and the code
  paths it touches as context; subagents do not share this conversation.
- Require the subagent to run the section 4 checks **scoped to the packages its change
  touches** and to report the raw output, not a summary claim. The parent runs the
  full-module checks once, after merging, so that N parallel writers do not each trigger a
  full build and test pass.
- The parent verifies the reported evidence before deleting the entry from `ROADMAP.md`; a
  subagent's self-report is not proof.
- A subagent that discovers missing design information must report it instead of inventing
  behaviour; the parent then records the decision in the committed file that owns it, or
  reports it for the maintainer to place.
- Keep one commit per task so progress can be audited with `git log`.

## 6. Parallel development with git worktrees

A branch alone isolates nothing: `HEAD`, the index, and the working tree are single per
checkout, so two writers in one directory will overwrite each other. Every parallel writer
therefore gets its own worktree. The rules below were verified on git 2.55.

**Layout and naming**

- The main checkout stays on `main` and is used only as the integration point. Do not
  develop in it.
- Worktrees live **outside** the repository directory, for example
  `../engram-wt/<task-id>`, so the main checkout's `git status` stays clean.
- Branch: `feat/<task-id>-<slug>` (for example `feat/m3-2-queue-builder`).
  Directory: `engram-wt/<task-id>`. Both use the task IDs from `ROADMAP.md`.

```bash
git worktree add -b feat/m3-2 ../engram-wt/m3-2 main
# ... work and commit inside ../engram-wt/m3-2 ...
git worktree remove ../engram-wt/m3-2   # or keep the worktree for review
git worktree prune                         # drop stale entries
```

**Working rules**

- One task = one worktree = one commit. The subagent works inside its worktree; the parent
  performs the merge serially (rebase onto `main`, run the section 4 checks, then merge).
  A subagent never merges or pushes.
- Concurrency budget: at most three writers at once, and only when the two tasks touch
  **disjoint file sets**. Parallelism is decided by file overlap, nothing else.
- Single-writer hotspots — one writer at a time, other tasks wait for the next phase:
  `internal/store/models.go`, `internal/config/`, `internal/i18n/locales/`,
  `frontend/src/lib/views/`.
- The locale catalogs are the one hotspot that can be shared, under a strict convention: each
  writer **appends its own block at the end of the file**, using a prefix it owns (`stats.`,
  `admin.audit.`), and never reorders or reformats an existing line. Measured over three rounds:
  three lanes appending in parallel merged with no conflict at all, while the same files conflict
  the moment two blocks land at the same position. Every dispatch that touches the catalogs must
  state this convention, and the writer must keep the two catalogs' key sets identical.
- Add a new route to `adminRoutes()` in the same change that registers it. That list is what the
  "non-admin gets 403 on every /admin route" test walks, so a route missing from it is a route
  that is never checked.
- Generated artifacts are per worktree: run `npm --prefix frontend run build` inside each
  worktree. The Go module cache and build cache are shared and safe for concurrent use. Never
  run repository maintenance commands (`git gc`, `git prune`, `git repack`) from a worktree.
- Subagents are session-scoped and are killed when the session ends. Require an early
  commit, even a work-in-progress one, so the work lands in the shared object database
  instead of an orphaned directory.

**Pitfalls (each reproduced on git 2.55)**

1. A branch can be checked out in only one worktree at a time, and `--force` does not
   override this. This is what enforces one task per branch, and it also means two writers
   can never share a branch.
2. Deleting a worktree directory does not remove the worktree. Until `git worktree prune`
   runs, the entry stays listed as `prunable` and the branch still counts as checked out,
   which blocks creating another worktree for that branch.
3. Hooks and scripts exist in a worktree only if they are committed. An untracked
   `.githooks/` does not run and produces no error, so commits can silently lose their
   signature.
4. Repository configuration is shared from the main repository: `user.signingkey` and
   `core.hooksPath` are visible inside every worktree, so signing needs no per-worktree
   setup.

**When to use separate clones instead**

Use `git clone --local` only when a writer needs its own `.git/config`, its own ignore
rules, or the freedom to run `git clean -xdf`. That is not the case in this repository;
worktrees are the default.

**Phase plan — which milestones may run in parallel**

| Phase | Lanes | Constraint |
|---|---|---|
| A | M0 alone | Everything depends on it; run it serially |
| B | M1 (auth) ∥ M2 (store, cardtype, web) | Disjoint packages |
| C | M3 (schedule) ∥ M4 (api, mcp) | Freeze the shared store models; neither lane may change them |
| D | M5 (grants) ∥ M7 (statistics) | Disjoint packages |
| E | M6 (admin views) **or** M8 (mobile, i18n) | Both rewrite `frontend/src/lib/views/`; run them in sequence. If they must overlap, split M8 into "gestures and JS" and "view text", and keep the view-text half exclusive with M6 |
| F | M9 last | Needs real review data produced by M3 |

