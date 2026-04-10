import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open("medical_cost_model.pkl", "rb"))

# Title
st.title("💊 Medical Cost Prediction App")
st.image("image.jpg")   
st.write("Enter patient details to predict medical charges")

# Inputs
age = st.number_input("Age", min_value=1, max_value=100, value=25)

sex = st.selectbox("Sex", ["Female", "Male"])
sex = 0 if sex == "Female" else 1

bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)

children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)

smoker = st.selectbox("Smoker", ["No", "Yes"])
smoker = 1 if smoker == "Yes" else 0

region = st.selectbox("Region", ["southwest", "southeast", "northwest", "northeast"])

# Encode region (simple label encoding)
region_dict = {
    "southwest": 0,
    "southeast": 1,
    "northwest": 2,
    "northeast": 3
}

region = region_dict[region]

# Prediction
if st.button("Predict Medical Cost"):
    input_data = np.array([[age, sex, bmi, children, smoker, region]])
    
    prediction = model.predict(input_data)
    
    st.success(f"Estimated Medical Charges: ${prediction[0]:,.2f}")