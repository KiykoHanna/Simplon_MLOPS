import os

import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.title("Insert Page")

# Ввод данных пользователя
user_name = st.text_input("Enter user name")
model_name = st.text_input("Enter AI model name")
probability = st.number_input("Prediction probability", min_value=0.0, max_value=1.0, step=0.01, value=0.5)

# Кнопка для отправки на API
if st.button("Insert Prediction"):
    # Сначала создаём пользователя
    r_user = requests.post(f"http://localhost:{os.getenv('API_PORT', 8000)}/users/", params={"name": user_name})
    user_id = r_user.json().get("id")

    # Создаём модель
    r_model = requests.post(f"http://localhost:{os.getenv('API_PORT', 8000)}/models/", params={"name": model_name})
    model_id = r_model.json().get("id")

    # Создаём предсказание
    r_pred = requests.post(
        f"http://localhost:{os.getenv('API_PORT', 8000)}/predictions/",
        params={"user_id": user_id, "model_id": model_id, "probability": probability}
    )

    if r_pred.status_code == 200:
        st.success("Prediction inserted successfully!")
        st.json(r_pred.json())
    else:
        st.error("Failed to insert prediction")
