"""Sample FastAPI code"""
from fastapi import FastAPI

app = FastAPI()


@app.get("/items")
async def get_items():
    """
    Sample FastAPI method
    """
    return {"message": "Hello World"}
