
import streamlit as st
import numpy as np
import pandas as pd
import joblib
from tensorflow.keras.models import load_model

# -------------------------
# Load Model
# -------------------------

model = load_model("trustfed_ckd_model.h5")
scaler = joblib.load("scaler.pkl")

# -------------------------
# Page Config
# -------------------------

st.set_page_config(
    page_title="TrustFed-CKD",
    layout="wide"
)

st.title("🏥 TrustFed-CKD Dashboard")

st.subheader(
    "AI-Powered Chronic Kidney Disease Prediction"
)

# -------------------------
# Inputs
# -------------------------

col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        "Age",
        18,
        100,
        50
    )

    gender = st.selectbox(
        "Gender",
        [1, 2]
    )

    race = st.selectbox(
        "Race",
        [1, 2, 3, 4, 6, 7]
    )

    bmi = st.number_input(
        "BMI",
        10.0,
        60.0,
        25.0
    )

    sys_bp = st.number_input(
        "Systolic BP",
        80,
        250,
        120
    )

    dia_bp = st.number_input(
        "Diastolic BP",
        40,
        150,
        80
    )

with col2:

    creatinine = st.number_input(
        "Creatinine",
        0.1,
        20.0,
        1.0
    )

    bun = st.number_input(
        "BUN",
        1.0,
        100.0,
        15.0
    )

    albumin = st.number_input(
        "Albumin",
        1.0,
        6.0,
        4.0
    )

    glucose = st.number_input(
        "Glucose",
        40.0,
        500.0,
        100.0
    )

    hemoglobin = st.number_input(
        "Hemoglobin",
        5.0,
        20.0,
        13.0
    )

    urine_albumin = st.number_input(
        "Urine Albumin",
        0.0,
        5000.0,
        10.0
    )

    urine_creatinine = st.number_input(
        "Urine Creatinine",
        1.0,
        500.0,
        100.0
    )
   
    urdact = st.number_input(
    "URDACT",
    0.0,
    15000.0,
    8.0
)

    acr = st.number_input(
        "Albumin-Creatinine Ratio",
        0.0,
        5000.0,
        30.0
    )

    hypertension = st.selectbox(
        "Hypertension",
        [0,1]
    )

    diabetes = st.selectbox(
        "Diabetes",
        [0,1]
    )

# -------------------------
# Prediction
# -------------------------

if st.button("Predict CKD Risk"):

  patient = np.array([[
    age,
    gender,
    race,
    bmi,
    sys_bp,
    dia_bp,
    creatinine,
    bun,
    albumin,
    glucose,
    hemoglobin,
    urine_albumin,
    urine_creatinine,
    urdact,
    acr,
    hypertension,
    diabetes
]])

    patient_scaled = scaler.transform(patient)

    pred = model.predict(patient_scaled)

    risk_class = np.argmax(pred)

    confidence = np.max(pred)

    labels = {
        0:"Low Risk",
        1:"Medium Risk",
        2:"High Risk"
    }

    st.success("Prediction Completed")

    st.metric(
        "Risk Level",
        labels[risk_class]
    )

    st.metric(
        "Confidence",
        f"{confidence*100:.2f}%"
    )

    if risk_class == 0:

        st.info(
            "Maintain healthy lifestyle and annual screening."
        )

    elif risk_class == 1:

        st.warning(
            "Kidney screening every 6 months."
        )

    else:

        st.error(
            "Immediate nephrologist consultation recommended."
        )
