from fastapi import FastAPI
from app.services.ai_service import analyze_log

app = FastAPI(title="AI Pipeline Assistant")

@app.get("/")
def health():
    return {"status": "running"}

@app.post("/analyze")
def analyze(payload: dict):
    log = payload.get("log", "")
    result = analyze_log(log)
    return {"analysis": result}