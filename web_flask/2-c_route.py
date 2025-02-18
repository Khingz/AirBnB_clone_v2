#!/usr/bin/python3
"""Start a flask server"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """say hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """say hello HNBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def hello_text(text):
    """say hello with text"""
    new_text = text.replace("_", " ")
    return "C " + new_text


if __name__ == '__main__':
    app.run(debug=True)
