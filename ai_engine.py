import cohere
from app.core.config import settings

co = cohere.Client(settings.COHERE_API_KEY)

async def generate_article(topic: str, category: str = None) -> str:
    prompt = f"""
    Write a detailed, SEO-optimized article (1000+ words) on the topic: "{topic}".
    {'Category: ' + category if category else ''}
    Structure the content with H1, H2, and H3 headers, use bullet points where necessary, and ensure it's engaging for online readers.
    """

    try:
        response = co.generate(
            model=settings.COHERE_MODEL,
            prompt=prompt,
            max_tokens=1000,
            temperature=0.7
        )
        return response.generations[0].text.strip()
    except Exception as e:
        print("Error generating article:", e)
        return "Failed to generate article."

async def generate_seo_metadata(article_text: str, topic: str) -> str:
    prompt = f"""
    Based on the following article, generate:
    - A compelling SEO title
    - A short meta description (max 160 characters)
    - 5 relevant keywords (comma-separated)

    Article: {article_text}
    """

    try:
        response = co.generate(
            model=settings.COHERE_MODEL,
            prompt=prompt,
            max_tokens=300,
            temperature=0.5
        )
        return response.generations[0].text.strip()
    except Exception as e:
        print("Error generating SEO metadata:", e)
        return "Failed to generate SEO metadata."
