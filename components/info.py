# intro_section.py

import streamlit as st
import requests
from streamlit_lottie import st_lottie


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


def gradient(color1, color2, color3, content1, content2):
    st.markdown(
        f'<h1 style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});font-size:60px;border-radius:2%;">'
        f'<span style="color:{color3};">{content1}</span><br>'
        f'<span style="color:white;font-size:17px;">{content2}</span></h1>',
        unsafe_allow_html=True,
    )


def render_intro_section(info: dict, lottie_url: str = None):
    # Load CSS
    local_css("style/style.css")

    # Sidebar profile image
    st.sidebar.markdown(info["Photo"], unsafe_allow_html=True)

    # Load Lottie animation
    lottie_gif = load_lottieurl(lottie_url) if lottie_url else None

    # Layout
    with st.container():
        col1, col2 = st.columns([8, 3])

        full_name = info["Full_Name"]
        with col1:
            gradient(
                "#FFD4DD",
                "#000395",
                "#e0fbfc",
                f"Hi, I'm {full_name}👋",
                info["Intro"],
            )
            st.write("")
            st.write(info["About"])

        with col2:
            if lottie_gif:
                st_lottie(lottie_gif, height=280, key="data")
