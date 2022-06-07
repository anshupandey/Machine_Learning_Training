# pip install fastapi uvicorn

from fastapi import FastAPI
import uvicorn
import joblib
from pydantic import BaseModel
model = joblib.load("ccpp_model.pkl")

app = FastAPI()

# data validation
class request_body(BaseModel):
    AT:float
    V:float
    AP:float
    RH:float
            

@app.post("/predict")
def mainfun(data:request_body):
    data = [[data.AT,data.V,data.AP,data.RH]]
    pred = model.predict(data)
    return {"prediction":str(round(pred[0],3))}

@app.get("/")
def fun1():
    return {"message":"Hello World from FastAPI"}


@app.get("/blr")
def fun2():
    return {"message":"Hello World from Bangalore"}


if __name__=="__main__":
    uvicorn.run(app,port=8000)