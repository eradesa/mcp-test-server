#from mcpserver.deployment import mcp
#from mcpserver.prompt_server import mcp
#from mcpserver.resources import mcp


#def main():
#    mcp.run(transport="streamable-http")

#if __name__ == "__main__":
#    main()

# combined.py
import asyncio
from fastmcp import FastMCP
from mcpserver.deployment  import register as register_deployment
from mcpserver.prompt_server import register as register_prompts
from mcpserver.resources import register as register_resources


def main():
    # Create the main combined server
    mcp = FastMCP("Combined MCP Server")
    # Register all components
    register_deployment(mcp)
    register_prompts(mcp)
    register_resources(mcp)

    #combined_mcp.run(transport="streamable-http")
    #combined_mcp.run(transport="streamable-http", host="0.0.0.0", port=8001)
    asyncio.run(mcp.run_async(transport="streamable-http", host="0.0.0.0", port=8005))
    #asyncio.run(mcp.run_async(transport="streamable-http"))

if __name__ == "__main__":
    # Run as a single HTTP server (Streamable HTTP)
    #combined_mcp.run(transport="streamable-http", host="0.0.0.0", port=8000)
    main()