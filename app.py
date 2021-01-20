from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def hello():
    
    f = open("response.txt", 'w+')
    print ("headers", file=f)
    print (request.headers, file=f)
    cookies = request.headers.get("Cookie")
    print (cookies, file=f)
    return "ok"
