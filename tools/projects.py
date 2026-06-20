import urllib.parse
from langchain_core.tools import tool
from aria_agent.infrastructure.client import make_request, clean_id

@tool
def fetchAllDenyProjects() -> list:
    """Fetches details of all deny projects from the database (maps to /api/deny-projects)"""
    return make_request("/api/deny-projects")

@tool
def fetchDenyProjectById(idVal: str) -> dict:
    """Fetches details of a specific deny project by its unique ID (maps to /api/deny-projects/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid deny project ID format: {idVal}"}
    return make_request(f"/api/deny-projects/{cleaned}")

@tool
def fetchAllHrProjects() -> list:
    """Fetches details of all hr projects from the database (maps to /api/hr-projects)"""
    return make_request("/api/hr-projects")

@tool
def fetchHrProjectById(idVal: str) -> dict:
    """Fetches details of a specific hr project by its unique ID (maps to /api/hr-projects/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid hr project ID format: {idVal}"}
    return make_request(f"/api/hr-projects/{cleaned}")

@tool
def fetchAllHrProjectDetails() -> list:
    """Fetches details of all hr project details from the database (maps to /api/hr-project-details)"""
    return make_request("/api/hr-project-details")

@tool
def fetchHrProjectDetailById(idVal: str) -> dict:
    """Fetches details of a specific hr project detail by its unique ID (maps to /api/hr-project-details/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid hr project detail ID format: {idVal}"}
    return make_request(f"/api/hr-project-details/{cleaned}")

@tool
def fetchAllHrProjectTypes() -> list:
    """Fetches details of all hr project types from the database (maps to /api/hr-project-types)"""
    return make_request("/api/hr-project-types")

@tool
def fetchHrProjectTypeById(idVal: str) -> dict:
    """Fetches details of a specific hr project type by its unique ID (maps to /api/hr-project-types/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid hr project type ID format: {idVal}"}
    return make_request(f"/api/hr-project-types/{cleaned}")

@tool
def fetchAllHrStores() -> list:
    """Fetches details of all hr stores from the database (maps to /api/hr-stores)"""
    return make_request("/api/hr-stores")

@tool
def fetchHrStoreById(idVal: str) -> dict:
    """Fetches details of a specific hr store by its unique ID (maps to /api/hr-stores/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid hr store ID format: {idVal}"}
    return make_request(f"/api/hr-stores/{cleaned}")

@tool
def fetchAllPrChangeHistory() -> list:
    """Fetches details of all pr change history from the database (maps to /api/pr-change-history)"""
    return make_request("/api/pr-change-history")

@tool
def fetchPrChangeHistoryById(idVal: str) -> dict:
    """Fetches details of a specific pr change history by its unique ID (maps to /api/pr-change-history/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid pr change history ID format: {idVal}"}
    return make_request(f"/api/pr-change-history/{cleaned}")

@tool
def fetchAllPrCloseReasons() -> list:
    """Fetches details of all pr close reasons from the database (maps to /api/pr-close-reasons)"""
    return make_request("/api/pr-close-reasons")

@tool
def fetchPrCloseReasonById(idVal: str) -> dict:
    """Fetches details of a specific pr close reason by its unique ID (maps to /api/pr-close-reasons/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid pr close reason ID format: {idVal}"}
    return make_request(f"/api/pr-close-reasons/{cleaned}")

@tool
def fetchAllPrClosed() -> list:
    """Fetches details of all pr closed from the database (maps to /api/pr-closed)"""
    return make_request("/api/pr-closed")

@tool
def fetchPrClosedById(idVal: str) -> dict:
    """Fetches details of a specific pr closed by its unique ID (maps to /api/pr-closed/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid pr closed ID format: {idVal}"}
    return make_request(f"/api/pr-closed/{cleaned}")

@tool
def fetchAllPrCodeUpdates() -> list:
    """Fetches details of all pr code updates from the database (maps to /api/pr-code-updates)"""
    return make_request("/api/pr-code-updates")

@tool
def fetchPrCodeUpdateById(idVal: str) -> dict:
    """Fetches details of a specific pr code update by its unique ID (maps to /api/pr-code-updates/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid pr code update ID format: {idVal}"}
    return make_request(f"/api/pr-code-updates/{cleaned}")

@tool
def fetchAllPrDenyClosedProjects() -> list:
    """Fetches details of all pr deny closed projects from the database (maps to /api/pr-deny-closed-projects)"""
    return make_request("/api/pr-deny-closed-projects")

@tool
def fetchPrDenyClosedProjectByPCode(pCode: str) -> dict:
    """Fetches details of a specific pr deny closed project by its unique project code (maps to /api/pr-deny-closed-projects/{pCode})"""
    sanitized = urllib.parse.quote(pCode)
    return make_request(f"/api/pr-deny-closed-projects/{sanitized}")

@tool
def fetchAllPrDenyProjects() -> list:
    """Fetches details of all pr deny projects from the database (maps to /api/pr-deny-projects)"""
    return make_request("/api/pr-deny-projects")

@tool
def fetchPrDenyProjectById(idVal: str) -> dict:
    """Fetches details of a specific pr deny project by its unique ID (maps to /api/pr-deny-projects/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid pr deny project ID format: {idVal}"}
    return make_request(f"/api/pr-deny-projects/{cleaned}")

@tool
def fetchAllPrExtends() -> list:
    """Fetches details of all pr extends from the database (maps to /api/pr-extends)"""
    return make_request("/api/pr-extends")

@tool
def fetchPrExtendById(idVal: str) -> dict:
    """Fetches details of a specific pr extend by its unique ID (maps to /api/pr-extends/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid pr extend ID format: {idVal}"}
    return make_request(f"/api/pr-extends/{cleaned}")

@tool
def fetchAllPrPastEnds() -> list:
    """Fetches details of all pr past ends from the database (maps to /api/pr-past-ends)"""
    return make_request("/api/pr-past-ends")

@tool
def fetchPrPastEndById(idVal: str) -> dict:
    """Fetches details of a specific pr past end by its unique ID (maps to /api/pr-past-ends/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid pr past end ID format: {idVal}"}
    return make_request(f"/api/pr-past-ends/{cleaned}")

@tool
def fetchAllPrProjects() -> list:
    """Fetches details of all pr projects from the database (maps to /api/pr-projects)"""
    return make_request("/api/pr-projects")

@tool
def fetchPrProjectBySerialNo(serialNo: str) -> dict:
    """Fetches details of a specific pr project by its unique serial number (maps to /api/pr-projects/{serialNo})"""
    cleaned = clean_id(serialNo)
    if not cleaned:
        return {"error": f"Invalid pr project serial number format: {serialNo}"}
    return make_request(f"/api/pr-projects/{cleaned}")

@tool
def fetchAllPrProjectAPCodes() -> list:
    """Fetches details of all pr project a p codes from the database (maps to /api/pr-project-ap-codes)"""
    return make_request("/api/pr-project-ap-codes")

@tool
def fetchPrProjectAPCodeById(idVal: str) -> dict:
    """Fetches details of a specific pr project a p code by its unique ID (maps to /api/pr-project-ap-codes/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid pr project a p code ID format: {idVal}"}
    return make_request(f"/api/pr-project-ap-codes/{cleaned}")

@tool
def fetchAllPrProjectTypes() -> list:
    """Fetches details of all pr project types from the database (maps to /api/pr-project-types)"""
    return make_request("/api/pr-project-types")

@tool
def fetchPrProjectTypeByPtCode(ptCode: str) -> dict:
    """Fetches details of a specific pr project type by its unique project type code (maps to /api/pr-project-types/{ptCode})"""
    cleaned = clean_id(ptCode)
    if not cleaned:
        return {"error": f"Invalid pr project type project type code format: {ptCode}"}
    return make_request(f"/api/pr-project-types/{cleaned}")

@tool
def fetchAllPrProjectTypes2() -> list:
    """Fetches details of all pr project types2 from the database (maps to /api/pr-project-types-2)"""
    return make_request("/api/pr-project-types-2")

@tool
def fetchPrProjectType2ById(idVal: str) -> dict:
    """Fetches details of a specific pr project type2 by its unique ID (maps to /api/pr-project-types-2/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid pr project type2 ID format: {idVal}"}
    return make_request(f"/api/pr-project-types-2/{cleaned}")

@tool
def fetchAllPrStores() -> list:
    """Fetches details of all pr stores from the database (maps to /api/pr-stores)"""
    return make_request("/api/pr-stores")

@tool
def fetchPrStoreById(idVal: str) -> dict:
    """Fetches details of a specific pr store by its unique ID (maps to /api/pr-stores/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid pr store ID format: {idVal}"}
    return make_request(f"/api/pr-stores/{cleaned}")
