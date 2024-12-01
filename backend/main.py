from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from pydantic import BaseModel
import os

# Load environment variables
load_dotenv()

from agents.bitcoin_agent import BitcoinAgent
from agents.language_agent import LanguageAgent

class QueryRequest(BaseModel):
    query: str
    language: str = "en"

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

bitcoin_agent = BitcoinAgent()
language_agent = LanguageAgent()

@app.post("/api/query")
async def process_query(request: QueryRequest):
    try:
        if not request.query.strip():
            raise HTTPException(status_code=400, detail="Query cannot be empty")

        if "bitcoin" in request.query.lower() or "price" in request.query.lower():
            result = bitcoin_agent.process_query(request.query)
        else:
            result = language_agent.process_query(request.query, request.language)

        if "error" in result:
            raise HTTPException(status_code=500, detail=result["error"])
            
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)