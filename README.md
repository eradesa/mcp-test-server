To install the add_tool MCP server, run the following command:
```
{
  "mcpServers": {
    "testmcpgit_add_tool": {      
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/eradesa/mcp-test-server.git@MCP-STDIO",
        "mcp-server"
      ]
    }
  }
}

- name: "git_web_search_serpstack_br"
      command: "uvx"
      args: ["--from", "git+https://github.com/eradesa/mcp-test-server.git@MCP-STDIO", "mcp-server"]
      #env:
      #  FILE_IO_BASE_DIR: "/home/erangadesarhttps://github.com/eradesa/mcp-test-server.git@MCP-STDIOam/Downloads"  # optional
      transport: "stdio"
```
This will fetch and set up the mcp-server from the specified GitHub repository.