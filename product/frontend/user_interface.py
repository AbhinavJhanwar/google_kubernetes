import streamlit as st
import requests

def get_fruits():
    url = "http://172.17.0.1:8000/fruits"
    # url = "http://0.0.0.0:8000/fruits"
    response = requests.get(url)
    return eval(response.text)

st.title("Sample Streamlit APP")
if st.button("Get Fruits"):
    st.write(", ".join(get_fruits()["fruits"]))
else:
    st.write("I want some fruits")
