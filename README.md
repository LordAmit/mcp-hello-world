# mcp-hello-world

A minimal Python MCP server with one tool, `greet`, that calls `greet(name)`
in `hello.py` and returns `Hello <name>`.

## Setup

```sh
uv sync
```

## Smoke test the Python function

```sh
uv run python -c "from hello import greet; print(greet('Claude'))"
# Hello Claude
```

## Run the server by hand

```sh
uv run server.py
```

It speaks MCP over stdio and waits for a client. Press Ctrl+C to stop.

## Claude Desktop

Edit the config file:

- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`

Add this server (adjust the `--directory` path if you cloned elsewhere):

```json
{
  "mcpServers": {
    "hello-world": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/mcp-hello-world",
        "run",
        "server.py"
      ]
    }
  }
}
```

If Claude Desktop cannot find `uv`, replace `"command": "uv"` with the full
path from `which uv` (for example `/Users/you/.local/bin/uv`).

Restart Claude Desktop, then ask: "Use the greet tool to greet Claude."
Expected tool result: `Hello Claude`.

## Claude Code

```sh
claude mcp add hello-world -- uv --directory /path/to/mcp-hello-world run server.py
```

## Gemini CLI

Gemini CLI reads `~/.gemini/settings.json` (user-wide) or `.gemini/settings.json`
(per project). Same stdio pattern as Claude Desktop, same key name:

```json
{
  "mcpServers": {
    "hello-world": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/mcp-hello-world",
        "run",
        "server.py"
      ]
    }
  }
}
```

Or let the CLI write it:

```sh
gemini mcp add hello-world uv --directory /path/to/mcp-hello-world run server.py
```

Then `/mcp` inside Gemini CLI lists the server. The consumer Gemini app
(web and mobile) does not take local MCP servers; use the CLI.

## OpenAI Codex CLI

Codex uses TOML at `~/.codex/config.toml` (or `.codex/config.toml` in a
trusted project). Stdio works directly:

```toml
[mcp_servers.hello-world]
command = "uv"
args = ["--directory", "/path/to/mcp-hello-world", "run", "server.py"]
```

Or:

```sh
codex mcp add hello-world -- uv --directory /path/to/mcp-hello-world run server.py
```

## Files

- `hello.py`: the plain Python function, no MCP imports
- `server.py`: the MCP server, one tool, stdio
- `pyproject.toml`: project metadata and the `mcp` dependency
- `SPEC.md`: the agreed scope
