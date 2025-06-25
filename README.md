# AI API Starter (Replicate + FastAPI)

## Features:
- Protected with API keys
- Usage-limited per key
- Replicate backend (LLaMA-2 by Meta)
- SQLite for simple usage tracking

## Run Locally:
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## API Call Example:
```bash
curl -X POST http://localhost:8000/generate \
    -H "Content-Type: application/json" \
    -d '{"prompt": "Tell me a joke", "api_key": "testkey123"}'
```
