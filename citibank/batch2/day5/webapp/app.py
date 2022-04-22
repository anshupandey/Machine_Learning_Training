from flask import Flask, render_template, request
import joblib

model = joblib.load("model.pkl")
prep = joblib.load("preprocesser.pkl")


app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/predict",methods=['GET','POST'])
def main2():
    data = request.form
    data = dict(data)
    vals = [data['cs'],data['geo'],data['gen'],data['age'],data['bal'],data['nop'],data['iam']]
    newcust = prep.transform([vals])
    out = model.predict(newcust)[0]
    if out==0:
        return "Customer will NOT leave the bank"
    else:
        return "Customer will leave the bank"

if __name__=="__main__":
    app.run(port=5000,debug=True)