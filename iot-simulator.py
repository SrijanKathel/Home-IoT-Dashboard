import requests
import random
import time

def generate_data():
    return {
        "temperature": round(random.uniform(18, 30), 1),
        "humidity": round(random.uniform(30, 60), 1),
        "light": round(random.uniform(100, 800), 0),
        "door": random.choice(["Open", "Closed"]),
        "smoke": random.choice(["Yes", "No"]),
        "motion": random.choice(["Detected", "Not Detected"]),
        "ac": random.choice(["On (24°C)", "Off"]),
        "light_status": random.choice(["On", "Off"])
    }

while True:
    data = generate_data()
    try:
        requests.post("http://localhost:5000/api/update", json=data)
        print("Sent →", data)
    except:
        print("❌ Couldn't connect to server.")
    time.sleep(2)
