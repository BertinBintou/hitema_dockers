from fastapi import FastAPI
import time

app = FastAPI()
items = []

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/items")
def list_items():
    return items

@app.post("/items")
def add_item(name: str):
    items.append(name)
    return {"added": name}

@app.get("/slow")   # pour le jour 4
def slow():
    time.sleep(2)
    return {"slow": True}