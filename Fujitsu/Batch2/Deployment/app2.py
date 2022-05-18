from flask import Flask,request
import joblib, json

model = joblib.load("ccpp_model.pkl")

# create an object (app) of type class Flask
app = Flask(__name__)

# use decorator route from app, to decorate a function, so that it returns some text when it receives request on a URL
@app.route("/",methods=['GET','POST'])
def fun1():
    data = request.data
    data = data.decode() # bytes to string
    data = json.loads(data) # strint to python dictionary
    out = model.predict(data['values'])
    print(data,type(data))
    return "Predictions for given values of AT,V,AP,RH are "+str(out)


if __name__=="__main__":
    app.run(port=5000)