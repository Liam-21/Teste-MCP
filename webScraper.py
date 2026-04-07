import httpx
from typing import TypedDict
import json
from pathlib import Path

class Info(TypedDict):
    urlEncoding: str
    urlStatusCode: int
    urlContent: str
    
    
class ResearchManager:
    def __init__(self, manifestPath: str):
        with open(manifestPath) as f:
            self.manifest = json.load(f)
            
        self.trustedDomains = self.manifest["trustedDomains"]
        
    def isAllowed(self, url: str) -> bool:
           if url in self.trustedDomains:
               return True
           else:
               raise Exception("That URL isn't allowed.")
            
    async def getURLInfo(self, url: str) -> dict | None:
        if self.isAllowed(url):
            r = httpx.get(url)
            urlEncoding:str = r.encoding
            urlStatusCode:int = r.status_code

            # Verifica se a página tem conteúdo (se o statusCode é diferente de 204: No Content, e se o tipo do conteúdo começa por applications/json, para saber se podemos obter o conteúdo através de um r.json(), ou se temos que usar .text
            if ( urlStatusCode != 204 and r.headers["content-type"].strip().startswith("application/json")):
                urlContent:str = r.json()
            else: 
                urlContent:str = r.text

            info: dict = {
                "urlEncoding": urlEncoding,
                "urlStatusCode": urlStatusCode,
                "urlContent": urlContent
            }

            # print(type(urlContent))

            infoJson: Info = json.dumps(info)
            # print(infoJson)
            return infoJson
        else:
            return "That URL is not allowed"
        
        
    ## Cuidado! Aqui estou só a encapsular algo que já está encapsulado. Ver isto, porque não é boa prática criar uma classe e ter métodos que simplesmente usam um método da biblioteca.
    async def postData(self, data: dict) -> str:
        r: str = httpx.post(self.manifest["post_endpoint"], data = data)
        return r.text     
