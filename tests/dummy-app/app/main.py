from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_root():
    return {"Message": "Testing FastAPI Cloud Action !! "}