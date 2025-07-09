# 🌾 Crop-Fertilizer-Prediction-with-ML

This project uses **Machine Learning** to recommend the most suitable crops and fertilizers based on soil nutrients and environmental conditions. It includes trained models and Jupyter notebooks for both crop and fertilizer prediction, helping to improve agricultural decisions through data-driven insights.

---

## 📌 Objectives

- To assist farmers in selecting optimal crops based on soil and weather conditions.
- To suggest the best fertilizer based on crop type and nutrient availability.
- To promote precision agriculture through intelligent, automated recommendations.

---

## 🔍 Project Modules

### 1. 🌿 Crop Recommendation
- **Function**: Predicts the most suitable crop.
- **Features Used**:
  - Nitrogen (N)
  - Phosphorus (P)
  - Potassium (K)
  - Temperature
  - Humidity
  - pH
  - Rainfall
- **Files**:
  - `Crop_Predictions.ipynb`
  - `crop_model.sav`
  - `crop_scaler.sav`

---

### 2. 💧 Fertilizer Recommendation
- **Function**: Recommends fertilizers based on soil and crop characteristics.
- **Features Used**:
  - Temperature
  - Humidity
  - Moisture
  - Soil Type (encoded)
  - Crop Type (encoded)
  - Nitrogen
  - Potassium
  - Phosphorus
- **Files**:
  - `Fertilizer_Recommendation.ipynb`
  - `fertilizer_model.sav`
  - `fertilizer_scaler.sav`

---

## 📂 Dataset Description

### `Crop_recommendation.csv`
- Soil nutrient and climate conditions with corresponding ideal crops.

### `Fertilizer_Prediction.csv`
- Crop type, soil data, and nutrient levels with recommended fertilizer types.

---

## 🛠️ Technologies Used

- **Programming Language**: Python
- **Libraries**:
  - `pandas`, `numpy`
  - `scikit-learn`
  - `matplotlib`, `seaborn`
- **Tools**:
  - Jupyter Notebook
  - Streamlit (for deployment)

---

## 📈 Output

- Trained `.sav` files for both crop and fertilizer models.
- Scalers (`crop_scaler.sav`, `fertilizer_scaler.sav`) for consistent preprocessing.
- Streamlit apps ready for local or cloud deployment:
  - `crop_app.py`
  - `fertilizer_app.py`
