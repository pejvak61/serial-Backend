# terminal> set FLASK_ENV=development
# terminal> set FLASK_APP=app.py
# app.py
salt='Ali'
hash='Mohammadi'
token=''
from flask import Flask, escape, url_for,jsonify
from flask import request
from flask import render_template,make_response
from http import HTTPStatus
from flask import Response
import json
import db
import jwt
import datetime
from functools import wraps
import secrets
import myCryptography
# ///////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\
app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisisthesecretkey'

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token') # http://127.0.0.1:2281/route?token=jdjklgadjkgakdfwjfwjljaslkfj2e
        if not token:
            return jsonify({'message' : 'Token is missing!'}), 403
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'message' : 'Token is invalid!'}), 403
        return f(*args, **kwargs)
    return decorated

@app.route('/unprotected')
def unprotected():
    return jsonify({'message' : 'Anyone can view this!'})

@app.route('/protected')
@token_required
def protected():
    return jsonify({'message' : 'This is only available for people with valid tokens.'})

@app.route('/login', methods=['GET'])
def login():
    # auth = request.authorization
    if request.form:
        uid = request.form['username']
        pwd = request.form['password']
        # print(request.form['username'])
        # print(request.form['password'])
        if uid == 'ali' and pwd == 'password':
            token = jwt.encode({'user' : uid, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},app.config['SECRET_KEY'])
            return jsonify({'token' : token.decode('UTF-8')})
        else:
            return jsonify({'message' : 'Invalid username or password!'}), 401
    else:
        return make_response('Could not verify!', 401, {'WWW-Authentication' : 'Basic realm="Login Required"'})


# \\\\\\\\\\\\\\\\\\\\\\\\\\\////////////////////////

# ///////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\
@app.route('/createNewUser')
def createUser():
    uid = request.json['uid']
    pwd = request.json['pwd']
    # print("uid:",uid,"pwd:",pwd)
    # return (myCryptography.pbkdf2_hmac_sha512(pwd,salt))
    # return jsonify({'uid' : uid, 'pwd' : pwd,'token_hex(16)' : secrets.token_hex(16)})
    return make_response('Received', 200, {'uid' : uid , 'pwd' : pwd})

@app.route('/testHashAndSalt')
def testHashAndSalt():
    return (myCryptography.hashandsaltindicator())
# \\\\\\\\\\\\\\\\\\\\\\\\\\\////////////////////////


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

# @app.route('/createUser', methods=['post'])
# def createUser(request.form['username'],request.form['password']):
    
    

@app.route('/loginX', methods=['GET', 'POST'])
def loginX():
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

# ///////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\
if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=2281, debug=True)
# \\\\\\\\\\\\\\\\\\\\\\\\\\\////////////////////////