from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from prometheus_client import Counter, Histogram, generate_latest
from fastapi.responses import Response

app = FastAPI(
    title="AegisOps Backend API",
    description="DevOps-Driven IoT Monitoring Platform",
    version="1.0.0"
)

# Prometheus Metrics
REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint"]
)

REQUEST_LATENCY = Histogram(
    "http_request_latency_seconds",
    "Request latency"
)

class IoTData(BaseModel):
    device_id: str
    temperature: int
    cpu: int
    memory: int

@app.get("/")
def root():
    REQUEST_COUNT.labels(method="GET", endpoint="/").inc()
    return {
        "project": "AegisOps",
        "developer": "Simran Anand",
        "status": "Backend is running successfully"
    }

@app.post("/api/metrics")
def collect_metrics(data: IoTData):
    REQUEST_COUNT.labels(method="POST", endpoint="/api/metrics").inc()

    status = "NORMAL"
    if data.temperature > 80 or data.cpu > 85 or data.memory > 85:
        status = "ALERT"

    log = {
        "timestamp": datetime.utcnow().isoformat(),
        "device_id": data.device_id,
        "temperature": data.temperature,
        "cpu": data.cpu,
        "memory": data.memory,
        "status": status,
        "handled_by": "Simran Anand"
    }

    print("📡 AegisOps Log:", log)
    return log

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")
