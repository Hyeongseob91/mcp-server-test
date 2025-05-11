from fastmcp import FastMCP
import sys

# MCP 서버 초기화 (HTTP 모드 명시)
mcp = FastMCP(
    name="Test Server",
    instructions="This is a test MCP server for tool scan validation."
)

# 테스트 툴 함수 정의
@mcp.tool()
def test_operation(num: int = 1, config: dict = None):
    try:
        num = int(num)
        return {"result": num * 2}
    except Exception as e:
        print(f"[test_operation ERROR] {e}", file=sys.stderr)
        return {"error": str(e)}

# 서버 실행
if __name__ == "__main__":
    print("[INFO] Starting Test MCP Server...", file=sys.stderr)
    mcp.run(transport="streamable-http", host="127.0.0.1", port=8000, path="/mcp")
