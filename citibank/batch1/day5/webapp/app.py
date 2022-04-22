from flask import Flask

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def main():
    return "Hello World on Friday"

if __name__=="__main__":
    app.run(port=5000)