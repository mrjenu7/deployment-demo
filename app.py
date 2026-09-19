from fastapi import FastAPI
import os

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Hello from my first production deployment!"
    }


@app.get("/hello/{name}")
def hello(name: str):
    return {
        "message": f"Hello {name}!"
    }

@app.get("/secret")
def secret():
    message = os.getenv("SECRET_MESSAGE", "Secret message not configured")
    
    return {
        "message": message
    }