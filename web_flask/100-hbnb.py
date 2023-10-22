#!/usr/bin/python3
"""Starts a Flask web app"""
from models import storage
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays the main HBnB filters HTML page."""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    return render_template("100-hbnb.html",
                           states=states, amenities=amenities, places=places)


@app.teardown_appcontext
def teardown_db(execute):
    """Teardown current session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
