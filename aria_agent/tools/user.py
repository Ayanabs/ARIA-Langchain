from langchain_core.tools import tool
from aria_agent.infrastructure.client import make_request, clean_id

@tool
def fetchAllUsers() -> list:
    """Fetches details of all users from the database (maps to /api/users)"""
    return make_request("/api/users")

@tool
def fetchUserById(idVal: str) -> dict:
    """Fetches details of a specific user by their unique ID (maps to /api/users/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid user ID format: {idVal}"}
    return make_request(f"/api/users/{cleaned}")
