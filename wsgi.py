import os
from dotenv import load_dotenv

load_dotenv()

from app import create_app

config_name = os.getenv("FLASK_CONFIG", "development")
app = create_app(config_name)
