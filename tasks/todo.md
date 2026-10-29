# Tasks: MCP Hello World

- [x] 1. pyproject.toml with `mcp` dependency; `uv sync` succeeds
  - Verify: `uv sync` exits 0
- [x] 2. hello.py with greet(name) -> "Hello {name}"
  - Verify: smoke test prints `Hello Claude`
- [x] 3. server.py: FastMCP server, one `greet` tool calling hello.greet
  - Verify: `uv run server.py` starts without traceback; tool call over stdio returns `Hello Claude`
- [x] 4. README.md with Claude Desktop config and `claude mcp add` line
  - Verify: paths in config are absolute and match this folder
- [ ] 5. Register in Claude Desktop and call greet("Claude") (user does this)
  - Verify: Claude Desktop returns `Hello Claude`
- [x] 6. Config for Gemini CLI and Codex CLI in README (ChatGPT and HTTP transport reverted, out of scope)
  - Verify: stdio tool call still returns `Hello Claude`
