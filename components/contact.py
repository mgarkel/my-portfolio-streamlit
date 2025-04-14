# contact_section.py
import os
import streamlit as st


def render_contact_section(linkedin_url: str):
    form_submit_key = os.getenv("FORM_SUBMIT_KEY")
    st.subheader("📨 Contact Me")

    contact_form = f"""
    <form action="https://formsubmit.co/{form_submit_key}" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    <p style='margin-top: 10px;'>
        Or connect with me on 
        <a href="{linkedin_url}" target="_blank">LinkedIn</a>
    </p>
    """

    st.markdown(contact_form, unsafe_allow_html=True)

    st.markdown(
        """
    <style>
        form {
            display: flex;
            flex-direction: column;
        }
        input, textarea {
            margin-bottom: 10px;
            padding: 8px;
            border-radius: 5px;
            border: 1px solid #ccc;
            font-size: 14px;
        }
        button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
        p {
            font-size: 14px;
            margin-top: 12px;
        }
        a {
            color: #1a73e8;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
    """,
        unsafe_allow_html=True,
    )
