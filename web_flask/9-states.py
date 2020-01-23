#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def finish_session(NaN):
    """ Tears down the session"""
    storage.close()


@app.route('/states/<id>', strict_slashes=False)
def states_all(id):
    """ Prints hello When someone enters / """
    all_st = storage.all("State")
    new_s = None
    for key, value in all_st.items():
        if value.id == id:
            new_s = value
            break
    return render_template('9-states.html',
                           dict_states=new_s)


if __name__ == "__main__":
    app.run(debug=True)
