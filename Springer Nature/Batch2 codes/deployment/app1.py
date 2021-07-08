from flask import Flask, request
import json
import joblib

app = Flask(__name__)
model = joblib.load("ccpp_model.pkl") # loading the trained model from the pickle file

@app.route("/",methods=['GET','POST'])
def main():
    return "Hello world from Flask"

@app.route("/predict",methods=['GET','POST'])
def main2():
    data = request.data # accepting data via post,get request
    print(data,type(data))
    data = data.decode() # converting from bytes to string
    data = json.loads(data) # string to dictionary
    data['predictions'] = model.predict(data['values']).tolist()
    return json.dumps(data)

if __name__=='__main__':
    app.run(port=5000,host="0.0.0.0")