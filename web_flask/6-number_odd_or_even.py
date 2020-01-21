#!/usr/bin/python3
from flask import Flask, render_template
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


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """display page if only is integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def even_or_odd(n):
    """check if a number is even or odd"""
    if int(n) % 2 == 0:
        return render_template('6-number_odd_or_even.html',
                               n=n, even_or_odd="even")
    else:
        return render_template('6-number_odd_or_even.html',
                               n=n, even_or_odd="odd")


if __name__ == "__main__":
    app.run(debug=True)
