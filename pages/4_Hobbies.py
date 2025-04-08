import streamlit as st
from PIL import Image
from utils.general_utils import local_css, render_sidebar_photo

local_css("style/style.css")
render_sidebar_photo()

img_1 = Image.open("images/1.jpg")
img_2 = Image.open("images/2.png")
img_3 = Image.open("images/3.png")

st.title("🫶 Hobbies")

col1, col2, col3 = st.columns(3)

with col1:
    st.image(img_1)

with col2:
    st.image(img_2)

with col3:
    st.image(img_3)
