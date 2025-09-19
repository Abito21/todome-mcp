# basic mcp produce
from mcp.server.fastmcp import FastMCP


mcp = FastMCP("Math MCP")

@mcp.tool()
def add(a: int, b: int):
    return a + b
