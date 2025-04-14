import streamlit as st
from components.chatbot import chat_with_bot
from components.info import render_intro_section
from constant import *

st.set_page_config(page_title="Home", layout="wide", page_icon="👨🏻‍💻")

# ----------------- info ----------------- #
render_intro_section(info)

# ----------------- Visual Gap ----------------- #
st.markdown("<div style='margin-top: 40px;'></div>", unsafe_allow_html=True)

# ----------------- Chatbot ----------------- #
chat_with_bot()

# ----------------- Visual Gap ----------------- #
st.markdown("<div style='margin-top: 40px;'></div>", unsafe_allow_html=True)
