# ─── Base ─────────────────────────────────────────────────────────────────────
FROM python:3.13-slim

WORKDIR /app

# ─── Install build tools, Poetry & export plugin ─────────────────────────────
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

# ─── Install Python deps ──────────────────────────────────────────────────────
COPY pyproject.toml poetry.lock* /app/
RUN poetry export \
      --format=requirements.txt \
      --output=requirements.txt \
      --without dev \
      --without-hashes \
  && pip install --no-cache-dir -r requirements.txt

# ─── Copy app code ────────────────────────────────────────────────────────────
COPY . /app

# ─── Expose & run ─────────────────────────────────────────────────────────────
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]
