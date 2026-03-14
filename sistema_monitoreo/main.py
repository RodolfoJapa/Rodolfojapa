from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(title="Monitor Industria 4.0")
model = joblib.load("industry_model.pkl")
ideals = joblib.load("normal_op.pkl")

class MachineInput(BaseModel):
    air_temp: float
    process_temp: float
    rpm: int
    torque: float
    tool_wear: int

@app.post("/predict")
def predict_and_prescribe(data: MachineInput):
    X = np.array([[data.air_temp, data.process_temp, data.rpm, data.torque, data.tool_wear]])
    prob = model.predict_proba(X)[0][1]
    prediction = 1 if prob > 0.5 else 0

    # --- MOTOR DE PRESCRIPCIÓN ---
    action = "Mantener parámetros actuales."
    if prediction == 1:
        recs = []
        if data.torque > ideals['Torque [Nm]']: recs.append(f"REDUCIR TORQUE a {ideals['Torque [Nm]']} Nm")
        if data.tool_wear > 180: recs.append("CAMBIO DE HERRAMIENTA URGENTE")
        action = " | ".join(recs) if recs else "Revisión técnica necesaria."

    return {
        "probabilidad_falla": f"{round(prob*100, 1)}%",
        "estado": "CRÍTICO" if prediction == 1 else "OK",
        "accion_prescriptiva": action
    }
