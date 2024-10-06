import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Загрузка модели и кодировщиков
model = joblib.load('random_forest_model.pkl')
label_encoders = joblib.load('label_encoders.pkl')

# Функция для кодирования категориальных данных
def encode_inputs(df, encoders):
    for col in ['Gender', 'Stress_Level', 'Support_Systems_Access', 'Work_Environment_Impact', 'Online_Support_Usage']:
        df[col] = encoders[col].transform(df[col])
    return df

# Заголовок приложения
st.title("Предсказание состояния психического здоровья")

# Ввод данных для предсказания
age = st.number_input("Возраст", min_value=18, max_value=100, value=25)
technology_usage = st.slider("Часы использования технологий", 0.0, 15.0, 6.0)
social_media_usage = st.slider("Часы использования социальных сетей", 0.0, 15.0, 3.0)
gaming_hours = st.slider("Часы на игры", 0.0, 10.0, 1.0)
screen_time = st.slider("Общее экранное время (часов)", 0.0, 20.0, 8.0)
sleep_hours = st.slider("Часы сна", 0.0, 12.0, 7.0)
physical_activity_hours = st.slider("Часы физической активности", 0.0, 10.0, 3.0)

# Категориальные данные
gender = st.selectbox("Пол", ["Male", "Female"])
stress_level = st.selectbox("Уровень стресса", ["Low", "Medium", "High"])
support_systems_access = st.selectbox("Доступ к системам поддержки", ["Yes", "No"])
work_environment_impact = st.selectbox("Влияние рабочей среды", ["Positive", "Negative"])
online_support_usage = st.selectbox("Использование онлайн-поддержки", ["Yes", "No"])

# Создаем DataFrame с введенными пользователем данными
input_data = pd.DataFrame({
    'Age': [age],
    'Technology_Usage_Hours': [technology_usage],
    'Social_Media_Usage_Hours': [social_media_usage],
    'Gaming_Hours': [gaming_hours],
    'Screen_Time_Hours': [screen_time],
    'Sleep_Hours': [sleep_hours],
    'Physical_Activity_Hours': [physical_activity_hours],
    'Gender': [gender],
    'Stress_Level': [stress_level],
    'Support_Systems_Access': [support_systems_access],
    'Work_Environment_Impact': [work_environment_impact],
    'Online_Support_Usage': [online_support_usage]
})

# Закодируем категориальные данные
input_data_encoded = encode_inputs(input_data, label_encoders)

# Предсказание состояния психического здоровья
if st.button("Предсказать"):
    prediction = model.predict(input_data_encoded)
    predicted_class = label_encoders['Mental_Health_Status'].inverse_transform(prediction)
    
    # Вывод предсказания
    st.subheader(f"Предсказанное состояние психического здоровья: {predicted_class[0]}")
