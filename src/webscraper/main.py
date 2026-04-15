# Verificar este import porque aparentemente este é o import para o FastMCP 1.0, enquanto que para o FastMCP 2.0 é suposto fazer assim from fastmcp import FastMCP (SUPOSTAMENTE)

from mcp.server.fastmcp import FastMCP
import sys
from resources.resources import register_resources
from tools.tools import register_tools
from prompts.prompts import register_prompts

# Inicialização do servidor
mcp = FastMCP("webscraper_server")

# Registar resources, tools e prompts ao mcp
register_resources(mcp)
register_tools(mcp)
register_prompts(mcp)

if __name__ == "__main__":
    sys.stdout.write("mcp is running!")
    mcp.run(transport='stdio')