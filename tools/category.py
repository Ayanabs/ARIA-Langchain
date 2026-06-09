from langchain_core.tools import tool
from .base import make_request, clean_id

@tool
def fetchAllCategories() -> list:
    """Fetches details of all categories from the database (maps to /api/categories)"""
    return make_request("/api/categories")

@tool
def fetchCategoryById(idVal: str) -> dict:
    """Fetches details of a specific category by its unique ID (maps to /api/categories/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid category ID format: {idVal}"}
    return make_request(f"/api/categories/{cleaned}")
