import os

import dotenv
import requests
import streamlit as st

# Load environment
dotenv.load_dotenv(".env.local")
DOCKER_MODE = os.getenv("DOCKER", "false").strip().lower() == "true"
API_URL: str

if DOCKER_MODE:
    API_URL = os.getenv("API_URL") or ""
    if not API_URL:
        raise ValueError("API_URL is not set in Docker mode")
else:
    API_URL = "http://localhost:8000"

# FUNCTIONS ----------------------------------------------------

def delete_prediction(api_url: str, pred_id: int) -> dict:
    """Delete a prediction by ID.

    Args:
        api_url (str): Base API URL.
        pred_id (int): Prediction ID.

    Returns:
        dict: API response.

    Raises:
        requests.exceptions.RequestException: If request fails.

    """
    r = requests.delete(f"{api_url}/prediction/{pred_id}")
    r.raise_for_status()
    return r.json()


def update_user(api_url: str, user_id: int, new_name: str) -> dict:
    """Update a user name.

    Args:
        api_url (str): Base API URL.
        user_id (int): User ID.
        new_name (str): New user name.

    Returns:
        dict: API response.

    """
    r = requests.put(
        f"{api_url}/users/{user_id}",
        params={"new_name": new_name},
    )
    r.raise_for_status()
    return r.json()


def update_model(api_url: str, model_id: int, new_name: str) -> dict:
    """Update a model name.

    Args:
        api_url (str): Base API URL.
        model_id (int): Model ID.
        new_name (str): New model name.

    Returns:
        dict: API response.

    """
    r = requests.put(
        f"{api_url}/models/{model_id}",
        params={"new_name": new_name},
    )
    r.raise_for_status()
    return r.json()

st.title("DB Operations: Delete / Update")

col1, col2, col3 = st.columns(3)

# ---------------- DELETE ----------------
with col1:
    st.subheader("Delete Prediction")
    pred_id = st.number_input("Prediction ID", min_value=1, step=1)
    ...

    if st.button("Delete", key="delete"):
        try:
            result = delete_prediction(API_URL, int(pred_id))
            st.success(result.get("result", "Deleted"))
        except Exception as e:
            st.error(f"Error: {e}")

# ---------------- UPDATE USER ----------------
with col2:
    st.subheader("Update User")
    user_id = st.number_input("User ID", min_value=1, step=1, key="user_id")
    new_user_name = st.text_input("New Name", key="user_name")

    if st.button("Update User", key="update_user"):
        try:
            result = update_user(API_URL, int(user_id), new_user_name)
            st.success(result.get("result", "Updated"))
        except Exception as e:
            st.error(f"Error: {e}")

# ---------------- UPDATE MODEL ----------------
with col3:
    st.subheader("Update Model")
    model_id = st.number_input("Model ID", min_value=1, step=1, key="model_id")
    new_model_name = st.text_input("New Name", key="model_name")

    if st.button("Update Model", key="update_model"):
        try:
            result = update_model(API_URL, int(model_id), new_model_name)
            st.success(result.get("result", "Updated"))
        except Exception as e:
            st.error(f"Error: {e}")
