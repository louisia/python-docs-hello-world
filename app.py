from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def hello():
    
    f = open("response.txt", 'w+')
    auth_ookies = request.headers.get("Cookie")
    response = requests.get('https://ztnaportal.azurewebsites.net/.auth/me',headers={'Cookie': auth_ookies})
    return response.json()[0]['user_id']
