import streamlit as st
import base64
from utils.general_utils import local_css, render_sidebar_photo

local_css("style/style.css")
render_sidebar_photo()

st.title("📝 Resume")
with open("images/Manav_Garkel_Resume.pdf", "rb") as f:
    base64_pdf = base64.b64encode(f.read()).decode("utf-8")
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="1000mm" height="1000mm" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)
