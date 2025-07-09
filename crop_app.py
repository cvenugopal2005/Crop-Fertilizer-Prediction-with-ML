import streamlit as st
import numpy as np
import pickle

# Load model and scaler
model = pickle.load(open("crop_model.sav", "rb"))
scaler = pickle.load(open("crop_scaler.sav", "rb"))

# Map encoded crop labels to names
CROP_LABELS = {
    1: 'rice',
    2: 'maize',
    3: 'jute',
    4: 'cotton',
    5: 'coconut',
    6: 'papaya',
    7: 'orange',
    8: 'apple',
    9: 'muskmelon',
    10: 'watermelon',
    11: 'grapes',
    12: 'mango',
    13: 'banana',
    14: 'pomegranate',
    15: 'lentil',
    16: 'blackgram',
    17: 'mungbean',
    18: 'mothbeans',
    19: 'pigeonpeas',
    20: 'kidneybeans',
    21: 'chickpea',
    22: 'coffee'
}


# UI
st.set_page_config(page_title="Crop Predictor", layout="centered")
st.title("🌾 Crop Prediction")
st.write("Enter the details below to get a crop recommendation:")

# Inputs
N = st.number_input("Nitrogen", 0, 500, 90)
P = st.number_input("Phosphorus", 0, 500, 40)
K = st.number_input("Potassium", 0, 500, 40)
temperature = st.number_input("Temperature (°C)", 0.0, 60.0, 25.0)
humidity = st.number_input("Humidity (%)", 0.0, 100.0, 60.0)
ph = st.number_input("pH Level", 0.0, 14.0, 6.5)
rainfall = st.number_input("Rainfall (mm)", 0.0, 500.0, 100.0)

if st.button("Predict Crop"):
    input_data = scaler.transform([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(input_data)[0]
    crop_name = CROP_LABELS.get(prediction, f"Unknown (label {prediction})")
    st.success(f"✅ Recommended Crop: **{crop_name}**")
