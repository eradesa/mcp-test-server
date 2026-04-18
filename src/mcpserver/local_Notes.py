#from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP

#mcp = FastMCP("LocalNotes")
def register(mcp: FastMCP):

    @mcp.tool()    
    def add_note_to_file(content: str) -> str:
        """
        Appends the given content to the user's local notes.
        Args:
            content: The text content to append.
        """
        import os
        from pathlib import Path

        # Use current working directory instead of home directory
        notes_dir = Path.cwd() / "mcp_notes"
        notes_dir.mkdir(exist_ok=True)

        filename = notes_dir / "notes.txt"

        try:
            with open(filename, "a", encoding="utf-8") as f:
                f.write(content + "\n")
            return f"Content appended to {filename}."
        except Exception as e:
            return f"Error appending to file {filename}: {e}"
                

    @mcp.tool()
    def read_notes() -> str:
        """
        Reads and returns the contents of the user's local notes.
        """
        import os
        from pathlib import Path

        # Use the SAME path as add_note_to_file
        notes_dir = Path.home() / "mcp_notes"  # Or Path("/tmp") / "mcp_notes" if that's what's actually being used
        filename = notes_dir / "notes.txt"

        try:
            with open(filename, "r", encoding="utf-8") as f:
                notes = f.read()
            return notes if notes else "No notes found."
        except FileNotFoundError:
            return "No notes file found."
        except Exception as e:
            return f"Error reading file {filename}: {e}"        
    