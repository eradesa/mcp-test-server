# mcpserver/__main__.py
from fastmcp import FastMCP
from mcpserver import register_deployment, register_prompts, register_resources, register_local_Notes, register_local_DB

# Create the combined server
mcp = FastMCP("Combined MCP Server")   # ← Must be named 'mcp', 'server', or 'app'

# Register all components
register_deployment(mcp)
register_prompts(mcp)
register_resources(mcp)
register_local_Notes(mcp)
register_local_DB(mcp)


# No need to call .run() here – the hosting platform will do that.