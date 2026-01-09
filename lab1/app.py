from flask import Flask
import os
from datetime import datetime

app = Flask(__name__)

DATA_DIR = os.environ.get("DATA_DIR", "/data")
COUNTER_PATH = os.path.join(DATA_DIR, "counter.txt")
LOG_PATH = os.path.join(DATA_DIR, "app.log")

def ensure_data_dir():
    os.makedirs(DATA_DIR, exist_ok=True)

def read_counter() -> int:
    try:
        with open(COUNTER_PATH, "r", encoding="utf-8") as f:
            return int(f.read().strip() or "0")
    except FileNotFoundError:
        return 0

def write_counter(value: int) -> None:
    with open(COUNTER_PATH, "w", encoding="utf-8") as f:
        f.write(str(value))

def log(line: str) -> None:
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(line + "\n")

@app.get("/")
def hello():
    ensure_data_dir()
    c = read_counter() + 1
    write_counter(c)
    log(f"{datetime.utcnow().isoformat()}Z  hit={c}")
    return {"message": "hello from container", "hits": c}

@app.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    ensure_data_dir()
    app.run(host="0.0.0.0", port=8000)
