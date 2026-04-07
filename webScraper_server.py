from mcp.server.fastmcp import FastMCP
from webScraper import ResearchManager
## Biblioteca para poder ler ficheiro assíncronamente
import anyio
from pathlib import Path

mcp = FastMCP("webscraper_server")

BASE_DIR = Path(__file__).parent.resolve()
MANIFEST_FILE = BASE_DIR / "manifest.json"
manager = ResearchManager(anyio.Path(MANIFEST_FILE))

@mcp.tool()
async def postData(data: dict):
    """Post a summary/result of the URL's research to the Website "httbin.org", through the url, "https://httbin.org/post". You have two parameters, url(string) and data(dict)
    
    Args:
        url: The path for the endpoint to post,
        data: A dictionary with some data to simulate a post request in httbin.org
    """
    return await manager.postData(data)

@mcp.tool()
async def getURLInfo(url: str):
    """Get information about a given URL (encoding, status code, content).
    
    Args:
        url: The url to get the info of
    """
    return await manager.getURLInfo(url)

@mcp.resource("research://manifest")
async def getTrustedDomains() -> str:
    """Returns the list of trusted domains/allowed sites, and the target endpoint for the post request to httpbin.org"""
    print(f"Searching for manifest at {MANIFEST_FILE}")
    filePath = anyio.Path(MANIFEST_FILE)
    content = await filePath.read_text()
    return content

if __name__ == "__main__":
    print("mcp is running!")
    mcp.run(transport='stdio')