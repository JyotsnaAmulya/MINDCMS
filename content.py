from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.generator import generate_article_with_metadata

router = APIRouter()

class ContentInput(BaseModel):
    topic: str
    category: str | None = None

@router.post("/generate")
async def generate_content(input: ContentInput):
    try:
        result = await generate_article_with_metadata(input.topic, input.category)
        return {"success": True, "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

