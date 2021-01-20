from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def hello():
    
    f = open("resonse.txt", 'w+')
    print ("headers", file=f)
    print (request.headers.Cookie, file=f)
    cookies = request.headers.Cookie
    print (cookies, file=f)
    return "ok"
