#!/usr/bin/python3
"""Start a flask server"""
from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello_world():
    """say hello HBNB"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(debug=True)
