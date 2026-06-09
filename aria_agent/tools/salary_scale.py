from langchain_core.tools import tool
from aria_agent.infrastructure.client import make_request

@tool
def fetchAllSalaryScales() -> list:
    """Fetches details of all salary scales from the database (maps to /api/salary-scales)"""
    return make_request("/api/salary-scales")

@tool
def fetchSalaryScaleByCode(code: str) -> dict:
    """Fetches details of a specific salary scale by its unique salary code (maps to /api/salary-scales/{code})"""
    return make_request(f"/api/salary-scales/{code}")
