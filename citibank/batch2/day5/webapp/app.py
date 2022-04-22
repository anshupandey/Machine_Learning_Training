from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "Hello from citibank"

if __name__=="__main__":
    app.run(port=5000,debug=True)