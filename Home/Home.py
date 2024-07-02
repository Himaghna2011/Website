
import requests
import streamlit as st 
import streamlit_lottie as st_lottie
from PIL import Image

st.set_page_config(page_title="Homepage", page_icon=":tada:", layout = "wide")

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
        st.empty()
