from mcp.server.fastmcp import FastMCP
from src.webscraper.common.webScraper import ResearchManager

mcp = FastMCP("webscraper_server")

from webscraper.resources.resources import register_resources
from webscraper.tools.tools import register_tools

register_resources(mcp)
register_tools(mcp)

if __name__ == "__main__":
    print("mcp is running!")
    mcp.run(transport='stdio')