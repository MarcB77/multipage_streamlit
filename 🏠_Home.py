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

def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        # Password correct.
        return True

if check_password():
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