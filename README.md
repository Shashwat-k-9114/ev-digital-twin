# ⚡ EV Digital Twin – Real-time Anomaly Detection Dashboard

A real-time EV Digital Twin system that simulates sensor data, detects anomalies using machine learning, and visualizes live telemetry using Firebase + Streamlit — with full end-to-end cloud sync.

---

## 🚀 Project Overview

This project simulates and monitors electric vehicle (EV) telemetry data in real-time, detects anomalies via a trained ML model, and displays it all through a dynamic dashboard. It's designed to demonstrate how a digital twin can be used for predictive maintenance and performance monitoring in electric mobility systems.

---

## 🧠 Key Features

- 🔁 Real-time EV data simulator (Python)
- 🧪 Trained machine learning anomaly detector (RandomForest)
- ☁️ Firebase Realtime Database integration (push & pull)
- 📊 Interactive Streamlit dashboard with live charts
- 🔄 Updates every 2 seconds autonomously (no refresh needed)
- 🛠️ Production-ready and free to deploy

---

## 🛠 Tech Stack

| Layer        | Tools Used                                       |
|--------------|--------------------------------------------------|
| Simulator    | Python, Pandas, NumPy                            |
| ML Model     | scikit-learn, joblib                             |
| Backend      | Firebase Realtime Database                       |
| Dashboard    | Streamlit, Plotly                                |
| Infra        | Replit (data simulator), Local/Cloud Streamlit   |
| Deployment   | GitHub + Streamlit Cloud                         |

---

## 📁 Folder Structure



ev-digital-twin/
│
├── Dashboard/               # Streamlit dashboard
│   └── dashboard.py
│
├── Scripts/                 # Data generator (sensor simulator)
│   └── ev\_data\_simulator.py
│
├── MLModel/                 # Anomaly detection model
│   └── train\_ev\_model.py
│
├── firebase\_config.json     # (Private, add to .gitignore)
├── requirements.txt
├── README.md
└── .gitignore


---

## 📊 How It Works

1. `ev_data_simulator.py` generates fake EV telemetry (speed, temperature, battery voltage, etc.)
2. Every 2 seconds, it pushes data to Firebase Realtime Database.
3. The dashboard (`dashboard.py`) reads data live from Firebase.
4. It runs a trained RandomForest model on every entry to detect anomalies.
5. Detected anomalies are highlighted on the dashboard in real-time.

---

## 📦 Installation & Setup

1. Clone the repo:
   
   git clone https://github.com/yourusername/ev-digital-twin.git
   cd ev-digital-twin
`

2. Create virtual environment & install dependencies:

   
   pip install -r requirements.txt
   

3. Add your Firebase admin SDK JSON file:

   * Save it as `firebase_config.json`
   * Add this line to `.gitignore`:

     
     firebase_config.json
     

4. Run the model trainer (once):


   python MLModel/train_ev_model.py


5. Start simulator:


   python Scripts/ev_data_simulator.py


6. Run dashboard:


   streamlit run Dashboard/dashboard.py


---

## 🧪 Sample Live Data Format

json
{
  "timestamp": "2025-07-04 19:36:18",
  "speed": 82.5,
  "battery_temp": 45.0,
  "motor_temp": 67.2,
  "voltage": 403.5,
  "current": 130.2,
  "anomaly": 0
}


---

## 🛡 Security

* Your Firebase admin config is private.
* Do NOT commit `firebase_config.json` — it is ignored via `.gitignore`.

---

## 🧠 Future Improvements

* Integrate real IoT hardware (e.g., Raspberry Pi + CAN bus)
* Add dashboard analytics (e.g., anomaly history, maintenance alerts)
* Dockerize the project for containerized deployment
* Setup CI/CD pipeline for deployment to Streamlit Cloud or GCP

---

## 🤝 Credits

Built with ❤️ by \[Your Name]
GitHub: [github.com/yourusername](https://github.com/yourusername)

---

## 📄 License

MIT License



Let me know if you'd like this tailored with your GitHub username or project repo link inserted.

