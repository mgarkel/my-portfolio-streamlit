from components.work_experience import (
    render_career_snapshot,
    render_work_experience_page,
)
from constant import work_experience
import streamlit as st

render_work_experience_page(work_experience)
st.markdown("<div style='margin-top: 40px;'></div>", unsafe_allow_html=True)
render_career_snapshot(work_experience)
