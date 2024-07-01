import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon=":tada:")

st.title("Projects")

if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

my_input = st.text_input("Input a text here", st.session_state["my_input"])
submit = st.button

if submit:
    st.session_state["my_input"] = my_input
    st.write("You have entered: ", my_input)

st.write("---")

def load_lottiesurl(url):
    requ = requests.get(url)
    if requ.status_code != 200:
        return None
    return requ.json()

lotties_files = load_lottiesurl("https://lottie.host/82be80b1-8f25-414e-8e8b-ec8639917416/H4sRDOIEgR.json")

st_lottie(lotties_files, height = 300, key = "coding")