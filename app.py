from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def hello():
    
    f = open("resonse.txt", 'w+')
    print (request.data, file=f)
    print ("headers", file=f)
    print (request.headers, file=f)
    return "ok"
