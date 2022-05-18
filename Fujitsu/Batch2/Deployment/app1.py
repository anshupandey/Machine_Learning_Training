from flask import Flask

# create an object (app) of type class Flask
app = Flask(__name__)

# use decorator route from app, to decorate a function, so that it returns some text when it receives request on a URL
@app.route("/",methods=['GET'])
def fun1():
    return "Hello WORLD from flask"

@app.route("/blr",methods=['GET'])
def fun2():
    out = "Bengaluru (also called Bangalore) is the capital of India's southern Karnataka state. The center of India's high-tech industry, the city is also known for its parks and nightlife. By Cubbon Park, Vidhana Soudha is a Neo-Dravidian legislative building. "
    return out

@app.route("/del",methods=['GET'])
def fun3():
    out = "Delhi, India’s capital territory, is a massive metropolitan area in the country’s north. In Old Delhi, a neighborhood dating to the 1600s, stands the imposing Mughal-era Red Fort, a symbol of India, and the sprawling Jama Masjid mosque, whose courtyard accommodates 25,000 people. "
    return out


if __name__=="__main__":
    app.run(port=5000)