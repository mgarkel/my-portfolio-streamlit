FROM python:3.13-slim

WORKDIR /app

# 1. Install build tools (including git & cmake), Poetry, and the export plugin
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
       build-essential \
       curl \
       git \
       cmake \
  && rm -rf /var/lib/apt/lists/* \
  && pip install --upgrade pip \
  && pip install poetry poetry-plugin-export \
  && poetry config virtualenvs.create false --local

# 2. Copy only pyproject files for cache
COPY pyproject.toml poetry.lock* /app/

# 3. Export dependencies and install via pip
RUN poetry export \
      --format=requirements.txt \
      --output=requirements.txt \
      --without dev \
      --without-hashes \
  && pip install --no-cache-dir -r requirements.txt

# 4. Copy your app
COPY . /app

# tell App Runner that your container listens on 8501
EXPOSE 8501

# bind to all interfaces, let Streamlit pick port 8501
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]
