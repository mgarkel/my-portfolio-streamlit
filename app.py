import streamlit as st
from components.chatbot import chat_with_bot
from components.contact import render_contact_section
from components.info import render_intro_section
from components.skills import render_skills_section
from components.work_experience import render_career_snapshot
from constant import *

st.set_page_config(page_title="Template", layout="wide", page_icon="👧🏻")

# ----------------- Chatbot ----------------- #
chat_with_bot()

# ----------------- info ----------------- #
render_intro_section(
    info,
    lottie_url="https://assets9.lottiefiles.com/packages/lf20_x17ybolp.json",
)

# ----------------- skillset ----------------- #
render_skills_section()

# ----------------- timeline ----------------- #
render_career_snapshot(work_experience)

# -----------------  contact  ----------------- #
render_contact_section(info["Email"])
