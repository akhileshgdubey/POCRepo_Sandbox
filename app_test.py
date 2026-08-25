from fastapi import FASTAPI

app = FASTAPI()

app.get("/")

def home():
    return {"message": "Hello, World!"}

app.get("/health")
def health():
    return {"status": "healthy"}
