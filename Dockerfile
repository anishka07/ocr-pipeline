FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies required for OCR
RUN apt-get update && apt-get install -y --no-install-recommends \
    tesseract-ocr \
    libgl1-mesa-glx \
    libglib2.0-0 \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency file
COPY pyproject.toml .

# Install UV and create virtual environment
RUN pip install uv
RUN uv sync

COPY app .

CMD ["uv", "run", "fastapi", "run"]
 