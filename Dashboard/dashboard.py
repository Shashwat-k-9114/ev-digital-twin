import streamlit as st
import pandas as pd
import joblib
import os
import time
from streamlit_autorefresh import st_autorefresh

# Load model
model = joblib.load("ev_anomaly_model.pkl")

# Auto-refresh every 2 seconds
st_autorefresh(interval=2000, key="refresh_counter")

st.set_page_config(page_title="⚙️ Real-Time EV Dashboard", layout="wide")
st.title("🔴 Live EV Health Monitoring Dashboard")

file_path = "live_ev_data.csv"

if not os.path.exists(file_path):
    st.warning("Waiting for live_ev_data.csv to be created...")
    st.stop()

# Read data
df = pd.read_csv(file_path)

if df.empty:
    st.info("Live data is streaming but no rows yet...")
    st.stop()

# Keep last 100 records
df = df.tail(100)

# Predict anomalies
features = df[["battery_temp", "state_of_charge", "motor_rpm", "vehicle_speed", "ambient_temp"]]
df["predicted_anomaly"] = model.predict(features)

# Dashboard display
col1, col2 = st.columns(2)

with col1:
    st.metric("📊 Total Records", len(df))
    st.metric("⚠️ Anomalies Detected", df["predicted_anomaly"].sum())

with col2:
    st.line_chart(df[["battery_temp", "state_of_charge", "motor_rpm", "vehicle_speed"]])

st.subheader("🔍 Recent EV Data with Predictions")
st.dataframe(df[::-1], use_container_width=True)
