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

