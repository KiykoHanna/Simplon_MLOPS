import os

import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.title("Read Page")

# Кнопка для загрузки данных
if st.button("Load Predictions"):
    try:
        # Получаем всех пользователей
        r_users = requests.get(f"http://localhost:{os.getenv('API_PORT', 8000)}/users/")
        users = {u["id"]: u["name"] for u in r_users.json()}

        # Получаем все модели
        r_models = requests.get(f"http://localhost:{os.getenv('API_PORT', 8000)}/models/")
        models = {m["id"]: m["name"] for m in r_models.json()}

        # Получаем все предсказания
        r_preds = requests.get(f"http://localhost:{os.getenv('API_PORT', 8000)}/predictions/")
        preds = r_preds.json()

        # Отображаем в таблице
        if preds:
            data = []
            for p in preds:
                data.append({
                    "User": users.get(p["user_id"], "Unknown"),
                    "AI Model": models.get(p["ai_model_id"], "Unknown"),
                    "Probability": p["probability"],
                    "Timestamp": p["timestamp"]
                })
            st.table(data)
        else:
            st.info("No predictions found.")

    except Exception as e:
        st.error(f"Error loading predictions: {e}")
