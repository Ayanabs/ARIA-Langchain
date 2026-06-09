from langchain_core.tools import tool
from aria_agent.infrastructure.client import make_request, clean_id

@tool
def fetchAllEmployeeTypes() -> list:
    """Fetches details of all employee types from the database (maps to /api/employee-types)"""
    return make_request("/api/employee-types")

@tool
def fetchEmployeeTypeById(idVal: str) -> dict:
    """Fetches details of a specific employee type by its unique ID (maps to /api/employee-types/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid employee type ID format: {idVal}"}
    return make_request(f"/api/employee-types/{cleaned}")
