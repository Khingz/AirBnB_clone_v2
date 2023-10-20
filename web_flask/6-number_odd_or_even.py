#!/usr/bin/python3
"""Start a flask server"""
from flask import Flask, render_template


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


@app.route("/python/", defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def hello_python(text):
    """say hello python"""
    new_text = text.replace("_", " ")
    return "Python " + new_text


@app.route("/number/<int:n>", strict_slashes=False)
def number_params(n):
    """return number params"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_params_template(n):
    """Render template if number"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_params_odd_even(n):
    """Render template if number"""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == '__main__':
    app.run(debug=True)
