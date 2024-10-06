import streamlit as st
import pickle
from catboost import CatBoostClassifier

st.title('Mental Health Prediction')

age = st.number_input('Enter Age:', min_value=10, max_value=100)
technology_usage = st.number_input('Technology Usage Hours:', min_value=0.0, max_value=24.0)
social_media_usage = st.number_input('Social Media Usage Hours:', min_value=0.0, max_value=24.0)
gaming_hours = st.number_input('Gaming Hours:', min_value=0.0, max_value=24.0)
screen_time_hours = st.number_input('Screen Time Hours:', min_value=0.0, max_value=24.0)
physical_activity = st.number_input('Physical Activity Hours:', min_value=0.0, max_value=24.0)

stress_level = st.selectbox('Stress Level:', ['Low', 'Medium', 'High'])

stress_mapping = {'Low': 0, 'Medium': 1, 'High': 2}
stress_level_encoded = stress_mapping[stress_level]

input_data = [[age, technology_usage, social_media_usage, gaming_hours, screen_time_hours, stress_level_encoded, physical_activity]]

model = CatBoostClassifier()
model.load_model('catboost_model.cbm')

if st.button('Predict'):
    prediction = model.predict(input_data)
    st.write(f'Mental Health Status Prediction: {prediction[0]}')
