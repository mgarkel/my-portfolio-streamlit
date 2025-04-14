import os

import streamlit as st
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    Settings,
)
from llama_index.core.response_synthesizers import get_response_synthesizer
from llama_index.core.prompts import PromptTemplate
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
from constant import info
from dotenv import load_dotenv

load_dotenv()


# get the user's input by calling the get_text function
def get_text():
    input_text = st.text_input(
        "Have a question about me? Ask my personal AI assistant, Buddy — a RAG-powered agent built to help recruiters quickly find the answers they need!",
        key="input",
    )
    if len(input_text.split()) > 10:
        st.warning("Sorry - please enter a question of 10 words or less.")
        return None
    return input_text


def get_personal_bio_documents():
    documents = SimpleDirectoryReader(input_files=["bio.txt"]).load_data()
    return documents


def ask_bot(input_text, name, pronoun):
    placeholder = st.empty()
    placeholder.info("🤔 Thinking...")

    # Load OpenAI API key from .env
    openai_api_key = os.getenv("OPENAPI_KEY")
    if not openai_api_key:
        placeholder.error("❌ OPENAPI_KEY not found in environment.")
        return

    # Set up LLM and embedding model
    llm = OpenAI(
        model_name="gpt-4o-mini",
        temperature=0,
        api_key=openai_api_key,
    )
    Settings.llm = llm
    Settings.embed_model = OpenAIEmbedding(api_key=openai_api_key)

    # Load documents and build index
    documents = get_personal_bio_documents()
    index = VectorStoreIndex.from_documents(documents)

    # Create custom prompt template (note the double braces)
    prompt_template = PromptTemplate(
        f"You're an AI assistant dedicated to assist {name} in his job search by providing recruiters with relevant and concise information."
        f"If you do not know the answer, politely admit it and let recruiters know how to contact {name} to get more information directly from {pronoun}."
        f"Don't put breakline in the front of your answer."
        f"Use the context below to answer the question.\n"
        "Context: {{context_str}}\n\n"
        "Question: {{query_str}}\n\n"
        "Answer:"
    )

    # Use retriever
    retriever = index.as_retriever()

    # Patch: Create a response synthesizer with your custom prompt
    response_synthesizer = get_response_synthesizer(
        text_qa_template=prompt_template
    )

    # Create a query engine with retriever + response synthesizer
    query_engine = RetrieverQueryEngine(
        retriever=retriever, response_synthesizer=response_synthesizer
    )

    # Query using the input text
    output = query_engine.query(input_text)
    print(f"output: {output}")

    placeholder.info(output.response)


def chat_with_bot():
    user_input = get_text()
    print(f"user input: {user_input}")
    if user_input:
        try:
            ask_bot(user_input, info["Name"], info["Pronoun"])
        except Exception as e:
            st.error("🚨 Something went wrong while querying the assistant.")
            st.exception(e)
