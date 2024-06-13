import streamlit as st
import requests

def get_fruits():
    # if running separate docker containers for backend and frontend then 
    # get the ip address of backend docker container by using typing 
    # http://localhost:<port>/docs and use that below
    # url = "http://172.17.0.1:8000/fruits"

    # if runnig using yaml file then url will be as below. where fastapi is the name of backend docker container- 
    # http://<backend container name>:8000/fruits
    url = "http://fastapi:8000/fruits"

    response = requests.get(url)
    return eval(response.text)

st.title("Sample Streamlit APP")
if st.button("Get Fruits"):
    st.write(", ".join(get_fruits()["fruits"]))
else:
    st.write("I want some fruits")
