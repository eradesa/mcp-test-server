# mcpserver/__main__.py
from fastmcp import FastMCP
from mcpserver import register_deployment, register_prompts,    register_vector_store

# Create the combined server
mcp = FastMCP("Combined MCP Server")   # ← Must be named 'mcp', 'server', or 'app'

# Register all components
register_deployment(mcp)
register_prompts(mcp)
#register_resources(mcp)
#register_local_Notes(mcp)
#register_local_DB(mcp)
register_vector_store(mcp)


# No need to call .run() here – the hosting platform will do that.
#def main():
    #mcp.run(transport="streamable-http")
#    mcp.run(transport="streamable-http", host="0.0.0.0", port=8005)

#if __name__ == "__main__":#
#    main()
