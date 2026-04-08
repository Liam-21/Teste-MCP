from mcp.server.fastmcp import FastMCP

mcp = FastMCP("webscraper_server")

from resources.resources import register_resources
from tools.tools import register_tools

register_resources(mcp)
register_tools(mcp)

if __name__ == "__main__":
    print("mcp is running!")
    mcp.run(transport='stdio')