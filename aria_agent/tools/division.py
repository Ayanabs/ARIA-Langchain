from langchain_core.tools import tool
from aria_agent.infrastructure.client import make_request, clean_id

@tool
def fetchAllDivisions() -> list:
    """Fetches details of all divisions from the database (maps to /api/divisions)"""
    return make_request("/api/divisions")

@tool
def fetchDivisionById(idVal: str) -> dict:
    """Fetches details of a specific division by its unique ID (maps to /api/divisions/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid division ID format: {idVal}"}
    return make_request(f"/api/divisions/{cleaned}")
