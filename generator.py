# from app.core.ai_engine import generate_article, generate_seo_metadata
# from app.db.connection import content_collection
# from app.db.models import ArticleModel
# import re

# async def generate_article_with_metadata(topic: str, category: str = None) -> dict:
#     # Step 1: Generate article text
#     article_text = await generate_article(topic, category)

#     # Step 2: Generate SEO metadata
#     seo_result = await generate_seo_metadata(article_text, topic)

#     # Step 3: Extract metadata from GPT response
#     seo_title = extract_field(seo_result, "title")
#     meta_description = extract_field(seo_result, "meta description")
#     keywords = extract_keywords(seo_result)

#     # Step 4: Save to MongoDB
#     article_data = ArticleModel(
#         topic=topic,
#         category=category,
#         content=article_text,
#         seo_title=seo_title,
#         meta_description=meta_description,
#         keywords=keywords
#     )
#     result = await content_collection.insert_one(article_data.dict(by_alias=True))
#     return {**article_data.dict(), "_id": str(result.inserted_id)}

# # Helpers to parse OpenAI output
# def extract_field(text: str, field: str) -> str:
#     pattern = rf"{field}:\s*(.*)"
#     match = re.search(pattern, text, re.IGNORECASE)
#     return match.group(1).strip() if match else "N/A"

# def extract_keywords(text: str) -> list[str]:
#     match = re.search(r"keywords:\s*(.*)", text, re.IGNORECASE)
#     if match:
#         keywords_str = match.group(1)
#         return [kw.strip() for kw in keywords_str.split(",")]
#     return []








import cohere
from app.core.config import settings

# Initialize the Cohere client with your API key
co = cohere.Client(settings.COHERE_API_KEY)

async def generate_content(title: str, description: str, keywords: str):
    prompt = f"""
    Write a well-optimized blog post for the web. 
    Title: {title}
    Description: {description}
    Keywords: {keywords}

    Make sure the content is SEO-friendly, engaging, and informative.
    """
    
    try:
        response = co.generate(
            model=settings.COHERE_MODEL,
            prompt=prompt,
            max_tokens=500,
            temperature=0.7
        )
        return response.generations[0].text.strip()
    except Exception as e:
        print("Error generating content:", e)
        return "Content generation failed due to an error."
