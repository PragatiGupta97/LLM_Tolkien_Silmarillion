import streamlit as st
import textwrap
from retrieval import *
import base64

st.title("Your Silmarillion Assistant")

import base64

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Use the function
set_png_as_page_bg("XLSdZFR.jpeg")

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