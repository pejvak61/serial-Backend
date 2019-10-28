from flask import Flask, escape, url_for
from flask import request
from flask import render_template,make_response
from http import HTTPStatus
from flask import Response
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
    return 'Username: %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return json.dumps(str(post_id))

@app.route('/dbconnectivity')
def connect():
    return db.db_connectivity()

@app.route('/auth')
def authentication(username = "ali", password = "123"):
    if username == "ali" and password == "123":
        return True
    return False

# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template('page_not_found.html'), 404

@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('page_not_found.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp    

@app.route('/createUser', methods=['post'])
def createUser(request.form['username'],request.form['password']):
    
    

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],request.form['password']):
            # return log_the_user_in(request.form['username'])
            return Response("{'message':'login succeed'}", status=201, mimetype='application/json')
        else:
            error = 'Invalid username/password'
    # return render_template('/login/login_error.html', error=error)
    return Response("{'message':'login failed'}", status=401, mimetype='application/json')

def valid_login(username, password):
    if username == "ali" and password == "123":
        return True
    return False

def log_the_user_in(username):
    return("login succeed")
    

def do_the_login():
    return ("logged in")

def show_the_login_form():
    return ("Showing login form")

@app.route('/test', methods=['POST'])
def test():
    return ("This is a test")