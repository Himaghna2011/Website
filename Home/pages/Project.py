import streamlit as st
from PIL import Image
import requests


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
