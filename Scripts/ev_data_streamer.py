import pandas as pd
import random
import time
from datetime import datetime

def generate_entry():
    return {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "battery_temp": round(random.uniform(20.0, 60.0), 2),
        "state_of_charge": round(random.uniform(20.0, 100.0), 2),
        "motor_rpm": random.randint(1000, 9000),
        "vehicle_speed": random.randint(20, 120),
        "ambient_temp": round(random.uniform(15.0, 45.0), 2),
        "anomaly": 1 if random.random() < 0.05 else 0
    }

# Start stream
print("🚗 Starting live EV data stream...")
while True:
    entry = generate_entry()
    df = pd.DataFrame([entry])
    
    with open("live_ev_data.csv", "a") as f:
        df.to_csv(f, index=False, header=f.tell()==0)
    
    print(f"⏱️  Row added: {entry}")
    time.sleep(1)
