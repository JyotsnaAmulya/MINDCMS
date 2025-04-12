from pydantic import BaseModel, Field
from typing import Optional, List
from bson import ObjectId

# Helper to convert MongoDB ObjectId to string
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return str(v)


class ArticleModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    topic: str
    category: Optional[str]
    content: str
    seo_title: str
    meta_description: str
    keywords: List[str]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class VideoModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    article_id: str
    video_url: str

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class PublishModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    article_id: str
    platforms: List[str]
    status: str  # e.g., "success", "failed"

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
