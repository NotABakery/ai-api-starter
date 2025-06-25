from fastapi import FastAPI, Request, HTTPException
from utils import verify_api_key, check_usage_limit
from models.model_handler import run_model
from database.usage_tracker import log_usage

app = FastAPI()

@app.post("/generate")
async def generate(request: Request):
    data = await request.json()
    api_key = data.get("api_key")
    prompt = data.get("prompt")

    if not verify_api_key(api_key):
        raise HTTPException(status_code=403, detail="Invalid API Key")

    if not check_usage_limit(api_key):
        raise HTTPException(status_code=429, detail="Usage limit exceeded")

    result = run_model(prompt)
    log_usage(api_key)

    return {"result": result}
