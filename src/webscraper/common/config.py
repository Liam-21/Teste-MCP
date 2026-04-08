from pathlib import Path
from common.webScraper import ResearchManager
import anyio

CURRENT_DIR = Path(__file__).resolve().parent

MANIFEST_FILE = CURRENT_DIR / "manifest.json"

manager = ResearchManager(MANIFEST_FILE)
