from fastapi import FastAPI

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