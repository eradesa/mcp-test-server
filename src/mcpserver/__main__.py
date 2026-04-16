#from mcpserver.deployment import mcp
#from mcpserver.prompt_server import mcp
#from mcpserver.resources import mcp


# main.py
from fastmcp import FastMCP
from mcpserver.deployment import create_file_io_server
from mcpserver.prompt_server import create_prompt_server
#from resources import create_resource_server

# Create the main combined server
main_mcp = FastMCP("Combined MCP Server")

# Mount or import tools from each sub-server
file_server = create_file_io_server()
prompt_server = create_prompt_server()
#resource_server = create_resource_server()

# Option 1: Use `include_server()` (if available in FastMCP)
# main_mcp.include_server(file_server)
# main_mcp.include_server(prompt_server)
# main_mcp.include_server(resource_server)

# Option 2: Manually copy tools/prompts/resources
for tool in file_server._tool_manager._tools.values():
    main_mcp.add_tool(tool)

for prompt in prompt_server._prompt_manager._prompts.values():
    main_mcp.add_prompt(prompt)

#for resource in resource_server._resource_manager._resources.values():
    #main_mcp.add_resource(resource)

#if __name__ == "__main__":
#    main_mcp.run(transport="streamable-http", port=8000)


def main():
    main_mcp.run(transport="streamable-http")

if __name__ == "__main__":
    main()