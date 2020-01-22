#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def finish_session(NaN):
    """ Tears down the session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Prints hello When someone enters / """
    return render_template('7-states_list.html',
                           dict_states=storage.all("State"))


if __name__ == "__main__":
    app.run(debug=True)
