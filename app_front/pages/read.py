import os

import requests
import streamlit as st
from dotenv import load_dotenv

# env ----------------------
load_dotenv(".env.local")

DOCKER_MODE = os.getenv("DOCKER", "false").strip().lower() == "true"
if DOCKER_MODE:
    API_URL = os.getenv("API_URL")
    if not API_URL:
        raise ValueError(
            "DOCKER mode is True but API_URL environment variable is not set"
        )
else:
    API_URL = "http://localhost:8000"


# function API ----------------------
def get_users(api_url: str) -> list[dict]:
    """Fetches the list of users from the API.

    Args:
      api_url (str): Base URL of the API.

    Returns:
        list[dict]: List of user dictionaries, each containing at least 'id' and 'name'.

    Raises:
        requests.exceptions.RequestException: If the API request fails.

    """  # noqa: D401
    r = requests.get(f"{api_url}/users/")
    r.raise_for_status()
    return r.json()


def get_models(api_url: str) -> list[dict]:
    """Fetches the list of AI models from the API.

    Args:
        api_url (str): Base URL of the API.

    Returns:
        list[dict]: List of model dictionaries,each containing at least 'id' and 'name'.

    Raises:
        requests.exceptions.RequestException: If the API request fails.

    """  # noqa: D401
    r = requests.get(f"{api_url}/models/")
    r.raise_for_status()
    return r.json()


def get_predictions(api_url: str) -> list[dict]:
    """Fetches the list of predictions from the API.

    Args:
        api_url (str): Base URL of the API.

    Returns:
        list[dict]: List of prediction dictionaries, each containing at least
            'user_id', 'ai_model_id', 'probability', and 'timestamp'.

    Raises:
        requests.exceptions.RequestException: If the API request fails.

    """  # noqa: D401
    r = requests.get(f"{api_url}/predictions/")
    r.raise_for_status()
    return r.json()


def format_predictions(
    preds: list[dict], users: list[dict], models: list[dict]
) -> list[dict]:
    """Formats predictions for display by replacing user and model IDs with their names.

    Args:
        preds (list[dict]): List of predictions with fields 'user_id', 'ai_model_id',
            'probability', 'timestamp'.
        users (list[dict]): List of users with fields 'id' and 'name'.
        models (list[dict]): List of models with fields 'id' and 'name'.

    Returns:
        list[dict]: List of formatted predictions with fields:
            - 'User': user name,
            - 'AI Model': model name,
            - 'Probability': probability value,
             - 'Timestamp': timestamp.

    Notes:
        If a user ID or model ID is not found, the value "Unknown" is used.

    """  # noqa: D401
    users_dict = {u["id"]: u["name"] for u in users}
    models_dict = {m["id"]: m["name"] for m in models}
    return [
        {
            "User": users_dict.get(p["user_id"], "Unknown"),
            "AI Model": models_dict.get(p["ai_model_id"], "Unknown"),
            "Probability": p["probability"],
            "Timestamp": p["timestamp"],
        }
        for p in preds
    ]


# Streamlit UI ----------------------
st.title("Read Data")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Read Users"):
        try:
            users = get_users(API_URL)
            st.dataframe(users)
        except Exception as e:
            st.error(f"Error fetching users: {e}")

with col2:
    if st.button("Read Models"):
        try:
            models = get_models(API_URL)
            st.dataframe(models)
        except Exception as e:
            st.error(f"Error fetching models: {e}")

with col3:
    if st.button("Read Predictions"):
        try:
            users = get_users(API_URL)  # fetch from API
            models = get_models(API_URL)  # fetch from API
            preds = get_predictions(API_URL)  # fetch from API

            # format predictions with user/model names
            data = format_predictions(preds, users, models)

            if data:
                st.dataframe(data)
            else:
                st.info("No predictions found.")
        except Exception as e:
            st.error(f"Error fetching predictions: {e}")
