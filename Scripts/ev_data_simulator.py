import pandas as pd
import random
import time
from datetime import datetime

# Define how many records you want
NUM_RECORDS = 200

# Create an empty list to store simulated data
data = []

for i in range(NUM_RECORDS):
    entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "battery_temp": round(random.uniform(20.0, 60.0), 2),  # Celsius
        "state_of_charge": round(random.uniform(20.0, 100.0), 2),  # %
        "motor_rpm": random.randint(1000, 9000),
        "vehicle_speed": random.randint(20, 120),  # km/h
        "ambient_temp": round(random.uniform(15.0, 45.0), 2),  # Celsius
        "anomaly": 1 if random.random() < 0.05 else 0  # 5% chance of anomaly
    }
    data.append(entry)
    time.sleep(0.05)  # Simulate data generation delay (optional)

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("ev_sensor_data.csv", index=False)
print("✅ Data simulation complete. File saved as 'ev_sensor_data.csv'.")
