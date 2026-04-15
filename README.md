# Webscraper Server

To run the project, I am using **Docker**, with **UV**.

## Getting Started

Use the command `docker compose up --build` in the terminal.
This builds the docker image and is also going to create a container for it.

It is going to run the command:
`uv run --python 3.12 src/webscraper/main.py`

Use `docker compose down` to stop and remove containers created.

## Claude Desktop MCP Integration

To test this MCP I am using **Claude Desktop**. Below is a walkthrough for the setup, or you can refer to the [official MCP documentation](https://modelcontextprotocol.io/docs/develop/connect-local-servers).

### Prerequisites

Please ensure you have **Claude Desktop** and **Node.js** installed on your machine:

* [Claude Desktop Download Link](https://claude.com/download)
* [Node.js Download Link](https://nodejs.org/)

---

### Installing and Configuring the Server

This process will configure Claude Desktop to automatically start the **webscraper MCP** whenever you launch the application.

#### 1. Open Claude Desktop Settings
Go to `Claude Desktop` -> `Settings` -> `Developer` -> `Edit Config`.

This will create a new configuration file if it doesn't yet exist, or open your existing one.

#### 2. Configuring the Server
Paste the following JSON configuration into the file (replacing `{path_to_the_main.py}` with your actual local path):

```json
{
  "mcpServers": {
    "webScraper": {
      "command": "uv",
      "args": [
        "run",
        "--with",
        "mcp",
        "{path_to_the_main.py}"
      ]
    }
  }
}
```

#### 3. Restart Claude Desktop

After saving the configuration file, you need to **completely quit** Claude Desktop and restart it. Upon restarting you should now be all setup.

### 4. Using the MCP

Now you can just create a new chat and if you click on the **"+" symbol** in the bottom left and then click on the **connectors** option and then you should now see the **webScraper mcp**.

If you want to use the prompt that I created you can, while in the **Connectors** option, select **Add from webScraper** -> **Get url info prompt** and then just select an url.

## Project Overview

In this project I used the **MCP Protocol**, in a **POC (Proof of Concept)** application, where I am using the `httpx` library to do some actions, related to a certain URL.

MCP is a protocol that follows a **server-client arquitecture**, where a **MCP Host** (an AI application, like Claude Desktop), that establishes connections with one or multiple MCP Servers.
The Host creates a **MCP Cliente** for each MCP Server. MCP is a simple way to integrate tools, resources and prompts. It's called the "USB-C port for AI applications"

### Key Partners in the Arquitecture:

* **MCP Host**: The AI app, that coordenates and manages one or multiple MCP Clients
* **MCP Client**: A component that keeps the connection with a MCP Server and obtains context for the MCP Host to use
* **MCP Server**: A program that supplies context to MCP Clients

### Protocol Layers:

* **Data Layer**: Defines the protocol, based in JSON-RPC, for client-server communication.
* **Transport Layer**: Defines the communication mechanisms and channels that allow for the exchange of data between clients and servers.

## Key Concepts

### There are 3 main important concepts to understand for this project, regarding MCP, and LLMs in general:

* **Tools**: Tools are something we use to make an LLM do some action, like a sum, or changing the lights on an LED
* **Resources**: Resources give passive data to an LLM, for example, you can access a database, and feed the data you want to an LLM
* **Prompts**: Prompts are specific instructions that we use to guide AI models, to generate desirable, relevant responses

### Implementation Details

In this project I created:
* **2 tools**: `post_data` and `get_url_info`
* **1 resource**: `get_trusted_domains`
* **1 prompt**: `get_url_info_prompt`