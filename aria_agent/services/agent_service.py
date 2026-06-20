import re
import json
import time
from typing import List, Dict, Any, Optional

from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, ToolMessage, BaseMessage

from aria_agent.config import OLLAMA_BASE_URL, MODEL_NAME, SYSTEM_PROMPT, logger
from aria_agent.infrastructure.client import called_endpoints_var, raw_results_var
from tools import all_tools as tools

def normalize_word(w):
    w = w.lower()
    SPELLING_MAP = {
        # Typos & Singularization
        "emloyee": "employee",
        "employe": "employee",
        "emloyees": "employee",
        "employes": "employee",
        "employees": "employee",
        "elployee": "employee",
        "elployees": "employee",
        "divison": "division",
        "divisons": "division",
        "divisions": "division",
        "desig": "designation",
        "designations": "designation",
        "sal": "salary",
        "salaries": "salary",
        "proj": "project",
        "projects": "project",
        "dep": "department",
        "dept": "department",
        "depts": "department",
        "departments": "department",
        "div": "division",
        "bkp": "backup",
        "edu": "education",
        "hi": "higher",
        "att": "attendance",
        "dt": "date",
        "pr": "project",
        "grade": "grade",
        "grades": "grade",
        "leave": "leave",
        "leaves": "leave",
        "type": "type",
        "types": "type",
        "store": "store",
        "stores": "store",
        "issue": "issue",
        "issues": "issue",
        "class": "class",
        "classes": "class",
        "category": "category",
        "categories": "category",
    }
    if w in SPELLING_MAP:
        w = SPELLING_MAP[w]
    if w.endswith("ies"):
        return w[:-3] + "y"
    if w.endswith("sses") or w.endswith("ches") or w.endswith("shes") or w.endswith("xes"):
        return w[:-2]
    if w.endswith("s") and not (w.endswith("ss") or w.endswith("us") or w.endswith("is") or w.endswith("as")):
        return w[:-1]
    return w

def filter_tools(tools_list: list, prompt: str) -> list:
    STOP_WORDS = {
        "show", "me", "all", "list", "get", "fetch", "find", "the", "a", "an",
        "of", "by", "for", "with", "is", "it", "to", "from", "in", "on", "at", "and",
        "details", "detail", "record", "records", "info", "information", "data",
        "table", "database", "db", "number", "no", "id", "val", "value", "code",
        "query", "search", "matching", "filter"
    }
    CORE_MODULES = {
        "employee",
        "salary_scale",
        "pr_project"
    }
    prompt_words = [normalize_word(pw) for pw in re.findall(r'[a-z0-9]+', prompt.lower()) if pw not in STOP_WORDS]
    filtered = []
    for t in tools_list:
        # Split camel case function names into separate words
        func_name = t.name
        func_words = [normalize_word(fw) for fw in re.findall(r'[a-zA-Z0-9]+', re.sub(r'([A-Z])', r' \1', func_name).lower()) if fw not in STOP_WORDS]
        
        candidate_words = set(func_words)
        
        matched = False
        for kw in candidate_words:
            if len(kw) < 2:
                continue
            for pw in prompt_words:
                if kw == pw:
                    matched = True
                    break
            if matched:
                break
        if matched:
            filtered.append(t)
            
    if not filtered:
        filtered = [
            t for t in tools_list
            if (t.func.__module__ if hasattr(t, "func") else t.__module__).split('.')[-1].lower() in CORE_MODULES or
            any(normalize_word(w) in CORE_MODULES for w in re.findall(r'[a-zA-Z0-9]+', re.sub(r'([A-Z])', r' \1', t.name).lower()))
        ]
        
    return filtered

class AgentService:
    def __init__(self):
        self.llm = ChatOllama(
            model=MODEL_NAME, 
            base_url=OLLAMA_BASE_URL, 
            temperature=0.0, 
            timeout=180.0,
            streaming=True,
            think=False,
            num_ctx=2048,             
            keep_alive="24h",
            options={
                "top_k": 10,        
                "top_p": 0.3,        
                "num_predict": 512    
            }
        )
        
        self.tool_map = {t.name: t for t in tools}
        logger.info("LangChain Native Tool Calling configured successfully.")

    def _clean_json(self, json_str: str) -> str:
        """Cleans and formats JSON response from LLM output, extracting content between brackets."""
        if not json_str:
            return "[]"
        cleaned = json_str.strip()
        if cleaned.startswith("```"):
            cleaned = cleaned[3:].strip()
            if cleaned.lower().startswith("json"):
                cleaned = cleaned[4:].strip()
        if cleaned.endswith("```"):
            cleaned = cleaned[:-3].strip()
        cleaned = cleaned.strip()
        if not cleaned.startswith("["):
            start_idx = cleaned.find('[')
            end_idx = cleaned.rfind(']')
            if start_idx >= 0 and end_idx > start_idx:
                cleaned = cleaned[start_idx:end_idx + 1]
            else:
                cleaned = "[]"
        return cleaned

    def _format_endpoint_summary(self, endpoint_results: List[Dict[str, Any]]) -> str:
        """Formats the called API endpoints into a summary trace."""
        if not endpoint_results:
            return "None"

        lines = ["Agent routed request to API endpoints via Tool Calls:"]
        for index, entry in enumerate(endpoint_results, start=1):
            records = entry.get("records", [])
            lines.append(f"{index}. {entry.get('endpoint', 'Unknown endpoint')} ({len(records)} record(s))")
        return "\n".join(lines)

    def execute_query(self, prompt: str) -> dict:
        """Executes a database assistant prompt by invoking the LangChain Agent, capturing
        API client queries, and parsing results.
        """
        endpoints_token = None
        results_token = None
        start_time = time.time()
        
        try:
            logger.info(f"Running Native Tool Calling for prompt: '{prompt}'")
            
            # Instantiate contextvar default tracking lists for current thread context
            called_endpoints = []
            raw_results = []
            endpoints_token = called_endpoints_var.set(called_endpoints)
            results_token = raw_results_var.set(raw_results)
            
            filtered_tools = filter_tools(tools, prompt)
            logger.info(f"Filtered tools count: {len(filtered_tools)}")
            llm_with_tools = self.llm.bind_tools(filtered_tools)
            
            messages: List[BaseMessage] = [
                SystemMessage(content=SYSTEM_PROMPT),
                HumanMessage(content=prompt)
            ]
            
            max_iterations = 10
            iteration = 0
            output_text = ""
            while iteration < max_iterations:
                iteration += 1
                response = llm_with_tools.invoke(messages)
                messages.append(response)
                
                if not isinstance(response, AIMessage) or not response.tool_calls:
                    content = response.content
                    output_text = content if isinstance(content, str) else json.dumps(content)
                    break
                    
                for tool_call in response.tool_calls:
                    tool_name = tool_call["name"]
                    tool_args = tool_call["args"]
                    tool_id = tool_call["id"]
                    
                    tool_obj = self.tool_map.get(tool_name)
                    if tool_obj:
                        try:
                            tool_result = tool_obj.invoke(tool_args)
                        except Exception as tool_err:
                            tool_result = {"error": f"Error executing tool: {str(tool_err)}"}
                    else:
                        tool_result = {"error": f"Tool {tool_name} not found."}
                    
                    messages.append(ToolMessage(content=json.dumps(tool_result), name=tool_name, tool_call_id=tool_id))
            else:
                logger.warning(f"Agent exceeded max iterations ({max_iterations}) without producing a final answer.")
                output_text = "[]"
            
            execution_time_ms = int((time.time() - start_time) * 1000)
            
            # Retrieve routing lists from thread context
            endpoints = called_endpoints_var.get()
            results = raw_results_var.get()
            
            endpoint_results = []
            combined_results = []

            for index, endpoint in enumerate(endpoints):
                res = results[index] if index < len(results) else None
                records = []
                if isinstance(res, list):
                    records = res
                elif isinstance(res, dict):
                    records = [res]

                endpoint_results.append({
                    "endpoint": endpoint,
                    "records": records
                })
                combined_results.extend(records)

            endpoint_summary = self._format_endpoint_summary(endpoint_results)
            
            # If no client calls recorded or they were empty, parse the text output
            if not combined_results:
                cleaned = self._clean_json(output_text)
                try:
                    combined_results = json.loads(cleaned)
                except Exception as parse_err:
                    logger.warning(f"Failed to parse agent JSON output: '{cleaned}'. Error: {parse_err}")
                    if cleaned == "[]" or re.match(r"^\[\s*\.*\s*\]$", cleaned):
                        combined_results = []
                    else:
                        return {
                            "error_type": "parsing_error",
                            "message": f"The agent returned an invalid JSON response. Please refine your query."
                        }
                        
            return {
                "sql": endpoint_summary,
                "results": combined_results,
                "endpointResults": endpoint_results,
                "calledEndpoints": endpoints,
                "error": None,
                "executionTimeMs": execution_time_ms
            }
            
        except Exception as e:
            logger.error(f"Error running agent execution: {str(e)}")
            execution_time_ms = int((time.time() - start_time) * 1000)
            return {
                "sql": "Agent Execution Error",
                "results": [],
                "endpointResults": [],
                "error": f"Agent Execution Error: {str(e)}",
                "executionTimeMs": execution_time_ms
            }
        finally:
            # Clean up thread context variables if they were set
            if endpoints_token is not None:
                called_endpoints_var.reset(endpoints_token)
            if results_token is not None:
                raw_results_var.reset(results_token)
