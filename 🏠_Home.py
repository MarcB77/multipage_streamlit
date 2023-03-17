import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout='wide',
    initial_sidebar_state='expanded'
)

col1, col2 = st.columns(2)

image = Image.open('image/southfields_logo.png')
image_aurai = Image.open('image/aurai_logo.png')

with col1:
    st.image(image)
with col2:
    st.image(image_aurai)

st.write("# Welcome to South-Fields Demo!")

st.sidebar.success("Selecteer een demo hierboven.")

st.markdown(
    """
    Author: Marc Blomvliet (Aurai) \n
    **👈 Selecteer een demo uit de sidebar** 
"""
)