import streamlit as st
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    Settings,
)
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
from constant import info


# get the user's input by calling the get_text function
def get_text():
    input_text = st.text_input(
        "After providing OpenAI API Key on the sidebar, you can send your questions and hit Enter to know more about me from my AI agent, Buddy!",
        key="input",
    )
    return input_text


def get_open_api_key():
    openai_api_key = st.sidebar.text_input(
        "Enter your OpenAI API Key and hit Enter", type="password"
    )
    if openai_api_key and not openai_api_key.startswith("sk-"):
        st.warning(
            "Please enter a valid open api key that startswith sk-", icon="⚠"
        )
        return None
    return openai_api_key


def get_personal_bio_documents():
    documents = SimpleDirectoryReader(input_files=["bio.txt"]).load_data()
    return documents


def ask_bot(input_text, name, pronoun, openai_api_key):
    # define LLM
    llm = OpenAI(
        model_name="gpt-4o-mini",
        temperature=0,
        api_key=openai_api_key,
    )

    Settings.llm = llm
    Settings.embed_model = OpenAIEmbedding(api_key=openai_api_key)
    documents = get_personal_bio_documents()
    index = VectorStoreIndex.from_documents(documents)

    # query LlamaIndex and GPT-3.5 for the AI's response
    PROMPT_QUESTION = f"""You are Buddy, an AI assistant dedicated to assisting {name} in her job search by providing recruiters with relevant and concise information. 
    If you do not know the answer, politely admit it and let recruiters know how to contact {name} to get more information directly from {pronoun}. 
    Don't put "Buddy" or a breakline in the front of your answer.
    Human: {input_text}
    """

    output = index.as_query_engine().query(
        PROMPT_QUESTION.format(input=input_text)
    )
    print(f"output: {output}")
    return output.response


def chat_with_bot():
    user_input = get_text()
    print(f"user input: {user_input}")
    openai_api_key = get_open_api_key()
    if user_input and openai_api_key and openai_api_key.startswith("sk-"):
        try:
            st.info(
                ask_bot(
                    user_input, info["Name"], info["Pronoun"], openai_api_key
                )
            )
        except Exception as e:
            st.error("🚨 Something went wrong while querying the assistant.")
            st.exception(e)
    elif not openai_api_key:
        st.warning(
            "Please enter a valid open api key that startswith sk-", icon="⚠"
        )
