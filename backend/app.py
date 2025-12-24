from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI(
    title="AegisOps Backend API",
    description="DevOps-Driven IoT Monitoring Platform | Developed by Simran Anand",
    version="1.0.0"
)

class IoTData(BaseModel):
    device_id: str
    temperature: int
    cpu: int
    memory: int

@app.get("/")
def root():
    return {
        "project": "AegisOps",
        "developer": "Simran Anand",
        "status": "Backend is running successfully"
    }

@app.post("/api/metrics")
def receive_metrics(data: IoTData):

    alert = "NORMAL"

    if data.temperature > 80 or data.cpu > 85 or data.memory > 85:
        alert = "ALERT"

    log = {
        "timestamp": datetime.now().isoformat(),
        "device_id": data.device_id,
        "temperature": data.temperature,
        "cpu": data.cpu,
        "memory": data.memory,
        "status": alert,
        "handled_by": "Simran Anand"
    }

    print("📡 AegisOps Log:", log)

    return {
        "message": "Data received successfully",
        "alert_status": alert,
        "developer": "Simran Anand"
    }
