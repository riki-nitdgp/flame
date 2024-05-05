from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def read_root():
    return {"message": "service is running up and fine"}