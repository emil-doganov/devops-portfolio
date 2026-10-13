from flask import Flask

app = Flask(__name__)

@app.get("/")
def hello():
    return {"message": "Hello, World!!!"}

@app.get("/health")
def health():
    return{"status": "healthy"}
