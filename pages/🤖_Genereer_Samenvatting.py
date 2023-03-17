import spacy
import streamlit as st
from PIL import Image
from streamlit_chat import message as st_message

from utils.api_gpt__3_5 import streamlit_prompt, streamlit_prompt_curie

st.set_page_config(page_title="Genereer Samenvatting", page_icon="🤖", layout='wide', initial_sidebar_state='expanded')
st.sidebar.success("Genereer een samenvatting op deze demo pagina.")

NER = spacy.load("nl_core_news_lg")
temperature_history = 0.50

image = Image.open('image/southfields_logo.png')
st.image(image)

st.write(""" # South-Fields Demo """)

temperature_GPT = st.number_input(
    label="Model Temperature",
    min_value=0.0,
    max_value=1.0,
    value=0.5
    )

input_data = st.text_area(
    label="Wedstrijd Data",
    value="..",
    height=200,
    max_chars=None
    )

with st.spinner("Even een samenvatting aan het schrijven, momentje..."):
    if input_data != "..":
        # st_message(input_data,
        #             avatar_style="thumbs",
        #             is_user=True)
        
        generated_output = streamlit_prompt_curie(input_data, TEMP=temperature_GPT)

        st_message(generated_output,
                avatar_style="bottts-neutral",
                seed="Aneka",
                is_user=False)
        
        spacy_NER_output = spacy.displacy.render(NER(generated_output),style="ent",jupyter=False)
        st.markdown("""# Named Entity Recognition """)
        st.markdown(spacy_NER_output, unsafe_allow_html=True)

st.info(
    """Model temperature:\n - Higher values like 0.8 will make the output more 
    random\n - Lower values like 0.2 will make it more focused and deterministic\n\n 
    De NER-functie: \n\n Kan entiteiten in ongestructureerde tekst identificeren en categoriseren. 
    Bijvoorbeeld: \n- Personen\n - Plaatsen\n - Organisaties\n - Hoeveelheden.""", 
    icon="ℹ️")

    # st.text_area(
    #     label="Your input:  \n", 
    #     value=input_data,
    #     height=200
    #     ) # Double whitesace before \n to get a newline.