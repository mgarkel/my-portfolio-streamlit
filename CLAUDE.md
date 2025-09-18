# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a personal portfolio website built with Streamlit that showcases Manav Garkel's professional background, skills, and experience. The application features an interactive AI chatbot powered by RAG (Retrieval Augmented Generation) using OpenAI's GPT-4 and FAISS vector store.

## Common Development Commands

**Start the application:**
```bash
streamlit run app.py
```

**Install dependencies:**
```bash
poetry install
```

**Lint and format code:**
```bash
ruff check .          # Check for linting issues
ruff format .         # Format code
pre-commit run --all-files  # Run pre-commit hooks
```

**Deploy to AWS (if configured):**
```bash
./deploy-to-ecr.sh     # Deploy to ECR
./deploy-and-check.sh  # Deploy and verify
```

## Architecture

### Core Structure
- **`app.py`** - Main Streamlit application entry point
- **`constant.py`** - Contains all static data (work experience, personal info, hobbies)
- **`components/`** - Modular Streamlit components for different sections
- **`pages/`** - Multi-page Streamlit application structure
- **`utils/`** - Utility functions for common operations
- **`bio.txt`** - Text data source for the RAG chatbot
- **`.streamlit/config.toml`** - Streamlit theming configuration

### Component Architecture
The application uses a modular component structure:
- `components/info.py` - Personal introduction section
- `components/chatbot.py` - RAG-powered AI assistant
- `components/work_experience.py` - Professional experience timeline
- `components/skills.py` - Technical skills display
- `components/contact.py` - Contact information

### RAG Chatbot Implementation
The chatbot (`components/chatbot.py`) implements:
- FAISS vector store for document retrieval
- OpenAI embeddings and GPT-4 for generation
- LangChain RetrievalQA chain
- Document chunking with RecursiveCharacterTextSplitter
- Caches the QA chain using `@st.cache_resource`

### Environment Configuration
- Uses `python-dotenv` for environment variable management
- Requires `OPENAPI_KEY` environment variable for OpenAI integration
- Custom Streamlit theme configured in `.streamlit/config.toml`

## Key Dependencies
- **streamlit** - Web framework
- **langchain** + **langchain-openai** - RAG implementation
- **faiss-cpu** - Vector similarity search
- **openai** - GPT-4 integration
- **ruff** - Linting and formatting
- **pre-commit** - Git hooks for code quality

## Development Notes
- Python version constraint: `>=3.9,<3.9.7 || >3.9.7,<4.0.0`
- Uses Poetry for dependency management
- Ruff configured with 80-character line length
- Pre-commit hooks run ruff-format automatically
- All static data is centralized in `constant.py` for easy updates