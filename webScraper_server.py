from mcp.server.fastmcp import FastMCP
from webScraper import URL

mcp = FastMCP("webscraper_server")

@mcp.tool()
async def get_content(url):
    """Get the content of a URL.
    
    Args:
        url: The url to get the content of
    """
    print(url)
    return await URL.getContent(url)

if __name__ == "__main__":
    mcp.run(transport='stdio')