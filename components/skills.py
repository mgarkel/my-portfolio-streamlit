import streamlit as st


def render_skills_section():
    with st.container():
        st.subheader("⚒️ Skills")

        with st.expander("💻 Languages"):
            st.markdown(
                "Python, Java, JavaScript, SQL, Bash, Groovy, C, C++, MATLAB"
            )

        with st.expander("🌐 Web & API Development"):
            st.markdown(
                "Flask, FastAPI, Streamlit, Node.js/Express, AngularJS, Grails, RESTful APIs, HTML5, CSS, jQuery, Requests"
            )

        with st.expander("🗄️ Databases"):
            st.markdown(
                "Oracle, IBM DB2, Sybase, MSSQL, DynamoDB, MongoDB, Snowflake"
            )

        with st.expander("🛠️ DevOps & Tools"):
            st.markdown(
                "Docker, Kubernetes, Jenkins, Git, Linux/Unix, Poetry, Conda, .venv, Pre-commit hooks, Oauth2.0, Postman, JIRA, Heroku, Twilio, Wireshark"
            )

        with st.expander("☁️ Cloud Platforms"):
            st.markdown("AWS, GCP, Azure")

        with st.expander("🧪 Testing & Automation"):
            st.markdown(
                "Pytest, monkeypatch, FitNesse, Integration & Regression Testing"
            )

        with st.expander("📊 Data Science & ML"):
            st.markdown(
                "Pandas, NumPy, Scikit-learn, PySpark, Hadoop, Classification, Clustering, Recommendation Systems, Anomaly Detection, Association Rule Mining, Dimensionality Reduction, Data Preprocessing"
            )

        with st.expander("🧠 AI / LLMs"):
            st.markdown("LLMs, RAG, Agentic Systems")

        with st.expander("📦 Other"):
            st.markdown("Microservices, Agile Methodologies, Web Scraping")
