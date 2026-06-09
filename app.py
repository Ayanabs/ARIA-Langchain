import os
import re
import time
import logging
import contextvars
import requests
import json
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Any, Dict

from langchain_ollama import ChatOllama
# pyrefly: ignore [missing-import]
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("langchain-agent")

from tools import all_tools as tools, called_endpoints_var, raw_results_var

SPRING_BOOT_BASE_URL = os.getenv("SPRING_BOOT_BASE_URL", "http://localhost:8080")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://192.168.84.205:11434")
MODEL_NAME = os.getenv("MODEL_NAME", "llama3.2:3b")

logger.info(f"SPRING_BOOT_BASE_URL set to: {SPRING_BOOT_BASE_URL}")
logger.info(f"OLLAMA_BASE_URL set to: {OLLAMA_BASE_URL}")
logger.info(f"MODEL_NAME set to: {MODEL_NAME}")

# Configure LangChain agent
system_prompt_text = (
    "You are an intelligent database assistant with tool-calling capabilities.\n"
    "Your task is to answer the user's prompt by fetching the appropriate data using the provided tools, and then processing/formatting the response.\n"
    "Rules:\n"
    "1. To satisfy the user's request, identify which specialized tool (e.g. `fetchAllEmployees`, `fetchEmployeeById`, `fetchAllDivisions`, `fetchDivisionById`, etc.) is needed to get the required data and call that tool with any necessary parameters.\n"
    "2. You only have read-only access to the database. You CANNOT perform any create, update, or delete operations.\n"
    "3. If you need data from multiple tools, you MUST call them sequentially (one after another), waiting for the result of the first tool before calling the next one. Do NOT request multiple tool calls in parallel.\n"
    "4. Once you receive the data from the tool, process it in-memory to satisfy the user's prompt. By default, unless the user prompt explicitly requests only specific fields, a count, or aggregates, you MUST preserve and output all fields from the retrieved database records.\n"
    "5. You MUST return the final processed data as a raw JSON array of objects (e.g., [{{\"field\": \"value\"}}]). Never abbreviate or truncate the data inside the JSON using '...' or placeholders.\n"
    "6. Output ONLY the raw JSON array. Do NOT wrap the JSON in markdown code blocks like ```json ... ```. Do NOT include any explanations or conversational text. Your response must start with '[' and end with ']'. Never output `[...]` as a placeholder.\n"
    "7. If no data is found, return an empty JSON array: []"
)

prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_prompt_text),
    ("placeholder", "{chat_history}"),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

llm = ChatOllama(
    model=MODEL_NAME, 
    base_url=OLLAMA_BASE_URL, 
    temperature=0.0, 
    timeout=180.0,
    streaming=False,
    
    think=False
)

# Bind tools and construct the agent executor
agent = create_tool_calling_agent(llm, tools, prompt_template)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# FastAPI application setup
app = FastAPI(title="ARIA Standalone LangChain Agent")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    prompt: str
    model: Optional[str] = None

def clean_json(json_str: str) -> str:
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


def format_endpoint_summary(endpoint_results: List[Dict[str, Any]]) -> str:
    if not endpoint_results:
        return "None"

    lines = ["Agent routed request to API endpoints via Tool Calls:"]
    for index, entry in enumerate(endpoint_results, start=1):
        records = entry.get("records", [])
        lines.append(f"{index}. {entry.get('endpoint', 'Unknown endpoint')} ({len(records)} record(s))")
    return "\n".join(lines)

@app.post("/api/query")
async def execute_query(request: QueryRequest):
    start_time = time.time()
    
    
    called_endpoints = []
    raw_results = []
    endpoints_token = called_endpoints_var.set(called_endpoints)
    results_token = raw_results_var.set(raw_results)
    
    try:
        logger.info(f"Running LangChain Agent for prompt: '{request.prompt}'")
        agent_response = agent_executor.invoke({"input": request.prompt})
        output_text = agent_response.get("output", "[]")
        
        execution_time_ms = int((time.time() - start_time) * 1000)
        
        # Retrieve final request context
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

        endpoint_summary = format_endpoint_summary(endpoint_results)
        
        
        if not combined_results:
            cleaned = clean_json(output_text)
            try:
                combined_results = json.loads(cleaned)
            except Exception as parse_err:
                logger.warning(f"Failed to parse agent JSON output: '{cleaned}'. Error: {parse_err}")
                if cleaned == "[]" or re.match(r"^\[\s*\.*\s*\]$", cleaned):
                    combined_results = []
                else:
                    raise HTTPException(
                        status_code=500, 
                        detail="The agent returned an invalid JSON response. Please refine your query."
                    )
                    
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
        called_endpoints_var.reset(endpoints_token)
        raw_results_var.reset(results_token)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}


if __name__ == "__main__":
    # Run with: python app.py
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
