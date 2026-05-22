# ─────────────────────────────────────────────────────────────────────────────
# HumanizeDoc — Hugging Face Spaces Dockerfile
# Runs on the free CPU tier (16 GB RAM, 2 vCPUs)
# Port 7860 is required by Hugging Face Spaces
# ─────────────────────────────────────────────────────────────────────────────
FROM python:3.11-slim

# System dependencies (needed by some transformers tokenizers)
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python dependencies first (layer-cached, only rebuilds on changes)
COPY requirements-prod.txt .
RUN pip install --no-cache-dir -r requirements-prod.txt

# Pre-download NLTK data so startup is instant
RUN python -c "import nltk; nltk.download('wordnet'); nltk.download('omw-1.4')"

# Copy the rest of the app (model weights in models/ are excluded via .dockerignore)
COPY . .

# Hugging Face Spaces requires port 7860
EXPOSE 7860

# Gunicorn: 1 worker (model loaded once), 4 threads (handles concurrent users)
CMD ["gunicorn", "-w", "1", "--threads", "4", "-b", "0.0.0.0:7860", "app:app", "--timeout", "180", "--log-level", "info"]
