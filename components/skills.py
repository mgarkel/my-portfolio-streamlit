import streamlit as st


def render_skills_section():
    with st.container():
        st.subheader("⚒️ Skills")

        with st.expander("💻 Languages"):
            st.markdown(
                "Python, Java, JavaScript, SQL, Bash, Groovy, PySpark, C, C++, MATLAB"
            )

        with st.expander("🌐 Web & API Development"):
            st.markdown(
                "Flask, FastAPI, Requests, Streamlit, Node.js/Express, RESTful APIs, HTML5, CSS, jQuery"
            )

        with st.expander("🗄️ Databases"):
            st.markdown(
                "Oracle, IBM DB2, Sybase, MSSQL, DynamoDB, MongoDB, Snowflake"
            )

        with st.expander("🛠️ DevOps & Tools"):
            st.markdown(
                "Docker, Kubernetes, CI-CD, Jenkins, Git, Linux/Unix, Poetry, Oauth2.0, Postman"
            )

        with st.expander("☁️ Cloud Platforms"):
            st.markdown("AWS, GCP, Azure")

        with st.expander("🧪 Testing & Automation"):
            st.markdown(
                "Pytest, monkeypatch, FitNesse, Integration & Regression Testing"
            )

        with st.expander("🧠 AI & ML"):
            st.markdown(
                "LangChain, LangGraph, OpenAI, ChromaDB, FAISS, llama-index, Scikit-learn"
            )

        with st.expander("📦 Other"):
            st.markdown("Pandas, NumPy, Microservices, Agile Methodologies, JIRA")

