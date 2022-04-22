from flask import Flask, render_template, request
import json
import joblib
prep = joblib.load("preprocessor.pkl")
model = joblib.load("model.pkl")


app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def main():
    return render_template("index.html")

@app.route("/predict",methods=['GET','POST'])
def main2():
    data = request.form
    data = dict(data)
    newcust = [data['cs'],data['geo'],data['gen'],data['age'],data['bal'],data['nop'],data['iam']]
    newcust = prep.transform([newcust])
    output = model.predict(newcust)[0]
    print(data,type(data))
    return "Prediction is "+str(output)

if __name__=="__main__":
    app.run(port=5000)