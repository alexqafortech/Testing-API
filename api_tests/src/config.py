import os
from dotenv import load_dotenv

load_dotenv()
class Config:
    BASE_URL: str = os.getenv("BASE_URL", "http://localhost:5000")
    API_TIMEOUT: int = int(os.getenv("API_TIMEOUT", "5"))

config = Config()