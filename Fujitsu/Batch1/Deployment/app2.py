# pip install flask

from flask import Flask, request
import joblib, json
app = Flask(__name__)
model =joblib.load("ccpp_model.pkl")

@app.route("/predict",methods=['GET','POST'])
def fun1():
    data = request.data
    data = data.decode() # byte  to string
    data = json.loads(data) # python string to python dictionary
    data = data["values"]
    out = model.predict(data)
    print(data,type(data))
    return "Prediction for today is = "+str(out[0]) + " MW"


if __name__=="__main__":
    app.run(port=5000)