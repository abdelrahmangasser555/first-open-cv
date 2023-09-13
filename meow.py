from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"meow": "world"}

@app.get("/meow/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"meow": item_id, "q": q}

