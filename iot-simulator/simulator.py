import time
import random
import requests

API_URL = "http://localhost:8000/api/metrics"

print("AegisOps IoT Simulator started...")

while True:
    payload = {
        "device_id": "iot-001",
        "temperature": random.randint(20, 100),
        "cpu": random.randint(10, 95),
        "memory": random.randint(20, 90)
    }

    try:
        response = requests.post(API_URL, json=payload)
        print("Sent:", payload, "Status:", response.status_code)
    except Exception as e:
        print("Error sending data:", e)

    time.sleep(5)
