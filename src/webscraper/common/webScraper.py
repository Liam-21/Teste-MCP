import httpx
from typing import TypedDict
import json

class Info(TypedDict):
    url_encoding: str
    url_status_code: int
    url_content: str
    
    
class ResearchManager:
    def __init__(self, manifest_path: str):
        with open(manifest_path) as f:
            self.manifest = json.load(f)
            
        self.trusted_domains = self.manifest["trusted_domains"]
        
    def is_allowed(self, url: str) -> bool:
           if url in self.trusted_domains:
               return True
           else:
               raise Exception("That URL isn't allowed.")
            
    async def get_url_info(self, url: str) -> dict | None:
        if self.is_allowed(url):
            r = httpx.get(url)
            url_encoding:str = r.encoding
            url_status_code:int = r.status_code

            # Verifica se a página tem conteúdo (se o statusCode é diferente de 204: No Content, e se o tipo do conteúdo começa por applications/json, para saber se podemos obter o conteúdo através de um r.json(), ou se temos que usar .text
            if ( url_status_code != 204 and r.headers["content-type"].strip().startswith("application/json")):
                url_content:str = r.json()
            else: 
                url_content:str = r.text

            info: dict = {
                "urlEncoding": url_encoding,
                "urlStatusCode": url_status_code,
                "url_content": url_content
            }

            # print(type(url_content))

            info_json: Info = json.dumps(info)
            # print(info_json)
            return info_json
        else:
            return "That URL is not allowed"
        
        
    ## Cuidado! Aqui estou só a encapsular algo que já está encapsulado. Ver isto, porque não é boa prática criar uma classe e ter métodos que simplesmente usam um método da biblioteca.
    async def post_data(self, data: dict) -> str:
        r: str = httpx.post(self.manifest["post_endpoint"], data = data)
        return r.text     
