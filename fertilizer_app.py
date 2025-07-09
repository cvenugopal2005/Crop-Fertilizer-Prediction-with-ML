import streamlit as st
import numpy as np
import pickle

# Load model and scaler
model = pickle.load(open("fertilizer_model.sav", "rb"))
scaler = pickle.load(open("fertilizer_scaler.sav", "rb"))

# Reverse mapping: label -> fertilizer name
FERTILIZER_LABELS = {
    1: 'Urea',
    2: 'DAP',
    3: '14-35-14',
    4: '28-28',
    5: '17-17-17',
    6: '20-20',
    7: '10-26-26'
}

# UI
st.set_page_config(page_title="Fertilizer Recommender", layout="centered")
st.title("🌱 Fertilizer Prediction")
st.write("Enter the details below to get a fertilizer recommendation:")

# Inputs
temperature = st.number_input("Temperature (°C)", 0.0, 60.0, 25.0)
humidity = st.number_input("Humidity (%)", 0.0, 100.0, 60.0)
moisture = st.number_input("Moisture (%)", 0.0, 100.0, 30.0)
soil_type = st.number_input("Soil Type (Encoded)", 0, 10, 2)
crop_type = st.number_input("Crop Type (Encoded)", 0, 22, 3)
nitrogen = st.number_input("Nitrogen", 0, 500, 10)
potassium = st.number_input("Potassium", 0, 500, 15)
phosphorus = st.number_input("Phosphorus", 0, 500, 6)

if st.button("Predict Fertilizer"):
    input_data = scaler.transform([[
        temperature,
        humidity,
        moisture,
        soil_type,
        crop_type,
        nitrogen,
        potassium,
        phosphorus
    ]])
    prediction = int(model.predict(input_data)[0])
    fert_name = FERTILIZER_LABELS.get(prediction, f"Unknown (label {prediction})")
    st.success(f"✅ Recommended Fertilizer: **{fert_name}**")
