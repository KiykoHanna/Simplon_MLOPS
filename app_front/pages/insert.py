import os

import requests
import streamlit as st
from dotenv import load_dotenv

# ENV ----------------
load_dotenv(".env.local")

DOCKER_MODE = os.getenv("DOCKER", "false").lower() == "true"

API_URL: str
if DOCKER_MODE:
    API_URL = os.getenv("API_URL") or ""
    if not API_URL:
        raise ValueError("API_URL must be set in Docker mode")
else:
    API_URL = "http://localhost:8000"

# function logique ------------------------------------------
def create_user(api_url: str, name: str) -> dict:
    """Create a user via API.

    Args:
        api_url (str): Base API URL.
        name (str): User name.

    Returns:
        int: Created user ID.

    """
    r = requests.post(f"{api_url}/users/", params={"name": name})
    r.raise_for_status()
    json_data = r.json()
    return {"id": json_data.get("id"), "name": json_data.get("name")}

def create_model(api_url: str, name: str) -> int:
    """Create an AI model via API.

    Args:
        api_url (str): Base API URL.
        name (str): Model name.

    Returns:
        int: Created model ID.

    """
    r = requests.post(f"{api_url}/models/", params={"name": name})
    r.raise_for_status()
    return r.json().get("id")

def create_prediction(
        api_url: str, user_id: int, model_id: int, probability: float) -> dict:
    """Create a prediction via API.

    Args:
        api_url (str): Base API URL.
        user_id (int): User ID.
        model_id (int): Model ID.
        probability (float): Prediction probability.

    Returns:
        dict: API response.

    """
    r = requests.post(
        f"{api_url}/predictions/",
        params={
            "user_id": user_id,
            "model_id": model_id,
            "probability": probability,
        },
    )
    r.raise_for_status()
    return r.json()

def insert_prediction_flow(
        api_url: str, user_name: str, model_name: str, probability: float) -> dict:
    """Full workflow: create user, model, and prediction.

    Args:
        api_url (str): Base API URL.
        user_name (str): User name.
        model_name (str): Model name.
        probability (float): Probability value.

    Returns:
        dict: Prediction response.

    """
    user_id = create_user(api_url, user_name)
    model_id = create_model(api_url, model_name)
    return create_prediction(api_url, user_id, model_id, probability)
# UI ----------------------------------------------------

st.title("Insert Page")

# Enter user data -------------------------------------------
user_name = st.text_input("Enter user name")
model_name = st.text_input("Enter AI model name")
probability = st.number_input(
    "Prediction probability",
    min_value=0.0,
    max_value=1.0,
    step=0.01,
    value=0.5,
)
# Button for sending --------------------------------------
if st.button("Insert Prediction"):
    try:
        result = insert_prediction_flow(API_URL, user_name, model_name, probability)

        st.success("Prediction inserted successfully!")
        st.json(result)

    except requests.exceptions.RequestException as e:
        st.error(f"API error: {e}")
    except Exception as e:
        st.error(f"Unexpected error: {e}")
