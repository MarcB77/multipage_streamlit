import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Home",
    page_icon="👋",
    layout='wide',
    initial_sidebar_state='expanded'
)

image = Image.open('image/southfields_logo.png')
st.image(image)

st.write("# Welcome to South-Fields Demo! 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    Author: Marc Blomvliet (Aurai) \n
    **👈 Select a demo from the sidebar** 
"""
)