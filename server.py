### Phase 1 - Prototype

## Building a Meaningful Prototype MCP tool: "Web Scraper" that fetches and summarises a URL with httpx

## Initial Imports

from dotenv import load_dotenv
from agents import Agent, Runner, trace
from agents.mcp import MCPServerStdio
from IPython.display import display, Markdown

load_dotenv(override=True)