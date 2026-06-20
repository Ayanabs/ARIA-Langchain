import re
import contextvars
from typing import Any
import requests  # type: ignore
from requests.adapters import HTTPAdapter  # type: ignore
from urllib3.util.retry import Retry

from aria_agent.config import SPRING_BOOT_BASE_URL, logger

# Use None as the default value to avoid the mutable default ContextVar/argument anti-pattern
called_endpoints_var: contextvars.ContextVar[Any] = contextvars.ContextVar("called_endpoints", default=None)
raw_results_var: contextvars.ContextVar[Any] = contextvars.ContextVar("raw_results", default=None)

# Configure a session with connection pooling and transient error retries
def _init_session() -> requests.Session:
    session = requests.Session()
    # Configure retry strategy for resilient HTTP requests
    retries = Retry(
        total=3,
        backoff_factor=0.3,
        status_forcelist=[500, 502, 503, 504],
        raise_on_status=False
    )
    adapter = HTTPAdapter(
        pool_connections=10,
        pool_maxsize=25,
        max_retries=retries  # type: ignore
    )
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session

# Global thread-safe session instance to reuse TCP connections
_session = _init_session()

def make_request(endpoint: str) -> Any:
    """Makes a GET request to the target Spring Boot endpoint and logs the routing path."""
    url = f"{SPRING_BOOT_BASE_URL}{endpoint}"
    

    endpoints = called_endpoints_var.get()
    if isinstance(endpoints, list):
        endpoints.append(endpoint)
    
    try:
        logger.info(f"Tool calling API: {url}")
    
        response = _session.get(url, timeout=(3.05, 10.0))
        response.raise_for_status()
        data = response.json()
        
        results = raw_results_var.get()
        if isinstance(results, list):
            results.append(data)
        
        return data
    except requests.exceptions.Timeout as e:
        logger.error(f"Timeout occurred while calling {url}: {e}")
        error_res = {"error": f"Request to {endpoint} timed out."}
    except requests.exceptions.ConnectionError as e:
        logger.error(f"Connection error occurred while calling {url}: {e}")
        error_res = {"error": f"Failed to connect to service at {endpoint}."}
    except requests.exceptions.HTTPError as e:
        status_code = e.response.status_code if e.response is not None else "unknown"
        logger.error(f"HTTP error {status_code} occurred while calling {url}: {e}")
        error_res = {"error": f"HTTP error {status_code} from {endpoint}."}
    except requests.exceptions.RequestException as e:
        logger.error(f"Request exception occurred while calling {url}: {e}")
        error_res = {"error": f"Request error calling {endpoint}: {str(e)}"}
    except ValueError as e:
        # Catch JSON decoding failures
        logger.error(f"Failed to parse JSON response from {url}: {e}")
        error_res = {"error": f"Invalid response format from {endpoint}."}
    except Exception as e:
        logger.error(f"Unexpected error calling {url}: {e}")
        error_res = {"error": f"Unexpected error fetching from {endpoint}: {str(e)}"}

    # Update raw results if context var is populated
    results = raw_results_var.get()
    if isinstance(results, list):
        results.append(error_res)
    
    return error_res

def clean_id(id_val: Any) -> str:
    """Removes non-numeric characters from IDs for security and formatting.
    
    Returns an empty string if id_val is None.
    """
    if id_val is None:
        return ""
    return re.sub(r'[^0-9]', '', str(id_val))
