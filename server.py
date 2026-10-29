from mcp.server.mcpserver import MCPServer

from hello import greet as _greet

mcp = MCPServer("hello-world")


@mcp.tool()
def greet(name: str) -> str:
    """Greet someone by name. Returns 'Hello <name>'."""
    return _greet(name)


if __name__ == "__main__":
    mcp.run(transport="stdio")
