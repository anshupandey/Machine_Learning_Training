# pip install fastapi uvicorn

from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def fun1():
    return {"message":"Hello World from FastAPI"}


@app.get("/blr")
def fun2():
    return {"message":"Hello World from Bangalore"}
