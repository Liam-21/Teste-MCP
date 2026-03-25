import httpx

class URL():
    async def getContent(url):
        print(url)
        return httpx.get(f"{url}").content
        