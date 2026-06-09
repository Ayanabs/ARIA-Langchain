import os
import re
import logging
import contextvars
import requests
from typing import Any


logger = logging.getLogger("langchain-agent.tools")


called_endpoints_var = contextvars.ContextVar("called_endpoints", default=[])
raw_results_var = contextvars.ContextVar("raw_results", default=[])

SPRING_BOOT_BASE_URL = os.getenv("SPRING_BOOT_BASE_URL", "http://localhost:8080")

def make_request(endpoint: str) -> Any:
    url = f"{SPRING_BOOT_BASE_URL}{endpoint}"
    
    endpoints = called_endpoints_var.get()
    endpoints.append(endpoint)
    called_endpoints_var.set(endpoints)
    
    try:
        logger.info(f"Tool calling API: {url}")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        
        results = raw_results_var.get()
        results.append(data)
        raw_results_var.set(results)
        
        return data
    except Exception as e:
        logger.error(f"Error calling {url}: {str(e)}")
        error_res = {"error": f"Failed to fetch from {endpoint}: {str(e)}"}
        results = raw_results_var.get()
        results.append(error_res)
        raw_results_var.set(results)
        return error_res

def clean_id(id_val: Any) -> str:
    return re.sub(r'[^0-9]', '', str(id_val))
