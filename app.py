from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def hello():
    
    f = open("response.txt", 'w+')
    auth_cookies = request.headers.get("Cookie")
    print (auth_cookies, file=f)
    response = requests.get('https://ztnaportal.azurewebsites.net/.auth/me',headers={'Cookie': auth_cookies})
    print (response, file=f)
    return response.json()[0]['user_id']
