from flask import Flask

app = Flask(__name__)


@app.route("/",methods=['GET','POST'])
def main():
    return "Hello World from FLASK"

@app.route("/anshu",methods=['GET','POST'])
def main2():
    return "Hello World from Anshu"


if __name__=='__main__':
    app.run(port=5000)