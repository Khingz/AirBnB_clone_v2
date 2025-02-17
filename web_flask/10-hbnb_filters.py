#!/usr/bin/python3
"""Starts a Flask web app"""
from models import storage
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """renders main html"""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown_db(execute):
    """tesrdown current session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
