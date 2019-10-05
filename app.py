from flask import Flask
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

# @app.route('/login', methods=['GET','POST'])
# def login():
#   if request.method == 'POST':
#     #check user details from db
#     login_user()
#   elif request.method == 'GET':
#     #serve login page
#     serve_login_page()

# @app.route('/user/<name>')
# def hello(name = None):
#   #name=None ensures the code runs even when no name is provided
#   return render_template('user-profile.html', name=name)

# @app.route('/user', methods=['GET','POST'])
# def get_user():
#   username = request.form['username']
#   password = request.form['password']
#   #login(arg,arg) is a function that tries to log in and returns true or false
#   status = login(username, password)
#   return status

# @app.route('/upload', methods=['GET', 'POST'])
# def upload_file():
    # if request.method == 'POST':
    #     static_file = request.files['the_file']
    #     # here you can send this static_file to a storage service
    #     # or save it permanently to the file system
    #     static_file.save('/var/www/uploads/profilephoto.png')

@app.route('/dbconnectivity')
def connect():
  return db.db_connectivity()

@app.route('/login')
def login(username = "ali", password = "123"):
  if username == "ali" and password == "123":
    return True
  return False
