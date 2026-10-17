# ankimcp/anki-mcp-server-addon

- 链接：https://github.com/ankimcp/anki-mcp-server-addon
- 作者：ankimcp
- 仓库说明：An Anki addon that implements an MCP server, enabling AI assistants to interact with Anki, the spaced repetition flashcard application.
- 星数：89
- 获取方式：GitHub README + SKILL/说明文件

---

## README

# AnkiMCP Server (Addon)

<div align="center">
  <img src="./docs/images/ankimcp.png" alt="Anki + MCP Integration" width="600" />

  <p><strong>Seamlessly integrate <a href="https://apps.ankiweb.net">Anki</a> with AI assistants through the <a href="https://modelcontextprotocol.io">Model Context Protocol</a></strong></p>
</div>

An Anki addon that exposes your collection to AI assistants via the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/).

## What is this?

AnkiMCP Server runs a local MCP server inside Anki, allowing AI assistants like Claude to interact with your flashcard collection. This enables AI-powered study sessions, card creation, and collection management.

Part of the [ankimcp.ai](https://ankimcp.ai) project.

## Note on First Run

On first run, this addon downloads `pydantic_core` (~2MB) from PyPI. This is required because pydantic_core contains platform-specific binaries (Windows/macOS/Linux) that cannot be bundled in a single addon file.

A second native dependency, `rpds` (from `rpds-py`), is handled the same way — but it is almost never downloaded: Anki already ships `rpds` as a transitive dependency of its own `jsonschema`, so the addon just imports it. The download only kicks in on the rare install where that import fails. Both downloads are cached under Anki's own data folder (outside the addon's own folder, so it survives addon updates cleanly on every OS), falling back to the addon's `_cache/` directory when that location isn't available — so either way they happen once, not on every launch. The old in-folder fallback cache is only ever removed once the outside-the-folder cache has proven itself usable (a successful load from it) and is never touched while a native module is still loaded from it — a failed first attempt (e.g. offline) leaves the old cache untouched rather than destroyed.

## Features

- **Local HTTP server** - Runs on `http://127.0.0.1:3141/` by default
- **Remote tunnel** - Access your collection from anywhere via a public HTTPS URL
- **MCP protocol** - Compatible with any MCP client (Claude Desktop, etc.)
- **Auto-start** - HTTP server starts automatically when Anki opens
- **Tunnel-friendly** - Works with Cloudflare Tunnel, ngrok, or the built-in tunnel (exposing the HTTP server this way also requires extending the [allowed hosts/origins](#allowed-hosts-and-origins-dns-rebinding-protection))
- **DNS-rebinding protection** - The HTTP server validates `Host`/`Origin` headers against a loopback allowlist by default; [extend it](#allowed-hosts-and-origins-dns-rebinding-protection) for tunnel/reverse-proxy exposure
- **Optional API key** - Require an `Authorization: Bearer` token on the HTTP transport via [`http_api_key`](#api-key-optional-http-auth) (AnkiConnect-style; empty = disabled)
- **Toolbar indicator** - A `● AnkiMCP` item in the top toolbar shows tunnel connection state at a glance (opt out via `show_toolbar_indicator`)
- **Diagnostic logging** - Opt-in [`log_to_file`](#diagnostic-file-logging) writes a rotating, secret-redacted log to `user_files/ankimcp.log`, with **Open log folder** / **Copy diagnostics** buttons in settings
- **Field management** - Add, rename, and reposition note-type fields via the `model_field_*` tools (with an opt-in [destructive](#destructive-tools-opt-in) `model_field_remove`)
- **Bulk card stats** - The read-only `cards_stats` tool returns compact per-card scheduling metrics (type/queue/interval/tags/`dueToday`) for a whole deck including subdecks, FSRS-independent — a lean bulk read for analytics
- **GUI review sessions** - Hands-free review in Anki's own reviewer window: `gui_deck_review` opens a deck, `gui_answer_card` presses the answer button for you. [Opt-in](#opt-in-tools), hidden until named in `enabled_opt_in_tools`
- **MCP tool annotations** - Every tool declares a `title`, `readOnlyHint`, `destructiveHint` and `openWorldHint` (plus `idempotentHint` on write tools that are safe to repeat), so clients can show readable names and confirm before data-changing calls
- **Cross-platform** - Works on macOS, Windows, and Linux (x64 and ARM)

## Installation

### From AnkiWeb (recommended)

1. Open Anki and go to *Tools → Add-ons → Get Add-ons...*
2. Enter code: `124672614`
3. Restart Anki

### From GitHub Releases

1. Download `anki_mcp_server.ankiaddon` from [Releases](https://github.com/ankimcp/anki-mcp-server-addon/releases)
2. Double-click to install, or use *Tools → Add-ons → Install from file...*
3. Restart Anki

### NixOS

#### With flakes (recommended)

Add the flake input and use the pre-built package:

```nix
# flake.nix
{
  inputs.anki-mcp.url = "github:ankimcp/anki-mcp-server-addon";

  outputs = { nixpkgs, anki-mcp, ... }: {
    # Option A: Standalone — Anki with the addon pre-installed
    environment.systemPackages = [
      anki-mcp.packages.${system}.default
    ];

    # Option B: Composable with other addons via overlay
    nixpkgs.overlays = [ anki-mcp.overlays.default ];
    environment.systemPackages = [
      (pkgs.anki.withAddons [ pkgs.ankiAddons.anki-mcp-server ])
    ];
  };
}
```

#### Without flakes

```nix
# configuration.nix
{ pkgs, ... }:
let
  python3 = pkgs.python3;

  ankiMcpPythonDeps = python3.withPackages (ps: with ps; [
    mcp pydantic pydantic-settings starlette uvicorn anyio httpx websockets
  ]);

  anki-mcp-server = pkgs.anki-utils.buildAnkiAddon (finalAttrs: {
    pname = "anki-mcp-server";
    version = "0.20.0";
    src = pkgs.fetchFromGitHub {
      owner = "ankimcp";
      repo = "anki-mcp-server-addon";
      rev = "v${finalAttrs.version}";
      hash = ""; # nix will tell you the correct hash on first build
    };
    sourceRoot = "${finalAttrs.src.name}/anki_mcp_server";
  });

  ankiWithMcp = pkgs.anki.withAddons [ anki-mcp-server ];

  ankiWrapped = pkgs.symlinkJoin {
    name = "anki-with-mcp";
    paths = [ ankiWithMcp ];
    nativeBuildInputs = [ pkgs.makeWrapper ];
    postBuild = ''
      wrapProgram $out/bin/anki \
        --prefix PYTHONPATH ':' "${ankiMcpPythonDeps}/${python3.sitePackages}"
    '';
  };
in
{
  environment.systemPackages = [ ankiWrapped ];
}
```

## Usage

The server starts automatically when you open Anki. Check status via *Tools → AnkiMCP Server Settings...*

### Connect with Claude Desktop

Requires [Node.js](https://nodejs.org/) installed. Add to your Claude Desktop config (`~/Library/Application Support/Claude/claude_desktop_config.json` on macOS):

```json
{
  "mcpServers": {
    "anki": {
      "command": "npx",
      "args": ["mcp-remote", "http://127.0.0.1:3141"]
    }
  }
}
```

> **Note:** Claude Desktop doesn't natively support HTTP servers in its JSON config — `mcp-remote` bridges the connection via stdio.

### Connect with Claude Code

```bash
claude mcp add anki --transport http http://127.0.0.1:3141/
```

### Opencode

```bash
opencode mcp add anki --url http://127.0.0.1:3141/
```

### Tunnel (Remote Access)

The built-in tunnel gives your Anki collection a public HTTPS URL, so AI assistants can reach it from anywhere — no port forwarding or reverse proxy needed. The collection is relayed through a WebSocket tunnel server (`wss://tunnel.ankimcp.ai` by default). Requires an [ankimcp.ai](https://ankimcp.ai) account to log in.

**How to connect:**

1. Open *Tools -> AnkiMCP Server Settings...*
2. Click **Connect Tunnel**
3. If not logged in, a login dialog appears — it shows a one-time code; click **Open Browser** and enter that code at the verification URL (OAuth 2.0 device flow)
4. Once connected, a public tunnel URL is displayed (e.g., `https://tunnel.ankimcp.ai/e3439277-9d1e-47a1-b961-d193a4590da0`)
5. Use this URL in your AI client instead of `http://127.0.0.1:3141`

**Using with Claude Desktop:**

Replace the localhost URL with your tunnel URL in the Claude Desktop config:

```json
{
  "mcpServers": {
    "anki": {
      "command": "npx",
      "args": ["mcp-remote", "https://tunnel.ankimcp.ai/<your-tunnel-id>"]
    }
  }
}
```

**Using with Claude Code:**

```bash
claude mcp add anki --transport http https://tunnel.ankimcp.ai/<your-tunnel-id>
```

**Disconnect vs. Logout:**
- **Disconnect** closes the tunnel connection. Credentials stay on disk — next Connect reconnects without re-login.
- **Logout** deletes credentials. Next Connect triggers the login dialog again.

**Tunnel config fields** (for advanced users / self-hosters):
- `tunnel_server_url` — WebSocket URL of the tunnel relay server (default: `wss://tunnel.ankimcp.ai`)
- `tunnel_client_id` — OAuth client identifier (default: `ankimcp-cli`)

Credentials are stored in the addon's own `user_files/credentials.json` (preserved across addon updates). They are not shared with the [AnkiMCP CLI](https://github.com/ankimcp/anki-mcp-cli) — the CLI keeps its own credentials under `~/.ankimcp/`, so you log in to the addon and the CLI independently. The on-disk format is identical between the two.

## Configuration

Edit via Anki's *Tools → Add-ons → AnkiMCP Server → Config*:

```json
{
  "http_enabled": true,
  "http_port": 3141,
  "http_host": "127.0.0.1",
  "http_path": "",
  "http_allowed_hosts": [],
  "http_allowed_origins": [],
  "http_api_key": "",
  "cors_origins": [],
  "cors_expose_headers": ["mcp-protocol-version"],
  "disabled_tools": [],
  "enabled_destructive_tools": [],
  "enabled_opt_in_tools": [],
  "max_notes_per_batch": 100,
  "tunnel_server_url": "wss://tunnel.ankimcp.ai",
  "tunnel_client_id": "ankimcp-cli",
  "media_import_dir": "",
  "media_allowed_types": [],
  "media_allowed_hosts": [],
  "show_settings_menu_item": true,
  "show_toolbar_indicator": true,
  "show_sync_tooltip": true,
  "log_to_file": false
}
```

### HTTP Server Toggle

The `http_enabled` setting controls whether the local HTTP server runs. When set to `false`, the HTTP server won't start — only the tunnel transport is available. Default is `true`.

```json
{
  "http_enabled": false
}
```

This is useful if you only use the tunnel and don't want a local HTTP server listening.

### Tools Menu Item

The *AnkiMCP Server Settings…* entry in Anki's *Tools* menu is shown by default. Set `show_settings_menu_item` to `false` to hide it (takes effect after an Anki restart).

```json
{
  "show_settings_menu_item": false
}
```

Note: if you hide the menu item **and** the toolbar indicator, there's no in-app way left to open the settings dialog — you can still edit the config via *Tools → Add-ons → AnkiMCP Server → Config*.

### Toolbar Status Indicator

A persistent `● AnkiMCP` item in Anki's top toolbar shows tunnel connection state (grey = off, amber = connecting, green = connected); clicking it opens the settings dialog. It's shown by default. Set `show_toolbar_indicator` to `false` to hide it (takes effect after an Anki restart).

```json
{
  "show_toolbar_indicator": false
}
```

### Sync Tooltip

When an AI client triggers a sync, the addon shows a brief, non-modal tooltip in Anki's UI as the sync starts and finishes (e.g. `AnkiMCP: syncing…`, `AnkiMCP: sync complete`). This is the only visual cue for these otherwise-silent background syncs. It's shown by default. Set `show_sync_tooltip` to `false` to suppress it.

```json
{
  "show_sync_tooltip": false
}
```

### Diagnostic File Logging

Set `log_to_file` to `true` to write a rotating log to `user_files/ankimcp.log` (~1 MB per file, 3 backups). It's **off by default**. When enabled, the addon records a startup diagnostics snapshot (addon/Anki/Qt/Python versions plus the live provenance of shared libraries like `pydantic`, `mcp`, `protobuf`, etc.), which is the key data for diagnosing cross-add-on conflicts. Secrets — the `http_api_key`, OAuth tokens, and any `Bearer` token — are **redacted** before anything is written to disk.

```json
{
  "log_to_file": true
}
```

The settings dialog (*Tools → AnkiMCP Server Settings…*) has an **Open log folder** button and a **Copy diagnostics** button (the same snapshot, formatted for pasting into a forum post). Takes effect after an Anki restart.

### Disabling Tools

Hide specific tools from AI clients to reduce token usage:

```json
{
  "disabled_tools": [
    "sync",
    "card_bury",
    "card_unbury"
  ]
}
```

Each entry is a tool name. Disabled tools are removed from the MCP schema entirely — AI clients never see them. Typos in tool names will produce console warnings.

#### Upgrading to 0.40.0

0.40.0 split the four multi-action tools into one tool per action: `card_management` → `card_*`, `tag_management` → `tag_*`, `filtered_deck` → `filtered_deck_*`, `model_fields` → `model_field_*` (see [Available Tools](#available-tools)). Old config entries keep working, with a deprecation warning naming the replacement:

- `"card_management:bury"` behaves exactly like `"card_bury"` — in `disabled_tools` and in both allow-lists below (`"model_fields:remove"` still opts in `model_field_remove`)
- A bare `"card_management"` in `disabled_tools` disables every `card_*` tool
- A bare old name in `enabled_destructive_tools` / `enabled_opt_in_tools` opts in nothing, as before

Only these old names are accepted in `"tool:action"` form; any other `"tool:action"` entry matches nothing and produces a warning. The deprecation warning appears on every profile open (after the server has started — it never delays it) until you switch to the new names.

The aliases cover config only. On the client side the old tools are gone: `tools/list` no longer has `card_management` & co., and the new tools take flat arguments — no `params` wrapper, no `action` field. If your AI client saved per-tool approvals, or you have scripts calling the old tools, re-approve the new tools and update the calls.

### Destructive Tools (Opt-In)

Tools classified as destructive (high-risk operations) are **hidden from AI clients by default**. To expose them, add them to the `enabled_destructive_tools` allow-list:

```json
{
  "enabled_destructive_tools": [
    "change_note_type",
    "model_field_remove"
  ]
}
```

- Each entry is the exact name of a destructive tool
- `disabled_tools` still applies on top — an opted-in tool can still be disabled
- Entries that don't match anything, or match a non-destructive tool, produce console warnings

This is server-side enforcement: until opted in, destructive tools are absent from the MCP schema, so even a misbehaving client cannot call them. Currently shipped destructive tools: `change_note_type` (rewrites every selected note's field layout) and `model_field_remove` (permanently deletes a field and its content on every note of the type).

### Opt-In Tools

Some tools ship **hidden from AI clients by default** for reasons other than "destructive" (e.g. new/experimental surface area). Expose them via the `enabled_opt_in_tools` allow-list, same syntax as `enabled_destructive_tools`:

```json
{
  "enabled_opt_in_tools": [
    "gui_answer_card",
    "gui_deck_review"
  ]
}
```

- Each entry is the exact name of an opt-in tool
- `disabled_tools` still applies on top — an opted-in tool can still be disabled
- Entries that don't match anything, or match a non-opt-in tool, produce console warnings

Currently shipped opt-in entries: `gui_deck_review` and `gui_answer_card` — the GUI hands-free review-session tools.

### Custom Path

Set `http_path` to serve the MCP endpoint under a custom path. Useful when exposing Anki via a tunnel (Cloudflare, ngrok) to avoid a fully open endpoint:

```json
{
  "http_path": "my-secret-path"
}
```

The server will be accessible at `http://localhost:3141/my-secret-path/` instead of the root. Leave empty for default behavior.

> **Note:** A custom path alone is not enough to expose the HTTP server through a tunnel or reverse proxy. You must also populate `http_allowed_hosts`/`http_allowed_origins`, or requests are rejected (`421` for a non-loopback `Host`, `403` for a non-loopback `Origin`) — see [Allowed Hosts and Origins (DNS-Rebinding Protection)](#allowed-hosts-and-origins-dns-rebinding-protection).

## Security

The local HTTP server accepts requests only from loopback `Host`/`Origin` values by default, so **ordinary local use needs no setup** — localhost clients work out of the box. The sections below cover the available hardening layers (DNS-rebinding allowlist, optional API key, CORS, and media-import validation) for when you expose the server beyond your machine.

**Upgrading from ≤ 0.20.0:** if you reach the server through a tunnel, reverse proxy, or by binding to `0.0.0.0`, requests now arrive with a non-loopback `Host` and are rejected with `421` until you allowlist that host — see [Allowed Hosts and Origins (DNS-Rebinding Protection)](#allowed-hosts-and-origins-dns-rebinding-protection). (Browser clients additionally need their `Origin` allowlisted, otherwise `403`.) Plain localhost setups are unaffected.

### Allowed Hosts and Origins (DNS-Rebinding Protection)

The HTTP server enables DNS-rebinding protection with a built-in loopback allowlist (copied verbatim from the MCP SDK's own default):

- Hosts: `127.0.0.1:*`, `localhost:*`, `[::1]:*`
- Origins: `http://127.0.0.1:*`, `http://localhost:*`, `http://[::1]:*`

Ordinary localhost clients therefore work out of the box. Two details of these defaults are worth knowing:

- The `:*` patterns match a **host with a port** (`localhost:3141` ✓). A port-less `Host` header — which browsers and clients send only when the server runs on port 80 — does not match, so a non-default `"http_port": 80` needs `"localhost"`/`"127.0.0.1"` added to `http_allowed_hosts` explicitly.
- The default origins are **`http://`-only**. An `https://localhost` origin is not covered and must be added to `http_allowed_origins`. (Requests with no `Origin` header at all — the normal case for non-browser MCP clients — always pass.)

If you expose the HTTP server through a tunnel or reverse proxy (e.g. ngrok, Cloudflare), requests arrive with a non-loopback `Host` (rejected with `421`) — and, for browser clients, a non-loopback `Origin` (rejected with `403`) — unless you extend the allowlist:

```json
{
  "http_allowed_hosts": ["myapp.ngrok.io", "myapp.ngrok.io:443"],
  "http_allowed_origins": ["https://myapp.example"]
}
```

- `http_allowed_hosts` — `Host`-header values **without** a scheme (e.g. `"myapp.ngrok.io"` or `"myapp.ngrok.io:443"`)
- `http_allowed_origins` — full origins **with** a scheme (e.g. `"https://myapp.example"`)

Both lists are appended to the built-in loopback defaults (the defaults are not replaced). Changing these requires an Anki restart, consistent with the other `http_*` settings.

> DNS-rebinding vulnerability reported by [avishaigo-commits](https://github.com/avishaigo-commits).

### API Key (Optional HTTP Auth)

`http_api_key` adds an optional shared-secret auth layer on top of the HTTP transport (AnkiConnect-style). It is **empty by default**, which disables the layer and leaves the default behavior unchanged. When set to a non-empty value, **every** HTTP request must send an `Authorization: Bearer <key>` header matching that value, or it is rejected with `403`:

```json
{
  "http_api_key": "a-long-random-secret-key"
}
```

Configure your client to send the header. With Claude Code:

```bash
claude mcp add anki --transport http http://127.0.0.1:3141/ --header "Authorization: Bearer a-long-random-secret-key"
```

With `mcp-remote` (e.g. Claude Desktop):

```json
{
  "mcpServers": {
    "anki": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "http://127.0.0.1:3141",
        "--header",
        "Authorization: Bearer a-long-random-secret-key"
      ]
    }
  }
}
```

Notes:

- **HTTP-only.** The key applies only to the local HTTP transport. The tunnel does its own OAuth login and is unaffected by `http_api_key`.
- **Complementary, not a replacement.** It sits alongside DNS-rebinding protection (Allowed Hosts and Origins) — it does not replace it. Both layers apply independently.
- **Pairs naturally with `http_path` + `http_allowed_hosts`** when exposing the HTTP server through a tunnel or reverse proxy: a secret path obscures the endpoint, the allowlist permits the proxy host, and the API key authenticates each request.
- Use a long, random key (at least 16 characters). Leading/trailing whitespace is stripped from the presented token, so a configured key with surrounding whitespace will never match.
- Changing this requires an Anki restart, consistent with the other `http_*` settings.

### CORS Configuration

To allow browser-based MCP clients (like web-hosted MCP Inspector), add allowed origins:

```json
{
  "cors_origins": ["https://inspector.example.com", "http://localhost:5173"]
}
```

Use `["*"]` to allow all origins (not recommended for production).

> **Note:** A browser origin allowed via `cors_origins` must **also** be added to `http_allowed_origins`. CORS and the DNS-rebinding allowlist are separate layers: even with CORS configured, a non-loopback `Origin` is rejected with `403` by DNS-rebinding protection unless it is in `http_allowed_origins`.

The `cors_expose_headers` setting controls which response headers browsers can read. The default (`mcp-protocol-version`) lets browser-based MCP clients negotiate the protocol version. Since v0.16.0 the server runs in stateless mode, so `mcp-session-id` is no longer emitted and no longer needs to be exposed.

### Media Security

> Thanks to **[Hideaki Takahashi](https://github.com/Koukyosyumei)** (Columbia University) for responsibly disclosing the media path traversal vulnerability.

The `store_media_file` tool validates all inputs to prevent path traversal and SSRF attacks:

- **File paths** are restricted to media files only (images, audio, video) via MIME type checking
- **URLs** must use `http://` or `https://` and cannot target private/internal networks
- **Filenames** are sanitized to remove path traversal sequences

Optional hardening via config:

```json
{
  "media_import_dir": "/Users/me/anki-media",
  "media_allowed_types": ["application/pdf"],
  "media_allowed_hosts": ["192.168.1.50", "my-nas.local"]
}
```

- `media_import_dir` — restrict file path imports to this directory tree (empty = no restriction)
- `media_allowed_types` — allow additional MIME types beyond image/audio/video
- `media_allowed_hosts` — allow specific hosts to bypass private network blocking

## Available Tools

Every tool parameter carries a short `description` in the MCP input schema (since 0.29.0), so clients that show or feed the schema to the model get argument shapes without trial and error. Nested objects (e.g. `tag_batch` operations, `filtered_deck_upsert` search terms) are described on their Pydantic models and appear under `$defs`.

Every tool also carries MCP annotations (since 0.31.0): a human-readable `title`, `readOnlyHint` (true for tools that never modify the collection), `destructiveHint` (false for read-only tools and for writes that are reversible and lose no data: `add_note`, `add_notes`, `create_deck`, `create_model`, `store_media_file`, `tag_add`, `card_bury`, `card_unbury`, `card_suspend`, `card_unsuspend`, `card_set_flag`, `card_change_deck`, `filtered_deck_empty` and `filtered_deck_rebuild`; true for every other write tool, i.e. those that delete, overwrite or irreversibly change data, or force a full AnkiWeb sync), `idempotentHint` (since 0.32.0; true only for write tools where repeating the same call has no further effect: `create_deck`, `delete_notes`, `delete_media_file`, `set_fsrs_params`, `card_change_deck`, `card_bury`, `card_unbury`, `card_suspend`, `card_unsuspend`, `card_set_flag`, every `tag_*` write tool, `filtered_deck_empty`, `filtered_deck_delete` and every `model_field_*` write tool; omitted on every other tool), and `openWorldHint` (true only for `sync`, which talks to AnkiWeb, and `store_media_file`, which can fetch URLs).

**Upgrading from ≤ 0.27.x:** `get_due_cards` no longer returns `back` unless you pass `include_answer=true`, and `front` is now the rendered question HTML rather than the raw field. Clients that read `back` from this tool need the flag.

### Essential Tools

| Tool | Description |
|------|-------------|
| `sync` | Synchronize collection with AnkiWeb (asynchronous job: `sync()` starts a sync, `sync(job_id)` polls its status, `sync(job_id, resolve=...)` resolves a full-sync conflict) |
| `list_decks` | List all decks in the collection |
| `create_deck` | Create a new deck |
| `find_notes` | Search for notes using Anki's search syntax. `include_first_field=true` adds a `noteLabels` array (`{noteId, firstField, truncated, fullLength}`) so you can search and label notes in one call |
| `notes_info` | Get detailed information about notes. `excerpt_chars` caps every field value at that many characters, marking each with `truncated`/`fullLength` — a cheap way to survey many notes |
| `add_note` | Add a new note to a deck |
| `add_notes` | Batch-add up to `max_notes_per_batch` notes (default 100) sharing the same deck and model. Uses Anki's native batch API for atomic undo. Supports partial success — individual failures don't affect others |
| `card_reposition` | Set the learning order of new cards (only new cards are affected) |
| `card_change_deck` | Move cards to another deck, creating it if needed |
| `card_bury` / `card_unbury` | Hide cards until tomorrow / restore every buried card in a deck |
| `card_suspend` / `card_unsuspend` | Exclude cards from review indefinitely / restore them |
| `card_set_flag` | Set or remove a color flag (0-7) |
| `card_set_due_date` | Reschedule cards with the days DSL (`0`, `5`, `5-7`, `5!`) |
| `card_forget` | Reset cards to new |
| `tag_add` / `tag_remove` | Bulk add/remove tags on notes |
| `tag_replace` | Swap one tag for another on notes |
| `tag_list` | List all tags, or scoped to a deck via the optional `deck` param — distinct tags on notes with a card in that deck, subdecks included |
| `tag_clear_unused` | Remove orphan tags |
| `tag_batch` | Apply multiple add/remove tag operations in one call, with partial success |
| `filtered_deck_upsert` | Create or modify a filtered deck from 1-2 search terms (Anki's hard limit) |
| `filtered_deck_rebuild` | Repopulate a filtered deck |
| `filtered_deck_empty` | Return a filtered deck's cards to their home decks |
| `filtered_deck_delete` | Return a filtered deck's cards, then remove the deck |
| `filtered_deck_get_info` | Read-only inspection of up to 50 deck IDs per call — returns search terms, limit, order, reschedule flag and card count; non-filtered decks come back with `is_filtered=false`, unknown IDs are skipped and counted in `not_found` |
| `update_note_fields` | Update fields of existing notes. Two modes: full replace, or patch via `old_str`/`new_str` (find-and-replace within a field; must match exactly once or nothing is written) |
| `update_notes` | Batch-update fields of multiple notes in one atomic undo step (single backend call). Validates every entry first; supports partial success up to `max_notes_per_batch` |
| `delete_notes` | Delete notes from the collection |
| `get_due_cards` | Get next due card for review (supports `skip_images`/`skip_audio` for voice mode). Returns the rendered question only; the answer is omitted unless `include_answer=true` |
| `cards_stats` | Bulk per-card scheduling stats for a deck (incl. subdecks): type/queue/interval/tags/dueToday, paginated. FSRS-independent, compact payload for analytics |
| `present_card` | Get card content for review |
| `rate_card` | Rate a card after review (Again/Hard/Good/Easy) |
| `model_names` | List available note types |
| `model_field_names` | Get field names and descriptions for a note type |
| `model_styling` | Get CSS styling for a note type. `include_latex=true` also returns the LaTeX preamble (`latex_pre`, `latex_post`, `latex_svg`) |
| `update_model_styling` | Update CSS styling for a note type — full replace, or patch via `old_str`/`new_str` (must match exactly once). Can also write the LaTeX preamble (`latex_pre`/`latex_post`/`latex_svg`) |
| `model_templates` | Read the Front/Back HTML templates for each card type in a note type |
| `update_model_templates` | Update Front/Back template HTML — full replace, or patch via `old_str`/`new_str` (must match exactly once). Rejects unrecognized keys (case-sensitive) and unknown template names up front, applying all edits atomically — a failed call leaves the model unchanged |
| `model_field_add` / `model_field_rename` / `model_field_reposition` | Manage fields on an existing note type: add (optionally at a 0-based index), rename (preserves content; card templates are **not** auto-updated), reposition (reorder). Add and reposition change field ordinals and force a one-way full sync; a pure rename does not. Every result carries `will_force_full_sync`, the collection's actual (sticky, collection-wide) state after the write |
| `model_field_remove` | Delete a field and its content from every note of the type. [Destructive](#destructive-tools-opt-in) — hidden unless opted in via `enabled_destructive_tools`. Forces a one-way full sync |
| `create_model` | Create a new note type |
| `change_note_type` | Move existing notes to a different note type, remapping fields by name (`{old field: new field or null}`). [Destructive](#destructive-tools-opt-in) — hidden unless opted in via `enabled_destructive_tools`. Two-step flow: `dry_run=true` returns the resolved plan (mapping, dropped fields, cards removed), then the same call with `dry_run=false` **and** `confirm=true` applies it. All notes must share one source note type |
| `store_media_file` | Store a media file (image/audio) via base64, file path, or URL. File paths are validated against a media-type allowlist; URLs are checked for SSRF |
| `get_media_files_names` | List media files matching a pattern |
| `delete_media_file` | Move a media file to Anki's trash (recoverable via Check Media) |

### FSRS Tools

| Tool | Description |
|------|-------------|
| `get_fsrs_params` | Get FSRS scheduler parameters for deck presets |
| `set_fsrs_params` | Update FSRS parameters (weights, desired retention, max interval) |
| `get_card_memory_state` | Get FSRS memory state (stability, difficulty, retrievability) for cards |
| `optimize_fsrs_params` | Run FSRS parameter optimization using Anki's built-in optimizer |

### GUI Tools

These tools interact with Anki's user interface:

| Tool | Description |
|------|-------------|
| `gui_browse` | Open the card browser with a search query |
| `gui_add_cards` | Open the Add Cards dialog |
| `gui_edit_note` | Open the note editor for a specific note |
| `gui_current_card` | Get info about the currently displayed card |
| `gui_show_question` | Show the question side of current card |
| `gui_show_answer` | Show the answer side of current card |
| `gui_select_card` | Select a specific card in the reviewer |
| `gui_deck_browser` | Navigate to deck browser |
| `gui_undo` | Undo the last operation |
| `gui_deck_review` | Open a deck in Anki's own reviewer window. [Opt-in](#opt-in-tools) — hidden unless opted in via `enabled_opt_in_tools` |
| `gui_answer_card` | Press an answer button on the card shown in the reviewer, hands-free rating. [Opt-in](#opt-in-tools) — hidden unless opted in via `enabled_opt_in_tools` |

`gui_current_card` no longer returns the note's `answer`/`fields` by default -- pass `include_answer=true` to get them.

### Resources

| Resource | URI | Description |
|----------|-----|-------------|
| `system_info` | `anki://system-info` | Anki version, profile, and scheduler info |
| `query_syntax` | `anki://query-syntax` | Anki search query syntax reference |
| `schema` | `anki://schema` | Data model documentation (entities, fields, relationships) |
| `stats_today` | `anki://stats/today` | Today's study statistics |
| `stats_forecast` | `anki://stats/forecast` | 30-day review forecast |
| `stats_collection` | `anki://stats/collection` | Overall collection statistics |
| `fsrs_config` | `anki://fsrs/config` | FSRS configuration summary and parameters |

### Prompts

| Prompt | Description |
|--------|-------------|
| `review_session` | Guided review session workflow. Args: `deck_name` (default `Default`), `card_limit` (default 20), `review_style` — `interactive`, `quick`, `voice`, or `gui` |
| `twenty_rules` | Dr. Piotr Woźniak's *Twenty Rules of Formulating Knowledge* (SuperMemo), as card-authoring guidance for the assistant. No arguments |

## Requirements

- **Anki 25.07 or later** (ships Python 3.13)
- Anki 25.02 and earlier ship Python 3.9, which is **not supported** — the MCP SDK requires Python 3.10+ ([#8](https://github.com/ankimcp/anki-mcp-server-addon/issues/8))

## Architecture

The addon runs an MCP server in a background thread with two independent transports: local HTTP (FastMCP + uvicorn) and remote tunnel (WebSocket relay with in-memory transport). Both share the same FastMCP server instance. All Anki operations are bridged to the main Qt thread via a queue system, following the same proven pattern as AnkiConnect.

For details, see [Anki Add-on Development Documentation](https://addon-docs.ankiweb.net/).

## Development

### Running E2E Tests

E2E tests run against a real Anki instance in Docker using [headless-anki](https://github.com/ankimcp/headless-anki).

```bash
# Install test dependencies
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt

# Build the addon
./package.sh

# Start Anki container
cd .docker && docker compose up -d && cd ..

# Run tests (waits for server automatically)
pytest tests/e2e/ -v

# Stop container
cd .docker && docker compose down
```

Or use the Makefile shortcuts:
```bash
make e2e        # Build, start container, run tests, stop
make e2e-up     # Just start container
make e2e-test   # Just run tests
make e2e-down   # Just stop container
```

### CI

E2E tests run automatically on push to any branch and on PRs to `main`. See `.github/workflows/e2e.yml`.

## License

AGPL-3.0-or-later

## Links

- [ankimcp.ai](https://ankimcp.ai) - Project homepage
- [MCP Protocol](https://modelcontextprotocol.io/) - Model Context Protocol specification
- [Anki Add-on Docs](https://addon-docs.ankiweb.net/) - Official Anki addon development documentation


## 文件 CLAUDE.md

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Quick Reference

```bash
./package.sh                    # Build .ankiaddon package
make e2e                        # Full E2E cycle: regular (port 3141) + filtered (port 3142)
make e2e-full                   # Regular tests only: build → Docker → test → teardown
make e2e-up                     # Build addon + start headless Anki container (port 3141)
make e2e-test                   # Run E2E tests (excludes test_tool_filtering_e2e.py and test_gui_review_session.py)
make e2e-down                   # Stop container
make e2e-debug                  # Start container and keep it running (VNC at localhost:5900)
make e2e-logs                   # Follow container logs (-f, interactive only — never in CI)
make e2e-logs-dump              # Dump last 2000 lines of container logs and exit (CI-safe)
make e2e-filtered               # Filtered tests only: build → Docker (port 3142) → test → teardown
make e2e-filtered-up            # Start filtered container (docker-compose.filtered.yml)
make e2e-filtered-test          # Run test_tool_filtering_e2e.py + test_model_fields_remove.py + test_gui_review_session.py against port 3142
make e2e-filtered-down          # Stop filtered container
make e2e-filtered-logs-dump     # Dump last 2000 lines of filtered container logs and exit (CI-safe)
make e2e INSPECTOR_VERSION=latest       # Same cycle against the newest MCP Inspector (nightly canary does this)
pytest tests/e2e/ -v --ignore=tests/e2e/test_tool_filtering_e2e.py --ignore=tests/e2e/test_gui_review_session.py  # Run tests directly
pytest tests/e2e/test_note_tools.py -v  # Run a single test file
pytest tests/unit/ -v                   # Run unit tests (tunnel in-memory transport)
```

## Project Overview

Anki addon that runs an MCP server inside Anki, exposing collection operations to AI assistants. Supports two independent transports: local HTTP (FastMCP + uvicorn) and remote tunnel (WebSocket relay to a public HTTPS URL).

- **Package**: `anki_mcp_server.ankiaddon`
- **Default Port**: 3141 (HTTP)
- **License**: AGPL-3.0-or-later

## Architecture

### Threading Model

```
┌──────────────────┐    ┌───────────────────────────────┐
│  AI Client (HTTP)│    │  AI Client (remote, via tunnel)│
└────────┬─────────┘    └──────────────┬────────────────┘
         │                             │
         ▼                             ▼
┌─────────────────────────────────────────────────────────┐
│    Background Thread (single asyncio event loop)        │
│                                                         │
│  HTTP path:                  Tunnel path:               │
│  uvicorn → StreamableHTTP    WebSocket → InMemoryTransport│
│       ↘                           ↙                     │
│         Server.run() (shared FastMCP)                   │
│         Tool handlers bridge to main thread              │
└───────────────────────┬─────────────────────────────────┘
                        │
                        │ queue.Queue (thread-safe)
                        ▼
┌─────────────────────────────────────────┐
│        QueueBridge                      │
│  - request_queue                        │
│  - response_queue                       │
└───────────────┬─────────────────────────┘
                │
                ▼
┌─────────────────────────────────────────┐
│     Qt Main Thread                      │
│  - Event-driven drain (run_on_main)     │
│  - RequestProcessor                     │
│  - Access to mw.col (safe here)         │
└─────────────────────────────────────────┘
```

**Key Principle**: Never access `mw.col` from background threads. All Anki operations must go through the queue bridge to execute on the main Qt thread.

Both HTTP and tunnel transports share the same `Server` object (same handlers, same tools). Each runs its own `Server.run()` with separate streams and session state. Either can be enabled/disabled independently.

A tool handler that reaches `mw.taskman.run_in_background` (e.g. via an async CollectionOp) can trigger a nested `RequestProcessor` drain mid-handler: `run_in_background`, when called from the main thread, synchronously flushes any `run_on_main` closures already queued before it returns — including a drain closure for a second MCP request that arrived while the first was still being handled. A `_draining` re-entrancy guard makes that nested drain call a safe no-op so the outer drain loop handles the queued request instead — see `request_processor.py`'s `_process_pending()` docstring for the full mechanics.

### Core Files

```
anki_mcp_server/
├── __init__.py              # Entry point, vendor path setup, lifecycle hooks
├── connection_manager.py    # Manages MCP server + tunnel lifecycle
├── config.py                # Configuration from Anki's addon config
├── credentials.py           # OAuth credentials file I/O (user_files/credentials.json)
├── mcp_server.py            # FastMCP server in background thread (HTTP via uvicorn)
├── queue_bridge.py          # Thread-safe request/response queue
├── request_processor.py     # Main thread handler dispatcher
├── handler_registry.py      # Maps handler names to functions
├── handler_wrappers.py      # Shared wrappers: _error_handler, _require_col, HandlerError
├── tool_decorator.py        # @Tool decorator implementation
├── resource_decorator.py    # @Resource decorator implementation
├── prompt_decorator.py      # @Prompt decorator implementation
├── dependency_loader.py     # Runtime pydantic_core download from PyPI
├── native_cache_cleanup.py  # Relocate/clean the out-of-folder native cache on uninstall + update
├── media_validators.py      # Path traversal / SSRF guards for media tools
├── tunnel/
│   ├── __init__.py              # Package marker
│   ├── protocol.py              # Close codes, message types, constants (pure data, no I/O)
│   ├── auth.py                  # OAuth 2.0 Device Flow client (async HTTP via httpx)
│   ├── client.py                # Single WebSocket connection lifecycle (no retry)
│   ├── reconnect.py             # Retry/backoff wrapper around client
│   ├── in_memory_transport.py   # Feeds JSON-RPC into Server.run() via anyio streams
│   ├── log.py                   # Thread-safe ring buffer with Qt signal
│   └── ui/
│       ├── login_dialog.py      # Qt device flow dialog (user code + browser button)
│       ├── settings_section.py  # Tunnel status/controls in settings dialog
│       └── toolbar_indicator.py # Persistent "● AnkiMCP" dot in Anki's top toolbar
└── primitives/
    ├── tools.py             # Triggers auto-discovery of tool modules
    ├── resources.py         # Triggers auto-discovery of resource modules
    ├── prompts.py           # Explicit imports of prompt modules (no auto-discovery)
    ├── essential/
    │   ├── tools/           # Core tools: sync, notes, decks, models, media, FSRS, cards
    │   │   ├── *_tool.py         # Single-file tools (auto-discovered)
    │   │   ├── _fsrs_helpers.py  # _ prefix = helper (imported, registers no tool)
    │   │   ├── card_management/  # Domain folder: card_* tools (card_bury, card_forget, ...)
    │   │   │   ├── __init__.py          # Imports every card_*_tool module
    │   │   │   ├── card_bury_tool.py    # One @Tool per file, flat params
    │   │   │   └── actions/             # Shared impls (bury_impl, ...)
    │   │   ├── tag_management/  # Domain folder: tag_* tools
    │   │   │   ├── __init__.py
    │   │   │   ├── tag_add_tool.py ...
    │   │   │   └── actions/
    │   │   ├── filtered_deck/   # Domain folder: filtered_deck_* tools
    │   │   │   ├── __init__.py
    │   │   │   ├── filtered_deck_upsert_tool.py ...
    │   │   │   └── actions/
    │   │   └── model_fields/    # Domain folder: model_field_* tools
    │   │       ├── __init__.py
    │   │       ├── model_field_add_tool.py ...
    │   │       └── actions/
    │   ├── resources/       # system_info, query_syntax, schema, stats, fsrs_config
    │   └── prompts/         # review_session, twenty_rules
    └── gui/tools/           # UI tools: browse, add_cards, edit_note, etc.
```

**Vendored Dependencies**: Located in `vendor/shared/`. The `__init__.py` prepends vendor path to `sys.path` at startup. On load, `_check_vendor_conflicts()` warns if any vendored packages (mcp, pydantic, starlette, uvicorn, etc.) are already in `sys.modules` from other addons — helps debug compatibility issues.

**Build (`package.sh`)**: Downloads wheels pinned to `--python-version 313` (Anki 25.07's Python). Deliberately **excludes `pydantic_core`** from the bundle — it has platform-specific binaries and is instead lazy-loaded at runtime via `dependency_loader.py`. If modifying the build, keep this exclusion intact.

**Keeping vendor lists in sync**: `requirements.txt` is the **vendoring source of truth** — `package.sh` runs `pip download -r requirements.txt`, so its top-level entries (plus transitive deps) are exactly what gets bundled. The `mcp>=1.27.0,<2` ceiling there pins the addon to the v1 MCP SDK (v2 is a breaking rewrite). When adding or removing a vendored dependency, update **both** `requirements.txt` (controls what gets downloaded/bundled) **and** `_VENDOR_PACKAGES` in `__init__.py` (controls conflict detection at startup). They must stay in sync.

### Decorator Patterns

All MCP primitives use decorator-based registration. At import time, decorators automatically:
1. Wrap functions with error handling and collection checks
2. Register handlers for main-thread dispatch
3. Store metadata for MCP registration at server startup

#### @Tool Decorator

```python
# primitives/essential/tools/my_tool.py
from ....tool_decorator import Tool
from ....handler_wrappers import HandlerError

@Tool(
    "my_tool",                    # Tool name exposed to MCP clients
    "Description for AI",         # Shown to AI to understand usage
    title="My Tool",              # Required: human-readable title shown by MCP clients
    write=True,                   # Set True for operations that modify collection
)
def my_tool(arg: str) -> dict[str, Any]:
    from aqt import mw
    # Runs on Qt main thread - safe to access mw.col
    if not arg:
        raise HandlerError("Invalid arg", hint="Provide a non-empty string")
    return {"status": "success"}
```

Options:
- `title="..."` (**required**, keyword-only): Human-readable title, Title Case (`"Add Note"`, `"Get FSRS Parameters"`). Empty/whitespace → `ValueError` at import time. Sent both as the Tool's top-level `title` and as `ToolAnnotations.title` so old and new clients see it.
- `write=True`: Marks the tool as mutating the collection. Drives the MCP `readOnlyHint` (`readOnlyHint = not write`) — so a tool that mutates the collection must be `write=True`; if an immediate `mw.reset()` would be wrong (it refreshes the UI itself, like `gui_undo`/`gui_answer_card`, or only starts a background job, like `sync`), add `refresh_ui=False`. It is also the `destructive` precondition, and gates `_write_lock`, which — when `refresh_ui` is also true — calls `mw.reset()` after the handler runs, on success or error, so open deck browser/overview/reviewer screens refresh (`maybeReset` is an obsolete no-op in current Anki; `requireReset` prints a deprecation notice plus a full stack trace before calling `mw.reset()` anyway, so neither is used here)
- `refresh_ui=True` (default): Only meaningful when `write=True`. Set `False` for a tool that already refreshes Anki's UI itself (e.g. `gui_answer_card`, whose reviewer op is its own async `CollectionOp`) — an extra `mw.reset()` there would race it.
- `require_col=True` (default): Checks collection is open before running
- `destructive=True`: Hides the tool from MCP clients unless the operator opts in via `enabled_destructive_tools` config (see "Tool Filtering"). Requires `write=True` — `ValueError` at import time otherwise.
- `opt_in=True`: Hides the tool from MCP clients unless the operator opts in via `enabled_opt_in_tools` config (see "Tool Filtering"). Does not require `write=True` — unlike `destructive`, this is for tools that are opt-in for reasons other than being dangerous.
- `destructive_hint=None` (default): The MCP `destructiveHint`. For `write=True` tools `None` resolves to `True` — conservative. Set `False` only when the write is reversible and loses no data (`add_note`, `add_notes`, `create_deck`, `create_model`, `store_media_file`, `tag_add`, `card_bury`, `card_unbury`, `card_suspend`, `card_unsuspend`, `card_set_flag`, `card_change_deck`, `filtered_deck_empty`, `filtered_deck_rebuild`). Leave it `True` when the tool deletes, overwrites or irreversibly changes data, or forces a full AnkiWeb sync (a schema change overwrites the other devices) (`model_field_add` / `_reposition` / `_remove`; `model_field_rename` doesn't dirty the schema but is kept `True` too). Passing any value on a `write=False` tool is a `ValueError`; read-only tools always send `destructiveHint: false` on the wire (the registry still stores `None` for them), so every tool carries explicit boolean `readOnlyHint`, `destructiveHint` and `openWorldHint` — plugin-directory scanners (e.g. OpenAI's) flag tools missing any of the three.
- `idempotent_hint=None` (default): The MCP `idempotentHint`. `None` omits it on the wire (MCP then assumes `False`). Set `True` only on write tools where repeating the same call with the same arguments has no further effect (`create_deck`, `delete_notes`, `delete_media_file`, `set_fsrs_params`, `card_change_deck`, `card_bury`, `card_unbury`, `card_suspend`, `card_unsuspend`, `card_set_flag`, `tag_add`, `tag_remove`, `tag_replace`, `tag_clear_unused`, `tag_batch`, `filtered_deck_empty`, `filtered_deck_delete`, and the four `model_field_*` tools). A repeat call that fails with no state change (e.g. `filtered_deck_delete` on a deck that's already gone) still counts as idempotent. Not on tools with a random or position-dependent result (`card_reposition`, `card_set_due_date`, `card_forget`, `filtered_deck_upsert`, `filtered_deck_rebuild`), nor on the `old_str`/`new_str` patch-mode tools (`update_note_fields`, `update_model_styling`, `update_model_templates`): a repeat patch call can re-apply the edit. Passing any value on a `write=False` tool is a `ValueError`; read-only tools omit `idempotentHint` on the wire.
- `open_world_hint=False` (default): The MCP `openWorldHint`. MCP's own default is `True`, which is wrong for a local-collection server, so it's always sent explicitly. Only `sync` (AnkiWeb) and `store_media_file` (URL fetches) set `True`.

**`destructive` vs `destructive_hint`** — separate concepts, don't conflate them. `destructive=True` is an operator-facing visibility gate (hidden unless opted in via `enabled_destructive_tools`) reserved for a few high-risk primitives. `destructive_hint` is the client-facing MCP annotation covering any write that deletes, overwrites, irreversibly changes data or forces a full sync — reversible, no-data-loss writes get `False`. `destructive=True` with `destructive_hint=False` is a contradiction → `ValueError`.

#### @Resource Decorator

```python
# primitives/essential/resources/my_resource.py
from ....resource_decorator import Resource

@Resource(
    "anki://deck/{deck_id}/stats",  # URI with template variables
    "Get statistics for a deck",
    name="deck_stats",               # Handler name (required, explicit)
    title="Deck Statistics",         # Human-readable title (optional)
)
def deck_stats(deck_id: str) -> dict[str, Any]:
    # deck_id extracted from URI template
    from aqt import mw
    return {"cards": 100}
```

Resources are read-only - no `write` option. URI template variables become function parameters.

#### @Prompt Decorator

```python
# primitives/essential/prompts/my_prompt.py
from ....prompt_decorator import Prompt

@Prompt("review_tips", "Tips for effective review")
def review_tips(deck_name: str = "Default") -> str:
    return f"When reviewing {deck_name}, focus on..."
```

Prompts don't access `mw.col` - they just generate text templates.

#### Tool Groups (Domain Subpackages)

Every tool is one `@Tool` with flat, `Annotated[..., Field(description=...)]` params — there are no multi-action dispatchers (no `params` wrapper, no discriminated union). Related tools share a `<domain>_` name prefix so they sort together in a client's tool list (`card_*`, `tag_*`, `filtered_deck_*`, `model_field_*`, like the existing `gui_*`), and live in a domain subpackage:

```
primitives/essential/tools/card_management/
├── __init__.py              # Imports every *_tool module and lists them in __all__
├── card_bury_tool.py        # @Tool("card_bury", ...) -- validation + impl call
├── card_unbury_tool.py
└── actions/
    ├── bury.py              # bury_impl()
    └── unbury.py            # unbury_impl()
```

Each tool file owns its own description, annotations and input validation, and calls the shared `_impl()` in `actions/`. The directory names (`card_management/`, `tag_management/`, `filtered_deck/`, `model_fields/`) are historical; they are domain folders now, not tools.

**Retired names / config aliases**: `card_management`, `tag_management`, `filtered_deck` and `model_fields` used to be multi-action dispatchers; 0.40.0 split them into one tool per action. `TOOL_ALIASES` in `tool_decorator.py` keeps old config entries working with a deprecation warning (startup dialog on every profile open, console once per process): `"card_management:bury"` behaves exactly like `"card_bury"` in every list, and a bare `"card_management"` in `disabled_tools` disables the whole group. In `enabled_destructive_tools` / `enabled_opt_in_tools` a bare old name opts in nothing (a whole-tool entry never opted in gated actions — expanding `"model_fields"` would silently reveal `model_field_remove`). The alias table is the only meaning a `"tool:action"` entry still has; any other one warns and matches nothing.

**Imports**: `pkgutil.walk_packages` in `primitives/essential/tools/__init__.py` imports every submodule (including `_`-prefixed helpers, which simply register nothing), so the subpackage `__init__.py` import list is belt-and-braces — keep it in sync anyway.

### Error Handling

Use `HandlerError` for structured errors with actionable hints:

```python
from ....handler_wrappers import HandlerError

raise HandlerError(
    "Deck not found",
    hint="Check spelling or use list_decks to see available decks",
    deck_name="Spansh"  # Extra context passed as kwargs
)
```

### Tunnel Architecture

The tunnel provides remote access to the MCP server via a public HTTPS URL, allowing AI clients that cannot reach `localhost` (e.g., Claude Desktop on a different machine, mobile clients) to connect.

#### How It Works

The tunnel client connects to a WebSocket relay server (SaaS). The relay assigns a public HTTPS URL. When an AI client sends an MCP request to that URL, the relay forwards it over WebSocket to the addon, which processes it via an in-memory transport directly into FastMCP and sends the response back.

```
AI Client (remote)
    → HTTPS request to public URL
    → Tunnel relay server (WebSocket)
    → TunnelClient._handle_request()
    → InMemoryTransport.handle_request(json_rpc_body)
    → Server.run() → FastMCP handlers → QueueBridge → Qt main thread
    → Response flows back the same path
```

#### In-Memory Transport

The tunnel does NOT proxy through HTTP. Instead, `in_memory_transport.py` feeds JSON-RPC strings directly into the MCP SDK's `Server.run()` via anyio memory streams. This makes the tunnel a first-class transport peer to HTTP, not a proxy layer.

Key details:
- Uses raw `anyio.create_memory_object_stream[SessionMessage | Exception](1)` (not the SDK's context manager helper)
- Runs `Server.run(stateless=True)` — skips MCP initialize handshake since the remote client drives initialization through the relay
- Matches responses to requests by JSON-RPC `id` via `asyncio.Future`
- Notifications (no `id`) are fire-and-forget
- One fresh `InMemoryTransport` per connection attempt (clean session on reconnect)

#### Threading

The tunnel runs on the **same asyncio event loop** as HTTP (the background thread in `mcp_server.py`). Both HTTP and tunnel share one `Server` object (via `FastMCP._mcp_server`). Each transport runs its own `Server.run()` with independent streams — no cross-contamination. When `http_enabled=False`, or HTTP fails to start (see "Port Already in Use"), the asyncio loop stays alive via an `asyncio.Event` wait instead of uvicorn.

#### Module Responsibilities

Each tunnel module has a single responsibility. Dependencies flow one direction (downward). UI is never imported by core tunnel logic.

- `protocol.py` — pure data types and constants (close codes, message TypedDicts, timeouts). Zero I/O, zero state.
- `credentials.py` — credential file I/O only (addon-owned `user_files/credentials.json`). No auth, no network. Lives at `anki_mcp_server/credentials.py` (not in tunnel/) since it's used across the main addon.
- `auth.py` — async OAuth Device Flow HTTP calls via httpx. No WebSocket, no file I/O.
- `client.py` — single WebSocket connection lifecycle. Receives tunnel requests, proxies via `InMemoryTransport`, handles ping/pong. No retry logic.
- `reconnect.py` — retry/backoff wrapper around `TunnelClient`. Creates a fresh client + transport per attempt. This is the main entry point callers use.
- `in_memory_transport.py` — feeds JSON-RPC into `Server.run()` via anyio memory streams.
- `log.py` — thread-safe ring buffer with Qt signal for cross-thread UI updates.
- `ui/login_dialog.py` — Qt device flow dialog (user code + "Open Browser" button).
- `ui/settings_section.py` — tunnel status/controls in the settings dialog.
- `ui/toolbar_indicator.py` — always-present `● AnkiMCP` item in Anki's top toolbar; its dot color reflects tunnel state (grey=idle, amber=connecting/reconnecting, green=connected), clicking opens the settings dialog. Like `settings_section.py`, it derives state by polling `ConnectionManager` on a 1-second `QTimer` (the established state channel) rather than a Qt signal — this keeps core tunnel modules UI-free. Gated by the `show_toolbar_indicator` config field.

#### Configuration

These config fields control tunnel behavior:

- `http_enabled: bool = True` — when `False`, uvicorn doesn't start. Only tunnel transport is available. Toggle via the settings dialog checkbox.
- `tunnel_server_url: str` — WebSocket URL of the tunnel relay server. Default is `wss://tunnel.ankimcp.ai` (production). Point at `ws://localhost:3004` for local relay development.
- `tunnel_client_id: str` — OAuth client identifier. Default is `ankimcp-cli` (shared with the TypeScript CLI).
- `show_toolbar_indicator: bool = True` — when `True`, adds the persistent `● AnkiMCP` status dot to Anki's top toolbar (see `ui/toolbar_indicator.py`). Set `False` to hide it.

There is no `mode` field. HTTP is always-on by default (controlled by `http_enabled`). Tunnel never auto-connects — the user must explicitly click "Connect Tunnel" in the settings dialog each time.

#### Credential Storage

Credentials are addon-owned: stored in the addon's `user_files/credentials.json` (preserved across addon updates) with `0o600` file permissions, in a directory created at mode `0o700`. They are **not** shared with the TypeScript CLI — the CLI keeps its own credentials under `~/.ankimcp/`, so the addon and CLI authenticate independently. The on-disk format is identical to the CLI's `CredentialsService`, but there is no migration or read-fallback: a user who previously logged in via the CLI (or an older addon build that used `~/.ankimcp/`) must log in again from the addon. The `Credentials` dataclass holds `access_token`, `refresh_token`, `expires_at`, and `user` (with email and tier).

#### Settings Dialog

The settings dialog (*Tools -> AnkiMCP Server Settings...*) has:
- **HTTP section**: status display, URL, "Copy URL" button. Shows "Disabled" when `http_enabled=False`.
- **Tunnel section**: Connect/Disconnect button, status with user email + tier + URL expiry, Logout link.
- **Log section**: scrollable ring buffer of recent tunnel events (connections, requests, errors, auth).

Connect flow: check credentials -> no credentials? launch device flow login dialog -> credentials expired? silent refresh -> connect WebSocket -> show tunnel URL.

Separately, the **top-toolbar indicator** (`ui/toolbar_indicator.py`, gated by `show_toolbar_indicator`) lives outside this dialog — it sits in Anki's main `Decks | Add | Browse | Stats | Sync` strip and clicking it opens this dialog.

#### Known Issues

**SIGKILL crash**: Anki can crash with SIGKILL when the tunnel relay server restarts while a tunnel connection is active. This is under investigation. The in-memory transport redesign was partly motivated by eliminating HTTP proxying as a potential crash vector, but the issue may persist.

#### Adding Tunnel-Related Code

Follow the existing module patterns:
- Pure data/constants go in `protocol.py`
- Network I/O gets its own module (like `auth.py` for HTTP, `client.py` for WebSocket)
- UI code goes in `tunnel/ui/` and must never be imported by core tunnel modules
- Use `TunnelLog` for user-visible events (not `print()` or `logging` alone)
- All callbacks are fire-and-forget — never let callback exceptions crash the tunnel

## Adding New Primitives

### Adding a Tool

**Single-file tool:**
1. Create `primitives/essential/tools/my_tool.py` (or `gui/tools/` for UI tools)
2. Use `@Tool` decorator with name, description, required `title=`, and optional `write=True` / `destructive_hint` / `open_world_hint`
3. Rebuild: `./package.sh` — auto-discovered via `pkgutil.walk_packages`

**Tool in a group:** Add a `<domain>_<verb>_tool.py` to the domain subpackage and import it in its `__init__.py` (see "Tool Groups" above). Don't build a multi-action dispatcher — one tool per action.

**Helper files:** Prefix with `_` (e.g., `_fsrs_helpers.py`) to mark them as helpers. `walk_packages` still imports them; they just register no tool.

### Adding a Resource

1. Create `primitives/essential/resources/my_resource.py`
2. Use `@Resource` decorator with URI, description, and explicit `name`
3. Rebuild: `./package.sh` — auto-discovered via `pkgutil.walk_packages` in `__init__.py`

### Adding a Prompt

1. Create `primitives/essential/prompts/my_prompt.py`
2. Use `@Prompt` decorator with name and description
3. **Manually import** in `primitives/prompts.py` (prompts are NOT auto-discovered)
4. Rebuild: `./package.sh`

## Key Implementation Details

### Versioning & Releases

Version lives in `__init__.py:__version__`. Release process: bump version (BOTH hand-bumped literals — see below) → commit → push tag `v*.*.*` → `version-gate` job checks the tag against `__version__` (seconds, no Docker) → `test` job runs E2E → `release` job creates the GitHub Release with the `.ankiaddon` artifact → `registry` job publishes to the MCP registry.

There are exactly TWO versions to bump by hand, and they must be equal: `__version__` (the source of truth — it is what the tag is checked against and what the registry is published with) and the `version = "...";` literal in `flake.nix` (a consumer of that value; a stale one makes `nix build .#addon` produce a mislabelled package). `tests/unit/test_version_consistency.py` enforces the equality, and `unit-tests.yml` runs it on push to every branch, so forgetting the flake goes red immediately rather than shipping silently. It is a hand-maintained literal deliberately — deriving it in Nix was considered and rejected. Everything ELSE is derived or verified, never hand-synced. `server.json` also carries a `version`, but the schema makes it required, so it holds the sentinel `0.0.0-set-by-ci` — the `registry` job **overwrites it** from `__version__` before publishing, and NOTHING in the pipeline runs past the `version-gate` job unless the pushed tag equals `v{__version__}` — that gate is `needs`-upstream of `test`, so a mistyped tag fails in seconds instead of after a ~20-minute E2E run. `release` and `registry` still re-derive and re-check the version themselves, so re-running one job alone is verified on its own rather than trusting the gate's earlier verdict. Do not hand-sync `server.json` — it drifted to a stale `0.19.0` once and the registry silently rejected every release from 0.20.0 to 0.27.0 as a duplicate version. Version resolution + tag check live in `.github/scripts/resolve_version.py`, shared by every workflow that needs them so they cannot disagree.

**The registry result is verified, never inferred.** `mcp-publisher login` and `publish` are run, their exit codes are logged, and then **both are ignored**. The job's verdict comes from asking the registry what it actually has, via `.github/scripts/check_registry_version.py`:

`GET https://registry.modelcontextprotocol.io/v0.1/servers/{name url-encoded}/versions/{version}`

- HTTP 200 + matching `name`/`version` + `_meta["io.modelcontextprotocol.registry/official"].status == "active"` → **green**.
- HTTP 404 → **red**: the registry accepted nothing.
- Anything else (transport error, 5xx, 429, unparseable body) → **red**: could not verify, re-run the job.

The `%2F` encoding of the `/` in the server name is mandatory (an unencoded slash 404s), and the exact-version endpoint is used deliberately instead of `?search=`, which is nginx-cached with a 30s TTL and no purge-on-publish and would additionally paginate out of correctness over time.

Do NOT reintroduce error-text classification. Three successive attempts to grade the release by pattern-matching the publisher's output all failed open; the last one because the registry's DNS-auth 401 body embeds the Go resolver's `lookup <domain> on 34.118.224.10:53: no such host`, which any "is this a transport failure?" allowlist reads as an outage. The strings belong to someone else and can be reworded at any time. This design also makes the job idempotent: on a re-run after a successful publish the publisher fails with a duplicate-version error, that is ignored, and verification finds the version live and passes.

**Job split.** `release` (builds + publishes the GitHub Release, `contents: write`) and `registry` (`needs: release`, `contents: read`) are separate jobs so a registry problem can be re-run alone. That matters because `package.sh` does a fresh `pip download` on every build with only `mcp` upper-bounded, so a rebuild of the same tag is not byte-identical — re-running the `release` job would otherwise replace an `.ankiaddon` users may already have downloaded. Two guards: the `registry` job cannot touch the Release (read-only token), and `Create Release` sets `overwrite_files: false` so even an accidental "Re-run all jobs" leaves the published asset alone.

**Drift check.** `.github/workflows/registry-drift.yml` runs weekly (and on demand), reads `__version__` off the default branch and does the same exact-endpoint GET. On anything but a clean yes it opens a `registry-drift`-labelled issue — deduped to at most one open issue at a time — and fails the job. This exists because nothing ever compared registry state to repo state, and that gap is what cost two months.

### Source Install Mode (Nix)

When installed from source (Nix, pip), vendored packages aren't used. `__init__.py` sets `_USING_SYSTEM_PACKAGES = True` and skips vendor path setup + conflict detection. The flag is toggled by checking whether system packages are importable before prepending the vendor path.

### No Linter / Formatter

This project has no pyproject.toml, ruff, flake8, or any configured linter. Don't try to run lint commands — they won't work.

### Profile Lifecycle

- Server starts on `profile_did_open` hook (HTTP auto-starts if `http_enabled`, tunnel never auto-starts)
- Server stops on `profile_will_close` hook (both HTTP and active tunnel)
- Fallback cleanup on `app_will_close`

### pydantic_core / rpds Runtime Loading

`pydantic_core` is lazy-loaded from PyPI at runtime via `dependency_loader.py` because it contains platform-specific binaries that can't be bundled in a single addon file.

`rpds` (from `rpds-py`) is a second native dependency handled by the same loader (`_ensure_rpds_with_callbacks`, wired in `__init__.py`), but it is almost never downloaded: Anki ships `rpds` transitively via its own `jsonschema`, so the common path is a plain `import rpds` with no network access. Both are cached under a resolved cache root (`dependency_loader._resolve_cache_root()`) — see "Native Dependency Cache Location" below for where that is, and "Background-thread / dependency-load resilience" below for the hardened load/retry/atomic-swap behavior shared by both.

### Native Dependency Cache Location

The pydantic_core/rpds cache does NOT always live inside the addon's own folder. Verified on a real Windows 11 VM:

- A loaded native extension (`.pyd`) can be **renamed/moved** on the same volume while the process holds it open, but it **cannot be deleted**.
- Anki updates and uninstalls an addon by **deleting its whole folder** (`aqt/addons.py` `_install` / `AddonsDialog.onDelete`). If the cache — and its locked `.pyd` — lives inside that folder, the delete dies halfway through and guts the addon (hundreds of files gone, `vendor/` emptied).

So the cache root is resolved per ensure-call by `dependency_loader._resolve_cache_root()`:
- **Preferred**: `<mw.pm.base>/ankimcp/<addon_folder_name>/cache` — outside the addon folder entirely, keyed by the installed folder name (`124672614` on AnkiWeb, `anki_mcp_server` from source) for the same one-cache-per-installed-copy isolation the old in-folder cache gave for free.
- **Fallback**: the legacy in-folder `CACHE_DIR` (`anki_mcp_server/_cache/`), used when `mw`/`mw.pm.base` isn't available or the preferred directory can't be created/written to.

`_resolve_cache_root()` only **decides** a root — it has no destructive side effects, and never touches the legacy `_cache/` dir itself. The legacy in-folder cache is removed only by `dependency_loader._cleanup_legacy_cache_dir_if_out_of_folder()`, called from `_ensure_pydantic_core_with_callbacks` / `_ensure_rpds_with_callbacks` **after a SUCCESSFUL outcome only** — i.e. only once the dependency has actually loaded (import or download) from the preferred out-of-folder root. A failed download to the preferred root (e.g. offline) therefore leaves the legacy cache exactly as it was, so it's still available as a working fallback on the next attempt; deleting it eagerly (the pre-fix behavior) could leave a user with no usable cache at all. On top of that, cleanup is a no-op whenever the legacy `CACHE_DIR` (or any path nested under it) is present on `sys.path` in this process — meaning a native extension may already be loaded from it — since deleting around a locked `.pyd`/`.so` in that case would recreate the exact gutting bug this relocation exists to avoid.

Since the cache is no longer guaranteed to be deleted along with the addon folder, `native_cache_cleanup.py` registers TWO hooks to clean it up / get it out of the way explicitly:

- `on_addons_dialog_will_delete_addons` on `gui_hooks.addons_dialog_will_delete_addons` — fires **only for deletion triggered from the Add-ons dialog** (uninstall). It is **cleanup-only** and never touches the download/retry logic:
  - POSIX: deletes the cache directories outright.
  - Windows: **renames** each into the temp dir (`os.rename`, unique `ankimcp-cache-<addon_folder_name>-<unix_ts>` name) instead of deleting, since the `.pyd` may still be loaded. Deliberately never `shutil.move` — its cross-volume fallback is copy-then-delete, which can copy the open `.pyd` successfully and then fail to delete the source, leaving BOTH behind instead of one. A failed `os.rename` (e.g. WinError 17, temp dir on another volume) is swallowed and the target is left in place.
- `on_addon_manager_will_install_addon` on `gui_hooks.addon_manager_will_install_addon` — closes the update-path gap: Anki's own update path (`download_addons` → `install` → `_install` → `backupUserFiles` → `deleteAddon`) never fires `addons_dialog_will_delete_addons`, so an install with a legacy in-folder cache still present was still exposed to the original Windows update failure. This hook fires right before `_install`, only acts when `module` is our own add-on folder name, and does two things in order: (1) on Windows only, relocates the **legacy** in-folder cache (`relocate_legacy_cache_before_update`, which reuses the exact same `_remove_or_relocate` primitive the delete hook uses) **whenever that directory exists** — there is no "fallback mode" gate, presence of the directory is the only signal checked; (2) releases the file-log handle via `file_log.release_log_handle` (see "Diagnostic File Logging" below) so it can't block `backupUserFiles`'s rename of `user_files`. Relocation runs FIRST and log release LAST, deliberately, so the handler's own INFO/WARNING lines about the relocation still land in the file before the handle closes. It NEVER touches the out-of-folder cache — that lives outside the folder being replaced and survives updates untouched. For AnkiWeb updates this hook runs on Anki's **background thread** (`taskman.run_in_background`), so it stays Qt/UI-free. Relocation deliberately does NOT apply the `_legacy_cache_in_use()` guard that gates `dependency_loader._cleanup_legacy_cache_dir`'s *deletion* of the legacy cache: that guard exists to avoid deleting around a loaded `.pyd`/`.so` (a delete of an open native extension fails outright on Windows), but this path *renames* the cache, which Windows permits even while the extension is loaded — renaming a possibly-loaded cache before Anki's own delete is the whole point of this hook.

Both hooks are wrapped so no exception can escape them: Anki drops a hook callback that raises (and never re-invokes it), so a raise here would look like nothing happened; on `addon_manager_will_install_addon` specifically, a re-raise aborts Anki's **whole batch update of every add-on**, not just ours. The registration itself lives in `__init__.py` **before** the `ensure_pydantic_core()` / `ensure_rpds()` gates on purpose: a gutted add-on (native extension deleted/moved mid-update on Windows) aborts import at one of those gates, and the hooks need to already exist at that point so the user's next uninstall/reinstall from the Add-ons dialog can still clean up the orphaned out-of-folder cache.

**Known residual gotcha**: the update TO the first version carrying the install-hook fix still fails once on Windows, because the OLD (already-loaded) code doesn't have the hook yet to release its own lock. Verified workaround: disable the addon → restart Anki → Check for Updates → re-enable → restart again. Every update after that first one is covered by the hook.

`dependency_loader._get_mw()` reads `sys.modules["aqt"]` instead of importing `aqt` — this keeps the standalone-module path (`spec_from_file_location`, e.g. the `anki-compat.yml` CI smoke script and the unit-test loaders) from dragging PyQt6 into a process that never otherwise touched Qt. Inside real Anki, `aqt` is always already imported before add-ons load, so behaviour there is unchanged.

### DNS Rebinding Protection

ENABLED on the HTTP transport with a loopback Host/Origin allowlist, built in `transport_security_config.build_transport_security(config)` and passed to `FastMCP` in `mcp_server.py`. The defaults (`DEFAULT_ALLOWED_HOSTS` / `DEFAULT_ALLOWED_ORIGINS`) mirror the MCP SDK loopback auto-default so ordinary localhost clients keep working. To expose the HTTP server through a tunnel/reverse proxy (Cloudflare, ngrok), operators ADD their hostname/origin to the `http_allowed_hosts` / `http_allowed_origins` config fields (which are appended to the defaults) — NOT by disabling protection. The tunnel (WebSocket) transport bypasses HTTP middleware entirely and is unaffected 

（文件较长，此处截取前 40000 字符）
