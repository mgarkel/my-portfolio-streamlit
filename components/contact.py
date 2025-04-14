# contact_section.py
import os
import streamlit as st


def render_contact_section(linkedin_url: str):
    st.title("📨 Contact Me")

    # LinkedIn CTA + Icon (top)
    linkedin_html = f"""
    <div style="text-align: left; margin-bottom: 30px;">
        <p style="font-size: 18px;">Prefer to connect on LinkedIn? Click the icon below!</p>
        <a href="{linkedin_url}" target="_blank" style="text-decoration: none;">
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg"
                 alt="LinkedIn"
                 style="width: 64px; height: 64px;">
        </a>
    </div>
    """

    # Contact form (below LinkedIn icon)
    form_submit_key = os.getenv("FORM_SUBMIT_KEY")
    contact_form = f"""
    <form action="https://formsubmit.co/{form_submit_key}" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

    # Render components
    st.markdown(linkedin_html, unsafe_allow_html=True)
    st.markdown(
        """
        <div style="text-align: center; margin: 20px 0; font-size: 16px; color: #666;">
            — or use the form below and I'll get back to you shortly —
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(contact_form, unsafe_allow_html=True)

    # Styling
    st.markdown(
        """
    <style>
        form {
            display: flex;
            flex-direction: column;
            margin-top: 20px;
        }
        input, textarea {
            margin-bottom: 10px;
            padding: 10px;
            border-radius: 6px;
            border: 1px solid #ccc;
            font-size: 15px;
        }
        button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 12px;
            border-radius: 6px;
            cursor: pointer;
            font-size: 15px;
        }
        button:hover {
            background-color: #45a049;
        }
        p {
            font-size: 18px;
            margin-bottom: 8px;
        }
        a:hover {
            opacity: 0.85;
        }
    </style>
    """,
        unsafe_allow_html=True,
    )
