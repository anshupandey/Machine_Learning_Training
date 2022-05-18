# pip install flask

from flask import Flask, request, render_template
import joblib, json
app = Flask(__name__)
model =joblib.load("ccpp_model.pkl")


@app.route("/",methods=['GET','POST'])
def fun1():
    return render_template("index.html")


@app.route("/predict",methods=['GET','POST'])
def fun2():
    data = request.form
    data = dict(data) # to python dictionary
    data = [[data['at'],data['v'],data['ap'],data['rh']]]
    out = model.predict(data)
    print(data,type(data))
    return "Prediction for today is = "+str(out[0]) + " MW"


if __name__=="__main__":
    app.run(port=5000,host="0.0.0.0")