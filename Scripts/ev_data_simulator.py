import firebase_admin
from firebase_admin import credentials, db
import random, time
from datetime import datetime

# Load your private key JSON
cred = credentials.Certificate("firebase_config.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://ev-digital-twin-default-rtdb.firebaseio.com/'
})

ref = db.reference("ev_data_stream")

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

print("🚀 Pushing EV sensor data to Firebase every second...")

while True:
    entry = generate_entry()
    ref.push(entry)
    print("✅ Pushed:", entry)
    time.sleep(1)
