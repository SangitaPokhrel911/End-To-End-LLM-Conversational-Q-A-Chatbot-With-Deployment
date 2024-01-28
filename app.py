## Conversational Q&A Chatbot

import streamlit as st 

from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain.chat_models import ChatOpenAI


##Streamlit UI
st.set_page_config(page_title = 'Conversational Q&A Chatbot')
st.header("Hey, Let's chat")

import os
from dotenv import load_dotenv
load_dotenv() #load environment variables from .env file



chat = ChatOpenAI( openai_api_key = 'OPENAI_API_KEY', temperature = 0.5) #fill the open ai api key here or you can connect from the environment

if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages'] = [
        SystemMessage(content = 'Ypu are a modeian AI assistant')
    ]

##Function to laod OpenAI model and get responses

def get_chatmodel_response(question):

#session state from streamlit
    st.session_state['flowmessages'].append(HumanMessage(content=question))
    answer = chat(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    return answer.content


input = st.text_input('Input:  ', key = 'input')
response = get_chatmodel_response(input)

submit = st.button('Ask the question')

##If ask button is clicked

if submit:
    st.subheader('The response is ')
    st.write(response)