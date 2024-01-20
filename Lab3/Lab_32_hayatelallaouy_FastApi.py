# Lab32 : FASTAPI
# Réalisé par : Hayat el allaouy/Emsi 2023-2024

from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"key": "Hello World"}

uvicorn.run(app, port=8000,host='0.0.0.0')