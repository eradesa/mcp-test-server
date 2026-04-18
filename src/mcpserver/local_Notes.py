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

        # Use home directory instead of current directory
        import os
        from pathlib import Path

        # Create notes directory in home folder

        home = Path.home()
        cwd = Path.cwd()
        print(f"Home: {home}")  # Check what this returns
        print(f"CWD: {cwd}")    # Check current directory
        print(f"User: {os.getlogin()}")  # Check running user

        notes_dir = Path.home() / "mcp_notes"
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

        home = Path.home()
        cwd = Path.cwd()
        print(f"Home: {home}")  # Check what this returns
        print(f"CWD: {cwd}")    # Check current directory
        print(f"User: {os.getlogin()}")  # Check running user

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
    