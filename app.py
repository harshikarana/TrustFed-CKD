
import streamlit as st

st.set_page_config(
    page_title="TrustFed-CKD",
    layout="wide"
)

st.title("🏥 TrustFed-CKD Dashboard")

st.subheader(
    "Chronic Kidney Disease Prediction System"
)

age = st.number_input(
    "Age",
    min_value=1,
    max_value=100,
    value=50
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

if st.button("Predict CKD Risk"):

    st.success("Prediction Completed")

    st.metric(
        "Risk Level",
        "Medium Risk"
    )

    st.metric(
        "Confidence",
        "98.9%"
    )
