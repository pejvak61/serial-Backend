from flask import Flask, escape, url_for
from flask import request
import json
import db

app = Flask(__name__)

@app.route('/')
def index():
  return 'Index Page'

@app.route('/hello')
def say_hello():
  return 'Hello, greetings from different endpoint'

#adding variables
@app.route('/user/<username>')
def show_user(username):
  #returns the username
  return 'Username: %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
  #returns the post, the post_id should be an int
  return json.dumps(str(post_id))

@app.route('/dbconnectivity')
def connect():
  return db.db_connectivity()

@app.route('/auth')
def authentication(username = "ali", password = "123"):
  if username == "ali" and password == "123":
    return True
  return False

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