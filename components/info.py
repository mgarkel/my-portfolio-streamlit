# intro_section.py

import streamlit as st
from utils.general_utils import local_css, render_sidebar_photo


def gradient(color1, color2, color3, content1, content2):
    st.markdown(
        f'<h1 style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});font-size:60px;border-radius:2%;">'
        f'<span style="color:{color3};">{content1}</span><br>'
        f'<span style="color:white;font-size:17px;">{content2}</span></h1>',
        unsafe_allow_html=True,
    )


def render_intro_section(info: dict):
    # Load CSS
    local_css("style/style.css")

    # Sidebar profile image
    render_sidebar_photo()

    # Layout
    with st.container():
        full_name = info["Full_Name"]
        gradient(
            "#FFD4DD",
            "#000395",
            "#e0fbfc",
            f"Hi, I'm {full_name}👋",
            info["Intro"],
        )
        st.write("")
        st.write(info["About"])
