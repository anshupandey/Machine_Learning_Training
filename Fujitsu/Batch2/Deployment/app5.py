from flask import Flask,request, render_template
import joblib, json
#import sqlite3

#conn = sqlite3.connect("mydb.db")

model = joblib.load("ccpp_model.pkl")

# create an object (app) of type class Flask
app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def fun1():
    return render_template("index.html")
    
@app.route("/predict",methods=['GET','POST'])
def fun2():
    data = request.form
    data = dict(data) # strint to python dictionary
    newd = [float(data['at']),float(data['v']),float(data['ap']),float(data['rh'])]
    out = model.predict([newd])
    data['prediction'] = out[0]
    print(data,type(data))
    #data = pd.DataFrame(data)
    #data.to_sql(con=conn,name='prediction_data',if_exist='append')
    return json.dumps(data)


if __name__=="__main__":
    app.run(port=5000,host="0.0.0.0")