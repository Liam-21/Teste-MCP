### Phase 1 - Prototype

## Building a Meaningful Prototype MCP tool: "Web Scraper" that fetches and summarises a URL with httpx

## Initial Imports

from dotenv import load_dotenv
from agents import Agent, Runner, trace, enable_verbose_stdout_logging
from agents.mcp import MCPServerStdio
# from agents.tracing.setup import GLOBAL_TRACE_PROVIDER

# GLOBAL_TRACE_PROVIDER._multi_processor.force_flush()

# enable_verbose_stdout_logging()

import asyncio
import webScraper

load_dotenv(override=True)

# from webScraper import URL

# urlContent = URL.getContent("https://marvel.fandom.com/wiki/Jeffrey_(Land_Shark)_(Earth-616)")
# print(urlContent)

# agent = Agent(name="Ass", instructions="You are a helpful assistant")

# result = Runner.run_sync(agent, "Write a poem about how sexy Alves is.")
# print(result.final_output)

params = {"command": "uv", "args": ["run", "webscraper_server.py"]}
# capabilities = {"capabilities": {"tools":{"listChanged": True}}}    

async def __main__():
    print("running e o Alves é sexy")
    # async with MCPServerStdio(params=params, client_session_timeout_seconds=30) as server:

    # print(mcp_tools)
    
    instructions = "You are able to give information about the content of a given URL"
    request = "Can you tell me the content of this URL: `https://www.marvel.com/characters/jeff-the-land-shark` ?"
    model = "gpt-5.2"
    
    async with MCPServerStdio(params=params, client_session_timeout_seconds=30) as mcp_server:
        mcp_tools = await mcp_server.list_tools()
        print(mcp_tools)
        agent = Agent(name="webScraper", instructions=instructions, model=model, mcp_servers=[mcp_server])
        with trace("webScraper"):
            result = await Runner.run(agent, request)
        print(result.final_output)

asyncio.run(__main__())
