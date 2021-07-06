from flask import Flask, request
import json
import joblib

app = Flask(__name__)
model = joblib.load("ccpp_model.pkl")


@app.route("/",methods=["GET","POST"])
def main():
    return "Hello world from Flask"

@app.route("/predict",methods=["GET","POST"])
def main2():
    data = request.data # loading data from post request in bytes format
    data = data.decode() # converting bytes to string
    data = json.loads(data) # converting string to dictionary
    data['prediction'] = model.predict(data['values']).tolist()
    print(data,type(data))
    return json.dumps(data)

if __name__=="__main__":
    app.run(port=5000,host="0.0.0.0")