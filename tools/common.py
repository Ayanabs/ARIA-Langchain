from langchain_core.tools import tool
from aria_agent.infrastructure.client import make_request, clean_id

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

@tool
def fetchAllClaimTypes() -> list:
    """Fetches details of all claim types from the database (maps to /api/claim-types)"""
    return make_request("/api/claim-types")

@tool
def fetchClaimTypeById(idVal: str) -> dict:
    """Fetches details of a specific claim type by its unique ID (maps to /api/claim-types/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid claim type ID format: {idVal}"}
    return make_request(f"/api/claim-types/{cleaned}")

@tool
def fetchAllDayTypes() -> list:
    """Fetches details of all day types from the database (maps to /api/day-types)"""
    return make_request("/api/day-types")

@tool
def fetchDayTypeById(idVal: str) -> dict:
    """Fetches details of a specific day type by its unique ID (maps to /api/day-types/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid day type ID format: {idVal}"}
    return make_request(f"/api/day-types/{cleaned}")

@tool
def fetchAllIncompleteSources() -> list:
    """Fetches details of all incomplete sources from the database (maps to /api/incomplete-sources)"""
    return make_request("/api/incomplete-sources")

@tool
def fetchIncompleteSourceById(idVal: str) -> dict:
    """Fetches details of a specific incomplete source by its unique ID (maps to /api/incomplete-sources/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid incomplete source ID format: {idVal}"}
    return make_request(f"/api/incomplete-sources/{cleaned}")

@tool
def fetchAllIssues() -> list:
    """Fetches details of all issues from the database (maps to /api/issues)"""
    return make_request("/api/issues")

@tool
def fetchIssueByAttDtId(attDtId: str) -> dict:
    """Fetches details of a specific issue by its unique attendance date ID (maps to /api/issues/{attDtId})"""
    cleaned = clean_id(attDtId)
    if not cleaned:
        return {"error": f"Invalid issue attendance date ID format: {attDtId}"}
    return make_request(f"/api/issues/{cleaned}")

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
