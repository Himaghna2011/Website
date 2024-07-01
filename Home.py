
import requests
import streamlit as st 
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="Homepage", page_icon=":tada:")

def load_lottieurl(url):
    req = requests.get(url)
    if req.status_code != 200:
        return None
    return req.json()

lottie_files = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact = Image.open("photo.jpg")

with st.container():
    st.subheader("Hi, :wave:")
    st.title("I am trying to learn how to code.")
    st.write("I am going to make a website")

with st.container():
    st.write("---")

    left_column, right_column = st.columns(2)
    
    with left_column:
        st.header("What I do:")
        st.write("##")
        st.write(
            """
            On my youtube channel I post gaming youtube videos. I am learning python to successfully launch a website one day.
            Since I am a content creator, I noticed that I can make website about content creators, where it will help them
            get new video ideas, clips, audio, effects and much more. Also, please subscribe to my youtube channel.
            """
        )
        st.write("[Youtube >](https://www.youtube.com/channel/UCOE97_MU5YQVOS4ruUyQtKA)")

    with right_column:
        st_lottie(lottie_files, height = 300, key = "coding")


with st.container():
    st.write("---")
    st.header("What videos I make")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_contact, use_column_width=True)
    with text_column:
        st.subheader("Fortnite Montage")
        st.write(
            """
            I grab some of the cool clips that I did in the game, and I add a song and sync it to the beat.
            I also add cool effects on top of that to make the gameplay look better synced and formatted.
            """
         )
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=XeRSEvH7-Io&t=4s)")