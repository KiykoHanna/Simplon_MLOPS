import os

import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()  # загружает переменные из .env

API_URL = os.getenv("API_URL", "http://api:8000")


# Functions logique -----------------------------------------------

def add_numbers(a: int, b: int) -> int:
    """Send request for summ."""
    r = requests.get(f"{API_URL}/add?a={a}&b={b}")
    return r.json()["result"]


def sub_numbers(a: int, b: int) -> int:
    """Send request for sub."""
    r = requests.get(f"{API_URL}/sub?a={a}&b={b}")
    return r.json()["result"]

def square_numbers(a: int) -> float:
    """Send request for square."""
    r = requests.get(f"{API_URL}/square?a={a}")
    return r.json()["result"]

# UI Streamlit ----------------------------------------------------

def main_ui():
    """Execute main."""
    st.title("Math App")

    a = st.number_input("A", value=0)
    b = st.number_input("B", value=0)

    if st.button("Add"):
        result = add_numbers(a, b)
        st.write(result)

    if st.button("Sub"):
        result = sub_numbers(a, b)
        st.write(result)

    if st.button("Square"):
        result = square_numbers(a)
        st.write(result)


#  ------------------------------------------------------------

def get_ui_labels():
    """Return labels for test."""
    return ["A", "B", "Add", "Sub", "Math App"]


# Enter--------------------------------------------------------


if __name__ == "__main__":
    main_ui()
