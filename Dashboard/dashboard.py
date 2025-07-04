import streamlit as st
import pandas as pd
import joblib
import time
import os
import json
import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime

# ✅ Load Firebase credentials safely
if not firebase_admin._apps:
    if "FIREBASE_CONFIG_JSON" in os.environ:
        # Running on Streamlit Cloud
        firebase_json = json.loads(os.environ["FIREBASE_CONFIG_JSON"])
        cred = credentials.Certificate(firebase_json)
    else:
        # Running locally
        cred = credentials.Certificate("firebase_config.json")

    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://ev-digital-twin-default-rtdb.firebaseio.com/'
    })

# Load ML model
model = joblib.load("Models/ev_anomaly_model.pkl")

# Streamlit UI setup
st.set_page_config(page_title="EV Digital Twin", layout="wide")
st.title("🔋 EV Digital Twin – Live Health Monitor")

# Autorefresh every 10 seconds
st.markdown("<meta http-equiv='refresh' content='10'>", unsafe_allow_html=True)

# Fetch data from Firebase
@st.cache_data(ttl=5)
def get_live_data():
    ref = db.reference("ev_data_stream")
    data = ref.get()
    if not data:
        return pd.DataFrame()
    df = pd.DataFrame(list(data.values()))
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    df = df.dropna().sort_values("timestamp", ascending=False).reset_index(drop=True)
    return df

# Load live data
df = get_live_data()

if df.empty:
    st.warning("⚠️ No data received from Firebase.")
    st.stop()

# Predict anomalies
features = ["battery_temp", "state_of_charge", "motor_rpm", "vehicle_speed", "ambient_temp"]
df["anomaly"] = model.predict(df[features])

# Show recent data
st.subheader("📡 Latest Sensor Snapshot")
st.dataframe(df[["timestamp"] + features + ["anomaly"]].head(10), use_container_width=True)

# Metrics
col1, col2 = st.columns(2)
col1.metric("🛑 Anomalies (last 100)", int(df["anomaly"].head(100).sum()))
col2.metric("⚙️ Total Records", len(df))

# Charts
st.subheader("📈 Battery Temp & Motor RPM")
chart_df = df.sort_values("timestamp").set_index("timestamp")
st.line_chart(chart_df[["battery_temp", "motor_rpm"]])

st.subheader("🚀 Speed & State of Charge")
st.line_chart(chart_df[["vehicle_speed", "state_of_charge"]])
