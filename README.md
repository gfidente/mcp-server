# what is this ?

This is my attempt at writing a basic MCP server to experiment with the use of [MCP](https://modelcontextprotocol.io/introduction) with LLMs.

This server is written using [FastMCP](https://github.com/jlowin/fastmcp) and exports for consumption as Tools some basic math functions.

## how to try and test it ?

My approach has been to try this using the IBM's granite3.1-dense model - which is designed to support tool-based use cases. For example, to run granite3.1-dense using ollama:

1. Install ollama, as per https://github.com/ollama/ollama/blob/main/docs/linux.md

2. Pull the model:
```
ollama pull granite3.1-dense:2b
```

3. Start serving it:
```
ollama serve
```

4. Download and install the MCP server with its dependencies:
```
git clone https://github.com/gfidente/mcp-server.git
cd mcp-server
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

5. Also install the [MCP client library for ollama](https://github.com/jonigl/mcp-client-for-ollama):
```
pip install ollmcp
```

6. Launch the server and start interacting with the LLM:
```
ollmcp --mcp-server calculator.py --model granite3.1-dense:2b
```
