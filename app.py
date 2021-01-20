from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def hello():
    print ("cicd")
    print (request.data)
    print ("headers")
    print (request.headers)
    return "ok"
