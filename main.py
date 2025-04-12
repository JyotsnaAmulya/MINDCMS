# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from app.api.v1 import content, media, publish

# app = FastAPI(title="MindCMS.ai")

# # Allow cross-origin (CORS) if needed for frontend
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Route registration
# app.include_router(content.router, prefix="/api/v1/content", tags=["Content"])
# # app.include_router(media.router, prefix="/api/v1/media", tags=["Media"])
# # app.include_router(publish.router, prefix="/api/v1/publish", tags=["Publish"])

# @app.get("/")
# async def root():
#     return {"message": "Welcome to MindCMS.ai 🚀"}






from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import content, publish  
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.core.ai_engine import generate_article, generate_seo_metadata

router = APIRouter()

class ContentInput(BaseModel):
    topic: str

app = FastAPI(
    title="MindCMS.ai",
    description="content management system",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[""],  
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)


app.include_router(content.router, prefix="/api/v1/content", tags=["Content"])


@app.get("/")
async def root():
    return {"message": "Welcome to MindCMS.ai"}


@router.post("/generate")
async def generate_content(data: ContentInput):
    try:
        article = await generate_article(data.topic)
        seo_meta = await generate_seo_metadata(data.topic)
        return {
            "article": article,
            "seo_metadata": seo_meta
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




