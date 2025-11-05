# tests/test_smoke.py
import os
import importlib
from fastapi.testclient import TestClient

# use a tiny model to avoid large downloads in CI/local tests
os.environ.setdefault("MODEL_NAME", "sshleifer/tiny-bart")  # ~30MB
os.environ.setdefault("DEVICE", "cpu")
os.environ.setdefault("MAX_INPUT_TOKENS", "512")

api = importlib.import_module("src.nlp.summarizer.api")
app = api.app
client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_summarize_basic():
    payload = {"text": "Artificial intelligence enables computers to learn from data."}
    r = client.post("/summarize", json=payload)
    assert r.status_code == 200
    body = r.json()
    assert isinstance(body["summary"], str)
    assert isinstance(body["tokens"], int)
    assert isinstance(body["latency_ms"], int)
