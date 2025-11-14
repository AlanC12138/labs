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

GET /
GET /ui/

#### Health Check

GET /health
→ { "status": "ok" }

#### Summarization Endpoint

POST /summarize
Content-Type: application/json


Request:
```json
{
  "text": "...",
  "max_new_tokens": 128,
  "min_new_tokens": 32,
  "temperature": 1.0
}
Response:
{
  "summary": "...",
  "tokens": 284,
  "latency_ms": 412
}

### UI Layer (ui/)
Served directly through FastAPI via:
app.mount("/ui", StaticFiles(directory=UI_DIR, html=True))
Provides:
Input text area
Token controls
Temperature slider
"Summarize" button
Output with copy-to-clipboard
Latency + token stats
Frontend uses pure HTML + CSS + JavaScript, no frameworks.

