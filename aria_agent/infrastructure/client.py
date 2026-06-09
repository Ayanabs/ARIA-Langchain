import re
import contextvars
import requests
from typing import Any
from aria_agent.config import SPRING_BOOT_BASE_URL, logger

# Context variables to track agent API routings for each individual query execution request
called_endpoints_var = contextvars.ContextVar("called_endpoints", default=[])
raw_results_var = contextvars.ContextVar("raw_results", default=[])

def make_request(endpoint: str) -> Any:
    """Makes a GET request to the target Spring Boot endpoint and logs the routing path."""
    url = f"{SPRING_BOOT_BASE_URL}{endpoint}"
    
    endpoints = list(called_endpoints_var.get())
    endpoints.append(endpoint)
    called_endpoints_var.set(endpoints)
    
    try:
        logger.info(f"Tool calling API: {url}")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        results = list(raw_results_var.get())
        results.append(data)
        raw_results_var.set(results)
        
        return data
    except Exception as e:
        logger.error(f"Error calling {url}: {str(e)}")
        error_res = {"error": f"Failed to fetch from {endpoint}: {str(e)}"}
        
        results = list(raw_results_var.get())
        results.append(error_res)
        raw_results_var.set(results)
        
        return error_res

def clean_id(id_val: Any) -> str:
    """Removes non-numeric characters from IDs for security and formatting."""
    return re.sub(r'[^0-9]', '', str(id_val))
