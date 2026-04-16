# combined.py
import os
from fastmcp import FastMCP
from mcpserver.deployment import register as register_deployment
from mcpserver.prompt_server import register as register_prompts
from mcpserver.resources import register as register_resources

def create_app() -> FastMCP:
    """Create and configure the combined MCP server."""
    app = FastMCP("Combined MCP Server")
    register_deployment(app)
    register_prompts(app)
    register_resources(app)
    return app

def main():
    app = create_app()
    # Use environment variables for host/port (common in cloud deployments)
    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", "8001"))
    # FastMCP's run() is blocking – perfect for a long‑running service
    app.run(transport="streamable-http", host=host, port=port)

if __name__ == "__main__":
    main()