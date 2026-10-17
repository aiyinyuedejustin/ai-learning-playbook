# ankimcp/anki-mcp-server

- 链接：https://github.com/ankimcp/anki-mcp-server
- 作者：ankimcp
- 仓库说明：A Model Context Protocol (MCP) server that enables AI assistants to interact with Anki, the spaced repetition flashcard application.
- 星数：516
- 获取方式：GitHub README + SKILL/说明文件

---

## README

# Anki MCP Server

[![Tests](https://github.com/ankimcp/anki-mcp-server/actions/workflows/test.yml/badge.svg)](https://github.com/ankimcp/anki-mcp-server/actions/workflows/test.yml)
[![npm version](https://badge.fury.io/js/@ankimcp%2Fanki-mcp-server.svg)](https://www.npmjs.com/package/@ankimcp/anki-mcp-server)

<div align="center">
  <img src="./docs/images/ankimcp.png" alt="Anki + MCP Integration" width="600" />

  <p><strong>Seamlessly integrate <a href="https://apps.ankiweb.net">Anki</a> with AI assistants through the <a href="https://modelcontextprotocol.io">Model Context Protocol</a></strong></p>
</div>

> [!IMPORTANT]
> **Prefer the [AnkiMCP addon](https://ankiweb.net/shared/info/124672614) for most setups.**
>
> The addon ([GitHub](https://github.com/ankimcp/anki-mcp-server-addon)) runs the MCP server directly inside Anki. There is no Node.js to install, no AnkiConnect to configure, no separate process to keep running: install it with code `124672614`, restart Anki, and the server is up every time Anki opens. It covers local HTTP access and remote access through a built-in tunnel.
>
> This repository is the right choice when you specifically need:
>
> - **STDIO transport** — Claude Desktop, Claude Code, Cursor, or any client that spawns the server as a subprocess
> - **MCPB bundle** — the one-click `.mcpb` install for Claude Desktop
>
> For HTTP, tunnel, or web-based clients (claude.ai, ChatGPT), the addon is the simpler and better-supported path.
>
> This repo is **not** being deprecated. It stays maintained and released alongside the addon as part of the same [ankimcp.ai](https://ankimcp.ai) project.

A Model Context Protocol (MCP) server that enables AI assistants to interact with Anki, the spaced repetition flashcard application.

Transform your Anki experience with natural language interaction - like having a private tutor. The AI assistant doesn't just present questions and answers; it can explain concepts, make the learning process more engaging and human-like, provide context, and adapt to your learning style. It can create and edit notes on the fly, turning your study sessions into dynamic conversations. More features coming soon!

## Examples and Tutorials

For comprehensive guides, real-world examples, and step-by-step tutorials on using this MCP server with Claude Desktop, visit:

**[ankimcp.ai](https://ankimcp.ai)** - Complete documentation with practical examples and use cases

See [`docs/`](./docs/README.md) for supplementary documentation, including the [reviewer setup guide](./docs/reviewer-setup.md) and the sample Anki deck.

## Example Use Cases

Three representative prompts showing the tool flows this server enables:

1. **"Help me review my Spanish deck."** — The assistant offers to sync with AnkiWeb (`sync`), fetches due cards (`get_due_cards` with deck filter), presents each card (`present_card`), and records your rating (`rate_card`). Natural study conversation with explanations tailored to you.

2. **"Create 10 Arabic vocab cards with RTL styling."** — The assistant lists note types (`modelNames`), creates a custom RTL model if needed (`createModel` + `updateModelStyling` for right-to-left CSS), then batch-creates the cards (`addNotes`).

3. **"Import this image from my Downloads folder into the front of the selected note."** — The assistant uploads the local file (`storeMediaFile` with a file path), reads the currently-selected note from the browser (`guiSelectedNotes` + `notesInfo`), and updates the front field with an `<img>` tag (`updateNoteFields`).

## Available Tools

The server exposes **53 MCP tools** — 42 essential tools for everyday Anki operations and 11 GUI tools that drive the Anki desktop interface for note editing/creation workflows.

### Essential Tools

#### Review & Study
- `sync` - Sync with AnkiWeb to pull latest data and push changes
- `get_due_cards` - Get cards that are due for review, optionally filtered by deck (answers omitted unless `include_answer: true`, default `false`)
- `get_cards` - Get cards with flexible filtering by state (due, new, learning, suspended, buried) and deck (answers omitted unless `include_answer: true`, default `false`)
- `present_card` - Show a card for review with its question/front side
- `rate_card` - Rate card performance (Again, Hard, Good, Easy) and schedule the next review
- `forgetCards` - Reset cards to new, discarding their scheduling without recording a review
- `setDueDate` - Reschedule cards to become due in N days (`"0"`, `"3-7"`, `"1!"`), without recording a review
- `areSuspended` - Check suspension state for one or more cards without changing anything
- `suspend` - Suspend cards so they are skipped during review until unsuspended
- `unsuspend` - Unsuspend cards so they return to normal review

> **Note:** `forgetCards` and `setDueDate` change scheduling *without* logging a review, which is what separates them from `rate_card`. Reach for them when a card's schedule is wrong rather than the answer: rating a card `Again` to bury it deeper records a real lapse and drops its ease factor, permanently skewing both future scheduling and your statistics. `forgetCards` wipes the interval and starts the card over; `setDueDate` keeps the card's history and just moves the next review.

> **Note:** Card `front`/`back` content is rendered per card from its own template (as Anki shows it), so reversed and cloze cards display the correct direction. Static text added by your card templates appears in the output as well.

#### Deck Management
- `listDecks` - List all decks, optionally with per-deck study-queue statistics
- `deckStats` - Get comprehensive statistics for a single deck (study queue, true card-state counts, ease/interval distributions)
- `createDeck` - Create a new empty deck (supports `Parent::Child`, max 2 levels)
- `changeDeck` - Move cards to a different deck (created if it doesn't exist)

> **Note:** Deck statistics come in two flavours. The `counts` block (and everything `listDecks` reports) mirrors Anki's deck browser: cards **due today**, capped by each deck's **daily new/review limits**, with suspended and buried cards excluded — so `review` is not "mature cards" and the `other` bucket is just the arithmetic remainder (mostly review cards not due today plus new cards over the daily limit). For true per-state totals use the `states` block on `deckStats` / `collection_stats`, which counts `new`, `learning`, `review`, `suspended` and `buried` via Anki searches, ignoring due dates and daily limits.

#### Note Management
- `addNote` - Create a single note with specified fields and tags
- `addNotes` - Batch-create up to 100 notes sharing a deck and model (partial success supported)
- `findNotes` - Search for notes using Anki query syntax (`deck:`, `tag:`, `is:due`, etc.)
- `notesInfo` - Get detailed information about notes (fields, tags, note type, card IDs; CSS comes from `modelStyling`)
- `updateNoteFields` - Update existing note fields (CSS-aware, supports HTML content)
- `deleteNotes` - Delete notes and all associated cards (destructive, requires confirmation)

#### Tag Management
- `getTags` - Get all tags in the collection (use first to avoid duplication)
- `addTags` - Add space-separated tags to specified notes
- `removeTags` - Remove space-separated tags from specified notes
- `replaceTags` - Rename a tag across specified notes
- `clearUnusedTags` - Remove orphaned tags not used by any notes (destructive)

#### Media Management
- `getMediaFilesNames` - List media files in `collection.media`, optionally filtered by pattern
- `retrieveMediaFile` - Download a media file as base64 content
- `storeMediaFile` - Upload media from base64 data, an absolute file path, or a URL
- `deleteMediaFile` - Remove a media file from `collection.media` (destructive)

**💡 Best Practice for Images:**
- ✅ **Use file paths** (e.g., `/Users/you/image.png`) - Fast and efficient
- ✅ **Use URLs** (e.g., `https://example.com/image.jpg`) - Direct download
- ❌ **Avoid base64** - Extremely slow and token-inefficient

Just tell Claude where the image is, and it will handle the upload automatically using the most efficient method.

#### Model/Template Management
- `modelNames` - List all available note types/models
- `modelFieldNames` - Get field names for a specific note type
- `modelStyling` - Get CSS styling information for a note type
- `modelTemplates` - Get the card templates (Front and Back HTML) for a note type
- `createModel` - Create a new note type with custom fields, card templates, and CSS (e.g., RTL models)
- `updateModelStyling` - Update the CSS styling for an existing note type (applies to all its cards)
- `updateModelTemplates` - Update the card templates (Front and Back HTML) for an existing note type (applies to all its cards)
- `addModelField` - Add a new field to an existing note type (appended at the end or inserted at a specific position)
- `removeModelField` - Remove a field from an existing note type (deletes its content from all notes; requires explicit confirmation)
- `renameModelField` - Rename a field in an existing note type (Anki rewrites references to the old name in the card templates)
- `repositionModelField` - Change the position of a field within an existing note type

#### Statistics
- `collection_stats` - Aggregated statistics across all decks with per-deck breakdown and collection-wide card-state counts
- `review_stats` - Review history analysis (temporal patterns, retention metrics, study streaks)

### GUI Tools

Tools that drive the Anki desktop interface. Intended for note editing/creation and deck-management workflows, **not** for review sessions.

- `guiBrowse` - Open the Card Browser and search for cards
- `guiSelectCard` - Select a specific card in the Card Browser
- `guiSelectedNotes` - Get IDs of notes currently selected in the Card Browser
- `guiAddCards` - Open the Add Cards dialog with preset note details
- `guiEditNote` - Open the note editor for a specific note
- `guiDeckOverview` - Open the Deck Overview dialog for a specific deck
- `guiDeckBrowser` - Open the Deck Browser dialog
- `guiCurrentCard` - Get info about the current card in review mode (includes the answer; errors outside review mode)
- `guiShowQuestion` - Show the question side of the current card
- `guiShowAnswer` - Show the answer side of the current card
- `guiUndo` - Undo the last action in Anki

## Prerequisites

- [Anki](https://apps.ankiweb.net/) with [AnkiConnect](https://github.com/FooSoft/anki-connect) plugin installed
- Node.js 22.12.0+

## Installation

There are a few ways to get the server onto your machine. Once it's installed, head to [Connecting an AI Client](#connecting-an-ai-client) to wire it up to your AI assistant — locally or remotely.

### npm (global or npx)

The general-purpose way to install the server, suitable for any MCP client that launches it directly.

Install it globally for clients that run the `ankimcp` command:

```bash
npm install -g @ankimcp/anki-mcp-server
```

Or run it on demand with no install required:

```bash
npx @ankimcp/anki-mcp-server
```

### MCPB Bundle (Recommended for Claude Desktop)

The easiest way to install this MCP server for Claude Desktop:

1. Download the latest `.mcpb` bundle from the [Releases](https://github.com/ankimcp/anki-mcp-server/releases) page
2. In Claude Desktop, install the extension:
    - **Method 1**: Go to Settings → Extensions, then drag and drop the `.mcpb` file
    - **Method 2**: Go to Settings → Developer → Extensions → Install Extension, then select the `.mcpb` file
3. Configure AnkiConnect URL if needed (defaults to `http://localhost:8765`)
4. Restart Claude Desktop

That's it! The bundle includes everything needed to run the server locally.

> **For Anthropic MCP Directory reviewers:** a zero-to-integration walkthrough with a pre-populated sample deck lives in [`docs/reviewer-setup.md`](./docs/reviewer-setup.md).

### Install from Source (for development)

For development or advanced usage (running the test suite requires Node.js 24.9+ — the npm test scripts load the ESM-only NestJS 12 packages via `require(esm)`, which Jest only supports there; the runtime requirement for *using* the server stays 22.12.0+):

```bash
npm install
npm run build
```

## Connecting an AI Client

There are two ways an AI assistant can reach this server, depending on where the assistant runs:

- **[Local](#local)** — the server runs on the same machine as the AI client (Claude Desktop, Cursor, Cline, Zed, or a local browser session). Use **STDIO** for desktop MCP clients, **HTTP** for local web-based tools.
- **[Remote](#remote)** — a hosted/remote AI (e.g. ChatGPT or Claude.ai in the cloud) needs to reach the Anki running on your local machine. Use the managed **Tunnel** (✅ recommended — authenticated) or, as a lighter-weight unauthenticated alternative, **ngrok**.

### Local

The server runs on the same computer as your AI client and talks to AnkiConnect on `localhost`.

#### STDIO (primary local integration)

STDIO is the standard transport for local desktop MCP clients — **Claude Desktop**, **Cursor IDE**, **Cline**, **Zed Editor**, **opencode**, and others. The client launches the server as a subprocess and communicates over standard input/output.

**Supported Clients:**
- [Claude Desktop](https://claude.ai/download)
- [Cursor IDE](https://www.cursor.com/) - AI-powered code editor
- [Cline](https://github.com/cline/cline) - VS Code extension for AI assistance
- [Zed Editor](https://zed.dev/) - Fast, modern code editor
- [opencode](https://opencode.ai) - Terminal AI coding agent
- Other MCP clients that support STDIO transport

For Claude Desktop, the [MCPB bundle](#mcpb-bundle-recommended-for-claude-desktop) is the easiest path. For other clients, configure the npm package with the `--stdio` flag.

**Configuration - Choose one method:**

**Method 1: Using npx (recommended - no installation needed)**

```json
{
  "mcpServers": {
    "anki-mcp": {
      "command": "npx",
      "args": ["-y", "@ankimcp/anki-mcp-server", "--stdio"],
      "env": {
        "ANKI_CONNECT_URL": "http://localhost:8765"
      }
    }
  }
}
```

**Method 2: Using global installation**

First, install globally:
```bash
npm install -g @ankimcp/anki-mcp-server
```

Then configure:
```json
{
  "mcpServers": {
    "anki-mcp": {
      "command": "ankimcp",
      "args": ["--stdio"],
      "env": {
        "ANKI_CONNECT_URL": "http://localhost:8765"
      }
    }
  }
}
```

**opencode** uses its own format — servers go under `mcp`, the command is a single array, and environment variables go under `environment`:
```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "anki-mcp": {
      "type": "local",
      "command": ["npx", "-y", "@ankimcp/anki-mcp-server", "--stdio"],
      "enabled": true,
      "environment": {
        "ANKI_CONNECT_URL": "http://localhost:8765"
      }
    }
  }
}
```

**Configuration file locations:**
- **Cursor IDE**: `~/.cursor/mcp.json` (macOS/Linux) or `%USERPROFILE%\.cursor\mcp.json` (Windows)
- **Cline**: Accessible via settings UI in VS Code
- **Zed Editor**: Install as MCP extension through extension marketplace
- **opencode**: `opencode.json` in your project root, or `~/.config/opencode/opencode.json` globally

For client-specific features and troubleshooting, consult your MCP client's documentation. See also [Connect to Claude Desktop](#connect-to-claude-desktop-local-mode) for a config that points directly at a built `dist/main-stdio.js`.

#### HTTP (local web-based AI)

HTTP mode runs the server as a local web server speaking the MCP Streamable HTTP protocol. It's the transport a web-based AI tool talks to when pointed at your machine, and it's also what the [Remote](#remote) options expose to the outside world. On its own, HTTP mode binds to `localhost` only.

> **Binding beyond localhost?** If you pass `--host 0.0.0.0` (or run behind a reverse proxy/public domain), the server only accepts loopback `Host` headers by default for DNS-rebinding protection — set `ALLOWED_HOSTS` to the hostname(s) clients use. See [HTTP Mode Configuration](#http-mode-configuration).

**Setup - Choose one method:**

**Method 1: Using npx (recommended - no installation needed)**

```bash
# Quick start
npx @ankimcp/anki-mcp-server

# With custom options
npx @ankimcp/anki-mcp-server --port 8080 --host 0.0.0.0
npx @ankimcp/anki-mcp-server --anki-connect http://localhost:8765
```

**Method 2: Using global installation**

```bash
# Install once
npm install -g @ankimcp/anki-mcp-server

# Run the server
ankimcp

# With custom options
ankimcp --port 8080 --host 0.0.0.0
ankimcp --anki-connect http://localhost:8765
```

**Method 3: Install from source (for development)**

```bash
npm install
npm run build
npm run start:prod:http
```

To make a local HTTP server reachable by a cloud-hosted AI, use one of the [Remote](#remote) options below.

### Remote

A hosted/remote AI (such as ChatGPT or Claude.ai running in the cloud) can't reach `localhost` directly. These options expose your **local** Anki to the internet so a remote assistant can talk to it.

#### Tunnel (✅ Recommended)

> **Recommended remote path — authenticated & secure.** Unlike a raw public port, tunnel mode requires you to log in (OAuth 2.0 device flow), so the endpoint isn't open to anyone who guesses the URL.

Tunnel mode lets web-based AI assistants reach your **local** Anki without running your own tunnel. The server connects out to the managed AnkiMCP tunnel service (`wss://tunnel.ankimcp.ai`) over a WebSocket and is assigned a public URL. Authentication is built in — no ngrok account or separate tunnel process required, and you log in once.

**Log in (OAuth device flow):**

Tunnel mode uses the OAuth 2.0 Device Authorization Grant. Logging in opens your browser automatically to an approval page with the code already embedded in the URL — nothing to type, just approve. (If the browser can't open, the terminal prints a verification URL and code to enter manually as a fallback.) On success, credentials are saved to `~/.ankimcp/credentials.json` (file permissions `0600`).

```bash
# Pre-authenticate (optional — --tunnel will trigger this automatically if needed)
ankimcp --login
npx @ankimcp/anki-mcp-server --login

# Clear saved credentials
ankimcp --logout
```

**Start the tunnel:**

```bash
# Connect to the managed tunnel service (wss://tunnel.ankimcp.ai)
ankimcp --tunnel
npx @ankimcp/anki-mcp-server --tunnel

# Override the tunnel server URL (must be ws:// or wss://) — e.g. for self-hosting
ankimcp --tunnel wss://my-tunnel.example.com
```

If no credentials exist, `--tunnel` automatically starts the login flow first, then continues to the tunnel. This auto-login requires an interactive terminal — when stdout is not a TTY (systemd, headless Docker, CI), the server fast-fails and asks you to run `ankimcp --login` first. Once connected, the public tunnel URL is printed; press Ctrl+C to disconnect. Share that URL with your AI assistant.

**Tunnel-mode environment variables:**

| Variable | Description | Default |
|----------|-------------|---------|
| `TUNNEL_SERVER_URL` | Tunnel server WebSocket URL (the `--tunnel`/`--login` flag value overrides this) | `wss://tunnel.ankimcp.ai` |
| `TUNNEL_AUTH_CLIENT_ID` | OAuth client ID for the device flow. Advanced — only needed when pointing at a self-hosted tunnel/auth service. | (built-in) |

The device-flow auth endpoints (`/auth/device`, `/auth/token`) are derived from `TUNNEL_SERVER_URL`, so pointing `--tunnel` (or `TUNNEL_SERVER_URL`) at a different host also moves authentication to that host.

**How it works:** Tunnel mode runs the MCP server in-process behind an in-memory transport (`TunnelTransport`). That transport owns the MCP server and turns each relayed request body into a response, and `TunnelClient` bridges it to the remote tunnel service over a WebSocket — relaying MCP requests in and responses out. AnkiConnect is still only ever reached on your local machine.

**Protocol revisions:** Because the tunnel connects the MCP server in-process, tunnel mode serves the 2025 revision of the MCP protocol only, while STDIO and HTTP modes serve both 2025 and the newer 2026-07-28 revision. Every tool behaves the same either way — but a client that speaks only 2026-07-28 is turned away over the tunnel with a protocol-version error; run [STDIO](#stdio-primary-local-integration) or [HTTP](#http-local-web-based-ai) mode for that client.

#### ngrok (unauthenticated alternative)

If you'd rather expose [local HTTP mode](#http-local-web-based-ai) publicly without an account on the managed tunnel, the built-in `--ngrok` flag launches an [ngrok](https://ngrok.com/) subprocess (`src/services/ngrok.service.ts`) and prints the public URL in the startup banner:

```bash
# One-time ngrok setup, then:
ankimcp --ngrok
```

This route is **unauthenticated** — anyone with the URL can reach your Anki, so it's less secure than [Tunnel](#tunnel--recommended). Prefer Tunnel unless you have a specific reason to manage your own ngrok endpoint. (Requires a global ngrok install and authtoken.)

The `--ngrok` flag launches ngrok with `--host-header=rewrite`, so ngrok rewrites the upstream `Host` to `localhost` before forwarding. That keeps requests within the loopback Host allowlist (see [DNS-rebinding protection](#http-mode-configuration)) without you having to add the public `*.ngrok` domain to `ALLOWED_HOSTS`. If you instead run ngrok manually, use the same flag — `ngrok http --host-header=rewrite 3000` — otherwise ngrok forwards the public ngrok hostname as `Host` and the server rejects it with `403`.

### CLI Options (all modes)

```bash
ankimcp [options]

Options:
  --stdio                        Run in STDIO mode (for MCP clients)
  --tunnel [url]                 Connect via the managed tunnel (authenticated)
  --login                        Authenticate for tunnel mode (OAuth device flow)
  --logout                       Clear saved tunnel credentials
  -p, --port <number>            Port to listen on (HTTP mode; default: 3000, or PORT env var)
  -h, --host <address>           Host to bind to (HTTP mode; default: 127.0.0.1, or HOST env var)
  -a, --anki-connect <url>       AnkiConnect URL (default: http://localhost:8765, or ANKI_CONNECT_URL env var)
  --ngrok                        Start ngrok tunnel (requires global ngrok installation)
  --read-only                    Run in read-only mode (blocks content changes and rescheduling; rating, suspend and sync still work)
  --help                         Show help message

Usage with npx (no installation needed):
  npx @ankimcp/anki-mcp-server                        # HTTP mode
  npx @ankimcp/anki-mcp-server --port 8080            # Custom port
  npx @ankimcp/anki-mcp-server --stdio                # STDIO mode
  npx @ankimcp/anki-mcp-server --tunnel               # Managed tunnel mode
  npx @ankimcp/anki-mcp-server --ngrok                # HTTP mode with ngrok tunnel
  npx @ankimcp/anki-mcp-server --read-only            # Read-only mode

Usage with global installation:
  npm install -g @ankimcp/anki-mcp-server             # Install once
  ankimcp                                             # HTTP mode
  ankimcp --port 8080                                 # Custom port
  ankimcp --stdio                                     # STDIO mode
  ankimcp --tunnel                                    # Managed tunnel mode
  ankimcp --ngrok                                     # HTTP mode with ngrok tunnel
  ankimcp --read-only                                 # Read-only mode
```

### Read-Only Mode (all modes)

The `--read-only` flag (or `READ_ONLY=true`) blocks changes to note content, decks, tags, media and note types, and manual rescheduling of cards. When enabled:
- All read operations work normally (browsing decks, viewing cards, searching notes)
- These changes are still allowed: rating a card during review (`rate_card`), suspending/unsuspending cards (`suspend`, `unsuspend`), syncing with AnkiWeb (`sync`), and the GUI tools that navigate Anki's windows (`guiBrowse`, `guiDeckOverview`, …)
- Content modifications are blocked (addNote, deleteNotes, createDeck, updateNoteFields, etc.); `createDeck` for a deck that already exists still succeeds, since nothing is written
- Manual rescheduling is blocked: `forgetCards` (reset to new) and `setDueDate`
- `guiUndo` is blocked, since an undo can revert a change to the collection
- `guiAddCards` and `guiEditNote` are blocked, since a note added or saved in the dialog they open is written to the collection
- Useful for exploring Anki data without accidental changes to its content

```bash
# HTTP mode with read-only
ankimcp --read-only

# STDIO mode with read-only
ankimcp --stdio --read-only

# Can combine with other flags
ankimcp --ngrok --read-only
```

You can also enable read-only mode via environment variable:
```bash
READ_ONLY=true ankimcp
```

Or in MCP client configuration:
```json
{
  "mcpServers": {
    "anki-mcp": {
      "command": "npx",
      "args": ["-y", "@ankimcp/anki-mcp-server", "--stdio", "--read-only"],
      "env": {
        "ANKI_CONNECT_URL": "http://localhost:8765"
      }
    }
  }
}
```

## Connect to Claude Desktop (Local Mode)

You can configure the server in Claude Desktop by either:
- Going to: Settings → Developer → Edit Config
- Or manually editing the config file

### Configuration

Add the following to your Claude Desktop config:

```json
{
  "mcpServers": {
    "anki-mcp": {
      "command": "node",
      "args": ["/path/to/anki-mcp-server/dist/main-stdio.js"],
      "env": {
        "ANKI_CONNECT_URL": "http://localhost:8765"
      }
    }
  }
}
```

Replace `/path/to/anki-mcp-server` with your actual project path.

### Config File Locations

- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

For more details, see the [official MCP documentation](https://modelcontextprotocol.io/docs/develop/connect-local-servers).

## Environment Variables (Optional)

| Variable | Description | Default |
|----------|-------------|---------|
| `ANKI_CONNECT_URL` | AnkiConnect URL | `http://localhost:8765` |
| `ANKI_CONNECT_API_VERSION` | API version | `6` |
| `ANKI_CONNECT_API_KEY` | API key if configured in AnkiConnect | - |
| `ANKI_CONNECT_TIMEOUT` | Request timeout in ms | `5000` |
| `READ_ONLY` | Enable read-only mode (`true` or `1`) | `false` |
| `PORT` | HTTP mode: port to listen on (`--port` flag takes precedence) | `3000` |
| `HOST` | HTTP mode: address to bind to (`--host` flag takes precedence) | `127.0.0.1` |
| `ALLOWED_HOSTS` | HTTP mode: extra `Host` header values to accept beyond loopback (comma-separated hostnames). Required when binding to a LAN/public address or running behind a reverse proxy. See [HTTP Mode Configuration](#http-mode-configuration). | loopback only |
| `ALLOWED_ORIGINS` | HTTP mode: comma-separated allowlist of browser `Origin`/`Referer` patterns (wildcards supported, e.g. `https://*.ngrok.io`). | `http://localhost:*,http://127.0.0.1:*,https://localhost:*,https://127.0.0.1:*` |
| `TUNNEL_SERVER_URL` | Tunnel server WebSocket URL (tunnel mode only) | `wss://tunnel.ankimcp.ai` |
| `MEDIA_ALLOWED_TYPES` | Extra MIME types to allow for file path imports (comma-separated, e.g., `application/pdf`) | - |
| `MEDIA_IMPORT_DIR` | Restrict file path imports to this directory | - |
| `MEDIA_ALLOWED_HOSTS` | Allow specific private network hosts for URL imports (comma-separated, e.g., `192.168.1.50,my-nas`) | - |

## Usage Examples

### Searching and Updating Notes

```
# Search for notes in a specific deck
findNotes(query: "deck:Spanish")

# Get detailed information about notes
notesInfo(notes: [1234567890, 1234567891])

# Update a note's fields (HTML content supported)
updateNoteFields(note: {
  id: 1234567890,
  fields: {
    "Front": "<b>¿Cómo estás?</b>",
    "Back": "How are you?"
  }
})

# Delete notes (requires confirmation)
deleteNotes(notes: [1234567890], confirmDeletion: true)
```

### Anki Query Syntax Examples

The `findNotes` tool supports Anki's powerful query syntax:

- `"deck:DeckName"` - All notes in a specific deck
- `"tag:important"` - Notes with the "important" tag
- `"is:due"` - Cards that are due for review
- `"is:new"` - New cards that haven't been studied
- `"added:7"` - Notes added in the last 7 days
- `"front:hello"` - Notes with "hello" in the front field
- `"flag:1"` - Notes with red flag
- `"prop:due<=2"` - Cards due within 2 days
- `"deck:Spanish tag:verb"` - Spanish deck notes with verb tag (AND)
- `"deck:Spanish OR deck:French"` - Notes from either deck

### Important Notes

#### CSS and HTML Handling
- The `notesInfo` tool returns each note's note type name; the CSS itself comes from `modelStyling`
- The `updateNoteFields` tool supports HTML content in fields and preserves CSS styling
- Each note model has its own CSS styling - use `modelStyling` to get model-specific CSS

#### Update Warning
⚠️ **IMPORTANT**: When using `updateNoteFields`, do NOT view the note in Anki's browser while updating, or the fields will not update properly. Close the browser or switch to a different note before updating. See [Known Issues](#known-issues) for more details.

#### Deletion Safety
The `deleteNotes` tool requires explicit confirmation (`confirmDeletion: true`) to prevent accidental deletions. Deleting a note removes ALL associated cards permanently.

## Security

### Media File Path and URL Validation

The media tools (`storeMediaFile`, `retrieveMediaFile`, `deleteMediaFile`) and `updateNoteFields` audio/picture fields include security validation to prevent misuse via prompt injection:

- **File path imports** are restricted to media file types only (images, audio, video). Non-media files (e.g., SSH keys, credentials, shell configs) are rejected based on MIME type. Configure `MEDIA_ALLOWED_TYPES` to allow additional file types, or `MEDIA_IMPORT_DIR` to restrict imports to a specific directory.
- **URL imports** are validated against SSRF attacks. Requests to private networks (10.x, 172.16.x, 192.168.x), loopback (127.x), link-local (169.254.x), and non-HTTP(S) schemes are blocked. Configure `MEDIA_ALLOWED_HOSTS` to allow specific private network hosts.
- **Filenames** are sanitized to prevent path traversal (e.g., `../../` sequences are stripped).

These protections apply to `storeMediaFile`, `retrieveMediaFile`, `deleteMediaFile`, and `updateNoteFields` audio/picture fields.

> Path traversal vulnerability reported by [Hideaki Takahashi](https://github.com/Koukyosyumei).

### DNS-Rebinding Protection (HTTP transport)

When running in HTTP mode, the server validates the `Host` header on every request. By default only loopback hosts (`localhost`, `127.0.0.1`, `::1`) are accepted, regardless of port. `Host` is a browser-forbidden header, so a malicious web page cannot forge it — this closes the DNS-rebinding path where a rebound page reaches the local server with a spoofed `Host` and no `Origin`, and reaches the MCP tools. A disallowed `Host` is rejected with `403`.

If you bind to `0.0.0.0`, run behind a reverse proxy, or expose a public tunnel domain, set `ALLOWED_HOSTS` (comma-separated hostnames) to permit those hosts. When tunneling with ngrok the server uses `--host-header=rewrite`, so the upstream still sees a loopback `Host`. See [HTTP Mode Configuration](#http-mode-configuration) for the full list of options.

> DNS-rebinding vulnerability reported by [avishaigo-commits](https://github.com/avishaigo-commits) and [yotampe-pluto](https://github.com/yotampe-pluto).

## Privacy Policy

This MCP server runs locally on your machine and collects no telemetry, analytics, or usage data.

Full policy: **[https://ankimcp.ai/privacy/](https://ankimcp.ai/privacy/)**

- **Data collection**: The server collects nothing. It proxies requests between your AI assistant and your local AnkiConnect plugin.
- **Usage / storage**: No server-side storage. All flashcard data stays in your Anki installation on your own device.
- **Third-party sharing**: None. The server only talks to the AnkiConnect URL you configure (default: localhost). If you enable Anki's built-in AnkiWeb sync, that happens between your Anki install and AnkiWeb directly — outside this server's scope.
- **Retention**: Not applicable — no data is retained server-side.
- **Contact**: support@ankimcp.ai

## Known Issues

For a comprehensive list of known issues and limitations, please visit our documentation:

**[Known Issues Documentation](https://ankimcp.ai/docs/known-issues/)**

### Critical Limitations

#### Note Updates Fail When Viewed in Browser
⚠️ **IMPORTANT**: When updating notes using `updateNoteFields`, the update will silently fail if the note is currently being viewed in Anki's browser window. This is an upstream AnkiConnect limitation.

**Workaround**: Always close the browser or navigate to a different note before updating.

For more details and other known issues, see the [full documentation](https://ankimcp.ai/docs/known-issues/).

## Troubleshooting

### ERR_REQUIRE_ESM Error

If you see an error like:
```
Error [ERR_REQUIRE_ESM]: require() of ES Module not supported
```

This means your Node.js version is not supported. The server requires **Node.js 22.12.0+**.

> **Note:** The minimum supported runtime is Node.js 22.12.0. Node.js 20 (Iron) reached end-of-life on 2026-04-30 and is no longer supported.

**Check your version:**
```bash
node --version
```

**Solution:** Update Node.js to version 22.12.0+. You can download it from [nodejs.org](https://nodejs.org/) or use a version manager like [nvm](https://github.com/nvm-sh/nvm).

## Development

### Transport Modes

This server supports three MCP transport modes via **separate entry points**:

#### STDIO Mode (Default)
- For local MCP clients like Claude Desktop
- Uses standard input/output for communication
- **Entry point**: `dist/main-stdio.js`
- **Run**: `npm run start:prod:stdio` or `node dist/main-stdio.js`
- **MCPB bundle**: Uses STDIO mode

#### HTTP Mode (Streamable HTTP)
- For remote MCP clients and web-based integrations
- Uses MCP Streamable HTTP protocol
- **Entry point**: `dist/main-http.js`
- **Run**: `npm run start:prod:http` or `node dist/main-http.js`
- **Default port**: 3000 (configurable via `PORT` env var)
- **Default host**: `127.0.0.1` (configurable via `HOST` env var)
- **MCP endpoint**: `http://127.0.0.1:3000/` (root path)

#### Tunnel Mode (Managed WebSocket Tunnel)
- For web-based AI assistants via the managed AnkiMCP tunnel service, with built-in authentication
- The MCP server runs in-process behind an in-memory transport; `TunnelTransport` owns the MCP server and `TunnelClient` bridges it to the tunnel service over a WebSocket
- **Protocol**: serves the 2025 MCP revision only (STDIO and HTTP also serve 2026-07-28)
- **Entry point**: `dist/main-tunnel.js`
- **Run**: `node dist/main-tunnel.js --tunnel` (or `ankimcp --tunnel`)
- **Auth**: `ankimcp --login` / `ankimcp --logout`; credentials stored at `~/.ankimcp/credentials.json` (`0600`)
- **Dev**: `npm run start:dev:tunnel` (watch mode, runs `--tunnel --debug`)

#### Building

```bash
npm run build  # Builds once, creates dist/ with all three entry points
```

`main-stdio.js`, `main-http.js`, and `main-tunnel.js` are all built into the same `dist/` directory. Choose which to run based on your needs.

#### HTTP Mode Configuration

**Environment Variables:**
- `PORT` - HTTP server port (default: 3000)
- `HOST` - Bind address (default: 127.0.0.1 for localhost-only)
- `ALLOWED_HOSTS` - Comma-separated extra `Host` header values to accept beyond the built-in loopback set (`localhost`, `127.0.0.1`, `::1`). Hostname-only and port-agnostic. Default: loopback only.
- `ALLOWED_ORIGINS` - Comma-separated allowlist of browser `Origin`/`Referer` patterns; wildcards supported (e.g. `https://*.ngrok.io`). Default: `http://localhost:*,http://127.0.0.1:*,https://localhost:*,https://127.0.0.1:*`.
- `LOG_LEVEL` - Logging level (default: info)

**Security:**
- **Host header validation (DNS-rebinding protection)** — every HTTP request must carry a `Host` header that matches the allowlist. By default only loopback hosts (`localhost`, `127.0.0.1`, `::1`) are accepted, regardless of port. `Host` is a browser-forbidden header, so a malicious web page cannot forge it — this closes the [DNS-rebinding](https://github.com/ankimcp/anki-mcp-server/security/advisories) path where a rebound page reaches the server with a spoofed `Host` and no `Origin`. A disallowed `Host` is rejected with `403`.
- **Origin header validation** — browser requests with a present-but-disallowed `Origin`/`Referer` are rejected. Requests with **no** `Origin` (curl, Postman, MCP-over-HTTP clients) are allowed; Host validation is the defense against rebinding.
- Binds to localhost (127.0.0.1) by default.
- No authentication in current version (OAuth support planned).

**Exposing HTTP mode beyond localhost** — if you bind to a LAN/public address or put the server behind a reverse proxy or public domain, you **must** set `ALLOWED_HOSTS` to the hostname(s) clients will use, otherwise every non-loopback request is rejected with `403`:

```bash
# Bind to all interfaces and accept the machine's LAN name + a public domain
ALLOWED_HOSTS=my-nas.local,anki.example.com PORT=8080 HOST=0.0.0.0 node dist/main-http.js
```

When you bind to `0.0.0.0`/`::` without `ALLOWED_HOSTS`, the server logs a startup warning that only loopback `Host` headers will be accepted.

> **Docker / reverse proxy / public domain:** the same rule applies. In Docker, requests usually arrive with the container's published hostname or the proxy's `Host`, so set `ALLOWED_HOSTS` accordingly. A reverse proxy (nginx, Caddy, Traefik) should either forward the original `Host` and have that hostname listed in `ALLOWED_HOSTS`, or rewrite the upstream `Host` to `localhost`. The built-in `--ngrok` integration handles this automatically (see below).

**Example: Running Modes**
```bash
# Development - STDIO mode (watch mode with auto-rebuild)
npm run start:dev:stdio

# Development - HTTP mode (watch mode with auto-rebuild)
npm run start:dev:http

# Production - STDIO mode
npm run start:prod:stdio
# or
node dist/main-stdio.js

# Production - HTTP mode
npm run start:prod:http
# or
PORT=8080 HOST=0.0.0.0 node dist/main-http.js
```

### Building an MCPB Bundle

To create a distributable MCPB bundle:

```bash
npm run mcpb:bundle
```

This command will:
1. Sync version from `package.json` to `manifest.json`
2. Remove old `.mcpb` files
3. Build the TypeScript project
4. Package `dist/` and `node_modules/` into an `.mcpb` file
5. Run `mcpb clean` to remove devDependencies (optimizes bundle from ~47MB to ~10MB)

The output file will be named `anki-mcp-server-X.X.X.mcpb` and can be distributed for one-click installation.

#### What Gets Bundled

The MCPB bundle includes:
- Compiled JavaScript (`dist/` directory - includes all three entry points)
- Production dependencies only (`node_modules/` - devDependencies removed by `mcpb clean`)
- Package metadata (`package.json`)
- Manifest configuration (`manifest.json` - configured to use `main-stdio.js`)
- Icon (`icon.png`)

Source files, tests, and development configs are automatically excluded via `.mcpbignore`.

### Logging in Claude Desktop

When running as an MCPB extension in Claude Desktop, logs are written to:

**Log Location**: `~/Library/Logs/Claude/` (macOS)

The logs are split across multiple files:
- **main.log** - General Claude Desktop application logs
- **mcp-server-Anki MCP Server.log** - MCP protocol messages for this extension
- **mcp.log** - Combined MCP logs from all servers

**Note**: The pino logger output (INFO, ERROR, WARN messages from the server code) goes to stderr and appears in the MCP-specific log files. Claude Desktop determines which log file receives which messages, but generally:
- Application startup and MCP protocol communication → MCP-specific log
- Server internal logging (pino) → Both MCP-specific log and sometimes main.log

To view logs in real-time:
```bash
tail -f ~/Library/Logs/Claude/mcp-server-Anki\ MCP\ Server.log
```

### Debugging the MCP Server

You can debug the MCP server using the MCP Inspector and attaching a debugger from your IDE (WebStorm, VS Code, etc.).

**Note for HTTP Mode:** When testing HTTP mode (Streamable HTTP) with MCP Inspector, use "Connection Type: Via Proxy" to avoid CORS errors.

#### Step 1: Configure Debug Server in MCP Inspector

The `mcp-inspector-config.json` already includes a debug server configuration:

```json
{
  "mcpServers": {
    "stdio-server-debug": {
      "type": "stdio",
      "command": "node",
      "args": ["--inspect-brk=9229", "dist/main-stdio.js"],
      "env": {
        "MCP_SERVER_NAME": "anki-mcp-stdio-debug",
        "MCP_SERVER_VERSION": "1.0.0",
        "LOG_LEVEL": "debug"
      },
      "note": "Anki MCP server with debugging enabled on port 9229"
    }
  }
}
```

#### Step 2: Start the Debug Server

Run the MCP Inspector with the debug server:

```bash
npm run inspector:debug
```

This will start the server with Node.js debugging enabled on port 9229 and pause execution at the first line.

#### Step 3: Attach Debugger from Your IDE

##### WebStorm
1. Go to **Run → Edit Configurations**
2. Add a new **Attach to Node.js/Chrome** configuration
3. Set the port to `9229`
4. Click **Debug** to attach

##### VS Code
1. Open the Debug panel (Ctrl+Shift+D / Cmd+Shift+D)
2. Select **Debug MCP Server (Attach)** configuration
3. Press F5 to attach

#### Step 4: Set Breakpoints and Debug

Once attached, you can:
- Set breakpoints in your TypeScript source files
- Step through code execution
- Inspect variables and call stack
- Use the debug console for evaluating expressions

The debugger will work with source maps, allowing you to debug the original TypeScript code rather than the compiled JavaScript.

### Debugging with Claude Desktop

You can also debug the MCP server while it runs inside Claude Desktop by enabling the Node.js debugger and attaching your IDE.

#### Step 1: Configure Claude Desktop for Debugging

Update your Claude Desktop config to enable debugging:

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
**Linux**: `~/.config/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "anki-mcp": {
      "command": "node",
      "args": [
        "--inspect=9229",
        "<path_to_project>/anki-mcp-server/dist/main-stdio.js"
      ],
      "env": {
        "ANKI_CONNECT_URL": "http://localhost:8765"
      }
    }
  }
}
```

**Key change**: Add `--inspect=9229` before the path to `dist/main-stdio.js`

**Debug options**:
- `--inspect=9229` - Start debugger immediately, doesn't block (recommended)
- `--inspect-brk=9229` - Pause execution until debugger attaches (for debugging startup issues)

#### Step 2: Restart Claude Desktop

After saving the config, restart Claude Desktop. The MCP server will now run with debugging enabled on port 9229.

#### Step 3: Attach Debugger from Your IDE

##### WebStorm

1. Go to **Run → Edit Configurations**
2. Click the **+** button and select **Attach to Node.js/Chrome**
3. Configure:
    - **Name**: `Attach to Anki MCP (Claude Desktop)`
    - **Host**: `localhost`
    - **Port**: `9229`
    - **Attach to**: `Node.js < 8` or `Chrome or Node.js > 6.3` (depending on WebStorm version)
4. Click **OK**
5. Click **Debug** (Shift+F9) to attach

##### VS Code

1. Add to `.vscode/launch.json`:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "node",
      "request": "attach",
      "name": "Attach to Anki MCP (Claude Desktop)",
      "port": 9229,
      "skipFiles": ["<node_internals>/**"],
      "sourceMaps": true,
      "outFiles": ["${workspaceFolder}/dist/**/*.js"]
    }
  ]
}
```

2. Open the Debug panel (Ctrl+Shift+D / Cmd+Shift+D)
3. Select **Attach to Anki MCP (Claude Desktop)**
4. Press F5 to attach

#### Step 4: Debug in Real-Time

Once attached, you can:
- Set breakpoints in your TypeScript source files (e.g., `src/mcp/primitives/essential/tools/create-model.tool.ts`)
- Use Claude Desktop normally - breakpoints will hit when tools are invoked
- Step through code execution
- Inspect variables and call stack
- Use the debug console

**Example**: Set a breakpoint in `create-model.tool.ts` at line 119, then ask Claude to create a new model. The debugger will pause at your breakpoint!

**Note**: The debugger stays attached as long as Claude Desktop is running. You can detach/reattach anytime without restarting Claude Desktop.

### Build Commands

```bash
npm run build              # Build the project (compile TypeScript to JavaScript)
npm run start:dev:stdio    # STDIO mode with watch (auto-rebuild)
npm run start:dev:http     # HTTP mode with watch (auto-rebuild)
npm run type-check         # Run TypeScript type checking
npm run lint               # Run ESLint
npm run mcpb:bundle        # Sync version, clean, build, and create MCPB bundle
```

### NPM Package Testing (Local)

Test the npm package locally before publishing:

```bash
# 1. Create local package
npm run pack:local         # Builds and creates @ankimcp/anki-mcp-server-*.tgz

# 2. Install globally from local package
npm run install:local      # Installs from ./@ankimcp/anki-mcp-server-*.tgz

# 3. Test the command
ankimcp                    # Runs HTTP server on port 3000

# 4. Uninstall when done testing
npm run uninstall:local    # Removes global installation
```

**How it works:**
- `npm pack` creates a `.tgz` file identical to what npm publish would create
- Installing from `.tgz` simulates what users get from `npm install -g ankimcp`
- This lets you test the full user experience before publishing to npm

### Testing Commands

```bash
npm test              # Run all tests
npm run test:unit     # Run unit tests only
npm run test:tools    # Run tool-specific tests
npm run test:workflows # Run workflow integration tests
npm run test:e2e      # Run end-to-end tests
npm run test:cov      # Run tests with coverage report
npm run test:watch    # Run tests in watch mode
npm run test:debug    # Run tests with debugger
npm run test:ci       # Run tests for CI (silent, with coverage)
```

### Test Coverage

The project maintains 70% minimum coverage thresholds for:
- Branches
- Functions
- Lines
- Statements

Coverage reports are generated in the `coverage/` directory.

## Versioning

This project follows [Semantic Versioning](https://semver.org/) with a pre-1.0 development approach:

- **0.x.x** - Beta/Development versions (current phase)
    - **0.1.x** - Bug fixes and patches
    - **0.2.0+** - New features or minor improvements
    - **Breaking changes** are acceptable in 0.x versions

- **1.0.0** - First stable release
    - Will be released when the API is stable and tested
    - Breaking changes will require major version bumps (2.0.0, etc.)

**Current Status**: `0.27.0` - Active beta development. Recent features include collection-wide review analysis (`review_stats` now aggregates across all decks when `deck` is omitted), model field management (`addModelField`, `removeModelField`, `renameModelField`, `repositionModelField`), batch note creation (`addNotes`), integrated ngrok tunneling (`--ngrok` flag), media file management, model/template management, and comprehensive deck statistics. APIs may change based on feedback and testing.

### MCPB spec evolution

This project targets Anthropic's MCPB bundle specification, which is still evolving. We track the spec at [https://github.com/modelcontextprotocol/mcpb](https://github.com/modelcontextprotocol/mcpb) and may introduce breaking changes to stay compliant. Breaking changes are permitted under the 0.x.x versioning scheme.

## Similar Projects

If you're exploring Anki MCP integrations, here are other projects in this space:

### [scorzeth/anki-mcp-server](https://github.com/scorzeth/anki-mcp-server)
- **Status**: Appears to be abandoned (no recent updates)
- Early implementation of Anki MCP integration

### [nailuoGG/anki-mcp-server](https://github.com/nailuoGG/anki-mcp-server)
- **Approach**: Lightweight, single-file implementation
- **Architecture**: Procedural code structure with all tools in one file
- **Good for**: Simple use cases, minimal dependencies

**Why this project differs:**
- **Enterprise-grade architecture**: Built on NestJS with dependency injection
- **Modular design**: Each tool is a separate class with clear separation of concerns
- **Maintainability**: Easy to extend with new features without touching existing code
- **Testing**: Comprehensive test suite with 70% coverage requirement
- **Type safety**: Strict TypeScript with Zod validation
- **Error handling**: Robust error handling with helpful user feedback
- **Production-ready**: Proper logging, progress reporting, and MCPB bundle support
- **Scalability**: Can easily grow from basic tools to complex workflows

**Use case**: If you need a solid foundation for building advanced Anki integrations or plan to extend functionality significantly, this project's architectural approach makes it easier to maintain and scale over time.

## Useful Links

- [Model Context Protocol Documentation](https://modelcontextprotocol.io/docs)
- [AnkiConnect API Documentation](https://git.sr.ht/~foosoft/anki-connect)
- [Claude Desktop Download](https://claude.ai/download)
- [Building Desktop Extensions (Anthropic Blog)](https://www.anthropic.com/engineering/desktop-extensions)
- [MCP Servers Repository](https://github.com/modelcontextprotocol/servers)
- [NestJS Documentation](https://docs.nestjs.com)
- [Anki Official Website](https://apps.ankiweb.net/)

## License & Attribution

This project is licensed under the MIT License — see [LICENSE](LICENSE) for the full text.

Copyright © 2026 Anatoly Tarnavsky.

### Third-Party Attributions

- **Anki®** is a registered trademark of Ankitects Pty Ltd. This project is an unofficial third-party tool and is not affiliated with, endorsed by, or sponsored by Ankitects Pty Ltd. The Anki logo is used under the alternative license for referencing Anki with a link to [https://apps.ankiweb.net](https://apps.ankiweb.net). For the official Anki application, visit [https://apps.ankiweb.net](https://apps.ankiweb.net).

- **Model Context Protocol (MCP)** is an open standard by Anthropic. The MCP logo is from the official [MCP documentation repository](https://github.com/modelcontextprotocol/docs) and is used under the MIT License. For more information about MCP, visit [https://modelcontextprotocol.io](https://modelcontextprotocol.io).

- This is an independent project that bridges Anki and MCP technologies. All trademarks, service marks, trade names, product names, and logos are the property of their respective owners.


## 文件 CLAUDE.md

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

MCP server enabling AI assistants to interact with Anki via AnkiConnect. Built with NestJS and `@rekog/mcp-nest`.

- **Package**: `@ankimcp/anki-mcp-server` (npm)
- **License**: MIT
- **Status**: Beta (0.x.x) - breaking changes allowed
- **User-facing docs**: `README.md` covers installation, client setup (Claude Desktop/MCPB, HTTP, tunnel), and the full tool catalog — consult it for anything user-facing rather than reconstructing it here.

## Quick Reference

```bash
# Build & Run
npm run build                    # Build → dist/ (all three entry points)
npm run start:dev:stdio          # STDIO mode with watch
npm run start:dev:http           # HTTP mode with watch

npm run start:dev:tunnel         # Tunnel mode with watch + debug

# Testing
npm test                         # All tests
npm test -- path/to/file.spec.ts # Single test file
npm run test:tools               # Tool unit tests only
npm run test:workflows           # Multi-tool workflow scenarios (mocked)
npm run test:cov                 # With coverage (70% threshold)
npm run e2e:full:local           # One-shot E2E: up → test → down
npm run smoke:pack               # Pack + install from tarball (no lockfile), verify initialize/tools-list

# Quality
npm run lint && npm run type-check   # Pre-push checks (also runs via Husky)

# Debugging
npm run inspector:stdio          # MCP Inspector UI for testing tools
npm run inspector:stdio:debug    # With debugger on port 9229
npm run inspector:http           # Inspector against HTTP transport
```

## Architecture

### Entry Points

Three entry points compiled in a single build:

| Mode | Entry | Use Case | Logging |
|------|-------|----------|---------|
| STDIO | `dist/main-stdio.js` | Claude Desktop, MCP clients | stderr |
| HTTP | `dist/main-http.js` | Web-based AI (ChatGPT, claude.ai) | stdout |
| Tunnel | `dist/main-tunnel.js` | Remote access via WebSocket tunnel | stderr |

### Core Files

```
src/
├── main-stdio.ts            # STDIO bootstrap: NestFactory.createMicroservice() with the MCP strategy
├── main-http.ts             # HTTP bootstrap: NestFactory.create() + guards + connectMicroservice()
├── main-tunnel.ts           # Tunnel bootstrap: auth commands + WebSocket tunnel
├── app.module.ts            # Root module with forStdio()/forHttp()/forTunnel() factories
├── bootstrap.ts             # Shared logger setup (pino → NestJS LoggerService) + createMcpStrategy()
├── version.ts               # Package version constant (read from package.json at build)
├── cli/                     # CLI layer (Commander parsing + user-facing output)
│   ├── args.ts              # Commander entrypoint: option parsing, subcommand dispatch
│   ├── cli-output.ts        # User-facing print helpers (cli.success/error/info/box) — separate from args.ts so non-CLI code can use it without pulling in Commander
│   ├── spinner.ts           # Terminal spinner for long-running CLI operations
│   └── index.ts             # Barrel re-export for the cli module
├── app-config.service.ts    # IAnkiConfig implementation (reads from validated AppConfig)
├── config/                  # Zod-validated config system (schema, factory, APP_CONFIG token)
├── services/ngrok.service.ts # Optional ngrok subprocess for HTTP-mode public tunneling
├── http/guards/             # HTTP-only guards: origin-validation + host-validation (DNS-rebinding protection)
├── http/mcp-http.factory.ts # StreamableHttpTransport + the Nest controller that owns the MCP route
├── tunnel/                  # Tunnel mode: WebSocket client, OAuth device flow, credentials
│   ├── tunnel.client.ts     # WebSocket client for tunnel server
│   ├── tunnel.transport.ts  # McpTransport for tunnel mode: owns the bound MCP server + handleRequest()
│   ├── in-memory.transport.ts # SDK Transport that pairs a relayed request with the server's response
│   ├── tunnel.protocol.ts   # WS message type definitions (request/response/ping/error)
│   ├── device-flow.service.ts # OAuth device flow authentication
│   ├── credentials.service.ts # Persistent credential storage
│   └── commands/            # CLI command handlers (login, logout, tunnel)
└── mcp/
    ├── clients/anki-connect.client.ts  # HTTP client using ky (retries, error handling, read-only guard)
    ├── config/anki-config.interface.ts # ANKI_CONFIG injection token + IAnkiConfig interface
    ├── types/anki.types.ts             # Shared Anki types (cards, notes, ratings)
    ├── utils/                          # Shared utilities (anki.utils, date.utils, markdown.utils, stats.utils, media-validation.utils, card-states.utils, deck-hierarchy.utils, card-validation.utils, card-suspension.utils)
    ├── primitives/essential/           # Core tools, prompts, resources
    └── primitives/gui/                 # GUI-specific tools (require user approval)
```

### Module System

```
AppModule.forStdio()/forHttp()/forTunnel()
  → MCP_STRATEGY provider           # the McpStrategy the entry point built
  → McpPrimitivesAnkiEssentialModule.forRoot()
  → McpPrimitivesAnkiGuiModule.forRoot()
```

Each entry point builds exactly one `McpStrategy` (`new McpStrategy({ name, version, icons, instructions, transports })` — see `createMcpStrategy()` in `bootstrap.ts`) and hands the same instance to both `AppModule.forX()` (as `MCP_STRATEGY`) and the NestJS microservice connection: `createMicroservice()` for STDIO/tunnel, `connectMicroservice()` + `startAllMicroservices()` for HTTP. Transports are instances, not enum values — `new StdioTransport()`, `new StreamableHttpTransport()`, `new TunnelTransport()`.

All tools/prompts/resources are `@McpController()` classes listed in each primitive module's `controllers` array (see `ESSENTIAL_MCP_TOOLS` and `GUI_MCP_TOOLS`). NestJS scans every module's controllers for the `@MessagePattern` handlers that `@Tool`/`@Prompt`/`@Resource` compile to, so `AppModule` does not re-list them.

**HTTP mode** does not let the transport self-mount its route. `createMcpHttpServer()` (`src/http/mcp-http.factory.ts`) builds the MCP endpoint as a controller via the `McpHttpControllerFor(transport)` mixin, so requests run through the Nest pipeline and the Origin/Host `APP_GUARD`s apply. A self-mounted route would register straight on the HTTP adapter and bypass them.

**Tunnel mode** uses `TunnelTransport` (`src/tunnel/tunnel.transport.ts`): it gets a fully-wired server from `ctx.createBoundServer(session)`, connects it to an `InMemoryTransport` channel, and exposes `handleRequest(body)`. `TunnelClient` relays request bodies from the tunnel server over WebSocket into that method. Bootstrap lives in `src/tunnel/commands/tunnel.command.ts`. The bound server is created with `era: "legacy"`, so tunnel mode serves only the 2025 protocol revision — STDIO and HTTP also negotiate the 2026-07-28 revision.

### Key Patterns

**Tool response format**: Success paths return raw objects matching the tool's `outputSchema`. The mcp-nest handler validates and wraps them automatically. Error paths use `createErrorResponse(error, context)` from `anki.utils.ts` which returns `CallToolResult` with `isError: true` and bypasses outputSchema validation. Two distinct `success: false` shapes exist: with `error` + `isError: true` (from `createErrorResponse`) the call failed; without them (see `add-notes.tool.ts`, `suspend`/`unsuspend`) the call ran and the payload describes a partial outcome — routing those through `createErrorResponse` would drop `structuredContent`.

**Action helper pattern**: The former aggregate tools (`deckActions`, `tagActions`, `mediaActions`) were split into single-purpose tools (`list-decks.tool.ts`, `deck-stats.tool.ts`, `create-deck.tool.ts`, `change-deck.tool.ts`, `store-media-file.tool.ts`, `replace-tags.tool.ts`, …). Their directories now hold only `actions/*.action.ts` — pure functions taking `(params, ankiClient)` that the split tools import. The tool class stays thin: log, call the helper, wrap failures in `createErrorResponse`.

**Read-only mode**: `AnkiConnectClient` enforces read-only mode by checking actions against a `WRITE_ACTIONS` set before sending requests. Throws `ReadOnlyModeError`. The set covers content, deck, tag, media and note-type writes, the manual rescheduling actions (`forgetCards`, `setDueDate`), `guiUndo`, and the Add/Edit dialogs (`guiAddCards`, `guiEditNote`). Still allowed: `answerCards` (rating during review), `suspend`/`unsuspend`, `sync`, and the GUI navigation actions. `createErrorResponse` replaces the caller's hint with a read-only hint for a `ReadOnlyModeError`, so tools need no special handling.

**Config system**: Two injection tokens:
- `APP_CONFIG` — validated `AppConfig` object (Zod schema in `src/config/config.schema.ts`). Provided as `useValue` after parsing env + CLI overrides.
- `ANKI_CONFIG` — AnkiConnect-specific config interface. Provided via `useClass: AppConfigService` in each module's `forRoot()`. Modules can swap the config provider for testing.

**Environment Configuration**: Config `process.env.*` reads go through `buildConfigInput()` in `src/config/config.factory.ts`. CLI args override env vars in memory (no `process.env` mutation). Services inject `AppConfigService` for type-safe access. Two deliberate exceptions sit outside the config system: `media-validation.utils.ts` (`MEDIA_*`) and `system-info.resource.ts` read `process.env` directly.

### Upstream AnkiConnect Quirks

These are upstream behaviors that shape tool design — surface them in tool descriptions, stated as facts about the tool (see "Description style" below), so the AI can avoid them:

- **`updateNoteFields` silently fails** if the target note is open in Anki's Browse window. The request returns 200 but fields don't persist. The tool description states this.
- **Model CSS is per-note-type, not per-note.** Use `modelStyling` to fetch CSS for a model; `notesInfo` tells you which model each note uses. `updateNoteFields` should preserve inline styles.
- **`sync` relies on the desktop app being logged into AnkiWeb.** There's no API path to authenticate — surface a helpful error hint.
- **`deleteNotes` permanently removes the notes and cascades to all their cards.** Anki's undo history (Edit > Undo, or `guiUndo`, which reverts the newest step) can restore them until that history is cleared, for example by a change Anki does not record for undo such as `updateNoteFields`; after that only a backup restores them. The tool requires explicit `confirmDeletion: true`.

### Build & Tooling Notes

- **NestJS CLI** builds the project (`nest build`). Asset copying is configured in `nest-cli.json` — all `**/*.md` files in `src/` are copied to `dist/`. This matters for prompt templates that reference markdown files.
- **`prebuild` hook** runs `scripts/generate-icon.mjs` before every `npm run build` (via npm's `pre*` lifecycle) — that's why an icon-generation step fires on build. It's expected, not a stray command.
- **ESLint flat config** (`eslint.config.mjs`) — not legacy `.eslintrc`. Uses `typescript-eslint` + Prettier integration.
- **TypeScript**: `strict: true`, target ES2023, `nodenext` module resolution. Path aliases are resolved by both `tsconfig.json` and Jest's `moduleNameMapper`.
- **Zod 4** (`^4.4.3`) — not Zod 3. Some patterns like `z.preprocess` in `config.schema.ts` are Zod 3 holdovers that still work but may need migration.

### Path Aliases

- `@/*` → `src/*`
- `@test/*` → `test/*`

### Key Dependencies

- **Zod v4** (`zod@^4.x`) — NOT v3. Zod 4 has different APIs (e.g., `z.interface()`, changed error handling). Don't use v3 patterns.
- **`@rekog/mcp-nest` v2** (`^2.0.0`) — NOT v1. No `McpModule.forRoot()`: the server is a NestJS microservice `CustomTransportStrategy` (`McpStrategy`), capability classes are `@McpController()`s, and handler methods take `@Payload()`.
- **`@modelcontextprotocol/{core,node,server}` v2** — the MCP SDK. The old single `@modelcontextprotocol/sdk` package is gone. Don't bump without testing MCP protocol compatibility.
- **`@nestjs/microservices`** — required by mcp-nest v2 (`CustomStrategy`, `@Payload()`), not optional.
- **TypeScript** — `strict: true`, `module: "nodenext"`, target `ES2023`. Path aliases (`@/`, `@test/`) handle most imports.
- **ESLint** — Flat config (`eslint.config.mjs`), not legacy `.eslintrc`.


### Logging Guidelines

**Two types of output - don't mix them:**

1. **CLI Output** (user-facing, clean, no timestamps):
   ```typescript
   import { cli } from '@/cli/cli-output';

   cli.success('Connected to Anki');      // ✓ Connected to Anki
   cli.error('Connection failed');         // ✗ Connection failed
   cli.info('Starting server...');         // Starting server...
   cli.box('Tunnel URL', 'https://...');   // Boxed message
   cli.blank();                            // Empty line
   ```

2. **Logger** (internal logging, with timestamps and levels):
   ```typescript
   import { Logger } from '@nestjs/common';

   private readonly logger = new Logger(MyService.name);

   this.logger.log('Info message');
   this.logger.warn('Warning message');
   this.logger.error('Error message');
   this.logger.debug('Debug message');
   ```

**When to use which:**
- `cli.*` → User-facing output in CLI commands (tunnel, login, logout, startup banners)
- `Logger` → Internal service logging, debugging, warnings

**Never use raw `console.log/error/warn`** - use `cli.*` or `Logger` instead.

## Adding New Tools

### Essential Tools (general Anki operations)

1. Create `src/mcp/primitives/essential/tools/your-tool.tool.ts`
2. Export from `src/mcp/primitives/essential/index.ts`
3. Add to `ESSENTIAL_MCP_TOOLS` array
4. **Update `manifest.json`** tools array
5. Create test: `src/mcp/primitives/essential/tools/__tests__/your-tool.tool.spec.ts`
6. **Add a `CHANGELOG.md` entry** under the top `[Unreleased]` section

**Note**: `ESSENTIAL_MCP_TOOLS` is the module's `controllers` array — tools, prompts, and resources that MCP-Nest discovers. Infrastructure (`AnkiConnectClient`, the config providers) is listed inline in the module's `providers`.

If the AnkiConnect logic is bulky or shared with another tool, put it in a pure `actions/*.action.ts` helper and keep the tool class thin — see `list-decks.tool.ts` → `deckActions/actions/listDecks.action.ts`.

For tools with complex output schemas, extract Zod types into a `*.types.ts` file alongside the tool (see `collection-stats/collection-stats.types.ts` and `review-stats/review-stats.types.ts`).

### GUI Tools (interface operations)

Same as above but in `src/mcp/primitives/gui/`. The description says, as facts, that the tool acts on the Anki desktop window on the user's screen and what it changes there, that it is for when the user asks for it, and (where relevant) that it is not part of a review session — e.g. "Opens the Card Browser window in the Anki desktop app on the user's screen… For when the user asks to open the browser… Not part of a review session." Any tool that opens a window or changes the displayed screen or current deck gets `readOnlyHint: false`; only tools that change neither Anki data nor the screen (`guiSelectedNotes`, `guiCurrentCard`) are read-only.

### Description style

Tool descriptions, parameter `.describe()` text and the server instructions (`MCP_SERVER_INSTRUCTIONS` in `src/mcp/mcp-instructions.ts`) state **facts** about the tool — what it does, when it is useful, its consequences — not **orders** to the model. No `IMPORTANT:`/`CRITICAL:`/`ALWAYS`/`NEVER`/`DO NOT`/"Use X FIRST"/"Wait for user". When an order carried a real signal, keep the signal as a fact ("Permanently deletes the notes and all their cards", "Records a real review in Anki's scheduler"). Cross-tool choreography (sync offer, review loop, GUI-on-request) lives in the server instructions. Cross-references to this server's own tools are fine. The `hint`, `message`, `warning` and error strings built in the tool and action files under `src/mcp/primitives` follow the same rule: "modelNames lists the available models", not "Use modelNames to see available models"; "This can happen when Anki is not running", not "Make sure Anki is running" (a catch-all branch names possible causes, not a definite one). Error messages thrown by `AnkiConnectClient` and the media-validation error classes are not covered. `src/mcp/primitives/__tests__/tool-metadata-policy.spec.ts` enforces the marker list and the annotation set for every registered tool.

### Tool Pattern

```typescript
// 1. Zod schema for input validation
// 2. @McpController() class with AnkiConnectClient injected (registered as a module controller)
// 3. @Tool({ name, description, parameters, outputSchema, annotations }) decorator
// 4. Handler method taking @Payload() params, calling AnkiConnectClient.invoke()
// 5. Success: return raw object matching outputSchema (handler wraps it automatically)
// 6. Error: return createErrorResponse() (bypasses outputSchema validation)
```

**outputSchema**: All tools define a Zod `outputSchema` in the `@Tool` decorator. The mcp-nest handler validates success returns via `safeParse()` and wraps them as `structuredContent`. Error returns via `createErrorResponse()` have a `content` array and bypass schema validation.

**annotations**: All tools declare `title`, `readOnlyHint`, `destructiveHint`, `openWorldHint`, and optionally `idempotentHint` in the `@Tool` decorator. `openWorldHint` is `true` only for tools that reach beyond the local collection (`sync`, `storeMediaFile`, `updateNoteFields` media URLs). `destructiveHint` is `true` when the call loses data that another call to this server cannot restore (field overwrite, full CSS/template replace, scheduling overwrite, media overwrite, deletes, undo); reversible changes (tag edits, deck moves, suspend, field rename/reposition) stay `false`.

See `src/mcp/primitives/essential/tools/sync.tool.ts` for minimal example.

## Testing

### Test Organization

Three distinct tiers — pick the right one for the change:

- **Unit** — `src/**/__tests__/*.spec.ts`, colocated with source. Mock `AnkiConnectClient`. Fast, run on every push.
  - Tool-level tests live next to each tool (e.g. `src/mcp/primitives/essential/tools/__tests__/`).
  - App-level wiring tests live in `src/__tests__/` (`app-config.service.spec.ts`, `cli.spec.ts`, `main-http.spec.ts`) — bootstrap, CLI parsing, config validation.
- **Workflows** — `test/workflows/*.spec.ts` (e.g., `note-management.spec.ts`, `review-session.spec.ts`). Multi-tool scenarios still against a mocked client. Use for cross-tool invariants.
- **E2E** — `test/e2e/*.e2e-spec.ts`. Hits a real Anki + AnkiConnect running in Docker. Covers both STDIO and HTTP transports.

Shared test infra:

- `src/test-fixtures/test-helpers.ts` — `parseToolResult()`
- `src/test-fixtures/mock-data.ts` — `mockNotes`, `mockDecks`, `mockCards`, `mockErrors`
- `test/jest-environments/timezone.environment.ts` — Jest environment that pins the process timezone for one spec file via a `@jest-environment` docblock (writing `process.env.TZ` inside a test has no effect — Jest sandboxes `process.env`). Use it for anything that depends on local-day boundaries.

```bash
# Single test file
npm test -- src/mcp/primitives/essential/tools/__tests__/sync.tool.spec.ts
```

**ESM deps load natively**: Jest runs with `--experimental-vm-modules` (wired into the npm test scripts via `NODE_OPTIONS` — see the Environment section), so ESM-only deps like `ky`, `unified`, and `remark-parse` load without transformation. The `transformIgnorePatterns` jest-config workaround was removed; new ESM deps need no special handling.

### E2E Tests (requires Docker)

```bash
npm run e2e:up              # Start Anki + AnkiConnect containers
npm run e2e:test            # Run all E2E tests
npm run e2e:test:stdio      # STDIO transport only
npm run e2e:test:http       # HTTP transport only
npm run e2e:down            # Stop containers
npm run e2e:full:local      # All-in-one: up → test → down
```

## Git Hooks (Husky)

- **pre-commit**: Runs `npm run sync-version` to sync `package.json` version → `manifest.json`, then stages `manifest.json`
- **pre-push**: Runs lint, type-check, and full test suite (all must pass)

## Release Process

1. Update version in `package.json` (single source of truth — pre-commit hook syncs to `manifest.json`)
2. Rename the `## [Unreleased]` section in `CHANGELOG.md` to the new version and date
3. **Add new tools to `manifest.json` tools array**
4. Commit and tag: `git tag -a v0.x.0 -m "message" && git push origin v0.x.0`
5. GitHub Actions handles: version sync, build, MCPB bundle, npm publish, GitHub release

**npm publishing** uses OIDC Trusted Publishing (no `NPM_TOKEN` needed). The `--provenance` flag triggers OIDC auth and generates cryptographic attestations. Configured in `npm-publish.yml` and `npm-publish-legacy.yml`.

**MCP Registry publishing** is handled by `mcp-registry-publish.yml`, which publishes `server.json` to the official MCP registry on tagged releases (wired in v0.18.4).

**Don't run `npm run mcpb:bundle` manually** - CI handles it.

## MCPB Bundle Notes

Bundle uses STDIO entry point. Key gotchas:

- User config keys in `manifest.json` must be **snake_case** (e.g., `anki_connect_url`)
- Peer dependencies of `@rekog/mcp-nest` must stay as direct deps (`@modelcontextprotocol/{core,node,server}`, `@nestjs/microservices`)
- `mcpb clean` removes devDeps to optimize size (47MB → ~10MB)
- Use **npm** (not pnpm) - `mcpb clean` doesn't work with pnpm's node_modules

## Environment

Node.js requirement: `>=22.12.0` (Node 20 reached end-of-life on 2026-04-30; oldest supported LTS is Node 22). That is the runtime floor — the highest `engines.node` among production deps is `commander`'s `>=22.12.0`.

**Development needs a newer Node than `engines` declares**: `@modelcontextprotocol/inspector` (devDependency, drives the E2E suite) requires `>=22.19.0`. NestJS 12 ships ESM-only packages (`@nestjs/{common,core,microservices,platform-express}`); Node's `require(esm)` interop lets the app itself run fine on Node `>=22.12`, but Jest's own module loader gates `require(esm)` on `vm.SourceTextModule` being available — that needs both Node `>=24.9` and the `--experimental-vm-modules` V8 flag, not the Node version alone. The npm test scripts (`test`, `test:tools`, `test:workflows`, `test:cov`, etc.) already set `NODE_OPTIONS=--experimental-vm-modules`, so contributors running `npm test` don't need to set anything manually. Without that combination, unit tests that import Nest fail with `ERR_REQUIRE_ESM`-style "Must use import to load ES Module" errors. So development/testing now needs Node `>=24.9` as the floor, even though `engines.node` deliberately stays at the runtime floor so consumers aren't forced higher for tooling they never install. On an older Node, `npm install` warns `EBADENGINE` and both E2E and unit tests can fail.

Key environment variables (all have defaults, see `src/config/config.schema.ts`):
- `ANKI_CONNECT_URL` — AnkiConnect URL (default: `http://localhost:8765`)
- `ANKI_CONNECT_API_KEY` — Optional AnkiConnect API key
- `TUNNEL_SERVER_URL` — Tunnel server WebSocket URL (default: `wss://tunnel.ankimcp.ai`)
- `TUNNEL_AUTH_CLIENT_ID` — OAuth/OIDC client ID for tunnel auth
- `LOG_LEVEL` — `debug|info|warn|error` (default: `info`)
- `READ_ONLY` — `true|1` to block write operations (enforced in `AnkiConnectClient`)

### Media Security

The media tools (`storeMediaFile`, `retrieveMediaFile`, `deleteMediaFile`) and `updateNoteFields` audio/picture/video fields validate inputs against prompt-injection and SSRF attacks:

- **File paths** — MIME-type allowlist (media only). Non-media files (SSH keys, creds, shell configs) are rejected.
  - `MEDIA_ALLOWED_TYPES` — extra MIME types (comma-separated)
  - `MEDIA_IMPORT_DIR` — restrict imports to a specific directory
- **URLs** — SSRF guard blocks loopback (127.x), RFC1918 (10/8, 172.16/12, 192.168/16), link-local (169.254.x), and non-HTTP(S) schemes.
  - `MEDIA_ALLOWED_HOSTS` — allowlist specific private hosts (e.g., `192.168.1.50,my-nas`)
- **Filenames** — path-traversal sanitization (`../`, absolute paths stripped).

Validation lives in `src/mcp/utils/media-validation.utils.ts`; callers are `mediaActions/actions/{store,retrieve,delete}MediaFile.action.ts` and `update-note-fields.tool.ts`. Unit coverage in `src/mcp/utils/__tests__/media-validation.utils.spec.ts`, E2E in `test/e2e/media-security.stdio.e2e-spec.ts`. When touching these, always add a test — the recent path-traversal fix (commit f94cfb8) was reported externally.

