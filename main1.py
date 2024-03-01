
import streamlit as st

from langchain.schema import HumanMessage,SystemMessage,AIMessage
from langchain_community.llms import Ollama

llm = Ollama(base_url="http://172.31.212.37:11434" , model="zephyr", temperature=0.8)


st.set_page_config(page_title="Conversational Q&A Chatbot")
st.header("Hey, Let's Chat")


import os


if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages']=[
        SystemMessage(content="Yor are a comedian AI assitant")
    ]


def get_chatmodel_response(question):
    st.session_state['flowmessages'].append(HumanMessage(content=question))
    
    # Extract the content from flowmessages and join them into a single string
    prompt = " ".join([message.content for message in st.session_state['flowmessages']])
    
    # Call the language model with the prompt string
    answer = llm(prompt)
    
    st.session_state['flowmessages'].append(AIMessage(content=answer))
    return answer  # Return the content of the answer (assuming it is a string)



input=st.text_input("Input: ",key="input")
response=get_chatmodel_response(input)

submit=st.button("Ask the question")



if submit:
    st.subheader("The Response is")
    st.write(response)