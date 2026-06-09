from langchain_core.tools import tool
from .base import make_request, clean_id

@tool
def fetchAllDesignations() -> list:
    """Fetches details of all designations from the database (maps to /api/designations)"""
    return make_request("/api/designations")

@tool
def fetchDesignationById(idVal: str) -> dict:
    """Fetches details of a specific designation by its unique ID (maps to /api/designations/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid designation ID format: {idVal}"}
    return make_request(f"/api/designations/{cleaned}")
