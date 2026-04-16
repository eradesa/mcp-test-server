from mcpserver.deployment import mcp
#from mcpserver.prompt_server import mcp
#from mcpserver.resources import mcp


def main():
    mcp.run(transport="streamable-http")

if __name__ == "__main__":
    main()