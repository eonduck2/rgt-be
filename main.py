# main.py
from fastapi import FastAPI

app = FastAPI()

@app.post("/")
async def root():
    return {"message": "Hello, FastAPI!"}
