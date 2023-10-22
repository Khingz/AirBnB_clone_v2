#!/usr/bin/python3
"""Fetch list of states"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def fetch_states():
    """fetch state"""
    data = storage.all("State")
    return render_template("7-states_list.html", states=data)


@app.teardown_appcontext
def teardown_db(exception):
    """Teardown method to clean up data"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0")
