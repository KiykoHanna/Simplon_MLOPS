import os

import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()  # загружает переменные из .env

API_URL = os.getenv("API_URL", "http://api:8000")

a = st.number_input("A", value=0)
b = st.number_input("B", value=0)

if st.button("Add"):
    r = requests.get(f"{API_URL}/add?a={a}&b={b}")
    st.write(r.json()["result"])

if st.button("Sub"):
    r = requests.get(f"{API_URL}/sub?a={a}&b={b}")
    st.write(r.json()["result"])
