from fastapi import FastAPI
from pydantic import BaseModel
from app.services.ai_service import analyze_log
from app.ml.anomaly_detector import predict_anomaly

app=FastAPI()
class LogRequest(BaseModel):
    log:str

@app.get('/')
def health():
    return {'status':'running'}

@app.post('/analyze')
def analyze(payload:LogRequest):
    return {'anomaly':predict_anomaly(payload.log),'analysis':analyze_log(payload.log)}
