import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings:
    PROJECT_NAME: str = "MindCMS.ai"
    COHERE_API_KEY: str = os.getenv("COHERE_API_KEY")
    MONGODB_URI: str = os.getenv("MONGODB_URI")
    DATABASE_NAME: str = os.getenv("DATABASE_NAME", "mindcms_db")
    COHERE_MODEL: str = "command-r" 

settings = Settings()
