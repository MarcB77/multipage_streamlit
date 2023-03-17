import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="👋",
    layout='wide',
    initial_sidebar_state='expanded'
)

st.write("# Welcome to South-Fields Demo! 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    Author: Marc Blomvliet\n
    In collaboration with Aurai \n
    **👈 Select a demo from the sidebar** 
"""
)