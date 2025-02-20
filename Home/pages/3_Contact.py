import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="Contact", page_icon=":tada:", layout = "wide")

def load_lottieurl(url):
    req = requests.get(url)
    if req.status_code != 200:
        return None
    return req.json()

lottie_files = load_lottieurl("https://lottie.host/9cd5a360-f5c4-4b61-85bd-e6dc0839ccbe/k79krqjg8g.json")

st.title("Contact me!")


css_code = """
/* CSS Snippet from W3schools: https://www.w3schools.com/howto/howto_css_contact_form.asp */
/* Style inputs with type="text", select elements and textareas */
input[type=message], input[type=email], input[type=text], textarea {
  width: 100%; /* Full width */
  padding: 12px; /* Some padding */ 
  border: 1px solid #ccc; /* Gray border */
  border-radius: 4px; /* Rounded borders */
  box-sizing: border-box; /* Make sure that padding and width stays in place */
  margin-top: 6px; /* Add a top margin */
  margin-bottom: 16px; /* Bottom margin */
  resize: vertical /* Allow the user to vertically resize the textarea (not horizontally) */
}

/* Style the submit button with a specific background color etc */
button[type=submit] {
  background-color: #0000FF;
  color: white;
  padding: 12px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

/* When moving the mouse over the submit button, add a darker green color */
button[type=submit]:hover {
  background-color: #45a049;
}

/* Hide Streamlit Branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
"""

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
contact_form = """
    <form action="https://formsubmit.co/himaghnasingh@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
        st.write("##")
    with right_column:
        st_lottie(lottie_files, height = 350, key = "coding")

st.markdown(f'<style>{css_code}</style>', unsafe_allow_html=True)
