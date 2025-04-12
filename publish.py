from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.publisher import publish_to_platforms

router = APIRouter()

class PublishInput(BaseModel):
    content_id: str
    platforms: list[str]  # e.g., ["blog", "twitter"]

@router.post("/auto-publish")
async def publish_content(input: PublishInput):
    try:
        status = await publish_to_platforms(input.content_id, input.platforms)
        return {"success": True, "status": status}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
