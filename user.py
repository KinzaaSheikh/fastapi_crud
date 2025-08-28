from fastapi import FastAPI

app = FastAPI()

@app.get("/user")
def index():
    return {"message": "Welcome to FastAPI nerds"}
