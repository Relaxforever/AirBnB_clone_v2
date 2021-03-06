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


@app.route('/python/', strict_slashes=False, defaults={'text': 'is Cool'})
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """ Prints hello When someone enters / """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """prints a number if there is one"""
    return '{} is a number'.format(n)


if __name__ == "__main__":
    app.run(debug=True)
