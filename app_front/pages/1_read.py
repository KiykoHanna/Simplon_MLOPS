import os

import requests
import streamlit as st
from dotenv import load_dotenv

# Загружаем локальный .env при запуске вне Docker
load_dotenv(".env.local")

DOCKER_MODE = os.getenv("DOCKER", "false").strip().lower() == "true"

if DOCKER_MODE:
    API_URL = os.getenv("API_URL")
    if not API_URL:
        raise ValueError("DOCKER mode is True but API_URL environment variable is not set")  # noqa: E501
else:
    API_URL = "http://localhost:8000"

# Title ---------------------------------------------------------
st.title("Read Data")

# Load data --------------------------------------------------
def fetch_database(api_url: str) -> list[dict]:
    """Fetch users, models, and predictions from the API and format them.

    Args:
        api_url (str): Base URL of the API.

    Returns:
        list[dict]: Formatted list of predictions
        with human-readable user and model names.

    """
    # Get users
    r_users = requests.get(f"{api_url}/users/")
    r_users.raise_for_status()
    users = {u["id"]: u["name"] for u in r_users.json()}

    # Get models
    r_models = requests.get(f"{api_url}/models/")
    r_models.raise_for_status()
    models = {m["id"]: m["name"] for m in r_models.json()}

    # Get predictions
    r_preds = requests.get(f"{api_url}/predictions/")
    r_preds.raise_for_status()
    preds = r_preds.json()

    # Format data
    data = [
        {
            "User": users.get(p["user_id"], "Unknown"),
            "AI Model": models.get(p["ai_model_id"], "Unknown"),
            "Probability": p["probability"],
            "Timestamp": p["timestamp"],
        }
        for p in preds
    ]
    return data


# Streamlit UI --------------------------------------------------
if st.button("Load All Database"):
    try:
        data = fetch_database(API_URL) # type: ignore
        if data:
            st.table(data)
        else:
            st.info("No predictions found.")
    except requests.exceptions.RequestException as e:
        st.error(f"Error loading predictions: {e}")
    except Exception as e:
        st.error(f"Unexpected error: {e}")
