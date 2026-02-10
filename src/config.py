import os
from dotenv import load_dotenv

load_dotenv()

LM_STUDIO_URL = os.getenv("LM_STUDIO_URL", "http://localhost:1234/v1")
LM_STUDIO_MODEL = os.getenv("LM_STUDIO_MODEL", "llama-3.2-7b-instruct")
TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))
MAX_TOKENS = int(os.getenv("MAX_TOKENS", "500"))
APP_NAME = os.getenv("APP_NAME", "Inteligencia Evolutiva")
APP_VERSION = os.getenv("APP_VERSION", "0.1.0")
