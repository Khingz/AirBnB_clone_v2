#!/usr/bin/python3
"""Fetch list of states"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """Fetch all states"""
    data = storage.all("State")
    return render_template("9-states.html", state=data)


@app.route("/states/<id>", strict_slashes=False)
def get_state(id):
    """Get a single state by id"""
    data = storage.all("State")
    for state in data.values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown_db(exception):
    """Teardown method to clean up data"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0")
