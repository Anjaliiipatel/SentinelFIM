from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# In-memory storage for demonstration (Use database.py for real SQL storage)
baselines = {} 
alerts = []

class FileReport(BaseModel):
    agent_id: str
    file_path: str
    current_hash: str

@app.post("/verify")
async def verify_file(report: FileReport):
    # If we don't have a baseline, the first report becomes the baseline
    key = f"{report.agent_id}:{report.file_path}"
    
    if key not in baselines:
        baselines[key] = report.current_hash
        return {"status": "Baseline Created"}
    
    if baselines[key] != report.current_hash:
        alert = {"agent": report.agent_id, "file": report.file_path, "status": "TAMPERED"}
        alerts.append(alert)
        return alert
    
    return {"status": "Secure"}

@app.get("/alerts")
async def get_alerts():
    return alerts