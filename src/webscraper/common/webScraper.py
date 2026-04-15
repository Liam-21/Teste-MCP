import httpx
from typing import TypedDict
import json

class Info(TypedDict):
    url_encoding: str
    url_status_code: int
    url_content: str
    
    
class ResearchManager:
    def __init__(self, manifest_path: str):
        
        # Damos load ao ficheiro manifest primeiro, com os domínios que aceita
        with open(manifest_path) as f:
            self.manifest = json.load(f)
            
        # Definimos os trusted domains na class com os dados do manifest, dos trusted_domains    
        self.trusted_domains = self.manifest["trusted_domains"]
        
    # Método para verificar se um url é um dos urls permitidos
    def is_allowed(self, url: str) -> bool:
           if url in self.trusted_domains:
               return True
           else:
               raise Exception("That URL isn't allowed.")
            
    async def get_url_info(self, url: str) -> dict | None:
        # Verifica que foi mandado um URL
        if not url:
            raise Exception("Please insert an URL")
        
        # Verifica se é um url permitido, e se for devolve informação sobre o URL
        if self.is_allowed(url):
            r = httpx.get(url)
            url_encoding:str = r.encoding
            url_status_code:int = r.status_code

            # Verifica se a página tem conteúdo (se o statusCode é diferente de 204: No Content), e se o tipo do conteúdo começa por applications/json, para saber se podemos obter o conteúdo através de um r.json(), ou se temos que usar .text
            if ( url_status_code != 204 and r.headers["content-type"].strip().startswith("application/json")):
                url_content:str = r.json()
            else: 
                url_content:str = r.text

            info: dict = {
                "urlEncoding": url_encoding,
                "urlStatusCode": url_status_code,
                "url_content": url_content
            }

            info_json: Info = json.dumps(info)
            
            return info_json
                
    # Método para "simular" um pedido post, com um certo data, através do httpbin
    async def post_data(self, data: dict) -> str:
        r: str = httpx.post(self.manifest["post_endpoint"], data = data)
        return r.text