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

# Pre-download ALL NLTK data so startup is instant (no runtime downloads)
# download_dir must match NLTK_DATA so the runtime finds them without re-downloading
ENV NLTK_DATA=/app/models/nltk_data
RUN mkdir -p /app/models/nltk_data && python -c "import nltk; [nltk.download(p, download_dir='/app/models/nltk_data') for p in ['wordnet','omw-1.4','words','punkt','punkt_tab','averaged_perceptron_tagger','averaged_perceptron_tagger_eng']]"

# Pre-download GPT-2 Small (~500MB) for perplexity scoring (anti-GPTZero)
RUN python -c "\
from transformers import GPT2LMHeadModel, GPT2TokenizerFast; \
t = GPT2TokenizerFast.from_pretrained('gpt2'); \
m = GPT2LMHeadModel.from_pretrained('gpt2'); \
t.save_pretrained('/app/models/gpt2-small'); \
m.save_pretrained('/app/models/gpt2-small'); \
print('[Docker] GPT-2 Small saved to /app/models/gpt2-small')"

# Copy the rest of the app (model weights in models/ are excluded via .dockerignore)
COPY . .

# Hugging Face Spaces requires port 7860
EXPOSE 7860

# Gunicorn: 1 worker (model loaded once), 4 threads (handles concurrent users)
CMD ["gunicorn", "-w", "1", "--threads", "4", "-b", "0.0.0.0:7860", "app:app", "--timeout", "180", "--log-level", "info"]
