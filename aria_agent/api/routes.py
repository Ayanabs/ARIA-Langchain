from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

from aria_agent.services.agent_service import AgentService

# Initialize FastAPI application
app = FastAPI(title="ARIA Standalone LangChain Agent")

# Configure CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Agent Service
agent_service = AgentService()

class QueryRequest(BaseModel):
    prompt: str
    model: Optional[str] = None

@app.post("/api/query")
async def execute_query(request: QueryRequest):
    result = agent_service.execute_query(request.prompt)
    
    # Handle parsing or validation failure as an HTTP Exception
    if isinstance(result, dict) and result.get("error_type") == "parsing_error":
        raise HTTPException(
            status_code=500,
            detail=result.get("message", "The agent returned an invalid JSON response. Please refine your query.")
        )
        
    return result

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
