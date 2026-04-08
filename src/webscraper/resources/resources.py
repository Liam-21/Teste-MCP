from common.config import MANIFEST_FILE
import anyio

def register_resources(mcp):
    @mcp.resource("research://manifest")
    async def get_trusted_domains() -> str:
        """Returns the list of trusted domains/allowed sites, and the target endpoint for the post request to httpbin.org"""
        print(f"Searching for manifest at {MANIFEST_FILE}")
        file_path = anyio.Path(MANIFEST_FILE)
        content = await file_path.read_text()
        return content