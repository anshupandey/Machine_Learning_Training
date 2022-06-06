from flask import Flask,request
import json
import joblib

model = joblib.load("model.pkl")
transformer = joblib.load("transformer.pkl")
app = Flask(__name__)

@app.route("/predict",methods=['GET','POST'])
def main():
    data = request.data
    data = data.decode() # bytes to string
    data = json.loads(data) # string to dict
    for cust in data['data']:
        temp_data = [cust['cs'],cust['geo'],cust['gen'],cust['age'],cust['bal'],cust['nop'],cust['iam']]
        temp_data = transformer.transform([temp_data])
        cust['Prediction_proba'] = model.predict_proba(temp_data).tolist()
        cust['Prediction'] = model.predict(temp_data).tolist()  
    return json.dumps(data)

if __name__=="__main__":
    app.run(debug=True)