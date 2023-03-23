import spacy
import streamlit as st
from PIL import Image
from streamlit_chat import message as st_message
import uuid
import sqlalchemy.orm as _orm

from utils.api_gpt__3_5 import streamlit_prompt, streamlit_prompt_curie
from utils.entity_dataframe import create_df
import utils.database_utils.services as _services


def create_AWS_DB():
    _services.create_AWS_database()

def prompt_to_DB(PROMPT):
    UUID = str(uuid.uuid1())

    _services.insert_prompt(UUID=UUID, prompt=PROMPT)

@st.cache_data(show_spinner="Een momentje...")
def load_images():
    return Image.open('image/southfields_logo.png')

@st.cache_resource(show_spinner="Een momentje...")
def load_nl_core_news_lg():
    return spacy.load("nl_core_news_lg")
     

def streamlit_page_config():
    st.set_page_config(page_title="Genereer Samenvatting", page_icon="🤖", layout='wide', initial_sidebar_state='expanded')
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

streamlit_page_config()
st.sidebar.success("Genereer een samenvatting op deze demo pagina.")
create_AWS_DB()
NER = load_nl_core_news_lg()
image = load_images()
st.image(image)

st.write(""" # South-Fields Demo """)

temperature_GPT = st.sidebar.number_input(
    label="Model Temperature",
    min_value=0.0,
    max_value=1.0,
    value=0.5
    )


submit = st.button("Genereer")

if submit:
    input_data = st.text_area(
        label="Wedstrijd Data",
        value="..",
        height=200,
        max_chars=None
        )
    with st.spinner("Even een samenvatting aan het schrijven, momentje..."):
        if input_data != "..":
            
            generated_output = streamlit_prompt_curie(input_data, TEMP=temperature_GPT)

            st_message(generated_output,
                    avatar_style="bottts-neutral",
                    seed="Aneka",
                    is_user=False)
            
            
            #spacy_NER_output = spacy.displacy.render(NER(generated_output),style="ent",jupyter=False)
            # st.markdown("""# Named Entity Recognition """)
            # st.markdown(spacy_NER_output, unsafe_allow_html=True)
            with st.spinner("Wegschrijven naar database"):
                prompt_to_DB(generated_output)

st.info(
        """Model temperature:\n - Hogere waarden zoals 0.8 zal de output meer random 
        maken\n - Lagere waarden zoals 0.2 zal de output meer gericht en deterministisch maken""", 
        icon="ℹ️")
    # st.info(
    #         """Model temperature:\n - Hogere waarden zoals 0.8 zal de output meer random 
    #         maken\n - Lagere waarden zoals 0.2 zal de output meer gericht en deterministisch maken
    #         \n\n De NER-functie: \n\n Kan entiteiten in ongestructureerde tekst identificeren en categoriseren.
    #         \n Entiteiten lijst: \n""", 
    #         icon="ℹ️")
    #st.dataframe(data=create_df(), width=550)