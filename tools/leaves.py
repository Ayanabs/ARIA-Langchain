from langchain_core.tools import tool
from aria_agent.infrastructure.client import make_request, clean_id

@tool
def fetchAllLeaveActing() -> list:
    """Fetches details of all leave acting from the database (maps to /api/leave-acting)"""
    return make_request("/api/leave-acting")

@tool
def fetchLeaveActingById(idVal: str) -> dict:
    """Fetches details of a specific leave acting by its unique ID (maps to /api/leave-acting/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid leave acting ID format: {idVal}"}
    return make_request(f"/api/leave-acting/{cleaned}")

@tool
def fetchAllLeaveDates() -> list:
    """Fetches details of all leave dates from the database (maps to /api/leave-dates)"""
    return make_request("/api/leave-dates")

@tool
def fetchLeaveDateById(idVal: str) -> dict:
    """Fetches details of a specific leave date by its unique ID (maps to /api/leave-dates/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid leave date ID format: {idVal}"}
    return make_request(f"/api/leave-dates/{cleaned}")

@tool
def fetchAllLeaveHeads() -> list:
    """Fetches details of all leave heads from the database (maps to /api/leave-heads)"""
    return make_request("/api/leave-heads")

@tool
def fetchLeaveHeadById(idVal: str) -> dict:
    """Fetches details of a specific leave head by its unique ID (maps to /api/leave-heads/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid leave head ID format: {idVal}"}
    return make_request(f"/api/leave-heads/{cleaned}")

@tool
def fetchAllLeaveHeadsPr() -> list:
    """Fetches details of all leave heads pr from the database (maps to /api/leave-heads-pr)"""
    return make_request("/api/leave-heads-pr")

@tool
def fetchLeaveHeadPrById(idVal: str) -> dict:
    """Fetches details of a specific leave head pr by its unique ID (maps to /api/leave-heads-pr/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid leave head pr ID format: {idVal}"}
    return make_request(f"/api/leave-heads-pr/{cleaned}")
