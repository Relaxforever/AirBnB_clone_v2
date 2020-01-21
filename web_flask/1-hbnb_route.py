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


if __name__ == "__main__":
    app.run(debug=True)
