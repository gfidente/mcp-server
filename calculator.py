from mcp.server.fastmcp import FastMCP
mcp = FastMCP("MCP Calculator Server")


# tools definitions
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return int(a + b)

# subtraction tool
@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract two numbers"""
    return int(a - b)

# multiplication tool
@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return int(a * b)

# division tool
@mcp.tool()
def divide(a: int, b: int) -> float:
    """Divide two numbers"""
    return float(a / b)

# power tool
@mcp.tool()
def power(a: int, b: int) -> int:
    """Power of two numbers"""
    return int(a ** b)

# remainder tool
@mcp.tool()
def remainder(a: int, b: int) -> int:
    """Remainder of two numbers divison"""
    return int(a % b)A


# execute using stdio for testing with local clients
if __name__ == "__main__":
    mcp.run(transport="stdio")
