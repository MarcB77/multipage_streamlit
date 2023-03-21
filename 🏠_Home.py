import streamlit as st
from PIL import Image


def streamlit_page_config():
    st.set_page_config(
        page_title="Home",
        page_icon="🏠",
        layout='wide',
        initial_sidebar_state='expanded'
    )

    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

@st.cache_data(show_spinner="Een momentje...")
def load_images():
    image = Image.open('image/southfields_logo.png')
    image_aurai = Image.open('image/aurai_logo.png')
    return image, image_aurai

streamlit_page_config()
image, image_aurai = load_images()
# col1, col2 = st.columns(2)
# with col1:
st.image(image)
# with col2:


st.write("# Welcome to South-Fields Demo!")

st.sidebar.success("Selecteer een demo hierboven.")
st.sidebar.image(image_aurai)

st.markdown(
    """
    Author: Marc Blomvliet (Aurai) \n
    **👈 Selecteer een demo uit de sidebar** 
"""
)