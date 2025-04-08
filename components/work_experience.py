import streamlit as st
from streamlit_timeline import st_timeline


def render_career_snapshot(work_experience: list):
    with st.container():
        # Inject styles to prevent item truncation
        st.markdown(
            """
            <style>
            .vis-item {
                white-space: normal !important;
                overflow: visible !important;
                text-overflow: unset !important;
                max-width: none !important;
                border-radius: 8px;
                padding: 6px 12px;
                font-size: 14px;
                box-shadow: 0 1px 3px rgba(0, 0, 0, 0.15);
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

        st.subheader("📌 Career Snapshot")

        options = {
            "stack": True,
            "orientation": "top",
            "zoomable": True,
            "editable": False,
            "margin": {"item": 30, "axis": 20},
            "verticalScroll": True,
            "horizontalScroll": True,
        }

        st_timeline(work_experience, options=options, height="750px")
