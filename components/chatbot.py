import os
from dotenv import load_dotenv

import streamlit as st
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter

from constant import info

load_dotenv()


def get_text():
    input_text = st.text_input(
        "Have a question about me? Ask my personal AI assistant, Buddy — a RAG-powered agent built to help recruiters quickly find the answers they need!",
        key="input",
    )
    if len(input_text.split()) > 10:
        st.warning("Sorry - please enter a question of 10 words or less.")
        return None
    return input_text


def load_documents():
    loader = TextLoader("bio.txt")
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return splitter.split_documents(docs)


@st.cache_resource
def load_qa_chain(name, pronoun):
    api_key = os.getenv("OPENAPI_KEY")
    embeddings = OpenAIEmbeddings(openai_api_key=api_key)
    llm = ChatOpenAI(model="gpt-4o", temperature=0, openai_api_key=api_key)

    docs = load_documents()
    vectorstore = FAISS.from_documents(docs, embeddings)
    retriever = vectorstore.as_retriever()

    prompt = PromptTemplate(
        template=(
            f"You are an AI assistant that helps recruiters learn about {name}'s background and experience."
            f"Use the provided context to answer. If unsure, say so and guide them to contact {name} directly for more info from {pronoun}.\n"
            f"Try to keep your answer to 1-2 paragraphs."
            f"Context:\n{{context}}\n\n"
            f"Question: {{question}}\n\n"
            f"Answer:"
        ),
        input_variables=["context", "question"],
    )

    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": prompt},
        return_source_documents=False,
    )


def ask_bot(user_input, name, pronoun):
    placeholder = st.empty()
    placeholder.info("🤔 Thinking...")

    qa_chain = load_qa_chain(name, pronoun)

    try:
        response = qa_chain.invoke(user_input)
        placeholder.info(response.get("result"))
    except Exception as e:
        st.error("🚨 Something went wrong while querying the assistant.")
        st.exception(e)


def chat_with_bot():
    user_input = get_text()
    if user_input:
        ask_bot(user_input, info["Name"], info["Pronoun"])
