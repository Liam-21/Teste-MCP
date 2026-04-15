from pathlib import Path
from common.webScraper import ResearchManager

# Definição de caminho para o ficheiro manifest.json
# Usamos isto para ele ter acesso ao caminho absoluto, para o Claude, por exemplo conseguir ver o sítio certo onde ele está

CURRENT_DIR = Path(__file__).resolve().parent

MANIFEST_FILE = CURRENT_DIR / "manifest.json"

# Instanciação da classe para usar globalmente
manager = ResearchManager(MANIFEST_FILE)