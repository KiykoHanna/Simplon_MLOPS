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

st.title("Insert Page")

# Enter user data -------------------------------------------
user_name = st.text_input("Enter user name")
model_name = st.text_input("Enter AI model name")
probability = st.number_input(
    "Prediction probability", min_value=0.0, max_value=1.0, step=0.01, value=0.5
    )

# Button for sending --------------------------------------
if st.button("Insert Prediction"):

    r_user = requests.post(f"{API_URL}/users/", params={"name": user_name})
    user_id = r_user.json().get("id")


    r_model = requests.post(f"{API_URL}/models/", params={"name": model_name})
    model_id = r_model.json().get("id")


    r_pred = requests.post(
        f"{API_URL}/predictions/",
        params={"user_id": user_id, "model_id": model_id, "probability": probability}
    )

    if r_pred.status_code == 200:
        st.success("Prediction inserted successfully!")
        st.json(r_pred.json())
    else:
        st.error("Failed to insert prediction")
