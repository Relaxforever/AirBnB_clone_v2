#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def finish_session(NaN):
    """ Tears down the session"""
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_all():
    """ Prints hello When someone enters / """
    return render_template('8-cities_by_states.html',
                           dict_states=storage.all("State"))


if __name__ == "__main__":
    app.run(debug=True)
