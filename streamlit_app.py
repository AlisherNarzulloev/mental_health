import streamlit as st
import pickle
import pandas as pd

# @st.cache_resource
# def load_model():
#     with open('random_forest_model.pkl', 'rb') as file:
#         loaded_model = pickle.load(file)
#     return loaded_model

model = pickle.load(open('random_forest_model.pkl', 'rb'))

st.title("Предсказание состояния психического здоровья")

age = st.number_input("Возраст", min_value=18, max_value=100, value=25)
technology_usage = st.slider("Часы использования технологий", 0.0, 15.0, 6.0)
social_media_usage = st.slider("Часы использования социальных сетей", 0.0, 15.0, 3.0)
gaming_hours = st.slider("Часы на игры", 0.0, 10.0, 1.0)
screen_time = st.slider("Общее экранное время (часов)", 0.0, 20.0, 8.0)
sleep_hours = st.slider("Часы сна", 0.0, 12.0, 7.0)
physical_activity_hours = st.slider("Часы физической активности", 0.0, 10.0, 3.0)

gender = st.selectbox("Пол", ["Male", "Female"])
stress_level = st.selectbox("Уровень стресса", ["Low", "Medium", "High"])
support_systems_access = st.selectbox("Доступ к системам поддержки", ["Yes", "No"])
work_environment_impact = st.selectbox("Влияние рабочей среды", ["Positive", "Negative"])
online_support_usage = st.selectbox("Использование онлайн-поддержки", ["Yes", "No"])

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

def preprocess_input(df):
    df['Gender'] = 1 if gender == "Male" else 0
    df['Stress_Level'] = 0 if stress_level == "Low" else 1 if stress_level == "Medium" else 2
    df['Support_Systems_Access'] = 1 if support_systems_access == "Yes" else 0
    df['Work_Environment_Impact'] = 1 if work_environment_impact == "Positive" else 0
    df['Online_Support_Usage'] = 1 if online_support_usage == "Yes" else 0
    return df

input_data = preprocess_input(input_data)

if st.button("Предсказать"):
    # prediction = model.predict(input_data)
    # st.subheader(f"Предсказанное состояние психического здоровья: {prediction[0]}")
    print('hi')
