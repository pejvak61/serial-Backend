from flask import request
from flask import Flask
app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

def do_the_login():
    return ("logged in")

def show_the_login_form():
    return ("Showing login form")

@app.route('/test', methods=['POST'])
def test():
    return ("This is a test")