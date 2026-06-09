import re
import json
import time
from typing import List, Dict, Any, Optional

from langchain_ollama import ChatOllama
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate

from aria_agent.config import OLLAMA_BASE_URL, MODEL_NAME, SYSTEM_PROMPT, logger
from aria_agent.tools import all_tools as tools, called_endpoints_var, raw_results_var

class AgentService:
    def __init__(self):
        logger.info("Initializing LangChain ChatOllama configuration...")
        self.prompt_template = ChatPromptTemplate.from_messages([
            ("system", SYSTEM_PROMPT),
            ("placeholder", "{chat_history}"),
            ("human", "{input}"),
            ("placeholder", "{agent_scratchpad}"),
        ])
        
        self.llm = ChatOllama(
            model=MODEL_NAME, 
            base_url=OLLAMA_BASE_URL, 
            temperature=0.0, 
            timeout=180.0,
            streaming=False,
            think=False
        )
        
        # Configure tool calling agent executor
        self.agent = create_tool_calling_agent(self.llm, tools, self.prompt_template)
        self.agent_executor = AgentExecutor(agent=self.agent, tools=tools, verbose=True)
        logger.info("LangChain AgentExecutor loaded successfully.")

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
        start_time = time.time()
        
        # Instantiate contextvar default tracking lists for current thread context
        called_endpoints = []
        raw_results = []
        endpoints_token = called_endpoints_var.set(called_endpoints)
        results_token = raw_results_var.set(raw_results)
        
        try:
            logger.info(f"Running LangChain Agent for prompt: '{prompt}'")
            agent_response = self.agent_executor.invoke({"input": prompt})
            output_text = agent_response.get("output", "[]")
            
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
            # Clean up thread context variables
            called_endpoints_var.reset(endpoints_token)
            raw_results_var.reset(results_token)
