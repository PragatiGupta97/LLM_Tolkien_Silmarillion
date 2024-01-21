from lang_funcs import *
from langchain.llms import Ollama
from langchain import PromptTemplate

#ignore warnings
import warnings
warnings.filterwarnings('ignore')
def load_models():
    # Loading orca-mini from Ollama
    llm = Ollama(model="mistral", temperature=0)

    # Loading the Embedding Model
    embed = load_embedding_model(model_path="all-MiniLM-L6-v2")
    
    return embed,llm

def create_db(embed,file_path="The_Silmarillion.pdf"):
    docs = load_pdf_data(file_path)
    documents = split_docs(documents=docs)

    # creating vectorstore
    vectorstore = create_embeddings(documents, embed)

    # converting vectorstore to a retriever
    retriever = vectorstore.as_retriever()
    
    return retriever




def create_prompt():
    template = """
    ### System:
    You are an respectful and honest assistant. You have to answer the user's questions using only the context \
    provided to you. If you don't know the answer, just say you don't know. Don't try to make up an answer.

    ### Context:
    {context}

    ### User:
    {question}

    ### Response:
    """

    
    
    return template

def create_chain(retriever,llm):
    template = create_prompt()
    prompt = PromptTemplate.from_template(template)
    chain = load_qa_chain(retriever, llm, prompt)
    return chain


if __name__ == "__main__":

    embed,llm = load_models()
    #check the vectorstore folder for the vectorstore

    #retriever = create_db(embed)
    retriever = load_retriever(embed)
    chain = create_chain(retriever,llm)
    get_response("How did Gondolin fall?", chain)
    
    
    
    
    


    