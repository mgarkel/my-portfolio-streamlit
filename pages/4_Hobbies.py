import streamlit as st
from constant import hobbies
from utils.general_utils import local_css, render_sidebar_photo

st.set_page_config(page_title="Hobbies", page_icon="🎯")

local_css("style/style.css")
render_sidebar_photo()

st.title("🎯 Hobbies & Interests")

st.markdown("Here’s a snapshot of what I enjoy outside of work:")

# Layout: 2 hobbies per row
cols = st.columns(2)

for idx, (emoji, title, desc) in enumerate(hobbies):
    with cols[idx % 2]:
        st.markdown(
            f"""
                <div class='hobby-card'>
                    <h3 style='margin-bottom: 0.5rem; color: white;'>{emoji} {title}</h3>
                    <p style='margin: 0; font-size: 15px;'>{desc}</p>
                </div>
                """,
            unsafe_allow_html=True,
        )
