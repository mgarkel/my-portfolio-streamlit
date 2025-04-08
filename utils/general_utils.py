import streamlit as st
from PIL import Image
from constant import info


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(
            "<style>{}</style>".format(f.read()), unsafe_allow_html=True
        )


def render_sidebar_photo():
    img = Image.open(info["Photo"])
    st.sidebar.image(img)
