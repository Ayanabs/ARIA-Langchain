# FastAPI application entry point.
# Delegates to the refactored routes in the aria_agent package.

from aria_agent.api.routes import app

if __name__ == "__main__":
    # Run with: python app.py
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
