#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """ Prints hello When someone enters / """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Prints hello When someone enters / """
    return 'HBNB'


app.run(host='0.0.0.0', port="5000")