import streamlit as st
from components.chatbot import chat_with_bot
from components.contact import render_contact_section
from components.info import render_intro_section
from constant import *

st.set_page_config(page_title="Template", layout="wide", page_icon="👧🏻")

# ----------------- info ----------------- #
render_intro_section(
    info,
    lottie_url="https://assets9.lottiefiles.com/packages/lf20_x17ybolp.json",
)

# ----------------- Visual Gap ----------------- #
st.markdown("<div style='margin-top: 40px;'></div>", unsafe_allow_html=True)

# ----------------- Chatbot ----------------- #
chat_with_bot()

# ----------------- Visual Gap ----------------- #
st.markdown("<div style='margin-top: 40px;'></div>", unsafe_allow_html=True)

# -----------------  contact  ----------------- #
render_contact_section(info["Email"])
