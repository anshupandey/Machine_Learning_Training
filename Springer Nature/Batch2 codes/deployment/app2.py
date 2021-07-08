from flask import Flask, request, render_template
import json
import joblib

app = Flask(__name__)
model = joblib.load("ccpp_model.pkl") # loading the trained model from the pickle file

@app.route("/",methods=['GET','POST'])
def main():
    return render_template("index.html")

@app.route("/predict",methods=['GET','POST'])
def main2():
    data = request.form # accepting data from form
    data = dict(data)
    print(data,type(data))
    values = [data['AT'],data['V'],data['AP'],data['RH']]
    values = [int(k[0]) for k in values]
    data['predictions'] = model.predict([values]).tolist()
    return render_template("output.html",output=data)

if __name__=='__main__':
    app.run(port=5000,host="0.0.0.0")