# server.py
from fastmcp import FastMCP
import requests

YOUR_API_KEY = '8692ebca30473ab0a3238a5047c1d00b'

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def perform_websearch(query: str) -> str:
    """
    Performs a web search for a query
    Args:
        query: the query to web search.
    Returns:
        A formatted string with search results
    """
    
    try:
        params = {
            'access_key': YOUR_API_KEY,
            'query': query
        }

        api_result = requests.get('https://api.serpstack.com/search', params=params)
        api_result.raise_for_status()  # Raise exception for bad status codes
        
        api_response = api_result.json()

        # Check if search was successful
        if 'error' in api_response:
            return f"Error: {api_response['error']['info']}"

        # Format results
        results_text = f"Total results: {api_response.get('search_information', {}).get('total_results', 'N/A')}\n\n"
        
        if 'organic_results' in api_response:
            for number, result in enumerate(api_response['organic_results'], start=1):
                title = result.get('title', 'No title')
                link = result.get('url', 'No URL')
                snippet = result.get('snippet', 'No snippet')
                results_text += f"{number}. {title}\n"
                results_text += f"   URL: {link}\n"
                results_text += f"   {snippet}\n\n"
        else:
            results_text += "No organic results found."
        
        return results_text
    
    except requests.exceptions.RequestException as e:
        return f"Request error: {str(e)}"
    except Exception as e:
        return f"Error: {str(e)}"
        
@mcp.tool()
def greeting(name: str) -> str:
    """Send a greeting"""
    try:
        if not name:
            raise ValueError("Name cannot be empty")
        return f"Hi, how are you, {name}"
    except Exception as e:
        #logger.error(f"Tool execution failed: {e}")
        raise e

#if __name__ == "__main__":
    # Ensure you are running with the SSE transport for HTTP connections
#    mcp.run(transport="sse")

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
