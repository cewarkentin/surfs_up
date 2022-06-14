# import flask dependency
from flask import Flask

# create a new flask app instance
app = Flask(__name__)

# create flask routes
@app.route('/')
def hello_world():
    return 'Hello world'