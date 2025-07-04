# ⚡ EV Digital Twin – Real-Time Anomaly Detection Dashboard

A real-time EV (Electric Vehicle) health monitoring and anomaly detection system using:

🚗 Simulated sensor data → ☁️ streamed to Firebase → 📊 analyzed live in a Streamlit dashboard  
Built with zero-cost cloud tools and open-source libraries.

---

## 🔍 Project Overview

This project simulates a real-time EV environment by:
- Generating synthetic vehicle sensor data every second
- Streaming it to Firebase Realtime Database
- Predicting anomalies using a trained machine learning model
- Visualizing insights in a clean, cloud-hosted dashboard

Perfect for predictive maintenance, EV health monitoring, and digital twin use cases.

---

## ⚙️ Tech Stack

| Layer           | Tech                           |
|----------------|--------------------------------|
| Simulator       | Python + Firebase Admin SDK    |
| ML Model        | Scikit-Learn (Random Forest)   |
| Dashboard       | Streamlit                      |
| Backend (cloud) | Firebase Realtime Database     |
| Hosting         | Streamlit Cloud                |

---

## 🎯 Features

- 🔁 Real-time streaming of EV sensor data
- 🧠 ML-based anomaly detection (battery/motor faults)
- 📈 Live charts (temperature, RPM, SoC)
- 🚨 Anomaly alerts and metrics
- 🌐 Zero-cost cloud deployment (Firebase + Streamlit)


## 🚀 Run It Locally

### 1. Clone the repo

```bash
git clone https://github.com/your-username/ev-digital-twin.git
cd ev-digital-twin
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Add your Firebase credentials
Download your service account key from Firebase Console → Project Settings → Service Accounts → "Generate private key"

Save it as:

pgsql
Copy
Edit
firebase_config.json
✅ Do NOT push this file to GitHub.

4. Start the simulator
bash
Copy
Edit
python scripts/ev_data_simulator.py
5. Launch the dashboard
bash
Copy
Edit
streamlit run dashboard/dashboard.py
🌐 Streamlit Cloud Link
🟢 Live Dashboard Demo

🧠 Model Training (Optional)
To retrain your model on simulated data:

bash
Copy
Edit
python scripts/train_ev_model.py
🛡️ Firebase Database Rules (for public read access)
json
Copy
Edit
{
  "rules": {
    ".read": true,
    ".write": true
  }
}
👨‍💻 Authors
Shashwat Kashyap (@Shashwat-k-9114)


📜 License
MIT License — feel free to use, fork, and build on this!

🏁 Acknowledgments
Firebase for free cloud infra

Streamlit for easy deployment

scikit-learn for quick model prototyping

yaml
Copy
Edit

---