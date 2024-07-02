
import requests
import streamlit as st 
from streamlit_lottie import st_lottie
from PIL import Image
import os

# Step 1: Ensure the .streamlit/config.toml file is in place
# This part is not needed if you have already created the config.toml manually

# Step 2: Use custom CSS to further style your app
css_content = """
<style>
    .css-18e3th9 {
        background-color: #00172b !important;
    }
    .css-1cpxqw2 {
        background-color: #041067 !important;
    }
    .stButton>button {
        background-color: #e694ff !important;
        color: #00172b !important;
    }
</style>
"""

# Embed the CSS style into the Streamlit app
st.markdown(css_content, unsafe_allow_html=True)

# Your Streamlit app code here
st.title("Welcome to My Streamlit App")
st.write("This app uses a custom theme with the specified colors and additional CSS styling!")

# Example widgets
st.button("Click me!")
st.text_input("Enter some text:")

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
