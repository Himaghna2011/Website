
import requests
import streamlit as st 
from streamlit_lottie import st_lottie
from PIL import Image
import os

# Create the .streamlit directory if it doesn't exist
os.makedirs(".streamlit", exist_ok=True)

# Define the content of the config.toml file
config_content = """
[theme]
primaryColor="#e694ff"
backgroundColor="#00172b"
secondaryBackgroundColor="#041067"
"""

# Write the content to the config.toml file
with open(".streamlit/config.toml", "w") as config_file:
    config_file.write(config_content)

st.set_page_config(page_title="Homepage", page_icon=":tada:", layout = "wide")

# Create the .streamlit directory if it doesn't exist
os.makedirs(".streamlit", exist_ok=True)

# Define the content of the config.toml file
config_content = """
[theme]
primaryColor="#e694ff"
backgroundColor="#00172b"
secondaryBackgroundColor="#041067"
"""

# Write the content to the config.toml file
with open(".streamlit/config.toml", "w") as config_file:
    config_file.write(config_content)


def load_lottieurl(url):
    req = requests.get(url)
    if req.status_code != 200:
        return None
    return req.json()

lottie_files = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")

with st.container():
    st.subheader("Hi, :wave:")
    st.title("I am trying to learn how to code.")
    st.write("This is my first website that I made!")

with st.container():
    st.write("---")

    left_column, right_column = st.columns(2)
    
    with left_column:
        st.header("What I do:")
        st.write("##")
        st.write(
            """
            So, I am a 13 year old kid who basically just sits and codes on the computer trying to figure out how to build this website, and coming from me, this has taken a lot of hard work to build. So I encourage you to please take a look at it. If you have any questions, you can contact me at the contact page.
            """
        )

    with right_column:
        st_lottie(lottie_files, height = 300, key = "coding")
