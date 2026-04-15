from common.config import manager

# Função para registar tools, a ser chamada pelo main.py
def register_tools(mcp):
    @mcp.tool()
    async def post_data(data: dict):
        """Post a summary/result of the URL's research to the Website "httbin.org", through the url, "https://httbin.org/post". You have two parameters, url(string) and data(dict)

        Args:
            url: The path for the endpoint to post,
            data: A dictionary with some data to simulate a post request in httbin.org
        """
        return await manager.post_data(data)

    @mcp.tool()
    async def get_url_info(url: str):
        """Get information about a given URL (encoding, status code, content).

        Args:
            url: The url to get the info of
        """
        return await manager.get_url_info(url)