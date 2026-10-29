# Spec: MCP Hello World

## Objective
A minimal Python MCP server that wraps one plain Python function. The function
`greet(name)` returns `"Hello " + name`. The server exposes it as a single MCP
tool over stdio so Claude Desktop (or any MCP client) can call it.

User: Amit, learning how an MCP server wraps a Python function.

Acceptance: In Claude Desktop, asking Claude to greet "Claude" makes it call
the tool and the tool returns `Hello Claude`.

## Tech Stack
- Python 3.11+ (3.14 is installed locally)
- `mcp` official Python SDK (FastMCP API), latest release at build time
- `uv` for environment and running (uv 0.10.4 installed)
- Transport: stdio

## Commands
```
Install deps:   uv sync
Run server:     uv run server.py
Smoke test:     uv run python -c "from hello import greet; print(greet('Claude'))"
Inspector:      npx @modelcontextprotocol/inspector uv run server.py
Claude Code:    claude mcp add hello-world -- uv --directory /path/to/mcp-hello-world run server.py
```

## Project Structure
```
hello.py        → greet(name: str) -> str, no MCP imports
server.py       → FastMCP server, one tool `greet` that calls hello.greet
pyproject.toml  → project metadata, dependency on mcp
README.md       → setup, config for Claude Desktop, Claude Code, Gemini CLI, Codex CLI
SPEC.md         → this file
```

## Code Style
```python
def greet(name: str) -> str:
    """Return a greeting for the given name."""
    return f"Hello {name}"
```
- Type hints on every function.
- One-line docstrings; the tool docstring is what the MCP client shows the model.
- No logic in `server.py` beyond registering the tool and calling `hello.greet`.
- No stdout printing in the server: stdio transport uses stdout for protocol messages.

## Testing Strategy
No automated tests (out of scope by agreement). Verification is manual:
1. Smoke test command above prints `Hello Claude`.
2. Server starts under `uv run server.py` without errors and waits on stdin.
3. In Claude Desktop, the `hello-world` server shows as connected and the
   `greet` tool returns `Hello Claude`.

## Boundaries
- Always: keep `hello.py` free of MCP imports; keep the server to one tool.
- Ask first: adding any dependency beyond `mcp`; adding a second tool.
- Never: print to stdout from the server; switch transport away from stdio.

## Success Criteria
- `uv run python -c "from hello import greet; print(greet('Claude'))"` prints `Hello Claude`.
- `uv run server.py` starts without a traceback.
- Claude Desktop config from README connects, and greeting "Claude" returns `Hello Claude`.

## Out of Scope
Tests, HTTP/SSE transport, distribution packaging, extra tools, ChatGPT (needs a remote HTTPS server). (Changed 2026-10-29: config snippets added for Gemini CLI and Codex CLI.)

## Open Questions
- Server name as shown in Claude Desktop: `hello-world` (default unless changed).
- Tool name: `greet` (default unless changed).
