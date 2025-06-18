# what is this ?

This is my attempt at writing a basic MCP server to experiment with the use of [MCP](https://modelcontextprotocol.io/introduction) with LLMs.

This server is written using [FastMCP](https://github.com/jlowin/fastmcp) and exports for consumption as Tools some basic math functions.

## how does it work ?

A typical convesaration, showing the available functions would look like this:
```
Query: hello there, I am Giulio. What can you do for me?
Answer:

Hello Giulio! I'm an AI, and I can help with a variety of tasks using the functions you've provided as a calculator. Here are some things I can do:

 1 Addition: calculator.add(a, b) - This will return the sum of numbers 'a' and 'b'.
 2 Subtraction: calculator.subtract(a, b) - This will return the difference between 'a' and 'b'.
 3 Multiplication: calculator.multiply(a, b) - This will return the product of 'a' and 'b'.
 4 Division: calculator.divide(a, b) - This will return the quotient of 'a' divided by 'b', provided that 'b' is not zero.
 5 Exponentiation: calculator.power(a, b) - This will return 'a' raised to the power of 'b'.
 6 Remainder: calculator.remainder(a, b) - This will return the remainder when 'a' is divided by 'b'.

Please provide me with the numbers and operation you'd like to perform, using these function names along with their respective parameters.

Query: Great, can you calculate the power of 4 by 4?
Answer:

Absolutely! Using the calculator.power function:


 calculator.power(4, 4)


The result is 256. This is because 4 raised to the power of 4 equals 256.
```

## how to try and test it ?

My approach has been to try this using the IBM's granite3.1-dense model - which is designed to support tool-based use cases. For example, to run granite3.1-dense using ollama and connect it with the calculator.py MCP server:

1. Install ollama, as per https://github.com/ollama/ollama/blob/main/docs/linux.md

2. Start the ollama service:
```
ollama serve
```

3. Pull the model:
```
ollama pull granite3.1-dense:2b
```

4. Download and install the MCP server with its dependencies in a virtual env:
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
