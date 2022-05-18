# pip install flask

from flask import Flask

app = Flask(__name__)

# we will use builtin decorator in app object (class Flask) to decorate a function to return specific text when input REST request is received
@app.route("/")
def fun1():
    return "Hello World from Flask"

@app.route("/code1")
def fun2():
    out = """ 
    import pandas as pd
    <br><br>
    df = pd.read_csv(r"abc.csv")<br>
    df.head()
    """
    return out

if __name__=="__main__":
    app.run(port=5000,host="0.0.0.0")