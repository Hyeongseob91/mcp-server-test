from fastmcp import FastMCP
import sys

mcp = FastMCP("Test Server")

@mcp.tool()
def test_operation(num: int):
    num = int(num)
    return num * 2

if __name__ == "__main__":
    print("Starting MCP server...", file=sys.stderr)
    mcp.run(transport="sse")