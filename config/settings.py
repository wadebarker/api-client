import os

from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "http://2.59.41.2:7320")

REQUEST_TIMEOUT=int(os.getenv("REQUEST_TIMEOUT", 10))