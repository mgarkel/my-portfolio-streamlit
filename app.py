import json

import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_timeline import timeline
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    ServiceContext,
)
from llama_index.llms.openai import OpenAI
from constant import *
import openai

st.set_page_config(page_title="Template", layout="wide", page_icon="👧🏻")

# -----------------  chatbot  ----------------- #
# Set up the OpenAI key
openai_api_key = st.sidebar.text_input(
    "Enter your OpenAI API Key and hit Enter", type="password"
)
openai.api_key = openai_api_key

# load the file
documents = SimpleDirectoryReader(input_files=["bio.txt"]).load_data()

pronoun = info["Pronoun"]
name = info["Name"]


def ask_bot(input_text):
    # define LLM
    llm = OpenAI(
        model_name="gpt-3.5-turbo",
        temperature=0,
        openai_api_key=openai.api_key,
    )
    service_context = ServiceContext.from_defaults(llm=llm)

    # load index
    index = VectorStoreIndex.from_documents(
        documents, service_context=service_context
    )

    # query LlamaIndex and GPT-3.5 for the AI's response
    PROMPT_QUESTION = f"""You are Buddy, an AI assistant dedicated to assisting {name} in her job search by providing recruiters with relevant and concise information. 
    If you do not know the answer, politely admit it and let recruiters know how to contact {name} to get more information directly from {pronoun}. 
    Don't put "Buddy" or a breakline in the front of your answer.
    Human: {input}
    """

    output = index.as_query_engine().query(
        PROMPT_QUESTION.format(input=input_text)
    )
    print(f"output: {output}")
    return output.response


# get the user's input by calling the get_text function
def get_text():
    input_text = st.text_input(
        "After providing OpenAI API Key on the sidebar, you can send your questions and hit Enter to know more about me from my AI agent, Buddy!",
        key="input",
    )
    return input_text


# st.markdown("Chat With Me Now")
user_input = get_text()

if user_input:
    # text = st.text_area('Enter your questions')
    if not openai_api_key.startswith("sk-"):
        st.warning(
            "⚠️Please enter your OpenAI API key on the sidebar.", icon="⚠"
        )
    if openai_api_key.startswith("sk-"):
        st.info(ask_bot(user_input))

# -----------------  loading assets  ----------------- #
st.sidebar.markdown(info["Photo"], unsafe_allow_html=True)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(
            "<style>{}</style>".format(f.read()), unsafe_allow_html=True
        )


local_css("style/style.css")

# loading assets
lottie_gif = load_lottieurl(
    "https://assets9.lottiefiles.com/packages/lf20_x17ybolp.json"
)


# ----------------- info ----------------- #
def gradient(color1, color2, color3, content1, content2):
    st.markdown(
        f'<h1 style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});font-size:60px;border-radius:2%;">'
        f'<span style="color:{color3};">{content1}</span><br>'
        f'<span style="color:white;font-size:17px;">{content2}</span></h1>',
        unsafe_allow_html=True,
    )


with st.container():
    col1, col2 = st.columns([8, 3])

full_name = info["Full_Name"]
with col1:
    gradient(
        "#FFD4DD", "#000395", "e0fbfc", f"Hi, I'm {full_name}👋", info["Intro"]
    )
    st.write("")
    st.write(info["About"])


with col2:
    st_lottie(lottie_gif, height=280, key="data")

# ----------------- skillset ----------------- #
with st.container():
    with st.container():
        st.subheader("⚒️ Skills")

        with st.expander("💻 Languages"):
            st.markdown(
                "Python, Java, JavaScript, SQL, Bash, Groovy, C, C++, MATLAB"
            )

        with st.expander("🌐 Web & API Development"):
            st.markdown(
                "Flask, FastAPI, Streamlit, Node.js/Express, AngularJS, Grails, RESTful APIs, HTML5, CSS, jQuery, Requests"
            )

        with st.expander("🗄️ Databases"):
            st.markdown(
                "Oracle, IBM DB2, Sybase, MSSQL, DynamoDB, MongoDB, Snowflake"
            )

        with st.expander("🛠️ DevOps & Tools"):
            st.markdown(
                "Docker, Kubernetes, Jenkins, Git, Linux/Unix, Poetry, Conda, .venv, Pre-commit hooks, Oauth2.0, Postman, JIRA, Heroku, Twilio, Wireshark"
            )

        with st.expander("☁️ Cloud Platforms"):
            st.markdown("AWS, GCP, Azure")

        with st.expander("🧪 Testing & Automation"):
            st.markdown(
                "Pytest, monkeypatch, FitNesse, Integration & Regression Testing"
            )

        with st.expander("📊 Data Science & ML"):
            st.markdown(
                "Pandas, NumPy, Scikit-learn, PySpark, Hadoop, Classification, Clustering, Recommendation Systems, Anomaly Detection, Association Rule Mining, Dimensionality Reduction, Data Preprocessing"
            )

        with st.expander("🧠 AI / LLMs"):
            st.markdown("LLMs, RAG, Agentic Systems")

        with st.expander("📦 Other"):
            st.markdown("Microservices, Agile Methodologies, Web Scraping")

# ----------------- timeline ----------------- #
with st.container():
    st.markdown("""""")
    st.subheader("📌 Career Snapshot")

    # load data
    with open("example.json", "r") as f:
        data = f.read()

    # render timeline
    timeline(data, height=400)

    # -----------------  contact  ----------------- #
    with col2:
        st.subheader("📨 Contact Me")
        contact_form = f"""
        <form action="https://formsubmit.co/{info["Email"]}" method="POST">
            <input type="hidden" name="_captcha value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)
