from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

client = AsyncIOMotorClient(settings.MONGODB_URI)
db = client[settings.DATABASE_NAME]

# Example collections
content_collection = db["content"]
video_collection = db["videos"]
publish_collection = db["published"]
