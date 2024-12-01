# AI Workflow Backend

This is the backend service for the AI Workflow system, built with FastAPI, CrewAI, and LlamaIndex.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Start the server:
```bash
python main.py
```

The server will start on http://localhost:8000

## API Endpoints

- GET `/api/bitcoin`: Fetches current Bitcoin price
- POST `/api/query`: Processes multilingual queries
  - Parameters:
    - query: string
    - language: string (default: "en")