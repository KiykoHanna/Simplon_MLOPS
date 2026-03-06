import os

import requests
import streamlit as st
from dotenv import load_dotenv

# Загружаем локальный .env при запуске вне Docker
load_dotenv(".env.local")

# Определяем API URL
if os.getenv("DOCKER", "false").lower() == "true":
    API_URL = os.getenv("API_URL")  # внутри Docker
else:
    API_URL = "http://localhost:8000"  # локально

st.title("Read Page")


if st.button("Load Predictions"):
    try:
        # get users ---------------------------------------
        r_users = requests.get(f"{API_URL}/users/")
        users = {u["id"]: u["name"] for u in r_users.json()}

        # get models -------------------------------------------
        r_models = requests.get(f"{API_URL}/models/")
        models = {m["id"]: m["name"] for m in r_models.json()}

        # get prediction -------------------------------------------
        r_preds = requests.get(f"{API_URL}/predictions/")
        preds = r_preds.json()

        # Show table ----------------------------------------------
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
