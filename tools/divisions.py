from langchain_core.tools import tool
from aria_agent.infrastructure.client import make_request, clean_id

@tool
def fetchAllComDivisions() -> list:
    """Fetches details of all com divisions from the database (maps to /api/com-divisions)"""
    return make_request("/api/com-divisions")

@tool
def fetchComDivisionById(idVal: str) -> dict:
    """Fetches details of a specific com division by its unique ID (maps to /api/com-divisions/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid com division ID format: {idVal}"}
    return make_request(f"/api/com-divisions/{cleaned}")

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

@tool
def fetchAllHrDivisions() -> list:
    """Fetches details of all hr divisions from the database (maps to /api/hr-divisions)"""
    return make_request("/api/hr-divisions")

@tool
def fetchHrDivisionById(idVal: str) -> dict:
    """Fetches details of a specific hr division by its unique ID (maps to /api/hr-divisions/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid hr division ID format: {idVal}"}
    return make_request(f"/api/hr-divisions/{cleaned}")

@tool
def fetchAllMainSubDivisions() -> list:
    """Fetches details of all main sub divisions from the database (maps to /api/main-sub-divisions)"""
    return make_request("/api/main-sub-divisions")

@tool
def fetchMainSubDivisionById(idVal: str) -> dict:
    """Fetches details of a specific main sub division by its unique ID (maps to /api/main-sub-divisions/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid main sub division ID format: {idVal}"}
    return make_request(f"/api/main-sub-divisions/{cleaned}")

@tool
def fetchAllSaLocations() -> list:
    """Fetches details of all sa locations from the database (maps to /api/sa-locations)"""
    return make_request("/api/sa-locations")

@tool
def fetchSaLocationById(idVal: str) -> dict:
    """Fetches details of a specific sa location by its unique ID (maps to /api/sa-locations/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid sa location ID format: {idVal}"}
    return make_request(f"/api/sa-locations/{cleaned}")
