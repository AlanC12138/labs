# AI Document Summarizer

A lightweight end-to-end text-summarization service built with **FastAPI**, **Hugging Face Transformers**, and a simple **HTML/JS UI**. Runs locally or in Docker with zero external dependencies.

---

## Features

- Fast REST API for text summarization  
- Powered by `facebook/bart-large-cnn`  
- Deterministic or sampling-based generation (temperature support)  
- Returns **latency** and **token usage**  
- Clean static UI served at `/ui/`  
- Full Docker support  
- Auto CPU/GPU device resolution  
- Minimal, production-style code layout  

---

## Project Structure
```text
src/
└── nlp/
    └── summarizer/
        ├── api.py             # FastAPI application + endpoints + UI mounting
        ├── model.py           # Summarizer class using Hugging Face pipeline
        ├── ui/                # Static UI served at /ui/
        │   ├── index.html
        │   ├── app.js
        │   └── styles.css
        └── requirements.txt   # Python dependencies
```
---

## How It Works

### 1. Model Layer (`model.py`)

Implements a wrapper around Hugging Face:

- `AutoTokenizer`
- `AutoModelForSeq2SeqLM`
- `pipeline("summarization")`

Supports:

- Automatic device resolution (`cpu`, `cuda`, `auto`)
- Robust input truncation
- Token counting
- Latency measurement

---

### 2. API Layer (`api.py`)

#### UI Routing
```text
GET /
GET /ui/
```
#### Health Check
```text
GET /health
→ { "status": "ok" }
```
#### Summarization Endpoint
```text
POST /summarize
Content-Type: application/json
```

Request:
```json
{
  "text": "...",
  "max_new_tokens": 128,
  "min_new_tokens": 32,
  "temperature": 1.0
}
```
Response:
```json
{
  "summary": "...",
  "tokens": 284,
  "latency_ms": 412
}
```
---
### 3. UI Layer (ui/)
Served directly through FastAPI via:
```python
app.mount("/ui", StaticFiles(directory=UI_DIR, html=True))
```

Provides:
- Input text area
- Token controls
- Temperature slider
- "Summarize" button
- Output with copy-to-clipboard
- Latency + token stats
  
Frontend uses pure HTML + CSS + JavaScript, no frameworks.

---

## Running Locally
### 1. Install dependencies
```bash
pip install -r src/nlp/summarizer/requirements.txt
```

### 2. Run the server
```bash
uvicorn src.nlp.summarizer.api:app --host 0.0.0.0 --port 8000 --reload
```

### 3. Open the UI
```bash
http://localhost:8000/ui/
```

---

## Running in Docker
### 1. Build the image
```bash
docker build -t summarizer -f src/nlp/summarizer/Dockerfile .
```

### 2. Run the container
```bash
docker run -p 8000:8000 summarizer
```

### 3. Open:
```bash
http://localhost:8000/ui/
```

---

## Configuration

Environment variables:

| Variable         | Description                  | Default                 |
|------------------|------------------------------|-------------------------|
| MODEL_NAME       | HuggingFace model name       | facebook/bart-large-cnn |
| DEVICE           | cpu / cuda / auto            | auto                    |
| MAX_INPUT_TOKENS | Max input tokens allowed     | 2048                    |
| SEED             | Random seed                  | 42                      |

Example:

```bash
DEVICE=cuda MODEL_NAME=sshleifer/distilbart-cnn-12-6 uvicorn src.nlp.summarizer.api:app --port 8000
```

---

## Tests

A light test suite (under `tests/`) checks:
- Model initialization
- API response structure
- Summarization output shape
- `/health` endpoint

Run with:
```bash
pytest
```

--- 

## Why This Project Exists

This project demonstrates a fully self-contained ML application:
- ML model inference pipeline
- Production-style REST API
- Static frontend served by backend
- Portable Docker packaging
- CPU-friendly defaults
- Clean, maintainable code

Useful as a template for:
- Internal summarization tools
- Document-processing utilities
- Lightweight ML demos
- Backend engineering practice

---

## Future Improvements
- GPU-enabled Dockerfile
- Batch summarization
- Streaming output
- Model hot-swapping
- Auth/rate limiting
- Multi-language support
