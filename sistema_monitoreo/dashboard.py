import streamlit as st
import pandas as pd
import numpy as np
import random
import time

from sklearn.ensemble import RandomForestClassifier, IsolationForest
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

st.set_page_config(page_title="Industrial AI Monitoring", layout="wide")

st.title("🏭 Industrial AI Monitoring System")

# -----------------------------
# CARGAR DATASET
# -----------------------------

@st.cache_data
def load_data():

    df = pd.read_csv("ai4i2020.csv")

    le = LabelEncoder()
    df["Type"] = le.fit_transform(df["Type"])

    features = [
        "Air temperature [K]",
        "Process temperature [K]",
        "Rotational speed [rpm]",
        "Torque [Nm]",
        "Tool wear [min]"
    ]

    X = df[features]
    y = df["Machine failure"]

    return df, X, y

df, X, y = load_data()

# -----------------------------
# ENTRENAR MODELO ML
# -----------------------------

@st.cache_resource
def train_model(X,y):

    X_train,X_test,y_train,y_test = train_test_split(
        X,y,test_size=0.2,random_state=42
    )

    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=8,
        random_state=42
    )

    model.fit(X_train,y_train)

    return model

model = train_model(X,y)

# -----------------------------
# ANOMALY DETECTION
# -----------------------------

@st.cache_resource
def train_anomaly_model(X):

    iso = IsolationForest(
        contamination=0.03,
        random_state=42
    )

    iso.fit(X)

    return iso

anomaly_model = train_anomaly_model(X)

# -----------------------------
# CONFIG DASHBOARD
# -----------------------------

st.sidebar.header("Configuración")

auto_refresh = st.sidebar.checkbox("Streaming sensores",True)
interval = st.sidebar.slider("Intervalo (seg)",1,10,3)

machines = [f"Machine {i}" for i in range(1,6)]

if "history" not in st.session_state:
    st.session_state.history = {m:[] for m in machines}

alerts = []

# -----------------------------
# STREAMING DE SENSORES
# -----------------------------

sensor_data = []

for machine in machines:

    air_temp = random.uniform(296,304)
    process_temp = random.uniform(306,314)
    rpm = random.randint(1400,1600)
    torque = random.uniform(30,70)
    tool_wear = random.randint(0,250)

    row = [
        air_temp,
        process_temp,
        rpm,
        torque,
        tool_wear
    ]

    pred_prob = model.predict_proba([row])[0][1]
    pred_class = model.predict([row])[0]

    anomaly = anomaly_model.predict([row])[0]

    rul = 250 - tool_wear

    # causas de falla
    TWF = int(tool_wear > 200)
    HDF = int(process_temp > 312)
    PWF = int(torque > 55)
    OSF = int(rpm > 1580)

    sensor_data.append({
        "Machine":machine,
        "Failure Prob":pred_prob*100,
        "RUL":rul,
        "TWF":TWF,
        "HDF":HDF,
        "PWF":PWF,
        "OSF":OSF,
        "Anomaly":anomaly
    })

    st.session_state.history[machine].append(pred_prob*100)

    st.session_state.history[machine] = st.session_state.history[machine][-30:]

    if pred_prob > 0.8:
        alerts.append(machine)

# -----------------------------
# ALERTAS
# -----------------------------

st.subheader("🚨 Alertas")

if alerts:

    for a in alerts:
        st.error(f"{a} riesgo crítico de falla")

else:

    st.success("Sistema estable")

# -----------------------------
# MONITOREO MAQUINAS
# -----------------------------

st.subheader("🏭 Estado de máquinas")

cols = st.columns(5)

for i,machine in enumerate(machines):

    with cols[i]:

        st.markdown(f"### {machine}")

        prob = sensor_data[i]["Failure Prob"]
        rul = sensor_data[i]["RUL"]

        st.metric("Prob falla",f"{prob:.1f}%")
        st.metric("RUL",f"{rul} min")

        if prob > 80:
            st.error("CRÍTICO")

        elif prob > 60:
            st.warning("RIESGO")

        else:
            st.success("NORMAL")

        df_hist = pd.DataFrame(
            st.session_state.history[machine],
            columns=["Prob"]
        )

        st.line_chart(df_hist)

# -----------------------------
# PANEL DE CAUSAS DE FALLA
# -----------------------------

st.subheader("📊 Causas de falla")

df_panel = pd.DataFrame(sensor_data)

cause_counts = df_panel[["TWF","HDF","PWF","OSF"]].sum()

st.bar_chart(cause_counts)

st.write("""
TWF → Tool Wear Failure  
HDF → Heat Dissipation Failure  
PWF → Power Failure  
OSF → Overstrain Failure
""")

# -----------------------------
# ANOMALY DETECTION
# -----------------------------

st.subheader("📉 Detección de anomalías")

anomaly_df = df_panel[df_panel["Anomaly"]==-1]

if len(anomaly_df)>0:

    st.error("Anomalías detectadas")

    st.dataframe(anomaly_df)

else:

    st.success("No hay anomalías")

# -----------------------------
# STREAMING
# -----------------------------

if auto_refresh:

    time.sleep(interval)
    st.rerun()
