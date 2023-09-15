from flask import Flask
from flask import request 

app = Flask(__name__)

@app.route('/')
def index():
    user = request.headers.get('User')
    return 'Your browser is {}'.format(user)

@app.route('/<name>')

def print_name(name):
    return'Hi, {}'.format(name)

if __name__ == '__main__':
    app.run(debug=True)