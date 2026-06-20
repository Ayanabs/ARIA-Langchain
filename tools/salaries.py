import urllib.parse
from langchain_core.tools import tool
from aria_agent.infrastructure.client import make_request, clean_id

@tool
def fetchAllDivBudgets() -> list:
    """Fetches details of all div budgets from the database (maps to /api/div-budgets)"""
    return make_request("/api/div-budgets")

@tool
def fetchDivBudgetById(idVal: str) -> dict:
    """Fetches details of a specific div budget by its unique ID (maps to /api/div-budgets/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid div budget ID format: {idVal}"}
    return make_request(f"/api/div-budgets/{cleaned}")

@tool
def fetchAllHrSalaryAllDetails() -> list:
    """Fetches details of all hr salary all details from the database (maps to /api/hr-salary-all-details)"""
    return make_request("/api/hr-salary-all-details")

@tool
def fetchHrSalaryAllDetailById(idVal: str) -> dict:
    """Fetches details of a specific hr salary all detail by its unique ID (maps to /api/hr-salary-all-details/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid hr salary all detail ID format: {idVal}"}
    return make_request(f"/api/hr-salary-all-details/{cleaned}")

@tool
def fetchAllHrSalaryDetails() -> list:
    """Fetches details of all hr salary details from the database (maps to /api/hr-salary-details)"""
    return make_request("/api/hr-salary-details")

@tool
def fetchHrSalaryDetailById(idVal: str) -> dict:
    """Fetches details of a specific hr salary detail by its unique ID (maps to /api/hr-salary-details/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid hr salary detail ID format: {idVal}"}
    return make_request(f"/api/hr-salary-details/{cleaned}")

@tool
def fetchAllHrSalaryScales() -> list:
    """Fetches details of all hr salary scales from the database (maps to /api/hr-salary-scales)"""
    return make_request("/api/hr-salary-scales")

@tool
def fetchHrSalaryScaleById(idVal: str) -> dict:
    """Fetches details of a specific hr salary scale by its unique ID (maps to /api/hr-salary-scales/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid hr salary scale ID format: {idVal}"}
    return make_request(f"/api/hr-salary-scales/{cleaned}")

@tool
def fetchAllHrSalaryScaleDetails() -> list:
    """Fetches details of all hr salary scale details from the database (maps to /api/hr-salary-scale-details)"""
    return make_request("/api/hr-salary-scale-details")

@tool
def fetchHrSalaryScaleDetailById(idVal: str) -> dict:
    """Fetches details of a specific hr salary scale detail by its unique ID (maps to /api/hr-salary-scale-details/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid hr salary scale detail ID format: {idVal}"}
    return make_request(f"/api/hr-salary-scale-details/{cleaned}")

@tool
def fetchAllHrSalaryTable() -> list:
    """Fetches details of all hr salary table from the database (maps to /api/hr-salary-table)"""
    return make_request("/api/hr-salary-table")

@tool
def fetchHrSalaryTableById(idVal: str) -> dict:
    """Fetches details of a specific hr salary table by its unique ID (maps to /api/hr-salary-table/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid hr salary table ID format: {idVal}"}
    return make_request(f"/api/hr-salary-table/{cleaned}")

@tool
def fetchAllHrTempSalaryInfo() -> list:
    """Fetches details of all hr temp salary info from the database (maps to /api/hr-temp-salary-info)"""
    return make_request("/api/hr-temp-salary-info")

@tool
def fetchHrTempSalaryInfoByEmpNo(empNo: str) -> dict:
    """Fetches details of a specific hr temp salary info by its unique employee number (maps to /api/hr-temp-salary-info/{empNo})"""
    cleaned = clean_id(empNo)
    if not cleaned:
        return {"error": f"Invalid hr temp salary info employee number format: {empNo}"}
    return make_request(f"/api/hr-temp-salary-info/{cleaned}")

@tool
def fetchAllSalaryScales() -> list:
    """Fetches details of all salary scales from the database (maps to /api/salary-scales)"""
    return make_request("/api/salary-scales")

@tool
def fetchSalaryScaleByCode(code: str) -> dict:
    """Fetches details of a specific salary scale by its unique salary code (maps to /api/salary-scales/{id})"""
    sanitized = urllib.parse.quote(code)
    return make_request(f"/api/salary-scales/{sanitized}")
