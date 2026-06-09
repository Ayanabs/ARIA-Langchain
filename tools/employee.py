from langchain_core.tools import tool
from .base import make_request, clean_id

@tool
def fetchAllEmployees() -> list:
    """Fetches details of all employees from the database (maps to /api/employees)"""
    return make_request("/api/employees")

@tool
def fetchEmployeeById(idVal: str) -> dict:
    """Fetches details of a specific employee by their unique ID (maps to /api/employees/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid employee ID format: {idVal}"}
    return make_request(f"/api/employees/{cleaned}")

@tool
def fetchEmployeeByEmail(email: str) -> dict:
    """Fetches employee details by their email address (maps to /api/employees/email/{email})"""
    return make_request(f"/api/employees/email/{email}")

@tool
def fetchEmployeeByEmpno(empno: str) -> dict:
    """Fetches employee details by their employee number (maps to /api/employees/empno/{empno})"""
    cleaned = clean_id(empno)
    if not cleaned:
        return {"error": f"Invalid employee number format: {empno}"}
    return make_request(f"/api/employees/empno/{cleaned}")

@tool
def fetchEmployeeByNicnum(nicnum: str) -> dict:
    """Fetches employee details by their National Identity Card (NIC) number (maps to /api/employees/nic/{nicnum})"""
    return make_request(f"/api/employees/nic/{nicnum}")

@tool
def fetchEmployeesByPhone(phone: str) -> list:
    """Fetches a list of employees matching a phone or mobile number (maps to /api/employees/phone/{phone})"""
    return make_request(f"/api/employees/phone/{phone}")
