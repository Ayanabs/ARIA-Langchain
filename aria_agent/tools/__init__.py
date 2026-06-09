from aria_agent.infrastructure.client import called_endpoints_var, raw_results_var
from .category import fetchAllCategories, fetchCategoryById
from .designation import fetchAllDesignations, fetchDesignationById
from .division import fetchAllDivisions, fetchDivisionById
from .employee_type import fetchAllEmployeeTypes, fetchEmployeeTypeById
from .salary_scale import fetchAllSalaryScales, fetchSalaryScaleByCode
from .employee import (
    fetchAllEmployees,
    fetchEmployeeById,
    fetchEmployeeByEmail,
    fetchEmployeeByEmpno,
    fetchEmployeeByNicnum,
    fetchEmployeesByPhone
)
from .user import fetchAllUsers, fetchUserById

all_tools = [
    fetchAllCategories,
    fetchCategoryById,
    fetchAllDesignations,
    fetchDesignationById,
    fetchAllDivisions,
    fetchDivisionById,
    fetchAllEmployeeTypes,
    fetchEmployeeTypeById,
    fetchAllSalaryScales,
    fetchSalaryScaleByCode,
    fetchAllEmployees,
    fetchEmployeeById,
    fetchEmployeeByEmail,
    fetchEmployeeByEmpno,
    fetchEmployeeByNicnum,
    fetchEmployeesByPhone,
    fetchAllUsers,
    fetchUserById
]
