from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to Business Intelligence Agent API"
    }


@app.get("/health")
def health():
    return {
        "status": "Running"
    }