import openai
import os

openai.api_key = os.environ['OPENAI_KEY']


def GPT_3(prompt, model_engine, TEMP):
    """
    max_tokens = Maximum of characters/tokens in the output (1000 tokens is about 750 words)
    n = amount of answers
    stop = Because we are define no stopping rules.
    temperature = internal parameter for the language model we use.

    Args:
        prompt (str): Your question to the language model

    Returns:
        str: The response of GPT 3
    """
    completion = openai.Completion.create(
        engine=model_engine,
        max_tokens=1200,
        prompt=prompt,
        temperature=TEMP
    )
    return completion

def GPT_3_5__chat_completion(prompt, model_engine, TEMP):
    """_summary_

    Args:
        prompt (_type_): _description_
        model_engine (_type_): _description_
    """
    completion = openai.ChatCompletion.create(
        model=model_engine,
        messages=[prompt],
        temperature=TEMP
    )
    return completion

def streamlit_prompt(user_prompt: str, TEMP: float):
    prompt = {
        "role": "user",
        "content": user_prompt
    }
    completion = GPT_3_5__chat_completion(
        prompt=prompt, 
        model_engine = "gpt-3.5-turbo-0301",
        TEMP=TEMP
        )
    return completion.choices[0].message.content

def streamlit_prompt_curie(user_prompt: str, TEMP: float):
    completion = GPT_3(
        prompt=user_prompt, 
        model_engine = "text-davinci-003",
        TEMP=TEMP
        )
    return completion.choices[0].text

#text-curie-001