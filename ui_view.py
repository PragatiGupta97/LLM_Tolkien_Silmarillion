import streamlit as st
import textwrap
from retrieval import *

st.title("Your Silmarillion Assistant")

with st.sidebar:
    with st.form(key='my_form'):
        query = st.sidebar.text_area(
            label="Ask me about The Elven world?",
            max_chars=50,
            key="query"
            )
        submit_button = st.form_submit_button(label='Submit')

if query:
    embed,llm = load_models()
    #check the vectorstore folder for the vectorstore
    #retriever = create_db(embed)
    retriever = load_retriever(embed)
    chain = create_chain(retriever,llm)
    
    response= get_response(query, chain)
    print("response is....",response)
    st.subheader("Answer:")
    st.text(textwrap.fill(response, width=85))