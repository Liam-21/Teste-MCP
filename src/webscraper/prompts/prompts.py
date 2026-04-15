# Função para registar prompts, para poder só dar copy paste para testar o código, que é chamada no main.py (Se calhar podia estar dinâmico mas está assim por enquanto por isso unlucky)
def register_prompts(mcp):
    @mcp.prompt()
    def get_url_info_prompt(url: str) -> str:
        """Creates a prompt for getting the url info. You need only send the url.
        """
        return f"Give me information on this url: '{url}'. Use the webscraper mcp with it's tools and resources and use the post tool, to post very simple data on the url. If there is an internal error saying that the url isn't allowed, stop the answer."