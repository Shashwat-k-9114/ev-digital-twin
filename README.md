# EV Digital Twin – Real-Time Anomaly Detection Dashboard

🚗 A real-time dashboard for monitoring electric vehicle sensor data and detecting system anomalies using machine learning.

## 📦 Folder Structure

- /data: Sensor datasets (simulated + live)
- /models: Trained ML model (Random Forest)
- /scripts: Data simulation and model training scripts
- /dashboard: Live Streamlit dashboard UI

## 🛠️ How to Run

1. Simulate data:
   python scripts/ev_data_simulator.py

2. Train model:
   python scripts/train_ev_model.py

3. Run dashboard:
   streamlit run dashboard/dashboard.py

✅ Built using Python, Streamlit, scikit-learn

📡 Auto-refreshes every 2 sec to show real-time predictions
