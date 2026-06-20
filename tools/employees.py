import urllib.parse
from langchain_core.tools import tool
from aria_agent.infrastructure.client import make_request, clean_id

@tool
def fetchAllDesignations() -> list:
    """Fetches details of all designations from the database (maps to /api/designations)"""
    return make_request("/api/designations")

@tool
def fetchDesignationById(idVal: str) -> dict:
    """Fetches details of a specific designation by its unique ID (maps to /api/designations/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid designation ID format: {idVal}"}
    return make_request(f"/api/designations/{cleaned}")

@tool
def fetchAllEmpCleanings() -> list:
    """Fetches details of all emp cleanings from the database (maps to /api/emp-cleanings)"""
    return make_request("/api/emp-cleanings")

@tool
def fetchEmpCleaningById(idVal: str) -> dict:
    """Fetches details of a specific emp cleaning by its unique ID (maps to /api/emp-cleanings/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid emp cleaning ID format: {idVal}"}
    return make_request(f"/api/emp-cleanings/{cleaned}")

@tool
def fetchAllEmpGrades() -> list:
    """Fetches details of all emp grades from the database (maps to /api/emp-grades)"""
    return make_request("/api/emp-grades")

@tool
def fetchEmpGradeById(idVal: str) -> dict:
    """Fetches details of a specific emp grade by its unique ID (maps to /api/emp-grades/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid emp grade ID format: {idVal}"}
    return make_request(f"/api/emp-grades/{cleaned}")

@tool
def fetchAllEmpLeaves() -> list:
    """Fetches details of all emp leaves from the database (maps to /api/emp-leaves)"""
    return make_request("/api/emp-leaves")

@tool
def fetchEmpLeaveById(idVal: str) -> dict:
    """Fetches details of a specific emp leave by its unique ID (maps to /api/emp-leaves/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid emp leave ID format: {idVal}"}
    return make_request(f"/api/emp-leaves/{cleaned}")

@tool
def fetchAllEmpLeavesBkp() -> list:
    """Fetches details of all emp leaves bkp from the database (maps to /api/emp-leaves-bkp)"""
    return make_request("/api/emp-leaves-bkp")

@tool
def fetchEmpLeaveBkpById(idVal: str) -> dict:
    """Fetches details of a specific emp leave bkp by its unique ID (maps to /api/emp-leaves-bkp/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid emp leave bkp ID format: {idVal}"}
    return make_request(f"/api/emp-leaves-bkp/{cleaned}")

@tool
def fetchAllEmpSecurities() -> list:
    """Fetches details of all emp securities from the database (maps to /api/emp-securities)"""
    return make_request("/api/emp-securities")

@tool
def fetchEmpSecurityById(idVal: str) -> dict:
    """Fetches details of a specific emp security by its unique ID (maps to /api/emp-securities/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid emp security ID format: {idVal}"}
    return make_request(f"/api/emp-securities/{cleaned}")

@tool
def fetchAllEmpShortLeaves() -> list:
    """Fetches details of all emp short leaves from the database (maps to /api/emp-short-leaves)"""
    return make_request("/api/emp-short-leaves")

@tool
def fetchEmpShortLeaveById(idVal: str) -> dict:
    """Fetches details of a specific emp short leave by its unique ID (maps to /api/emp-short-leaves/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid emp short leave ID format: {idVal}"}
    return make_request(f"/api/emp-short-leaves/{cleaned}")

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
    sanitized = urllib.parse.quote(email)
    return make_request(f"/api/employees/email/{sanitized}")

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
    sanitized = urllib.parse.quote(nicnum)
    return make_request(f"/api/employees/nic/{sanitized}")

@tool
def fetchEmployeesByPhone(phone: str) -> list:
    """Fetches a list of employees matching a phone or mobile number (maps to /api/employees/phone/{phone})"""
    sanitized = urllib.parse.quote(phone)
    return make_request(f"/api/employees/phone/{sanitized}")

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

@tool
def fetchAllHrDepDetails() -> list:
    """Fetches details of all hr dep details from the database (maps to /api/hr-dep-details)"""
    return make_request("/api/hr-dep-details")

@tool
def fetchHrDepDetailById(idVal: str) -> dict:
    """Fetches details of a specific hr dep detail by its unique ID (maps to /api/hr-dep-details/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid hr dep detail ID format: {idVal}"}
    return make_request(f"/api/hr-dep-details/{cleaned}")

@tool
def fetchAllHrDependentRelationships() -> list:
    """Fetches details of all hr dependent relationships from the database (maps to /api/hr-dependent-relationships)"""
    return make_request("/api/hr-dependent-relationships")

@tool
def fetchHrDependentRelationshipById(idVal: str) -> dict:
    """Fetches details of a specific hr dependent relationship by its unique ID (maps to /api/hr-dependent-relationships/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid hr dependent relationship ID format: {idVal}"}
    return make_request(f"/api/hr-dependent-relationships/{cleaned}")

@tool
def fetchAllHrDesigCadres() -> list:
    """Fetches details of all hr desig cadres from the database (maps to /api/hr-desig-cadres)"""
    return make_request("/api/hr-desig-cadres")

@tool
def fetchHrDesigCadreById(idVal: str) -> dict:
    """Fetches details of a specific hr desig cadre by its unique ID (maps to /api/hr-desig-cadres/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid hr desig cadre ID format: {idVal}"}
    return make_request(f"/api/hr-desig-cadres/{cleaned}")

@tool
def fetchAllHrDesignations() -> list:
    """Fetches details of all hr designations from the database (maps to /api/hr-designations)"""
    return make_request("/api/hr-designations")

@tool
def fetchHrDesignationById(idVal: str) -> dict:
    """Fetches details of a specific hr designation by its unique ID (maps to /api/hr-designations/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid hr designation ID format: {idVal}"}
    return make_request(f"/api/hr-designations/{cleaned}")

@tool
def fetchAllHrEduLevels() -> list:
    """Fetches details of all hr edu levels from the database (maps to /api/hr-edu-levels)"""
    return make_request("/api/hr-edu-levels")

@tool
def fetchHrEduLevelById(idVal: str) -> dict:
    """Fetches details of a specific hr edu level by its unique ID (maps to /api/hr-edu-levels/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid hr edu level ID format: {idVal}"}
    return make_request(f"/api/hr-edu-levels/{cleaned}")

@tool
def fetchAllHrEduLevelsDes() -> list:
    """Fetches details of all hr edu levels des from the database (maps to /api/hr-edu-levels-des)"""
    return make_request("/api/hr-edu-levels-des")

@tool
def fetchHrEduLevelDesById(idVal: str) -> dict:
    """Fetches details of a specific hr edu level des by its unique ID (maps to /api/hr-edu-levels-des/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid hr edu level des ID format: {idVal}"}
    return make_request(f"/api/hr-edu-levels-des/{cleaned}")

@tool
def fetchAllHrHigherEduDetails() -> list:
    """Fetches details of all hr higher edu details from the database (maps to /api/hr-higher-edu-details)"""
    return make_request("/api/hr-higher-edu-details")

@tool
def fetchHrHigherEduDetailById(idVal: str) -> dict:
    """Fetches details of a specific hr higher edu detail by its unique ID (maps to /api/hr-higher-edu-details/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid hr higher edu detail ID format: {idVal}"}
    return make_request(f"/api/hr-higher-edu-details/{cleaned}")

@tool
def fetchAllHrIncrementReports() -> list:
    """Fetches details of all hr increment reports from the database (maps to /api/hr-increment-reports)"""
    return make_request("/api/hr-increment-reports")

@tool
def fetchHrIncrementReportById(idVal: str) -> dict:
    """Fetches details of a specific hr increment report by its unique ID (maps to /api/hr-increment-reports/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid hr increment report ID format: {idVal}"}
    return make_request(f"/api/hr-increment-reports/{cleaned}")

@tool
def fetchAllHrOfficialDetails() -> list:
    """Fetches details of all hr official details from the database (maps to /api/hr-official-details)"""
    return make_request("/api/hr-official-details")

@tool
def fetchHrOfficialDetailById(idVal: str) -> dict:
    """Fetches details of a specific hr official detail by its unique ID (maps to /api/hr-official-details/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid hr official detail ID format: {idVal}"}
    return make_request(f"/api/hr-official-details/{cleaned}")

@tool
def fetchAllHrPersonalDetails() -> list:
    """Fetches details of all hr personal details from the database (maps to /api/hr-personal-details)"""
    return make_request("/api/hr-personal-details")

@tool
def fetchHrPersonalDetailById(idVal: str) -> dict:
    """Fetches details of a specific hr personal detail by its unique ID (maps to /api/hr-personal-details/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid hr personal detail ID format: {idVal}"}
    return make_request(f"/api/hr-personal-details/{cleaned}")

@tool
def fetchAllHrQAL() -> list:
    """Fetches details of all hr q a l from the database (maps to /api/hr-q-al)"""
    return make_request("/api/hr-q-al")

@tool
def fetchHrQALById(idVal: str) -> dict:
    """Fetches details of a specific hr q a l by its unique ID (maps to /api/hr-q-al/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid hr q a l ID format: {idVal}"}
    return make_request(f"/api/hr-q-al/{cleaned}")

@tool
def fetchAllHrQALSubjects() -> list:
    """Fetches details of all hr q a l subjects from the database (maps to /api/hr-q-al-subjects)"""
    return make_request("/api/hr-q-al-subjects")

@tool
def fetchHrQALSubjectById(idVal: str) -> dict:
    """Fetches details of a specific hr q a l subject by its unique ID (maps to /api/hr-q-al-subjects/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid hr q a l subject ID format: {idVal}"}
    return make_request(f"/api/hr-q-al-subjects/{cleaned}")

@tool
def fetchAllHrQClasses() -> list:
    """Fetches details of all hr q classes from the database (maps to /api/hr-q-classes)"""
    return make_request("/api/hr-q-classes")

@tool
def fetchHrQClassById(idVal: str) -> dict:
    """Fetches details of a specific hr q class by its unique ID (maps to /api/hr-q-classes/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid hr q class ID format: {idVal}"}
    return make_request(f"/api/hr-q-classes/{cleaned}")

@tool
def fetchAllHrQExperience() -> list:
    """Fetches details of all hr q experience from the database (maps to /api/hr-q-experience)"""
    return make_request("/api/hr-q-experience")

@tool
def fetchHrQExperienceById(idVal: str) -> dict:
    """Fetches details of a specific hr q experience by its unique ID (maps to /api/hr-q-experience/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid hr q experience ID format: {idVal}"}
    return make_request(f"/api/hr-q-experience/{cleaned}")

@tool
def fetchAllHrQGrades() -> list:
    """Fetches details of all hr q grades from the database (maps to /api/hr-q-grades)"""
    return make_request("/api/hr-q-grades")

@tool
def fetchHrQGradeById(idVal: str) -> dict:
    """Fetches details of a specific hr q grade by its unique ID (maps to /api/hr-q-grades/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid hr q grade ID format: {idVal}"}
    return make_request(f"/api/hr-q-grades/{cleaned}")

@tool
def fetchAllHrQHiEdu() -> list:
    """Fetches details of all hr q hi edu from the database (maps to /api/hr-q-hi-edu)"""
    return make_request("/api/hr-q-hi-edu")

@tool
def fetchHrQHiEduById(idVal: str) -> dict:
    """Fetches details of a specific hr q hi edu by its unique ID (maps to /api/hr-q-hi-edu/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid hr q hi edu ID format: {idVal}"}
    return make_request(f"/api/hr-q-hi-edu/{cleaned}")

@tool
def fetchAllHrQHiEduProjects() -> list:
    """Fetches details of all hr q hi edu projects from the database (maps to /api/hr-q-hi-edu-projects)"""
    return make_request("/api/hr-q-hi-edu-projects")

@tool
def fetchHrQHiEduProjectById(idVal: str) -> dict:
    """Fetches details of a specific hr q hi edu project by its unique ID (maps to /api/hr-q-hi-edu-projects/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid hr q hi edu project ID format: {idVal}"}
    return make_request(f"/api/hr-q-hi-edu-projects/{cleaned}")

@tool
def fetchAllHrQHiEduQualifications() -> list:
    """Fetches details of all hr q hi edu qualifications from the database (maps to /api/hr-q-hi-edu-qualifications)"""
    return make_request("/api/hr-q-hi-edu-qualifications")

@tool
def fetchHrQHiEduQualificationById(idVal: str) -> dict:
    """Fetches details of a specific hr q hi edu qualification by its unique ID (maps to /api/hr-q-hi-edu-qualifications/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid hr q hi edu qualification ID format: {idVal}"}
    return make_request(f"/api/hr-q-hi-edu-qualifications/{cleaned}")

@tool
def fetchAllHrQInstitutes() -> list:
    """Fetches details of all hr q institutes from the database (maps to /api/hr-q-institutes)"""
    return make_request("/api/hr-q-institutes")

@tool
def fetchHrQInstituteById(idVal: str) -> dict:
    """Fetches details of a specific hr q institute by its unique ID (maps to /api/hr-q-institutes/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid hr q institute ID format: {idVal}"}
    return make_request(f"/api/hr-q-institutes/{cleaned}")

@tool
def fetchAllHrQOL() -> list:
    """Fetches details of all hr q o l from the database (maps to /api/hr-q-ol)"""
    return make_request("/api/hr-q-ol")

@tool
def fetchHrQOLById(idVal: str) -> dict:
    """Fetches details of a specific hr q o l by its unique ID (maps to /api/hr-q-ol/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid hr q o l ID format: {idVal}"}
    return make_request(f"/api/hr-q-ol/{cleaned}")

@tool
def fetchAllHrQOLSubjects() -> list:
    """Fetches details of all hr q o l subjects from the database (maps to /api/hr-q-ol-subjects)"""
    return make_request("/api/hr-q-ol-subjects")

@tool
def fetchHrQOLSubjectById(idVal: str) -> dict:
    """Fetches details of a specific hr q o l subject by its unique ID (maps to /api/hr-q-ol-subjects/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid hr q o l subject ID format: {idVal}"}
    return make_request(f"/api/hr-q-ol-subjects/{cleaned}")

@tool
def fetchAllPositions() -> list:
    """Fetches details of all positions from the database (maps to /api/positions)"""
    return make_request("/api/positions")

@tool
def fetchPositionById(idVal: str) -> dict:
    """Fetches details of a specific position by its unique ID (maps to /api/positions/{id})"""
    cleaned = clean_id(idVal)
    if not cleaned:
        return {"error": f"Invalid position ID format: {idVal}"}
    return make_request(f"/api/positions/{cleaned}")
