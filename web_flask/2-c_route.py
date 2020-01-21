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


@app.route('/c/<text>', strict_slashes=False)
def c_text(text=None):
    """ Prints hello When someone enters / """
    if text is not None:
        return 'C {}'.format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(debug=True)
