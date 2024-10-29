# main.py
from fastapi import FastAPI

app = FastAPI()

@app.post("/order")
async def root():
    return {"message": "Hello, FastAPI!"}
