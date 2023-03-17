import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout='wide',
    initial_sidebar_state='expanded'
)

image = Image.open('image/southfields_logo.png')
image_aurai = Image.open('image/aurai_logo.png')

st.image(image)
st.image(image_aurai)

st.write("# Welcome to South-Fields Demo!")

st.sidebar.success("Selecteer een demo hierboven.")

st.markdown(
    """
    Author: Marc Blomvliet (Aurai) \n
    **👈 Selecteer een demo uit de sidebar** 
"""
)